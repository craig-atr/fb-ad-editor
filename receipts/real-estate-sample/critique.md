# Second Pass — critique of real-estate-sample

A run of the editor on a **constructed** realtor ad ([`ad-plan.md`](ad-plan.md)) with the
`real-estate` profile active. Its purpose is to prove the domain layer swaps: **no spine
file changed** — same critique method, same Meta specs — only the profile did, and the
compliance regime is now Fair Housing instead of medical claims.

> This ad is constructed (the `atomic-*` receipts are real). Drop in a real agent's ad the
> same way: `python check.py --profile real-estate <plan>`, then critique.

---

## Step 1 — pre-pass (`python check.py --profile real-estate receipts/real-estate-sample/ad-plan.md`)

```
[profile: real-estate]
ERROR  [compliance] "perfect for families" - Fair Housing - familial-status steering
ERROR  [compliance] "family-friendly" - Fair Housing - familial-status steering
ERROR  [compliance] "guaranteed price" - unverifiable guaranteed-sale/price claim
WARN  [copy-limit] primary text is 221 chars, past Meta's ~125 (truncates in-feed)

3 error(s), 1 warning(s).
```

Two things to notice. The CTA "Learn More" was **not** flagged — the `real-estate` profile accepts it for a lead objective, where the `tattoo-removal` profile would have (wrongly) demanded "Book Now." That's the swap working. And the pre-pass caught the direct phrases but **missed "safe, family-friendly neighborhood"** — the literal regex wants "safe" next to "neighborhood," and the comma splits them. The editor catches it below by meaning. *Code catches the wording; the editor catches the meaning.*

## Step 2 — the critique

**Verdict:** This can't run as written — the copy carries Fair Housing violations that are a legal landmine, and the ad leans on stock proof and "#1 agent" bragging instead of a real result and the offer sellers actually want. Fix the Fair Housing language first; nothing else matters until it's legal.

**Findings, worst-first:**

1. **Compliance — Fair Housing (primary text + headline).** Standard: no steering by protected class (`compliance-redlines.md` → active profile). The pre-pass flagged "perfect for families" and "family-friendly" (familial-status steering) and "guaranteed price" (unverifiable). Add the one the literal check missed: **"safe … neighborhood"** — coded steering that implies who is and isn't there. Any one of these can draw a HUD complaint. *Hand-back: describe the **property** by its features (beds, baths, lot, updates), never the buyer it's "perfect for." What are the facts about this home that don't signal who should live there? And can you stand behind "guaranteed price," or does it go?*

2. **Dead hook + muted-first (beats 01–02, 0:00–0:10).** Standard: the hook is the ad; on-screen text carries it muted (`method.md`; `failure-modes.md` B1/C1). Ten seconds open on a generic house exterior and the agent talking — a muted seller scrolling sees a house that isn't theirs and no message. *Hand-back: what's on screen in second one that stops a **seller's** scroll with the sound off — a number, a question, their own street?*

3. **No real proof — the "SOLD" is stock (beat 03).** Standard: real footage sells; the proof can't be faked (`method.md`; `failure-modes.md` E2/A2). The entire credibility of a "just sold" ad is that *you* sold it; a stock sign proves nothing and edges toward the faked-proof line. *Hand-back: what real, recent sold result (address blurred, real number) can carry this beat?*

4. **Bragging over offer.** Standard: lead with what the viewer gets (`method.md`; `failure-modes.md` F3/D2). It opens on "#1 agent in town" — about you — while the thing a seller actually wants, the **free home valuation**, is buried in the description. *Hand-back: why isn't the free valuation the spine of the ad?*

5. **Copy truncation (pre-pass).** Primary text is 221 chars, so "find out what your home is worth" — the actual ask — lands well past the in-feed fold (`meta-placement-specs.md`; `failure-modes.md` F1). *Hand-back: what are the first ~120 characters, and is the valuation offer inside them?*

6. **Ad↔landing mismatch.** Standard: the destination echoes the ad (`failure-modes.md` G1). It points at the homepage, not a valuation page. *Hand-back: does the destination open with the free-valuation offer, or make the seller hunt for it?*

**Make this first:** strip the Fair Housing language and the price guarantee (#1) — that's the legal exposure. Then rebuild the opening around the free-valuation offer (#2, #4). Back to you.

---

> **What this receipt proves:** the same editor that critiqued two tattoo-removal ads just critiqued a real-estate ad against an entirely different compliance regime (Fair Housing), catching a legal landmine tattoo rules would never mention — with **zero changes to the spine.** The domain layer is genuinely swappable.
