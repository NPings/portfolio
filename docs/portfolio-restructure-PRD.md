# PRD: Portfolio restructure, three discipline landing pages

- **Project:** portfolio (nickpings.com), static HTML/CSS/JS, no build step, hosted on GitHub Pages
- **Branch:** `feature/portfolio-restructure`, cut from `main` at `f76ff62`. Pushing this branch to origin is allowed as a backup. GitHub Pages builds only from `main`. Never push to or merge into `main` without Nick's explicit approval.
- **Card:** t_eb4fd595 (PRD). Build cards: not cut yet (PMO cuts them after Nick approves).
- **Author:** product, 2026-11-17
- **Status:** Draft for Crit review, then Nick's approval
- **ADR:** `docs/adr/0001-discipline-page-urls.md` (the URL scheme, because shared job-application links are expensive to change later)
- **davinci-prd skill:** not installed on this Mac. Sections written by hand to the same structure as `docs/intro-experience-PRD.md`.
- **This card changed no existing file.** It adds only this PRD and the ADR under `docs/`.

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
