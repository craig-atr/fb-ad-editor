# Compliance Red-Lines — the non-negotiables

Aesthetic/medical advertising has hard limits. A violation here is always the **first** finding — it risks the ad account and legal exposure, not just performance. These are the patterns the `check.py` pre-pass flags mechanically; this file is the source of truth and the reasoning.

The editor flags these; it does not "fix" them — the maker rewrites the claim.

## 1. No guaranteed outcomes

Laser results vary by ink, skin, and immune response. Never promise the outcome. Flag any of:

- **guarantee / guaranteed**, "results guaranteed"
- **permanent / permanently**, "gone forever," "gone for good"
- **completely / fully / 100%** removed / erased / gone
- **erase / erases** (as a promise), "removes all the ink"
- **painless / pain-free / no pain**
- **no risk / risk-free / zero risk / no side effects**
- "works on **any** skin type / **everyone** / **all** tattoos" (safety + efficacy overreach)

**Target (hand back, don't write it for them):** capability + honesty — "can help fade," "most clients see significant fading over a series," "results vary." Set realistic expectations instead of promising.

## 2. Proof must be real

- Before/after images and treatment footage must be **actual outcomes** from real clients (with permission).
- **Never** AI-generate fake before/after or fake clinical results, and never present stock as a real client. This is the trust of the whole ad; faking it is deceptive and violates platform policy.
- If the plan's only "proof" beat is `AI_CLIP` / `AI_IMAGE`, the ad has **no real proof** — flag it.

## 3. No medical overreach

- No diagnosing a viewer's skin or tattoo from an ad.
- No claims of medical safety/approval that aren't true. "FDA-cleared/approved" language must be **verified true for the specific device** before it runs — flag it for the maker to confirm, don't assume.
- Keep to non-diagnostic, consultation-first framing ("a free consultation to see if you're a candidate").

## 4. Honesty of the ad↔offer↔destination chain

- The offer stated in the ad must be real and available, and the landing page must honor it. A bait offer that the destination doesn't back is both a conversion killer and a trust/compliance problem.

---

**Note for the pre-pass:** `check.py` scans the ad plan's text for the phrases in §1 and for a proof beat that's only AI. It cannot judge whether a before/after is genuinely real or whether an "FDA-cleared" claim is true — those stay human-verified findings. Code catches the wording; the editor catches the meaning.
