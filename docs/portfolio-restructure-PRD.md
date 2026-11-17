# PRD: Portfolio restructure, three discipline landing pages

- **Project:** portfolio (nickpings.com), static HTML/CSS/JS, no build step, hosted on GitHub Pages
- **Branch:** `feature/portfolio-restructure`, cut from `main` at `f76ff62`. Pushing this branch to origin is allowed as a backup. GitHub Pages builds only from `main`. Never push to or merge into `main` without Nick's explicit approval.
- **Card:** t_eb4fd595 (PRD). Build cards: not cut yet (PMO cuts them after Nick approves).
- **Author:** product, 2026-11-17
- **Status:** Draft for Crit review, then Nick's approval
- **ADR:** `docs/adr/0001-discipline-page-urls.md` (the URL scheme, because shared job-application links are expensive to change later)
- **davinci-prd skill:** not installed on this Mac. Sections written by hand to the same structure as `docs/intro-experience-PRD.md`.
- **This card changed no existing file.** It adds only this PRD and the ADR under `docs/`.
- **Addendum A (2026-11-17):** sections 17 to 26 and requirements R20 to R28 lock Nick's O1 to O9 decisions, make the one shared `resume.html` read for all three disciplines, and give each landing page its own session-notes voice (exact copy in 20.5). It also puts Nick's new `evaluating-my-agent.html` (on `main` at 3d25fb4) on the AI Evaluations page and adds link-preview images. Card t_48ff0069 (PRD addendum), build card t_2e68d7bf (assignee `design`). Where it changes R2, R4, R8 to R10, R12 to R17 or the section 13 non-goals, section 17.3 says how, and the addendum wins.
- **Addendum B (2026-11-17):** sections 27 to 32 and requirements R29 to R32 fix the positioning story (consumer research is the root and ongoing; AI evaluation of consumer AI products and internal AI systems runs alongside it), give exact copy for the homepage disciplines intro, the three hero ledes and the resume masthead, and replace R6 (section 29). Card t_7e1550e9. Copy only; it follows the design prototype from card t_de460a73.

---

## 0. Source brief (Nick, verbatim, from card t_eb4fd595)

> I think we need to restructure the portfolio. I'm trying to diversify and move out of just UXR. Current potential trajectories are AI evaluations, research operations, or traditional consumer research (mixed methods UXR basically). I think we need discrete pages for each of these potential disciplines following the same formula that our current portfolio index page shows. The intro is fun... but we need to think more broadly about the portfolio site as a whole. We need it to really represent my work in these various fields. The common thread among all of these fields is that they are fundamentally research disciplines. I think instead of having one 'index' we should have three landing pages with their own URLs, case studies, etc, that I can point job apps at. The domain, Nickpings.com will still need a homepage, but we can figure that out later.

Citation shorthand used below: **[Nick]** = the brief above. **[Card]** = Maestro's card body (the 7 numbered items and the done-when). **[index.html Lnn]** = the current `index.html` on `main` at `f76ff62`, line nn. **[case:<file>]** = an existing case-study page. **[resume.html]** = the current resume. **[BACKLOG]** = the repo's `BACKLOG.md`. **[evals-reps]** = Nick's private practice repo `~/Documents/github/ai-evals-reps` (README reps log). **[Probe]** = a check I ran while writing this PRD, results in section 12.

## Map to the card's seven items

| Card item | Where it is decided |
|---|---|
| 1. Inventory and the "formula" | Sections 1 and 2, R2 |
| 2. Three landing pages, URL scheme | Section 3, ADR 0001, R1, R3, R16 |
| 3. Shared thread across all three | Section 4, R4, R5, R6, R10 |
| 4. Case studies, mapping, gaps, content plan | Section 6, R8, R9, R10 |
| 5. nickpings.com homepage (flag only) | Section 7, R17 |
| 6. intro.html recommendation | Section 8, R18 |
| 7. Technical approach, files and assets | Section 9, R14, R15, section 11 |

---

## 1. Inventory: the current site

Repo root on `main` at `f76ff62`. All pages are flat at the root, every page inlines its own CSS, and nothing is built.

| File | Lines | What it is | Linked from `index.html`? | Live |
|---|---|---|---|---|
| `index.html` | 880 | The portfolio front page (the "formula", section 2). Title "Nicholas Pings Rodriguez · Research, Research Operations & AI". | is the root | 200 |
| `resume.html` | 257 | Printable resume. Headline "Senior UX Researcher · Consumer Products & Research Operations". | footer | 200 |
| `experian-eva.html` | 257 | Case study, complete. Eyebrow "Generative & evaluative research · Experian · Multi-phase". | card | 200 |
| `hp-wolf-security.html` | 195 | Case study, complete. Eyebrow "Generative & evaluative research · HP Inc. · 2021". | card | 200 |
| `research-knowledge-base.html` | 333 | Case study, complete. Eyebrow "Research operations · Experian · Ongoing". | card | 200 |
| `research-pmo-agent.html` | 297 | Case study, **draft**: 7 `[Nick to add]`/`[Nick to confirm]` markers. Eyebrow "AI research operations · Experian". | commented out [index.html L440-455] | 200 (unlinked) |
| `skill-kits.html` | 297 | Case study, **draft**: 7 markers. Eyebrow "AI research operations · Experian". | commented out | 200 (unlinked) |
| `research-self-service.html` | 14 | `noindex` redirect stub to `research-knowledge-base.html`. | no | 200 |
| `intro.html` | 2136 | Scroll-driven intro experience (its own PRD, `docs/intro-experience-PRD.md`). Its "straight to business" pill and skip link point at `index.html`. | no | 200 |
| `assets/passions/...` | | Media for `intro.html` only. | no | |

Case-study page pattern (all five): a `← Back to portfolio` link to `index.html` at top and bottom, a header (eyebrow, h1 title, one-paragraph summary, a 4-cell facts row: Role / Method or Approach / third fact / Company), then numbered sections ("01 The question / 02 What I did / 03 What we learned / 04 What changed" for the two consumer cases; "01 The problem" through "07 What I learned" for the three ops/AI cases), then a colophon ("Nicholas Pings Rodriguez · UX Research" or "· UX Research & AI Research Operations"). Each page carries about 110 to 150 lines of near-identical inline CSS with the same token names as `index.html` minus `--rec` [Probe P5].

## 2. The formula (what `index.html` does, top to bottom)

This is the template every discipline page follows. "Shared" means identical on all three pages. "Per page" means the structure is the same but the content is chosen per discipline (section 5).

| # | Section (`id`, `data-obs`) | What it contains [index.html lines] | Behavior | Shared or per page |
|---|---|---|---|---|
| 0 | Hero (`header.hero#top`) | Eyebrow label (L374), `h1.name` "Nicholas Pings Rodriguez" with a moss period (L375), italic thesis with a leaf-highlight `.mark` (L376), "Session in progress" pill with a blinking `--rec` dot (L378) | `.rise` fade-up on load; `.mark` highlight draws in | Name and pill shared; eyebrow and thesis per page |
| S-01 | Philosophy (`#philosophy`) | Two facets: "Find what matters", "Make it go further" (L382-396) | static | **Shared, verbatim** (the identity anchor, section 4) |
| S-02 | Practice (`#practice`) | Four labeled facets (L398-420) | static | Per page: same four facets, order changes |
| S-03 | Selected work (`#selected-work`) | `.case-card` links to case-study pages, title + arrow + one-paragraph blurb (L422-465) | hover lift | Per page: which cards, order, blurb |
| S-04 | Impact (`#impact`) | Marquee of `.stat` number + label (L467-477) | infinite marquee, stops under reduced motion | Per page; optional |
| S-05 | Experience (`#work`) | Three `details.role` accordions: Experian, HP, Freelance (L479-541) | one open at a time | Per page: same roles, bullet order changes |
| S-06 | Methods (`#methods`) | Affinity "sort board": four clusters of `details.chip` with descriptions, 25 chips (L543-592) | chips scatter, then sort when scrolled into view | Per page: cluster set and order |
| S-07 | Tools (`#tools`) | Tool-name marquee (L594-607) | infinite marquee | Per page; optional |
| S-08 | Debrief (`#debrief`) | "Your session": time on page, furthest scroll, methods explored, roles opened (L609-620) | live counters | Shared |
| foot | Footer (`footer.foot`) | "Get in touch." Email, phone, based, resume link, education colophon (L622-631) | static | Shared |
| fixed | Observer panel (`aside#observer`) | "Participant #1 · Session Notes": a live, local-only log that narrates the visit as a usability session and writes a debrief at full scroll (L636-644, script L692-877) | IntersectionObserver per `data-obs`, idle and return notes; nothing stored | Shared |

The through-line of the formula is the **usability-session conceit**: the session pill, the observer log and the debrief treat every visit as a small research session. That conceit is research-generic, not UXR-specific, so it carries the shared identity onto all three pages unchanged (section 4).

Section codes (`S-01`...) are renumbered contiguously on each page, so a page that omits an optional section has no gap in its codes (R2).

## 3. URL and naming scheme (decision)

| Discipline (display name) | File | URL Nick shares |
|---|---|---|
| AI Evaluations | `ai-evaluations.html` | `nickpings.com/ai-evaluations` |
| Research Operations | `research-operations.html` | `nickpings.com/research-operations` |
| Consumer Research | `consumer-research.html` | `nickpings.com/consumer-research` |

Why:

- **Flat top-level files.** Every existing page is flat, and every existing link is a bare relative path. Subfolders would need `../` on every asset and case link and put case pages at a different depth. Full reasoning in ADR 0001.
- **Clean URLs come free.** GitHub Pages already serves `/resume` for `resume.html` [Probe P1], so Nick can paste `nickpings.com/ai-evaluations` without a `.html`. A trailing slash 404s [Probe P2], so the share form has no slash.
- **Full words, matching how roles are titled.** "AI evaluation(s)" and "research operations" are the terms used in the job titles Nick is targeting. "Consumer research" is Nick's own phrase ("traditional consumer research"); the page's eyebrow carries "mixed methods" (section 5.1). `ux-research` was the alternative for the third slug; Flag O3 asks Nick to pick before anything is shared, because slugs are permanent once they sit in applications.
- **One fixed order everywhere:** AI Evaluations, Research Operations, Consumer Research, the order Nick listed them in.

## 4. Shared identity: "fundamentally research disciplines"

Each page must stand alone (a recruiter who opens only `/ai-evaluations` gets a complete portfolio) and still read as one researcher seen from three angles. Six devices do this, in order of weight:

1. **One design system.** Same palette, fonts, components and motion as `index.html`, served from one shared stylesheet (R14). No per-discipline accent colors: color difference would say "three people", and the brief says one identity.
2. **A discipline switcher at the top of every page**, landing and case-study pages alike (R4, R10): the name, then "Research in", then the three disciplines in fixed order, with the current one marked. A visitor who lands on one sees at once that the other two exist, and that all three are "research in" something.
3. **Shared Philosophy, verbatim** (R6). "Find what matters" and "Make it go further" are discipline-neutral. Identical text on all three pages is the plainest signal that the same researcher sits under each.
4. **The same usability-session conceit** (pill, observer, debrief) on all three (R15). Every page treats the visitor as a research participant, whichever discipline it is.
5. **Same name, same footer, same resume, same roles.** The h1, contact block, education line and job titles never change per page (R3, R5, R11). Only emphasis changes: which facets lead, which bullets come first, which cases show.
6. **Footer cross-links**: "Same research, other angles:" with links to the other two pages (R5).

What stays per page: eyebrow, thesis, Practice order, Selected work, Impact, Experience bullet order, Methods clusters, Tools, and the head metadata (title, description, preview text).

## 5. Per-page content matrix

All copy below is drawn from text already on the site or in the case studies, cited per row. Rows marked **draft** are my wording built from that text; Nick can replace any of them, and the build uses whatever this table says at build time (changing copy means amending this table, so Crit has one source of truth).

### 5.1 Hero and head

| Page | Eyebrow | Thesis (the `.mark` span in brackets) | Source |
|---|---|---|---|
| AI Evaluations | `AI evaluations` | `Deciding [where a model is trusted] and where a person decides.` (draft) | [index.html L499] "set the standards for where a model is trusted and where a person decides"; [resume.html] same |
| Research Operations | `Research operations` | `Research that [goes further] than the readout.` (draft) | [index.html L392] "Make it go further ... past the readout"; [resume.html] "instead of stopping at a readout" |
| Consumer Research | `Mixed-methods consumer research` | `Turning [consumer behavior] into product decisions.` (draft) | [resume.html] "Eight years turning consumer behavior into product decisions" |

| Page | `<title>` | `<meta name="description">` (draft) |
|---|---|---|
| AI Evaluations | `Nicholas Pings Rodriguez · AI Evaluations` | `Researcher who sets the standards for where a model is trusted and where a person decides, and evaluates generative AI with the people who use it.` |
| Research Operations | `Nicholas Pings Rodriguez · Research Operations` | `Researcher who rebuilt how research gets done at Experian: self-service access, research standards, onboarding, mentoring, and an AI research knowledge base.` |
| Consumer Research | `Nicholas Pings Rodriguez · Consumer Research` | `Mixed-methods consumer researcher with eight years turning consumer behavior into product decisions, from generative discovery to diary studies.` |

### 5.2 Practice order

The four facets are copied verbatim from [index.html L402-417]: **P1** "Questions before methods", **P2** "Cover the whole lifecycle", **P3** "Apply AI strategically and safely", **P4** "Open access to findings".

| Page | Order |
|---|---|
| AI Evaluations | P3, P1, P4, P2 |
| Research Operations | P4, P3, P2, P1 |
| Consumer Research | P1, P2, P3, P4 (same as `index.html`) |

### 5.3 Selected work

See section 6 for the mapping and gaps. Card titles and hrefs are fixed; blurbs:

| Page | # | Card (href) | Blurb | Source |
|---|---|---|---|---|
| AI Evaluations | 1 | Research Knowledge Base (`research-knowledge-base.html?from=ai-evaluations`) | `An LLM-as-a-judge decides what enters the research knowledge base when it safely can. Researcher sign-off and manager approval stay fixed, and a person steps in whenever the judge can't make a safe call.` (draft) | [case:research-knowledge-base.html] section 03 |
| AI Evaluations | 2 | Experian Virtual Assistant (`experian-eva.html?from=ai-evaluations`) | `Round after round of usability testing on a generative AI assistant for credit questions, including participants who said they'd never use an AI chatbot and changed their minds mid-session.` (draft) | [case:experian-eva.html] sections 02-03 |
| Research Operations | 1 | Research Knowledge Base (`research-knowledge-base.html?from=research-operations`) | verbatim from [index.html L431] | |
| Consumer Research | 1 | Experian Virtual Assistant (`experian-eva.html?from=consumer-research`) | verbatim from [index.html L438] | |
| Consumer Research | 2 | HP Wolf Security (`hp-wolf-security.html?from=consumer-research`) | verbatim from [index.html L461] | |

### 5.4 Impact (S-04, optional)

| Page | Stats (number / label) | Source |
|---|---|---|
| AI Evaluations | **omitted** (no sourced evaluation numbers exist; Flag O5) | |
| Research Operations | `2.3K+` / `Findings coded`; `30+` / `Teams supported`; `Weeks → hours` / `Cross-team topic review` | [index.html L472-473]; [case:research-knowledge-base.html] section 06 "went from weeks to hours" |
| Consumer Research | `24+` / `Products launched`; `1.5K+` / `Voices heard`; `30+` / `Teams supported` | [index.html L471, L473-474] |

### 5.5 Experience bullet order (S-05)

Org names, titles, dates, the Experian intro paragraph, and the HP and Freelance roles are byte-identical to [index.html L484-537]. Only the order of the five Experian bullets changes. Bullets, verbatim from [index.html L497-501]:

- **E1** `Rebuilt research operations over about two years: self-service access for stakeholders, research standards, onboarding, and mentoring.`
- **E2** `Led research on integrating generative AI into the consumer experience; recommendations shaped Experian's educational tools.`
- **E3** `Introduced AI-assisted screening, analysis, and synthesis, and set the standards for where a model is trusted and where a person decides.`
- **E4** `Helped define Experian's internal Applied AI practices, and work closely with the Applied AI team on pilot projects: a research knowledge base, a PMO agent, and skill kits. Also built PII-stripping preprocessing tools and competitor monitoring.`
- **E5** `Partner with design, engineering, and product teams, translating findings into roadmaps and design decisions.`

| Page | Order |
|---|---|
| AI Evaluations | E3, E2, E4, E1, E5 |
| Research Operations | E1, E4, E3, E5, E2 |
| Consumer Research | E5, E2, E3, E1, E4 |

### 5.6 Methods board (S-06)

Existing clusters and chips are copied verbatim from [index.html L549-588]: **Generative** (7), **Evaluative** (6), **Quantitative** (6), **Operations** (6).

The AI Evaluations page adds one new cluster, **Evaluation**, with four chips that are each evidenced on the site today:

