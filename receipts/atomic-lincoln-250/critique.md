# Second Pass — critique of atomic-lincoln-250

A real run of this editor on a real, shipped `fb-ad-studio` ad ([`ad-plan.md`](ad-plan.md)).
Nothing here is cherry-picked: the pre-pass output is verbatim, and the critique
follows this repo's own `rules.md` (four-part findings, worst-first, no rewrites).

---

## Step 1 — pre-pass (`python check.py receipts/atomic-lincoln-250/ad-plan.md`)

```
WARN  [copy-limit] primary text is 182 chars, past Meta's ~125 (truncates in-feed)
WARN  [copy-limit] description is 33 chars, past Meta's ~30 (truncates in-feed)
WARN  [length] ~23s - target is 15-20s (<=22 for a story piece)

0 error(s), 3 warning(s).
```

**Zero compliance errors** — worth stating, because it's a real result, not a rubber stamp. The copy sells a "fresh start," never a guaranteed outcome; the studio's compliance discipline held. The pre-pass earns trust by clearing a clean ad, not just flagging a dirty one.

## Step 2 — the critique

**Verdict:** Genuinely strong hook and concept — this stops a scroll. Its risk is the opposite of most ads: it's a *muted brand film with no on-screen text and AI-only proof*, so a viewer who doesn't watch all the way to the 0:20 end-card (most of them) never gets the message or the offer — and the payoff only lands if they catch the history joke. A superb top-of-funnel *hooker*; it won't close on its own.

**Load-bearing strength — keep it (`rules.md` §5):** the "Ann" reveal (beat 4b) is your pattern-interrupt; the entire hook rides on it. Whatever you change, don't let a text-overlay pass bury that beat. And the offer framing is right — "$250 off" is nominally a discount, but tied to the 250th and framed as *independence / a fresh start*, it reads as a themed gift, not a bargain (`method.md` → offer framing; dodges `failure-modes.md` D1).

**Findings, worst-first:**

1. **Muted-first failure — no on-screen text in beats 1–7 (0:00–0:20).** Standard: on-screen text carries the message on muted playback (`meta-placement-specs.md`; `failure-modes.md` C1). The whole story is told in visuals that assume sound-optional viewing *and* watching to the end. A muted scroller sees a costumed man on a hover-cycle with no idea what it's for until 0:20. This is the finding that caps everything else. *Hand-back: what minimal on-screen text could carry the "regret → fresh start" throughline from the first few seconds, without stepping on the "Ann" reveal?*

2. **Concept legibility for a cold audience.** Standard: the hook must be arresting *and emotionally relatable* (`method.md` → the hook is the ad). The payoff depends on decoding "Ann" (Ann Rutledge) and the "Four Score" riff. Clever and shareable *if you get it* — but a 25–55 scroller who misses the lore just sees a costume. The relatable emotion (regret over an old-flame's name) is in the concept but never surfaced for someone who doesn't catch the reference. Compounds #1. *Hand-back: what cue makes "old tattoo you've outgrown → fresh start" read even if the Lincoln joke doesn't?*

3. **No real proof — the treatment beat is AI (beat 5).** Standard: real footage sells; the money shot isn't faked (`method.md`; `failure-modes.md` E2). The only treatment moment is AI-generated; there's no real before/after anywhere. For a top-of-funnel story piece that hooks and hands off, defensible — but nothing here does the trust-building a real result does. *Hand-back: is this ad meant to hook or to close? If close, where does one real client result live?*

4. **Offer reaches the muted viewer only at 0:20.** Standard: muted-first (`meta-placement-specs.md`). The offer lives in the end-card and the copy; a viewer who drops at 0:10 never learns there is one. Same root as #1. *Hand-back: what's the earliest the offer can appear on screen without deflating the story?*

5. **Copy truncation (pre-pass).** Primary text is 182 chars — "$250 off an 8-session package" and "Book your free consultation" fall past the ~125 in-feed fold, so the offer and the ask are what get cut (`meta-placement-specs.md`; `failure-modes.md` F1). Description is 33/30 (minor). *Hand-back: what are the first ~120 characters that must survive — is the offer in them?*

6. **Length ~23s.** Marginally over the ~22s ceiling for a story piece (`meta-placement-specs.md`). Minor; a second trimmed off beat 1 or 3 buys it back.

**Make this first:** the muted-first text layer (#1). One change — surfacing the regret→fresh-start line and the offer on screen without sound — fixes #1, softens #2, and resolves #4 at once. Then decide whether this ad's job is to hook or to close (#3); that answers whether the AI-only proof is fine or a gap.

Back to you — the targets are named; the writing is yours.

---

> **How this receipt was produced:** the ad plan was assembled from the real `fb-ad-studio` campaign files, `check.py` was run on it (output above, verbatim), and the critique was written by following this repo's `identity.md` + `rules.md` + `reference/`. It finds real problems in a real, strong ad, names a genuine strength, and never rewrites a line — which is the whole point of the tool.
