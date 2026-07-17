# Meta Placement Specs — the checkable limits

Hard numbers to critique an ad plan against. These are objective — either the plan honors them or it doesn't. (The `check.py` pre-pass automates the parts it can see; this file is the human-readable source and covers what code can't.)

Default target: **9:16 vertical (Reels / Stories)**, 1080 × 1920.

## Aspect ratio & size

| Placement | Aspect | Pixels |
| --- | --- | --- |
| **Reels / Stories (default)** | **9:16** | **1080 × 1920** |
| Feed (square) | 1:1 | 1080 × 1080 |
| Feed (vertical) | 4:5 | 1080 × 1350 |

An asset at the wrong aspect ratio for its placement is a finding. Vertical video that's actually 16:9 or 1:1 letterboxes and reads as an afterthought.

## Copy limits (before truncation)

| Element | Limit |
| --- | --- |
| Primary text | ~125 characters (front-load hook + offer) |
| Headline | ~40 characters |
| Description | ~30 characters |
| CTA | Fixed choices — **Book Now** for a booking objective |

Copy over the limit isn't "too long" as a style note — it's **literally cut off in-feed**, so anything after the limit may never be seen. Front-load accordingly.

## Safe zones (9:16) — design for muted, UI-occluded viewing

```
Canvas 1080 × 1920
  Top 250 px ............ avoid (profile / sound icons)
  Middle ~1080 × 1420 ... SAFE — key text and subject here
  Bottom ~700 px (Reels)  caption + CTA + profile row — avoid for headlines
```

Practical rule: center important text vertically, keep it in roughly the middle 60% of the frame, never put a headline in the bottom third. The subject can fill the frame edge-to-edge; only text/logos need the safe band. Text outside the safe zone is a finding.

## On-screen text (muted playback)

- Assume **sound off** — on-screen text must carry the message.
- **Big, high-contrast**, 2–6 words per beat.
- Something changes on screen **every 2–3 seconds** (cut or motion).
- Keep burned-in text inside the safe zone.

## Length

- Target **15–20 s** assembled (a story/brand piece can reach ~22 s if the hook holds). Per-scene 2–5 s.
