#!/usr/bin/env python3
"""
Second Pass - ad-plan pre-pass.

The mechanical layer of the editor. It catches the red-lines that are objective -
compliance wording, copy over Meta's character limits, a missing/wrong CTA, the
wrong aspect ratio, over-length - so the human editor spends judgment on the things
code can't see (a dead hook, a weak offer, faked proof).

The compliance wording and the preferred CTA are DOMAIN-SPECIFIC, so they load from
the active industry profile in reference/profiles/. The universal checks (copy
limits, aspect, length) are the same for every industry. Swap the profile, and the
same script critiques a different domain.

Usage:
    python check.py adplan.md                       # default profile (tattoo-removal)
    python check.py --profile real-estate adplan.md # swap the domain rules
    cat adplan.md | python check.py                 # stdin
    python check.py --selftest                      # run the built-in fixtures

Exit code 0 when there are no ERRORs, 1 when a compliance ERROR is found (or a
self-test fails). Pass --strict to also fail on WARNs.

Standard library only. ASCII output; stdout switched to UTF-8 where possible so it
runs on a stock Windows (cp1252) console without crashing.
"""

import os
import re
import sys

DEFAULT_PROFILE = "tattoo-removal"

# Copy limits are the same for every advertiser - they're Meta's, not the industry's.
FIELD_LIMITS = {"primary text": 125, "headline": 40, "description": 30}
FIELD_LABELS = ["primary text", "headline", "description", "cta", "format",
                "placement", "aspect", "aspect ratio", "duration", "length"]

# Emergency fallback ONLY if a profile file can't be found (e.g. check.py copied out
# of the repo). The profile files are the source of truth; this is a safety net.
MINIMAL_FALLBACK = [
    (r"\bguarantee(d|s)?\b", "guaranteed-outcome claim"),
    (r"\bpermanent(ly)?\b", "permanence claim"),
    (r"\bpain[\s-]?(less|free)\b", "painless claim"),
]


def _make_stdout_safe():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def _profiles_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "reference", "profiles")


def load_profile(name_or_path):
    """Load an industry profile: its red-line phrases and preferred CTA(s).
    Accepts a bare name ('real-estate') or a path to a .md file."""
    path = name_or_path if name_or_path.endswith(".md") else os.path.join(_profiles_dir(), name_or_path + ".md")
    name = os.path.splitext(os.path.basename(path))[0]

    if not os.path.exists(path):
        return {"name": name, "patterns": [(re.compile(p, re.I), l) for p, l in MINIMAL_FALLBACK],
                "ctas": ["book now"], "missing": True, "path": path}

    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    patterns, ctas, section = [], [], None
    for raw in lines:
        line = raw.strip()
        if line.startswith("## "):
            section = line[3:].strip().lower()
            continue
        if section and section.startswith("red-line phrases") and line.startswith("- "):
            body = line[2:]
            if "::" not in body:
                continue
            rgx, label = body.split("::", 1)
            rgx, label = rgx.strip().strip("`").strip(), label.strip()
            if not rgx or rgx.startswith("<"):   # skip the _TEMPLATE placeholder
                continue
            try:
                compiled = re.compile(rgx, re.I)
            except re.error:
                compiled = re.compile(re.escape(rgx), re.I)   # plain phrases work too
            patterns.append((compiled, label))
        elif section and section.startswith("preferred cta") and line and not line.startswith("<"):
            for c in line.split(","):
                c = c.strip().lower()
                if c and c not in ctas:
                    ctas.append(c)

    if not patterns:
        patterns = [(re.compile(p, re.I), l) for p, l in MINIMAL_FALLBACK]
    if not ctas:
        ctas = ["book now"]
    return {"name": name, "patterns": patterns, "ctas": ctas, "missing": False, "path": path}


def _clean(line):
    return line.replace("*", "").replace("`", "").lstrip("> ").rstrip()


def extract_fields(text):
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


def lint(text, profile):
    """Return a list of (severity, label, message). severity is 'ERROR' or 'WARN'."""
    findings = []
    low = text.lower()

    # 1. Compliance red-lines (ERROR) - from the active profile
    for pattern, label in profile["patterns"]:
        for m in pattern.finditer(low):
            findings.append(("ERROR", "compliance", '"' + m.group(0).strip() + '" - ' + label))

    fields = extract_fields(text)

    # 2. Copy over Meta's limits (WARN) - universal
    for field, limit in FIELD_LIMITS.items():
        if field in fields and len(fields[field]) > limit:
            findings.append(("WARN", "copy-limit",
                             f"{field} is {len(fields[field])} chars, past Meta's ~{limit} (truncates in-feed)"))

    # 3. CTA (WARN) - preferred CTA(s) come from the profile
    if "cta" in fields:
        val = fields["cta"].lower()
        if not any(acc in val for acc in profile["ctas"]):
            findings.append(("WARN", "cta",
                             f'CTA is "{fields["cta"]}" - this profile expects: {", ".join(profile["ctas"])}'))
    elif any(k in fields for k in ("primary text", "headline")):
        findings.append(("WARN", "cta", f'no CTA found - this profile expects: {", ".join(profile["ctas"])}'))

    # 4. Aspect ratio (WARN) - universal
    if re.search(r"\b16\s*:\s*9\b", low) or re.search(r"\b(horizontal|landscape)\b", low):
        findings.append(("WARN", "aspect", "16:9 / horizontal - vertical placements want 9:16 (or 1:1 / 4:5)"))

    # 5. Over-length (WARN) - universal
    durations = [int(n) for n in re.findall(r"~?\s*(\d{1,3})\s*(?:s\b|sec\b|secs\b|second|seconds)", low)]
    if durations and max(durations) > 22:
        findings.append(("WARN", "length", f"~{max(durations)}s - target is 15-20s (<=22 for a story piece)"))

    # 6. Proof possibly faked (WARN - heuristic; editor verifies) - universal
    if re.search(r"before\s*/?\s*(and\s+)?after", low) and re.search(r"\bai[\s-]?(generated|clip|image|made)\b", low):
        findings.append(("WARN", "proof",
                         "a before/after appears near 'AI' - proof must be real footage, not AI (verify)"))

    return findings


