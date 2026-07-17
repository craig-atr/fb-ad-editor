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
| [`atomic-lincoln-250/`](atomic-lincoln-250/critique.md) | A real, shipped `fb-ad-studio` brand/story ad (America's 250th) | Pre-pass clean on compliance; 3 mechanical warnings; critique surfaces a real muted-first gap and AI-only proof, keeps the load-bearing hook, rewrites nothing |

Re-run any of them:

```
python check.py receipts/atomic-lincoln-250/ad-plan.md
```
