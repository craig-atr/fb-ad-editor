# Failure Modes — the mistakes junior ad-makers make

The catalog the editor scans an ad plan against. Each entry: the **mistake**, the **standard** it breaks, **why** it costs, and the **target** a good version hits (a target to hand back — *never* a rewrite to paste in).

Ordered by cost (matches the triage order in `rules.md` §3). Cite these by name in findings.

---

## A. Compliance red-lines (always first — see `compliance-redlines.md`)
- **A1. Guaranteed results.** "Guaranteed removal," "erases completely," "100% gone," "permanent," "painless." → Medical/aesthetic ads can't promise outcomes. Risks the ad account and legal exposure. Target: capability language ("can help fade," "most clients see…"), never a guarantee.
- **A2. Faked proof.** AI-generated "before/after," stock skin passed as a real client. → The proof is the trust; faking it is deceptive and a policy violation. Target: the before/after and treatment shots are *real footage*.
- **A3. Medical overreach.** Diagnosing, promising safety for every skin type, ignoring realistic expectations. → Scope + liability. Target: honest, non-diagnostic framing.

## B. The hook (0:00–0:03) — if this fails, nothing else matters
- **B1. Logo/intro open.** First seconds spent on the brand mark or a slow establishing shot. → On a muted scroll there's no pattern-interrupt and no reason to stop. Target: an arresting image or the viewer's problem, on screen, in second one.
- **B2. Slow build.** The interesting moment arrives at 0:06. → You've already lost most viewers by 0:03. Target: the most arresting beat *is* the opener.
- **B3. No stakes / not relatable.** A pretty shot that doesn't name a feeling or problem. → Nothing to hook onto. Target: the regret/desire the viewer already feels.

## C. Muted-first
- **C1. Audio-carried message.** The point lives in the voiceover; screen has no text. → ~85% watch muted; the message never lands. Target: big on-screen text carries the message alone.
- **C2. Tiny/low-contrast/late text.** Text too small, poor contrast, or appears after the beat it explains. → Unreadable on a phone at a glance. Target: 2–6 words per beat, big, high-contrast, on time.
- **C3. Text in the UI-occluded zone.** Headline in the top 250px or bottom third. → Meta's UI covers it. Target: key text in the middle ~60% (see `meta-placement-specs.md`).

## D. Offer
- **D1. Discount-led.** "20% OFF!!" as the whole angle. → Cheapens a premium service, attracts price-shoppers. Target: Gift + Confidence + Fresh Start, urgency without heavy discounting.
- **D2. No offer / no reason now.** "Book a consultation" with nothing behind it. → No incentive to act today. Target: a concrete offer + a real urgency line.
- **D3. Vague offer.** "Great deals on removal." → Nothing specific to want. Target: a named, specific offer.

## E. Structure & proof
- **E1. No hook→proof→offer arc.** Beats don't build; offer buried or offer-only. → The ad doesn't earn the click. Target: the three-act shape in `method.md`.
- **E2. No real proof.** No laser-in-action or real before/after — or it's faked (see A2). → Nothing builds trust in a trust-first purchase. Target: real footage is the money shot.
- **E3. Static / no cadence.** Long holds, no cut or motion every 2–3s. → Reads as a slideshow; scroll-past. Target: something changes every 2–3 seconds.
- **E4. Polished-over-authentic.** Stock-commercial look. → Doesn't read as native, underperforms real. Target: authentic-professional.

## F. Copy & CTA
- **F1. Truncation death.** Hook/offer not in the first ~125 chars of primary text; headline over ~40. → The key line is cut off in-feed. Target: front-load hook + offer (see `meta-placement-specs.md`).
- **F2. Weak/wrong CTA.** "Learn More," or no CTA. → Booking is the goal; a soft CTA leaks intent. Target: **Book Now**.
- **F3. Bragging, not benefit.** Copy about the studio, not the viewer's outcome. → No reason for *them* to care. Target: the viewer's fresh start, not the business's features.

## G. Ad ↔ landing page
- **G1. Hook not repeated at destination.** Ad promises one thing; landing page is a generic homepage. → The disconnect kills conversion. Target: the destination echoes the ad's hook line and offer.

## H. Testing
- **H1. One hook only.** A single ad, no variants. → The platform never gets to find the winner. Target: 3 hooks, same offer, let Meta pick.
