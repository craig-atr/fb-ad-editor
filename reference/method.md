# The Standard — Direct-Response Video Ad Method

The method a local-service video ad is critiqued *against*. Distilled from the Van Clief Facebook video-ad process (the method the companion generator `fb-ad-studio` automates). When an ad plan violates one of these, that's a finding — cite this file.

This file says what *good* looks like. It is a yardstick, not a script to hand the maker.

## Core beliefs (each one is a standard; violating it is a finding)

- **The offer beats the ad.** The offer/angle is the biggest lever. Frame around the customer's core motivation — the **active profile** names it for your industry — not around a generic discount. A strong ad on a weak offer still under-books.
- **The hook is the ad.** The first 3 seconds decide whether anyone watches. It must lead with the most arresting, emotionally relatable image or line — a pattern-interrupt, not a warm-up or a logo.
- **Muted-first.** Most people watch with sound off. Big on-screen text carries the message; audio is a bonus, never the plan. An ad whose message only exists in the voiceover fails muted.
- **Authentic beats polished.** Real treatment room, real client examples, real sound outperform overproduced stock-style content. "Authentic professional" wins; "commercial" loses.
- **Real footage sells; AI supports.** The winning combo is **AI hook + real proof + real results + strong CTA.** AI is for hooks, emotional beats, lifestyle, brand frames. The money shot — *your profile's real proof* (the treatment in action, the real before/after, the real sold result) — is *real footage*. Faking proof with AI is both a performance miss and a compliance red-line.
- **Fast cuts.** Movement or a cut every 2–3 seconds. A static or slow scene is a scroll-past.
- **Test hooks, not ads.** Ship 3 versions, same offer, different hooks; let the platform pick. One-hook ads leave the winner undiscovered.

## The shape — 15–20 s vertical, three acts

An ad plan should map to this arc. If it doesn't, name where it breaks.

```
0:00–0:03  HOOK       Arresting line/image + fast visual movement. Pattern-interrupt.
0:03–0:12  PROOF      Real treatment in action, real before/after, close-ups. The trust.
0:12–0:20  OFFER+CTA  Offer on screen, then brand close. CTA: Book Now.
```

Typical: 5–6 scenes, 2–5 s each. Total ~15–20 s (a story/brand piece can stretch to ~22 s if the hook holds).

## Offer framing

The strongest offer *type* varies by industry — the **active profile** lists the good-to-weak options for your field (`reference/profiles/<profile>.md` → Offer framing). Two rules hold everywhere:

- **Lead with what the viewer gets**, framed around their motivation — not "call me," not your credentials.
- **Add urgency without heavy discounting.** Discount-as-the-whole-angle cheapens a premium service and attracts price-shoppers. If the plan leads with "% off" as the whole angle, that's a finding (`failure-modes.md` D1).

## Copy structure

- **Headline** — the hook line (~40 chars).
- **Subheadline** — the offer framing.
- **Primary text** — a short punchy version (usually wins) and optionally a longer one. Front-load hook + offer so they survive truncation (~125 chars).
- **Description** — the urgency line (~30 chars).
- **CTA** — **Book Now** (not "Learn More"), unless the objective genuinely isn't a booking.

**Ad↔landing-page match:** the ad copy and the landing page must repeat the **same hook line.** A disconnect between what the ad promised and what the destination says kills conversion — always a finding when the destination doesn't echo the hook.

## Scene source discipline

Every scene is one of: `AI_CLIP` / `AI_IMAGE` (hooks, emotional beats, lifestyle, brand) or `REAL_FOOTAGE` (the real proof your profile defines — the treatment in action, the real before/after, the real listing). **Real footage is the trust builder and must not be faked with AI.** If the plan's only proof is AI-generated, the ad has no real proof — a finding under both performance and compliance.
