#!/usr/bin/env python3
"""Check the positioning copy (PRD Addendum B section 28, as superseded by Addendum C section 34).

Usage, from the repo root:
  python3 docs/tools/narrativecheck.py

The PRD holds the copy in ```narrative blocks in docs/portfolio-restructure-PRD.md, one `key: text`
per line. The LAST block is the live one: each addendum appends its own block and the latest wins,
earlier blocks stay in the doc as history. Brackets [like this] mark the .mark span and are stripped
before checks. Prints OK and exits 0, or prints each problem and exits 1.

What it enforces (the two hard constraints from card t_7e1550e9, plus site voice):
  1. Translated, not verbatim: no run of 5 or more words shared with Nick's framing quote.
  2. No pivot story: no "used to / pivot / no longer / moved into / in recent years" style wording,
     and any line that names an origin (started, roots, grew out of...) also carries a present-tense
     continuity marker (still, alongside, and counting...).
  3. Both practices together: the homepage intro, the three hero ledes and the resume lede each
     name consumer research and AI.
  4. Site voice: no em or en dashes.
  5. Locked copy (Addendum C, card t_d1b547d2): lines Nick wrote himself match his text exactly.

EXCEPTIONS: Nick's locked words are never edited to satisfy a heuristic. Where a rule over-fires on
them, the waiver is listed below with its reason (full reasoning in PRD section 34.3), scoped as
narrowly as possible:
  - a "pivot" waiver names the exact phrase that is exempt; the rest of the line is still checked;
  - a "both" waiver exempts that one line from rule 3 only.
A waiver applies only while the line still matches its LOCKED hash, and a waiver that no longer
fires fails as stale, so an exception can't outlive the text it was written for.
"""
import hashlib, re, sys

PRD = "docs/portfolio-restructure-PRD.md"

# Nick's framing (card t_7e1550e9). Used only to prove the site copy is not a transcript of it.
QUOTE = ("My research roots are in consumer research. In recent years I've been pivoting to research on "
         "AI systems, both consumer and internal. I evaluate/test AI products for our consumers, and "
         "evaluate internal AI systems for reliability and scalability to ensure blockers don't arise.")
MAX_SHARED_RUN = 4

KEYS = ["homepage.intro", "homepage.row.ai-evaluations", "homepage.row.research-operations",
        "homepage.row.consumer-research", "lede.ai-evaluations", "lede.research-operations",
        "lede.consumer-research", "resume.headline", "resume.lede", "switcher.label", "footer.cross"]
BOTH = ["homepage.intro", "lede.ai-evaluations", "lede.research-operations", "lede.consumer-research",
        "resume.lede"]

# Nick's own copy (card t_d1b547d2), locked verbatim: sha256 of the bracket-stripped text, first 16 hex.
LOCKED = {
    "homepage.intro": "d4136752c5dd3e98",
    "homepage.row.ai-evaluations": "56c32e825369bd48",
    "homepage.row.research-operations": "156babccc2b3d9e2",
    "homepage.row.consumer-research": "2be1bfd009b65c64",
    "resume.headline": "6fa09d6096c47cad",
    "resume.lede": "7a33bbdd13836432",
    "switcher.label": "4d9e046e7bf09e85",
    "footer.cross": "e235e5f8669e6cca",
}

# (key, rule) -> (exempt phrase for "pivot", or None for "both"; one-line reason)
EXCEPTIONS = {
    ("homepage.intro", "pivot"): ("Now, I'm broadening",
        "'Now' dates the broadening and replaces nothing: 'broadening' keeps what came before, and the "
        "sentence before it is present perfect (I've spent years honing in on user problems)."),
    ("homepage.row.ai-evaluations", "pivot"): ("can be used to attain",
        "'used to' here is passive 'used' plus 'to attain' (technology is used in order to attain "
        "results), not the habitual past 'I used to'. The line says nothing about Nick's history."),
    ("homepage.intro", "both"): (None,
        "consumer research is named in substance ('user problems', 'guiding businesses toward long term "
        "solutions'), not by the word, and the Consumer Research row sits directly below it."),
    ("resume.lede", "both"): (None,
        "names both by example ('trust breaks down in an onboarding flow', 'agentic experiences'), and "
        "the resume headline directly above it names Consumer Research and AI Evaluations outright."),
}

