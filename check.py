#!/usr/bin/env python3
"""
Second Pass - ad-plan pre-pass.

The mechanical layer of the editor. It catches the red-lines that are objective -
banned compliance wording, copy over Meta's character limits, a missing/wrong CTA,
the wrong aspect ratio, over-length - so the human editor spends judgment on the
things code can't see (a dead hook, a weak offer, faked proof).

Code catches the wording; the editor catches the meaning.

Usage:
    python check.py adplan.md          # scan a file
    cat adplan.md | python check.py    # or stdin
    python check.py --selftest         # run the built-in fixtures

Exit code 0 when there are no ERRORs, 1 when a compliance ERROR is found (or a
self-test fails). Pass --strict to also fail on WARNs.

Standard library only. Output is ASCII and stdout is switched to UTF-8 where
possible, so it runs on a stock Windows (cp1252) console without crashing.
"""

import re
import sys

# --- Compliance red-lines (ERROR) - mirrors reference/compliance-redlines.md sec 1 ---
# Guaranteed-outcome / safety-overreach wording. The pre-pass flags the phrase;
# the editor judges intent. False positives are acceptable - a flagged safe use is
# cheaper than a missed violation.
BANNED_PATTERNS = [
    (r"\bguarantee(d|s)?\b", "guaranteed-outcome claim"),
    (r"\bpermanent(ly)?\b", "permanence claim"),
    (r"\bgone (for good|forever)\b", "permanence claim"),
    (r"\b100\s*%", "absolute claim"),
    (r"\b(completely|fully)\s+(remove|removed|removes|gone|erased?|eliminat\w+)\b", "absolute-removal claim"),
    (r"\berase[sd]?\b", "erasure-as-promise claim"),
    (r"\bremoves?\s+all\s+(the\s+)?ink\b", "absolute-removal claim"),
    (r"\bpain[\s-]?(less|free)\b", "painless claim"),
    (r"\bno\s+pain\b", "painless claim"),
    (r"\b(no|zero)\s+risk\b|\brisk[\s-]?free\b", "no-risk claim"),
    (r"\bno\s+side\s+effects?\b", "no-side-effects claim"),
    (r"\b(any|every|all)\s+skin\s+types?\b", "works-on-everyone claim"),
    (r"\bworks?\s+on\s+(everyone|anybody|any\s+tattoo)\b", "works-on-everyone claim"),
    (r"\bfda[\s-]?(approved|cleared)\b", "FDA claim - must be verified true for the device"),
]

# --- Labeled-field limits (WARN) - mirrors reference/meta-placement-specs.md ---
FIELD_LIMITS = {"primary text": 125, "headline": 40, "description": 30}
FIELD_LABELS = ["primary text", "headline", "description", "cta", "format",
                "placement", "aspect", "aspect ratio", "duration", "length"]


def _make_stdout_safe():
    """Windows consoles default to cp1252 and crash on non-ASCII (dashes, and any
    unicode echoed from the user's ad plan). Switch stdout to UTF-8 where we can."""
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def _clean(line):
    """Strip markdown noise so a labeled field is easy to parse."""
    return line.replace("*", "").replace("`", "").lstrip("> ").rstrip()


def extract_fields(text):
    """Pull labeled fields (label -> value) from an ad plan. Heuristic, forgiving."""
    fields = {}
    label_re = re.compile(r"^\s*([A-Za-z][A-Za-z /]+?)\s*[:\-]\s*(.*)$")
    for raw in text.splitlines():
        line = _clean(raw)
        m = label_re.match(line)
        if not m:
            continue
        label = m.group(1).strip().lower()
        if label in FIELD_LABELS:
            value = m.group(2).strip().strip('"').strip("'").strip()
            if value and label not in fields:
                fields[label] = value
    return fields


