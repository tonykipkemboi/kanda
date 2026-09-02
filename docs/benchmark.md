# Benchmark — same prompt, different models

The rules I set for myself: score only what can be verified (frames, cut timing, measured adherence). Motion quality and audio are judged by ear and recorded as opinion. Every score carries its sample size. "Unknown" is a valid score. And the caveats go at the top, not the bottom.

The single biggest caveat: Seedance ran on the *original* prompt — before the language and anatomy fixes existed — because Seedance's failures are what produced those fixes. Every other model got the debugged prompt. Until Seedance re-runs on the fixed prompt, its language and anatomy scores aren't comparable.

---


**Test concept:** Same creative brief (fast-cut 1980s VHS home video, Nairobi estate "plot"), same music overlay (Suno benga track), identical post pipeline (scene detection → beat alignment → sidechain-ducked mix).

**Scorekeeping rules:** Scores cover only what can be verified (frames, cut timing, measurable adherence). Audio and motion quality are judged by ear/eye and recorded as opinion. Every score notes its evidence and sample size. "Unknown" is a valid score.

---

## ⚠️ Methodology caveats (unresolved)

1. **Prompt mismatch:** Seedance ran on prompt v1 (no language spec, no anatomy instructions). Omni ran on prompt v3 (Swahili + sparse-speech + anatomy). Language and anatomy scores are NOT comparable until Seedance re-runs on v3.
2. **Length mismatch:** Seedance = 30s single generation; Omni = 10s base, extension untested.
3. **Sample size:** n=1 generation per model (Omni: 1×360p draft + 1×720p, same prompt).

---

## Scores to date (Sep 1, 2026)

### Seedance 2.5 (via fal) — prompt v1, 30s, 720p, n=1

| Dimension | Score | Evidence |
|---|---|---|
| Cut cadence adherence | Partial | Asked ~1.5s; delivered ~2.5s avg (11 cuts/30s) — measured |
| Named props | Good | Peugeot 504-era car, jerry cans, tap, clotheslines present — frames |
| Anatomy | 1 major, 1 minor | Three hands at tap (4.2s shot removed); mirrored clothes on line — frames + Tony |
| Language authenticity | Fail* | West African-sounding, not Swahili — Tony's ear. *Prompt v1 gave no language spec — retest needed |
| Human moments | Standout | Man glancing at camera — Tony rated "sublime" |
| VHS texture | Good | Convincing in frames; motion judgment = Tony's |
| Cleanup cost | 2 interventions | 1 shot excision + re-encode; 1 realignment pass |
| Temporal consistency (30s single gen) | Untested as score | No drift complaints noted |

### Gemini Omni 1.1 Flash (Gemini app, 3.7 Flash orchestrating) — prompt v3, 10s base, 720p, n=1

