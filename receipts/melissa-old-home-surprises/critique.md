# Second Pass — critique of old-home-surprises

A real run on a **real ad from a working real estate agent** (Melissa Bonina, Custom Homes
Realty), supplied by the agent. Profile: `real-estate`. Pre-pass output verbatim; critique
follows this repo's `rules.md`.

This is the outside-domain receipt: an ad the editor's author didn't write, in an industry
the editor wasn't originally built for, critiqued with **no spine changes** — only the
profile.

---

## Step 1 — pre-pass (`python check.py --profile real-estate receipts/melissa-old-home-surprises/ad-plan.md`)

```
[profile: real-estate]
WARN  [copy-limit] primary text is 221 chars, past Meta's ~125 (truncates in-feed)

0 error(s), 1 warning(s).
```

**Zero compliance errors** — and that's the headline result, not a formality. Fair Housing is the #1 legal risk in real estate advertising, and this copy describes the *property and the process* ("knob-and-tube wiring," "hidden water damage," "understand the hidden costs") and never the buyer it's "perfect for." A large share of agent ads trip this; this one doesn't.

## Step 2 — the critique

**Verdict:** Genuinely strong, differentiated concept — the comedy earns attention and it dramatizes a real buyer fear instead of showing another listing. Two things cap it: with no on-screen text until 0:20 and no voiceover, a muted viewer never learns *who this is* or *that there's a free consultation*; and every beat — including Melissa herself — is AI, so an ad selling *her judgment* has nothing real in it.

**Load-bearing strengths — keep these (`rules.md` §5):**
- **The Fair Housing discipline.** Confirmed clean above. If this gets rewritten, don't let "perfect for families" or "safe neighborhood" creep in — that's the one edit that could turn a good ad into a legal problem.
- **The premise.** "Dream home → comedic surprises" is a real differentiator in a category of headshots and listing slideshows, and it dramatizes an anxiety buyers actually have. That's the asset here.
- **Description (27 chars) and the "Learn More" CTA** are both right for a consult lead — correctly *not* flagged under this profile.

**Findings, worst-first:**

1. **Muted-first: no words on screen until 0:20.** Beats 1–6 are text-free with no voiceover — music and SFX only. Credit where due: the *gags* do read muted, which is more than most ads manage. But the *message* doesn't. Twenty seconds in, a muted viewer has learned "old houses have problems" and nothing about who's telling them or what to do next; anyone who drops before 0:20 never sees Melissa's name or the offer at all. Standard: on-screen text carries the message on muted playback (`meta-placement-specs.md`; `failure-modes.md` C1). *Hand-back: the gags don't need explaining — the stakes and the offer do. What 2–6 word line per beat threads "hidden costs → she finds them first" without stepping on the comedic timing?*

2. **Nothing in the ad is real — including Melissa (beats 6–7).** All seven beats are AI Clip / AI Still. In a business where the product is *her judgment and presence*, the one beat that exists to build trust — "Melissa arrives, reviewing inspection paperwork, everyone relaxes" — is a generated person. There's no real home she sold, no real client, no real her. Standard: real footage sells; AI supports; the trust shot isn't faked (`method.md`; `failure-modes.md` E2/A2). Separately: a realistic AI depiction of a **real, named person** can trigger Meta's AI-disclosure rules — verify before this runs. *Hand-back: can beats 6 and 7 be real footage of Melissa? It's the cheapest real footage in the whole ad to capture, it's the only beat that has to be believed, and it retires the disclosure question at the same time.*

3. **The offer is past the fold and only on the end card.** Primary text is 221 chars, so "Schedule your free consultation today" — the actual ask — is cut in-feed (`meta-placement-specs.md`; `failure-modes.md` F1). On screen it appears only at 0:20. Between the two, a muted scroller who doesn't expand the caption effectively never sees the offer. *Hand-back: what are the first ~120 characters, and is "free buyer consultation" inside them?*

4. **No landing destination in the plan.** "Learn More" has to go somewhere and the plan doesn't say where. Standard: the destination repeats the ad's hook (`failure-modes.md` G1). *Hand-back: where does this click to — and does that page open with "Old Homes Have Stories…" and the free consultation, or a generic homepage?*

5. **The first 3 seconds sell the dream, not the twist.** Beat 1 is three full seconds of a beautiful home at golden hour — which is what *every* real estate ad looks like, so for the length of the entire hook window there's no signal this one is different. The comedy needs its setup, so this is a real trade-off rather than a flat error (`failure-modes.md` B2). *Hand-back: can the first flicker land at 0:01–0:02, or does the gag die without the full beat? Worth shipping both and letting the platform decide.*

6. **One hook, no variants.** Standard: test hooks, not ads (`method.md`; `failure-modes.md` H1). Same offer, three openers, let Meta find the winner. *Hand-back: what are two other 3-second openers — leading on the furnace, or opening on the mug under the drip?*

*Minor:* the plan says ~22 seconds but the beat sheet runs to 0:23 — trim a beat or restate the target (~22s is the ceiling for a story piece).

**Make this first:** get Melissa on screen for real (#2). It's the cheapest real footage in the ad, it's the only beat that has to be believed, and it answers the AI-disclosure question in the same stroke. The on-screen text layer (#1 and #3) is the close second — and those two together are one afternoon of work.

Back to you — targets named, nothing rewritten.

---

> **Tool note (honest):** the original plan labels its copy "Primary Text (Short)"; the pre-pass parses canonical labels ("Primary text:"), so the labels were normalized in [`ad-plan.md`](ad-plan.md) — copy verbatim, nothing else changed. A real usability limit of `check.py` worth knowing: it reads the format the README asks for, not every format a human writes.