def report(text, profile, strict=False):
    _make_stdout_safe()
    if profile.get("missing"):
        print(f"(!) profile '{profile['name']}' not found at {profile['path']} - using minimal fallback\n")
    else:
        print(f"[profile: {profile['name']}]")
    findings = lint(text, profile)
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

TATTOO_CLEAN = """
Offer: Free Consultation + $50 off your first package (limited seasonal availability)
Format: 9:16 vertical, 1080x1920, ~18s
Primary text: Ready for a fresh start? Free consult + $50 off this month.
Headline: A fresh start this spring
CTA: Book Now
"""

TATTOO_BAD = """
Offer: 20% off all packages, guaranteed results!
Format: 16:9 video, ~30 seconds
0:12-0:20: an AI-generated before/after showing the tattoo fading
Primary text: We use the latest laser technology to completely and permanently erase your unwanted ink, guaranteed, with no pain and no risk for any skin type - our friendly staff will make you feel at home.
Headline: The Best Tattoo Removal in Town - Guaranteed Results
CTA: Learn More
"""

RE_CLEAN = """
Offer: What's your home worth? Free instant valuation.
Format: 9:16 vertical, ~18s
Primary text: Curious what your home is worth? Get a free instant estimate in 30 seconds.
Headline: What's your home worth?
CTA: Learn More
"""

RE_BAD = """
Offer: guaranteed sale in 30 days
Format: 16:9, ~30 seconds
Primary text: Perfect for families in a safe neighborhood - an exclusive community, walking distance to church. Ideal for young professionals.
Headline: A great place to raise a family
CTA: Book Now
"""


def selftest():
    _make_stdout_safe()
    failures = 0
    tattoo = load_profile("tattoo-removal")
    realestate = load_profile("real-estate")

    def errs(text, prof):
        return [f for f in lint(text, prof) if f[0] == "ERROR"]

    def labels(text, prof):
        return {f[1] for f in lint(text, prof)}

    checks = [
        (not tattoo.get("missing"), "tattoo-removal profile file loads"),
        (not realestate.get("missing"), "real-estate profile file loads"),
        (len(errs(TATTOO_CLEAN, tattoo)) == 0, "tattoo clean plan: no compliance errors"),
        (len(errs(TATTOO_BAD, tattoo)) >= 3, "tattoo bad plan: multiple compliance errors"),
        ("copy-limit" in labels(TATTOO_BAD, tattoo), "tattoo bad plan: copy over limit"),
        ("aspect" in labels(TATTOO_BAD, tattoo), "tattoo bad plan: flags 16:9"),
        ("proof" in labels(TATTOO_BAD, tattoo), "tattoo bad plan: flags AI before/after"),
        (len(errs(RE_CLEAN, realestate)) == 0, "real-estate clean plan: no compliance errors"),
        ("cta" not in labels(RE_CLEAN, realestate), "real-estate profile accepts 'Learn More' CTA"),
        ("cta" in labels(RE_CLEAN, tattoo), "tattoo profile flags 'Learn More' (profile swap matters)"),
        (len(errs(RE_BAD, realestate)) >= 3, "real-estate bad plan: multiple Fair Housing errors"),
        (all("Fair Housing" not in e[2] for e in errs(RE_BAD, tattoo)),
         "tattoo profile does not flag Fair-Housing-specific terms (isolation)"),
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
    print("SELFTEST: passed - both profiles load, each catches its own domain, the swap changes the result.")
    return 0


# --- Entry point ------------------------------------------------------------

def main(argv):
    args = argv[1:]
    strict = "--strict" in args
    args = [a for a in args if a != "--strict"]

    if "--selftest" in args:
        return selftest()

    profile_name = DEFAULT_PROFILE
    if "--profile" in args:
        i = args.index("--profile")
        if i + 1 < len(args):
            profile_name = args[i + 1]
            del args[i:i + 2]
        else:
            print("usage: --profile <name>"); return 1

    profile = load_profile(profile_name)

    paths = [a for a in args if not a.startswith("--")]
    if paths:
        with open(paths[0], "r", encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = sys.stdin.read()

    return report(text, profile, strict=strict)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
