# ADR 0001: Discipline landing pages are flat top-level files, shared without the extension

- **Date:** 2026-11-17
- **Status:** Proposed (pending Nick's approval of `docs/portfolio-restructure-PRD.md`)
- **Card:** t_eb4fd595 (product)
- **PRD:** `docs/portfolio-restructure-PRD.md`, section 3 and R1

## Context

Nick wants three discipline landing pages "with their own URLs ... that I can point job apps at." A URL pasted into a job application lives on in that application forever, so the URL scheme is expensive to reverse once Nick starts applying. The site is static HTML on GitHub Pages with no build step, and every existing page sits flat at the repo root (`index.html`, `resume.html`, five case-study pages, `intro.html`), linking each other with bare relative paths like `href="resume.html"`.

Probe results on the live site (2026-11-17, `curl` against nickpings.com):

- `https://nickpings.com/resume` and `https://nickpings.com/experian-eva` return 200: GitHub Pages serves `<name>.html` for the extensionless path.
- `https://nickpings.com/resume/` and `https://nickpings.com/experian-eva/` return 404: a trailing slash does not resolve to a flat file.
- `https://nickpings.com/experian-eva.html?from=ai-evaluations` and `https://nickpings.com/experian-eva?from=ai-evaluations` return 200: query strings pass through.

## Decision

1. The three pages are flat files at the repo root: `ai-evaluations.html`, `research-operations.html`, `consumer-research.html`.
2. The form Nick shares in applications is the extensionless lowercase URL: `nickpings.com/ai-evaluations`, `nickpings.com/research-operations`, `nickpings.com/consumer-research`.
3. Internal links between pages keep the `.html` form (`href="ai-evaluations.html"`), matching every existing link on the site and working on a plain local static server.

## Alternatives considered

- **Subdirectories (`/ai-evaluations/index.html`).** Gives `/ai-evaluations/` with a trailing slash, but every shared asset and case-study link would need `../`, the case-study pages would sit at a different depth than the landing pages, and it breaks the repo's flat pattern. Rejected.
- **Short slugs (`/evals`, `/ops`, `/research`).** Shorter, but less readable to a recruiter scanning a link, and `/research` is ambiguous because all three are research. Rejected.
- **Hash routes on one page (`/#ai-evaluations`).** Not three pages; previews, titles and descriptions could not differ per discipline. Rejected.

## Consequences

- The slugs are effectively permanent once shared. Renaming one later means keeping the old file as a redirect stub, the way `research-self-service.html` already redirects to `research-knowledge-base.html`.
- Nick must share the URL without a trailing slash (`/ai-evaluations`, not `/ai-evaluations/`).
- Local previews use the `.html` form, because `python3 docs/tools/serve.py` does not resolve extensionless paths.