def lint(text):
    """Return a list of (severity, label, message). severity is 'ERROR' or 'WARN'."""
    findings = []
    low = text.lower()

    # 1. Compliance red-lines (ERROR)
    for pattern, label in BANNED_PATTERNS:
        for m in re.finditer(pattern, low):
            findings.append(("ERROR", "compliance", '"' + m.group(0).strip() + '" - ' + label))

    fields = extract_fields(text)

    # 2. Copy over Meta's limits (WARN)
    for field, limit in FIELD_LIMITS.items():
        if field in fields and len(fields[field]) > limit:
            findings.append(("WARN", "copy-limit",
                             f"{field} is {len(fields[field])} chars, past Meta's ~{limit} (truncates in-feed)"))

    # 3. CTA (WARN)
    if "cta" in fields:
        if "book now" not in fields["cta"].lower():
            findings.append(("WARN", "cta", f'CTA is "{fields["cta"]}" - booking objective wants "Book Now"'))
    elif any(k in fields for k in ("primary text", "headline")):
        findings.append(("WARN", "cta", "no CTA found - a booking ad should specify Book Now"))

    # 4. Aspect ratio (WARN)
    if re.search(r"\b16\s*:\s*9\b", low) or re.search(r"\b(horizontal|landscape)\b", low):
        findings.append(("WARN", "aspect", "16:9 / horizontal - vertical placements want 9:16 (or 1:1 / 4:5)"))

    # 5. Over-length (WARN)
    durations = [int(n) for n in re.findall(r"~?\s*(\d{1,3})\s*(?:s\b|sec\b|secs\b|second|seconds)", low)]
    if durations and max(durations) > 22:
        findings.append(("WARN", "length", f"~{max(durations)}s - target is 15-20s (<=22 for a story piece)"))

    # 6. Proof possibly faked (WARN - heuristic; editor verifies)
    if re.search(r"before\s*/?\s*(and\s+)?after", low) and re.search(r"\bai[\s-]?(generated|clip|image|made)\b", low):
        findings.append(("WARN", "proof",
                         "a before/after appears near 'AI' - proof must be real footage, not AI (verify)"))

    return findings


def report(text, strict=False):
    _make_stdout_safe()
    findings = lint(text)
    errors = [f for f in findings if f[0] == "ERROR"]
    warns = [f for f in findings if f[0] == "WARN"]
    for sev, label, msg in findings:
        print(f"{sev}  [{label}] {msg}")
    if not findings:
        print("clean pre-pass - no mechanical red-lines. Now critique by eye against the rubric.")
    print(f"\n{len(errors)} error(s), {len(warns)} warning(s).")
    if errors:
        print("-> Compliance errors are the FIRST finding. The ad can't run until they're fixed.")
        return 1
    if strict and warns:
        return 1
    return 0


# --- Self-test --------------------------------------------------------------

CLEAN_PLAN = """
Offer: Free Consultation + $50 off your first package (limited seasonal availability)
Format: 9:16 vertical, 1080x1920, ~18s
Hook (0:00-0:03): tight shot of someone covering an old tattoo
Primary text: Ready for a fresh start? Free consult + $50 off your first package this month.
Headline: A fresh start this spring
Description: Free consult + $50 off
CTA: Book Now
Landing: /book-consultation (repeats the hook line)
"""

BAD_PLAN = """
Offer: 20% off all packages, guaranteed results!
Format: 16:9 video, ~30 seconds
0:12-0:20: an AI-generated before/after showing the tattoo fading
Primary text: We use the latest laser technology to completely and permanently erase your unwanted ink, guaranteed, with no pain and no risk for any skin type - our friendly staff will make you feel at home.
Headline: The Best Tattoo Removal in Town - Guaranteed Results
CTA: Learn More
"""


def selftest():
    _make_stdout_safe()
    failures = 0

    clean_errors = [f for f in lint(CLEAN_PLAN) if f[0] == "ERROR"]
    if clean_errors:
        failures += 1
        print("SELFTEST FAIL: clean plan raised compliance ERRORs:")
        for f in clean_errors:
            print("   ", f)
    else:
        print(f"ok: clean plan has no compliance errors ({len(lint(CLEAN_PLAN))} minor warning(s))")

    bad = lint(BAD_PLAN)
    bad_errors = [f for f in bad if f[0] == "ERROR"]
    bad_labels = {f[1] for f in bad}
    checks = [
        (len(bad_errors) >= 3, "bad plan flags multiple compliance errors"),
        ("copy-limit" in bad_labels, "bad plan flags copy over limit"),
        ("cta" in bad_labels, "bad plan flags the wrong CTA"),
        ("aspect" in bad_labels, "bad plan flags 16:9"),
        ("length" in bad_labels, "bad plan flags over-length"),
        ("proof" in bad_labels, "bad plan flags AI before/after"),
    ]
    for ok, name in checks:
        if ok:
            print(f"ok: {name}")
        else:
            failures += 1
            print(f"SELFTEST FAIL: {name}")

    print()
    if failures:
        print(f"SELFTEST: {failures} failure(s).")
        return 1
    print("SELFTEST: passed - clean plan clears, bad plan caught on every axis.")
    return 0


# --- Entry point ------------------------------------------------------------

def main(argv):
    args = argv[1:]
    strict = "--strict" in args
    args = [a for a in args if a != "--strict"]

    if "--selftest" in args:
        return selftest()

    paths = [a for a in args if not a.startswith("--")]
    if paths:
        with open(paths[0], "r", encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = sys.stdin.read()

    return report(text, strict=strict)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
