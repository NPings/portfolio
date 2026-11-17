#!/usr/bin/env python3
"""Check the session-notes copy (PRD section 20, R25).

Usage, from the repo root:
  python3 docs/tools/voicecheck.py                       # checks the copy block in the PRD
  python3 docs/tools/voicecheck.py assets/js/site.js     # also checks site.js carries it unchanged

The PRD holds the copy as the only ```json block in docs/portfolio-restructure-PRD.md.
site.js must hold the same object between the markers /*VOICES-BEGIN*/ and /*VOICES-END*/,
as `var VOICES = {...};`. Prints OK and exits 0, or prints each problem and exits 1.
"""
import json, re, sys

PRD = "docs/portfolio-restructure-PRD.md"
SLUGS = ["research-operations", "consumer-research"]
SECTIONS = ["Philosophy", "Practice", "Selected Work", "Impact", "Experience", "Methods", "Tools", "Debrief"]
EVENTS = ["open", "hero", "sections", "sectionFallback", "depth50", "method1", "method5",
          "methodAll", "role", "idle", "return"]
OPTIONAL_EVENTS = {}
CONDS = {"always", "long", "full", "methods5", "methodsAny", "rolesAny", "pausesAny", "clickedAny", "rageAny"}
PLACEHOLDERS = {"cards", "name", "label", "role", "time", "seen", "total", "mN", "mNames", "mTotal",
                "rN", "rNames", "rTotal", "pN", "rage"}
# Tone guard (R25): words that grade or doubt the visitor. "No judgment." is the one allowed use of "judg".
BANNED = re.compile(r"apparently|presumably|didn't|did not|fail|skipp|ignor|lazy|should have|missed|"
                    r"bounce|admired from|only skim|judg|wrong|lost you|gave up", re.I)
ALLOWED = ["No judgment."]
DASHES = re.compile("[\u2014\u2013]|&mdash;|&ndash;| -- ")


def load_prd():
    text = open(PRD, encoding="utf-8").read()
    blocks = re.findall(r"```json\n(.*?)\n```", text, re.S)
    if len(blocks) != 1:
        sys.exit("expected exactly one ```json block in %s, found %d" % (PRD, len(blocks)))
    return json.loads(blocks[0])


def strings(v):
    out = [v["panelTitle"], v["panelTitleDone"], v["debriefLabel"], v["debriefNote"]]
    for k, s in v["events"].items():
        out += list(s.values()) if k == "sections" else [s]
    for item in v["debrief"]:
        out += [c[1] for c in item["cases"]]
    return out


def check(voices):
    errs = []
    if sorted(voices) != sorted(SLUGS):
        errs.append("voice keys %s != %s" % (sorted(voices), sorted(SLUGS)))
    for slug, v in voices.items():
        want = set(EVENTS) | {k for k, who in OPTIONAL_EVENTS.items() if slug in who}
        if set(v["events"]) != want:
            errs.append("%s: event keys %s != %s" % (slug, sorted(v["events"]), sorted(want)))
        if list(v["events"].get("sections", {})) != SECTIONS:
            errs.append("%s: section keys not %s" % (slug, SECTIONS))
        for item in v["debrief"]:
            conds = [c[0] for c in item["cases"]]
            if conds[-1] != "always" or not set(conds) <= CONDS:
                errs.append("%s: bad debrief cases %s" % (slug, conds))
        for s in strings(v):
            for p in re.findall(r"\{(\w+)\}", s):
                if p not in PLACEHOLDERS:
                    errs.append("%s: unknown placeholder {%s} in %r" % (slug, p, s))
            t = s
            for a in ALLOWED:
                t = t.replace(a, "")
            if BANNED.search(t):
                errs.append("%s: tone guard hit %r in %r" % (slug, BANNED.search(t).group(0), s))
            if DASHES.search(s):
                errs.append("%s: dash in %r" % (slug, s))
            if re.search(r"intro", s, re.I):
                errs.append("%s: 'intro' in %r (R18)" % (slug, s))
    return errs


def main():
    voices = load_prd()
    errs = check(voices)
    if len(sys.argv) > 1:
        js = open(sys.argv[1], encoding="utf-8").read()
        m = re.search(r"/\*VOICES-BEGIN\*/\s*var VOICES\s*=\s*(\{.*?\});\s*/\*VOICES-END\*/", js, re.S)
        if not m:
            errs.append("%s: no /*VOICES-BEGIN*/ var VOICES = {...}; /*VOICES-END*/ block" % sys.argv[1])
        elif json.loads(m.group(1)) != voices:
            errs.append("%s: VOICES differs from the PRD copy block" % sys.argv[1])
    for e in errs:
        print(e)
    n = sum(len(strings(v)) for v in voices.values())
    print("OK: %d voices, %d strings" % (len(voices), n) if not errs else "FAIL: %d problem(s)" % len(errs))
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
