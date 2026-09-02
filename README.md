# kanda

*Kanda — Swahili for tape. As in "kanda ya video."*

AI-generated found footage that feels like a memory. Prompts, music, and the post-production pipeline behind every clip — so you can make your own.

![Nairobi, 1980s](examples/001-nairobi-1980s-plot/media/preview.gif)

**▶ [Watch the 25-second clip](examples/001-nairobi-1980s-plot/media/nairobi-1980s-plot-v3-25s.mp4)** — 1980s Nairobi, shot on a "VHS camcorder" that never existed, in a plot in Jericho estate. Benga on the radio. That's [Example 001](examples/001-nairobi-1980s-plot/).

<!-- For GitHub's inline video player: open this README in the web editor, drag the mp4 into it, and replace the link above with the URL GitHub gives you. -->

## What this is

A working method for making AI video that looks like real home footage from a specific place and time — shaky, over-saturated, tape-hiss VHS, with the right cars, roofs, clothes, and music for that place. The first example is 1980s Nairobi, and it got a lot more attention than a generic "80s home video" would have. The difference was the research and the prompt, not the model.

Everything is documented: the prompt that worked, the prompt that gave a woman three hands, the music prompt, the exact edits, and the ffmpeg pipeline that makes the music duck when the kids scream. Take any place and any decade, follow the same steps.

## How a clip gets made

1. **Cultural research first, prompt second.** What did the cars, roofs, clothes, water, and shops actually look like there, then? What was on the radio? Get the nouns right.
2. **Video prompt** — one paragraph, fast cuts, handheld, period texture, *named language*, anatomy instructions for hand-heavy actions, and a precise description of the soundscape.
3. **Music prompt** — take a genre you can already describe well and map it line-for-line onto the genre that was actually playing there. Instrumental.
4. **Post** — `pipeline/align_and_mix.py` detects the cuts, beat-tracks the music, slides the song until the beats land on the cuts, then mixes it under the natural sound with sidechain ducking. Surgical shot removal is plain ffmpeg.
5. **Look at the whole thing** — a contact sheet, one frame a second — before you write the next prompt or post it.

There's a [`SKILL.md`](SKILL.md) at the root: point any agent at this repo and it will walk you through all five steps and run the pipeline for you.

## Examples

| # | Place / time | Models | Watch |
|---|---|---|---|
| [001](examples/001-nairobi-1980s-plot/) | Nairobi, Kenya · 1980s · a plot in Jericho estate, morning to lamp-light | Seedance 2.5 + Suno v5.5 | [25s](examples/001-nairobi-1980s-plot/media/nairobi-1980s-plot-v3-25s.mp4) · [55s](examples/001-nairobi-1980s-plot/media/nairobi-1980s-plot-full-story-55s.mp4) |

Each example folder has the same shape — the prompts exactly as they were run, the media, and a README with what was made and the exact edits. Add yours with [`templates/example-template.md`](templates/example-template.md).

## Stack

| | |
|---|---|
| Video generation | [Seedance 2.5](https://fal.ai/models/bytedance/seedance-2.5) via fal — text-to-video for the first clip, reference-to-video for the continuation |
| Music generation | [Suno](https://suno.com) v5.5, style prompt, instrumental |
| Post-production | [ffmpeg](https://ffmpeg.org) for cuts, mixing, sidechain ducking · [librosa](https://librosa.org) for beat tracking · Python · [`pipeline/align_and_mix.py`](pipeline/align_and_mix.py) |
| Agent | [`SKILL.md`](SKILL.md) — works with any agent that reads skills |

```bash
pip install -r pipeline/requirements.txt          # ffmpeg on your PATH
python pipeline/align_and_mix.py video.mp4 music.mp3 out.mp4
```

MIT. The prompts are yours to use.
