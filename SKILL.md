---
name: kanda
description: Make an AI-generated "found footage" clip end to end using this repo — save the video prompt and music prompt into a new example folder, walk the user through generating the video (Seedance 2.5 on fal, or another model) and the music (Suno), then run pipeline/align_and_mix.py to beat-align the music to the cuts and mix it under the natural sound with ducking. Use this skill whenever someone in this repo wants to make a new clip, add an example, combine a video with a music track, fix a bad shot, or asks how the pipeline works — even if they don't say "kanda" or "skill."
---

# kanda — make a clip

You are helping someone produce one clip: a video prompt → a generated video, a music prompt → a generated track, then the pipeline mixes them. Two of the three steps are manual (the user generates video and music in a browser); your job is to prepare everything, tell them exactly what to do, and run the combine step the moment the files land.

## 0. Check the environment once

```bash
ffmpeg -version | head -1 && python3 -c "import librosa, numpy; print('ok')"
```

If that fails: `pip install -r pipeline/requirements.txt`, and ffmpeg from the OS package manager.

## 1. Create the example folder

Pick the next number and a short slug. Copy the template:

```
examples/NNN-place-decade/
  README.md        ← copy templates/example-template.md, fill in as you go
  prompts/
  media/
```

## 2. Save the prompts as files

The user will give you (or ask you to write) a video prompt and a music prompt. Save them **verbatim** — the whole point of this repo is that prompts are recorded exactly as run:

- `prompts/01-<model>-video.md` — one heading, then the prompt in a fenced code block
- `prompts/02-suno-<genre>.md` — same shape

If you're writing the video prompt, follow `examples/001-nairobi-1980s-plot/prompts/02-seedance-v3-recommended.md` as the pattern: fast cuts every ~1.5s, handheld, period texture, **named language and region**, "exactly two hands" for any hand-heavy action, and a described soundscape ("no music, no narration" is required — the pipeline adds the music).

If you're writing the music prompt, follow `.../prompts/04-suno-benga.md`: instrumental, named genre, named era, tape/production texture, a BPM, a key, and the sentence "pure instrumental no vocals no singing." The track must be **longer than the video** — the pipeline slides it to find the best-aligned slice, so ask Suno for a full-length song.

## 3. Tell the user how to generate — exactly this

**Video (Seedance 2.5 on fal):** go to `fal.ai/models/bytedance/seedance-2.5/text-to-video`, paste the video prompt, 16:9, 720p, 30s, run. Download the mp4 into `examples/NNN-.../media/`. (Any model works — the pipeline only needs an mp4 with its own audio track.)

**Music (Suno):** go to `suno.com`, Create → Custom, switch to instrumental, paste the music prompt into the *Style* field, leave lyrics empty, generate. Download the mp3 into the same `media/` folder.

Then say: "Drop both files in `media/` and tell me when they're there."

## 4. Combine

```bash
python3 pipeline/align_and_mix.py media/<video>.mp4 media/<music>.mp3 media/<slug>-final.mp4
```

Read what it prints back to the user in plain language: how many cuts, the song's BPM, where in the song it started, and the alignment number (under ~100 ms mean = on beat). It exits with an error if the output is silent — never hand over a file it refused.

If the user says the music is too loud, too quiet, or not ducking enough under voices, rerun with `--music-level`, `--natural-level`, or `--ratio` (see `pipeline/README.md`). Don't guess — change one knob, rerender, ask.

## 5. If a shot is bad (extra hands, a broken object)

Find it, then cut the whole shot — don't try to fix it. Get the cut times from the contact sheet and the scene list:

```bash
ffmpeg -i media/<video>.mp4 -vf "fps=1,scale=320:-1,tile=5x6" -frames:v 1 media/contact.jpg
ffmpeg -i media/<video>.mp4 -vf "select='gt(scene,0.12)',metadata=print" -fps_mode vfr -f null - 2>&1 | grep pts_time
```

Remove the segment between two cuts (example removes 7.708s–11.875s):

```bash
ffmpeg -i media/<video>.mp4 -filter_complex \
"[0:v]trim=0:7.708,setpts=PTS-STARTPTS[v1];[0:v]trim=11.875,setpts=PTS-STARTPTS[v2];[v1][v2]concat=n=2:v=1:a=0[v];\
 [0:a]atrim=0:7.708,asetpts=PTS-STARTPTS[a1];[0:a]atrim=11.875,asetpts=PTS-STARTPTS[a2];[a1][a2]concat=n=2:v=0:a=1[a]" \
-map "[v]" -map "[a]" -c:v libx264 -crf 17 -preset slow -c:a aac media/<video>-cut.mp4
```

Then run step 4 again on the cut version — the alignment has to be recomputed because the cuts moved.

## 6. Finish the example

- Preview GIF: `ffmpeg -ss <good 6s start> -t 6 -i media/<final>.mp4 -vf "fps=12,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4" media/preview.gif`
- Fill the example README: model, format, what was made in order, any shot you cut and why.
- Add a row to the Examples table in the root README.

## Rules

- Never rewrite a prompt the user asked you to save. Save it as given; suggest changes separately.
- Never claim to have generated video or music — you can't. The user does that in a browser.
- Never present a mix you didn't run through `align_and_mix.py` (it verifies the audio exists).
- Keep the story out of it unless the user wants one. The README needs what was made, not why it matters.
