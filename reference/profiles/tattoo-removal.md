# Profile: Laser Tattoo Removal / Aesthetic Clinic

The **default** domain profile — the industry-specific layer Second Pass ships tuned for.
The spine (`rules.md`, `method.md`, `meta-placement-specs.md`, `failure-modes.md`) is
general to any direct-response video ad; *this* file is what makes it specific to laser
tattoo removal. Swap this file (see `_TEMPLATE.md`) to retarget the editor to another
industry — the critique method doesn't change, the domain rules do.

Active profile is named in `identity.md`. `check.py` reads the machine-readable
**Red-line phrases** and **Preferred CTA** sections below.

## Audience & objective

- Local, appointment-based clinic; **bookings (free consultations) are the priority metric.**
- Audience: adults 25–55; women-first for gifting/relational angles, then broaden.
- The purchase is trust-first and emotionally loaded (regret, nervousness about a laser) — the writing has to reassure, not hype.

## Offer framing (what a strong offer looks like here)

Frame as **Gift + Confidence + Fresh Start**, not "discount." Strongest → weakest:

1. **Free consultation + small bonus** ("Free Consultation + $50 Off First Package") — low friction, best for cold traffic.
2. **Gift-card / package bonus** ("Buy $300, Get $50 Bonus") — feels like a gift.
3. **Limited package %-off** — only for bigger jobs; pair with premium language or it cheapens the service.

Add urgency ("limited seasonal availability") *without* heavy discount language. Leading with "% off" as the whole angle is a finding (`failure-modes.md` D1).

## What "real proof" means here

The money shot is **real footage of the laser in action and real client before/afters** (with permission). That footage is the trust of the whole ad. AI is for hooks, emotional beats, lifestyle, and brand frames — **never** the proof. An AI-generated before/after is both a performance miss and a compliance violation (below).

## Compliance red-lines (the non-negotiables for this industry)

Medical/aesthetic advertising can't promise outcomes — laser results vary by ink, skin, and immune response. A violation here is always the **first** finding: it risks the ad account and legal exposure, not just performance.

- **No guaranteed outcomes.** Capability + honesty only ("can help fade," "most clients see significant fading over a series," "results vary"), never a promise of removal, permanence, painlessness, or zero risk.
- **Proof must be real** (see above) — never AI-faked, never stock passed as a client.
- **No medical overreach** — no diagnosing from an ad; any "FDA-cleared" claim must be verified true for the specific device before it runs.

`check.py` flags the *wording*; the editor judges whether a before/after is genuinely real and whether an FDA claim is true — those stay human-verified.

## Red-line phrases (check.py reads this list)

Format: `- <regex> :: <why>`

- guarantee(d|s)? :: guaranteed-outcome claim
- permanent(ly)? :: permanence claim
- gone (for good|forever) :: permanence claim
- 100\s*% :: absolute claim
- (completely|fully)\s+(remove|removed|removes|gone|erased?|eliminat\w+) :: absolute-removal claim
- erase[sd]? :: erasure-as-promise claim
- removes?\s+all\s+(the\s+)?ink :: absolute-removal claim
- pain[\s-]?(less|free) :: painless claim
- no\s+pain :: painless claim
- (no|zero)\s+risk :: no-risk claim
- risk[\s-]?free :: no-risk claim
- no\s+side\s+effects? :: no-side-effects claim
- (any|every|all)\s+skin\s+types? :: works-on-everyone claim
- works?\s+on\s+(everyone|anybody|any\s+tattoo) :: works-on-everyone claim
- fda[\s-]?(approved|cleared) :: FDA claim - must be verified true for the device

## Preferred CTA

Book Now
