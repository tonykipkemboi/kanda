# Pipeline

One script does the whole post-production step: `align_and_mix.py`.

```bash
pip install -r requirements.txt   # plus ffmpeg on your PATH
python align_and_mix.py video.mp4 music.mp3 out.mp4
```

It prints what it found (cuts, BPM, chosen offset, alignment quality) and refuses to hand you a silent file.

## What it actually does

**Beat alignment.** Scene-detects the hard cuts in the video, beat-tracks the music, then slides the music across the video 10 ms at a time and picks the offset where the cuts land closest to beats. Under ~100 ms mean distance reads as "on beat" to the eye. The video is never re-cut — we move the music, not the picture.

**Ducking.** The music sits under the video's natural sound, and a compressor keyed off the *voice band* (250 Hz+) of the natural track pulls the music down 6–8 dB whenever someone talks or a kid screams, then lets it swell back over ~0.9 s. That slow release is what makes it feel like a human riding a fader rather than a machine switching levels.

**Key calibration.** Different models generate soundtracks at very different loudness (Grok's came out ~9 dB hotter than Seedance's). The script measures the source and adjusts the ducking key so the compressor triggers on loud moments, not on the whole track. Without this, a hot soundtrack keeps the music pinned and you'll swear the music isn't there.

**Tape EQ.** Music gets a gentle 50 Hz–11 kHz rolloff so it sounds like it's coming off the same worn tape as the footage, not a clean digital overlay.

## Knobs worth knowing

| Flag | Default | When to touch it |
|---|---|---|
| `--music-level` | 0.85 | Music too loud/quiet between ducks |
| `--natural-level` | 0.7 | Want more/less of the street in the mix |
| `--ratio` | 10 | Music should drop further under voices → raise |
| `--release` | 900 | Music "breathes" too obviously coming back → raise |
| `--offset` | auto | Force a specific slice of the song |
| `--scene-threshold` | 0.12 | Missing subtle cuts → lower; false cuts → raise |

## Things this doesn't do (yet)

- Multi-track cues (silence → tension → resolution). For the ad format I cut tracks manually.
- Surgical shot removal. That's plain ffmpeg trim/concat — see the example READMEs for the exact commands.

## Preview GIF recipe

```bash
ffmpeg -ss 17 -t 6 -i clip.mp4 -vf "fps=12,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4" preview.gif
```

## Contact sheet (look before you prompt again)

```bash
ffmpeg -i clip.mp4 -vf "fps=1,scale=320:-1,tile=5x6" -frames:v 1 contact.jpg
```
