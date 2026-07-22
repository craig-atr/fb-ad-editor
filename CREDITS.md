# Credits — ideas taken from Comp #8

The Comp #8 feedback package named an original idea in each of thirty-two builds and told the
community to take from them freely. This build did. Below is what was borrowed, from whom, and
**exactly where it shows up here** — so the credit is checkable rather than decorative.

Where someone's *named* idea differs from the specific pattern borrowed, the pattern is what's
credited.

---

### "A must in markdown is a request; a must in code is a constraint"
**[Jodi Paige-Lee — Debrief Specialist](https://github.com/jmarielee/debrief-specialist)**
The reason [`check.py`](check.py) exists at all. This build is deliberately two-layered the way
Jodi named it: `rules.md` + `reference/` are the request layer the model is asked to honor, and
`check.py` is the constraint layer that fails out loud. Her framing is why the compliance
red-lines aren't only prose.

### The blocking, self-tested gate in code
**[Gabriel Azoulay — Visit Ready](https://github.com/NFTYoginis/prepare-dr-visit)**
Gabriel moved the invariant everyone else wrote as prose into a `check.py` with a self-test
corpus. That's the shape of this repo's pre-pass: compliance hits are **errors** that exit
non-zero, and `python check.py --selftest` proves the gate still catches what it claims —
including across both industry profiles.

### "No draft, just the decision" — stopping one step before the artifact
**[Greg Prince — Agentic Loop Editorial Specialist](https://github.com/optimarketai-arch/agentic-loop-specialist)**
The single most load-bearing idea in this build. An editor that stops one step before the
artifact is exactly what Comp #9 asked for, and Greg had already named the discipline. It's
[`rules.md`](rules.md) §4 ("Critique, never create") and the hand-back test: *if your hand-back
could be pasted straight into the ad, you've rewritten it.*

### The boundary as product
**[Jen Cortez-Walters — Revenue Runaway Audit](https://github.com/JenCW/revenue-runaway-audit)**
"You close nothing. You run nothing" as the *spine* of the product, not a disclaimer. Here it's
[`identity.md`](identity.md) — "You critique. You do not create." — and the line in `rules.md`:
*you do the diagnosis; the maker does the surgery.* The refusal is the value.

### The ordered, citable rubric
**[Matt H — Realee Lead Desk](https://github.com/Realeeai/realee-lead-desk)**
Judgment externalized into an ordered rubric with citable IDs, so every call is contestable line
by line. That's [`reference/failure-modes.md`](reference/failure-modes.md): failure modes ranked
by cost and given IDs (`A1`…`H1`) that every finding cites, so a critique can be argued with
instead of taken on faith. *(Matt's named idea is FLAG-as-the-fifth-outcome — a different one;
the rubric shape is what's borrowed here.)*

### "A blank is not a gap" — presence resolution
**[Charlie Weeks — Marshal](https://github.com/fastedd27/marshal)**
Charlie's distinction between *absent* and *undocumented* is why this editor treats missing
inputs as findings rather than silence: [`identity.md`](identity.md) — "an ad plan with no offer,
or no hook, **is itself a finding**" — and `rules.md` §6, which forbids critiquing around a hole
or inventing what isn't there.

### Receipts — the run shipped as inspectable evidence
**[Mira Bradshaw — chalky-prd](https://github.com/mirabradshaw-data/chalky-prd)**
The whole [`receipts/`](receipts/) folder is Mira's idea applied: each run ships the exact input,
the **verbatim** pre-pass output, and the critique, so a stranger can re-run it
(`python check.py receipts/<run>/ad-plan.md`) instead of trusting a claim.

### Canonical source — name one file canonical, make disagreement a bug
**[Nicolás Patrón — structure-call-ar](https://github.com/Nicopatron/structure-call-ar)**
Why the red-line phrases live in **one** place. `check.py` *reads* the active profile rather than
keeping its own copy — the only thing in code is a clearly-labeled emergency fallback for when the
profile file is missing. No second source of truth to drift.

### The preferences table as an edit surface
**[Sunny Singh — Context Re-Entry](https://github.com/ms-codehorizon/context-reentry)**
Sunny's pattern of exposing the tunable decisions as one editable surface is the shape of
[`reference/profiles/`](reference/profiles/) — the domain rules (compliance, offer framing, real
proof, preferred CTA) are one file you swap, instead of settings scattered through the spine.

---

Method credit: the direct-response video standard in [`reference/method.md`](reference/method.md)
is distilled from the Van Clief Facebook video-ad process, by way of this build's companion
generator, [`fb-ad-studio`](https://github.com/craig-atr/fb-ad-studio).
