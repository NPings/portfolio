#!/usr/bin/env python3
"""Check the positioning copy (PRD Addendum B, section 28, R29 to R32).

Usage, from the repo root:
  python3 docs/tools/narrativecheck.py

The PRD holds the copy as the only ```narrative block in docs/portfolio-restructure-PRD.md,
one `key: text` per line. Brackets [like this] mark the .mark span and are stripped before checks.
Prints OK and exits 0, or prints each problem and exits 1.

What it enforces (the two hard constraints from card t_7e1550e9, plus site voice):
  1. Translated, not verbatim: no run of 5 or more words shared with Nick's framing quote.
  2. No pivot story: no "used to / pivot / no longer / moved into / in recent years" style wording,
     and any line that names an origin (started, roots, grew out of...) also carries a present-tense
     continuity marker (still, alongside, and counting...).
  3. Both practices together: the homepage intro, the three hero ledes and the resume lede each
     name consumer research and AI.
  4. Site voice: no em or en dashes.
"""
import re, sys

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


def load():
    text = open(PRD, encoding="utf-8").read()
    blocks = re.findall(r"```narrative\n(.*?)\n```", text, re.S)
    if len(blocks) != 1:
        sys.exit("expected exactly one ```narrative block in %s, found %d" % (PRD, len(blocks)))
    copy = {}
    for line in blocks[0].splitlines():
        if line.strip():
            k, _, v = line.partition(": ")
            copy[k.strip()] = v.strip()
    return copy


def main():
    copy = load()
    errs = []
    if list(copy) != KEYS:
        errs.append("keys %s != %s" % (list(copy), KEYS))
    for k, raw in copy.items():
        v = raw.replace("[", "").replace("]", "")
        if DASHES.search(v):
            errs.append("%s: has a dash" % k)
        m = PIVOT.search(v)
        if m:
            errs.append("%s: pivot wording %r" % (k, m.group(0)))
        if ORIGIN.search(v) and not CONTINUITY.search(v):
            errs.append("%s: names an origin with no continuity marker" % k)
        run = longest_shared_run(v, QUOTE)
        if run > MAX_SHARED_RUN:
            errs.append("%s: shares a %d-word run with Nick's quote" % (k, run))
        if k in BOTH and not (CONSUMER.search(v) and AI.search(v)):
            errs.append("%s: must name both consumer research and AI" % k)
    if errs:
        print("\n".join(errs))
        sys.exit(1)
    longest = max(longest_shared_run(v.replace("[", "").replace("]", ""), QUOTE) for v in copy.values())
    print("OK: %d strings, longest run shared with the quote = %d words" % (len(copy), longest))


if __name__ == "__main__":
    main()
