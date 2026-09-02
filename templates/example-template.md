# NNN — Place, decade. One-line setting.

<!-- Copy this folder structure:
examples/NNN-short-slug/
  README.md          (this file)
  prompts/
    01-<model>-original.md
    02-<model>-fixed.md        (if there was a second pass)
    03-suno-<genre>.md
  media/
    <slug>-<length>s.mp4
    preview.gif                (~6s, 480px wide, 12fps — see pipeline/README for the ffmpeg line)
    poster.jpg
-->

![preview](media/preview.gif)

**Watch:** [the clip](media/your-clip.mp4)

| | |
|---|---|
| Video model | |
| Music | |
| Post | `pipeline/align_and_mix.py` |
| Format | |
| Prompts | [01](prompts/01-...md) · [02](prompts/02-...md) |

## The story
What is this a home video *of*? Who's holding the camera and why? Two or three sentences. If the story emerged from what the model gave you, say so.

## Cultural research
The nouns that make it real: cars, roofs, clothes, shops, what's on the radio. Where you got them.

## What was made, in order
Generation → edit → music → mix. Include exact ffmpeg commands for any surgery.

## What went wrong
Be specific. Timestamps. What you cut, what you left in and why.

## Lessons
Only the ones you actually learned on this one. Bold the takeaway, one or two sentences each.