| Chip | Description | Source |
|---|---|---|
| `LLM-as-a-judge` | `A model makes the call when it safely can, inside fixed human checkpoints, and a person steps in when it can't.` | [case:research-knowledge-base.html] section 03 |
| `Human-in-the-loop review` | `Researcher sign-off and manager approval before anything a model produced is released.` | [case:research-knowledge-base.html] section 03 |
| `Model trust standards` | `Written rules for where a model is trusted and where a person decides.` | [index.html L499] |
| `Evaluating AI with users` | `Testing a generative AI assistant with real people across live builds, competitors, and prototypes.` | [case:experian-eva.html] section 02 |

| Page | Clusters, in order | Chip total |
|---|---|---|
| AI Evaluations | Evaluation (4), Evaluative (6), Quantitative (6), Operations (6) | 22 |
| Research Operations | Operations (6), Generative (7), Evaluative (6), Quantitative (6) | 25 |
| Consumer Research | Generative (7), Evaluative (6), Quantitative (6), Operations (6) | 25 |

More evaluation chips (rubric design, golden datasets, pairwise comparison, red-teaming, judge validation) are evidenced only in Nick's private practice repo [evals-reps], not on the site. They are added only if Nick confirms (Flag O4).

### 5.7 Tools (S-07, optional)

| Page | Tools | Source |
|---|---|---|
| AI Evaluations | **omitted** until Nick confirms a list (Flag O4; [evals-reps] shows promptfoo and LangSmith, [resume.html] lists Python) | |
| Research Operations | Condens, Dovetail, Great Question, User Interviews, Ethnio, TheyDo, Jira, Miro, FigJam | subset of [index.html L598-604]; the subset is my choice (assumption) |
| Consumer Research | the full [index.html L598-604] list, same order | |

## 6. Case studies: mapping, gaps, content plan

### 6.1 Mapping

| Case study | State | AI Evaluations | Research Operations | Consumer Research |
|---|---|---|---|---|
| Research Knowledge Base | complete | **yes** (LLM-as-a-judge gate, human fallback) | **yes** (primary) | no |
| Experian Virtual Assistant | complete | **yes** (user evaluation of a generative AI product) | no | **yes** (primary) |
| HP Wolf Security | complete | no | no | **yes** |
| Research PMO Agent | draft, 7 markers | no | later, once complete | no |
| Skill Kits | draft, 7 markers | later, once complete (AI guardrails angle) | later, once complete | no |

### 6.2 Gaps (known, not filled with invented work)

- **AI Evaluations has no case study of a structured model evaluation** (eval set, rubric, judge validation, regression check). Both cards on that page are adjacent evidence: an LLM-as-a-judge gate in a pipeline and user research on an AI product. A hiring manager screening for eval engineering will read the page that way. The strongest candidate for a real eval case study is Nick's own practice work in [evals-reps]: promptfoo evals of his Hermes agent profiles with an independent judge, 3x repeats, and a before/after check of a routing fix (week 3: 11/14 passed, with real findings). It is personal practice, not employer work, so whether and how to feature it is Nick's call (Flag O1).
- **Research Operations has one complete case study.** PMO Agent and Skill Kits are drafts with `[Nick to add]` markers and stay unlinked until Nick fills them. The two-year ops rebuild (standards, onboarding, mentoring) [index.html L497] has no case study.
- **Consumer Research is the best covered** (two complete cases). Freelance work (travel, health and wellness, personal organization) has no case study. No gap needs filling before launch.
- No discipline gets a "coming soon" card. An empty slot reads as weakness to a recruiter; a short page reads as focus.

### 6.3 Content plan per page

- **Pattern:** keep the current one: a card on the landing page links to a full case-study page. No inline case sections on landing pages.
- **One canonical page per project.** A project that serves two disciplines (Knowledge Base, EVA) keeps one case-study page; the landing-page card blurb carries the discipline angle (5.3). No duplicated case pages per discipline.
- **Count:** 1 to 4 cards per page. At launch: AI Evaluations 2, Research Operations 1, Consumer Research 2.
- **Back links know where the visitor came from:** cards link with `?from=<slug>`, and the case page's back link returns to that discipline page (R10).
- **A case page is linked only when it is complete** (zero `[Nick to` markers, R9).
- **Growth path** (follow-ups, section 16): an AI eval case study from [evals-reps] (Flag O1), then PMO Agent and Skill Kits once Nick fills them.

## 7. nickpings.com homepage: explicit follow-up, out of scope

Nick: "Nickpings.com will still need a homepage, but we can figure that out later." This PRD does **not** design it. Until a separate homepage card decides, `index.html` stays byte-identical and keeps serving the bare domain (R17).

Questions the homepage card must answer (none decided here):

1. How does a visitor on the bare domain choose or get routed between the three disciplines?
2. Does `index.html` become that homepage (edited), or get replaced, or stay as a fourth "generalist" page?
3. Does `intro.html` factor in (first-visit routing per [BACKLOG] L33, a "Replay intro" easter egg per [BACKLOG] L34, a link, or nothing)?
4. Where does "Back to portfolio" on case pages point by default once the homepage changes (today: `index.html`, R10)?
5. Does the switcher's name become a link to the homepage (today: plain text, R4)?
6. Does `index.html` move onto the shared stylesheet (today: it keeps its inline CSS, R14)?

Consequence for the interim: the current homepage does not link to the three new pages. They are reachable by direct link (which is how job applications reach them) and from each other. If Nick wants a temporary link from `index.html` before the homepage card, that is a one-line edit he can approve separately (Flag O2).

## 8. intro.html: recommendation (Nick to confirm)

**Recommendation: keep `intro.html` live and unchanged as a standalone personality piece at `nickpings.com/intro`, outside the job-application path.** Specifically:

- The three discipline pages and the case pages do **not** link to it, and never redirect to it (R18). A recruiter opening `/ai-evaluations` from an application must land on the evaluation page every time.
- It is **not retired.** Its in-progress branches (research, technology, passions) stay where they are, and its blue pill keeps pointing at `index.html`, which still exists.
- If the [BACKLOG] L33 first-visit routing is ever built, it may only apply to the bare domain, never to the discipline pages (R18 edge case).
- Whether it becomes the homepage's front door, an easter egg, or a footer link is decided in the homepage card (section 7, Q3).

Why: Nick called it "fun" and said the portfolio needs to "think more broadly" than it. A hiring manager arriving from an application wants evidence fast; a scroll-driven intro in front of that costs attention. As a separate page it keeps its value (personality, craft) without gating the work. Flag O6 asks Nick to confirm or pick another fate.

## 9. Technical approach: files and shared assets

**Platform choice:** responsive static web, the first stop in the cheapest-first order (tech-viability skill, section 2). Nothing here needs native capability, a framework, or a build step. Nick's constraint is "static HTML, no build step" [Card] item 7.

New files (all at repo root unless noted):

| File | Purpose | Used by |
|---|---|---|
| `ai-evaluations.html`, `research-operations.html`, `consumer-research.html` | The three landing pages: markup only, no inline `<style>` or `<script>` blocks (except the `<noscript><style>` fallback) | |
| `assets/css/site.css` | Everything a landing page needs, copied from [index.html L13-363]: the `:root` tokens (unchanged), base type, hero, bands, facets, case cards, marquee, roles, sort board, debrief, footer, observer, reduced-motion rules, plus the new `.foot-cross` line | 3 landing pages |
| `assets/css/disc-nav.css` | The switcher only, self-contained: uses `var(--pine, #2F5B44)` style fallbacks so it works on case pages, whose inline CSS defines the same token names | 3 landing pages and 5 case pages |
| `assets/js/site.js` | Copied from [index.html L646-877] and generalized: methods scatter and sort, marquees, one-open roles, observer, debrief, with every count read from the DOM | 3 landing pages |
| `assets/js/back-link.js` | Under 20 lines: reads `?from=`, and if it is one of the three slugs, points both back links at that page | 5 case pages |

Why this split: three landing pages would otherwise carry three copies of about 350 lines of CSS and 230 lines of JS, and the next tweak would have to land three times. Plain `<link>` and `<script src>` need no build step and GitHub Pages serves them as-is. The switcher markup itself is static HTML repeated in each page (about 10 lines), not injected by JS, so it renders with JS off and without a flash; R4 checks the copies stay identical.

What is deliberately **not** refactored here: `index.html` keeps its inline CSS and JS (it belongs to the homepage card), `intro.html` is untouched, `resume.html` is untouched, and the case pages keep their own inline CSS and only gain the switcher, the back-link script and a colophon line (R10).

---

## 10. Requirements

Every requirement's verification runs on branch `feature/portfolio-restructure` against the local server `python3 docs/tools/serve.py 8000` from the repo root, in Chromium driven over CDP (the Browser Use helper on this Mac). Viewports: desktop `Emulation.setDeviceMetricsOverride(width=1440,height=900,deviceScaleFactor=1,mobile=false)`, mobile `(width=390,height=844,deviceScaleFactor=3,mobile=true)`. Reduced motion: `Emulation.setEmulatedMedia(features=[{name:"prefers-reduced-motion",value:"reduce"}])`. No JS: `Emulation.setScriptExecutionDisabled(value=true)`. "JS check" means `js(...)` on `http://localhost:8000/<file>`. `$PAGES` means `ai-evaluations research-operations consumer-research`; `$CASES` means `experian-eva hp-wolf-security research-knowledge-base research-pmo-agent skill-kits`.

Build/deployment for **every** requirement: not Docker, by the static-site exception in section 11. No requirement adds a container, service, process or dependency beyond the local preview server.

### R1. The three discipline pages exist as flat files at the repo root, named per section 3.
- **Source:** [Nick] "three landing pages with their own URLs, case studies, etc, that I can point job apps at"; [Card] items 2 and 7; ADR 0001; [Probe] P1, P2.
- **Acceptance:** `for p in $PAGES; do test -f $p.html || echo MISSING $p; done` prints nothing; `ls -d ai-evaluations research-operations consumer-research 2>&1 | grep -vc "No such"` prints `0` (no folders of those names); each page loads at `http://localhost:8000/<slug>.html` with HTTP 200. After Nick approves and the branch reaches `main`: `curl -s -o /dev/null -w "%{http_code}" https://nickpings.com/<slug>` returns `200` for each slug.
- **Edge cases:** `nickpings.com/<slug>/` (trailing slash) returns 404 on Pages; that is expected and Nick shares the no-slash form (Flag O3). Uppercase paths are not supported. The local server does not resolve extensionless paths, so local checks always use `.html`. No `index.html` inside a folder.
- **Resources:** `ai-evaluations.html`, `research-operations.html`, `consumer-research.html` (new).

### R2. Each page follows the section 2 formula in order, omits only the optional sections section 5 omits, and numbers its section codes without gaps.
- **Source:** [Nick] "following the same formula that our current portfolio index page shows"; [Card] item 1; section 2.
- **Acceptance:** JS check per page: `[...document.querySelectorAll('main > header, main > section')].map(e => e.id)` equals: ai-evaluations `["top","philosophy","practice","selected-work","work","methods","debrief"]`; research-operations and consumer-research `["top","philosophy","practice","selected-work","impact","work","methods","tools","debrief"]`. `[...document.querySelectorAll('.sec-code')].map(e => e.textContent)` equals `S-01` to `S-06` (ai-evaluations) or `S-01` to `S-08` (the other two), in order. Every `main > section` has a `data-obs` attribute. Exactly one `main`, one `footer.foot`, one `aside#observer` per page.
- **Edge cases:** an omitted section is absent from the DOM, not hidden with CSS (`document.getElementById('impact') === null` on ai-evaluations); the Observer's coverage line counts only sections present; no empty `<section>` shells.
- **Resources:** the 3 landing pages.

### R3. Each hero has the shared name and session pill and the per-page eyebrow and thesis from section 5.1.
- **Source:** [index.html L373-380]; section 5.1 table and its cited sources.
- **Acceptance:** JS check per page: exactly one `h1`, `h1.name` text normalized for whitespace equals `Nicholas Pings Rodriguez.` and its `.dot` computed color is `rgb(126, 156, 96)`; `.hero .eyebrow` text equals the 5.1 eyebrow; `.thesis` `textContent` normalized equals the 5.1 thesis without brackets, and `.thesis .mark` text equals the bracketed part; `.session-pill` text contains `Session in progress`.
- **Edge cases:** the thesis must not wrap the period onto its own line at 320px wide (no horizontal overflow, R19); with no JS the `.mark` highlight is fully drawn (the `<noscript>` rule from [index.html L366] is kept); copy changes go through this PRD's table, not straight into HTML.
- **Resources:** the 3 landing pages; `assets/css/site.css`.

### R4. Every landing page opens with the same discipline switcher, with the current page marked.
- **Source:** [Card] item 3 "a visible way to jump between the 3 discipline pages so a visitor lands on one and can see the others exist"; section 4 device 2.
- **Acceptance:** JS check per page: the first element child of `.page` is `nav.disc-nav` with `aria-label="Research disciplines"`; it contains the text `Nicholas Pings Rodriguez` (not a link: `nav.disc-nav .disc-name` is a `span`), the label `Research in`, and exactly three `a[href]` whose `getAttribute('href')` values are, in order, `ai-evaluations.html`, `research-operations.html`, `consumer-research.html`, with texts `AI Evaluations`, `Research Operations`, `Consumer Research`; exactly one link has `aria-current="page"` and it is the page's own file; the current link's computed style differs from the others (e.g. `textDecorationLine` or `fontWeight`). Markup is identical across pages: `python3 -c "import re,sys;n=[re.sub(r' aria-current=\"page\"','',re.search(r'<nav class=\"disc-nav\".*?</nav>',open(f+'.html').read(),re.S).group(0)) for f in sys.argv[1:]];print(len(set(n)))" $PAGES $CASES` prints `1`. At 390x844 each switcher link's bounding box is at least 44px tall; at 320x568 `document.documentElement.scrollWidth <= innerWidth`.
- **Edge cases:** works with JS disabled (plain links); no hamburger, dropdown or sticky positioning; keyboard Tab reaches the three links first, in order, each with a visible `:focus-visible` outline; the name is not a link until the homepage card decides (section 7, Q5).
- **Resources:** the 3 landing pages; `assets/css/disc-nav.css` (new).

### R5. The footer is identical on all three pages, matches today's contact block, and cross-links the other two disciplines.
- **Source:** [index.html L622-631]; section 4 devices 5 and 6.
- **Acceptance:** `python3 -c "import re,sys;g=lambda f:re.search(r'<div class=\"foot-grid\">.*?</div>\s*</div>',open(f).read(),re.S).group(0);print(len({g(f) for f in sys.argv[1:]}))" index.html ai-evaluations.html research-operations.html consumer-research.html` prints `1`; each page's `.colophon` text equals index.html's; JS check: `footer .foot-cross` text starts with `Same research, other angles:` and contains exactly two links, the two disciplines other than the current page, in section 3 order; the resume link `href` is `resume.html`.
- **Edge cases:** the `mailto:` and `tel:` links are unchanged from index.html; there is one resume for all three (a per-discipline resume is Flag O7, not built); the cross-link line wraps cleanly at 320px.
- **Resources:** the 3 landing pages; `index.html` (read-only reference).

### R6. Philosophy is word-for-word the same on all three pages and on `index.html`.
- **Source:** section 4 device 3; [index.html L382-396]; [Nick] "The common thread among all of these fields is that they are fundamentally research disciplines."
- **Acceptance:** `python3 -c "import re,sys;g=lambda f:re.sub(r'\s+',' ',re.search(r'id=\"philosophy\".*?</section>',open(f).read(),re.S).group(0));print(len({g(f) for f in sys.argv[1:]}))" index.html ai-evaluations.html research-operations.html consumer-research.html` prints `1`.
- **Edge cases:** the section code may differ only if Philosophy ever stops being S-01 (it does not on any page today); no discipline-specific sentence is appended.
- **Resources:** the 3 landing pages.

### R7. Practice shows the four existing facets with unchanged text, in the per-page order of section 5.2.
- **Source:** [index.html L398-420]; section 5.2.
- **Acceptance:** JS check per page: `[...document.querySelectorAll('#practice .facet > .label')].map(e => e.textContent)` equals the 5.2 order using the P1-P4 titles; for each facet, the following `p` text equals the text of the facet with the same label in index.html.
- **Edge cases:** exactly four facets on every page; no new facet text without a PRD amendment.
- **Resources:** the 3 landing pages.

