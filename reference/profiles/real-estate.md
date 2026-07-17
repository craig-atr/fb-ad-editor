# Profile: Residential Real Estate Agent

A second shipped profile — proof the domain layer is swappable. Nothing in the spine
(`rules.md`, `method.md`, `meta-placement-specs.md`, `failure-modes.md`) changed to
support it; only *this* file did. To use it, set the active profile in `identity.md`
to `real-estate` and run `check.py --profile real-estate`.

The point: a real-estate agent's ads are still Meta direct-response video — the hook,
muted-first, structure, and testing rules are identical. What changes is the offer, the
proof, and — most sharply — the **compliance regime**.

## Audience & objective

- Local buyers and sellers; **lead capture** (seller valuations, buyer consults) is the priority metric.
- Two very different audiences: sellers ("what's my home worth?") and buyers ("show me homes"). An ad should pick one.
- Trust- and stakes-heavy (largest transaction of most people's lives) — credibility and local proof matter more than polish.

## Offer framing (what a strong offer looks like here)

Frame around the lead's actual question, not "call me":

1. **Free home valuation** ("What's your home worth? Free instant estimate") — the strongest seller-lead hook.
2. **Buyer consult / new-listing alerts** ("Get first look at homes before they hit Zillow") — buyer-lead.
3. **Just-sold / market-update proof** ("Sold in 6 days, $22k over ask") — credibility that converts to a call.

Avoid "I'm the #1 agent" bragging with no offer (`failure-modes.md` D2/F3) — lead with what the viewer gets.

## What "real proof" means here

**Real listings, real sold results, real neighborhoods** — not stock photos of houses or generic luxury b-roll. The proof is that *you actually sell homes here*: real property footage, real sold numbers (accurate), real client outcomes (with permission). AI/stock is for hooks and lifestyle, never the "sold" proof.

## Compliance red-lines (the non-negotiables for this industry)

The dominant risk is **Fair Housing**. Ads may not express a preference, limitation, or discrimination based on a protected class (race, color, religion, sex, familial status, national origin, disability). This is the equivalent of the medical profile's "no guaranteed outcomes" — the first finding, always, because violations carry real legal/HUD exposure.

- **No language that steers or signals a preferred/excluded group** — including coded terms ("perfect for families," "safe neighborhood," "exclusive community," "walking distance to [house of worship]," "ideal for young professionals").
- **No guaranteed sale/price claims** ("guaranteed to sell," "guaranteed price") — and any "we'll buy it if it doesn't sell" guarantee needs the program's disclosures.
- **Required disclosure** — brokerage/license identification per state rules and Meta's requirements; "Equal Housing Opportunity" where applicable. (The editor flags when disclosure is absent; you confirm your state's exact rule.)
- **55+ / age-restricted** communities are a lawful exception (HOPA) — so "adult community" / "55+" is flagged to **verify** the exemption applies, not auto-condemned.

`check.py` flags the *wording*; the editor judges steering intent and whether a disclosure is actually present.

## Red-line phrases (check.py reads this list)

Format: `- <regex> :: <why>`

- (perfect|great|ideal)\s+for\s+families :: Fair Housing - familial-status steering
- family[\s-]?friendly :: Fair Housing - familial-status steering
- no\s+(kids|children) :: Fair Housing - familial-status exclusion
- safe\s+(neighborhood|area|community) :: Fair Housing - coded steering (implies who is/isn't there)
- exclusive\s+(neighborhood|community|area) :: Fair Housing - coded steering
- walking\s+distance\s+to\s+(a\s+)?(church|synagogue|mosque|temple) :: Fair Housing - religious steering
- (christian|catholic|jewish|muslim)\s+(community|area|neighborhood) :: Fair Housing - religious steering
- ideal\s+for\s+(singles|couples|young\s+professionals|bachelors?) :: Fair Housing - marital/familial steering
- (handicap|crippled|able[\s-]?bodied) :: Fair Housing - disability language
- integrated\s+(neighborhood|community) :: Fair Housing - race-coded steering
- guarantee(d)?\s+(sale|sold|price|offer) :: unverifiable guaranteed-sale/price claim
- (55\+|adult\s+community|age[\s-]?restricted) :: verify HOPA age-exemption applies before running

## Preferred CTA

Learn More, Sign Up, Get Quote, Contact Us
