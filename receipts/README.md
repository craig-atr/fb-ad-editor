# Receipts — real runs

Real runs of Second Pass on real ads, kept end-to-end so anyone can check the work
(and re-run it). Each folder holds the **exact ad plan** reviewed, the **verbatim
`check.py` output**, and the **critique** the editor produced by following this
repo's own `rules.md`.

The point of a receipt is that it's inspectable: the input is here, the pre-pass is
reproducible (`python check.py <folder>/ad-plan.md`), and the critique finds real
problems in real work — including in a *strong* ad — without rewriting a line.

| Run | Ad | Result |
|-----|----|--------|
| [`atomic-lincoln-250/`](atomic-lincoln-250/critique.md) | A real `fb-ad-studio` brand/story ad (America's 250th) | Pre-pass clean on compliance; 3 mechanical warnings; critique surfaces a real muted-first gap and AI-only proof, keeps the load-bearing hook, rewrites nothing |
| [`atomic-mothers-day/`](atomic-mothers-day/critique.md) | A real `fb-ad-studio` direct-response ad (Mother's Day) | A textbook execution — the editor mostly *endorses* it (real proof, muted-first text, right offer) and flags only genuine delivery risks: unshot proof footage, copy truncation, an unconfirmed landing match |

The two runs are chosen to show **calibration**: the editor pulls apart a strong-concept / muted-blind ad, and largely endorses a well-built one — same rubric, tuned to the work in front of it, which is what separates an editor from a checklist.

Re-run either:

```
python check.py receipts/atomic-lincoln-250/ad-plan.md
python check.py receipts/atomic-mothers-day/ad-plan.md
```