| Dimension | Score | Evidence |
|---|---|---|
| Cut cadence adherence | Good | ~1.1s avg (9 cuts/10s) vs ~1.5s asked — measured |
| Named props | Good | Peugeot 504 w/ Kenyan-style plate, jerry cans, clotheslines — frames |
| Anatomy | Clean so far | No extra limbs found in sampled frames; clothesline shot correct |
| Language authenticity | Good, w/ caveat | Fluent Swahili (Tony's ear) — but v2 prompt caused constant narration; fixed by v3 sparse-speech prompt |
| Human moments | Unscored | Tony hasn't flagged a standout |
| VHS texture | Good | Convincing in frames incl. plate-level detail; motion judgment = Tony's |
| Cleanup cost | 0 interventions | Base clip needed no visual fixes |
| Temporal consistency (extension joins) | **UNTESTED** | The headline question — pending extension to ~30s |

### MiniMax H3 Max — fal slug: minimax/h3-max/text-to-video — prompt v3 **with fal prompt expansion "balanced"**, 15s, 768p (1344×768), n=1

| Dimension | Score | Evidence |
|---|---|---|
| Cut cadence adherence | Best of three | ~1.5s intervals, near-metronomic (10 cuts/15s) — measured. Caveat: regularity may read as mechanical vs. organic; Tony to judge in motion |
| Named props | Good, w/ flaws | VW Kombi T2 w/ era-accurate peeling paint; jerry-can queue at tap (authentic Kenyan detail); BUT plate is garbled pseudo-text — frames |
| Anatomy | Clean in sampled frames | Clothesline shot (screenshot) two hands; no extra limbs found — limited sampling |
| Language authenticity | Unscored | Tony hasn't reported; audio track present (−31dB RMS ambience) |
| VHS texture | **Weakest of three** | Frames notably sharp, clean, saturated — reads as modern footage w/ vintage border, not VHS — frames |
| Cleanup cost | 0 so far | No visual interventions yet |
| ⚠️ Methodology | Prompt expansion ON | fal rewrote the prompt ("balanced" mode) — not the exact v3 text. Retest with expansion off for fair adherence scoring |

**Run 2 (expansion OFF, custom/empty) — 15s, 768p, n=2 total:**
- Cut cadence: still metronomic (~1.6s, 9 cuts) → **finding: the regular cadence is the model's behavior, not the expansion's**
- Texture: improved — muted, softer than run 1; still reads more "vintage cine-film" than true VHS smear (frames)
- Human moment: kid in doorway, direct gaze at camera — strongest MiniMax moment yet; Tony rates run 2 "much better" overall
- Anatomy: clean in sampled frames
- Alignment: offset 1.96s, 85 ms mean cut→beat

### Pipeline metrics (identical post-processing)

| Metric | Seedance | Omni | MiniMax H3 Max |
|---|---|---|---|
| Beat alignment (mean cut→beat) | 79–86 ms | 54 ms | 75 ms |
| Music offset used | 60.22s → 11.03s (v3) | 10.40s | 11.32s |
| Native audio | Yes | Yes | Yes |
| Cost note | — | $0.10/s @720p | $0.02/s @768p promo (reverts to $0.08/s Sep 7) |

---

### Grok Imagine Video 1.5 (SpaceXAI — xAI post-SpaceX acquisition/rebrand, 2026) — prompt v3, 15s, 720p, n=1

| Dimension | Score | Evidence |
|---|---|---|
| Cut cadence adherence | Partial | ~2.5s avg (6 cuts/15s) vs ~1.5s asked — same laxity as Seedance — measured |
| VHS texture | **Best of four** | Soft smear, muted color, tracking-noise band at frame bottom — the only model producing genuine tape artifacts — frames |
| Human moments | Strong | Woman taking clothespin from her mouth while hanging laundry — accurately observed real-world behavior — frames |
| Anatomy | Clean in sampled frames | Two hands, plausible grips — limited sampling |
| Language authenticity | Unscored | Tony to report |
| Native audio | Yes, hot | −22.5dB RMS (vs −31 others); natural bed pulled to 0.5 in mix to compensate |
| Cleanup cost | 0 so far | No visual interventions |
| Alignment | 53 ms mean (offset 7.03s) | Tied w/ Omni for tightest |

---

## Pending tests (in order)

1. **Seedance re-run on prompt v3** — required before language/anatomy comparison is valid
2. **Omni extension to ~30s** — the temporal-consistency headline test (joins across 3 generations)
3. **n≥3 per model** — before any public "X beats Y" claim
4. Cost per postable second, including rerolls — track once all reach postable length
5. Four-way side-by-side once all models have ≥15s on prompt v3

## Format notes
- Omni also produced a 360p draft (prompt v2) — confirmed draft tier is usable for iteration; over-talkative audio caught at 1/3 cost
- Suno track: 129.2 BPM detected (128 prompted) — prompt adherence point for Suno, incidentally

---

## Update — Sep 2, 2026: Seedance continuation test

- **Seedance 2.5 reference-to-video** followed a three-act, 30-second continuation prompt (courtyard → lane → dusk, with a lighting change and two character callbacks) in **one generation, first try**. Pre-run estimate was ~40% for the full story; it delivered all of it. Two post fixes: a plastic-bag ball rendered as a flat disc for ~1s (trimmed), a rooster crow at dusk (low-passed).
- **Workflow finding:** fal's reference mode runs a likeness filter that rejects AI-generated faces as if they were real. Chaining your own footage requires a face-free reference cut. Gemini Omni's chat-based extension had no such wall.
- Full 55s cut: 29 cuts, 97 ms mean cut-to-beat alignment.
