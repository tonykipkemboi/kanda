# kanda

*Kanda — Swahili for tape. As in "kanda ya video."*

AI-generated found footage that feels like a memory. Prompts, music, and the post-production pipeline behind every clip — so you can make your own.

![Nairobi, 1980s](examples/001-nairobi-1980s-plot/media/preview.gif)

**▶ [Watch the 25-second clip](examples/001-nairobi-1980s-plot/media/nairobi-1980s-plot-v3-25s.mp4)** — 1980s Nairobi, shot on a "VHS camcorder" that never existed, in a plot in Jericho estate. Benga on the radio. That's [Example 001](examples/001-nairobi-1980s-plot/).

<!-- To get GitHub's inline video player, open this README in the web editor and drag the mp4 into it — GitHub will host it and render a player. Then replace the link above with that URL. -->

## What this is

I grew up around this kind of footage — the shaky, over-saturated, tape-hiss home video that somebody's uncle shot at a family thing and nobody watched again for twenty years. The AI video models got good enough to fake it, and when I pointed one at a Kenyan estate in the 80s instead of the usual American suburb, something clicked for people. So I'm documenting how it's done, all of it: the prompt that worked, the prompt that gave a woman three hands, the music prompt, and the ffmpeg pipeline that makes the music duck when the kids scream.

The goal is that you can take any place and any decade, follow the same steps, and get something that makes someone from there stop scrolling.

## How a clip gets made

1. **Cultural research first, prompt second.** What did the cars, roofs, clothes, water, and shops actually look like there, then? What was on the radio? Get the nouns right.
2. **Video prompt** — one paragraph, fast cuts, handheld, period texture, *named language*, anatomy instructions for hand-heavy actions, and a precise description of the soundscape. Seedance 2.5 has been the strongest for this; the benchmark below tracks the others.
3. **Music prompt** — take a genre you can already describe well and map it line-for-line onto the genre that was actually playing there. Suno v5.5. Instrumental.
4. **Post** — `pipeline/align_and_mix.py`: detects the cuts, beat-tracks the music, slides the song until the beats land on the cuts, then mixes it under the natural sound with sidechain ducking. Surgical shot removal is plain ffmpeg.
5. **Look at the whole thing** — a contact sheet, one frame a second — before you write the next prompt or post it. That's where the three hands and the wrong-colour car get caught.

## Examples

| # | Place / time | Models | Watch |
|---|---|---|---|
| [001](examples/001-nairobi-1980s-plot/) | Nairobi, Kenya · 1980s · a plot in Jericho estate, morning to lamp-light | Seedance 2.5 + Suno v5.5 | [25s](examples/001-nairobi-1980s-plot/media/nairobi-1980s-plot-v3-25s.mp4) · [55s](examples/001-nairobi-1980s-plot/media/nairobi-1980s-plot-full-story-55s.mp4) |

Each example folder has the same shape — prompts as they were actually run, the media, and a README with what was made, the exact edits, and what I learned. Add yours with [`templates/example-template.md`](templates/example-template.md).

## Lessons so far

The long versions live in each example. The short versions:

- **Translate the culture, not the words.** A trailer park has no Kenyan equivalent. A *plot* is the same social structure. Swap the structure.
- **Name the language and the region.** Or you get a generic "African" that's wrong everywhere.
- **Describe the soundscape, not the dialogue.** Tell a model people speak Swahili and everyone narrates their chores. Tell it what the wind and the jerry cans sound like and speech becomes rare, like real life.
- **Hands get their own sentence.** "Exactly two hands, done simply and naturally."
- **Cut, don't fix.** An extra limb is unfixable and it's the first thing people screenshot. Fast-cut footage forgives a missing shot completely.
- **Move the music, not the picture.** Slide the song under the cuts. Under ~100 ms and it reads as intentional.
- **Ducking is the difference between a slideshow and a film.**
- **The best moments are accidents.** When a model does something great, write it down and ask for it by name next time.

## Benchmark

I've been running the same prompt through the leading video models and keeping honest score — including the caveats (which model got the debugged prompt, sample sizes, what I can and can't judge from stills). It's in [`docs/benchmark.md`](docs/benchmark.md). Short version so far: Seedance owns the aesthetic and the accidental magic; Gemini Omni is the most obedient; Grok Imagine does the most convincing tape texture; MiniMax is the value play with a film-not-video look. It's early and n is small. Read the caveats.

## Running the pipeline

```bash
cd pipeline
pip install -r requirements.txt     # ffmpeg needs to be on your PATH
python align_and_mix.py your_video.mp4 your_music.mp3 out.mp4
```

More in [`pipeline/README.md`](pipeline/README.md).

## Where this is going

More places, more decades. A Christmas trip ushago in '92. Maziwa ya Nyayo at a primary school in '88. The Likoni ferry. Not-nostalgic stuff too — silent 30-second comedy spots in the same spirit. If you make one with these prompts, open a PR and add it to the table.

Everything here is MIT. The prompts are yours to use. If you post something made from them, a mention is nice but not required.

— Tony
