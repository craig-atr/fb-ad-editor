# Second Pass — a video ad editor for laser tattoo removal clinics

**Second Pass** is a folder-based **editor** for Meta (Facebook/Instagram) direct-response **video ads**, tuned for **laser tattoo removal / aesthetic clinics**. You hand it an ad concept before you spend a dollar making or running it, and it tells you the few beats that will make it get skipped or waste budget — and hands it back for **you** to fix. The industry-specific rules live in a swappable **profile**, so the same editor retargets to another field (a `real-estate` profile ships as proof).

> **What it reviews & who it's for (submission summary):** Second Pass critiques Meta video-ad concepts for laser tattoo removal clinics. It catches the mistakes that make an ad die on the muted scroll — dead hooks, audio-carried messages, discount-led offers, AI-faked proof, guaranteed-results claims that break medical-ad policy — against the direct-response video method. It's an editor, not a rewriter: it points at what's weak, names the standard, and hands it back. Its domain rules are a swappable profile, so it also ships working on real estate (Fair Housing) as a worked example.

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
  compliance-redlines.md  how the compliance layer works (the specifics live in the active profile)
  profiles/               the swappable DOMAIN layer — the only industry-specific files
    tattoo-removal.md     default: medical/aesthetic compliance, offer framing, real proof
    real-estate.md        a second industry (Fair Housing) — proof the layer swaps
    _TEMPLATE.md          copy this to add your own industry
README.md      you are here
```

## Quickstart

1. **Drop this folder into a Claude project** (or load `identity.md` + `rules.md` + `reference/` into a chat). Claude becomes the editor.
2. **Run the pre-pass** on your ad plan first — it catches the mechanical stuff so the editor spends judgment on the rest:
   ```
   python check.py my-ad-plan.md                        # default profile (tattoo-removal)
   python check.py --profile real-estate my-ad-plan.md  # a different industry
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

A dependency-free script that catches what's objective — the active profile's banned compliance wording, copy over Meta's character limits, a missing/wrong CTA, the wrong aspect ratio, over-length, and an AI-faked before/after. The compliance list and the preferred CTA load from the **active profile** (`reference/profiles/`), so the same script critiques a different industry when you pass `--profile`. The universal checks (copy limits, aspect, length) don't change. Prove it works anytime:

```
python check.py --selftest
```

The self-test loads both shipped profiles and proves each catches its own domain — including that a realtor's "Learn More" CTA is fine under `real-estate` but flagged under `tattoo-removal`, and that Fair Housing wording is caught under `real-estate` but not `tattoo-removal`. The swap is real, not cosmetic.

Compliance hits are **errors** (the ad can't run until they're fixed); the rest are **warnings**. The editor then critiques the things code can't see — the dead hook, the weak offer, the missing proof. *Code catches the wording; the editor catches the meaning.*

## Make it yours (retarget to another industry)

Second Pass ships tuned for laser tattoo removal, but the **spine** — the critique method (`rules.md`), the DR-video standard (`method.md`), the Meta specs — is the same for any local direct-response video ad. **You don't touch the spine.** You write one **profile**:

1. Copy `reference/profiles/_TEMPLATE.md` to `reference/profiles/<your-industry>.md` and fill in your compliance red-lines (the machine-readable list `check.py` reads), your offer framing, and what counts as real proof.
2. Name it the active profile in `identity.md`, and run `check.py --profile <your-industry>`.
3. Optionally swap `examples.md` for weak/strong plans from your field.

The shipped `real-estate.md` is a full worked example — a completely different compliance regime (Fair Housing instead of medical claims), the same editor, no spine changes. See it run in [`receipts/`](receipts/).

The whole point: an editor that catches the mistakes a junior ad-maker makes in *your* domain, so you catch them on paper instead of paying for them in the feed.
