# Profile: <Your Industry>

Copy this file to `reference/profiles/<your-industry>.md`, fill it in, set the active
profile in `identity.md`, and run `check.py --profile <your-industry>`. You do **not**
touch the spine (`rules.md`, `method.md`, `meta-placement-specs.md`, `failure-modes.md`)
— the critique method and the Meta/video standards are the same for every industry. Only
these domain rules change.

Look at `tattoo-removal.md` (medical/aesthetic compliance) and `real-estate.md` (Fair
Housing) as worked examples — deliberately different compliance regimes.

## Audience & objective

- Who is this for, and what's the priority metric (bookings, leads, calls)?
- What's the emotional state of the viewer (nervous, aspirational, in a hurry)?

## Offer framing (what a strong offer looks like here)

- What's the strongest offer type in your industry, and how is it framed?
- What framing *cheapens* your service and should be flagged?

## What "real proof" means here

- What is the credible, real proof in your field (before/afters, results, testimonials)?
- What counts as faking it (stock, AI, exaggerated numbers)?

## Compliance red-lines (the non-negotiables for this industry)

- What claims can get you fined, sued, or your ad account pulled? (Every regulated
  service has them — medical, legal, financial, housing, childcare, supplements…)
- Prose explanation here; the machine-readable list below is what `check.py` enforces.

## Red-line phrases (check.py reads this list)

Format: `- <regex> :: <why>`  (case-insensitive; plain phrases work too)

- <regex-or-phrase> :: <why this is a red-line>
- <regex-or-phrase> :: <why>

## Preferred CTA

<the Meta CTA button(s) that fit your objective — comma-separated if more than one>
