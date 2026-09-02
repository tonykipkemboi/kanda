# Prompt 03 — the continuation (Seedance 2.5, reference-to-video, 30s)

The second generation. This extends the first video from afternoon into evening, and it's the one that convinced me the story format works: three acts, callbacks to characters from the first clip, a lighting change, and a paraffin lamp at the end — all from one 30-second generation, first try.

## Setup (this part matters more than the prompt)

fal's reference-to-video mode has a **likeness filter** — it refused my own AI-generated clip because it saw faces, and it can't tell generated faces from real ones. So the reference video it actually received was a **face-free cut** of the original: the roof, the Peugeot grille, the tap with jerry cans. ~10 seconds, no people. Plus two face-free still frames (roof with smoke, the grille) in the image slots.

The characters therefore live in the *text*, described by clothing. Faces came out different from the first clip — wardrobe matched, which is what sells continuity in fast-cut footage anyway.

Cost note: with a video reference, 720p ran about $0.28/s on fal at the time, so ~$8.50 per 30s attempt.

## The prompt

```
This video continues directly from the reference video: the same messy, fast-cut 1980s home video shot on a VHS camcorder in the same Kenyan "plot" compound in Nairobi's Jericho estate — the same dirt courtyard, the same blue plastic water tank and communal tap with yellow jerry cans, the same clotheslines of bright kitenge fabric strung between mabati-roofed rooms with peeling plaster walls, and the same single dark navy-blue Peugeot 504 sedan parked in the courtyard. The same people: the man in a light shirt and tan trousers who leans against the Peugeot; the woman in the green, yellow and red kitenge wrap who was filling jerry cans at the tap; the young woman with braids and a cream top who was hanging a pink kitenge cloth on the line; the woman in a blue top leaning out of a green-framed window; and the group of children in colorful clothes who were running across the courtyard. Same bright afternoon sunlight, same shaky handheld camera, same VHS texture and color, cuts every 1.5 seconds. All people are Kenyan. Most people do not speak; at most once or twice a distant voice or brief shout in fluent Swahili is half-heard from across the compound, never directed at the camera. Every person has exactly two hands with correct anatomy.

The person filming now walks out of the courtyard through the compound gate into the estate lane. The camera jumps between: a group of boys playing football with a ball made of tied plastic bags on a dusty stretch of lane; a woman selling tomatoes, onions and sukuma wiki from a wooden stall; a man fixing a bicycle upside-down on its saddle; a battered matatu minibus grinding past in a cloud of dust; children chasing it; rusted mabati roofs against the sky; a goat tied to a post; a radio on a windowsill.

As the light turns golden and then orange, the camera returns into the courtyard. Charcoal smoke rises from small jikos as women cook outside their doors. The man in the light shirt who leaned against the Peugeot sits on a low stool, glances up at the lens again, and gives a small nod before looking away. The woman in the blue top is still at her green-framed window. Mothers call the children in from the lane. The last shots: the sky going deep orange over the roofs, a paraffin lamp being lit in a doorway, the courtyard now dim and quiet, laundry still hanging, the Peugeot in shadow, and the camera drifting down and shutting off.

Natural ambient sound only, as recorded by the camcorder's built-in microphone: football thumps, a matatu engine, distant traffic, a radio playing faintly, crackling charcoal, evening insects. No music, no soundtrack, no narration, no dialogue near the camera.
```

## Why the anchors are written like that

The first paragraph names concrete nouns — *navy-blue Peugeot 504*, *blue plastic water tank*, five people by their clothes — instead of saying "same as before." Models respond to nouns, not pronouns. I originally wrote "a white car" in there from a quick look at one frame. It was a navy Peugeot. A contact sheet of the whole clip fixed that before it went in; if the anchor is wrong, the model decides the reference doesn't match and drifts on the whole scene.

## What came back
Everything I asked for, in order. Two fixes in post: the plastic-bag ball looked like a frisbee for about a second (trimmed), and a rooster crowed at dusk (roosters do that in real life, but on a soundtrack a crow means morning — low-passed it out).
