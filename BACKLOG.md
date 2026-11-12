# portfolio BACKLOG

Open / In progress / Shipped. Never delete shipped rows; merge, never overwrite.

## Open
- Fork scene, **research** prong: define and build what it leads to. Stub today ("coming soon"). (Nick, 2026-11-12: "We will talk about each of the prongs after." PRD addendum section 13.2.)
- Fork scene, **technology** prong: define and build what it leads to. Stub today. (Same source.)
- Passion deep-dives: build **techie**, **gamer** and **photographer** as **one page** (one `#passions` layer in `intro.html` with three subsections `#passions-techie`, `#passions-gamer`, `#passions-photographer`), never three routes, files or layers. The act-three chips already link to these hashes; only the router's `#passions-` branch and the stub lines change. (Nick, 2026-11-12: "Those passions should all be contained on one page." PRD section 19.3.)
  - Backgrounds spec'd in PRD addendum 3 (sections 25-31, R50-R65, card t_027c5838): techie circuit board draws itself, gamer rotating gameplay clips + disclaimer, photographer collage scaffold. Build card t_24e05978.
  - **Built (card t_24e05978), awaiting Crit and Nick's review, not merged to main:** `#passions` act four with the self-drawing circuit board, the six-game clip rotation (`assets/passions/gamer/`, 4,352 KB, sources and takedown recipe in `SOURCES.md`) with the disclaimer and credits, the photographer collage running on labeled placeholder frames, and one "Pause motion" toggle. Photographer stays a placeholder until the photos row below is done.
- **Photographer photos, BLOCKED on Nick:** swap the placeholder frames in `#passions-photographer` for Nick's photos (10-15, resized to a 1000px long edge, location data stripped) per PRD R61. Nick: "I'll send photos in a later message."
- Passion panel content: what Nick wants to say on the techie, gamer and photographer panels (placeholder "More on this soon." today). PRD Flag C4.
- Lower-risk gamer footage: replace the web-sourced clips with captures Nick records himself, after checking each publisher's fan-content policy. Decide before merging to `main`. PRD section 28.8, Flag C1.
  - Sharper footage: fire-emblem, smash-bros, destiny and baldurs-gate clips are 480 to 640 px wide sources (soft at full screen under the dim). Three of the six (fire-emblem, smash-bros, destiny) are Tenor user uploads, not official channels. See `assets/passions/gamer/SOURCES.md`.
- Optional: a captioned photo gallery behind the photographer collage. PRD section 31.5.
- Optional: glitch-on-hover touch for the techie/gamer/photographer chips, if Nick wants more life on the rest screen. Needs its own flash-rate check (PRD R45). (PRD section 24.5.)
- Avatar likeness pass: swap the placeholder hair/skin colors (and any signature detail) in the 12×16 pixel map. Needs Nick's input. (PRD addendum Flag A3.)
- Decide whether the fork scene gets a visible exit to the site ("straight to business"). (PRD addendum Flag A6.)
- Intro experience becomes the first-launch page: first-visit detection (e.g. localStorage flag) routes new visitors to `intro.html`, returning visitors land straight on `index.html`. (Nick, 2026-11-12, follow-up to the intro-experience build.)
- "Replay intro" CTA on `index.html`: hidden behind the logo, revealed on hover/tap, links to `intro.html`. (Nick, 2026-11-12, same follow-up.)

## In progress
- Intro experience (scroll-driven walkthrough: welcome → idle nudge → "Nice to meet you. I'm Nick." → red pill/blue pill choice). PRD approved (`docs/intro-experience-PRD.md`, Crit-passed), building on branch `feature/intro-experience`.
- Intro addendum (card t_4749555c): pill-scene prompt "What’ll it be? The choice is yours." + red-pill ember glow; "indulge me" now plays "I knew I liked you." on a red curtain that raises to the fork scene ("Where should we start?", pixel avatar, research/technology/passion stub prongs). Built in `intro.html` on `feature/intro-experience` per PRD sections 16-17; awaiting Crit and Nick's review. Not merged to main.
- Passion branch intro beat (PRD card t_a8f81d69, build card t_593e8d60): the fork's **passion** prong wipes in from the right to "I'm. 👏 A. 👏 Nerd. 👏", and as the visitor scrolls, "Nerd." glitches, takes over the page (paper flips to ink) and branches into three stub links: techie, gamer, photographer. Spec'd in PRD sections 19-24 (R33-R49); built in `intro.html` on `feature/intro-experience` (card t_593e8d60), awaiting Crit and Nick's review. Not merged to main. The research and technology prongs stay stubs.

## Shipped
(none yet)
