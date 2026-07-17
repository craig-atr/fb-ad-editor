# Second Pass — a video ad editor for local service businesses

**Second Pass** is a folder-based **editor** for Meta (Facebook/Instagram) direct-response **video ads** — the kind local, appointment-based service businesses run to book consultations (laser/med-spas, dental, aesthetics, salons, HVAC, clinics). You hand it an ad concept before you spend a dollar making or running it, and it tells you the few beats that will make it get skipped or waste budget — and hands it back for **you** to fix.

> **What it reviews & who it's for (submission summary):** Second Pass critiques Meta video-ad concepts for local, appointment-based service businesses on small budgets. It catches the mistakes that make an ad die on the muted scroll — dead hooks, audio-carried messages, discount-led offers, faked proof, guaranteed-results claims that break ad policy — against the direct-response video method. It is an editor, not a rewriter: it points at what's weak, names the standard, and hands it back.

## The one rule: it critiques, it does not create

An editor doesn't do the work for you. Second Pass will **never** write your hook, rewrite your copy, or hand back a "fixed" ad. For each problem it gives you four things — the exact **beat/line**, the **standard** it breaks, **why it fails for this audience/placement**, and a **target** to hit — then hands the pen back. If you want something that *generates* the ad, that's its sibling project, [`fb-ad-studio`](https://github.com/craig-atr/fb-ad-studio). Studio makes; this one critiques.

## Folder map

```
identity.md    who the editor is, what it reviews, and the critique-not-rewrite contract
rules.md       HOW it critiques — the four-part finding, the specificity bar, the triage order
examples.md    what good critique looks like (a weak plan fully critiqued + a strong one with real gaps)
check.py       the pre-pass — flags the mechanical red-lines before the human critique
reference/
  method.md               the direct-response video standard it critiques against (the yardstick)
  failure-modes.md        the catalog of junior mistakes, worst-first
  meta-placement-specs.md the checkable limits (aspect, safe zones, copy limits, length)
  compliance-redlines.md  the non-negotiables (no guaranteed results, real proof only)
README.md      you are here
```

## Quickstart

1. **Drop this folder into a Claude project** (or load `identity.md` + `rules.md` + `reference/` into a chat). Claude becomes the editor.
2. **Run the pre-pass** on your ad plan first — it catches the mechanical stuff so the editor spends judgment on the rest:
   ```
   python check.py my-ad-plan.md      # or:  cat my-ad-plan.md | python check.py
   ```
3. **Hand it your ad concept** and ask for a critique. Rough is fine.
4. **Get back** a one-line verdict, then the findings worst-first, then the one fix to make first. Never a rewritten ad.

## What to hand it

Paste whatever you have — the editor reviews what's there and names what's missing:

- The **offer** and who it's for
- The **hook** (what's on screen in the first 3 seconds)
- A **shot-by-shot** breakdown (beats, timing, what's on screen, on-screen text)
- The **Meta copy** — primary text, headline, description, CTA
- The **format** (aspect ratio, length) and the **landing page** it clicks to

A plan with no offer or no hook is itself a finding — it'll tell you.

## What you get back

```
Verdict:  one line — will this stop the scroll and drive a booking, and the single biggest reason.
Findings: worst-first. Each = location -> standard (cited) -> why it fails HERE -> a target to hit.
Make this first: the highest-leverage fix. Then it's back to you.
```

See [`examples.md`](examples.md) for two full worked critiques, and [`receipts/`](receipts/) for **real runs on real ads** — including this editor critiquing a real shipped `fb-ad-studio` campaign, pre-pass output and all.

## The pre-pass (`check.py`)

A dependency-free script that catches what's objective — banned compliance wording ("guaranteed," "permanently erase," "painless"), copy over Meta's character limits, a missing/wrong CTA, the wrong aspect ratio, over-length, and an AI-faked before/after. It mirrors `reference/compliance-redlines.md` and `reference/meta-placement-specs.md`. Prove it works anytime:

```
python check.py --selftest
```

Compliance hits are **errors** (the ad can't run until they're fixed); the rest are **warnings**. The editor then critiques the things code can't see — the dead hook, the weak offer, the missing proof. *Code catches the wording; the editor catches the meaning.*

## Make it yours (for another local service business)

Second Pass ships tuned for laser/aesthetics, but the method is general to local appointment-based service ads. To retarget it:

1. Adjust `reference/method.md` (offer framing, audience) and `reference/compliance-redlines.md` (your industry's ad rules — every regulated service has them) for your business.
2. Swap the examples in `examples.md` for weak/strong plans from your own field.
3. Keep `rules.md` as-is — the critique discipline is the same everywhere.

The whole point: an editor that catches the mistakes a junior ad-maker makes in *your* domain, so you catch them on paper instead of paying for them in the feed.