### R8. Selected work shows exactly the cards in section 5.3, in order, with discipline-tagged links and the listed blurbs.
- **Source:** [Card] item 4; section 6.3; section 5.3 table and its sources.
- **Acceptance:** JS check per page: `[...document.querySelectorAll('#selected-work a.case-card')].map(a => [a.querySelector('h3').textContent, a.getAttribute('href')])` equals the 5.3 rows for that page; each card's `p` text equals the 5.3 blurb; card count is between 1 and 4; `grep -c "<!--" <page>.html` prints `0` (no commented-out cards or other HTML comments).
- **Edge cases:** following a card lands on the case page with `?from=<slug>` preserved (`location.search === "?from=<slug>"`); Cmd/Ctrl-click opens a new tab (plain `<a>`, no JS handler); a single-card grid (research-operations) does not stretch the card to a broken width at 1440px (card width at most 50% of `.cases` width, or the grid's normal single-column width).
- **Resources:** the 3 landing pages; the 3 linked case pages (read targets).

### R9. No landing page shows or links placeholder content.
- **Source:** [Card] item 4 "flag it as a known gap rather than inventing fake work"; [Probe] P4 (7 markers each in PMO Agent and Skill Kits).
- **Acceptance:** `grep -ciE "\[Nick to|coming soon|lorem|TBD" ai-evaluations.html research-operations.html consumer-research.html` prints `0` for each file; for every case page linked from any landing page, `grep -c "\[Nick to" <case>.html` prints `0`; `grep -cE "research-pmo-agent|skill-kits" ai-evaluations.html research-operations.html consumer-research.html` prints `0` for each.
- **Edge cases:** when Nick completes PMO Agent or Skill Kits, adding them is a PRD amendment to 5.3 plus this check passing; the gaps in section 6.2 are documented here and in BACKLOG, never on the live pages.
- **Resources:** the 3 landing pages; `research-pmo-agent.html`, `skill-kits.html` (read-only).

### R10. Each case page gains the switcher, a back link that returns to the referring discipline, and a neutral colophon, and nothing else changes.
- **Source:** [Card] item 3 (switcher on every page); section 6.3; [case:*] current `← Back to portfolio` links to `index.html`.
- **Acceptance:** for each of `$CASES`: (a) the same `nav.disc-nav` as R4, with no `aria-current`, is the first element inside the page wrapper, before `a.back`; `<link rel="stylesheet" href="assets/css/disc-nav.css">` and `<script src="assets/js/back-link.js" defer></script>` are present. (b) In the static HTML both back links (top `a.back` and the `footer.case-foot` link) still have `href="index.html"` and text `Back to portfolio`. (c) JS check on `experian-eva.html?from=ai-evaluations`: both back links' `getAttribute('href') === "ai-evaluations.html"` and text normalized equals `← Back to AI Evaluations`; same pattern for `research-operations` (`Back to Research Operations`) and `consumer-research` (`Back to Consumer Research`). (d) On `?from=evil`, `?from=`, no query, and with JS disabled: `href === "index.html"`, text `← Back to portfolio`. (e) `.case-foot .colophon` text is `Nicholas Pings Rodriguez · Research`. (f) `git diff main -- <case>.html | grep '^-[^-]' ` shows only the old colophon line.
- **Edge cases:** `?from=` values are matched against a fixed allowlist of the three slugs, never written into the page as HTML (no `innerHTML`, no open redirect: `grep -c innerHTML assets/js/back-link.js` = 0); extra query params (`?from=consumer-research&utm_source=x`) still work; `research-self-service.html` is not edited (it redirects); case-page inline CSS is not touched, so its look is unchanged apart from the nav.
- **Resources:** `experian-eva.html`, `hp-wolf-security.html`, `research-knowledge-base.html`, `research-pmo-agent.html`, `skill-kits.html` (edited); `assets/js/back-link.js` (new); `assets/css/disc-nav.css`.

### R11. Experience shows the same three roles as `index.html`, with titles and dates unchanged and only the Experian bullet order per section 5.5.
- **Source:** [index.html L479-541]; [resume.html]; section 5.5.
- **Acceptance:** JS check per page: `.role-org`, `.role-title` and `.role-when` texts equal index.html's, in the same order; the Experian `li` texts equal the 5.5 order of E1-E5, verbatim; the HP and Freelance `role-body` innerHTML equals index.html's after whitespace normalization; every `details.role` is closed on load and opening one closes the others.
- **Edge cases:** no job title, employer name or date is reworded to suit a discipline (a hard non-goal); with JS off, the `details` still open and close natively; no bullet appears that is not in E1-E5.
- **Resources:** the 3 landing pages; `assets/js/site.js`.

### R12. The methods board shows the clusters and chips of section 5.6, with correct counts.
- **Source:** [index.html L543-592]; section 5.6 table and its sources.
- **Acceptance:** JS check per page: `[...document.querySelectorAll('#methods .cluster-head .label')].map(e => e.textContent)` equals the 5.6 cluster order; for each cluster, `.n` text equals its number of `details.chip`; total `details.chip` equals 22 (ai-evaluations) or 25 (the others); every chip name and description outside the Evaluation cluster equals index.html's text for that chip; the Evaluation cluster's four chips match the 5.6 table verbatim. After scrolling `#board` into view and waiting 1500ms, `#board` has class `sorted`.
- **Edge cases:** with reduced motion or no JS the board renders already sorted and fully opaque (index.html L355, L365 rules kept); no chip appears in two clusters; no evaluation chip beyond the four is added without Flag O4.
- **Resources:** the 3 landing pages; `assets/js/site.js`.

### R13. Impact and Tools show only the sourced items of sections 5.4 and 5.7, and are absent where the table says omitted.
- **Source:** sections 5.4 and 5.7 and their sources; [Card] item 4 "rather than inventing fake work".
- **Acceptance:** JS check: on ai-evaluations, `#impact` and `#tools` are `null`; on research-operations, the first copy of the `.track-impact` stats (before the marquee duplicates them) is `[["2.3K+","Findings coded"],["30+","Teams supported"],["Weeks → hours","Cross-team topic review"]]` and the tool names, deduplicated in order, equal the 5.7 list; on consumer-research, stats equal the 5.4 row and tools equal index.html's list. Check against the static HTML before JS runs: `curl -s localhost:8000/<page>.html` and parse, since the marquee repeats items.
- **Edge cases:** a three-item marquee still loops with no visible gap at 1440px (the existing repeat-until-wide logic, [index.html L673-682]); under reduced motion the marquee does not move and every item is still readable (wrapping or scrollable, no clipped text); no number appears that is not in a cited source.
- **Resources:** the 3 landing pages; `assets/js/site.js`.

### R14. Landing pages get all their styling from the shared stylesheets, with tokens and fonts unchanged from `index.html`.
- **Source:** [Card] item 7 "avoid duplicating CSS/fonts three times, while keeping it simple given the no-build-step constraint"; section 9.
- **Acceptance:** for each landing page: `grep -c "<style" <page>.html` prints `1` (the `<noscript><style>` fallback only); `grep -c 'href="assets/css/site.css"' ` and `grep -c 'href="assets/css/disc-nav.css"'` each print `1`; the Google Fonts `<link>` href is byte-identical to [index.html L12]. `diff <(sed -n '/:root{/,/}/p' index.html) <(sed -n '/:root{/,/}/p' assets/css/site.css)` prints nothing. No color outside index.html's own stylesheet: `comm -23 <(grep -ohiE "#[0-9a-f]{3,6}\b" assets/css/site.css assets/css/disc-nav.css | tr a-f A-F | sort -u) <(sed -n '/<style>/,/<\/style>/p' index.html | grep -oiE "#[0-9a-f]{3,6}\b" | tr a-f A-F | sort -u)` prints nothing (today that set is the ten `:root` tokens plus `#7E9179`, `#E6EDE0` and `#000` [Probe]). `git diff main --stat -- index.html intro.html resume.html` is empty.
- **Edge cases:** CSS path is relative (`assets/css/...`), so it also works from a local file server and any future subpath; if `site.css` fails to load the page is still readable in document order (no content hidden by default except `.rise`, which the `<noscript>` rule and a reduced-motion rule reveal); no `@import`, no CSS framework, no locally hosted fonts.
- **Resources:** `assets/css/site.css`, `assets/css/disc-nav.css` (new); the 3 landing pages.

### R15. The shared script runs the formula's behaviors on any page, reads every count from the DOM, and stores and sends nothing.
- **Source:** [index.html L646-877]; section 4 device 4; [index.html L618] "stored nowhere, and disappears when you leave".
- **Acceptance:** each landing page has exactly one `<script` tag, `<script src="assets/js/site.js" defer></script>`. `grep -cE "localStorage|sessionStorage|document\.cookie|fetch\(|XMLHttpRequest|sendBeacon|location\.(href|assign|replace)" assets/js/site.js` prints `0`. `grep -cE "/ 25|of 25|All 25|' / 3'|of 3 |Three to choose|Four principles" assets/js/site.js` prints `0`. JS check on ai-evaluations after load: `#dMethods` text is `0 / 22` and `#dRoles` text is `0 / 3`; open one chip, `#dMethods` becomes `1 / 22`; scroll `#selected-work` into view, the observer log gains `Participant reaches the case studies. Two to choose from.` (number word from the card count: One, Two, Three, Four); scroll to the bottom, the debrief line reads `Coverage: N of 7 sections reached.` with 7 equal to `document.querySelectorAll('[data-obs]').length`. On research-operations the case-studies line says `One to choose from.`
- **Edge cases:** a page missing `#impact` or `#tools` runs without console errors (CDP `Runtime.exceptionThrown` count is 0 after a full scroll on every page); the observer works the same at 390px; reduced motion stops the rec dot and marquees; nothing is written to storage (`localStorage.length` and `sessionStorage.length` stay 0 after a full session).
- **Resources:** `assets/js/site.js` (new); the 3 landing pages.

### R16. Each page has a complete head, including a canonical URL and link-preview tags.
- **Source:** [Nick] "that I can point job apps at" (links get pasted into ATS forms and LinkedIn, which render previews); [index.html L5-9]; section 5.1.
- **Acceptance:** per page: `<title>` and `<meta name="description">` equal section 5.1; `<link rel="canonical" href="https://nickpings.com/<slug>">`; `og:title` equals the title, `og:description` equals the description, `og:url` equals the canonical, `og:type` is `website`; the viewport and color-scheme meta tags are byte-identical to [index.html L5-7]; `<html lang="en">`.
- **Edge cases:** canonical and `og:url` use the extensionless form, no trailing slash; no `og:image` (no approved image exists; Flag O8); no `noindex`.
- **Resources:** the 3 landing pages.

### R17. The homepage and every existing URL stay exactly as they are.
- **Source:** [Nick] "Nickpings.com will still need a homepage, but we can figure that out later"; [Card] item 5; section 7.
- **Acceptance:** `git diff --name-only main...feature/portfolio-restructure` lists only: the 3 landing pages, `assets/css/site.css`, `assets/css/disc-nav.css`, `assets/js/site.js`, `assets/js/back-link.js`, the 5 case pages from R10, `README.md`, `BACKLOG.md`, and files under `docs/`. `git diff main -- index.html intro.html resume.html research-self-service.html CNAME AGENTS.md` is empty. Every URL in the section 1 table still returns 200 on the local server.
- **Edge cases:** no redirect at the root, no `404.html`, no `CNAME` change; `README.md` only gains a list of the three pages; any change to `index.html` waits for the homepage card.
- **Resources:** whole repo (read-only except the files listed).

### R18. Discipline pages and case pages never link to or redirect into `intro.html`.
- **Source:** [Nick] "The intro is fun... but we need to think more broadly"; [Card] item 6; section 8 recommendation (pending Flag O6).
- **Acceptance:** `grep -c "intro" ai-evaluations.html research-operations.html consumer-research.html assets/js/site.js assets/js/back-link.js` prints `0` for each; `grep -ciE 'http-equiv="refresh"' ai-evaluations.html research-operations.html consumer-research.html` prints `0`; `git diff main -- intro.html` is empty; JS check: loading each landing page and waiting 5000ms leaves `location.pathname` unchanged.
- **Edge cases:** if the [BACKLOG] first-visit routing is ever built, it must not run on these pages (a later homepage card restates this); the word "intro" may appear in body copy only if a PRD amendment allows it.
- **Resources:** the 3 landing pages; `intro.html` (read-only).

### R19. Every landing page works at phone and desktop sizes, with reduced motion, with no JS, and by keyboard.
- **Source:** [index.html] responsive and reduced-motion rules (L350-362); assumption that the new pages meet the same bar as the current one.
- **Acceptance:** at 1440x900, 768x1024, 390x844 and 320x568: `document.documentElement.scrollWidth <= innerWidth` on all three pages. With reduced motion: `document.getAnimations().filter(a => a.playState === "running" && a.effect.getComputedTiming().iterations === Infinity).length === 0`. With JS disabled: every `main > section` has computed opacity `1`, all case-card links and switcher links are present, and the `.observer`, `.session-pill` and `.debrief` elements are `display:none` (the [index.html L367] rule). Keyboard: from load, Tab order starts with the three switcher links, then the case cards; every focusable element shows an outline on `:focus-visible`.
- **Edge cases:** the observer panel does not cover the footer's contact links at 390px when collapsed (its bounding box does not intersect `.foot-grid` links at full scroll, or the panel is collapsible to a size that clears them); landscape phone (844x390) has no horizontal overflow; long thesis lines wrap without clipping.
- **Resources:** the 3 landing pages; `assets/css/site.css`; `assets/js/site.js`.

---

## 11. Deployment and build

**Not Docker, by justified exception.** Nick's standing rule is Docker for every project except homelab and agent-town. This site is static files on GitHub Pages: no server process, runtime or dependency exists to containerize, and production deploy is a merge to `main`, which needs Nick's approval. This is the same exception `docs/intro-experience-PRD.md` section 8 documents for this repo.

- **Local preview:** `python3 docs/tools/serve.py 8000` from the repo root on `feature/portfolio-restructure` (byte-range server already in the repo). Demo URLs: `http://localhost:8000/ai-evaluations.html`, `.../research-operations.html`, `.../consumer-research.html`.
- **Build step:** none. HTML files plus two CSS and two JS files referenced by relative path.
- **Production:** nothing ships from this card or the build cards. After Nick approves the built pages, a merge to `main` publishes them at the section 3 URLs.
- If Nick wants the preview containerized anyway: `docker run --rm -p 8000:80 -v "$PWD":/usr/share/nginx/html:ro nginx:alpine` (nginx would also resolve extensionless paths only with a `try_files` rule, so local checks stay on `.html`).

## 12. Feasibility (spike method) and risks

| # | Given / When / Then | Verdict | Evidence |
|---|---|---|---|
| P1 | Given a flat `name.html` on GitHub Pages, when someone opens `nickpings.com/name`, then Pages serves it. | VALIDATED | `curl` 2026-11-17: `/resume` 200 (serves the resume page), `/experian-eva` 200, `/intro` 200. |
| P2 | Given the same, when the URL has a trailing slash, then it still resolves. | INVALIDATED (expected) | `/resume/` 404, `/experian-eva/` 404. Share the no-slash form. |
| P3 | Given a case page, when the URL carries `?from=<slug>`, then Pages serves the page normally. | VALIDATED | `/experian-eva.html?from=ai-evaluations` 200 and `/experian-eva?from=ai-evaluations` 200. |
| P4 | Given the hidden case studies, when checked for unfinished content, then they are not linkable yet. | VALIDATED | `grep -c "\[Nick to"`: `research-pmo-agent.html` 7, `skill-kits.html` 7, all others 0. |
| P5 | Given case pages keep their inline CSS, when a shared `disc-nav.css` uses token names, then the tokens resolve. | VALIDATED | `experian-eva.html` `:root` defines `--paper` to `--leaf` and `--pad`, same names and values as index.html (no `--rec`); `disc-nav.css` adds hex fallbacks anyway (R14). |
| P6 | Given the index.html script, when it runs on a page with fewer sections or chips, then it works. | PARTIAL | Read [index.html L646-877]: section and marquee logic are already data-driven; `/ 25`, `/ 3`, "Three to choose from" and "Four principles" are hard-coded literals. R15 requires reading them from the DOM. |

No AI/LLM component is built, so the AI three-dimension check does not apply.

Risks:

- **Biggest risk: the AI Evaluations page is the thinnest, in the discipline where Nick is pushing hardest.** Two adjacent case studies, no impact numbers, no tools. A hiring manager for eval roles screens for building and validating judges and regression checks, and these cards don't show that. Mitigation: Flag O1 (write up the [evals-reps] work as a case study before pointing eval applications at the page).
- **Research Operations ships with one case study** until PMO Agent or Skill Kits are finished.
- **Slugs are permanent once shared** (ADR 0001). Decide O3 before the first application goes out.
- **Interim discoverability:** the current homepage doesn't link to the new pages until the homepage card (Flag O2). Direct links work regardless.
- **Copy drift:** three pages repeat the switcher, footer and Philosophy. R4, R5 and R6 check the copies match, so drift fails review instead of shipping.
- **Two sources of the design system** until the homepage card: `index.html` inline and `site.css`. A token change must land in both until `index.html` moves over (section 7, Q6).

## 13. Non-goals (do not build)

- The nickpings.com homepage: any change to `index.html`, a root redirect, a chooser page, or routing logic (section 7).
- Any change to `intro.html`, a link to it, first-visit detection, or a "Replay intro" control (section 8).
- New case studies, new case-study content, or filling the `[Nick to add]` markers in PMO Agent or Skill Kits.
- Duplicate case-study pages per discipline, or inline case sections on landing pages.
- Per-discipline resumes, or any edit to `resume.html`.
- Rewording job titles, employers, dates or any claim to suit a discipline; new stats, tools or methods not in section 5.
- Per-discipline color themes, dark mode, new fonts, new tokens.
- A JS-injected header or footer, a templating step, a static-site generator, `package.json`, `node_modules`, or any CDN script.
- Analytics, tracking, cookies or storage of any kind; the Observer stays local-only.
- `og:image` or social-card artwork, favicon changes, sitemap, `robots.txt`, `404.html`.
- Moving existing pages into folders or renaming any existing file.
- Opening a PR to `main`, merging, or pushing to `main`.

**Authorized boundaries (build cards):** create the 3 landing pages and the 4 asset files in section 9; make the R10 edits to the 5 case pages; add the three pages to `README.md`; add rows to `BACKLOG.md` (merge, never overwrite); commit on `feature/portfolio-restructure` and `git push origin feature/portfolio-restructure`; run the local preview server.

**Forbidden actions:** editing `index.html`, `intro.html`, `resume.html`, `research-self-service.html`, `CNAME`, `AGENTS.md` or anything under `assets/passions/`; committing to, pushing to or merging into `main`; adding dependencies, containers or always-on services.

## 14. Flags for Nick (open questions to confirm before design and build)

1. **O1. AI evals case study.** The AI Evaluations page has no case study of a real model evaluation. Your `ai-evals-reps` work (promptfoo evals of your own agent profiles, independent judge, repeats, a before/after fix check) is the strongest candidate. Do you want it written up as a case study (personal project, clearly labeled), and should eval applications wait for it?
2. **O2. Interim homepage link.** Until the homepage card, `index.html` won't link to the new pages. Fine as-is (direct links only), or approve a one-line temporary link?
3. **O3. Slugs.** `ai-evaluations`, `research-operations`, `consumer-research`. The main alternative is `ux-research` for the third. These are permanent once in applications. Confirm or change.
4. **O4. AI evals methods and tools.** I added only four evaluation chips that the site already evidences, and left Tools off that page. Want rubric design, golden datasets, pairwise comparison, red-teaming or judge validation as chips, and promptfoo, LangSmith or Python as tools? They're backed by `ai-evals-reps`, not by anything on the site yet.
5. **O5. AI evals impact numbers.** No sourced numbers exist, so the page has no Impact strip. Any you can stand behind?
6. **O6. intro.html.** My recommendation is to keep it live at `/intro`, unlinked from the discipline pages, and decide its role in the homepage card. Confirm, or pick another fate (homepage front door, easter egg, retire).
7. **O7. One resume or three?** All pages link the same `resume.html` ("Consumer Products & Research Operations"). Angled resumes per discipline would be a separate card.
8. **O8. Link previews.** Pages get title and description previews but no image. Want a share image made later?
9. **O9. Draft copy.** Theses, descriptions and two AI-evals card blurbs in section 5 are my wording, built from your existing text. Edit freely before build.
10. **Docker exception.** Static GitHub Pages, so no container (section 11), same as the intro PRD.

No ongoing cost, no new services, no recurring manual steps.

## 15. Resources touched (summary)

New: `ai-evaluations.html`, `research-operations.html`, `consumer-research.html`, `assets/css/site.css`, `assets/css/disc-nav.css`, `assets/js/site.js`, `assets/js/back-link.js`. Edited: the 5 case pages (R10), `README.md`, `BACKLOG.md`. Read-only: `index.html`, `intro.html`, `resume.html`, `research-self-service.html`. Profiles: `design` or the build lane PMO picks; Crit for review.

## 16. Follow-ups (not requirements; for BACKLOG.md when the build lands)

This card was told not to touch existing files, so these rows go into `BACKLOG.md` with the first build card:

- Homepage card: the six questions in section 7.
- AI evals case study from `ai-evals-reps` (Flag O1).
- Finish PMO Agent and Skill Kits, then add them to Research Operations (and Skill Kits to AI Evaluations) by PRD amendment.
- Case study for the two-year research-ops rebuild (standards, onboarding, mentoring).
- Move `index.html` onto `assets/css/site.css` and `assets/js/site.js` (homepage card).
- Optional: per-discipline resumes (O7), share image (O8).

---

# Addendum A: locked decisions, a resume that reads for all three disciplines, and per-page session notes (card t_48ff0069)

Added 2026-11-17 by product. Builds on sections 1 to 16 and R1 to R19 above (Crit-passed at da0d2b3). Same harness, tokens, fonts and conventions unless a line below says otherwise. Build card: t_2e68d7bf (assignee `design`), which builds R1 to R19 and R20 to R28 together. Sections 1 to 16 are not edited; where this addendum changes them, section 17.3 says exactly how, and the addendum wins.

## 17. Addendum source, scope and what it changes

### 17.1 Source (verbatim)

From the card body (t_48ff0069), quoting Nick:

> we need to make sure resume.html supports each of the 3 things.

> The 'session notes' gag will need to be adjusted for each discipline... Need to keep that light hearted though. Don't want to seem like we are judging people for not clicking into things.

The card also records Nick accepting Maestro's proposed defaults on O1 to O9 (section 18) and Maestro's three creative directions for the session notes, which Nick did not object to (section 20).

Citation shorthand added: **[Nick-R]** and **[Nick-S]** = the two quotes above. **[Card-A]** = card t_48ff0069's body. **[case:evaluating-my-agent.html]** = the case study on `main` at commit 3d25fb4. **[Probe A-n]** = a check I ran for this addendum, results in section 24.2.

### 17.2 One new fact since the base PRD

On 2026-11-17 at 10:48, after the base PRD was written, Nick committed `evaluating-my-agent.html` to `main` (commit 9d55508, "Add case study: Evaluating My Own Agent (AI evals practice project)"), and at 10:59 reframed it (commit 3d25fb4, "drop pivot/reps framing, add real design+product examples"). This addendum cites the 3d25fb4 version. It is a complete case study of his `ai-evals-reps` work: eyebrow "AI evaluation & agent observability · Independent project", facts row "Project: Independent, ongoing", "Subject: My own multi-agent operations team", "Methods: Promptfoo, LangSmith, LLM-as-judge", zero `[Nick to` markers, real numbers (11/14 first regression pass, 2/2 routing scenarios fixed, 0 secrets reached the trace). Nick's reframe dropped the "practice" and "pivot" language on purpose, so this addendum calls it an independent project, not a practice project. It is live on nickpings.com and not linked from `index.html`. `feature/portfolio-restructure` was cut before it and does not contain it [Probe A1].

This is the trigger Nick set in O1 ("build ai-evals-reps into the AI Evals case study eventually, labeled as a personal project") and O4/O5 ("once there's something concrete to cite"). It is concrete and on the site, so section 21 and R20/R21 put it on the AI Evaluations page now, clearly labeled as independent work. If Nick would rather keep it off until later, dropping R20 and R21 (and the `Independent` block in R23) restores the base PRD's AI Evaluations page exactly; nothing else depends on them (Flag A1).

### 17.3 What this addendum changes in sections 1 to 16 (the addendum wins)

| Base text | Change | Why |
|---|---|---|
| Section 6.2 and R8: AI Evaluations has 2 cards and "no case study of a structured model evaluation" | AI Evaluations has 3 cards; card 1 is `evaluating-my-agent.html` (section 21.1). The gap is closed for launch. | 17.2, O1 |
| `$CASES` (section 10 preamble), R4, R9, R10 | `$CASES` gains `evaluating-my-agent`, so it gets the switcher, `back-link.js`, the `?from=` back links and the neutral colophon like the other five case pages. | R20 |
| R2 (ai-evaluations section ids) | `["top","philosophy","practice","selected-work","work","methods","tools","debrief"]`, section codes `S-01` to `S-07`. | Tools added, R21 |
| R12 / section 5.6 (Evaluation cluster) | Evaluation cluster has 7 chips (the 4 in 5.6 plus 3 in section 21.2). ai-evaluations chip total is 25, not 22. | R21 |
| R13 / section 5.7 (AI Evaluations tools omitted) | AI Evaluations has a Tools section: `Promptfoo`, `LangSmith`, `Python`. Impact stays omitted. | R21, Flag A2 |
| R14: `git diff main --stat -- index.html intro.html resume.html` is empty | Drop `resume.html` from that command. `index.html` and `intro.html` stay untouched. | R22, R23 |
| R15: the hard-coded observer lines it checks (`Two to choose from.`, `Coverage: N of 7`, `0 / 22`) and the `Four principles` literal in its grep | Observer copy now comes from the per-page voice (section 20, R24, R25). ai-evaluations expects `0 / 25` and the line `Case studies in view. Three to choose from. Hallucination risk: LOW. They all happened.`; research-operations expects `Participant reaches the case studies. One to choose from. Scheduling is flexible.` Coverage totals are read from the DOM (7 on ai-evaluations, 8 on the other two). Remove `Four principles` from the R15 grep pattern: R7 fixes every page at exactly four facets, so the word is copy, not a count. All other R15 checks stand. | R24, R25 |
| R16 edge case "no `og:image`" | Superseded by R27: each landing page gets its own preview image and Twitter card tags. | O8 |
| R17 changed-file list | Also allowed: `resume.html`, `evaluating-my-agent.html` (R10 edits only), `assets/og/*.png`, `docs/tools/og-card.html`, `docs/tools/voicecheck.py`. The "must be empty" diff drops `resume.html`. | R20, R22, R23, R27 |
| Section 4 device 4 ("the same usability-session conceit ... unchanged") and section 2 row "Observer ... Shared" | The mechanism (pill, observer panel, debrief cells, local-only, nothing stored) stays shared. The words are per page (section 20). | [Nick-S] |
| Section 13 non-goals: "Per-discipline resumes, or any edit to `resume.html`" | Per-discipline resumes stay a non-goal (O7). Editing `resume.html` is allowed, only as R22 and R23 specify. | O7, [Nick-R] |
| Section 13 non-goals: "`og:image` or social-card artwork" | Allowed as R27 specifies (three PNGs and the template). Favicon, sitemap, `robots.txt`, `404.html` stay non-goals. | O8 |
| Section 13 forbidden actions: editing `resume.html` | Removed from the forbidden list. `index.html`, `intro.html`, `research-self-service.html`, `CNAME`, `AGENTS.md`, `assets/passions/` stay forbidden. | R22, R23 |
| Section 14 flags O1 to O9 | Closed. See section 18. | [Card-A] |

## 18. Decisions O1 to O9: confirmed and locked

Nick accepted Maestro's proposed default on every open question [Card-A]. The build card must not re-ask any of these.

| # | Question (section 14) | Locked decision | Effect on the build |
|---|---|---|---|
| O1 | Write up `ai-evals-reps` as an AI evals case study? | Yes, labeled as a personal project. Do not gate the AI Evaluations page on it. | Already written by Nick (`evaluating-my-agent.html`, 17.2). R20 and R21 link it as card 1, labeled "Independent project". |
| O2 | Temporary link from `index.html` to the new pages? | No. Wait for the homepage card. | `index.html` stays byte-identical (R17). |
| O3 | Slugs | Keep `ai-evaluations`, `research-operations`, `consumer-research`. Not `ux-research`. | Section 3 and ADR 0001 stand as written. |
| O4 | More evaluation methods and tools? | Yes, once there is something concrete to cite. Don't invent. | The concrete source now exists on the site (17.2). R21 adds 3 chips and 3 tools, each traced to `evaluating-my-agent.html` or `resume.html`. Nothing from the private repo that is not on the site. |
| O5 | AI evals impact numbers? | Same as O4: only real, cited numbers. | The Impact strip stays omitted on AI Evaluations. The case study's numbers are evaluation pass rates, not impact, and stay on the case page and resume (Flag A2). |
| O6 | Fate of `intro.html` | Confirmed: live at `/intro`, unlinked from the discipline pages. | R18 stands. |
| O7 | One resume or three? | One shared `resume.html`. | Still one file, but it now has to read credibly for all three disciplines (section 19, R22, R23). |
| O8 | Link-preview image? | Yes. | R27: one preview image per landing page. |
| O9 | Draft copy | Acknowledged: draft copy in section 5 (and in this addendum) is editable by Nick. | The build ships the copy as written. A later edit is a PRD amendment to the relevant table, not a direct HTML edit. |

## 19. resume.html: audit and the fix

### 19.1 What the current resume says (read on `feature/portfolio-restructure` at da0d2b3, 257 lines)

| Element | Current text | How it reads to each reader |
|---|---|---|
| `<title>` | `Nicholas Pings Rodriguez — Resume` | Neutral. Has an em dash, which the site voice avoids. |
| Headline (`.role`) | `Senior UX Researcher · Consumer Products & Research Operations` | Consumer research: strong. Research ops: present. AI evaluation: absent. This is the line every recruiter reads first. |
| Lede | Consumer behavior and the full consumer portfolio, then two years rebuilding how research gets done. | AI evaluation: absent. Nothing about models, judges or evaluation. |
| Experian bullets (5) | Portfolio partner; partner with teams; generative AI research; AI-assisted automation and "where a model is trusted"; self-service and mentoring. | AI evaluation evidence is one clause in bullet 4. The LLM-as-a-judge pipeline Nick designed and built (`research-knowledge-base.html`, "Role: Designed & built") is missing. The Applied AI pilots bullet that is on `index.html` (E4: knowledge base, PMO agent, skill kits, PII stripping, competitor monitoring) is missing. Ops work is split across two bullets and never says "rebuilt research operations". |
| HP, Freelance | Launch-aligned studies, workshops, needs mapping; scoped, recruited and ran end-to-end research. | Consumer research and ops both covered ("recruited"). Fine as is. |
| Independent work | none | The one structured model-evaluation project Nick has is not on the resume at all. |
| Methods | Generative, Evaluative, Quantitative, Operations | No AI evaluation group. Operations has no recruiting or fielding term, which is the core of many research ops roles. |
| Tools | One run-on line of 23 tools | Reads as a UXR tool list. Promptfoo and LangSmith are missing. An ops reader can't see the recruiting stack; an eval reader can't see any eval tooling. |
| Job titles and dates | `Sr. User Experience Researcher`, `User Experience Researcher`, `Principal User Experience Researcher` | These are the real titles. They stay (base non-goal: never reword titles, employers or dates). |

Diagnosis: the resume is credible for consumer research, half-credible for research operations, and nearly silent on AI evaluation, while the evidence for all three already exists on the site. It doesn't need splitting. It needs the masthead to name all three, the Experian bullets to be sorted by discipline instead of by history, the missing evidence put back, and the Methods and Tools blocks grouped so each reader finds their own vocabulary in one glance. Nothing gets vaguer: every new line is a specific claim with a source.

### 19.2 The approach: one resume, three entry points

1. **Headline names all three, in the site's fixed order.** The real job titles stay below it, so a keyword search for "UX Researcher" still hits.
2. **Lede in three sentences, one per discipline,** consumer research first because it is the longest record.
3. **Experian bullets get short bold lead-ins** (`Consumer research.`, `Generative AI research.`, `AI evaluation.`, `Research operations.`, `Applied AI.`). Each reader scans to their label. Still five bullets, still one role.
4. **A new `Independent` block** for the agent-evaluation project, labeled independent so it is never read as employer work, and using Nick's reframed wording (an ongoing independent project, not "practice").
5. **Methods gains an `AI evaluation` group; Operations gains recruiting and onboarding terms.** Tools splits into four labeled lines.
6. **No numbers are added that are not tied to a role in a source.** The `index.html` stats (24+, 2.3K+, 30+, 1.5K+) are not attributed to a specific role anywhere, so they stay off the resume (Flag A3). The one exception is "weeks to hours", which the knowledge-base case study attributes directly.

Tested as a throwaway prototype in scratch (not in the repo): prints to 2 letter pages, same as today, and has no horizontal overflow at 390px [Probe A2, A3].

### 19.3 Exact new copy

Everything not listed here stays byte-identical: contact block, job titles, dates, org lines, HP and Freelance bullets, Education, the first three Methods groups, CSS tokens.

**`<title>`:** `Nicholas Pings Rodriguez &middot; Resume`

**Headline (`.role`):** `Senior Researcher &middot; AI Evaluation, Research Operations &amp; Consumer Research`

**Lede (`p.lede`, the `.mark` span in brackets):**

> Eight years of mixed-methods research, turning consumer behavior into product decisions across Experian's full consumer portfolio, [at every stage of the product life cycle]. For the last two years I've also rebuilt how that research gets done, so findings reach the people making decisions instead of stopping at a readout. And I hold AI to the same standard of evidence: setting where a model is trusted and where a person decides, and evaluating AI systems on what they actually do, not how they sound.

Sources: [resume.html] current lede (sentences 1 and 2); [index.html L499] "set the standards for where a model is trusted and where a person decides"; [case:evaluating-my-agent.html] "Grading the final answer only tells you whether it sounds right" and "The standard of proof didn't [change]".

**Experian bullets (replace all five, in this order; `<b class="pt-k">` holds the lead-in):**

| # | Bullet text (the lead-in is the bold label) | Sources |
|---|---|---|
| X1 | **Consumer research.** Research partner across the full consumer product portfolio, from flagship experiences to narrow edge cases, matching method and rigor to each stage of the life cycle, and translating findings into roadmaps and design decisions with design, engineering, and product teams. | [resume.html] current bullets 1 and 2, merged |
| X2 | **Generative AI research.** Led research on integrating generative AI into the consumer experience, including usability studies of Experian's virtual assistant across live builds, competitor products, and prototypes; recommendations shaped Experian's educational tools. | [index.html L498] E2; [case:experian-eva.html] section 02 "usability studies across live builds, competitor products, and prototypes" |
| X3 | **AI evaluation.** Designed and built an LLM-as-a-judge gate for the research knowledge base, with fixed researcher sign-off and manager approval and a person stepping in whenever the judge can't make a safe call. Set the standards for where a model is trusted and where a person decides across AI-assisted screening, analysis, and synthesis. | [case:research-knowledge-base.html] "Role: Designed & built", section 03; [resume.html] current bullet 4 |
| X4 | **Research operations.** Rebuilt research operations over about two years: self-service access to insight for stakeholders, research standards, onboarding, and mentoring through study design review. The research knowledge base cut cross-team topic review from weeks to hours. | [index.html L497] E1; [resume.html] current bullet 5; [case:research-knowledge-base.html] "went from weeks to hours" |
| X5 | **Applied AI.** Helped define Experian's internal Applied AI practices and work with the Applied AI team on pilots: a research knowledge base, a PMO agent, and skill kits. Also built PII-stripping preprocessing tools and competitor monitoring. | [index.html L500] E4 |

**New block after Experience, before Education** (same `section.block` / `article.job` markup as the jobs):

- `.block-label`: `Independent`
- `.job-title`: `Evaluating My Own Agent` · `.job-when`: `2026`
- `.job-org`: `Independent project <span>&middot; Ongoing</span>`
- Bullets, in order:
  - I1 `Evaluate the multi-agent team I run my day-to-day work through, with a Promptfoo regression suite that mixes deterministic checks and model-graded rubrics, run against fresh sessions.`
  - I2 `Moved from grading replies to inspecting tool-call traces. Turned a vague sense that routing was off into three testable scenarios, confirmed the defect, had it fixed, and reran the same suite as a before/after check (2 of 2 routing scenarios fixed).`
  - I3 `Built an on-demand LangSmith tracing tool with a secret-scanning gate, tested against a probe designed to slip past redaction (0 secrets reached the trace).`
  - I4 `Case study: <a href="evaluating-my-agent.html">nickpings.com/evaluating-my-agent</a>`
- Sources: [case:evaluating-my-agent.html] Approach, What I built, Outcomes (2/2, 0), facts row; [evals-reps] git log, first commit 2026-11-15 (the year).

**Methods block:** keep Generative, Evaluative, Quantitative byte-identical, then:

- `AI evaluation`: `LLM-as-a-judge &middot; Model-graded &amp; deterministic rubrics &middot; Regression suites &middot; Tool-call trace review &middot; Human-in-the-loop review &middot; Model trust standards` (sources: research-knowledge-base.html section 03; evaluating-my-agent.html Approach and What I built; index.html L499)
- `Operations` (full width, `.m-wide`): `Participant recruitment &middot; Research repositories &middot; Self-service enablement &middot; Research standards &middot; Onboarding &amp; mentorship &middot; AI-assisted synthesis &middot; Stakeholder management` (sources: current Operations group; Freelance bullet "Scoped, recruited, and ran"; index.html E1 "onboarding, and mentoring")

**Tools block:** same `.methods` / `.m-group` markup as Methods, replacing the inline-styled paragraph. Every one of today's 23 tools kept, plus Promptfoo and LangSmith (25, no duplicates):

- `Research &amp; recruiting` (full width): `Condens · Dovetail · Great Question · User Interviews · Lyssna · Outset · UserTesting · dscout · LookBack · Optimal Workshop · Maze · Sprig · Ethnio · UserZoom`
- `Analysis`: `Qualtrics · SPSS · Tableau · Python`
- `AI evaluation`: `Promptfoo · LangSmith`
- `Collaboration` (full width): `TheyDo · Figma · FigJam · Miro · Jira`

(`·` is written `&middot;` in the HTML, as today.)

**CSS added (3 rules, existing tokens only):** `.pt-k{font-weight:600;color:var(--pine);}` · `.m-wide{grid-column:1/-1;}` · `.job,.m-group{break-inside:avoid;}`

## 20. Session notes: one voice per discipline

### 20.1 The hard constraint (applies to every line on every page)

**The notes never judge the visitor.** [Nick-S] Concretely:

1. A line may describe what the visitor did, or grade the page, never grade the visitor.
2. Every "zero" outcome (no methods opened, no roles opened, sections scrolled past, a short visit) is written as a valid way to read the page. No line may imply the visitor missed, skipped, failed or should have done anything.
3. Lighthearted and self-deprecating: the joke is on Nick and the page, never on the reader.
4. Site voice: plain, first person where it speaks as Nick, no marketing words, no em dashes or en dashes.
5. Same mechanism everywhere: same triggers, same local-only measuring, nothing stored or sent. Only the words change.

`docs/tools/voicecheck.py` (committed with this addendum) enforces the mechanical part: a banned-word guard for grading or doubting language (`apparently`, `presumably`, `didn't`, `failed`, `skipped`, `ignored`, `missed`, `should have`, and others; "No judgment." is the one allowed use of "judg"), no dashes, no "intro" (R18), the same event keys in every voice, known placeholders only. Points 1 to 3 also need a human read, which is Crit's job on this PRD and on the build.

### 20.2 The three directions

- **AI Evaluations: the page grades itself.** A rubric-style readout of the page, never the visitor: consistency, factuality, hallucination risk, rage clicks counted as the page's bugs. The joke: once you start writing evals, you can't stop scoring things, including your own website. (Maestro's "I built eval pipelines for a living" line is softened to "Once you start writing evals", because Nick's eval work is one employer pipeline plus an independent project, and the resume should not be contradicted by its own website.)
- **Research Operations: the visit is fielded.** Recruitment, quota, no-shows, scheduling, incentives, panel health, repository hygiene. The joke: I run studies for a living, and now I'm fielding you.
- **Consumer Research: today's `index.html` notes, nearly unchanged.** Only the lines that could read as judging a visitor who didn't click are softened (20.4).

### 20.3 How the build wires it (mechanism)

- Each landing page's `<body>` carries `data-voice="<slug>"` (its own slug).
- `assets/js/site.js` holds all three voices as one object, pasted verbatim from the JSON block in 20.5, between the markers `/*VOICES-BEGIN*/` and `/*VOICES-END*/`, written as `var VOICES = {...};`. `python3 docs/tools/voicecheck.py assets/js/site.js` proves it matches.
- The voice is `VOICES[document.body.dataset.voice]`; a missing or unknown value falls back to `consumer-research`.
- What each key drives, using the same triggers as [index.html L692-877]:
  - `panelTitle`: the observer button title on load; `panelTitleDone`: the title after the debrief starts.
  - `debriefLabel`: the `#debrief .sec-head .label` text; `debriefNote`: the `.debrief-note` paragraph. Both written in the HTML (not by JS) so they render with JS off; the JSON is the source.
  - `events.open`: first note on load; `events.hero`: after 6s if no debrief yet; `events.sections[<data-obs>]`: first time each section is 30% visible, `sectionFallback` for any other name; `depth50`: first time scroll depth reaches 50%; `method1`, `method5`, `methodAll`: the 1st, 5th and last distinct chip opened (last = the page's chip count); `role`: each distinct role opened; `idle`: after 30s without input, once per idle stretch; `return`: tab becomes visible again; `rage` (AI Evaluations only, R26): the first rage-click burst.
  - `debrief`: the lines written at 98% depth, in order, 650ms apart as today. Each item has a CSS class (`note-head`, `note-key` or none) and `cases`, a list of `[condition, text]`; the first true condition wins and the last is always `always`.
- Conditions: `long` = at least 2 minutes on page; `full` = sections reached equals sections on the page; `methodsAny` / `methods5` = at least 1 / at least 5 chips opened; `rolesAny` = at least 1 role opened; `pausesAny` = at least 1 idle stretch; `clickedAny` = methodsAny or rolesAny; `rageAny` = at least 1 rage-click burst.
- Placeholders, all computed from the DOM or the session: `{cards}` case-card count as a capitalized word (One to Four); `{name}` the section's `data-obs`; `{label}` the chip name; `{role}` the role's `data-role`; `{time}` m:ss on page; `{seen}` / `{total}` sections reached / `[data-obs]` count; `{mN}`, `{mNames}`, `{mTotal}` chips opened, first three names joined as today (", and N more"), chip count; `{rN}`, `{rNames}`, `{rTotal}` the same for roles; `{pN}` idle stretches; `{rage}` rage-click bursts.
- The hero pill (`Session in progress`), the debrief cells (`#dTime`, `#dDepth`, `#dMethods`, `#dRoles` and their labels) and the observer's `aria-label` stay shared and unchanged.

### 20.4 Consumer Research: what changes from `index.html`

All other lines are verbatim from [index.html L736-860] (with the hard-coded counts replaced by placeholders, which R15 already required).

| Trigger | `index.html` today | Consumer Research | Why |
|---|---|---|---|
| Impact in view | `Impact numbers in view. Noticed, presumably.` | `Impact numbers in view. No need to catch them all.` | "presumably" doubts the reader |
| Experience in view | `Participant reaches Experience. The rows are waiting for a first click.` | `Participant reaches Experience. The rows open if you want the details.` | pressure to click |
| Debrief coverage, all reached | `Complete. No skipped tasks.` | `Complete. Every task attempted.` | "skipped" frames the other case as a failure |
| Debrief coverage, some missed | `A few were scrolled past. Noted without judgment.` | `A few went by quickly. Skimming counts.` | "noted" is still a mark against |
| Debrief, no methods opened | `Methods opened: none. The board was admired from a respectful distance.` | `Methods opened: none. The board reads fine sorted, too.` | a joke about not clicking, the exact thing Nick flagged |
| Debrief, no roles opened | `Roles expanded: none. The headlines were enough, apparently.` | `Roles expanded: none. The headlines cover the basics.` | "apparently" is a judgment about not clicking |

`index.html` itself keeps its current lines (it is forbidden to edit until the homepage card); BACKLOG row in R28.

### 20.5 The copy (exact, ship-ready, the single source)

Ship these strings exactly. Typographic note: `·` is U+00B7, quotes are straight `"` and `'` as in today's script. Changing any line is a PRD amendment to this block, re-checked with `python3 docs/tools/voicecheck.py`.

```json
{
  "research-operations": {
    "panelTitle": "Study #1 · Field Notes",
    "panelTitleDone": "Study #1 · Field Report",
    "debriefLabel": "Field status",
    "debriefNote": "I run studies for a living, so this visit got fielded like one: recruited, scheduled, and thanked. Nothing above is about how well you did. It was measured in this tab alone, is stored nowhere, and disappears when you leave.",
    "events": {
      "open": "Field status: live. Recruitment: 1 of 1, quota met.",
      "hero": "Participant arrived on time. No-show rate: 0%.",
      "sections": {
        "Philosophy": "Participant reaches Philosophy. No consent form needed. Nothing here is recorded.",
        "Practice": "Participant reaches Practice. Four principles, straight from the research playbook.",
        "Selected Work": "Participant reaches the case studies. {cards} to choose from. Scheduling is flexible.",
        "Impact": "Impact numbers in view. Coded, tagged, and filed in the repository.",
        "Experience": "Participant reaches Experience. Rows open on request. No booking link required.",
        "Methods": "Methods board in view. Every card tagged and filed. Repository hygiene: excellent.",
        "Tools": "Tools marquee in view. Every one of these has sent me a renewal notice.",
        "Debrief": "Participant reaches the debrief. Session wrapped, right on schedule."
      },
      "sectionFallback": "Participant reaches {name}. Right on schedule.",
      "depth50": "Halfway through the session. Running on time.",
      "method1": "First method opened: \"{label}\". Logged to the repository.",
      "method5": "Five methods opened. This participant would be great for the panel.",
      "methodAll": "All {mTotal} methods opened. Somebody get this participant an incentive.",
      "role": "Participant opens {role}. Task completed, no facilitator needed.",
      "idle": "Participant pauses. Bio break, probably. The session will wait.",
      "return": "Participant is back. No need to reschedule."
    },
    "debrief": [
      {
        "cls": "note-head",
        "cases": [
          [
            "always",
            "Field report. Closing out the study."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "long",
            "Session length: {time}. Ran long. Good sessions usually do."
          ],
          [
            "always",
            "Session length: {time}. Wrapped early. The calendar appreciates it."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "full",
            "Protocol coverage: {seen} of {total} sections. Full protocol, no deviations."
          ],
          [
            "always",
            "Protocol coverage: {seen} of {total} sections. A few went by quickly. Unmoderated sessions are like that."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "methods5",
            "Methods opened: {mN} of {mTotal} ({mNames}). Rich data."
          ],
          [
            "methodsAny",
            "Methods opened: {mN} of {mTotal} ({mNames}). Useful data."
          ],
          [
            "always",
            "Methods opened: none. Observation-only is a valid study design."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "rolesAny",
            "Roles opened: {rN} of {rTotal} ({rNames}). Follow-up questions welcome."
          ],
          [
            "always",
            "Roles opened: none. The summary was enough to go on."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "pausesAny",
            "Breaks taken: {pN}. Participant wellbeing comes first."
          ],
          [
            "always",
            "Breaks taken: 0. Powered straight through."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "always",
            "No-show rate: 0%. Panel health: n=1, feeling great about it."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "always",
            "Incentive: good vibes only. The budget request is still pending."
          ]
        ]
      },
      {
        "cls": "",
        "cases": [
          [
            "always",
            "Recommendation: Get in touch to schedule a follow-up. The details are just above this panel."
          ]
        ]
      },
      {
        "cls": "note-head",
        "cases": [
          [
            "always",
            "Study closed. Thank you for participating. Nothing was recorded, and nothing leaves this tab."
          ]
        ]
      }
    ]
  },
  "consumer-research": {
    "panelTitle": "Participant #1 · Session Notes",
    "panelTitleDone": "Participant #1 · Session Debrief",
    "debriefLabel": "Your session",
    "debriefNote": "Every visit here is a small usability session. I observe it the way I'd observe any study, with the same respect for the participant. Everything above was measured in this tab alone, is stored nowhere, and disappears when you leave.",
    "events": {
      "open": "Session begins. One participant, unmoderated.",
      "hero": "Participant reads the hero. Or skims it. No judgment.",
      "sections": {
        "Philosophy": "Participant reaches Philosophy. Reading pattern assumed F-shaped.",
        "Practice": "Participant reaches Practice. Four principles, no pop quiz.",
        "Selected Work": "Participant reaches the case studies. {cards} to choose from.",
        "Impact": "Impact numbers in view. No need to catch them all.",
        "Experience": "Participant reaches Experience. The rows open if you want the details.",
        "Methods": "Methods board in view. The cards sorted themselves.",
        "Tools": "Tools marquee observed. It doesn't stop. Neither does research.",
        "Debrief": "Participant reaches the debrief. Full scroll achieved."
      },
      "sectionFallback": "Participant reaches {name}.",
      "depth50": "Halfway down the page. Engagement looks healthy.",
      "method1": "First method opened: \"{label}\". Curiosity confirmed.",
      "method5": "Five methods explored. A thorough participant.",
      "methodAll": "All {mTotal} methods opened. Above and beyond.",
      "role": "Participant expands {role}. Task success.",
      "idle": "Participant pauses. Thinking, or getting coffee.",
      "return": "Participant returns. Welcome back."
    },
    "debrief": [
      {
        "cls": "note-head",
        "cases": [
          [
            "always",
            "Debrief. Synthesizing the session while it is still fresh."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "long",
            "Duration: {time}. A considered read. Coffee may have been involved."
          ],
          [
            "always",
            "Duration: {time}. Brisk. The participant knows what they came for."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "full",
            "Coverage: {seen} of {total} sections reached. Complete. Every task attempted."
          ],
          [
            "always",
            "Coverage: {seen} of {total} sections reached. A few went by quickly. Skimming counts."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "methods5",
            "Methods opened: {mN} of {mTotal} ({mNames}). A hands-on participant."
          ],
          [
            "methodsAny",
            "Methods opened: {mN} of {mTotal} ({mNames}). Selective. Respect."
          ],
          [
            "always",
            "Methods opened: none. The board reads fine sorted, too."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "rolesAny",
            "Roles expanded: {rN} of {rTotal} ({rNames}). The details were wanted."
          ],
          [
            "always",
            "Roles expanded: none. The headlines cover the basics."
          ]
        ]
      },
      {
        "cls": "note-key",
        "cases": [
          [
            "pausesAny",
            "Pauses observed: {pN}. Reflection, or a second tab. Both are valid."
          ],
          [
            "always",
            "Pauses observed: 0. Momentum held the whole way."
          ]
        ]
      },
      {
        "cls": "",
        "cases": [
          [
            "always",
            "Finding 1: The participant made it to the end. Content held attention, which is the whole point."
          ]
        ]
      },
      {
        "cls": "",
        "cases": [
          [
            "clickedAny",
            "Finding 2: The participant clicked things. Interest moved from passive to active."
          ],
          [
            "always",
            "Finding 2: The participant read rather than clicked. A reader, not a clicker."
          ]
        ]
      },
      {
        "cls": "",
        "cases": [
          [
            "always",
            "Recommendation: Get in touch. The details are just above this panel."
          ]
        ]
      },
      {
        "cls": "note-head",
        "cases": [
          [
            "always",
            "Session closed. Thank you for participating. Nothing was recorded, and nothing leaves this tab."
          ]
        ]
      }
    ]
  }
}
```

Read as a session, AI Evaluations (a visitor who opens nothing and scrolls to the end in under 2 minutes) produces: "Eval run starts. Subject: this page. You are not the one being graded." … "Scroll depth: PASS. 7 of 7 sections came into view. Nothing broke on the way down." "Methods board: sorted itself on cue. PASS. Opening chips is optional." "Experience: headlines readable without expanding. PASS." "Rage-click events: 0. Grading myself here, not you." "Hallucination risk: LOW. Every claim on this page traces to real work." "Overall: PASS. Sample size of one page, so read with caution." "Finding: Once you start writing evals, you start grading everything. Including your own website." The same visitor on Research Operations gets "Field status: live. Recruitment: 1 of 1, quota met." … "Methods opened: none. Observation-only is a valid study design." "No-show rate: 0%. Panel health: n=1, feeling great about it." "Incentive: good vibes only. The budget request is still pending." Neither page holds the visitor's choices against them.

## 21. AI Evaluations page: using the new case study

### 21.1 Selected work (replaces the AI Evaluations rows of the 5.3 table)

| # | Card title (`h3`) | href | Blurb | Source |
|---|---|---|---|---|
| 1 | `Evaluating My Own Agent` | `evaluating-my-agent.html?from=ai-evaluations` | `Independent project. I evaluate the multi-agent team I run my own work through: rubric scoring, tool-call traces instead of grading how replies sounded, and a routing bug found, fixed, and confirmed with the same suite.` (draft) | [case:evaluating-my-agent.html] summary, Approach, What I built |
| 2 | `Research Knowledge Base` | `research-knowledge-base.html?from=ai-evaluations` | as in 5.3, unchanged | 5.3 |
| 3 | `Experian Virtual Assistant` | `experian-eva.html?from=ai-evaluations` | as in 5.3, unchanged | 5.3 |

Order: the one structured model evaluation first, because it is the evidence an eval hiring manager screens for (base section 12, biggest risk). The blurb opens with "Independent project." so it can't be mistaken for employer work (O1).

### 21.2 Methods: three more Evaluation chips (appended after the four in 5.6)

| Chip | Description | Source |
|---|---|---|
| `Model-graded rubrics` | `Deterministic checks for what can be checked exactly, and a model-graded rubric for what can't.` | [case:evaluating-my-agent.html] Approach ("mixing deterministic checks with model-graded rubrics") and Outcomes (when a rubric "earns its keep over a keyword match") |
| `Tool-call trace review` | `Grading what an agent actually called, not just whether its reply sounded right.` | [case:evaluating-my-agent.html] Approach, What I learned |
| `Regression suites` | `The same eval rerun before and after a fix, to prove the fix held.` | [case:evaluating-my-agent.html] What I built, How it works |

AI Evaluations clusters: Evaluation (7), Evaluative (6), Quantitative (6), Operations (6), 25 chips.

### 21.3 Tools (new S-07 on AI Evaluations)

`Promptfoo`, `LangSmith`, `Python`, in that order. Sources: [case:evaluating-my-agent.html] (Promptfoo, LangSmith); [resume.html] Tools (Python). The three-item marquee uses the existing repeat-until-wide logic (R13 edge case).

### 21.4 Still omitted

Impact (S-04) stays omitted on AI Evaluations. 11/14 and 2/2 are pass rates from an independent evaluation run; next to employer stats in an "Impact" strip they would read as business impact, which they are not (Flag A2).

## 22. Link-preview images (O8)

One 1200x630 PNG per landing page, so a link pasted into an application or LinkedIn shows which discipline it is. Rendered once from a committed HTML template and committed as files; there is no build step at serve time.

- **Template:** `docs/tools/og-card.html?d=<slug>`. Static HTML, inline CSS, `<meta name="robots" content="noindex">`, the same Google Fonts link as `index.html`. Body is exactly 1200x630.
- **Content per card:** the name `Nicholas Pings Rodriguez.` (Young Serif, moss period), a small-caps label `Research in`, the discipline display name (section 3) as the largest text, the section 5.1 thesis with its `.mark` highlight, and `nickpings.com/<slug>` in muted ink. Colors only from the `index.html` `:root` tokens: `--paper` background, `--ink`, `--pine`, `--moss`, `--leaf`, `--muted`.
- **Render:** Chromium over CDP, viewport 1200x630, deviceScaleFactor 1, after `document.fonts.ready`, `Page.captureScreenshot` PNG, saved to `assets/og/<slug>.png`.
- **Tags on each landing page** (in addition to R16): `og:image` = `https://nickpings.com/assets/og/<slug>.png`, `og:image:width` `1200`, `og:image:height` `630`, `og:image:alt` = `Nicholas Pings Rodriguez. Research in <Display name>.`, `twitter:card` `summary_large_image`, `twitter:title` = the page title, `twitter:description` = the page description, `twitter:image` = the og:image URL.
- Case pages and `resume.html` get no preview image (non-goal, 24.4).

---

## 23. Addendum requirements (R20 to R28)

Harness: section 10's (local `python3 docs/tools/serve.py 8000` on `feature/portfolio-restructure`, Chromium over CDP, the same viewports, reduced-motion and no-JS emulation). "JS check" means `js(...)` on `http://localhost:8000/<file>`. `$PAGES` as in section 10; `$CASES` now also includes `evaluating-my-agent`. "Session script" means: load the page fresh, wait 7s, scroll each `[data-obs]` section into view in order with 400ms between, then scroll to the bottom and wait 8s; read `#observerLog li span:last-child` texts in order.

Build/deployment for **every** addendum requirement: **not Docker**, same justified exception as section 11 (static GitHub Pages site, nothing to containerize). The OG render uses the existing Chromium-over-CDP harness once at build time; no service, container or dependency is added.

### R20. The branch carries Nick's AI evals case study, and it is treated like every other case page.
- **Source:** 17.2; [case:evaluating-my-agent.html] at `main` 3d25fb4; O1; [Probe A1].
- **Acceptance:** `git merge-base --is-ancestor 3d25fb4 feature/portfolio-restructure && echo yes` prints `yes` (bring it in with `git merge origin/main` on the feature branch; never the other direction). `git diff 3d25fb4 -- evaluating-my-agent.html | grep '^-[^-]'` shows only the old colophon line (`UX Research &amp; AI Research Operations`). R10's checks (a) to (f) pass for `evaluating-my-agent.html`, including `?from=ai-evaluations` turning both back links into `← Back to AI Evaluations`, and its `.colophon` reading `Nicholas Pings Rodriguez · Research`. `grep -c "\[Nick to" evaluating-my-agent.html` prints `0`. R4's identical-switcher check passes over `$PAGES $CASES` with the new member.
- **Edge cases:** the merge must be a clean merge with no conflicts (the branch only adds files under `docs/` so far); if `main` has moved again by build time, merge the latest `origin/main` and re-run R17 against it; the case page keeps its own inline CSS and Fraunces font (only the switcher, back-link script and colophon change, like the others); its back link with no `?from=` still goes to `index.html`, which does not link back to it (expected until the homepage card).
- **Resources:** `evaluating-my-agent.html` (merged from `main`, then R10 edits); `assets/js/back-link.js`; `assets/css/disc-nav.css`.

### R21. The AI Evaluations page shows the new case study, the three new chips and the Tools section, and still no Impact strip.
- **Source:** section 21 and its cited sources; O1, O4, O5.
- **Acceptance:** JS check on ai-evaluations: section ids equal `["top","philosophy","practice","selected-work","work","methods","tools","debrief"]` and `.sec-code` texts equal `S-01` to `S-07`; `[...document.querySelectorAll('#selected-work a.case-card')].map(a => [a.querySelector('h3').textContent, a.getAttribute('href')])` equals the three 21.1 rows in order, and card 1's `p` text equals the 21.1 blurb exactly (starts `Independent project.`); the Evaluation cluster's `.n` is `7` and its chip names are the 5.6 four followed by `Model-graded rubrics`, `Tool-call trace review`, `Regression suites`, with the 21.2 descriptions verbatim; total `details.chip` is `25`; `#impact` is `null`; static-HTML tools list (curl and parse before the marquee duplicates it) equals `["Promptfoo","LangSmith","Python"]`. `#dMethods` reads `0 / 25` on load.
- **Edge cases:** no chip, tool or number from the private `ai-evals-reps` repo that is not on the site (`grep -ciE "golden|pairwise|MT-Bench" ai-evaluations.html` prints `0`); with JS off the 3-card grid and 3-item tools list are readable; a 3-item marquee shows no visible gap at 1440px.
- **Resources:** `ai-evaluations.html`; `assets/js/site.js` (no change needed beyond R15/R24).

### R22. resume.html's masthead, lede and Experian bullets read for all three disciplines, with the real titles and dates unchanged.
- **Source:** [Nick-R]; O7; section 19.1 audit; 19.3 copy and sources.
- **Acceptance:** JS check on `resume.html`: `document.title === "Nicholas Pings Rodriguez · Resume"`; `.role` text equals `Senior Researcher · AI Evaluation, Research Operations & Consumer Research`; `.lede` text, whitespace-normalized, equals the 19.3 lede without brackets and `.lede .mark` equals `at every stage of the product life cycle`; `[...document.querySelectorAll('.job-title')].map(e => e.textContent)` equals `["Sr. User Experience Researcher","User Experience Researcher","Principal User Experience Researcher","Evaluating My Own Agent"]`; the first three `.job-when` and `.job-org` texts equal `main`'s; the Experian `li` texts, normalized, equal X1 to X5 in order and each starts with a `b.pt-k` whose text is, in order, `Consumer research.`, `Generative AI research.`, `AI evaluation.`, `Research operations.`, `Applied AI.`; the HP and Freelance `ul.pts` innerHTML equal `main`'s after whitespace normalization; the `.contact` block's innerHTML equals `main`'s.
- **Edge cases:** no new em or en dashes (`grep -c "—" resume.html` prints `0` and `grep -o "&mdash;" resume.html | wc -l` prints `3`, the three unchanged date ranges); no bullet contains a number not in a cited source; "Senior Researcher" appears only in the headline (job titles keep "User Experience Researcher" for keyword searches); still one file (`ls resume*.html` prints only `resume.html`).
- **Resources:** `resume.html`.

### R23. resume.html gains the Independent block and discipline-legible Methods and Tools, still prints within two pages, and stays a single static file.
- **Source:** [Nick-R]; O7; 19.2 and 19.3; [Probe A2, A3].
- **Acceptance:** JS check: `[...document.querySelectorAll('.block-label')].map(e => e.textContent)` equals `["Experience","Independent","Education","Methods","Tools"]`; the Independent article's title, when and org text equal 19.3, its four `li` texts equal I1 to I4, and I4 holds `a[href="evaluating-my-agent.html"]`; Methods `h4` texts equal `["Generative","Evaluative","Quantitative","AI evaluation","Operations"]`, the first three `p` texts equal `main`'s and the last two equal 19.3; Tools `h4` texts equal `["Research & recruiting","Analysis","AI evaluation","Collaboration"]` and the tool names split on `·` form a set of 25 with no duplicates, equal to `main`'s 23 plus `Promptfoo` and `LangSmith`. `Page.printToPDF` (letter, `preferCSSPageSize: true`) of `resume.html` produces at most 2 pages; no `.job` or `.m-group` is split across the page break (the `break-inside:avoid` rule from 19.3 is present). At 390x844 and 320x568, `document.documentElement.scrollWidth <= innerWidth`. `grep -c "<script" resume.html` prints `0`. New CSS uses only existing tokens (no new hex colors: the R14 `comm` method applied to `resume.html`'s `<style>` against `main`'s prints nothing).
- **Edge cases:** today's resume already prints to 2 pages at 100% scale [Probe A2]; this requirement keeps it at 2, it does not promise 1 (Flag A4); the Independent block is visibly labeled personal in its org line, never mixed into the Experian role; the `Case study` link prints as readable text (no URL hidden behind "click here").
- **Resources:** `resume.html`.

### R24. Each landing page speaks in its own voice through one shared script, with the same triggers and nothing stored.
- **Source:** [Nick-S]; 20.3; R15 (local-only, counts from the DOM).
- **Acceptance:** `grep -o 'data-voice="[a-z-]*"' <page>.html` prints exactly the page's own slug, once, on `<body>`, for each of `$PAGES`. `python3 docs/tools/voicecheck.py assets/js/site.js` prints `OK: 3 voices, 116 strings` and exits 0. JS check per page after load: `.observer-title` text equals the voice's `panelTitle`; the first log line equals `events.open`; `#debrief .sec-head .label` and `.debrief-note` texts equal `debriefLabel` and `debriefNote` (also with JS disabled, from the static HTML). After the session script: the observer title equals `panelTitleDone`, and the debrief lines equal the voice's `debrief` list resolved for that session (no chips or roles opened, under 2 minutes, all sections reached). Changing `data-voice` to `nonsense` on a copy of a page and loading it gives the consumer-research `panelTitle`. R15's no-storage grep and storage checks still pass.
- **Edge cases:** a page without `#impact` or `#tools` never logs those section lines and raises no console error; repeated visibility changes log `events.return` each time, as today; `MAX_NOTES` (90) still caps the log; the debrief runs once; reduced motion and 390px behave as in R15 and R19.
- **Resources:** `assets/js/site.js`; the 3 landing pages; `docs/tools/voicecheck.py`.

### R25. The shipped copy is exactly the section 20.5 block, and no line judges the visitor.
- **Source:** [Nick-S] "Need to keep that light hearted though. Don't want to seem like we are judging people for not clicking into things"; 20.1; Maestro's directions as recorded in [Card-A].
- **Acceptance:** `python3 docs/tools/voicecheck.py` (PRD block) and `python3 docs/tools/voicecheck.py assets/js/site.js` both exit 0 (exact match, tone guard, no dashes, no "intro", key parity). Live, per page, run the session script twice: once opening nothing, once opening 5 chips and 1 role. Each log line equals a 20.5 string with its placeholders filled; in the "opened nothing" run, the methods and roles debrief lines are the `always` cases (for ai-evaluations: `Methods board: sorted itself on cue. PASS. Opening chips is optional.` and `Experience: headlines readable without expanding. PASS.`). Crit reads every zero-outcome line of all three voices against the 20.1 rules and records PASS or the offending line.
- **Edge cases:** placeholders never show raw (`grep -c "{" ` on the collected log text is `0`); `{cards}` renders `One` on research-operations and `Three` on ai-evaluations; names with quotes (chip labels) render as text, never HTML (notes are built with `textContent`, as today; `grep -c innerHTML assets/js/site.js` prints `0`).
- **Resources:** `assets/js/site.js`; `docs/portfolio-restructure-PRD.md` section 20.5; `docs/tools/voicecheck.py`.

### R26. AI Evaluations counts rage clicks as the page's bugs, locally, and the other pages don't count them.
- **Source:** Maestro's direction "Rage-click events: 0 (we're grading ourselves, not you)" [Card-A]; 20.2. Measured instead of hard-coded, so the scorecard is honest.
- **Acceptance:** a rage-click burst is 3 or more clicks within 700ms, each within 30px of the first; one burst counts once. JS check on ai-evaluations: dispatching 3 `click` events at the same point within 300ms logs `events.rage` once and makes the debrief line `Rage-click events: 1. Those are page bugs, not user errors.`; a second burst logs nothing new and the debrief says `2`; with no bursts the line is `Rage-click events: 0. Grading myself here, not you.` On research-operations and consumer-research the same 3 clicks log nothing about rage.
- **Edge cases:** double-clicking to select a word (2 clicks) is not a burst; clicks on links or `summary` count the same as anywhere else; the counter lives in a closure variable only, nothing stored (R15 greps still 0); touch taps count as clicks.
- **Resources:** `assets/js/site.js`; `ai-evaluations.html`.

### R27. Each landing page has its own 1200x630 link-preview image and Twitter card tags.
- **Source:** O8 [Card-A]; [Nick] "that I can point job apps at"; section 22.
- **Acceptance:** for each slug: `sips -g pixelWidth -g pixelHeight assets/og/<slug>.png` reports `1200` and `630`; `stat -f%z assets/og/<slug>.png` is at most `307200` (300 KB). JS check on `docs/tools/og-card.html?d=<slug>`: `document.body.getBoundingClientRect()` is 1200x630, the text contains `Nicholas Pings Rodriguez.`, `Research in`, the display name and `nickpings.com/<slug>`, `document.fonts.check('48px "Young Serif"')` is `true`, and every text element's box is at least 60px inside each edge. JS check on each landing page: the eight tags in section 22 exist with those exact values. The PNG's colors come only from the `:root` tokens (the template's CSS passes the R14 `comm` check against `index.html`). Crit opens each PNG and confirms it shows the right discipline.
- **Edge cases:** the absolute `og:image` URL 404s until Nick merges to `main` (expected; locally the file check stands in); LinkedIn caches previews, so after the merge each URL is run once through LinkedIn's Post Inspector (manual step, Flag A5); an unknown `?d=` on the template shows the consumer-research card rather than a blank one; `og-card.html` is not linked from any page and carries `noindex`.
- **Resources:** `docs/tools/og-card.html` (new), `assets/og/ai-evaluations.png`, `assets/og/research-operations.png`, `assets/og/consumer-research.png` (new); the 3 landing pages.

### R28. BACKLOG.md records this addendum's follow-ups next to the section 16 rows.
- **Source:** Nick's standing rule (follow-ups go to BACKLOG, not the PRD); sections 20.4, 21.4, 25.
- **Acceptance:** `grep -ciE "index.html.*(session|observer|apparently)" BACKLOG.md`, `grep -ciE "impact.*(ai eval|evaluat)" BACKLOG.md` and `grep -ciE "resume.*(number|stat)" BACKLOG.md` each print at least `1`; every section 16 row is also present; no existing row is deleted (`git diff main -- BACKLOG.md | grep -c '^-[^-]'` prints `0`).
- **Edge cases:** merge into the existing Open section, never overwrite; shipped rows untouched.
- **Resources:** `BACKLOG.md`.

## 24. Addendum: deployment, feasibility, risks

### 24.1 Deployment and build

Unchanged from section 11: **not Docker**, static GitHub Pages, no build step, preview with `python3 docs/tools/serve.py 8000`. The three OG PNGs are rendered once by the build card with the existing CDP harness and committed. Production is still a merge to `main` after Nick's explicit approval.

### 24.2 Feasibility probes (spike method)

| # | Given / When / Then | Verdict | Evidence |
|---|---|---|---|
| A1 | Given Nick's new case study, when I check the feature branch, then it is missing and mergeable. | VALIDATED | `git log --oneline da0d2b3..origin/main` shows only 9d55508 (adds `evaluating-my-agent.html`) and 3d25fb4 (reframes it), both touching that one file; the feature branch's only commit adds files under `docs/`, so the merge cannot conflict. `grep -c "\[Nick to"` on the case = 0. |
| A2 | Given today's `resume.html`, when printed to letter at 100%, then it fits on one page. | INVALIDATED | CDP `Page.printToPDF` (letter, preferCSSPageSize): 2 pages. Print-media sheet height 1150px against a 1056px page. R23 holds the line at 2 pages instead (Flag A4). |
| A3 | Given the 19.3 changes applied to a scratch copy (not the repo), when printed and shown on a phone, then it stays at 2 pages with no overflow. | VALIDATED | Scratch prototype: `Page.printToPDF` 2 pages; at 390x844 `scrollWidth` 390 = `innerWidth`; Methods grid lands as Generative/Evaluative, Quantitative/AI evaluation, Operations full width; Tools as Research & recruiting full width, Analysis/AI evaluation, Collaboration full width. |
| A4 | Given the 20.5 copy block, when checked mechanically, then every voice has the same keys, known placeholders, no dashes, no banned grading words, and no "intro". | VALIDATED | `python3 docs/tools/voicecheck.py` on the committed PRD: `OK: 3 voices, 116 strings`. |
| A5 | Given `index.html`'s observer script, when the voice copy replaces its literals, then the triggers stay the same. | VALIDATED (by reading) | [index.html L736-860]: every note is a string literal passed to `note()` from a fixed trigger; 20.3 maps each literal to a key. No trigger is added except R26's click counter. |

No AI/LLM component is built, so the AI three-dimension check does not apply.

### 24.3 Risks

- **Biggest risk: a joke that lands wrong on a recruiter.** The notes are the most personality-forward part of pages people open from job applications. Mitigation: the 20.1 rules, the mechanical guard, Crit's line-by-line read of every zero-outcome line, and Nick's own read of 20.5 before build.
- **The AI Evaluations page now leads with personal work.** Labeled "Independent project" on the card, the case page and the resume, so it can't be mistaken for employer work. It is still the strongest eval evidence Nick has. If he prefers employer work first, swap cards 1 and 3 in 21.1 (Flag A1).
- **"Senior Researcher" headline.** Broader than the real title. Mitigated by the real titles staying in Experience, unchanged.
- **Copy drift between the PRD and `site.js`.** Mitigated by `voicecheck.py`, which fails on any difference.
- **`index.html` keeps the old notes**, including the two lines this addendum softens, until the homepage card (R28 logs it).

### 24.4 Non-goals for the addendum (in addition to section 13, as amended in 17.3)

- Three resumes, resume variants, `?d=`-style resume switching, or JS on `resume.html`.
- Changing any job title, employer, date, contact detail or education line on the resume.
- Adding the `index.html` impact stats to the resume, or any number not tied to a role by a source.
- Editing `index.html`'s observer lines (homepage card).
- New session-notes triggers beyond R26's rage-click counter; a voice switcher the visitor can toggle; storing anything.
- An Impact strip on AI Evaluations, or eval methods/tools that appear only in the private `ai-evals-reps` repo.
- Preview images for case pages or the resume; favicons.

**Authorized boundaries (addendum):** everything in section 13's list, plus: merge `origin/main` into `feature/portfolio-restructure`; edit `resume.html` per R22 and R23; R10 edits to `evaluating-my-agent.html`; create `docs/tools/og-card.html` and `assets/og/*.png`; run `docs/tools/voicecheck.py`.

**Forbidden actions (addendum):** section 13's list as amended in 17.3. Still: never commit to, push to, or merge into `main`.

## 25. Flags for Nick (addendum)

1. **A1. Your new case study is on the AI Evaluations page, first.** You committed `evaluating-my-agent.html` this morning (and reframed it at 10:59; I cite the reframed version), which is exactly the O1/O4 trigger, so I put it on the page as card 1, labeled "Independent project", plus 3 chips and 3 tools it backs up. Say the word and I drop it back to "later", or move it below the two Experian cards.
2. **A2. No Impact strip on AI Evaluations.** 11/14 and 2/2 are pass rates from an independent evaluation run, not business impact. They stay on the case page and resume.
3. **A3. The resume has almost no numbers.** The homepage stats (24+ products, 2.3K+ findings, 30+ teams, 1.5K+ voices) aren't tied to a role anywhere I can cite. If you tell me which role each belongs to, they'd strengthen X1 and X4.
4. **A4. The resume already prints on 2 pages.** True today too, at 100% scale. The update keeps it at 2. Getting to 1 page would mean cutting content, which is a separate call.
5. **A5. One manual step after merge:** run each of the three URLs through LinkedIn's Post Inspector once so LinkedIn picks up the new preview images.
6. **A6. Read the 20.5 copy before build.** Especially the AI Evaluations finding line ("Once you start writing evals, you start grading everything. Including your own website.") and the Research Operations tools line ("Every one of these has sent me a renewal notice."). Edits go into 20.5, not the HTML.
7. **Docker exception** unchanged: static GitHub Pages, no container.

No ongoing cost, no new services, no new recurring steps beyond A5 (once).

## 26. Follow-ups (BACKLOG rows the build card adds, R28)

- Homepage card: bring `index.html`'s observer lines in line with section 20.4 (the softened consumer-research lines) when `index.html` moves onto `site.js`.
- AI Evaluations Impact strip, once there are cited, role-attributed evaluation numbers (O5).
- Resume: attribute the homepage stats to roles so they can go on the resume (Flag A3).
- Resume: a one-page cut, if Nick wants one (Flag A4).
- LinkedIn Post Inspector pass after merge (Flag A5).


---

# Addendum B: one story across every page, consumer research and AI evaluation both ongoing (card t_7e1550e9)

Added 2026-11-17 by product. Builds on sections 1 to 26 and R1 to R28 above and on the design prototype from card t_de460a73 (`~/.hermes/profiles/design/prototypes/t_de460a73/`, built from this branch at 9079db5). Same harness and conventions as section 10 and section 23. Sections 1 to 26 are not edited; where this addendum changes them, section 27.3 says exactly how, and the addendum wins. **Copy and positioning only.** No site file changes on this card. All copy below is approved-pending-Nick: the build ships it word for word once Nick signs off, and any later edit goes into the section 28 block, not the HTML.

## 27. Source, the story, and what this changes

### 27.1 Source

From card t_7e1550e9, quoting Nick. The quote is the true story to work from and is **not** to appear on the site:

> My research roots are in consumer research. In recent years I've been pivoting to research on AI systems, both consumer and internal. I evaluate/test AI products for our consumers, and evaluate internal AI systems for reliability and scalability to ensure blockers don't arise.

(The card renders the second sentence's break with a dash; it is shown here with a period because this doc avoids dashes.)

The card's two hard constraints: (1) translate it into site copy, don't transcribe it; (2) don't insinuate Nick has left consumer research. He is both, now and ongoing. Consumer research is the root and an active practice; AI evaluation is the newer, growing practice layered alongside it, not a replacement.

Citation shorthand added: **[Nick-N]** = the quote above. **[Card-B]** = card t_7e1550e9's body. **[Proto]** = the design prototype's `README.md` and `build_proto.py` (t_de460a73). **[Probe B-n]** = a check I ran for this addendum, results in section 31.2.

### 27.2 The story, in one paragraph (for the builder and Crit, not for the site)

There is one researcher with one root. Consumer research is where the work started and where it still sits at the center. AI evaluation grew out of it and runs next to it, in two directions: AI products that consumers use (tested with those consumers, as in `experian-eva.html` and `evaluating-my-agent.html`), and internal AI systems that teams depend on (checked so they hold up at scale, as in `research-knowledge-base.html`'s LLM-as-a-judge gate and the Applied AI pilots). Research operations is how all of that research gets done and reaches people. Every page tells this same story from a different door, so a visitor who lands on any one page learns the other two exist and that they share one root.

The words that would break constraint 2, and are banned from all section 28 copy by `docs/tools/narrativecheck.py`: pivot, transition, used to, no longer, former, previously, in recent years, recently, now, moved into, shift, switch, away from, left, beyond, rather than, anymore. Any line that names an origin ("started", "grew out of") must also carry a present-tense continuity marker ("still", "alongside", "and counting").

### 27.3 What this addendum changes in sections 1 to 26 (the addendum wins)

| Base text | Change | Why |
|---|---|---|
| Section 4 device 3 (shared Philosophy, verbatim) and R6 | Replaced. The "same researcher" signal is now carried by the narrative copy itself (section 29), backed by the switcher (R4) and footer (R5), which stay identical. R6 is restated in section 29. | [Proto] flag 2; [Card-B] |
| R3 (hero has name, pill, eyebrow, thesis) | Each discipline hero also has one `p.lede` directly after `.thesis`, with the exact text in section 28. | [Proto] change 1; R30 |
| R22 (resume `.lede` equals the 19.3 lede) | The `.lede` now equals `resume.lede` in section 28. The headline (`.role`) is unchanged and confirmed. Everything else in R22 stands. | R31 |
| Section 5.1 meta descriptions | Unchanged. Read for the new story: none implies a pivot, and none contradicts it (section 30). | [Probe B3] |

Not changed by this addendum, and still owed by the structural spec for the prototype (see Flag B4): R2's section-id lists and S-codes, R7 (Practice), R15/R21's section lists, R17's "index.html untouched", and the dead Philosophy/Practice lines in the 20.5 voices plus `voicecheck.py`'s `SECTIONS` list. This addendum only fixes copy and R6, as the card asks.

## 28. The copy (exact, approved-pending-Nick, the single source)

Format: one `key: text` per line. Square brackets mark the `.mark` highlight span. The middot in `resume.headline` is written `&middot;` and the ampersand `&amp;` in the HTML, as today. `python3 docs/tools/narrativecheck.py` checks this block mechanically (section 28.2).

```narrative
homepage.intro: Consumer research is where my work started, and it's still at the center of it. Alongside it, I evaluate AI: the AI products consumers use, and the internal AI systems teams depend on, so they hold up at scale. I've also rebuilt how the research itself gets done. Same researcher, three angles, each with its own case studies and methods.
homepage.row.ai-evaluations: Testing AI products with the consumers who use them, and testing the internal AI systems teams depend on so they hold up at scale. Deciding where a model is trusted and where a person decides.
homepage.row.research-operations: Research that goes further than the readout: self-service access, research standards, onboarding, mentoring, and an AI research knowledge base.
homepage.row.consumer-research: Eight years of mixed-methods research turning consumer behavior into product decisions, from generative discovery to diary studies.
lede.ai-evaluations: I test AI products with the consumers who use them, and test the internal AI systems teams depend on so they hold up at scale. Both grow out of the consumer research I've done for eight years and still do.
lede.research-operations: Alongside my own consumer research and AI evaluation work, I've rebuilt how research gets done at Experian: self-service access, research standards, onboarding, mentoring, and an AI research knowledge base.
lede.consumer-research: I've done mixed-methods consumer research for eight years, from generative discovery to diary studies, and it's at the center of my work. It's also how I test AI products: with the consumers who use them.
resume.headline: Senior Researcher · AI Evaluation, Research Operations & Consumer Research
resume.lede: Eight years and counting of mixed-methods consumer research, turning consumer behavior into product decisions across Experian's full consumer portfolio, [at every stage of the product life cycle]. Alongside that work, I evaluate AI to the same standard of evidence: AI products, tested with the consumers who use them, and the internal AI systems teams depend on, tested so they hold up at scale. For the last two years I've also rebuilt how research gets done, so findings reach the people making decisions instead of stopping at a readout.
switcher.label: Research disciplines:
footer.cross: Same research, other angles:
```

### 28.1 Where each line goes, and what it replaces

| Key | Location | Today / in the prototype | Decision | Sources |
|---|---|---|---|---|
| `homepage.intro` | `index.html`, `#disciplines p.disc-intro` (the new section from the prototype, replacing Selected work) | [Proto] draft: "Same researcher, three angles. Each page has its own case studies, impact, and methods." | **Revised.** Sets up the root, the two AI directions and research ops before the visitor picks a door. Keeps "Same researcher, three angles" (it pairs with the footer line). Drops "impact" because AI Evaluations has no Impact strip (O5). | [Nick-N]; [Proto]; [resume.html] lede sentence 2; section 18 O5 |
| `homepage.row.ai-evaluations` | `index.html`, the AI Evaluations row's description `p` | [Proto] draft: "Deciding where a model is trusted and where a person decides, and evaluating generative AI with the people who use it." | **Revised.** The draft only covered consumer-facing AI; it now names internal systems too. Not one of the four required locations; changed because it states the story. | [Nick-N]; [index.html L499]; [case:research-knowledge-base.html] |
| `homepage.row.research-operations` | same, Research Operations row | [Proto] draft, same text | **Confirmed**, no change. | [Proto]; section 5.1 thesis and meta |
| `homepage.row.consumer-research` | same, Consumer Research row | [Proto] draft, same text | **Confirmed**, no change. Present participle ("turning"), no past framing. | [Proto]; [resume.html] |
| `lede.ai-evaluations` | `ai-evaluations.html`, `p.lede` right after `.thesis` | [Proto] draft: "Researcher who evaluates generative AI with the people who use it, and with rubric scoring and tool-call traces when the thing being tested is an agent." | **Revised.** Names both AI directions and ties them back to consumer research as ongoing. Rubric and trace detail stays in the case study and Methods, where it already is. | [Nick-N]; [case:experian-eva.html]; [case:evaluating-my-agent.html]; [case:research-knowledge-base.html] section 03 |
| `lede.research-operations` | `research-operations.html`, `p.lede` | [Proto]: the page's meta description verbatim ("Researcher who rebuilt how research gets done at Experian: ...") | **Revised.** Same list, now opening with "Alongside my own consumer research and AI evaluation work", so the ops page shows the researcher still does the research. The meta description stays as is. | [Nick-N]; section 5.1 meta; [index.html L497] E1 |
| `lede.consumer-research` | `consumer-research.html`, `p.lede` | [Proto] draft: "Mixed-methods consumer researcher with eight years in the field, from generative discovery to diary studies." | **Revised.** Present perfect ("I've done ... for eight years") plus "at the center of my work" says ongoing; the second sentence shows the same methods now also test AI products, so the page connects to AI Evaluations instead of reading as a separate practice. | [Nick-N]; section 5.1; [case:experian-eva.html] |
| `resume.headline` | `resume.html`, `.role` | `Senior Researcher · AI Evaluation, Research Operations & Consumer Research` (19.3, shipped) | **Confirmed**, no change. Three present-tense practices in the site's fixed order (section 3); order is navigation order, not chronology, and nothing in a three-item headline reads as "used to". The real titles below it stay "User Experience Researcher". | section 3; 19.3; R22 |
| `resume.lede` | `resume.html`, `p.lede` | 19.3 lede: consumer research, then research ops, then "And I hold AI to the same standard of evidence: setting where a model is trusted ... not how they sound." | **Revised.** Sentence 1 gains "and counting" and names consumer research outright. AI moves to sentence 2, right next to consumer research, and names both directions (consumer AI products, internal AI systems). The ops sentence is kept word for word and moves to third. "Where a model is trusted" stays on the resume in Experian bullet X3. | [Nick-N]; 19.3; [resume.html] at 9079db5 |
| `switcher.label` | `nav.disc-nav .disc-label` on all 9 switcher pages | `Research disciplines:` (shipped at 1101bdc) | **Confirmed**, no change. A neutral label for three parallel options; it doesn't rank or date them. No supporting tagline is added: the switcher stays one line (R4). | R4; commit 1101bdc |
| `footer.cross` | `footer .foot-cross` lead-in on the 3 landing pages | `Same research, other angles:` | **Confirmed**, no change. It is now one of the three carriers of the same-researcher signal (section 29). | R5 |

### 28.2 How the copy meets the two hard constraints

**Constraint 1, translated not verbatim.** No line repeats Nick's sentences. The quote's frame ("my roots are", "in recent years I've been pivoting", "to ensure blockers don't arise") does not appear anywhere. The internal-systems point is restated in plain outcome terms ("the internal AI systems teams depend on, so they hold up at scale") instead of "reliability and scalability to ensure blockers don't arise". Mechanical check: `narrativecheck.py` fails any line that shares a run of 5 or more words with the quote; the longest shared run across all 11 lines is 3 words ("internal AI systems"), which is the name of the thing, not a transcript [Probe B1].

**Constraint 2, no "used to".** Three devices, in every line that names both practices:

1. **Present tense for consumer research, everywhere.** "it's still at the center of it", "I've done ... for eight years and still do", "it's at the center of my work", "Eight years and counting". Nothing about consumer research is in the simple past.
2. **"Alongside", never "instead" or "now".** AI evaluation is introduced with "Alongside it" or "Both grow out of", which layers it on top of consumer research. The banned list in 27.2 (pivot, transition, used to, no longer, previously, now, moved into, shift, beyond, rather than) is enforced by the checker.
3. **Every door names both.** The homepage intro, all three hero ledes and the resume lede each name consumer research and AI (checked mechanically). So the consumer research page says it also tests AI products, and the AI evaluations page says it grows out of consumer research that continues. No page reads as a standalone practice, and no page reads as the "after" of another.

What was deliberately avoided: "From consumer research to AI evaluation" (a journey), "now focused on" (a replacement), "beyond UX research" (Nick's own brief says "move out of just UXR", but on the site it would read as leaving), and "still" repeated in every line (three uses read as defensive, so the consumer research lede uses "at the center of my work" instead).

## 29. R6, restated: what carries the "same researcher" signal now

**The decision.** Shared Philosophy (base section 4 device 3) is gone from the discipline pages in the prototype, and with it the old R6 mechanism. The prototype's own note says the switcher and the footer line carry the signal now [Proto flag 2]. Those two say the pages are connected, but not why. A recruiter who opens only `/consumer-research` needs to read, in the hero, that this researcher also evaluates AI, and one who opens only `/ai-evaluations` needs to read that the AI work rests on ongoing consumer research. So the signal now has three carriers, in order of weight:

1. **The narrative copy (new, primary).** The homepage intro and every hero lede tell the one story of 27.2 and name consumer research and AI together (section 28). This replaces Philosophy as the main "same researcher" device. It is the thing a visitor actually reads first.
2. **The switcher (unchanged, R4).** Identical markup on all 9 pages, `Research disciplines:` label, three links in fixed order.
3. **The footer cross-link (unchanged, R5).** `Same research, other angles:` plus the other two disciplines, and the homepage intro's `Same researcher, three angles` echoes it.

Base section 4 devices 1, 2, 4, 5 and 6 are unchanged.

**If Nick keeps Philosophy on the discipline pages** (he can still reject that part of the prototype), the old R6 check runs as well and this R6 still applies: the ledes add to Philosophy, they don't compete with it.

### R6 (restated, replaces the base R6). The same-researcher signal is carried by the narrative copy, the identical switcher and the identical footer, and every carrier matches section 28.
- **Source:** [Card-B] ("resolve the design prototype's open flag #2 ... update PRD R6"); [Proto] README flag 2; [Nick-N]; base section 4 and [Nick] "The common thread among all of these fields is that they are fundamentally research disciplines."
- **Acceptance:** `python3 docs/tools/narrativecheck.py` prints a line starting `OK: 11 strings`. JS check per page in `$PAGES`: `document.querySelector('.hero .thesis + p.lede')` is not null and its text, whitespace-normalized, equals that page's `lede.<slug>` line; on `index.html`, `#disciplines .disc-intro` text equals `homepage.intro`. R4's identical-switcher command prints `1` over `$PAGES $CASES`, and every `.disc-label` text equals `switcher.label`. R5's identical-footer command prints `1`, and every `.foot-cross` text starts with `footer.cross`. If the prototype's Philosophy removal ships: `document.getElementById('philosophy') === null` on each of `$PAGES`; if it doesn't, the base R6 command also prints `1`.
- **Edge cases:** with JS off the lede and intro are present (static HTML, not injected); the prototype's `data-proto="lede"` toggle and `assets/proto/*` never ship (`grep -rc "data-proto" $PAGES.html index.html` is 0 for every file); a page opened with no referrer still gets the full story from its own lede (no copy depends on where the visitor came from); case pages carry only the switcher, not a lede (they have their own heroes, R10 unchanged).
- **Resources:** `index.html`, the 3 landing pages, `assets/css/disc-nav.css` (read), `docs/tools/narrativecheck.py`.

## 30. Everything else checked for the story (no change)

Read on this branch at 9079db5 for pivot wording [Probe B2, B3]:

- All four `<meta name="description">` texts (index and the three landing pages): present tense, no past framing. Unchanged. The AI Evaluations one doesn't mention internal systems; it doesn't have to (it's a search snippet, and the lede now says it). Optional tweak in Flag B3.
- `index.html` hero (eyebrow `Mixed-methods research · Research operations · AI in research`, thesis "Adaptive research to support a consistently shifting landscape."): the word "shifting" describes the landscape, not Nick, so it doesn't imply a pivot. Unchanged (the homepage hero is the homepage card's call).
- Experience role body on `index.html` and the landing pages ("I research across the full consumer product portfolio ..."): present tense. Unchanged.
- `evaluating-my-agent.html`: Nick's own 3d25fb4 reframe already removed the "pivot" language. Unchanged.
- Session-notes voices (20.5): no positioning claims. Unchanged.

## 31. Requirements, feasibility, deployment

Harness as section 23. Build/deployment for **every** Addendum B requirement: **not Docker**, same justified exception as section 11 (static GitHub Pages site, nothing to containerize). No service, container, dependency or recurring step is added.

### R29. The homepage's Research disciplines section opens with the section 28 intro and its three rows carry the section 28 descriptions.
- **Source:** [Card-B] location 1; [Proto] change 2; section 28.1.
- **Acceptance:** JS check on `index.html`: `#disciplines .disc-intro` text, whitespace-normalized, equals `homepage.intro`; `[...document.querySelectorAll('#disciplines .disc-card')].map(a => [a.getAttribute('href'), a.querySelector('.disc-body > p').textContent.trim()])` equals `[["ai-evaluations.html", homepage.row.ai-evaluations], ["research-operations.html", homepage.row.research-operations], ["consumer-research.html", homepage.row.consumer-research]]`; `python3 docs/tools/narrativecheck.py` prints `OK`.
- **Edge cases:** the intro wraps without horizontal overflow at 320x568 (`scrollWidth <= innerWidth`); it is a `p`, not a heading, so the heading outline stays `Research disciplines`; it renders with JS off; in the prototype's Layout B (Columns) the same text is used, so the layout choice can't change the story; the words "impact" and "case studies, impact" do not appear in the intro.
- **Resources:** `index.html` (the homepage card's build, not this card).

### R30. Each discipline page's hero has exactly one lede, right after the thesis, with its section 28 text.
- **Source:** [Card-B] location 2; [Proto] change 1 ("Why add a lede"); section 28.1.
- **Acceptance:** JS check per page in `$PAGES`: `document.querySelectorAll('.hero p.lede').length === 1`; `document.querySelector('.hero .thesis').nextElementSibling.matches('p.lede')`; its text, whitespace-normalized, equals `lede.<slug>`; it contains no `.mark` span (the thesis keeps the only highlight); `.hero .eyebrow` and `.thesis` still equal section 5.1 (R3).
- **Edge cases:** at 390x844 the lede is at most 6 lines and Selected work's heading is still reached within two screen heights (prototype measured 676px on Research Ops with the old lede); at 320x568 no overflow; reduced motion shows it without animation (it uses the existing `.rise` classes); with JS off it is visible; the meta descriptions and link previews are not changed to match the lede (section 30).
- **Resources:** `ai-evaluations.html`, `research-operations.html`, `consumer-research.html`; `assets/css/site.css` (the prototype's `.lede` rule, tokens only).

### R31. resume.html keeps its headline and replaces its lede with the section 28 text, and still prints within two pages.
- **Source:** [Card-B] location 3; 19.3; R22, R23; section 28.1.
- **Acceptance:** JS check on `resume.html`: `.role` text equals `resume.headline` (unchanged from 19.3); `.lede` text, whitespace-normalized, equals `resume.lede` without brackets; `.lede .mark` text equals `at every stage of the product life cycle`; every other R22 and R23 check still passes (except R22's `Evaluating My Own Agent` job-title entry and R23's `Independent` block checks, since that block was removed from `resume.html` at 9079db5 on Nick's call), including `Page.printToPDF` (letter, `preferCSSPageSize: true`) producing at most 2 pages and `grep -c "—" resume.html` printing `0`.
- **Edge cases:** the new lede is about 20 words longer than the 19.3 lede; if that pushes the print to 3 pages, the build shortens nothing on its own and stops for a PRD amendment (Flag B2), because the copy is fixed here; job titles, dates and bullets X1 to X5 are untouched; no new number appears ("eight years" is already on the resume).
- **Resources:** `resume.html`.

### R32. The switcher label and footer lead-in stay as shipped, and no new tagline is added.
- **Source:** [Card-B] location 4; commit 1101bdc; R4, R5; section 28.1.
- **Acceptance:** `grep -l 'class="disc-label">Research disciplines:</span>' *.html | wc -l` prints `9` (the 3 landing pages plus the 6 case pages); `grep -c 'class="disc-tagline\|class="disc-sub' *.html` prints `0` for every file; JS check on `$PAGES`: `.foot-cross` text starts with `Same research, other angles:`; R4 and R5 commands still print `1`.
- **Edge cases:** if the homepage gains the switcher in the homepage card, it uses the same label and the count becomes 10, not a new wording; the label never takes a qualifier like "current" or "past", which would date the disciplines.
- **Resources:** the 3 landing pages, the 6 case pages (read only).

### 31.1 Deployment and build

Unchanged from section 11 and 24.1: not Docker, static GitHub Pages, no build step, preview with `python3 docs/tools/serve.py 8000`. Production is still a merge to `main` after Nick's explicit approval. This card adds only text to this PRD and the checker `docs/tools/narrativecheck.py`.

### 31.2 Feasibility probes (spike method)

| # | Given / When / Then | Verdict | Evidence |
|---|---|---|---|
| B1 | Given the section 28 block, when checked mechanically, then every line is dash-free, free of pivot wording, shares no 5-word run with [Nick-N], and the five story lines name both consumer research and AI. | VALIDATED | `python3 docs/tools/narrativecheck.py` on the committed PRD: `OK: 11 strings, longest run shared with the quote = 3 words`. Negative control (scratch copy, not committed): with [Nick-N] pasted in as `lede.consumer-research` and "My work started in consumer research and I moved into AI evaluation." as `homepage.intro`, it exits 1 with five errors: pivot wording "In recent years" and "moved into", an origin with no continuity marker on both lines, and a 44-word run shared with the quote. |
| B2 | Given the live site copy at 9079db5, when searched for pivot wording, then nothing implies Nick left consumer research. | VALIDATED | `grep -iE "pivot|used to|no longer|formerly|transition|moving (in)?to|moved (in)?to|shift(ed|ing)? (to|from|away)|away from|these days|in recent years|beyond (ux|consumer)|move out"` over the 3 landing pages, `index.html`, `resume.html`, `evaluating-my-agent.html`: only CSS `transition` properties match, no copy. |
| B3 | Given the meta descriptions and the shipped switcher/footer copy, when read against 27.2, then none contradicts the story. | VALIDATED (by reading) | Section 30. |
| B4 | Given the resume lede grows by about 20 words, when printed, then it stays at 2 pages. | PARTIAL | Not printed on this card (copy only). Addendum A measured the print sheet at 1150px against a 1056px page, i.e. well inside page 2, so a few extra lines are very likely fine; R31 makes the build prove it. |

No AI/LLM component is built, so the AI three-dimension check does not apply. No platform choice is made, so no ADR.

### 31.3 Risks

- **Biggest risk: the internal-AI-systems claim has thin public evidence.** The site shows the LLM-as-a-judge gate and the Applied AI pilots, but no case study is about testing an internal AI system for reliability at scale. The copy says it because Nick says it [Nick-N]; a recruiter who clicks through finds supporting but not direct evidence (Flag B1).
- **"Still" read as defensive.** Used twice in the 11 lines (homepage intro, AI lede), never in the consumer research lede. Nick's read decides.
- **Copy drift.** The build could tweak a lede in HTML. Mitigation: R29 to R31 compare against the section 28 block, and `narrativecheck.py` guards the block itself.
- **The structural spec isn't written yet** (Flag B4). If PMO cuts build cards from this addendum alone, R2, R7, R15, R17 and the 20.5 voices would still describe pages with Philosophy and Practice.

### 31.4 Non-goals (in addition to sections 13 and 24.4)

- Removing Philosophy/Practice, building the homepage disciplines section, or any other structural change from the prototype (a separate spec, Flag B4).
- Changing the eyebrows, theses, meta descriptions, OG images or case-study copy.
- A tagline or sub-label under the switcher.
- Rewording job titles to "AI Evaluation" or anything not on Nick's real record.
- A new case study about internal AI reliability work (BACKLOG follow-up, Flag B1), or putting Experian-internal system names or details on the site.

**Authorized boundaries (this card):** append this addendum and the header line to `docs/portfolio-restructure-PRD.md`; add `docs/tools/narrativecheck.py`; commit and push `feature/portfolio-restructure`.

**Forbidden actions (this card):** any site file (`*.html`, `assets/`), `BACKLOG.md`, and anything on `main`. Never commit to, push to, or merge into `main`.

## 32. Flags for Nick (Addendum B) and follow-ups

1. **B1. The internal AI systems claim.** The copy says you test the internal AI systems teams depend on so they hold up at scale, because that's what you told me. The site backs it only indirectly (the knowledge-base judge gate, the Applied AI pilots). If there's a reliability or scale evaluation you can describe without Experian specifics, it would make a strong second AI Evaluations case. Otherwise the copy still stands.
2. **B2. Resume lede is about 20 words longer.** Should still print on 2 pages; the build checks. If it spills, I'd cut from the ops sentence, but that's your call.
3. **B3. Optional:** the AI Evaluations meta description (search/preview snippet) only names consumer-facing AI. I left it alone; say if you want it to mention internal systems too.
4. **B4. The structural spec for the prototype still needs writing** before PMO cuts build cards: dropping Philosophy/Practice changes R2, R7, R15, R17 and the 20.5 voices. The prototype's flag 1 (keep Philosophy/Practice on the homepage?) is also still open. This card fixed the copy and R6 only.
5. **B5. Read the 11 lines in section 28 out loud once.** That block is what ships, word for word.

No cost, no infrastructure, no recurring manual step.

**Follow-ups (for BACKLOG.md when the build lands, not requirements):**
- A case study on evaluating an internal AI system for reliability at scale, if Nick can share one (B1).
- AI Evaluations meta description mentioning internal systems, if Nick wants it (B3).
- Structural spec for the prototype's Philosophy/Practice removal and homepage section (B4).
