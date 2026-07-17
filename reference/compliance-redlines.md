# The Compliance Layer — how it works

Compliance is **domain-specific**, so the actual red-lines live in the **active industry
profile** (`reference/profiles/<profile>.md`), not here. This file explains the *layer* —
the part that's the same for every industry. The specifics change per profile; the
discipline below does not.

## The rule that never changes

A compliance violation is **always the first finding** (`rules.md` §3). It risks the ad
account and legal exposure, not just performance — so it outranks even a dead hook. The
editor flags it and hands it back; it never "fixes" the claim.

## Where the specifics live

Each profile carries two things the editor and `check.py` use:

- A **Compliance red-lines** section (prose) — what claims can get you fined, sued, or your
  ad account pulled in that industry, and the compliant framing to aim for.
- A **Red-line phrases** list (machine-readable) — the wording `check.py` flags mechanically.

Two shipped profiles show how different these regimes are:

| Profile | The dominant compliance regime | Example red-line |
|---------|--------------------------------|------------------|
| `tattoo-removal` (default) | Medical/aesthetic advertising — no guaranteed outcomes | "guaranteed removal," "painless," "erases completely" |
| `real-estate` | **Fair Housing** — no steering by protected class | "perfect for families," "safe neighborhood," "exclusive community" |

Same editor, same critique method, same `check.py` — the compliance layer swaps with the profile.

## What code catches vs. what the editor catches

`check.py` scans for the profile's red-line *wording*. It cannot judge meaning — whether a
before/after is genuinely real, whether an "FDA-cleared" claim is true, whether a phrase is
steering *in context*, or whether a required disclosure is actually present. Those stay
human-verified findings.

**Code catches the wording; the editor catches the meaning.**

> Retargeting to a new industry? You don't touch this file or the rest of the spine — you
> write a new profile. See `reference/profiles/_TEMPLATE.md`.
