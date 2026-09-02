# Prompt 02 — the fixed version (what I run now)

Same prompt with the two fixes from 01, plus a third one I learned from Gemini Omni: if you tell a model "people speak Swahili," it makes *everyone* speak, *constantly* — narrating the tap, the clothes, everything. So the instruction is phrased as "the rare speech that occurs is Swahili," and the audio line lists what the soundscape *is* instead. Models fill silence with whatever you name. Name ambience, not dialogue.

This is the prompt every model in the benchmark ran.

```
This is messy, fast-cut 1980s home video shot on a VHS camcorder in a "plot" — a cluster of rented rooms around a shared dirt courtyard — in Nairobi's Jericho estate, Kenya. All people are Kenyan. Most people are quietly going about their day and do not speak. Occasionally — no more than once or twice in the whole video — a distant voice or a brief shout is heard in fluent Swahili, natural and unintelligible, as if overheard from across the courtyard, never directed at the camera and never commenting on what is happening. Cuts happen very frequently, around every 1.5 seconds. The camera jumps quickly between lots of different shots: different angles of the mabati (corrugated iron) roofs and doorways, people outside, the dirt courtyard, clotheslines strung between buildings, a parked Peugeot 504 or VW Kombi, jerry cans by the communal water tap, and random moments happening around the compound. Each person has exactly two hands and anatomically correct arms; actions like opening a tap or pinning clothes to a line are done simply and naturally with two hands. The editing feels spontaneous and slightly chaotic, as if the person filming keeps changing their mind about what to show. The camera is extremely shaky and handheld, with constant movement and loose framing. The footage has the distinctive texture and color of real 1980s VHS video. Audio: natural ambient sound only, as recorded by the camcorder's built-in microphone — the soundscape is mostly wind against the mic, footsteps on dirt, distant traffic, birds, the clatter of jerry cans and daily chores. Speech is rare and always distant and half-heard. No music, no soundtrack, no background score, no narration, no conversations near the camera.
```

Three changes from 01, and why each one is there:

| Change | Why |
|---|---|
| "fluent Swahili ... never commenting on what is happening" | Kills both failure modes at once: wrong language, and tour-guide narration |
| "no more than once or twice in the whole video" | An explicit frequency cap. Vague words like "occasionally" don't work |
| "exactly two hands ... done simply and naturally" | Name the hand-heavy actions specifically. The tap and the clothesline were the two failures, so both are in the sentence |