PIVOT = re.compile(
    r"pivot|transition|used to|no longer|former|previous|prior to|nowadays|these days|lately|"
    r"in recent years|recently|\bnow\b|moved (in)?to|moving (in)?to|move (in)?to|shift|switch|"
    r"away from|\bleft\b|leaving|beyond|then I\b|instead of(?! stopping at a readout)|rather than|"
    r"no more|anymore|once a|graduat|outgrew|retire", re.I)
ORIGIN = re.compile(r"\bstarted\b|\bbegan\b|\broots?\b|foundation|grew out|grow out|origin", re.I)
CONTINUITY = re.compile(r"\bstill\b|alongside|and counting|\bremains?\b|continu", re.I)
CONSUMER = re.compile(r"consumer", re.I)
AI = re.compile(r"\bAI\b")
DASHES = re.compile("[\u2014\u2013]|&mdash;|&ndash;| -- ")


def words(s):
    return re.findall(r"[a-z0-9']+", s.lower().replace("\u2019", "'"))


def longest_shared_run(a, b):
    a, b = words(a), words(b)
    best = 0
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            best = max(best, k)
    return best


def digest(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def load():
    text = open(PRD, encoding="utf-8").read()
    blocks = re.findall(r"```narrative\n(.*?)\n```", text, re.S)
    if not blocks:
        sys.exit("no ```narrative block in %s" % PRD)
    copy = {}
    for line in blocks[-1].splitlines():
        if line.strip():
            k, _, v = line.partition(": ")
            copy[k.strip()] = v.strip()
    return copy, len(blocks)


def main():
    copy, nblocks = load()
    errs, waived, used = [], [], set()
    if list(copy) != KEYS:
        errs.append("keys %s != %s" % (list(copy), KEYS))
    for k, raw in copy.items():
        v = raw.replace("[", "").replace("]", "")
        locked_ok = k in LOCKED and digest(v) == LOCKED[k]
        if k in LOCKED and not locked_ok:
            errs.append("%s: differs from Nick's locked text (sha256 %s, want %s)" % (k, digest(v), LOCKED[k]))
        if DASHES.search(v):
            errs.append("%s: has a dash" % k)
        checked = v
        exc = EXCEPTIONS.get((k, "pivot"))
        hit = PIVOT.search(exc[0]) if exc else None
        if exc and hit and locked_ok and exc[0] in checked:
            used.add((k, "pivot"))
            waived.append("EXCEPTION %s [pivot]: %r hits the pivot list; %s" % (k, hit.group(0), exc[1]))
            checked = checked.replace(exc[0], " ")
        m = PIVOT.search(checked)
        if m:
            errs.append("%s: pivot wording %r" % (k, m.group(0)))
        if ORIGIN.search(v) and not CONTINUITY.search(v):
            errs.append("%s: names an origin with no continuity marker" % k)
        run = longest_shared_run(v, QUOTE)
        if run > MAX_SHARED_RUN:
            errs.append("%s: shares a %d-word run with Nick's quote" % (k, run))
        if k in BOTH and not (CONSUMER.search(v) and AI.search(v)):
            missing = " or ".join(n for n, r in (("'consumer'", CONSUMER), ("'AI'", AI)) if not r.search(v))
            if (k, "both") in EXCEPTIONS and locked_ok:
                used.add((k, "both"))
                waived.append("EXCEPTION %s [both]: doesn't say %s; %s" % (k, missing, EXCEPTIONS[(k, "both")][1]))
            else:
                errs.append("%s: must name both consumer research and AI (doesn't say %s)" % (k, missing))
    for key in EXCEPTIONS:
        if key not in used:
            errs.append("stale exception %s: it no longer fires; remove it here and in PRD 34.3" % (key,))
    for w in waived:
        print(w)
    if errs:
        print("\n".join(errs))
        sys.exit(1)
    longest = max(longest_shared_run(v.replace("[", "").replace("]", ""), QUOTE) for v in copy.values())
    print("OK: %d strings (block %d of %d), %d locked, %d documented exceptions, "
          "longest run shared with the quote = %d words"
          % (len(copy), nblocks, nblocks, len(LOCKED), len(waived), longest))


if __name__ == "__main__":
    main()
