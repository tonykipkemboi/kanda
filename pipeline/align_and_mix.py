#!/usr/bin/env python3
"""
align_and_mix.py — beat-align a music track to a video's cuts, then mix it under
the video's natural sound with film-style sidechain ducking.

This is the whole post-production step for every example in this repo.

    python align_and_mix.py video.mp4 music.mp3 out.mp4

What it does:
  1. Detects hard cuts in the video (ffmpeg scene detection)
  2. Beat-tracks the music (librosa)
  3. Slides the music across the video and picks the offset where the cuts
     land closest to beats (mean cut-to-beat distance, squared)
  4. Mixes: music sits under the natural sound, and a compressor keyed off the
     voice band of the natural track ducks the music whenever people talk or
     shout, then lets it swell back — like a mixer riding a fader
  5. Verifies the output actually has audio (learned that one the hard way)

Requires: ffmpeg + ffprobe on PATH, `pip install librosa numpy`
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np


def sh(cmd, capture=True):
    r = subprocess.run(cmd, capture_output=capture, text=True)
    if r.returncode != 0:
        sys.exit(f"command failed: {' '.join(cmd)}\n{r.stderr}")
    return r


def probe_duration(path):
    r = sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)])
    return float(json.loads(r.stdout)["format"]["duration"])


def probe_rms_db(path):
    """Mean RMS of the video's own audio, in dBFS. Used to calibrate the ducking key."""
    r = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", str(path), "-map", "0:a", "-af", "astats=metadata=0", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    m = re.findall(r"RMS level dB:\s*(-?[\d.]+|-inf)", r.stderr)
    vals = [float(x) for x in m if x != "-inf"]
    return float(np.mean(vals)) if vals else -31.0


def detect_cuts(video, threshold=0.12, merge_window=0.2):
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tf:
        meta = tf.name
    sh(["ffmpeg", "-v", "error", "-i", str(video),
        "-vf", f"select='gt(scene,{threshold})',metadata=print:file={meta}",
        "-fps_mode", "vfr", "-f", "null", "-"])
    raw = [float(x) for x in re.findall(r"pts_time:([\d.]+)", Path(meta).read_text())]
    cuts = []
    for t in raw:  # collapse near-duplicate detections
        if not cuts or t - cuts[-1] > merge_window:
            cuts.append(t)
    return np.array(cuts)


def best_offset(music, cuts, video_len, step=0.01, min_beats=8):
    import librosa
    y, sr = librosa.load(str(music), sr=22050)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr, units="time")
    beats = np.asarray(beats)
    track_len = len(y) / sr
    if track_len < video_len:
        sys.exit(f"music ({track_len:.1f}s) is shorter than video ({video_len:.1f}s)")
    best = None
    for off in np.arange(0, track_len - video_len, step):
        b = beats[(beats >= off) & (beats <= off + video_len)] - off
        if len(b) < min_beats:
            continue
        d = np.array([np.min(np.abs(b - c)) for c in cuts])
        score = float(np.mean(d ** 2))
        if best is None or score < best["score"]:
            best = {"offset": float(off), "score": score, "mean_ms": float(np.mean(d) * 1000)}
    best["tempo"] = float(np.atleast_1d(tempo)[0])
    return best


def mix(video, music, out, offset, video_len, *, music_level, natural_level,
        key_gain_db, threshold, ratio, attack, release, fade_in, fade_out):
    fo_start = max(0.0, video_len - fade_out)
    fc = (
        # music: slice, tape-ish EQ, fades, level
        f"[1:a]atrim={offset:.3f}:{offset + video_len:.3f},asetpts=PTS-STARTPTS,"
        f"highpass=f=50,lowpass=f=11000,"
        f"afade=t=in:st=0:d={fade_in},afade=t=out:st={fo_start:.3f}:d={fade_out},"
        f"volume={music_level}[music];"
        # natural sound split: one copy to mix, one copy as the ducking key
        f"[0:a]asplit=2[natsrc][keysrc];"
        # key = voice band only, boosted so the threshold means something
        f"[keysrc]highpass=f=250,volume={key_gain_db}dB[key];"
        f"[music][key]sidechaincompress=threshold={threshold}:ratio={ratio}:"
        f"attack={attack}:release={release}:makeup=1[mduck];"
        f"[natsrc]volume={natural_level}[nat];"
        f"[mduck][nat]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[aout]"
    )
    sh(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(music),
        "-filter_complex", fc, "-map", "0:v", "-map", "[aout]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", str(out)])


def verify(out):
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", str(out), "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True)
    mean = re.search(r"mean_volume:\s*(-?[\d.]+)", r.stderr)
    dur = probe_duration(out)
    if not mean or float(mean.group(1)) < -60:
        sys.exit("output audio is silent — mix failed")
    return float(mean.group(1)), dur


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video")
    p.add_argument("music")
    p.add_argument("out")
    p.add_argument("--music-level", type=float, default=0.85)
    p.add_argument("--natural-level", type=float, default=0.7)
    p.add_argument("--threshold", type=float, default=0.09, help="sidechain threshold (linear)")
    p.add_argument("--ratio", type=float, default=10)
    p.add_argument("--attack", type=float, default=90, help="ms")
    p.add_argument("--release", type=float, default=900, help="ms — long = swells back musically")
    p.add_argument("--fade-in", type=float, default=0.4)
    p.add_argument("--fade-out", type=float, default=1.2)
    p.add_argument("--scene-threshold", type=float, default=0.12)
    p.add_argument("--offset", type=float, default=None, help="skip alignment, force this music offset (s)")
    p.add_argument("--reference-rms", type=float, default=-31.0,
                   help="dBFS the ducking defaults were tuned for; louder sources get their key gain reduced automatically")
    a = p.parse_args()

    video, music, out = Path(a.video), Path(a.music), Path(a.out)
    vlen = probe_duration(video)

    cuts = detect_cuts(video, a.scene_threshold)
    print(f"video {vlen:.2f}s · {len(cuts)} cuts at {np.round(cuts, 2).tolist()}")

    if a.offset is None:
        res = best_offset(music, cuts, vlen)
        print(f"music {res['tempo']:.1f} BPM · best offset {res['offset']:.2f}s · mean cut→beat {res['mean_ms']:.0f} ms")
        offset = res["offset"]
    else:
        offset = a.offset
        print(f"forced offset {offset:.2f}s")

    # Calibrate the ducking key to the source's loudness. A soundtrack 9 dB hotter than
    # the reference would otherwise keep the compressor pinned and bury the music.
    src_rms = probe_rms_db(video)
    key_gain = 14.0 - (src_rms - a.reference_rms)
    print(f"natural audio {src_rms:.1f} dBFS · key gain {key_gain:.1f} dB")

    mix(video, music, out, offset, vlen,
        music_level=a.music_level, natural_level=a.natural_level, key_gain_db=key_gain,
        threshold=a.threshold, ratio=a.ratio, attack=a.attack, release=a.release,
        fade_in=a.fade_in, fade_out=a.fade_out)

    mean_db, dur = verify(out)
    print(f"wrote {out} · {dur:.2f}s · mean {mean_db:.1f} dB ✓")


if __name__ == "__main__":
    main()
