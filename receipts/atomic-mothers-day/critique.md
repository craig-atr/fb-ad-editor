# Second Pass — critique of atomic-mothers-day

A real run of this editor on a real `fb-ad-studio` ad ([`ad-plan.md`](ad-plan.md)).
Pre-pass output is verbatim; the critique follows this repo's `rules.md`.

This one is a useful contrast to [`atomic-lincoln-250`](../atomic-lincoln-250/critique.md): that ad was a strong *concept* with a muted-blind execution. This is a **textbook execution** — so a good editor should mostly validate it and flag only what's genuinely at risk. It does. An editor that manufactured a long problem list here would be miscalibrated.

---

## Step 1 — pre-pass (`python check.py receipts/atomic-mothers-day/ad-plan.md`)

```
WARN  [copy-limit] primary text is 195 chars, past Meta's ~125 (truncates in-feed)
WARN  [copy-limit] description is 46 chars, past Meta's ~30 (truncates in-feed)

0 error(s), 2 warning(s).
```

Zero compliance errors, and nothing on aspect, length, CTA, or proof — because the plan is 9:16, ~20s, ends on Book Now, and uses **real footage** for its proof beats. The pre-pass has nothing to invent here; only the copy runs long.

## Step 2 — the critique

**Verdict:** This is the muted-first version of an ad done right — a universally legible hook on screen at 0:00, real footage carrying the proof, text on every beat, the strongest offer type, and ad↔page match written into the plan. The remaining risks are **delivery**, not design: the proof footage is still a to-film TODO, and the copy truncates. Shoot the footage to spec and this converts.

**Load-bearing strengths — keep these (`rules.md` §5):**
- **The hook "Mom never liked that tattoo anyway."** On screen at 0:00, relatable to anyone, no lore required (the thing the Lincoln ad's hook depended on). Don't touch it.
- **The two `REAL_FOOTAGE` proof beats (03–04).** This is exactly the real trust the Lincoln ad lacked. Keep them real.
- **Three A/B hook variants.** Satisfies "test hooks, not ads" (`method.md`; `failure-modes.md` H) — a step most makers skip.

**Findings, worst-first:**

1. **The proof beats are unshot placeholders (scenes 03–04, "to film").** Standard: real footage is the money shot and sells the trust (`method.md`; `failure-modes.md` E2). The plan is *right* to specify real footage — but the ad's entire credibility rides on footage that doesn't exist yet. If those beats get skipped, faked with AI, or shot off-spec (not vertical, no genuine results), the ad collapses into a text-and-AI piece. This is a delivery dependency to lock, not a design flaw — and it's the highest-risk item here. *Hand-back: are scenes 03/04 filmed to spec (vertical 9:16, real results, ~2–3× length for trim room) before this runs?*

2. **Copy truncation (pre-pass).** Primary text is 195 chars — "Free consultation + $50 off your first package" and "Book now to reserve your spot" fall past the ~125 in-feed fold, so the *offer and the ask* are what get cut (`meta-placement-specs.md`; `failure-modes.md` F1). Description is 46/30. *Silver lining to protect:* the hook line doubles as the headline and beat-1 text, so it survives regardless — it's the offer in the primary text that doesn't. *Hand-back: what are the first ~120 characters, and is the offer inside them?*

3. **Ad↔landing match is specified but unconfirmed.** Standard: the destination repeats the hook (`failure-modes.md` G1 — and the plan's own consistency note). The plan correctly *requires* the landing page to open with "Mom never liked that tattoo anyway." A requirement in the plan isn't a confirmation on the live page. *Hand-back: does the actual landing page open with that line, or does the ad point at the generic homepage?*

4. **Tone check — beat 2, "She still doesn't."** Standard: humor stays light, never judgmental (brand voice; `method.md` → authentic/relatable). The primary hook is the safe, shareable version of the joke; "She still doesn't." nudges one step further. Probably still funny — but it's the single line where the gifting audience (women 25–55) could read a dig at Mom instead of an inside joke. *Hand-back: does beat 2 still feel playful, not judgmental, read cold?*

**Make this first:** lock the real footage for scenes 03/04 to spec (#1). Everything else here is strong, but the ad literally can't do its job without that footage. Then fix the truncation so the offer survives the fold (#2).

Back to you — targets named, nothing rewritten.

---

> **Why two receipts:** the [Lincoln](../atomic-lincoln-250/critique.md) run shows the editor pulling apart a strong-concept / muted-blind ad; this run shows it largely *endorsing* a textbook ad and flagging only real delivery risks. Same rubric, calibrated to the work in front of it — which is what separates an editor from a checklist.
