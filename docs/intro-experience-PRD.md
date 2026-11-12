# PRD: Intro experience (scroll-driven walkthrough)

- **Project:** portfolio (nickpings.com), static HTML/CSS/JS, no build step, hosted on GitHub Pages
- **Branch:** `feature/intro-experience` (pushing this branch to origin is allowed as a backup, per Nick via Maestro 2026-11-12; GitHub Pages builds only from `main`. Never push to or merge into `main` without Nick's explicit approval.)
- **Card:** t_94229c29 (PRD). Build card: t_48cb87aa (assignee `design`)
- **Author:** product, 2026-11-12
- **Status:** Draft for Crit review, then Nick's approval
- **davinci-prd skill:** not installed on this Mac. Sections written by hand to the same structure.
- **Addendum (2026-11-12):** sections 13 to 18 and requirements R16 to R32 add the pill-scene polish and the "indulge me" continuation (fork scene). Card t_fb2bf2d9 (PRD addendum), build card t_4749555c (assignee `design`). Where the addendum changes an earlier decision (R10, the section 11 non-goal about "indulge me", the section 4 JS budget, the R14 palette), it says so in section 13.3. Sections 1 to 12 are otherwise unchanged.
- **Addendum 2 (2026-11-12):** sections 19 to 24 and requirements R33 to R49 add the passion branch intro beat ("I'm. 👏 A. 👏 Nerd. 👏", the scroll-driven "nerd" glitch and takeover, and three stub links: techie, gamer, photographer). Card t_a8f81d69 (PRD addendum), build card t_593e8d60 (assignee `design`). It narrows R26 and R30 to research and technology, raises the R31 script budget to 330 lines, and fixes the one-page constraint for the future passion deep-dives (section 19.3). See section 19.4.
- **Addendum 3 (2026-11-12):** sections 25 to 31 and requirements R50 to R65 add the passion deep-dive backgrounds: one `#passions` layer with three stacked subsections; techie (a circuit board that draws itself, buildable now), gamer (rotating gameplay clips with a disclaimer, buildable now, copyright risk flagged as C1) and photographer (collage mechanism with marked placeholders; real photos BLOCKED on Nick, R61). Card t_027c5838 (PRD addendum), build card t_24e05978 (assignee `design`). It replaces R42 with R50 and amends R31, R43, R49 and the 24.4 non-goal. See section 25.3.
- **Addendum 4 (2026-11-12):** sections 32 to 37 and requirements R66 to R79 add the research branch intro beat: the research prong wipes in from the left to an affinity-map board where 12 sticky notes drift in, sort themselves into three pinned clusters (Education, Philosophy, Practice) joined by a self-drawing copper thread, under "Research, sorted." The clusters are stub links reserved for one future shared page (`#research-*`). Card t_b6a0515b (PRD addendum), build card t_f25a55e9 (assignee `design`). It narrows R26, R30 and R33 to technology, extends the router (R78) and allows a fourth inline script. See section 32.4.

---

## 0. Source brief (Nick, verbatim, from card t_94229c29)

> I want to make an intro experience. A dynamic walk through of me, my experience and work philosophy.
>
> This will be a dynamic scrollable experience. I'm not sure the actual terminology but many sites now deploy scroll that is not simply move up and down the page but instead move content on the page, that is what we are going for (i.e. scroll-driven / scrollytelling animation, not plain document scroll).
>
> It will open on "welcome." Centered on the screen using our current font and design system. After a delay, if the user doesn't click or do anything, the page can pop up at the bottom "pssst! scroll down."
>
> As they scroll the page shifts to an introduction: "Nice to meet you. I'm Nick." And I'd like Nick to be a new logotype including the period at the end. The period at the end should be the accent color of the site (green).
>
> From there as they keep scrolling it will transition to "Allow me to introduce myself…. Or we can get right to business." And it will give them a "red pill" that says "indulge me" in an alluring font and a "blue pill" in a technical font (courier?) that says "straight to business." Straight to business takes them to the current front page.
>
> This is our intro sequence and we can talk more about what comes with "indulge me" after but I'd like to start with this.
>
> It needs to be desktop and mobile friendly.

Citation shorthand used below: **[Nick]** = the brief above. **[Card]** = Maestro's card body (design-system notes and the 6 required sections). **[index.html]** = the current file on this branch (commit aba4454). **[Research]** = sources listed in section 11. **[Probe]** = a check I ran while writing this PRD, result recorded in section 10.

## Map to the card's six required sections

| Card section | Where it is decided in this PRD |
|---|---|
| 1. Scene-by-scene breakdown | Section 3 (scenes), R5 to R8 |
| 2. The two-choice step (pills) | Section 3.4, R8 to R10 |
| 3. Scroll mechanics | Section 4, R3, R4 |
| 4. Responsive behavior | Section 5, R11 |
| 5. Entry point | Section 2, R1 |
| 6. Accessibility | Section 6, R12, R13 |

---

## 1. Design tokens (reused, plus two new ones)

Copied as-is from `index.html` `:root` [index.html lines 14 to 27]. The build copies these into `intro.html`; it does not link or edit `index.html`.

| Token | Hex | Use in the intro |
|---|---|---|
| `--paper` | `#EAEEE4` | page background, every scene |
| `--card` | `#F8FAF4` | nudge background, pill label color |
| `--ink` | `#16241C` | primary text |
| `--ink-soft` | `#3B5245` | secondary lines |
| `--muted` | `#6E8270` | red-pill stub message |
| `--rule` | `#C8D3BE` | nudge border |
| `--pine` | `#2F5B44` | focus outline (same as site) |
| `--moss` | `#7E9C60` | **the accent green: every period treatment (`welcome.`, `Nick.`)** |

**New tokens (explicitly called for by this PRD, intro.html only):**

| Token | Hex | Why |
|---|---|---|
| `--pill-red` | `#9A3B2E` | The site has no red. `--rec` (#B0703A) only reaches 3.82:1 against `#F8FAF4` label text, which fails WCAG AA for normal text. `#9A3B2E` is a muted brick that sits with the green palette and gives 6.57:1 [Probe]. |
| `--pill-blue` | `#2E4A6B` | The site has no blue. A desaturated slate that reads as "blue pill" without clashing with pine. 8.65:1 against `#F8FAF4` [Probe]. |

**Fonts:** EB Garamond, Fraunces, IBM Plex Mono only. No new families. The intro's Google Fonts link adds Fraunces's `ital`, `SOFT` and `WONK` axes so the red pill can use a soft, wonky italic. Exact URL (verified HTTP 200 [Probe]):

```
https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..600;1,400..500&family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..800,0..100,0..1;1,9..144,300..800,0..100,0..1&family=IBM+Plex+Mono:wght@400;500&display=swap
```

---

## 2. Entry point (card section 5)

**Decision: a new file, `intro.html`, at the repo root. `index.html` stays the front page and is not modified.**

Why: it keeps the live site untouched while Nick reviews the demo, the blue pill can link to `index.html` with zero changes to it, and the five case-study pages that link back to `index.html` [index.html grep: experian-eva, hp-wolf-security, research-knowledge-base, research-pmo-agent, skill-kits] keep working.

Not ambiguous for this card. What is open is whether the intro later becomes the front door of nickpings.com. That is a Flag for Nick (section 9), not a requirement here. If he says yes, it is a follow-up card: rename `index.html` (for example to `work.html`), rename `intro.html` to `index.html`, update the five back-links and the blue pill's href.

---

## 3. Scene-by-scene breakdown (card sections 1 and 2)

The page is one sticky "stage" the height of the viewport. Scrolling moves through three scroll segments; content on the stage fades and moves in response, the stage itself never scrolls away. There is no footer and nothing after scene 3.

Scroll budget: the scroll track is `300svh` tall, so the scrollable distance is `200svh`. Progress `p` runs 0% to 100% across that distance.

| p (scroll progress) | What is on screen |
|---|---|
| 0% to 10% | Scene 1 at rest |
| 10% to 40% | Scene 1 out, scene 2 in |
| 40% to 60% | Scene 2 at rest |
| 60% to 90% | Scene 2 out, scene 3 in |
| 90% to 100% | Scene 3 at rest, pills live |

Snap points (proximity, not mandatory) sit at p = 0%, 50%, 100%.

### 3.1 Scene 1: "welcome."

- **Copy:** `welcome.` lowercase, exactly as Nick wrote it. The period is a `<span class="dot">` in `--moss`, the same pattern as `h1.name .dot` [index.html line 57].
- **Type:** Fraunces, weight 600, `font-variation-settings:"opsz" 144`, size `clamp(56px, 15vw, 160px)`, letter-spacing `-0.02em` (matches `h1.name` tracking), color `--ink`.
- **Layout:** centered horizontally and vertically in the viewport (`display:grid; place-items:center` on a `100svh` stage).
- **On load:** fades in over 600ms (opacity 0 to 1, translateY 12px to 0). Reduced motion: appears instantly.
- **Out (p 10% to 40%):** opacity 1 to 0, translateY 0 to `-12svh`, scale 1 to 0.92.

### 3.2 Idle nudge: "pssst! scroll down"

- **Copy:** `pssst! scroll down` lowercase, plus a down arrow `↓` in `--moss` after the text (decorative, `aria-hidden="true"`).
- **Element:** a `<button type="button">` fixed at bottom center, `bottom: calc(24px + env(safe-area-inset-bottom))`. Background `--card`, 1px `--rule` border, `border-radius:999px`, padding `10px 18px`, EB Garamond italic 18px, color `--ink-soft`.
- **Timing:** appears **4000ms** after `DOMContentLoaded` if none of these have happened first: `scroll`, `wheel`, `touchstart`, `pointerdown`, `keydown`. Mouse movement alone does **not** count as interaction (a resting cursor is not engagement).
- **Appear:** fade + slide up 16px over 400ms. The arrow bobs 4px on a 2s loop. Reduced motion: appears instantly, no bob.
- **Dismissal:** hides (opacity to 0 over 250ms, then `hidden`) on the first scroll past 8px or a click/tap on it. Clicking it scrolls to the scene 2 snap point (p = 50%), smooth unless reduced motion. Once dismissed it never reappears during that page load.
- **Never shows** if the page loads with `scrollY > 0` (reload mid-scroll, or back-button from `index.html`).

### 3.3 Scene 2: "Nice to meet you. I'm Nick."

- **Structure:** this is the page's single `<h1>`, three visual lines:
  1. `Nice to meet you.` EB Garamond italic, `clamp(22px, 4.4vw, 40px)`, `--ink-soft`.
  2. `I'm` EB Garamond italic, same size and color, on its own line.
  3. `Nick.` the logotype (below).
  Screen readers read it as one heading: "Nice to meet you. I'm Nick."
- **"Nick." logotype spec (new treatment, class `.logotype`):**
  - Font: Fraunces, weight **800**, `font-variation-settings:"opsz" 144, "SOFT" 50, "WONK" 0`.
  - Size: `min(clamp(96px, 30vw, 280px), 40svh)` (the `40svh` cap keeps it inside landscape phones).
  - Letter-spacing `-0.045em`, line-height `0.9`, color `--ink`.
  - **Period:** a `<span class="dot">` in **`--moss` `#7E9C60`**, pulled in with `margin-left:-0.03em` so it tucks against the k. It is the same glyph from the same font (not a drawn circle), so it scales and wraps with the word. `white-space:nowrap` on `.logotype` so the period never wraps alone.
  - What makes it "new" versus the homepage `h1.name` (Fraunces 700, -0.02em): heavier weight, tighter tracking, the Soft axis, larger optical size, and an animated period.
  - Contrast note: `#7E9C60` on `#EAEEE4` is 2.62:1 [Probe]. That is acceptable here because the period is decorative punctuation; the meaning is carried by "Nick" in `--ink` (13.7:1). Do not use `--moss` for any word that carries meaning.
- **In (p 10% to 40%):** opacity 0 to 1, translateY `10svh` to 0. The period starts at scale 0 and pops to scale 1 between p 32% and 40% (`transform-origin: 50% 80%`), so the green dot lands last.
- **Out (p 60% to 90%):** opacity 1 to 0, translateY 0 to `-12svh`.

### 3.4 Scene 3: the choice

- **Copy, two lines:**
  1. `Allow me to introduce myself…` Fraunces 500, `clamp(30px, 5.6vw, 64px)`, `--ink`, a single ellipsis character `…`.
  2. `Or we can get right to business.` EB Garamond italic, `clamp(22px, 3.6vw, 38px)`, `--ink-soft`.
  Nick's brief has four dots ("myself…."). I normalized it to one ellipsis because the next sentence starts on its own line with a capital. Flagged in section 9.
- **In (p 60% to 90%):** line 1 opacity 0 to 1 and translateY `8svh` to 0 over p 60% to 80%; line 2 over p 68% to 86%; the pills over p 80% to 90%.
- **The pills.** Both are capsules: `border-radius:999px`, min-height 56px (52px under 560px wide), horizontal padding 32px, label color `--card` `#F8FAF4`, `box-shadow: inset 0 1px 0 rgba(255,255,255,.25), 0 8px 20px -10px rgba(22,36,28,.5)` so they read as glossy pills. Hover (pointer devices only): translateY(-2px). Active: scale(0.98). Focus: 2px `--pine` outline, 3px offset (site standard [index.html line 361]).

| | Red pill | Blue pill |
|---|---|---|
| Label | `indulge me` | `straight to business` |
| Font | **Fraunces italic**, weight 400, `font-variation-settings:"opsz" 72, "SOFT" 100, "WONK" 1`, size `clamp(22px, 2.4vw, 28px)` | **IBM Plex Mono** 500, size `clamp(15px, 1.4vw, 17px)`, letter-spacing `0.02em` |
| Fill | `--pill-red` `#9A3B2E` | `--pill-blue` `#2E4A6B` |
| Element | `<button type="button">` | `<a href="index.html">` |
| Behavior | Stub (R10) | Navigates to the current front page (R9) |
| Order | First in DOM and visually (left on desktop, top on mobile) | Second |

- **Why Fraunces italic and not a new font for "indulge me":** Fraunces with Soft 100 and Wonk 1 switches on its swashy, ball-terminal italic forms, which reads as alluring and a little playful, and it is already the site's display face, so the intro needs zero new font families. A script face (Pinyon Script, Great Vibes) would be a fourth family on a site that currently has three, and scripts get hard to read at button sizes.
- **Why IBM Plex Mono for "straight to business":** it is the site's existing technical font [index.html line 47, `.mono`], it is the Courier-style answer to Nick's "(courier?)" without adding Courier.
- **Red pill stub ("indulge me"):** TBD, out of scope for this card. On click it reveals one line under the pills, in an `aria-live="polite"` region: `Coming soon. Take the blue pill for now.` (EB Garamond italic, `--muted`). It does not navigate.

---

## 4. Scroll mechanics (card section 3)

### Options

| Approach | One-line tradeoff |
|---|---|
| A. CSS `scroll-snap` + `position:sticky` only | Zero JS and very robust, but content only jumps scene to scene; nothing moves *with* the scroll, which is the opposite of what Nick asked for. |
| B. Lightweight JS library (GSAP ScrollTrigger, Lenis, etc.) | Most control and smoothest cross-browser scrubbing, but it adds the repo's first third-party JS dependency (CDN or vendored), and libraries like Lenis hijack native scroll, which hurts touch and accessibility. |
| C. Native CSS `animation-timeline: scroll()` + sticky stage | Content scrubs with the scroll in pure CSS on the compositor, no dependency, no build step; it is Baseline as of Firefox 159 (2026-10-27), so only users on older browsers need a fallback. |

### Decision: C, with a small scroll-snap assist and a vanilla JS fallback

1. **Structure:** `<main class="track">` is `300svh` tall. Inside it, `.stage` is `position:sticky; top:0; height:100svh`. The three scenes are stacked layers inside the stage (`position:absolute; inset:0`).
2. **Animation:** each scene's enter/exit is a normal `@keyframes` with `animation-timeline: scroll(root block)` and `animation-range` set to the percentages in section 3. Write `animation-timeline` as its own declaration after the `animation` shorthand (the shorthand resets it) [Research: dev.to Baseline article].
3. **Only `opacity` and `transform` are animated.** No `filter`, no layout properties, so it stays smooth on low-end phones.
4. **Snap assist:** `html{scroll-snap-type:y proximity}` with three zero-height snap markers at p = 0%, 50%, 100% (`scroll-snap-align:start`). Proximity, never mandatory, so the user is never trapped.
5. **No scroll hijacking.** No `preventDefault` on `wheel`/`touchmove`, no custom smooth-scroll, no `overflow:hidden` on `html` or `body`. Use `overflow-x:clip` instead of `hidden` if horizontal clipping is needed, because `hidden` creates a scroll container and breaks both sticky and the root scroll timeline [Research].
6. **Gate:** all scroll-driven styles live inside `@supports (animation-timeline: scroll()) and @media (prefers-reduced-motion: no-preference)`.
7. **Fallback (browser lacks `animation-timeline`, motion allowed):** about 30 lines of inline vanilla JS. An `IntersectionObserver` watches the three snap markers and sets `data-scene="1|2|3"` on `.stage`; CSS crossfades scenes with 500ms `opacity`/`transform` transitions keyed on that attribute. Discrete, not scrubbed, but same layout and same scenes.
8. **Total JS budget:** one inline `<script>`, under 120 lines, no external scripts. It covers: idle nudge, fallback observer, scene-3 pointer gating, focus scroll, red-pill stub.

No ADR: this is one self-contained page and the choice is cheap to reverse (swap keyframe timelines for a JS driver). The tech-viability skill reserves ADRs for expensive-to-reverse choices.

---

## 5. Responsive behavior (card section 4)

| Concern | Desktop (≥ 900px wide, wheel/trackpad) | Mobile (< 560px wide, touch) |
|---|---|---|
| Input | Mouse wheel, trackpad inertia, Space/PageDown/arrows. All native scroll. | Native touch swipe with iOS/Android momentum. Same scroll track, no gesture code. |
| Viewport unit | `svh` everywhere (stable when the mobile URL bar shows/hides). `dvh` is not used, because it causes jumps mid-scroll. | Same. |
| `welcome.` | up to 160px | ~56px to 60px at 375 to 390px wide |
| `Nick.` logotype | up to 280px | ~112px to 117px at 375 to 390px; capped at `40svh` in landscape |
| Scene 3 line 1 | up to 64px | 30px |
| Pills | Side by side, `display:flex; gap:24px; justify-content:center`, each sized to its label | Stacked in a column, `gap:14px`, each `width:100%; max-width:320px`, centered; min-height 52px (above the 44px touch-target minimum) |
| Hover lift | Only under `@media (hover:hover)` | None |
| Nudge | Bottom center, 24px up | Bottom center, 24px + safe-area inset (clears the iPhone home indicator) |
| Side padding | `--pad` from the site: `clamp(22px, 6vw, 72px)` | same token, resolves to 22 to 23px |

Between 560px and 899px (tablets) the desktop layout applies with the clamp() sizes scaling down. Landscape phones (height under 500px) rely on the `svh` caps so nothing in a scene exceeds the viewport.

---

## 6. Accessibility (card section 6)

- **Reduced motion (`prefers-reduced-motion: reduce`):** none of the scroll-driven CSS applies. The page renders as three ordinary stacked sections, each `min-height:100svh`, content centered and fully visible at opacity 1, no transforms. Scrolling is a plain document scroll. The nudge still appears after 4s but without slide or bob. Clicking it jumps (not smooth-scrolls). This is also exactly what users without JavaScript and without CSS support get, because the static stack is the base CSS and motion is layered on top.
- **Skip path:** the first focusable element in `<body>` is a skip link, `Skip intro, go to the site`, `href="index.html"`, visually hidden until focused, then shown top-left in IBM Plex Mono 14px on `--card`. One Tab plus Enter from page load takes a keyboard or screen-reader user to the current front page.
- **Semantics:** `<html lang="en">`, a `<main>` landmark, three `<section aria-label="...">` scenes, one `<h1>` (scene 2). Decorative arrows are `aria-hidden="true"`. Pills are a real `<button>` and a real `<a>`, so they are announced with their roles and visible text.
- **Focus never lands on something invisible:** both pills are focusable at all times (hidden by opacity only, never `display:none` or `visibility:hidden`). When either pill receives focus while scene 3 is not on screen, JS scrolls to the end (p = 100%) so the focused pill is visible (WCAG 2.4.11).
- **No invisible click traps:** scene 3 has `pointer-events:none` until the page is within the last 10% of scroll (JS adds `.is-live`). Without this, a tap where an invisible pill sits during scene 1 would navigate away.
- **Focus styling:** 2px `--pine` outline, 3px offset, same as the site.

---

## 7. Requirements

Every requirement's verification runs against a local static server from the repo root on this branch (`python3 -m http.server 8000`), in a Chromium browser driven over CDP (the Browser Use helper on this Mac). Viewports: desktop `Emulation.setDeviceMetricsOverride(width=1440,height=900,deviceScaleFactor=1,mobile=false)`, mobile `(width=390,height=844,deviceScaleFactor=3,mobile=true)`. Reduced motion: `Emulation.setEmulatedMedia(features=[{name:"prefers-reduced-motion",value:"reduce"}])`. "JS check" means `js(...)` on `http://localhost:8000/intro.html`.

Build/deployment for **every** requirement: not Docker. See section 8 for the justification. No requirement adds a container, service or process beyond the local preview server.

### R1. The intro lives in a new `intro.html` at the repo root, and no existing site file changes.
- **Source:** [Card] section 5 and "no code changes to index.html or other site files"; [Nick] "Straight to business takes them to the current front page."
- **Acceptance:** `test -f intro.html` exits 0, and `git diff --name-only main...feature/intro-experience` lists only `intro.html` and files under `docs/`.
- **Edge cases:** the builder must not "helpfully" add a link to the intro from `index.html`, nor share a CSS file by extracting styles from `index.html`. Styles are inlined in `intro.html` like every other page in the repo.
- **Resources:** `intro.html` (new); `index.html` (read-only).

### R2. With no JavaScript, or with reduced motion, all three scenes render as a readable static stack.
- **Source:** [Card] section 6; assumption that the no-JS case should match the reduced-motion case (progressive enhancement).
- **Acceptance:** with JS disabled (`Emulation.setScriptExecutionDisabled(value=true)`) and with reduced motion emulated, each of these JS/DOM checks holds: `document.body.innerText` contains `welcome.`, `Nice to meet you.`, `Nick.`, `Allow me to introduce myself…`, `Or we can get right to business.`, `indulge me`, `straight to business`; for each `section` in `main`, `getComputedStyle(s).opacity === "1"`; the blue pill's `href` ends in `index.html`.
- **Edge cases:** no JS means no nudge and no red-pill message; that is acceptable. Content must not be hidden by a default `opacity:0` that only JS removes.
- **Resources:** `intro.html` base CSS.

### R3. Scenes transform with scroll using native CSS `animation-timeline: scroll()`, gated by `@supports` and motion preference, with no scroll hijacking and no external scripts.
- **Source:** [Nick] "scroll that is not simply move up and down the page but instead move content on the page"; [Card] section 3; [Research] Baseline status.
- **Acceptance:** (a) `grep -c "animation-timeline" intro.html` ≥ 3 and `grep -c "@supports (animation-timeline: scroll())" intro.html` ≥ 1; (b) `grep -cE "<script[^>]+src=" intro.html` = 0 and `grep -ciE "preventDefault" intro.html` = 0; (c) at 1440x900 in Chromium, JS check after `scrollTo(0,0)`: scene 1 opacity > 0.95 and scene 2 opacity < 0.05; after `scrollTo(0, (scrollHeight-innerHeight)*0.5)` and two animation frames: scene 2 opacity > 0.95 and scene 1 opacity < 0.05; after scrolling to the bottom: scene 3 opacity > 0.95; (d) at the midpoint between snaps (p = 25%) scene 1 and scene 2 both have opacity strictly between 0.05 and 0.95, proving it scrubs rather than jumps.
- **Edge cases:** fast fling to the bottom lands on scene 3 fully visible; scrolling back up reverses every animation; `html`/`body` must not use `overflow:hidden` (`getComputedStyle(document.documentElement).overflowY !== "hidden"`); resizing the window mid-scroll keeps the current scene visible.
- **Resources:** `intro.html` CSS.

### R4. Browsers without `animation-timeline` get a JS crossfade fallback with the same scenes.
- **Source:** [Research] older browsers lack support; assumption that a discrete crossfade is an acceptable degraded experience.
- **Acceptance:** Chromium supports `animation-timeline`, so force the fallback with a throwaway copy outside the repo whose `@supports` condition can never match: `mkdir -p "$TMPDIR/fb" && sed 's/animation-timeline: scroll()/animation-timeline: nope()/' intro.html > "$TMPDIR/fb/intro.html"`, serve that folder (`python3 -m http.server 8001 -d "$TMPDIR/fb"`), load `http://localhost:8001/intro.html`, scroll to p = 50%, wait 700ms, JS check `document.querySelector('.stage').dataset.scene === "2"` and scene 2 opacity > 0.95; scroll to bottom, wait 700ms, `dataset.scene === "3"`.
- **Edge cases:** no `IntersectionObserver` (very old browsers): fall back to the R2 static stack, not a blank stage.
- **Resources:** `intro.html` inline script.

### R5. Scene 1 shows "welcome." centered, in Fraunces 600, with a moss period.
- **Source:** [Nick] "open on 'welcome.' Centered on the screen using our current font and design system"; [index.html] `.dot` pattern.
- **Acceptance:** at both viewports with `scrollY = 0`, JS check on the welcome element: `textContent.trim() === "welcome."`; computed `fontFamily` starts with `"Fraunces"`; `fontWeight === "600"`; the `.dot` span's computed `color === "rgb(126, 156, 96)"`; the element's bounding-box center is within 5% of the viewport center on both axes.
- **Edge cases:** web font slow or blocked: falls back to Georgia (font stack `"Fraunces", Georgia, serif`) and stays centered; text never overflows at 320px wide (`scrollWidth <= innerWidth`).
- **Resources:** `intro.html`; Google Fonts.

### R6. If the visitor does nothing for 4 seconds, "pssst! scroll down" appears at the bottom and goes away for good once they scroll or tap it.
- **Source:** [Nick] "After a delay, if the user doesn't click or do anything, the page can pop up at the bottom 'pssst! scroll down.'"; 4000ms and dismissal rules are an assumption (section 3.2).
- **Acceptance:** (a) load, wait 4500ms with no input: the nudge button is visible (`!hidden`, computed opacity > 0.95), its text contains `pssst! scroll down`, and its bottom edge is within 120px of `innerHeight`; (b) fresh load, dispatch a `keydown` at 2000ms, wait until 6000ms: nudge never visible; (c) after (a), `scrollTo(0, 50)`, wait 400ms: nudge `hidden === true`; scroll back to 0 and wait 6000ms: still hidden; (d) after (a) on a fresh load, click the nudge: within 1500ms `scrollY` is ≥ 45% of `scrollHeight - innerHeight`.
- **Edge cases:** loads with `scrollY > 0` (reload, back button): never shows; mouse movement alone does not cancel the timer; tab in background: fine if it is already showing when the visitor arrives; the nudge must not cover scene 3's pills (it is dismissed long before scene 3 by definition, since reaching scene 3 requires scrolling).
- **Resources:** `intro.html` inline script and CSS.

### R7. Scene 2 shows "Nice to meet you. I'm Nick." with "Nick." as the new logotype and a moss-green period.
- **Source:** [Nick] "Nice to meet you. I'm Nick." and "I'd like Nick to be a new logotype including the period at the end. The period at the end should be the accent color of the site (green)."; [Card] `--moss` as accent.
- **Acceptance:** JS check: exactly one `h1` exists and its `innerText` normalized for whitespace equals `Nice to meet you. I'm Nick.`; `.logotype` computed `fontFamily` starts with `"Fraunces"`, `fontWeight === "800"`, `fontVariationSettings` contains `"SOFT" 50`, `letterSpacing` is negative; `.logotype .dot` computed `color === "rgb(126, 156, 96)"`; `.logotype` `whiteSpace === "nowrap"`; at p = 50% the period's computed transform is `none` or scale 1 (fully landed).
- **Edge cases:** at 320x568 and 844x390 (landscape phone) the logotype's bounding box fits inside the viewport; the period never wraps to its own line; text is real text, selectable and readable by screen readers (no SVG or image).
- **Resources:** `intro.html`.

### R8. Scene 3 shows the two-line choice copy and two pills styled per section 3.4.
- **Source:** [Nick] "Allow me to introduce myself…. Or we can get right to business." with a red pill "indulge me" in an alluring font and a blue pill in a technical font; [Card] section 2.
- **Acceptance:** JS check at the bottom of the page: body text contains `Allow me to introduce myself…` and `Or we can get right to business.`; red pill computed `fontFamily` starts with `"Fraunces"`, `fontStyle === "italic"`, `backgroundColor === "rgb(154, 59, 46)"`; blue pill computed `fontFamily` starts with `"IBM Plex Mono"`, `backgroundColor === "rgb(46, 74, 107)"`; both pills' computed `color === "rgb(248, 250, 244)"` and `borderRadius` ≥ 28px; red pill precedes blue pill in DOM order.
- **Edge cases:** long-press or right-click on the blue pill shows the normal link menu (it is a real link); if Fraunces italic fails to load, Georgia italic is the fallback; no other buttons or links appear in scene 3.
- **Resources:** `intro.html`; Google Fonts URL in section 1.

### R9. The blue pill ("straight to business") takes the visitor to the current front page.
- **Source:** [Nick] "Straight to business takes them to the current front page."
- **Acceptance:** JS check: blue pill is an `<a>` whose `getAttribute("href") === "index.html"`; click it and after load `location.pathname` ends in `/index.html` and `document.title` starts with `Nicholas Pings Rodriguez`.
- **Edge cases:** Back from `index.html` returns to the intro at scene 3 with no nudge; Cmd/Ctrl-click opens in a new tab (native link behavior, no JS click handler on the blue pill).
- **Resources:** `intro.html`; `index.html` (read-only target).

### R10. The red pill ("indulge me") is a clickable stub that shows a "coming soon" line and does not navigate.
> **Superseded by the addendum (R19 to R21, section 17).** Shipped as written in commit 8b1efa5; the build card t_4749555c replaces this stub with the act-two sequence. Kept here for history.
- **Source:** [Nick] "we can talk more about what comes with 'indulge me' after"; [Card] "TBD, out of scope for this card."
- **Acceptance:** red pill is a `<button type="button">`; click it: `location.href` unchanged, and an element with `aria-live="polite"` now has `textContent.trim() === "Coming soon. Take the blue pill for now."`.
- **Edge cases:** clicking it repeatedly does not duplicate the message; keyboard Enter and Space both trigger it; the message wraps cleanly at 320px.
- **Resources:** `intro.html` inline script.

### R11. The page works at desktop and mobile sizes with no horizontal overflow, pills stack under 560px, and touch targets are at least 44px.
- **Source:** [Nick] "It needs to be desktop and mobile friendly."; [Card] section 4.
- **Acceptance:** at 1440x900, 768x1024, 390x844, 320x568 and 844x390, at p = 0%, 50% and 100%: `document.documentElement.scrollWidth <= innerWidth`; at 390 wide the two pills' bounding boxes stack (red `bottom` ≤ blue `top`) and each is ≥ 52px tall; at 1440 wide they sit on one row (equal `top` within 2px); `grep -c "svh" intro.html` ≥ 1 and `grep -c "dvh" intro.html` = 0; at 390x844 a CDP touch swipe (`Input.dispatchTouchEvent` start at y=700, move to y=200, end) increases `scrollY`.
- **Edge cases:** iOS URL bar collapse does not make scenes jump (`svh`); landscape phone keeps the logotype inside the viewport; nudge clears the safe-area inset; hover lift does not apply on touch (`@media (hover:hover)` present in source).
- **Resources:** `intro.html` CSS.

### R12. With reduced motion, nothing animates on scroll and the page is fully usable.
- **Source:** [Card] section 6 "users with prefers-reduced-motion should get a non-animated equivalent."
- **Acceptance:** with reduced motion emulated, JS check: `document.getAnimations().filter(a => a.timeline && a.timeline.constructor.name === "ScrollTimeline").length === 0`; every scene section has computed opacity `"1"` and transform `"none"`; scrolling from top to bottom shows each scene in normal document flow (each section's `offsetTop` is distinct and increasing); the nudge still appears after 4500ms with computed `transitionDuration` ≤ `0.01s`; blue pill still navigates (R9 check passes).
- **Edge cases:** the user toggles reduced motion while the page is open: the media query applies live with no reload; smooth-scroll from the nudge becomes an instant jump.
- **Resources:** `intro.html` CSS and script.

### R13. Keyboard and screen-reader users can skip straight to the site in one step and never land focus on something invisible.
- **Source:** [Card] section 6 "keyboard/screen-reader path to skip straight to the current site."
- **Acceptance:** from a fresh load, one `Tab` focuses an `<a>` with text `Skip intro, go to the site` and `href="index.html"` that is visible when focused (bounding box inside the viewport, opacity 1); with `scrollY = 0`, `document.querySelector(<blue pill>).focus()` then wait 1000ms: the pill's bounding box is fully inside the viewport and its computed opacity > 0.95; at `scrollY = 0`, `document.elementFromPoint` at the red pill's center (computed from its bounding box) does **not** return the red pill or the blue pill (pointer gating); the page has `<html lang="en">`, one `<main>`, three `<section>` elements with `aria-label`, one `<h1>`.
- **Edge cases:** Tab order is skip link, nudge (if visible), red pill, blue pill; focus outline visible on every focusable element (`outline-style` not `none` on `:focus-visible`); VoiceOver reads the h1 as one sentence.
- **Resources:** `intro.html`.

### R14. Fonts and colors come only from the existing system plus the two pill tokens.
- **Source:** [Card] "reuse these, don't invent new ones unless the PRD explicitly calls for a new logotype treatment."
- **Acceptance:** `grep -o "fonts.googleapis.com/css2[^\"]*" intro.html` returns exactly the URL in section 1; `grep -oiE "#[0-9a-f]{6}" intro.html | sort -u` returns only `#EAEEE4 #F8FAF4 #16241C #3B5245 #6E8270 #C8D3BE #2F5B44 #7E9C60 #9A3B2E #2E4A6B` (case-insensitive) plus any `#CFE2A6`/`#B0703A` only if copied in the unchanged `:root` block.
- **Edge cases:** no `@import` of other fonts; no Courier added; no locally hosted font files.
- **Resources:** `intro.html` `<head>`.

### R15. The page has a proper document head.
- **Source:** assumption, mirrors `index.html` conventions [index.html lines 1 to 12].
- **Acceptance:** `grep -c '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">' intro.html` = 1; `<title>` is `Nicholas Pings Rodriguez · Welcome`; `<meta name="description">` present; `color-scheme: only light` in `:root`.
- **Edge cases:** `viewport-fit=cover` is required for the safe-area inset on the nudge (R6/R11).
- **Resources:** `intro.html`.

---

## 8. Deployment and build

**Not Docker, by justified exception.** Nick's standing rule is Docker for every project except homelab and agent-town. This project is a static site served by GitHub Pages (README: "Hosted for free on GitHub Pages"). There is no server process, runtime or dependency to put in a container, and production deploy is a `git push` to `main`, which this card and the build card both forbid. A container would add infrastructure with nothing inside it to run.

- **Local preview:** `python3 -m http.server 8000` from the repo root on `feature/intro-experience`, as the build card t_48cb87aa already specifies. Demo URL: `http://localhost:8000/intro.html`.
- **Build step:** none. One HTML file with inline CSS and JS.
- **Production:** nothing ships. The branch stays local until Nick approves.
- If Nick prefers the preview containerized anyway, the drop-in is `docker run --rm -p 8000:80 -v "$PWD":/usr/share/nginx/html:ro nginx:alpine`. Flagged in section 9.

---

## 9. Flags for Nick

1. **Docker exception.** This PRD runs the local preview with `python3 -m http.server`, not Docker, because the site is static GitHub Pages (section 8). Say if you want the nginx container instead.
2. **Should the intro become the front door later?** For now it is `intro.html` and nickpings.com still opens on the current page. Making it the root is a later rename plus five back-link edits.
3. **Two new colors.** The site has no red or blue, so the pills get `#9A3B2E` (brick) and `#2E4A6B` (slate). They are muted to fit the green palette. If you want true Matrix red/blue, say so.
4. **Copy tweak.** Your brief has "myself…." (four dots). I set it as "myself…" with "Or we can get right to business." on its own line.
5. **Red pill stub copy.** I wrote "Coming soon. Take the blue pill for now." as placeholder text. Change it freely.
6. **Real-device check.** Verification is browser emulation on this Mac. A 2-minute check on your own iPhone is the only way to confirm iOS momentum scroll and the URL-bar behavior feel right.
7. **No BACKLOG.md in this repo.** AGENTS.md says to ask you before creating one, so follow-ups are listed in section 12 instead.

No ongoing cost, no new services, no recurring manual steps.

---

## 10. Feasibility (spike method) and risks

Feasibility questions, ordered by risk, closed with verdicts:

| # | Given / When / Then | Verdict | Evidence |
|---|---|---|---|
| F1 | Given a static page, when it uses `animation-timeline: scroll()`, then current Chrome, Safari and Firefox scrub it natively. | VALIDATED | Baseline since 2026-10-27: Chrome/Edge 115, Safari 26, Firefox 159 [Research]. |
| F2 | Given Google Fonts, when the URL requests Fraunces `ital,opsz,wght,SOFT,WONK`, then it serves CSS. | VALIDATED | `curl` of the section 1 URL returned HTTP 200 [Probe, 2026-11-12]. |
| F3 | Given the new pill fills, when labels are `#F8FAF4`, then contrast passes WCAG AA. | VALIDATED | Computed: red 6.57:1, blue 8.65:1; `--rec` would be 3.82:1 (fail) [Probe]. |
| F4 | Given iOS Safari, when the stage is `position:sticky; height:100svh`, then it does not jump as the URL bar collapses. | PARTIAL | `svh` is designed for exactly this and is widely supported; emulation can't reproduce the real URL bar. Needs Flag 6. |

Risks:

- **Older browsers (pre-Firefox 159, pre-Safari 26):** get the R4 discrete crossfade, not scrubbing. Acceptable; Baseline is "newly available," so keep the fallback.
- **`overflow:hidden` on `html`/`body`** (the homepage uses it, [index.html line 30]) silently breaks sticky and the root scroll timeline. The builder must not copy that line; use `overflow-x:clip`.
- **Invisible scene-3 pills catching taps** during scenes 1 and 2. Mitigated by R13's pointer gating.
- **Extra font weight:** the Fraunces italic + Soft/Wonk axes add one more font file to the intro only. Acceptable; `display=swap` prevents invisible text.
- **The nudge feeling naggy:** 4s, once per load, and gone after first scroll limits it.
- **The pill gag could read as costume rather than craft** if the gloss is overdone. Section 3.4 keeps it to one inset highlight and one soft shadow.

---

## 11. Non-goals (do not build)

- Anything behind "indulge me" beyond the R10 stub line (no new page, no scenes, no experience or work-philosophy content yet). *(Addendum: now narrowed. "Indulge me" leads through the fork scene in section 17 and stops there; see section 18.4 for the updated non-goals.)*
- Any change to `index.html`, the case-study pages, `resume.html`, `README.md`, `CNAME` or `AGENTS.md`.
- Making the intro the site root, redirects, or a link to the intro from the homepage.
- "Skip intro next time" memory (cookies, localStorage, sessionStorage).
- Analytics, the homepage's Observer panel, or any tracking.
- SVG/PNG export of the logotype, favicon or social-card changes.
- Sound, video, canvas, WebGL, cursor effects, preloaders or page-transition animations into `index.html`.
- Dark mode.
- Any JS library, CDN script, `package.json`, `node_modules` or build tooling.
- Opening a PR, pushing to `main`, or merging to `main`. (Pushing `feature/intro-experience` itself to origin is allowed as a backup.)

**Authorized boundaries:** create `intro.html` at the repo root of `~/Documents/github/portfolio` on branch `feature/intro-experience`, commit to that branch, `git push origin feature/intro-experience` as a backup (Nick, 2026-11-12: Pages builds only from `main`), run a local static server for the demo.

**Forbidden actions:** editing any existing file in the repo; pushing any branch other than `feature/intro-experience`; committing to or merging into `main`; adding dependencies; adding a container or any always-on service other than the demo preview server the build card asks for.

---

## 12. Follow-ups (not requirements; for BACKLOG.md once Nick approves creating one)

- Define and build the "indulge me" path (the walk through experience and work philosophy).
- Decide whether the intro becomes the nickpings.com root (Flag 2).
- Optional persistent, always-visible "skip intro" link if user testing shows people want it.

---

# Addendum: pill-scene polish and the "indulge me" fork scene (card t_fb2bf2d9)

Added 2026-11-12 by product. Builds on the shipped, Crit-passed `intro.html` (commit 8b1efa5). Same harness, tokens, fonts and conventions as sections 1 to 12 unless a line below says otherwise. Build card: t_4749555c (assignee `design`).

## 13. Addendum source, scope and what it changes

### 13.1 Source brief (Nick, verbatim, via card t_fb2bf2d9)

> **Part A.** On the pill page we should have it say 'what'll it be? The choice is yours.' Over the pills. Give it a little separation from the text above as well. Make the red pill appear to glow little bit. We are going for 'tempting.'
>
> **Part B.** Ok, indulge me will launch into a continuation of this experience that goes through a 'choose your own adventure' prompt. Immediately after someone clicks 'indulge me' the briefly get 'I knew I liked you.' And then a 'curtain' raises to reveal the next screen. The next screen is a a fork in the road visualization with a pixelated avatar facing the fork. The top of the screen reads 'where should we start?' And the three fork prongs are 'research' 'technology' and 'passion.' We will talk about each of the prongs after.

Citation shorthand added for the addendum: **[Nick-A]** / **[Nick-B]** = Part A / Part B above. **[Card2]** = card t_fb2bf2d9's body (scope boundary and the six items it requires). **[intro.html]** = the shipped file at commit 8b1efa5. **[Spike]** = the throwaway prototype I ran for this addendum; results in section 18.3.

### 13.2 Scope boundary: the three prongs are stubs

This pass builds **up to and including** the fork scene: the headline, the road, the avatar and three labeled, clickable-looking prongs. **What each prong leads to (research, technology, passion) is out of scope** [Nick-B: "We will talk about each of the prongs after."]. Each prong is a stub: activating it announces a "coming soon" line (R26) and goes nowhere. This is the same pattern the red pill followed before this card (R10). The prong content is logged as follow-ups in BACKLOG.md, not specified here.

### 13.3 What this changes in sections 1 to 12

| Earlier decision | Change |
|---|---|
| R10 (red pill shows "Coming soon. Take the blue pill for now.") | **Superseded** by R19 to R21. The `#stub` paragraph and that string are removed. |
| Section 11, first non-goal ("nothing behind indulge me") | Narrowed: the act-two sequence through the fork scene is now in scope; everything past the fork stays a non-goal (section 18.4). |
| Section 4, item 8 (one inline script, under 120 lines) | Raised to **under 220 lines**, still one inline script, still no external scripts (R31). |
| Section 1 / R14 palette | Adds one hex (`#C9946E`, avatar skin) and two rgb-triplet glow tokens; puts the existing `--leaf` `#CFE2A6` to use (R31). |
| Section 3: "There is no footer and nothing after scene 3." | Still true for the **scroll track**. Act two is a click-triggered layer on top of it, not more scroll (section 14). |

### 13.4 Map to the card's six required items

| Card item | Decided in |
|---|---|
| 1. Pill-scene polish (copy, font, spacing, glow values) | Section 16, R16 to R18 |
| 2. Transition sequence (line, curtain, timing, easing) | Section 17.2, R19 to R21 |
| 3. Fork scene (headline, avatar approach, road, prong styling) | Section 17.3, R22 to R26 |
| 4. Where it lives | Section 14, R27 |
| 5. Responsive notes | Section 17.4, R28 |
| 6. Accessibility (reduced motion, stub announcements) | Section 17.5, R29, R30 |

---

## 14. Where the continuation lives (card item 4)

**Decision: inside `intro.html`, as a click-triggered "act two" layer that sits on top of the scroll track. Not appended to the scroll sequence, and not a new file.**

| Option | One-line tradeoff |
|---|---|
| A. Append new scenes to the scroll track (p > 100%) | Breaks the gag: a visitor could scroll past the pills into "indulge me" content without choosing, and it changes the scroll budget every R3/R11 check is written against. Rejected. |
| B. New file (`intro-indulge.html`), red pill navigates to it | A full page load lands between "I knew I liked you." and the curtain, so the reveal flashes white mid-sequence; it also duplicates the whole `<head>`, tokens and fonts. Rejected. |
| **C. Same file, fixed overlay layer revealed by the red pill** | One continuous moment (click, line, curtain, fork) with no load; fonts already loaded; the scroll mechanic stays exactly as Crit passed it. Chosen. |

Mechanics of C:

1. A new `<section class="act2" id="where" aria-labelledby="where-title" hidden>` sits **after `</main>`**, so R2/R12/R13's "sections inside `main`" checks keep counting only the three scroll scenes.
2. Act two is `position:fixed; inset:0; z-index:15` (above the nudge at 10, **below the skip link at 20**, so "Skip intro, go to the site" stays usable on top of it), `background-color:var(--paper)`, `overflow-y:auto`, `overscroll-behavior:contain`.
3. While act two is open, `main` gets the `inert` attribute. The page **never** sets `overflow:hidden` on `html`/`body` (section 10 risk; R3 check). If the document scrolls underneath, nothing is visible and closing restores it (R27).
4. The URL gains `#where` via `history.pushState` when the sequence starts, so Back returns to the pill scene and `intro.html#where` opens the fork scene directly (R27). This is cheap, and it makes Nick's review and Crit's tests direct.
5. No ADR: this choice is local to one file and cheap to reverse (same reasoning as section 4).

---

## 15. New tokens and the avatar asset decision

**Asset check (card item 3).** I searched the repo for an existing avatar, headshot or pixel image: `git ls-files` with an image-extension filter returns only `eva-contextual-cta.png` and `eva-evergreen-cta.jpeg` (case-study screenshots), and `index.html` has no `<img>` of Nick (only two commented-out logo placeholders, lines 486 and 508). **There is no avatar asset to reuse, so the avatar is drawn from scratch.**

**Avatar technique, decided: inline SVG, `<rect>` per pixel, built at runtime from a 12×16 character map in the inline script.**

| Approach | Tradeoff |
|---|---|
| CSS `box-shadow` pixel grid | No markup, but one giant unreadable declaration; scaling it means rewriting every offset; can't share a pixel grid with the road. |
| Pre-made PNG | Needs an image file (a new site file) and image-editing tooling; blurs unless `image-rendering:pixelated`; Nick can't tweak it in a text editor. |
| **Inline SVG rects from a char map** | Crisp at any size with `shape-rendering="crispEdges"`, shares one coordinate grid with the road, and the char map in section 17.3 is the editable source of truth. Act two only exists with JS anyway (R19), so building the rects in JS costs nothing in the no-JS case. **Chosen.** |

**New tokens (intro.html `:root` only):**

| Token | Value | Use |
|---|---|---|
| `--glow-ember` | `196,84,58` (rgb triplet, = `#C4543A`) | inner ring of the red-pill glow, used as `rgba(var(--glow-ember), a)` |
| `--glow-warm` | `222,132,84` (rgb triplet, = `#DE8454`) | outer haze of the red-pill glow |
| `--px-skin` | `#C9946E` | avatar neck and hands only. **Placeholder, Flag A3.** |

Existing tokens newly used: `--leaf` `#CFE2A6` (the period of "I knew I liked you." on the red curtain); `--pill-red`, `--pill-blue`, `--pine` as the three prong colors.

---

## 16. Pill-scene polish (Part A)

### 16.1 The prompt line

- **Copy:** `What’ll it be? The choice is yours.` One `<p class="prompt" id="choice-prompt">`, typographic apostrophe (U+2019, `&rsquo;`), sentence case. Nick typed "what'll" lowercase inside quotes; the card capitalizes it, and it opens a sentence, so it is capitalized. Flag A1.
- **Placement:** in scene 3, **between `.or` and `.pills`**, centered. It labels the pill group: `.pills` gets `role="group" aria-labelledby="choice-prompt"`.
- **Font, decided: Fraunces, not EB Garamond.** `font-family:"Fraunces",Georgia,serif; font-weight:500; font-style:normal; font-variation-settings:"opsz" 24, "SOFT" 100; font-size:clamp(18px,1.9vw,22px); line-height:1.3; letter-spacing:.01em; color:var(--ink); text-wrap:balance`.
- **Why Fraunces:** the line directly above (`.or`) is EB Garamond italic. Another Garamond italic line would read as the *same* sentence continuing, which is the opposite of the separation Nick asked for. Upright Fraunces at a small optical size is visibly a different voice (a label, not narration), and its Soft axis echoes the red pill's soft Fraunces italic, so the prompt quietly leans toward "indulge me". Size sits well below `.ask` (64px) and `.or` (38px), so the hierarchy stays: statement, aside, prompt, choice.

### 16.2 Separation from the text above

- `.prompt { margin: clamp(40px, 7svh, 72px) 0 0; }` (the gap from `.or`).
- `.pills { margin-top: clamp(14px, 2svh, 20px); }` (was `clamp(30px,5svh,56px)`; the prompt now carries the big gap).
- Result: the prompt sits 3 to 4× farther from the text above than from the pills, so it groups with the pills (proximity). Measured in the spike: 63px / 18px at 1440×900; 59px / 17px at 390×844; 40px / 14px at 320×568 [Spike].
- **Short screens** (`@media (max-height:500px)`, landscape phones): `.scene-3 { padding-block: 16px; } .prompt { margin-top: 18px; } .pills { margin-top: 10px; }`. Without this the extra line pushes the pills out of a 390px-tall viewport, and the stage's `overflow:clip` would cut them off silently.
- No rule, ornament or divider. Spacing alone does it.

### 16.3 The red-pill glow ("tempting")

Soft, warm and breathing slowly, like an ember, not a neon tube. It lives on a pseudo-element so only `opacity` animates (section 4 item 3: compositor-only animation).

```css
.pill-red{ position:relative; }            /* new: anchors the glow layer */
.pill-red::before{
  content:""; position:absolute; inset:0; border-radius:inherit; pointer-events:none;
  box-shadow:
    0 0 18px 2px  rgba(var(--glow-ember), .38),
    0 0 44px 10px rgba(var(--glow-warm),  .20);
  opacity:.85;                              /* static value: reduced motion, no JS */
}
@media (prefers-reduced-motion:no-preference){
  .pill-red::before{ animation: ember 3.2s ease-in-out infinite alternate; }
}
@keyframes ember{ from{opacity:.55;} to{opacity:1;} }

/* on intent, it warms fully and holds */
@media (hover:hover){ .pill-red:hover::before{ animation:none; opacity:1; } }
.pill-red:focus-visible::before{ animation:none; opacity:1; }
```

- The existing pill `box-shadow` (gloss highlight + drop shadow) stays on `.pill` unchanged; the glow is additive.
- **Not neon, by construction:** alpha never above `.38`, blur never under 18px, no saturated hues (the glow colors are the pill's own brick lifted toward amber), no `text-shadow`, no flicker, one slow 6.4s breath cycle.
- **The blue pill gets no glow.** The asymmetry is the point.
- Spike render: 8px outside the red pill the paper shifts from `rgb(234,238,228)` to `rgb(229,218,204)` (visibly warm); 8px outside the blue pill it stays `rgb(232,236,226)`; by 30px the glow has faded back to paper. An image check described it as "a diffuse warm halo… soft amber/tan rather than a bright saturated red… subtle and tempting, not harsh neon" [Spike].

### 16.4 Requirements, Part A

All addendum requirements use the section 7 harness (local `python3 -m http.server 8000`, Chromium over CDP, the same desktop/mobile/reduced-motion emulation). "At the pill scene" means `scrollTo(0, scrollHeight)` then two animation frames. Build/deployment for every addendum requirement: **not Docker**, same justified exception as section 8 (static GitHub Pages site, nothing to containerize).

### R16. Scene 3 shows "What’ll it be? The choice is yours." between the two copy lines and the pills, in upright Fraunces.
- **Source:** [Nick-A] "have it say 'what'll it be? The choice is yours.' Over the pills."; [Card2] item 1; font choice reasoning in 16.1.
- **Acceptance:** at the pill scene, JS check: `document.getElementById('choice-prompt').textContent === "What\u2019ll it be? The choice is yours."`; its computed `fontFamily` starts with `"Fraunces"`, `fontStyle === "normal"`, `fontWeight === "500"`; DOM order is `.or`, then `.prompt`, then `.pills` (`or.compareDocumentPosition(prompt) & 4` and `prompt.compareDocumentPosition(pills) & 4` both truthy); `.pills` has `role="group"` and `aria-labelledby="choice-prompt"`; the prompt's horizontal center is within 4px of the red/blue pill group's horizontal center.
- **Edge cases:** a straight apostrophe (`'`) fails the check, so the build must use U+2019; at 320px wide the line may wrap to two balanced lines but never overflows (`scrollWidth <= innerWidth`); if Fraunces fails to load it falls back to Georgia and keeps its spacing; with no JS / reduced motion the prompt appears in the static stack (R2's text list gains this string).
- **Resources:** `intro.html` scene 3 markup and CSS.

### R17. The prompt is clearly separated from the text above and grouped with the pills, at every size, without pushing the pills off a short screen.
- **Source:** [Nick-A] "Give it a little separation from the text above as well."; values in 16.2.
- **Acceptance:** at the pill scene, JS check with `gapAbove = prompt.top − or.bottom` and `gapBelow = redPill.top − prompt.bottom` (bounding rects): at 1440×900 `gapAbove` between 56 and 76 and `gapBelow` between 14 and 22; at 390×844 `gapAbove` ≥ 40 and `gapBelow` between 12 and 22; at every tested size `gapAbove ≥ 2.5 × gapBelow`. At 844×390, `gapAbove` ≥ 16, the blue and red pills' `bottom` ≤ `innerHeight`, and the `.ask` line's `top` ≥ 0. `grep -c "clamp(40px, *7svh, *72px)" intro.html` ≥ 1.
- **Edge cases:** landscape phone (844×390, 667×375): short-screen rules in 16.2 apply and nothing is clipped by the stage; tablet 768×1024 keeps the desktop ratios; the static stack (reduced motion) keeps the same margins.
- **Resources:** `intro.html` CSS.

### R18. The red pill has a soft, warm, slowly breathing glow, and the blue pill does not.
- **Source:** [Nick-A] "Make the red pill appear to glow little bit. We are going for 'tempting.'"; values in 16.3.
- **Acceptance:** (a) JS check: `getComputedStyle(redPill, '::before').boxShadow` contains `rgba(196, 84, 58, 0.38)` and `rgba(222, 132, 84, 0.2)`; `getComputedStyle(bluePill, '::before').content` is `"none"` or its `boxShadow` is `"none"`. (b) Motion allowed: `document.getAnimations().some(a => a.animationName === "ember")` is true and its effect timing is `duration 3200`, `iterations Infinity`, `direction "alternate"`. (c) **Rendered-pixel check** with reduced motion emulated (glow static at opacity .85): `Page.captureScreenshot` at 1440×900, deviceScaleFactor 1, at the pill scene; decode the PNG (Python stdlib `zlib`+`struct`, as the spike did, or any PNG reader); the pixel 8px left of the red pill's left edge at its vertical center has `R − G ≥ 6`, and the pixel 8px right of the blue pill's right edge at its vertical center has `R − G ≤ −2` (paper is `234,238,228`). (d) Hovering the red pill (CDP `Input.dispatchMouseEvent` mouseMoved to its center) makes the `::before` computed `opacity === "1"`.
- **Edge cases:** reduced motion: glow present but static (no `ember` animation in `getAnimations()`); the glow must not count toward page width (`scrollWidth <= innerWidth` at 320 and 390, where the full-width pill's glow reaches the screen edge); the glow is invisible while scene 3 is faded out because it inherits the scene's opacity; label contrast is unchanged (`#F8FAF4` on `#9A3B2E`, 6.57:1).
- **Resources:** `intro.html` CSS (`.pill-red`, new tokens).

---

## 17. Indulge-me continuation (fork scene) (Part B)

### 17.1 Structure

```html
<!-- after </main> -->
<section class="act2" id="where" aria-labelledby="where-title" hidden>
  <div class="fork-scene">                         <!-- inert while the curtain is down -->
    <h2 id="where-title" tabindex="-1">Where should we start?</h2>
    <div class="fork">
      <div class="prongs" role="group" aria-labelledby="where-title">
        <button type="button" class="prong" data-prong="research"   aria-describedby="fork-soon">research</button>
        <button type="button" class="prong" data-prong="technology" aria-describedby="fork-soon">technology</button>
        <button type="button" class="prong" data-prong="passion"    aria-describedby="fork-soon">passion</button>
      </div>
      <svg class="road" viewBox="0 0 120 80" shape-rendering="crispEdges"
           preserveAspectRatio="xMidYMax meet" role="img"
           aria-label="A pixel-art figure, seen from behind, standing where a road splits three ways.">
        <!-- road rects (17.3.2), then <g class="avatar"><g class="avatar-body">…</g></g> -->
      </svg>
    </div>
    <p class="fork-status" id="fork-status" role="status" aria-live="polite"></p>
    <span class="vh" id="fork-soon">Coming soon.</span>
  </div>
  <div class="curtain">
    <p class="liked" tabindex="-1">I knew I liked you<span class="dot">.</span></p>
  </div>
</section>
```

The red pill keeps its element (`<button type="button" id="pill-red">`) and its text. Its click handler changes from the R10 stub to "start act two". The `#stub` paragraph and its string are deleted.

State machine (one variable in the inline script): `closed → playing → open`, plus `open → closed` on Back. Clicks on the red pill are ignored unless the state is `closed`.

### 17.2 Transition sequence (card item 2)

Times are milliseconds from the red-pill click.

| t (ms) | What happens | Technique |
|---|---|---|
| 0 | State `playing`. `history.pushState({act:2}, "", "#where")`. `main.inert = true`. Act two un-hides with `.fork-scene` inert. `.act2` gets class `is-playing`. Focus moves to `.liked` (`focus({preventScroll:true})`) so screen readers speak the line. | JS |
| 0 to 280 | **Curtain drops in:** the curtain fades from opacity 0 to 1. ("Immediately", per Nick.) | `curtain-in 280ms ease-out both` |
| 250 to 750 | **"I knew I liked you." appears** on the curtain: opacity 0 to 1, rises 12px. | `liked-in 500ms cubic-bezier(.22,.7,.2,1) 250ms both` |
| 750 to 2250 | **Hold.** The line is fully readable for 1.5s (five words; "briefly" per Nick, long enough to read twice). | none |
| 2250 to 3150 | **Curtain raises.** One panel translates straight up off the top of the screen, the line riding up with it, revealing the fork scene already sitting underneath. Slow start, slow stop, like a heavy theater curtain on a fly line. | `curtain-raise 900ms cubic-bezier(.7,0,.2,1) 2250ms both`, `transform: translateY(0)` to `translateY(calc(-100% - 48px))` (the extra 48px carries the hem shadow fully off screen) |
| 3150 | **End step** (on `animationend` for `curtain-raise`, or a 3600ms safety timeout, whichever comes first): `curtain.hidden = true`, `.fork-scene` inert removed, state `open`, focus moves to `#where-title`, prong pop-in (17.3.4) starts. | JS |

Why a single panel moving up, not two panels parting: Nick said the curtain *raises*. Two halves sliding apart is a curtain *opening*. A single fly-curtain going up is also simpler (one transform, one element).

**The curtain itself:**

```css
.curtain{
  position:absolute; inset:0; z-index:2;
  display:grid; place-items:center; padding:0 var(--pad); text-align:center;
  background-color:var(--pill-red);
  background-image:repeating-linear-gradient(90deg,
    rgba(22,36,28,0) 0px, rgba(22,36,28,.16) 28px, rgba(22,36,28,0) 56px);   /* soft pleats */
  box-shadow: inset 0 -10px 0 rgba(22,36,28,.28),                        /* hem */
              0 18px 36px -12px rgba(22,36,28,.45);                      /* weight under the hem */
}
.curtain[hidden]{ display:none; }
```

It is the red pill's own color: the visitor took the red pill and the room turns red.

**"I knew I liked you." style:** `.liked { margin:0; max-width:14ch; font-family:"Fraunces",Georgia,serif; font-style:italic; font-weight:400; font-variation-settings:"opsz" 144, "SOFT" 100, "WONK" 1; font-size:clamp(36px,7vw,88px); line-height:1.05; letter-spacing:-.01em; color:var(--card); text-wrap:balance; }`. Same soft, wonky italic as the "indulge me" label, so it reads as the red pill answering back. The period is `<span class="dot">` colored `--leaf` `#CFE2A6` (the site's light green; `--moss` would disappear on brick), continuing the green-period signature from `welcome.` and `Nick.`. Text contrast `#F8FAF4` on `#9A3B2E` is 6.57:1 [section 1 probe].

**How it dismisses:** it does not fade out separately. It leaves with the curtain as the curtain raises (2250 to 3150ms).

**Skip (impatient visitors):** from t = 400ms until the raise starts, a `pointerdown` on the curtain or a `keydown` of Escape, Enter or Space starts the raise immediately: find the `curtain-raise` animation via `curtain.getAnimations()` and set its `currentTime` to `2250`; set `liked-in`'s `currentTime` to its end. The 400ms arming delay stops the key press that activated the red pill from also skipping. Skip fires once.

### 17.3 Fork scene (card item 3)

Layout: `.fork-scene { min-height:100%; display:grid; grid-template-rows:auto 1fr auto; justify-items:center; text-align:center; padding: max(env(safe-area-inset-top), clamp(28px,7svh,80px)) var(--pad) calc(clamp(20px,4svh,40px) + env(safe-area-inset-bottom)); }`. Row 1: headline at the top. Row 2: the fork, vertically centered in the remaining space (`align-self:center`). Row 3: the status line.

#### 17.3.1 Headline

`Where should we start?` in an `<h2 id="where-title" tabindex="-1">` (the page keeps its single `<h1>`, scene 2). Fraunces 500, `clamp(30px,5vw,56px)`, `line-height:1.08`, `letter-spacing:-.015em`, `--ink`, `margin:0`, `text-wrap:balance`, matching scene 3's `.ask` so act two feels like the same voice. Sentence case for the same reason as the prompt (Flag A1). No focus ring on the heading when it receives programmatic focus (`#where-title:focus{outline:none}`): it is not interactive.

#### 17.3.2 The road (fork visual)

One inline SVG, `viewBox="0 0 120 80"`, every coordinate an integer so each user unit is one "pixel". `.road { display:block; width:100%; aspect-ratio:3/2; }`. Drawing order: all edge rects, then all fill rects, then dashes, then tufts, then the avatar.

- **Trunk:** fill rect `(55, 56, 10, 24)` (x, y, w, h), runs off the bottom edge so the road continues toward the viewer.
- **Center prong (technology):** fill rect `(55, 0, 10, 56)`.
- **Left prong (research):** for k = 1 to 28, fill rect `(x, 56 − 2k, 10, 2)` with `x = floor(55 − 1.9k + 0.5)`. Ends at x = 2 at the top edge.
- **Right prong (passion):** same, `x = floor(55 + 1.9k + 0.5)`. Ends at x = 108.
- **Edges:** for every fill rect `(x, y, w, h)` an edge rect `(x − 1, y, w + 2, h)` in `--muted` `#6E8270`, drawn first, so the road reads clearly against the paper (the spike's version without edges was too faint).
- **Fill color:** `--card` `#F8FAF4`.
- **Center dashes, one color per prong:** technology: rects `(60, y, 1, 4)` for y = 2, 8, 14 … 44, in `--pill-blue` `#2E4A6B`. Research: on the left-prong step k (k ≥ 4, k mod 3 ≠ 0), rect `(x + 5, 56 − 2k, 1, 2)` in `--pine` `#2F5B44`. Passion: same on the right prong in `--pill-red` `#9A3B2E`. No dashes below y = 48, so the junction stays clean.
- **Grouping:** each prong's fills and dashes sit in `<g data-prong="research|technology|passion">`; trunk and edges in `<g data-part="trunk">` / `<g data-part="edges">`.
- **Grass tufts:** eight 3-pixel tufts in `--moss` `#7E9C60`, shape `(x, y+1), (x+1, y), (x+2, y+1)`, at (10,60), (28,72), (38,46), (34,12), (110,60), (92,72), (82,46), (86,12). All verified clear of the road.
- **Avatar shadow:** rect `(55, 78, 10, 1)` in `--rule` `#C8D3BE`.

Why these prong colors: technology = the blue pill's blue (blue already means "technical" on this page); passion = the red pill's red (red already means "indulge"); research = `--pine`, the site's own green, because research is Nick's home field. This is an assumption and a design call (Flag A4).

#### 17.3.3 The pixel avatar

Back view (the visitor sees the figure from behind, so it is facing the fork). 12 × 16 pixels, origin at (54, 62) in road coordinates, so it stands on the trunk just below the split. Built by the inline script from this map (one `<rect width="1" height="1">` per non-`.` character):

```
....HHHH....
...HHHHHH...
..HHHHHHHH..
..HHHHHHHH..
..SHHHHHHS..
...HHHHHH...
....SSSS....
..GGRRRRGG..
.GGRRRRRRGG.
.GGRRRRRRGG.
.SGRRRRRRGS.
..GGRRRRGG..
...BBBBBB...
...BB..BB...
...BB..BB...
..KKK..KKK..
```

Key: `H` hair `#16241C` (`--ink`), `S` skin `#C9946E` (`--px-skin`, placeholder), `G` shirt `#2F5B44` (`--pine`), `R` backpack `#9A3B2E` (`--pill-red`, the adventurer's pack), `B` trousers `#2E4A6B` (`--pill-blue`), `K` shoes `#16241C`.

- Rendered size: 6px per pixel at the 720px desktop fork (72 × 96px figure), about 2.9px per pixel at 390px wide (about 46px tall) [Spike].
- **Idle:** the inner `<g class="avatar-body">` hops up 1 unit and back, `@keyframes idle{0%,100%{transform:none}50%{transform:translateY(-1px)}}`, `animation: idle 1.6s steps(1,end) infinite`. Stepped, not eased, so it moves like a sprite.
- **Looks toward a prong:** the outer `<g class="avatar">` gets `data-look="research|technology|passion"` while a prong is hovered (pointer devices) or focused, and keeps it after a prong is activated until another one is. `research`: `transform:translate(-2px,0)`; `technology`: `translate(0,-1px)`; `passion`: `translate(2px,0)` (user units). `transition: transform .2s steps(2)`. Cleared on `pointerleave`/`blur` unless that prong was the last activated.
- A screenshot check of the spike read it as "a person standing with their back to us, deciding which way to go"; it also noted the backpack can read as a red shirt at small sizes, which is acceptable [Spike].

#### 17.3.4 The three prongs (clickable-looking stubs)

Labels are lowercase exactly as Nick wrote them: `research`, `technology`, `passion`, in that order, left to right. They sit in one flex row directly above the road so each label caps the end of its path: `.prongs { display:flex; justify-content:space-between; align-items:flex-end; gap:8px; flex-wrap:nowrap; margin:28px 0 6px; }`. The first chip anchors left over the left prong's end (x ≈ 2 to 12), the middle centers over the straight prong, the last anchors right over the right prong's end (x ≈ 108 to 118).

**Font, decided: IBM Plex Mono 500.** The scene is pixel art, and a choose-your-own-adventure menu reads as a game menu; Plex Mono is the only family on the site with that terminal/8-bit voice.

```css
.prong{
  --prong-c: var(--pine);                       /* research */
  position:relative; min-height:44px; padding:10px 16px;
  font-family:"IBM Plex Mono",monospace; font-weight:500; font-size:16px; letter-spacing:.04em; line-height:1.2;
  color:var(--ink); background-color:var(--card);
  border:2px solid var(--ink); border-radius:0;          /* square, pixel corners */
  box-shadow:4px 4px 0 0 var(--prong-c);                 /* hard pixel drop shadow = a raised key */
  cursor:pointer; -webkit-tap-highlight-color:transparent;
  transition: transform .12s steps(2), box-shadow .12s steps(2);
}
.prong[data-prong="technology"]{ --prong-c: var(--pill-blue); }
.prong[data-prong="passion"]   { --prong-c: var(--pill-red); }
@media (hover:hover){
  .prong:hover{ transform:translate(-2px,-2px); box-shadow:6px 6px 0 0 var(--prong-c); }
}
.prong:focus-visible{ transform:translate(-2px,-2px); box-shadow:6px 6px 0 0 var(--prong-c);
                      outline:2px solid var(--pine); outline-offset:3px; }
.prong:active{ transform:translate(2px,2px); box-shadow:2px 2px 0 0 var(--prong-c); }

/* pixel pointer above the hovered/focused chip */
.prong::after{
  content:"\25BC"; position:absolute; left:50%; bottom:calc(100% + 6px);
  transform:translateX(-50%); font-size:10px; line-height:1; color:var(--prong-c);
  opacity:0; pointer-events:none;
}
@media (hover:hover){ .prong:hover::after{ opacity:1; } }
.prong:focus-visible::after{ opacity:1; }
@media (prefers-reduced-motion:no-preference){
  .prong:hover::after, .prong:focus-visible::after{ animation: caret 0.8s steps(1,end) infinite; }
}
@keyframes caret{ 0%,100%{ transform:translate(-50%,0); } 50%{ transform:translate(-50%,-2px); } }
```

- **Distinct:** each chip's shadow color matches its path's dash color (pine / blue / red), so the label and its road read as a pair.
- **Alive on touch screens too** (no hover there): when the fork scene is revealed, the chips pop in once, left to right, `@keyframes pop{from{transform:scale(.9);opacity:0}to{transform:none;opacity:1}}`, `animation: pop 240ms steps(3) backwards` with delays 0 / 120 / 240ms. Fill mode must be `backwards`, not `both`: a held `transform:none` would override the hover and focus lift. Plus the avatar idle. Reduced motion: no pop.
- **Stub behavior (R26):** activating a prong (click, tap, Enter, Space): sets the avatar's look, clears `#fork-status`, then on the next animation frame writes `<Label> is coming soon. I'm still paving that road.` (`Research is…`, `Technology is…`, `Passion is…`). Clearing first makes screen readers re-announce on a repeat activation. **No navigation, no new scene, no hash change.** Status line style: EB Garamond italic, `clamp(17px,1.6vw,19px)`, `--ink-soft` (not `--muted`, for AA contrast on paper), `min-height:1.6em`, `margin:16px 0 0`.
- **Why `aria-describedby` "Coming soon." and not `aria-disabled`:** `aria-disabled="true"` makes VoiceOver announce "dimmed", which contradicts chips that are deliberately styled to look live, and it tells people not to bother pressing them. Real, enabled buttons whose description says "Coming soon." are honest *and* consistent with how they look. A screen-reader user hears "research, button, Coming soon."

#### 17.3.5 Fork sizing

`.fork { align-self:center; width:min(100%, 720px, max(200px, calc((100svh - 300px) * 1.5))); }`. The road keeps its 3:2 ratio; the avatar scales with it.

### 17.4 Responsive (card item 5)

| Concern | Desktop (≥ 900px, wheel/trackpad) | Mobile (< 560px, touch) | Short screens (`max-height:500px`) |
|---|---|---|---|
| "I knew I liked you." | up to 88px, one or two lines (`max-width:14ch`) | 36px, two to three balanced lines | `clamp` floor 36px |
| Curtain | full viewport, pleats every 56px | same | same |
| Headline | up to 56px | 30px | 28px (`h2{font-size:28px}`) |
| Fork width | up to 720px (6px per pixel) | `100%` of padded width (≈346px at 390) | `min(100%, 400px)` |
| Prong chips | 16px, padding 10px 16px | 15px, padding 10px 12px; under 360px wide: 14px, padding 8px, letter-spacing 0 | 14px, padding 8px 10px, `.prongs` margin-top 12px |
| Chip height | ≥ 44px | ≥ 44px | ≥ 44px |
| Hover lift and pointer caret | under `@media (hover:hover)` | none; focus-visible still shows them | per device |
| Act-two padding | `clamp(28px,7svh,80px)` top | same, plus safe-area insets top and bottom | 16px top, 8px bottom |
| Overflow | none horizontal; act two scrolls vertically only if the content truly can't fit | same | same |

`svh` only, never `dvh` (section 5). Spike measurements, without the edge rects (which add no width): at 1440×900, 390×844 and 320×568 the three chips never overlap and stay inside the viewport; at 844×390, with the short-screen rules, the headline, all three chips and the avatar fit on one screen (avatar bottom at 373px of 390) [Spike].

### 17.5 Accessibility (card item 6)

- **Reduced motion:** no fade, no rise, no raise. The curtain and line appear instantly; after **1500ms** the curtain is removed in one cut (`hidden = true`) and focus moves to the headline. The global `@media (prefers-reduced-motion:reduce)` rule already in `intro.html` neutralizes every new animation; the reduced path is driven by a JS `setTimeout`, not `animationend` (which never fires when animations are off). Also off under reduced motion: the ember breathing (glow stays static at .85), avatar idle, chip pop-in, caret bob. The avatar look-shift becomes an instant 2-unit shift, which is a state change, not motion.
- **Skip still works** under reduced motion: a skip key or tap ends the 1500ms wait immediately.
- **Focus management:** click: focus to `.liked` (the line is announced). End step: focus to `#where-title` (the headline is announced). Back: focus returns to the red pill. Focus never sits on an invisible element: `main` is inert while act two is open, and `.fork-scene` is inert while the curtain is down.
- **Skip link** stays first in the DOM and above act two (`z-index:20` vs `15`), so Shift+Tab from the fork reaches "Skip intro, go to the site".
- **Semantics:** act two is a `<section>` with `aria-labelledby="where-title"` (a named region); `<h2>` headline; prongs are real `<button type="button">` in a `role="group"` labelled by the headline; each is described by "Coming soon."; the SVG is one `role="img"` with an `aria-label`; the status line is `role="status"`, `aria-live="polite"`.
- **No JS:** act two cannot open (it is `hidden` and the red pill is a plain button). No-JS visitors still have the blue pill and the skip link. This is an accepted limitation, the same as the R10 stub had (section 18.3).

### 17.6 Requirements, Part B

### R19. Clicking the red pill starts act two in the same page: no navigation, the URL gains `#where`, and the old stub is gone.
- **Source:** [Nick-B] "indulge me will launch into a continuation of this experience"; section 14 decision.
- **Acceptance:** at the pill scene, set `window.__stay = 1`, click `#pill-red`; after 4000ms: `window.__stay === 1` (no page load), `location.pathname` ends in `/intro.html`, `location.hash === "#where"`, `document.getElementById('where').hidden === false`, `document.querySelector('main').inert === true`. `document.getElementById('stub') === null` and `grep -c "Coming soon. Take the blue pill" intro.html` = 0. Red pill is still a `<button type="button">` with text `indulge me`.
- **Edge cases:** double-click or Enter-then-click during the sequence starts it only once (`document.getAnimations().filter(a => a.animationName === "curtain-raise").length <= 1` at any time); keyboard Enter and Space on the red pill both start it; clicking while the nudge is visible is not possible (the nudge is gone by scene 3, R6); with no JS the red pill does nothing and nothing breaks.
- **Resources:** `intro.html` markup and inline script.

### R20. "I knew I liked you." appears immediately on a red curtain, in soft Fraunces italic with a light-green period, readable for 1.5s, and is announced.
- **Source:** [Nick-B] "Immediately after someone clicks 'indulge me' the briefly get 'I knew I liked you.'"; style and timing in 17.2 (assumption: 1500ms hold).
- **Acceptance:** motion allowed, 1440×900: click the red pill; at t ≈ 1000ms JS check: `.liked` `textContent === "I knew I liked you."`, computed `opacity` > 0.95, `fontFamily` starts with `"Fraunces"`, `fontStyle === "italic"`, `color === "rgb(248, 250, 244)"`; `.liked .dot` `color === "rgb(207, 226, 166)"`; `.curtain` computed `backgroundColor === "rgb(154, 59, 46)"`; `document.activeElement === document.querySelector('.liked')`. The `liked-in` animation exists with `delay 250`, `duration 500`.
- **Edge cases:** at 320×568 the line wraps to at most three lines and `scrollWidth <= innerWidth`; slow font load falls back to Georgia italic in place; a screen reader hears the line once (focus, not a live region, so it is not double-announced).
- **Resources:** `intro.html` act-two markup, CSS, script.

### R21. A single red curtain then raises over 900ms to reveal the fork scene, with a skip for impatient visitors.
- **Source:** [Nick-B] "And then a 'curtain' raises to reveal the next screen."; technique and timing in 17.2.
- **Acceptance:** motion allowed, 1440×900, click the red pill at t = 0: (a) at t ≈ 1000ms, `.curtain` bounding `top` within 1px of 0 and `height ≥ innerHeight`, computed `opacity === "1"`; (b) a `curtain-raise` animation exists with `getTiming()` `duration 900`, `delay 2250`, `easing "cubic-bezier(0.7, 0, 0.2, 1)"`; (c) at t ≈ 2700ms the curtain's computed transform has a `ty` strictly between `−innerHeight` and `−10` (mid-raise), and the `.liked` element has moved up with it; (d) at t ≈ 3800ms, `.curtain.hidden === true`, `.fork-scene.inert === false`, `document.activeElement.id === "where-title"`. **Skip:** fresh load, click the red pill, at t ≈ 800ms dispatch a `keydown` Escape on `document`; by t ≈ 2000ms the curtain is hidden or its `ty` is below `−innerHeight/2` (it raised early). A `keydown` at t ≈ 100ms does **not** skip (arming delay).
- **Edge cases:** background tab during the raise: the 3600ms safety timeout still finishes the end step; window resize mid-raise: the curtain still clears the viewport (`-100%` is relative to its own height); `scrollWidth <= innerWidth` throughout; the hem shadow never lingers at the top edge after the end step.
- **Resources:** `intro.html` CSS keyframes `curtain-in`, `liked-in`, `curtain-raise`; inline script.

### R22. The fork scene's top reads "Where should we start?" as an h2 in Fraunces 500.
- **Source:** [Nick-B] "The top of the screen reads 'where should we start?'"; style in 17.3.1.
- **Acceptance:** after the end step (or on direct load of `intro.html#where`): `#where-title` is an `H2`, `textContent === "Where should we start?"`, computed `fontFamily` starts with `"Fraunces"`, `fontWeight === "500"`; its bounding `top` is less than the `.prongs` row's `top` and less than 25% of `innerHeight` at 1440×900 and at 390×844; `document.querySelectorAll('h1').length === 1` still.
- **Edge cases:** at 320px wide it wraps to two balanced lines without overflow; it gets focus without a visible outline (`outline-style` computed `none` on `:focus`), since it is not interactive.
- **Resources:** `intro.html`.

### R23. A pixel-art road splits into three visually distinct prongs, drawn as crisp inline SVG.
- **Source:** [Nick-B] "a fork in the road visualization"; geometry in 17.3.2.
- **Acceptance:** JS check on the open fork scene: one `svg.road` with `getAttribute('viewBox') === "0 0 120 80"`, `getAttribute('shape-rendering') === "crispEdges"`, `role="img"` and a non-empty `aria-label`; it contains `g[data-prong="research"]`, `g[data-prong="technology"]`, `g[data-prong="passion"]`; each group contains at least one rect whose `fill` is, respectively, `#2F5B44`, `#2E4A6B`, `#9A3B2E` (case-insensitive); every `rect` in the SVG has integer `x`, `y`, `width`, `height`; total `rect` count ≥ 150 (road, edges, dashes, tufts, avatar). Bounding check: the left group's top-left rect is within the leftmost 12% of the SVG's width, the right group's within the rightmost 12%, and the technology group spans the horizontal center.
- **Edge cases:** no `<image>`, `<img>`, `<canvas>` or external file references in act two (`grep -cE "<img|<canvas|<image" intro.html` = 0); the road scales without blurring at 320, 390 and 1440 wide; there is no horizontal overflow.
- **Resources:** `intro.html` inline SVG.

### R24. A pixelated avatar, seen from behind, stands on the trunk facing the fork, built from the 12×16 map, idles and looks toward the hovered or chosen prong.
- **Source:** [Nick-B] "a pixelated avatar facing the fork"; asset decision in section 15; map in 17.3.3.
- **Acceptance:** JS check: `svg.road g.avatar` exists and contains exactly as many `rect`s as non-`.` characters in the section 17.3.3 map (**110**, counted by script); every avatar rect has `width === "1"` and `height === "1"`; the avatar's bounding box is horizontally centered on the trunk (center within 2% of the SVG's center) and its bottom is within the bottom 10% of the SVG; at 390×844 its rendered height ≥ 40px, at 1440×900 ≥ 90px. Motion allowed: an `idle` animation is running on `.avatar-body`. Focusing the `research` prong sets `.avatar` `dataset.look === "research"` and its computed transform has a negative `tx`; focusing `passion` gives a positive `tx`.
- **Edge cases:** colors limited to the six listed in 17.3.3; reduced motion: no `idle` in `getAnimations()`, but the look shift still applies; the avatar never covers a prong chip.
- **Resources:** `intro.html` inline script (map plus builder), CSS.

### R25. The three prongs are labeled "research", "technology", "passion" and look and feel clickable.
- **Source:** [Nick-B] "the three fork prongs are 'research' 'technology' and 'passion.'"; [Card2] "should look clickable/alive even though they're stubs"; styling in 17.3.4.
- **Acceptance:** JS check: `.prongs` contains exactly three `button[type="button"]` with `textContent` `research`, `technology`, `passion` in that DOM order and left-to-right on screen; each computed `fontFamily` starts with `"IBM Plex Mono"`, `borderRadius === "0px"`, height ≥ 44px; their computed `boxShadow` colors are `rgb(47, 91, 68)`, `rgb(46, 74, 107)`, `rgb(154, 59, 46)` respectively (three distinct values); `cursor === "pointer"`. Hover (CDP mouseMoved to a chip's center, 1440×900): its computed transform becomes `translate(-2px, -2px)` (matrix `tx = −2, ty = −2`) and its `::after` `opacity === "1"`. Motion allowed, right after the end step: a `pop` animation exists on each chip, with delays 0, 120 and 240ms.
- **Edge cases:** at 320, 390 and 1440 wide, and at 844×390, the three chips' bounding boxes do not intersect and all sit inside the viewport; on touch emulation there is no hover lift; `:focus-visible` shows the pine outline and the caret; label text is lowercase exactly as Nick wrote it.
- **Resources:** `intro.html` CSS and markup.

### R26. Each prong is an honest stub: activating it announces that it is coming soon, and nothing navigates.
- **Source:** [Nick-B] "We will talk about each of the prongs after."; [Card2] "stub prongs must still be announced sensibly to screen readers… rather than silently doing nothing"; section 13.2.
- **Acceptance:** for each prong: activate it (click, then separately `keydown`/`keyup` Enter and Space on the focused chip); within 300ms `#fork-status` (`role="status"`, `aria-live="polite"`) has `textContent === "<Label> is coming soon. I'm still paving that road."` with the label capitalized (`Research`, `Technology`, `Passion`); `location.href` is unchanged and `window.__stay === 1`; no new section or scene appears (`document.querySelectorAll('section').length` unchanged). Each chip has `aria-describedby="fork-soon"`, and `#fork-soon` `textContent === "Coming soon."` and is visually hidden (bounding width ≤ 1px). No chip has `aria-disabled` or `disabled`. No console errors during the whole act-two run (CDP `Runtime.exceptionThrown` and `console` error events: zero).
- **Edge cases:** activating the same prong twice re-announces (the status is cleared, then refilled on the next frame); activating a different prong replaces the message (never two messages); the message wraps cleanly at 320px; the stub copy is placeholder text Nick can change (Flag A5).
- **Resources:** `intro.html` inline script and markup.

### R27. Act two lives in `intro.html` on top of the scroll track, with working Back, Forward and direct links.
- **Source:** [Card2] item 4; decision and mechanics in section 14.
- **Acceptance:** (a) `git diff --name-only 8b1efa5..HEAD` after the build lists only `intro.html`, `BACKLOG.md` and files under `docs/` (no new HTML file); (b) after the end step, `history.back()`, wait 500ms: `#where.hidden === true`, `main.inert === false`, `location.hash === ""`, `scrollY ≥ (scrollHeight − innerHeight) − 2` (back at the pill scene), `document.activeElement.id === "pill-red"`, and scene 3 is visible (R3's bottom-of-page check passes); (c) `history.forward()`: the fork scene shows again directly, with no curtain (`.curtain.hidden === true` within 300ms); (d) a fresh load of `http://localhost:8000/intro.html#where`: within 500ms the fork scene is open, the curtain is hidden, `main.inert === true`, and after 4500ms the nudge is still `hidden` (the R6 timer is cancelled); (e) `#where` sits after `</main>` (`document.querySelector('main #where') === null`) and `main` still contains exactly three `section`s.
- **Edge cases:** Back pressed during the curtain sequence aborts it cleanly (act two hidden, no orphaned animations: `document.getAnimations().filter(a => /curtain|liked/.test(a.animationName)).length === 0` after 500ms); reloading on `#where` reopens the fork; the blue pill and the skip link are unaffected; the page never sets `overflow:hidden` on `html` or `body` (R3).
- **Resources:** `intro.html` inline script (history, state machine).

### R28. The new scenes work at desktop, mobile and landscape-phone sizes with no horizontal overflow.
- **Source:** [Card2] item 5; [Nick] original brief "desktop and mobile friendly"; values in 17.4.
- **Acceptance:** at 1440×900, 768×1024, 390×844, 320×568 and 844×390, with the fork scene open: `document.documentElement.scrollWidth <= innerWidth` and `#where.scrollWidth <= #where.clientWidth`; the headline, three chips and the avatar are fully inside the viewport without scrolling act two (bounding `top ≥ 0`, `bottom ≤ innerHeight`); each chip is ≥ 44px tall. During the curtain step at 390×844, `.liked` fits inside the viewport. `grep -c "dvh" intro.html` stays 0.
- **Edge cases:** iPhone home indicator and notch: safe-area padding on act two (`env(safe-area-inset-*)` present in its CSS); rotating the phone with act two open keeps it covering the screen (`position:fixed; inset:0`); touch devices get no hover-only styling.
- **Resources:** `intro.html` CSS.

### R29. With reduced motion, the sequence becomes a 1.5s cut and nothing in act two animates.
- **Source:** [Card2] item 6 "reduced-motion fallback for the curtain-raise transition"; section 17.5.
- **Acceptance:** with reduced motion emulated, click the red pill: at t ≈ 300ms the curtain is visible (`top` ≈ 0, computed opacity "1") and `.liked` is visible; `document.getAnimations().length === 0` at t ≈ 300ms and at t ≈ 2200ms; at t ≈ 1900ms `.curtain.hidden === true` and focus is on `#where-title`; the red-pill glow is present but has no `ember` animation (R18 edge). Skip still works: Escape at t ≈ 600ms hides the curtain within 100ms.
- **Edge cases:** toggling reduced motion while act two is open applies live; the reduced path does not wait for `animationend`.
- **Resources:** `intro.html` CSS and script.

### R30. Keyboard and screen-reader users get the whole sequence: announced line, announced headline, operable prongs, and no focus on hidden content.
- **Source:** [Card2] item 6; section 17.5.
- **Acceptance:** keyboard only, from a fresh load: Tab to the red pill (the R13 focus scroll brings scene 3 into view), press Enter; `document.activeElement` is `.liked` during the hold and `#where-title` after the end step; then `Tab` focuses `research`, `technology`, `passion` in that order, and `Shift+Tab` from `research` eventually reaches the skip link, which is visible and on top (`document.elementFromPoint` at its center returns the skip link while act two is open). While playing, `main.inert === true` and `.fork-scene.inert === true`; after the end step `.fork-scene.inert === false`. CDP `Accessibility.getFullAXTree` shows: a `region` named "Where should we start?", a `heading` level 2 with that name, a `group` containing three `button`s each with description "Coming soon.", one `image` with the road's label, and a `status` node.
- **Edge cases:** no focusable element inside the curtain other than the `.liked` target; the hidden act two is not in the accessibility tree before the click; VoiceOver does not hear "dimmed" on the chips.
- **Resources:** `intro.html`.

### R31. Tokens, palette, script budget and file footprint stay inside the agreed system.
- **Source:** [Card] original "reuse these, don't invent new ones"; section 15; section 13.3.
- **Acceptance:** `grep -oiE "#[0-9a-f]{6}" intro.html | tr a-f A-F | sort -u` returns only the R14 list plus `#C9946E` (and `#CFE2A6`, `#B0703A` from the copied `:root`); `grep -c -- "--glow-ember:196,84,58" intro.html` = 1 and `grep -c -- "--glow-warm:222,132,84" intro.html` = 1 (spacing as written, or the builder adjusts this grep to the exact written form and shows it); the Google Fonts URL is unchanged from section 1; `grep -cE "<script[^>]+src=" intro.html` = 0; the main inline script (the second `<script>`) is under 220 lines; `grep -ci "preventDefault" intro.html` = 0.
- **Edge cases:** no new font families, no new image or SVG files, no CSS or JS files, no third-party code.
- **Resources:** `intro.html`.

### R32. Nothing the first build shipped regresses.
- **Source:** [Card2] build card done-when "Blue pill path… still works unchanged"; sections 7 and 13.3.
- **Acceptance:** the acceptance checks of R1 to R9 and R11 to R15 all pass again on the addendum build, with these amendments only: R1's file list also allows `BACKLOG.md` (already on the branch before this addendum); R2's text list adds `What’ll it be? The choice is yours.`; R13's section count means sections inside `main`. In particular, R9 passes unchanged (the blue pill is `<a href="index.html">`, has no JS handler, and lands on the front page), and R3's scrubbing checks (scene opacities at p = 0, 25%, 50%, 100%) pass.
- **Edge cases:** the red pill's new `position:relative` must not shift the pill row (pill bounding boxes at 1440 and 390 within 2px of their 8b1efa5 positions, apart from the planned 16.2 spacing change); the R13 pointer gating still keeps both pills untappable at `scrollY = 0`.
- **Resources:** `intro.html`; `index.html` (read-only).

---

## 18. Addendum: deployment, flags, feasibility, non-goals, follow-ups

### 18.1 Deployment and build

Unchanged from section 8: **not Docker**, by the same justified exception (static GitHub Pages site; nothing to containerize; production deploy is a push to `main`, which stays forbidden). Local preview `python3 -m http.server 8000` from the repo root on `feature/intro-experience`, demo URLs `http://localhost:8000/intro.html` and `http://localhost:8000/intro.html#where`. No build step. The build card may push `feature/intro-experience` to origin as a backup.

### 18.2 Flags for Nick (addendum)

1. **A1, copy case.** You typed "what'll it be?" and "where should we start?" lowercase. I set both in sentence case ("What’ll it be?", "Where should we start?") because they open sentences and Maestro's card did the same. Prong labels stay lowercase as you wrote them. Say if you want the lowercase look (like "welcome.").
2. **A2, the curtain is red.** It is the red pill's brick color with soft pleats. The line "I knew I liked you." sits on it in cream with a light-green period. If you pictured a dark theater curtain, `--ink` is the swap.
3. **A3, the avatar is generic.** Back view, dark hair, green shirt, red backpack, blue jeans. Skin `#C9946E` and the hair color are placeholders. Tell me your hair and skin tones (or anything signature, like glasses or a hat) and the map in 17.3.3 is a 2-minute edit.
4. **A4, prong colors.** research = site green, technology = the blue pill's blue, passion = the red pill's red. That is my call, not yours.
5. **A5, stub copy.** "Research is coming soon. I'm still paving that road." is placeholder text in your voice. Change freely.
6. **A6, no exit button on the fork scene.** Back returns to the pills, and the skip link still works for keyboard users, but there is no visible "straight to business" on the fork screen. I didn't add one since you didn't ask. Easy to add later.
7. **A7, timing.** The whole sequence takes about 3.2 seconds (1.5s of that is the line held on screen). Tapping or pressing a key skips ahead. Worth feeling on your phone; the numbers are one place to change.

No new cost, services, infrastructure or recurring manual steps.

### 18.3 Feasibility (spike method) and risks

I ran a throwaway spike (one HTML page with the prompt, glow, road, avatar and chips, served locally and measured in headless Chromium 145 over CDP, plus an image check of two screenshots). It lived in my scratch folder and is not part of the repo.

| # | Given / When / Then | Verdict | Evidence |
|---|---|---|---|
| F5 | Given the 16.3 glow values, when rendered on `--paper`, then the warmth is visible beside the red pill but stays subtle and absent beside the blue. | VALIDATED | 8px out: red side `229,218,204`, blue side `232,236,226`, paper `234,238,228`; back to paper by 30px. Image check: "soft amber/tan… subtle and tempting, not harsh neon". |
| F6 | Given the prompt and new margins, when scene 3 renders at 1440×900, 390×844, 320×568 and 844×390, then the gaps group the prompt with the pills and nothing is clipped. | VALIDATED | Gaps above/below: 63/18, 59/17, 40/14, 18/10 (short-screen rules on); pill bottoms at 600, 582, 444, 300 px, all inside the viewport. |
| F7 | Given a 3:2 fork and a flex row of three Plex Mono chips, when rendered at 1440, 390, 320 and 844×390, then the chips don't overlap, stay in view, and the scene fits one screen. | VALIDATED | No overlap and all in view at every size; at 844×390, avatar bottom at 373 of 390 px with the short-screen rules (spike used a 420px fork and no top margin on the chip row; the spec's 400px fork plus 12px margin nets out to about 372px). Road geometry checked by script: prongs end at x = 2 and x = 108, all eight tufts clear of the road and its edges, avatar map is 12 × 16 with 110 filled pixels. |
| F8 | Given the 12×16 map in back view, when drawn as crisp SVG rects, then it reads as a person facing the fork. | PARTIAL | Image check: "a person standing with their back to us, deciding which way to go"; the backpack can read as a red shirt; the figure is about 46px tall on a 390px phone. Likeness is Flag A3. |
| F9 | Given Chromium, Safari and Firefox, when the page uses `inert` and seeks a CSS animation with `currentTime`, then focus-trapping and skip work without libraries. | VALIDATED | `inert` is Baseline (Chrome 102, Safari 15.5, Firefox 112); in the spike browser `'inert' in HTMLElement.prototype === true`, and setting an animation's `currentTime` to its delay (2250) worked. |

Risks:

- **`animationend` lost** (background tab, interrupted animation): the 3600ms safety timeout and the reduced-motion `setTimeout` path cover it (R21, R29).
- **Act two over a scrollable document:** wheel input on the overlay may scroll the hidden page underneath. Harmless while covered, and closing it restores the scroll position (R27). Locking scroll with `overflow:hidden` is forbidden because it breaks the scroll timeline.
- **Glow clipped or noisy on phones:** the full-width mobile pill's glow reaches the screen edge and the stage clips it. Verified harmless: box-shadows don't add scroll width.
- **The pixel style vs. the editorial serif type:** an intentional contrast ("game inside a book"), flagged in the spike's image check. The headline stays Fraunces to keep the site voice.
- **No-JS visitors can't reach act two.** Accepted, as with the R10 stub; they keep the blue pill and the skip link.
- **Scope creep into the prongs:** the biggest practical risk for an AI builder. Section 13.2 and 18.4 rule it out explicitly.

### 18.4 Non-goals for the addendum (do not build)

- **Anything a prong leads to:** no research, technology or passion content, no new scenes, pages, routes, hashes, modals or drawers. A prong only announces "coming soon" (R26).
- A visible exit or "straight to business" link on the fork scene (Flag A6), a "replay" control, or a way to re-trigger the curtain other than Back then the red pill.
- Sound, particle effects, a typewriter effect on the line, parallax, a walking animation along a path, or any avatar movement beyond the idle hop and look shift.
- A second avatar pose (front, side) or any avatar customization UI.
- Persisting the choice (cookies, localStorage, sessionStorage) or analytics on prong clicks.
- Any change to `index.html`, the case-study pages, `resume.html`, `README.md`, `CNAME`, `AGENTS.md`, or new HTML, CSS, JS, image or font files.
- Changing the scroll budget, scenes 1 and 2, the nudge, or the blue pill.
- Any JS library, CDN script or build tooling. Pushing to or merging into `main`, or opening a PR.

**Authorized boundaries (build card t_4749555c):** edit `intro.html` on `feature/intro-experience` in `~/Documents/github/portfolio`; update `BACKLOG.md` rows for this work; commit and `git push origin feature/intro-experience`; run or reuse the local preview server on port 8000.

**Forbidden actions:** editing any other site file; pushing any other branch; committing to or merging into `main`; adding dependencies, files or services beyond the preview server.

### 18.5 Follow-ups (logged in BACKLOG.md, not requirements)

- Define and build the **research** prong.
- Define and build the **technology** prong.
- Define and build the **passion** prong.
- Avatar likeness pass once Nick gives hair, skin and any signature details (Flag A3).
- Decide whether the fork scene gets a visible exit to the site (Flag A6).

---

# Addendum 2: passion branch, intro beat ("I'm. 👏 A. 👏 Nerd. 👏") (card t_a8f81d69)

Added 2026-11-12 by product. Builds on the shipped, Crit-passed `intro.html` at commit 15e3e2a (act two, fork scene, three stub prongs). Same harness, tokens, fonts and conventions as sections 1 to 18 unless a line below says otherwise. Build card: t_593e8d60 (assignee `design`). The card suggested numbering this "18"; section 18 already exists, so this addendum is sections 19 to 24 and requirements R33 to R49.

## 19. Source, scope and what it changes

### 19.1 Source brief (Nick, verbatim, via card t_a8f81d69)

> Let's start with 'passion.' It opens to a dramatic animations showing 'I'm. 👏 A. 👏 Nerd.👏' as they scroll the word 'nerd' should start to 'glitch out' and take over the page. Nerd can branch out and link to a few things 'techie' 'gamer' 'photographer' that people can click on. Go ahead and build this next stage and then we can do the three actual things to dig into the passions. That will be end of this 'passion' branch.' Those passions should all be contained on one page.

Citation shorthand added: **[Nick-C]** = the brief above. **[Card3]** = card t_a8f81d69's body (scope boundary and its seven required items). **[Spike2]** = the throwaway prototype I ran for this addendum; results in section 24.3. **[WCAG]** = the WCAG 2.2 sources listed under Research sources.

### 19.2 Scope boundary

This pass builds **from the passion prong up to and including the three branch links**: the entry transition, the staccato reveal, the scroll-driven glitch and takeover, and three clickable links (`techie`, `gamer`, `photographer`). **What is behind each link is out of scope** [Nick-C: "then we can do the three actual things to dig into the passions"]. Each link is an honest stub (R42). The `research` and `technology` prongs stay exactly as they are (stubs, R26).

### 19.3 The one-page constraint (for the next card, decided now)

Nick: **"Those passions should all be contained on one page."** So the techie, gamer and photographer deep-dives will live **together on ONE page**: one scrolling layer, three subsections, in that order. **Not** three files, **not** three overlay layers, **not** three hash-routed scenes that replace each other. Whoever builds the deep-dive content must not fork it into three routes.

Decided shape of that future page, so the links can be wired to it today:

| Thing | Decision |
|---|---|
| The page | One `<section class="act4" id="passions">` in `intro.html`, after `#nerd`, using the same fixed-layer pattern as act two and act three (section 14). |
| Its parts | Three subsections inside it, ids `passions-techie`, `passions-gamer`, `passions-photographer`, in that order, one after another on the same scroll. |
| The links | Real `<a>` elements with `href="#passions-techie"`, `#passions-gamer`, `#passions-photographer`. Set **now**, and never changed by the next card. |
| Routing | The `#passions-` hash prefix is reserved now. Today the router answers it with the stub (R42). The next card changes **only** that router branch (open `#passions`, scroll to the subsection), adds the section, and deletes the stub line and the `aria-describedby`. No href or markup rewiring on the chips. |

If Nick later prefers a separate file (`passions.html`), the one-page rule still holds; the three hrefs change to `passions.html#techie` etc. That is Flag B6, not a requirement.

### 19.4 What this changes in sections 1 to 18

| Earlier decision | Change |
|---|---|
| R26: all three prongs are stubs | **Narrowed.** `passion` now starts act three (R33). `research` and `technology` stay stubs exactly as R26 says. The `passion` prong loses `aria-describedby="fork-soon"`. |
| R30: "a `group` containing three `button`s each with description 'Coming soon.'" | Now two of the three buttons (`research`, `technology`) carry that description. |
| R31: main inline script under 220 lines | Raised to **under 330 lines**, still one inline script, no external scripts (R49). |
| R31: `grep -ci "preventDefault" intro.html` = 0 | **Unchanged.** The chips are wired so no `preventDefault` is needed (R42). |
| Section 14 mechanics / R27 router (`#where` or closed) | Extended to four states: closed, `#where`, `#nerd`, `#passions-*` (R48). |
| Section 18.4 non-goal "anything a prong leads to" | Narrowed: the passion prong's intro beat is now in scope; everything behind techie, gamer and photographer stays a non-goal (24.4). |

### 19.5 Map to the card's seven required items

| Card item | Decided in |
|---|---|
| 1. Entry point (transition from the fork) | Section 20.2, R33, R34 |
| 2. The "I'm. 👏 A. 👏 Nerd. 👏" reveal (copy, emoji, timing, font, screen readers) | Section 20.3, R35, R36, R37 |
| 3. The glitch on "nerd" and what "takes over the page" means | Section 21, R38, R39, R40 |
| 4. The three branch links (appearance, styling, affordance, stub) | Section 22, R41, R42 |
| 5. The one-page constraint for the deep-dive | Section 19.3, R43 |
| 6. Reduced motion and screen readers | Section 23.2, 23.3, R44, R45, R46 |
| 7. Responsive | Section 23.1, R47 |

---

## 20. Structure, entry and the staccato reveal

### 20.1 Structure

```html
<!-- after </section> of #where, before the inline script -->
<section class="act3" id="nerd" aria-labelledby="nerd-title" hidden>
  <div class="nerd-track">                                  <!-- 300svh tall when motion is allowed -->
    <div class="nerd-stage" id="nerd-stage">                <!-- position:sticky; top:0; height:100svh -->
      <div class="nerd-scan" aria-hidden="true"></div>      <!-- scanline overlay, 21.3 -->
      <h2 class="nerd-title" id="nerd-title" tabindex="-1">
        <span class="vh">I'm a nerd.</span>
        <span class="beats" aria-hidden="true">
          <span class="beat beat-1">I'm.<span class="clap">👏</span></span>
          <span class="beat beat-2">A.<span class="clap">👏</span></span>
          <span class="beat beat-3"><span class="nerd-word" data-text="Nerd.">Nerd<span class="dot">.</span></span><span class="clap">👏</span></span>
        </span>
      </h2>
      <div class="chips" role="group" aria-labelledby="nerd-title">
        <a class="prong chip" data-passion="techie"       href="#passions-techie"       aria-describedby="nerd-soon">techie</a>
        <a class="prong chip" data-passion="gamer"        href="#passions-gamer"        aria-describedby="nerd-soon">gamer</a>
        <a class="prong chip" data-passion="photographer" href="#passions-photographer" aria-describedby="nerd-soon">photographer</a>
      </div>
      <p class="nerd-status" id="nerd-status" role="status" aria-live="polite"></p>
      <span class="vh" id="nerd-soon">Coming soon.</span>
      <button type="button" class="nerd-cue" id="nerd-cue" hidden>keep scrolling <span aria-hidden="true">&darr;</span></button>
    </div>
  </div>
</section>
```

- **Layer:** `.act3 { position:fixed; inset:0; z-index:16; background-color:var(--paper); overflow-y:auto; overscroll-behavior:contain; scrollbar-width:none; scroll-timeline:--nerd block; }` plus `.act3::-webkit-scrollbar{display:none}` and `.act3[hidden]{display:none}`. z-index 16 sits above act two (15) and **below the skip link (20)**. The scrollbar is hidden because the spike showed it as a grey strip down the right edge of the dark takeover screen [Spike2]; the cue (21.5) replaces it as the scroll affordance.
- **While act three is open:** `main.inert = true` (already true from act two), act two stays un-hidden underneath with `.fork-scene.inert = true`. The page never sets `overflow:hidden` on `html`/`body` (R3).
- **No new class reuse traps:** the "Nerd." word gets its own class `.nerd-word`. It must **not** reuse `.logotype`, because `html.js .logotype .dot` already carries the root-scroll `dot-pop` animation and would hide the period.
- **State machine** (one variable, separate from act two's): `closed → entering → open`, plus `open|entering → closed` on Back.

### 20.2 Entry: a right-hand wipe, not a second curtain (card item 1)

**Decision: reuse the curtain's technique (one full-screen panel, one transform, the same `cubic-bezier(.7,0,.2,1)` "heavy fly line" easing), but as a horizontal wipe in from the right, with nothing written on it.**

| Option | Tradeoff |
|---|---|
| A. Reuse the red curtain (drop, line, raise) | The curtain is the red pill's moment. Repeating it for every prong turns it into a loading screen, and research and technology will need entries too. Rejected. |
| B. Crossfade to the new scene | Paper over paper: a fade reads as a content swap, not "dramatic" [Nick-C]. Rejected. |
| **C. Wipe in from the right** | `passion` is the **right-hand road** on the fork (17.3.2), and the avatar already looks right when it is chosen (17.3.3). The new scene arriving from the right is literally taking that road. Same easing and single-panel build as the curtain, so it belongs to the same family. **Chosen.** |

Times are milliseconds from the passion prong's activation (click, tap, Enter or Space).

| t (ms) | What happens | Technique |
|---|---|---|
| 0 | The existing prong handler sets `last='passion'` and the avatar's `data-look="passion"` (unchanged, 17.3.3). `#fork-status` is cleared. Act three state `entering`. `history.pushState({act:3}, "", "#nerd")`. `act3.hidden = false`, `act3.scrollTop = 0`, class `is-entering`. `.fork-scene.inert = true`. `.chips.inert = true` (released at the end step). | JS |
| 120 to 820 | **The wipe.** Act three slides in from the right over the fork scene. The 120ms delay lets the avatar's look-right register first. Its leading edge carries the curtain's hem shadow. | `.act3.is-entering { animation: nerd-wipe 700ms cubic-bezier(.7,0,.2,1) 120ms both; box-shadow:-18px 0 36px -12px rgba(22,36,28,.45); overflow-y:hidden; }` and `@keyframes nerd-wipe { from{transform:translateX(calc(100% + 48px));} to{transform:none;} }` |
| 820 | Focus moves to `#nerd-title` (`focus({preventScroll:true})`), so a screen reader says "I'm a nerd., heading level 2" (R46). | JS |
| 820 to 1220 | **Empty paper, held for 400ms.** The dramatic pause before the first word. | none |
| 1220 to 2720 | **The staccato reveal** (20.3). | CSS |
| 2720 | **End step** (on `animationend` of the third clap, or a 3200ms safety timeout, or a skip, whichever comes first): class `is-entering` removed, state `open`, the act becomes scrollable. | JS |
| 3420 | If `act3.scrollTop` is still under 4% of its scroll range, the cue appears (21.5). | JS |

- **No scrolling during the entry:** `.act3.is-entering` has `overflow-y:hidden`. That is set on the overlay, not on `html`/`body`, so the R3 rule is untouched. Without it, a scroll during the reveal would jump the glitch timeline forward while the entry animations still own the beats.
- **Skip (impatient visitors):** same rules as 17.2. From t = 400ms until the end step, a `pointerdown` on act three or a `keydown` of Escape, Enter or Space calls `finish()` on every animation in `act3.getAnimations({subtree:true})` and runs the end step immediately. The 400ms arming delay stops the key press that activated the prong from also skipping. Skip fires once.
- The reveal is time-based, not scroll-based, because Nick separates the two: it "opens to a dramatic animation", and then "as they scroll" the glitch starts [Nick-C].

### 20.3 The staccato reveal (card item 2)

**Copy, exact, three stacked lines, centered:**

| Line | Text | Characters |
|---|---|---|
| 1 | `I'm.` then 👏 | straight apostrophe U+0027 (matches scene 2's `I'm` and Nick's typing) |
| 2 | `A.` then 👏 | |
| 3 | `Nerd.` then 👏 | the period is `<span class="dot">` |

- **Clap placement:** one 👏 (U+1F44F, no variation selector needed, it is emoji-presentation by default) after each word's period, on the same line, as in Nick's string. Nick typed `Nerd.👏` with no space and the other two with a space; I normalized all three to the same small gap (`margin-left:.18em`, no literal space character). Flag B1.
- **Why stacked, at every width:** each beat lands on its own line, like a slide, which is what makes it staccato. It also keeps "Nerd." alone on the bottom line, ready to take over (21.2), and it avoids a one-line layout that would need a different layout on phones.
- **The period:** only the "Nerd." period is `--moss`, the site's green-period signature (`welcome.`, `Nick.`). The first two periods are `--ink`, so the green lands once, on the last beat.

**Type (no new families):**

| Part | Spec |
|---|---|
| `.beat` (all lines) | `display:block; white-space:nowrap; font-family:"Fraunces",Georgia,serif; font-weight:600; font-variation-settings:"opsz" 144; font-size:min(clamp(56px,16vw,128px),22svh); line-height:1; letter-spacing:-.02em; color:inherit;` (the `welcome.` voice). `.beats { display:grid; justify-items:center; gap:.04em; }` |
| `.nerd-word` | `display:inline-block; position:relative; font-weight:800; font-variation-settings:"opsz" 144, "SOFT" 50, "WONK" 0; letter-spacing:-.045em; transform-origin:50% 55%;` The `Nick.` logotype treatment, so "I'm. A. Nerd." echoes "I'm Nick." two scenes earlier. **No `will-change`** on it (21.2). |
| `.clap` | `display:inline-block; margin-left:.18em; font-size:.62em; vertical-align:.06em; font-style:normal; font-family:"Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif;` These are the OS emoji fonts, not web fonts. The Google Fonts URL does not change. |
| `.nerd-title` | `margin:0; font-weight:400;` and `#nerd-title:focus{outline:none}` (programmatic focus target, not interactive, same as `#where-title`). |

Spike sizes: at 1440×900 the lines measure 271, 191 and 371px wide at 128px; the claps render in full color [Spike2]. The `22svh` cap keeps all three lines inside a landscape phone (3 × 86px at 844×390).

**Timing (ms from the prong activation; per-beat interval 520ms, the clap 260ms after its word):**

| Beat | Word lands | Clap lands |
|---|---|---|
| `I'm.` | 1220 (`beat-in`, 180ms) | 1480 (`clap-in`, 200ms) |
| `A.` | 1740 (`beat-in`, 180ms) | 2000 (`clap-in`, 200ms) |
| `Nerd.` | 2260 (`beat-in-big`, 240ms) | 2520 (`clap-in`, 200ms), ends at 2720 |

```css
.act3.is-entering .beat   { animation: beat-in 180ms cubic-bezier(.2,.9,.3,1.25) both; }
.act3.is-entering .beat-1 { animation-delay:1220ms; }
.act3.is-entering .beat-2 { animation-delay:1740ms; }
.act3.is-entering .beat-3 { animation: beat-in-big 240ms cubic-bezier(.2,.9,.3,1.25) 2260ms both; }
.act3.is-entering .clap   { animation: clap-in 200ms cubic-bezier(.2,.9,.3,1.4) both; }
.act3.is-entering .beat-1 .clap { animation-delay:1480ms; }
.act3.is-entering .beat-2 .clap { animation-delay:2000ms; }
.act3.is-entering .beat-3 .clap { animation-delay:2520ms; }
@keyframes beat-in     { from{opacity:0; transform:scale(1.35);} to{opacity:1; transform:none;} }
@keyframes beat-in-big { from{opacity:0; transform:scale(1.6);}  to{opacity:1; transform:none;} }
@keyframes clap-in     { from{opacity:0; transform:scale(.4) rotate(-14deg);} to{opacity:1; transform:none;} }
```

Each word **slams** in (starts large, drops to size with a small overshoot), and each clap **pops** with a twist like a hand hitting. The reveal lasts 1.5 seconds from first word to last clap, plus the 400ms pause before it. When `is-entering` is removed, the beats' base style is fully visible, so nothing depends on a held fill.

**Screen readers and the emoji:** the whole visual line is `aria-hidden="true"`. Assistive tech reads only the visually hidden `I'm a nerd.` inside the same `<h2>`, so the heading's accessible name is exactly "I'm a nerd." No "clapping hands" read three times, and no "I'm period A period". This also covers emoji rendering differences: if a device draws 👏 badly, it is purely visual. Every platform this site targets (iOS, Android, macOS, Windows 10+) ships 👏 (Unicode 6.0, 2010). An old Linux box with no emoji font shows an empty box. That is accepted and listed in the risks (24.3).

---

## 21. The glitch and the takeover (card item 3)

### 21.1 The scroll track

When motion is allowed, `.nerd-track { height:300svh; }` and `.nerd-stage { position:sticky; top:0; height:100svh; overflow:clip; display:grid; place-items:center; text-align:center; padding:0 var(--pad); }`, the same sticky-stage pattern as the intro (section 4). The timeline is the act's own scroller: `scroll-timeline:--nerd block` on `.act3`, and `animation-timeline:--nerd` on the animated children (written after the `animation` shorthand, section 4 item 2). Progress `q` runs 0% to 100% across the 200svh of scroll.

| q | What is on screen |
|---|---|
| 0 to 5% | Rest: the reveal as it landed, on paper. |
| 5 to 20% | `I'm.`, `A.` and all three claps fall away (opacity 1 to 0, up 4svh). "Nerd." starts to glitch and drifts to the vertical center. |
| 20 to 55% | **Takeover.** "Nerd." grows until it is 130% of the viewport width (edges cropped). The glitch peaks. Between 25 and 55% the page turns from paper to ink and the word from ink to cream. Scanlines fade in between 35 and 60%. |
| 55 to 75% | **Settle.** "Nerd." shrinks back to fit (`--s-rest`) and rises to 36% of the screen height. The glitch fully clears by 75%. |
| 70 to 88% | **Branch out.** The three links emerge from the word, staggered (22.1). |
| 90 to 100% | Rest. Links live (pointer gating lifts at q ≥ 90%, as scene 3 does). |

Gate: every scroll-driven rule lives inside `@supports (animation-timeline: scroll())` **and** `@media (prefers-reduced-motion:no-preference)`. Only `transform`, `translate`, `scale`, `opacity`, `background-color`, `color` and the two registered custom properties animate.

### 21.2 What "takes over the page" means, concretely

Three things at once, all scrubbed by scroll:

1. **The word grows past the edges.** "Nerd." scales from 1 to `--s-peak`, where its width is 130% of the viewport, centered. It is bigger than the screen, so it reads as the word swallowing the page.
2. **The page flips to "terminal mode".** The stage background goes from `--paper` `#EAEEE4` to `--ink` `#16241C`, and the word goes from `--ink` to `--card` `#F8FAF4`. This is the first dark screen on the site (Flag B2). The moss period stays moss.
3. **Scanlines.** A full-stage overlay, `.nerd-scan { position:absolute; inset:0; pointer-events:none; background:repeating-linear-gradient(0deg, rgba(248,250,244,.05) 0 1px, transparent 1px 3px); opacity:0; }`, fades in. This is texture, not motion. The lines never move.

Not tiling or repeating the word: one giant word is a stronger image, and repeated text would be extra DOM for screen readers to skip.

**Geometry is computed once, not per frame.** On act three's open, after `document.fonts.ready`, and on `resize`, the script removes the word's transform, measures it, and sets four custom properties on `#nerd-stage`:

```
w, h  = nerdWord.offsetWidth, nerdWord.offsetHeight          (untransformed)
cy    = nerdWord.getBoundingClientRect() center y              (stage is sticky at top:0)
pad   = parseFloat(getComputedStyle(stage).paddingLeft)
--s-peak  = innerWidth * 1.3 / w
--s-rest  = min((innerWidth - 2*pad) * 0.92 / w,  innerHeight * 0.38 / h)
--dy      = innerHeight * 0.50 - cy      (px)
--dy-rest = innerHeight * 0.36 - cy      (px)
```

Spike values: at 1440×900, `--s-peak` 6.686 and `--s-rest` 2.672; at 390×844, 4.829 and 3.007 [Spike2]. **No `will-change:transform`** on the word: it makes browsers rasterize the text once at its small size and stretch the bitmap, which blurs it at 6×. Without it, the spike's 6.7× word was judged "sharp… no obvious blur" in an image check [Spike2].

### 21.3 The glitch technique

**Decision: two pseudo-element copies of the word (`::before`, `::after`), offset left and right in two palette colors (an RGB-split look), cut into horizontal slices by stepped `clip-path: inset()` keyframes. Intensity and offset are scroll-scrubbed through two registered custom properties. No libraries, no canvas, no SVG filters.**

```css
@property --g    { syntax:'<length>'; inherits:true; initial-value:0px; }
@property --g-on { syntax:'<number>'; inherits:true; initial-value:0; }

@media (prefers-reduced-motion:no-preference){            /* the layers only exist when motion is allowed */
  .nerd-word::before, .nerd-word::after{
    content:attr(data-text); content:attr(data-text) / "";  /* empty alt text: never read aloud */
    position:absolute; inset:0; pointer-events:none;
    opacity:var(--g-on);
  }
  .nerd-word::before{ color:rgb(var(--glow-ember));          /* #C4543A, existing token */
    transform:translateX(calc(var(--g) * -1));
    animation:slice-a 1.5s steps(1,end) infinite paused; }
  .nerd-word::after { color:var(--leaf);                     /* #CFE2A6, existing token */
    transform:translateX(var(--g));
    animation:slice-b 1.5s steps(1,end) infinite paused; }
  .act3.is-scrolling .nerd-word::before,
  .act3.is-scrolling .nerd-word::after{ animation-play-state:running; }
}
@keyframes slice-a{
  0%      { clip-path:inset(8% 0 72% 0); }   16.667% { clip-path:inset(55% 0 20% 0); }
  33.333% { clip-path:inset(30% 0 52% 0); }  50%     { clip-path:inset(78% 0 6% 0); }
  66.667% { clip-path:inset(15% 0 64% 0); }  83.333% { clip-path:inset(44% 0 38% 0); }
}
@keyframes slice-b{
  0%      { clip-path:inset(62% 0 14% 0); }  16.667% { clip-path:inset(10% 0 70% 0); }
  33.333% { clip-path:inset(70% 0 12% 0); }  50%     { clip-path:inset(22% 0 58% 0); }
  66.667% { clip-path:inset(48% 0 30% 0); }  83.333% { clip-path:inset(4% 0 80% 0); }
}
```

**The scroll-driven parts** (inside the `@supports` + motion gate):

```css
.nerd-stage           { animation:nerd-bg linear both;        animation-timeline:--nerd; }
.beat-1, .beat-2, .beats .clap
                      { animation:nerd-drop linear both;      animation-timeline:--nerd; }
.nerd-word            { animation:nerd-takeover linear both;  animation-timeline:--nerd; }
.nerd-scan            { animation:nerd-scan linear both;      animation-timeline:--nerd; }

@keyframes nerd-bg{ 0%,25%{ background-color:var(--paper); color:var(--ink); }
                    55%,100%{ background-color:var(--ink); color:var(--card); } }
@keyframes nerd-drop{ 0%,5%{ opacity:1; transform:none; } 20%,100%{ opacity:0; transform:translateY(-4svh); } }
@keyframes nerd-takeover{
  0%,5%    { --g:0px;   --g-on:0;  transform:none; }
  20%      { --g:.03em; --g-on:.8; transform:translate(0,var(--dy)) scale(1.15); }
  55%      { --g:.06em; --g-on:1;  transform:translate(0,var(--dy)) scale(var(--s-peak)); }
  75%,100% { --g:0px;   --g-on:0;  transform:translate(0,var(--dy-rest)) scale(var(--s-rest)); }
}
@keyframes nerd-scan{ 0%,35%{ opacity:0; } 60%,100%{ opacity:1; } }
```

(While `is-entering` is set, the entry rules in 20.3 win over these by specificity, so the beats never have two owners at once. Scrolling is blocked during that time anyway.)

**The glitch only moves while the visitor is scrolling.** The act's `scroll` listener (passive) adds `.is-scrolling` to `.act3` and removes it 400ms after the last scroll event. While it is off, the slices freeze in place, still offset and colored, but static. That is Nick's wording taken literally ("as they scroll the word… should start to glitch out"), and it is also the accessibility design (21.4).

**Colors:** ember (`--glow-ember`, from the red-pill glow) and leaf (`--leaf`). Not a true red/cyan RGB split, because the site has neither and this addendum adds no new hex. The spike's image check read it as "a sliced, offset-layer glitch… deliberately misregistered print layers combined with a digital slicing effect" [Spike2]. Flag B3.

### 21.4 Photosensitivity rules (a hard requirement, not polish)

Glitch effects can trigger photosensitive seizures. These rules apply **even when motion is allowed** (R45):

1. **At most 4 visual state changes per second, so at most 2 flashes per second.** WCAG 2.3.1 sets the limit at 3 [WCAG]. Both slice layers use the same 1.5s duration, 6 steps, `steps(1,end)`, with no delay or offset between them, so they change together: 6 states ÷ 1.5s = 4 changes per second.
2. **Time-based change only while scrolling.** With `.is-scrolling` off, the slices are paused. Nothing on act three changes on its own after the reveal, so WCAG 2.2.2 (pause, stop, hide) is met without a pause button [WCAG].
3. **The dark flip is scrubbed, never automatic.** Paper to ink happens across 30% of the track (60svh of scroll). It never toggles on a timer. No `filter:invert`, no opacity blinking, no full-screen color strobe.
4. **The glitch fully clears at rest.** `--g-on` reaches 0 at q = 75%, so the screen with the links is clean. (The spike's version left a 0.3 residue; an image check called it "glitch residue… not a fully settled result", so it is removed.)
5. **Reduced motion gets none of it** (23.2).

### 21.5 The scroll cue

A visitor who has never seen a scrolling overlay may not scroll. `#nerd-cue` is a `<button type="button">` reading `keep scrolling ↓` (arrow `aria-hidden`), styled after the nudge (3.2) in the technical voice: `position:absolute; left:50%; bottom:calc(24px + env(safe-area-inset-bottom)); transform:translateX(-50%); min-height:44px; padding:8px 16px; border:1px solid var(--rule); border-radius:999px; background-color:var(--card); color:var(--ink-soft); font-family:"IBM Plex Mono",monospace; font-size:14px;`. It sits inside the sticky stage, not `position:fixed`, because act three is transformed during the wipe.

- Appears 700ms after the end step if `act3.scrollTop` < 4% of its scroll range. Fade in 300ms (`opacity`, motion allowed only).
- Gone for good once q ≥ 4% or it is clicked. Clicking it scrolls act three to the end (`behavior:'smooth'`).
- Never shown under reduced motion (there is nothing to scroll for, 23.2).

### 21.6 Fallback: browsers without `animation-timeline`

Same idea as R4. In `html.fb` (motion allowed, no scroll timelines), the act's scroll listener sets `#nerd-stage` `data-q` to `0` (q < 5%), `1` (5 to 20%), `2` (20 to 75%) or `3` (q ≥ 75%). CSS keyed on that attribute applies the same end states as the keyframes (q=0: rest; 1: beats gone, `--g-on:.8`; 2: ink, `--s-peak`, `--g-on:1`; 3: ink, `--s-rest`, `--g-on:0`, chips visible) with `transition: transform .6s cubic-bezier(.22,.7,.2,1), opacity .5s ease, background-color .6s ease, color .6s ease, --g .4s, --g-on .4s`. Steps, not scrubbing, but the same scenes. The slice animation and the `.is-scrolling` rule are unchanged.

---

## 22. The three branch links (card item 4)

### 22.1 How they appear

They **emerge from the word**: between q = 70% and 88% each chip moves out and down from the word's center to its place, growing from 60% to full size and fading in, staggered left to right, so the word visibly "branches out" into three [Nick-C]. Their final row sits under the word: `.chips { position:absolute; left:0; right:0; bottom:clamp(40px,14svh,140px); display:flex; justify-content:center; flex-wrap:wrap; gap:16px; padding:0 var(--pad); }` (gap 12px under 560px wide).

```css
/* individual transform properties, so the chip's hover/focus `transform` still works on top */
.chip[data-passion="techie"]      { animation:nerd-branch-1 linear both; animation-timeline:--nerd; }
.chip[data-passion="gamer"]       { animation:nerd-branch-2 linear both; animation-timeline:--nerd; }
.chip[data-passion="photographer"]{ animation:nerd-branch-3 linear both; animation-timeline:--nerd; }
@keyframes nerd-branch-1{ 0%,70%{ opacity:0; translate:48px -40px;  scale:.6; } 84%,100%{ opacity:1; translate:0 0; scale:1; } }
@keyframes nerd-branch-2{ 0%,72%{ opacity:0; translate:0 -40px;     scale:.6; } 86%,100%{ opacity:1; translate:0 0; scale:1; } }
@keyframes nerd-branch-3{ 0%,74%{ opacity:0; translate:-48px -40px; scale:.6; } 88%,100%{ opacity:1; translate:0 0; scale:1; } }
```

Why `translate`/`scale` and not `transform`: a scroll animation with `both` fill holds its end value forever. If it held `transform:none`, it would override the chip's hover and focus lift (the same trap 17.3.4 avoided with `backwards`). The individual properties stack with `transform`.

**Pointer gating:** `.chips { pointer-events:none; }` until JS adds `.is-live` to `#nerd-stage` at q ≥ 90% (same pattern as scene 3, section 6). Keyboard focus is never gated (23.3).

### 22.2 Styling: the fork scene's chip, on ink

**Decision: reuse the prong chip exactly.** Each link carries both classes, `prong chip`, so it inherits every `.prong` rule from 17.3.4: IBM Plex Mono 500 16px, square corners, 2px border, `--card` face, `--ink` text, the hard 4px pixel shadow, the hover/focus lift to `translate(-2px,-2px)` with a 6px shadow, the press-down on `:active`, the pine focus outline and the blinking ▼ caret above. Same game-menu voice as "research / technology / passion", one level deeper. (The existing prong script selects `.prongs .prong`, so these chips, which sit outside `.prongs`, are not picked up by it.)

Additions for anchors on ink:

```css
.chip{ display:inline-flex; align-items:center; text-decoration:none; }
.chip[data-passion="techie"]      { --prong-c: var(--leaf); }             /* terminal green */
.chip[data-passion="gamer"]       { --prong-c: rgb(var(--glow-ember)); }  /* ember red */
.chip[data-passion="photographer"]{ --prong-c: var(--rule); }             /* silver, like film */
.nerd-status{ margin:0; position:absolute; left:0; right:0; bottom:clamp(8px,5svh,48px);
  padding:0 var(--pad); min-height:1.6em; font-style:italic; font-size:clamp(17px,1.6vw,19px); color:var(--rule); }
```

The prong colors (pine, slate, brick) mostly disappear on ink, so the three shadows use existing tokens that show up on dark: leaf, ember, rule. No new hex. Labels are lowercase exactly as Nick wrote them, in his order: `techie`, `gamer`, `photographer`.

Spike measurements (rest state): at 1440×900 the chips sit at y 730 to 774, under a word ending at y 484; at 390×844 they fit on one row (x 31 to 359); at 320×568 `photographer` wraps to a second centered row; at 844×390 they sit at y 291 to 335 under a word ending at y 212. No overlap and no horizontal overflow at any size [Spike2].

### 22.3 Stub behavior for this card (decided: real links, honest stub, no `preventDefault`)

**Product call:** the content is coming very soon, so the links are **real anchors wired to their final hrefs now** (19.3). They are not buttons that will need rewiring later. What changes is only what the router does when it sees `#passions-…`.

When a chip is activated (click, tap, Enter):

1. The browser follows the fragment link natively. The URL becomes `intro.html#passions-techie` and a history entry is pushed. No element has that id yet, so nothing scrolls. **No `preventDefault`** (R31 stays at zero).
2. The chip's own `click` handler clears `#nerd-status`, then on the next animation frame writes `<Label> is coming soon. Still nerding out on it.` (`Techie is…`, `Gamer is…`, `Photographer is…`). Clearing first makes a repeat click re-announce. Placeholder copy, Flag B4.
3. The router (R48) sees a `#passions-` hash and leaves act three exactly as it is (open, scrolled to the links). It does **not** announce (the click handler already did), unless this is a direct load (step 4).
4. Direct load or new tab (`intro.html#passions-gamer`, from a Cmd-click or a shared link): the router opens act three at its end state (q = 100%, chips live, no wipe, no reveal) and announces the matching line once.

Each chip has `aria-describedby="nerd-soon"` ("Coming soon."), the same reasoning as 17.3.4: real, enabled links whose description says "Coming soon." are honest and look as live as they are. No `aria-disabled`. Back from `#passions-techie` returns to `#nerd` (same screen, status cleared), which is exactly how Back will behave once the deep-dive page exists.

---

## 23. Responsive and accessibility (card items 6 and 7)

### 23.1 Responsive

| Concern | Desktop (≥ 900px) | Mobile (< 560px) | Short screens (`max-height:500px`) |
|---|---|---|---|
| Wipe | full viewport, from the right | same | same |
| Beats | 128px, three lines | `16vw` (62px at 390, 56px floor at 320) | capped at `22svh` (86px at 390 tall) |
| Clap | `.62em` of the line | same | same |
| Takeover peak | 130% of viewport width | same | same |
| Rest word | `--s-rest`: 92% of padded width or 38% of height, whichever is smaller | same formula | same formula (word about 150px tall at 844×390) |
| Chips | one row, gap 16px, 16px text | one row at 390 (gap 12px, 15px text); wraps to two centered rows under 360px | one row, 14px text, padding 8px 10px |
| Chip height | ≥ 44px | ≥ 44px | ≥ 44px |
| Hover lift / caret | `@media (hover:hover)` | none; focus-visible still shows them | per device |
| Cue | bottom center | bottom center plus safe-area inset | bottom center |
| Status line | under the chips | same, wraps | same |
| Scrollbar | hidden | hidden | hidden |

`svh` only, never `dvh` (section 5). Safe-area insets on the cue and status line. Touch scrolling of act three is native momentum scrolling with no gesture code, so the glitch follows the thumb.

### 23.2 Reduced motion (photosensitivity: a real requirement)

With `prefers-reduced-motion: reduce`:

- **No wipe.** Act three appears in one cut at t = 0. Focus goes to `#nerd-title` at once.
- **No staccato slams, no clap pops, no glitch layers at all** (the `::before`/`::after` rules only exist inside the motion-allowed media query), no scale, no dark flip, no scanlines, no slices, no cue.
- **Layout is static:** `.nerd-track { height:auto; }`, `.nerd-stage { position:static; min-height:100svh; height:auto; }`, paper background, ink text, the three lines centered and the chips directly below them in normal flow (`.chips`, `.nerd-status` `position:static; margin-top:clamp(28px,5svh,48px)`), chips live at once (no pointer gating).
- **A clean fade, as the card asks:** the script runs two Web Animations API fades, opacity only, no transforms: `.beats` from 0 to 1 over 400ms `ease-out`, and `.chips` from 0 to 1 over 300ms starting at 300ms. The spike confirmed WAAPI fades still run under the page's global reduced-motion rule (`animation:none !important`), because that rule only stops CSS animations [Spike2]. An opacity fade is not motion and cannot flash.
- **No flashing in any state.**
- Toggling the setting while act three is open applies live through the media queries. A visitor who switches to reduced motion mid-glitch gets the static layout at once.

### 23.3 Screen readers and keyboard

- **Clean text only:** the `<h2>`'s accessible name is exactly `I'm a nerd.` The visual beats, claps, period span and glitch copies are all `aria-hidden` or empty-alt pseudo content. Nothing glitched, doubled or emoji-named reaches assistive tech.
- **Announcements:** focus at t = 820ms to `#nerd-title` says "I'm a nerd., heading level 2". Chip activation is announced by the `role="status"` line. The section is a named region (`aria-labelledby="nerd-title"`); the chips are a group labelled by the heading; each chip is a `link` described by "Coming soon.".
- **Tab order inside act three:** cue (if visible), `techie`, `gamer`, `photographer`. The skip link stays above everything (`z-index:20`), so Shift+Tab reaches it.
- **Focus never sits on something invisible:** while act three is entering, `.chips` is `inert`, so the chips can't be tabbed to. After the end step, when a chip receives focus while q < 90%, the script scrolls act three to the end (`smooth`, or `auto` under reduced motion), the same rule as R13.
- **Keyboard scrolling:** with focus on `#nerd-title` (inside the act's scroller), Space, Page Down and the arrow keys scroll act three natively. No key handling code beyond the skip.
- **Back:** focus returns to the `passion` prong on the fork scene (R48).

---

## 24. Requirements, deployment, flags, feasibility, non-goals

All requirements use the section 7 harness (local `python3 -m http.server 8000`, Chromium over CDP, the same desktop, mobile and reduced-motion emulation). "At the fork" means a direct load of `http://localhost:8000/intro.html#where`, wait 600ms. "Open act three" means at the fork, click `.prong[data-prong="passion"]`, wait 3400ms. "Set q" means `const a=document.getElementById('nerd'); a.scrollTop=(a.scrollHeight-a.clientHeight)*q`, then wait 400ms. Build/deployment for every requirement: **not Docker**, by the same justified exception as section 8 (static GitHub Pages site; nothing to containerize; deploy is a push to `main`, which stays forbidden).

### R33. Activating the passion prong starts act three in the same page: no navigation, the URL becomes `#nerd`, and research and technology are unchanged stubs.
- **Source:** [Nick-C] "Let's start with 'passion.' It opens to…"; [Card3] item 1; section 20.1, 19.4.
- **Acceptance:** at the fork, set `window.__stay = 1`, click the passion prong; after 3400ms: `window.__stay === 1`, `location.pathname` ends in `/intro.html`, `location.hash === "#nerd"`, `document.getElementById('nerd').hidden === false`, `document.querySelector('#where .fork-scene').inert === true`, `document.querySelector('main').inert === true`, avatar `dataset.look === "passion"`. The passion prong has no `aria-describedby`; research and technology still have `aria-describedby="fork-soon"`, and clicking each still writes the R26 line to `#fork-status` with `location.hash` staying `#where`. `#nerd` comes after `#where` in the DOM, outside `main` (`document.querySelector('main #nerd') === null`).
- **Edge cases:** double-click, or Enter then click, starts act three once (`document.getAnimations().filter(a => a.animationName === "nerd-wipe").length <= 1` at all times); Enter and Space on the focused passion prong both start it; activating passion while act two is still in its curtain sequence is impossible (`.fork-scene` is inert until act two's end step).
- **Resources:** `intro.html` markup, prong handler, state machine.

### R34. Act three wipes in from the right over 700ms after a 120ms beat, with a hem shadow and a skip.
- **Source:** [Card3] item 1; section 20.2 (assumption: timings).
- **Acceptance:** motion allowed, 1440×900, at the fork click passion at t = 0: (a) a `nerd-wipe` animation exists on `#nerd` with `getTiming()` `duration 700`, `delay 120`, `easing "cubic-bezier(0.7, 0, 0.2, 1)"`; (b) at t ≈ 450ms the act's computed transform `tx` is strictly between 0 and `innerWidth`; (c) at t ≈ 1000ms `tx` is 0 and `document.activeElement.id === "nerd-title"`; (d) while `is-entering`, `getComputedStyle(nerd).overflowY === "hidden"`; after the end step (t ≈ 3400ms) it is `auto` and `nerd.classList.contains('is-entering') === false`. **Skip:** fresh run, at t ≈ 900ms dispatch `keydown` Escape on `document`; within 150ms `is-entering` is gone and every `.beat` has computed opacity `"1"`. A `keydown` at t ≈ 100ms does **not** skip.
- **Edge cases:** background tab during the entry: the 3200ms safety timeout still runs the end step; resizing mid-wipe still covers the screen; `document.documentElement.scrollWidth <= innerWidth` throughout (the off-screen start position must not add page width).
- **Resources:** `intro.html` CSS (`nerd-wipe`), script.

### R35. The reveal shows "I'm. 👏", "A. 👏", "Nerd. 👏" on three centered lines, and assistive tech gets exactly "I'm a nerd."
- **Source:** [Nick-C] "'I'm. 👏 A. 👏 Nerd.👏'"; [Card3] item 2; sections 20.1, 20.3.
- **Acceptance:** after the end step: the three `.beat` elements' `textContent` are `"I'm.👏"`, `"A.👏"`, `"Nerd.👏"` (U+0027 apostrophe, U+1F44F); each `.clap` contains exactly `👏`; `.beats` has `aria-hidden="true"`; `#nerd-title` is an `H2` containing a `.vh` span whose `textContent === "I'm a nerd."`. CDP `Accessibility.getFullAXTree`: the heading node's name is exactly `I'm a nerd.` and no AX node's name contains `👏`, `clapping` or `Nerd.Nerd`. The three `.beat` boxes are stacked (`beat1.bottom <= beat2.top + 2`, `beat2.bottom <= beat3.top + 2`) and each box's horizontal center is within 4px of `innerWidth/2` at 1440 and 390.
- **Edge cases:** no line wraps (`white-space:nowrap`) and no horizontal overflow at 320 wide; a missing emoji font only affects the hidden visual; the `.vh` text stays out of view (bounding width ≤ 1px).
- **Resources:** `intro.html` act-three markup.

### R36. The reveal is staccato: each word slams in on a 520ms beat, each clap pops 260ms after its word, and it ends 2720ms after the click.
- **Source:** [Nick-C] "a dramatic animation"; [Card3] item 2 "concrete per-segment timing"; table in 20.3 (assumption: values).
- **Acceptance:** motion allowed, open act three, and at t ≈ 900ms read `document.getAnimations()`: `beat-in` animations with delays `1220` and `1740` (duration 180), `beat-in-big` with delay `2260` (duration 240), and three `clap-in` with delays `1480`, `2000`, `2520` (duration 200), all with `easing` starting `cubic-bezier(0.2, 0.9, 0.3`. At t ≈ 1300ms `.beat-1` opacity > 0.5 and `.beat-2` opacity < 0.05; at t ≈ 2100ms `.beat-2` opacity > 0.95 and `.beat-3` opacity < 0.05; at t ≈ 3000ms all beats and claps opacity > 0.95.
- **Edge cases:** skip (R34) jumps straight to the landed state; a slow font load falls back to Georgia in place without moving the timing; the `is-entering` removal must not make anything blink (base styles are fully visible).
- **Resources:** `intro.html` CSS keyframes `beat-in`, `beat-in-big`, `clap-in`.

### R37. The reveal uses Fraunces in the `welcome.` voice, "Nerd." in the `Nick.` logotype voice with a moss period, and OS color emoji, with no new font families.
- **Source:** [Card3] item 2 "font choice (reuse Fraunces/EB Garamond…)"; section 20.3.
- **Acceptance:** `.beat-1` computed `fontFamily` starts with `"Fraunces"`, `fontWeight === "600"`; `.nerd-word` computed `fontWeight === "800"`, `fontVariationSettings` contains `"SOFT" 50`, `letterSpacing` negative; `.nerd-word .dot` `color === "rgb(126, 156, 96)"`; the first two beats' periods are `--ink` (no `.dot` inside `.beat-1`/`.beat-2`); `.clap` `fontFamily` starts with `"Apple Color Emoji"`; `.beat` computed `fontSize` is `128px` at 1440×900, between 60 and 64px at 390×844, `56px` at 320×568, and ≤ 86px at 844×390. `.nerd-word` does not have class `logotype` and its computed `willChange === "auto"`. The Google Fonts URL is unchanged (R14).
- **Edge cases:** Fraunces blocked: Georgia fallback keeps the stack centered; at 844×390 the three lines plus gaps fit inside the viewport before any scroll (`beat3.bottom <= innerHeight`).
- **Resources:** `intro.html` CSS.

### R38. Act three is a scroll track driven by its own named scroll timeline, gated by `@supports` and motion preference, with no scroll hijacking.
- **Source:** [Nick-C] "as they scroll"; section 21.1; [Spike2] F10.
- **Acceptance:** `grep -c "scroll-timeline: *--nerd" intro.html` ≥ 1 and `grep -c "animation-timeline: *--nerd" intro.html` ≥ 6; motion allowed, act three open: `document.getAnimations().filter(a => a.timeline && a.timeline.constructor.name === "ScrollTimeline" && a.timeline.source === document.getElementById('nerd')).length` ≥ 6; `#nerd .nerd-track` height ≥ 2.9 × `innerHeight`; `#nerd-stage` computed `position === "sticky"`. Scrubbing: at q = 0.12 the `.beat-1` opacity is strictly between 0.05 and 0.95. `grep -ci "preventDefault" intro.html` = 0; `getComputedStyle(document.documentElement).overflowY !== "hidden"` and the same for `body`. **Cue:** after the end step with no scroll, wait 900ms: `#nerd-cue` is not hidden and its text contains `keep scrolling`; set q = 0.05: within 500ms the cue is hidden; on a fresh run, clicking the cue brings q ≥ 0.95 within 1500ms.
- **Edge cases:** scrolling back up reverses every scroll animation; touch swipe on 390×844 (`Input.dispatchTouchEvent` start y=700, move to y=200, end) increases `#nerd`'s `scrollTop`, not `window.scrollY`; the act's scrollbar is hidden (`getComputedStyle(nerd).scrollbarWidth === "none"`); wheel input at the end of act three does not scroll the page underneath (`overscroll-behavior:contain`).
- **Resources:** `intro.html` CSS and script.

### R39. "Nerd." glitches with two offset, sliced color copies whose strength follows the scroll, and the slices move only while the visitor is scrolling.
- **Source:** [Nick-C] "the word 'nerd' should start to 'glitch out'"; [Card3] item 3; section 21.3.
- **Acceptance:** motion allowed, act three open: the registered property scrubs: `getComputedStyle(nerdWord).getPropertyValue('--g')` is `0px` at q = 0 and ≥ `6px` at q = 0.55 (1440×900); `getComputedStyle(nerdWord,'::before').content` contains `Nerd.` and its `color === "rgb(196, 84, 58)"`; `::after` `color === "rgb(207, 226, 166)"`; at q = 0.55 `::before` opacity ≥ 0.95 and its transform `tx` ≤ −6. Animations named `slice-a` and `slice-b` exist with `duration 1500`, `iterations Infinity`, `easing "steps(1, end)"`, and equal `delay` (0). With no scroll for 600ms, both have `playState === "paused"`; during a scroll (dispatch a scroll by `scrollBy(0,40)` every 100ms for 600ms) at least one check sees `playState === "running"` and `#nerd.classList.contains('is-scrolling')`. **Rendered check:** screenshot at q = 0.55, 1440×900, while paused: at least one pixel inside the word's box matches ember (`R ≥ 170, G ≤ 110, B ≤ 90`) and at least one matches leaf (`R ≥ 190, G ≥ 210, B ≥ 140`).
- **Edge cases:** no `<canvas>`, SVG filter or external script is used (`grep -cE "<canvas|feTurbulence|feDisplacementMap" intro.html` = 0); the glitch copies never change the word's accessible name (R46); the word stays sharp at peak (no `will-change`, R37).
- **Resources:** `intro.html` CSS (`@property`, `slice-a`, `slice-b`), scroll listener.

### R40. As the visitor scrolls, "Nerd." takes over the page: it grows past both screen edges, the page turns to ink with scanlines, then it settles clean.
- **Source:** [Nick-C] "take over the page"; [Card3] item 3 "give a specific visual direction"; section 21.2.
- **Acceptance:** motion allowed, act three open, at 1440×900 and 390×844: at q = 0.55, `.nerd-word` bounding `width ≥ innerWidth` and its `left ≤ 0`; `#nerd-stage` computed `backgroundColor === "rgb(22, 36, 28)"`; `.nerd-word` `color === "rgb(248, 250, 244)"`; `.nerd-scan` opacity ≥ 0.75. At q = 0.15: `backgroundColor === "rgb(234, 238, 228)"`. At q = 1: word `width ≤ innerWidth − 2·pad + 2`, `width ≥ 0.35 × innerWidth`, `top ≥ 0`; `--g-on` is `0`; `.beat-1`, `.beat-2` and all `.clap` opacity < 0.05. `#nerd-stage` has inline custom properties `--s-peak`, `--s-rest`, `--dy`, `--dy-rest`, and resizing from 1440×900 to 390×844 changes `--s-peak`.
- **Edge cases:** no horizontal page overflow at any q (`document.documentElement.scrollWidth <= innerWidth`; the stage's `overflow:clip` crops the word); the period stays moss on ink; resizing mid-scroll re-measures without a jump larger than one frame; the scanlines never animate position.
- **Resources:** `intro.html` CSS (`nerd-bg`, `nerd-takeover`, `nerd-scan`) and the geometry function.

### R41. Three links, "techie", "gamer", "photographer", branch out of the word and wear the fork scene's chip style.
- **Source:** [Nick-C] "Nerd can branch out and link to a few things 'techie' 'gamer' 'photographer' that people can click on"; [Card3] item 4; section 22.1, 22.2.
- **Acceptance:** motion allowed, act three open: `.chips` contains exactly three `a.prong.chip` with `textContent` `techie`, `gamer`, `photographer` in DOM order and left to right on screen (or, under 360px, the first two on row one); each has computed `fontFamily` starting `"IBM Plex Mono"`, `borderRadius === "0px"`, height ≥ 44px, `textDecorationLine === "none"`, `cursor === "pointer"`; box-shadow colors `rgb(207, 226, 166)`, `rgb(196, 84, 58)`, `rgb(200, 211, 190)`. At q = 0.6 all three have opacity < 0.05; at q = 1 all three have opacity > 0.95 and their tops are > the word's bottom + 24px. Animations `nerd-branch-1/2/3` exist on the scroll timeline. Hover at q = 1 (CDP mouseMoved to a chip's center, 1440×900): computed `transform` `tx = −2, ty = −2` and `::after` opacity `"1"`. Pointer gating: at q = 0.5, `document.elementFromPoint` at a chip's final center does not return the chip; at q = 1, it does.
- **Edge cases:** at 1440, 768, 390, 320 and 844×390 (q = 1) chip boxes don't intersect and sit inside the viewport; touch emulation shows no hover lift; the prong script does not attach its avatar-look handlers to these chips; labels stay lowercase.
- **Resources:** `intro.html` CSS and markup.

### R42. Each link is an honest stub: it goes to its final `#passions-…` hash, announces "coming soon", and shows nothing else.
- **Source:** [Nick-C] "then we can do the three actual things"; [Card3] item 4 "be explicit"; section 22.3.
- **Acceptance:** at q = 1, for each chip: its `getAttribute('href')` is `#passions-techie`, `#passions-gamer`, `#passions-photographer` respectively; click it: within 300ms `location.hash` equals that href, `#nerd-status` (`role="status"`, `aria-live="polite"`) has `textContent === "<Label> is coming soon. Still nerding out on it."` (`Techie`, `Gamer`, `Photographer`), `#nerd.hidden === false`, `window.__stay === 1`, `document.getElementById('passions') === null`, and no new `section` appears. Clicking the same chip twice re-announces (the status is empty on the frame after the click, then refilled). Keyboard: focus a chip and press Enter: same result. Each chip has `aria-describedby="nerd-soon"` and `#nerd-soon` `textContent === "Coming soon."`, visually hidden. No chip has `aria-disabled`. `grep -ci "preventDefault" intro.html` = 0. Zero console errors and zero `Runtime.exceptionThrown` across the run.
- **Edge cases:** a direct load of `intro.html#passions-gamer` opens act three at q = 1 with chips live and announces `Gamer is coming soon. Still nerding out on it.` once; an unknown `#passions-foo` opens act three at q = 1 with no announcement; middle-click opens the same direct-load case in a new tab.
- **Resources:** `intro.html` markup, chip click handler, router.

### R43. The deep-dive constraint is wired in now: all three links point into one future page, never three routes.
- **Source:** [Nick-C] "Those passions should all be contained on one page."; [Card3] item 5; section 19.3.
- **Acceptance:** `grep -oE 'href="#passions-[a-z]+"' intro.html | sort -u` returns exactly the three hrefs in R42 and nothing else; `grep -cE 'href="[^"#]*(techie|gamer|photographer)' intro.html` = 0 (no file links); `git ls-files | grep -ciE "techie|gamer|photographer|passion"` = 0 (no new files); the PRD section 19.3 table exists (`grep -c "passions-photographer" docs/intro-experience-PRD.md` ≥ 1); `BACKLOG.md` has an Open row for the passion deep-dives that contains the words `one page` and `#passions`.
- **Edge cases:** the router treats every `#passions-` hash the same way (one branch, not three); the next card's diff should touch only the router branch, the new `#passions` section and the stub lines (stated in 19.3, verified on that card, not this one).
- **Resources:** `intro.html`, `BACKLOG.md`, this PRD.

### R44. Browsers without `animation-timeline` get a stepped fallback with the same scenes.
- **Source:** section 21.6; same reasoning as R4.
- **Acceptance:** build the forced-fallback copy as in R4 (`sed 's/animation-timeline: scroll()/animation-timeline: nope()/'` so the `@supports` test fails and `html.fb` is set), serve it on 8001, open act three, set q = 0.5, wait 900ms: `#nerd-stage` `dataset.q === "2"`, `backgroundColor === "rgb(22, 36, 28)"`, `.nerd-word` width ≥ `innerWidth`; set q = 1, wait 900ms: `dataset.q === "3"`, all three chips opacity > 0.95 and clickable (R42 click check passes); `getAnimations()` contains no `ScrollTimeline`.
- **Edge cases:** if `CSS.registerProperty` is missing, `--g` jumps instead of easing, and nothing else breaks; the slice pause rule is unchanged.
- **Resources:** `intro.html` CSS (`html.fb` rules) and script.

### R45. Nothing in act three can flash more than 2 times a second, nothing changes on its own after the reveal, and reduced motion gets a clean fade with no glitch at all.
- **Source:** [Card3] item 6 "treat it as a real accessibility requirement"; [WCAG] 2.3.1 and 2.2.2; sections 21.4 and 23.2.
- **Acceptance:** **(a) Motion allowed:** `slice-a` and `slice-b` each have exactly 6 keyframes, `duration 1500`, `steps(1, end)`, the same `delay`, so changes per second = 6 / 1.5 = 4 (≤ 6, the 3-flash limit); after the end step and 600ms with no input, `document.getAnimations().filter(a => a.effect && a.effect.target && document.getElementById('nerd').contains(a.effect.target) && a.playState === "running" && !(a.timeline && a.timeline.constructor.name === "ScrollTimeline")).length === 0` (nothing time-based runs inside act three while still; the avatar idle and pill ember underneath are outside it and out of scope); `grep -ciE "filter: *invert|animation:[^;]*blink" intro.html` = 0. **(b) Reduced motion emulated:** open act three: `#nerd.hidden === false` and focus on `#nerd-title` within 100ms (no wipe); `document.getAnimations()` contains no `CSSAnimation` and nothing on a `ScrollTimeline` at t = 50, 500 and 2000ms; every script-made animation (`a.constructor.name === "Animation"`) animates only `opacity` (`a.effect.getKeyframes()` keys limited to `opacity`, `offset`, `easing`, `composite`, `computedOffset`); ignore `CSSTransition`s, which the global rule shortens to 0.01ms; at t ≈ 150ms `.beats` opacity strictly between 0.05 and 0.95 (it fades), at t ≈ 800ms both `.beats` and `.chips` opacity "1"; `getComputedStyle(nerdWord,'::before').content === "none"`; `#nerd-stage` background `rgb(234, 238, 228)` and `position` not `sticky`; chips are clickable at once (R42 passes without scrolling); `#nerd-cue` stays hidden.
- **Edge cases:** toggling reduced motion while act three is open switches to the static layout without a reload; skip still works; R29's act-two checks still pass.
- **Resources:** `intro.html` CSS and script.

### R46. Keyboard and screen-reader users get the whole beat: the clean heading, operable links, and no focus on hidden content.
- **Source:** [Card3] item 6; section 23.3.
- **Acceptance:** keyboard only, at the fork: Tab to `passion`, press Enter; at t ≈ 1000ms `document.activeElement.id === "nerd-title"`; after the end step, Tab reaches `techie`, `gamer`, `photographer` in order (the cue first if it is showing); focusing `techie` at q = 0 brings q ≥ 0.95 within 1500ms (motion) or immediately (reduced) and the chip is fully inside the viewport. While act three is open, `main.inert === true` and `.fork-scene.inert === true`. Shift+Tab from `techie` eventually focuses the skip link, which `elementFromPoint` confirms is on top. CDP `Accessibility.getFullAXTree`: a `region` named `I'm a nerd.`, a `heading` level 2 with that name, a `group` with three `link`s named `techie`, `gamer`, `photographer`, each with description `Coming soon.`, a `status` node, and no node whose name contains `👏` or a doubled `Nerd.`.
- **Edge cases:** before the click, act three is `hidden` and absent from the AX tree; VoiceOver hears no "dimmed"; the visible focus outline shows on every chip (`outline-style` not `none` on `:focus-visible`).
- **Resources:** `intro.html`.

### R47. Act three works at desktop, tablet, mobile and landscape-phone sizes with no horizontal overflow.
- **Source:** [Card3] item 7; [Nick] original brief "desktop and mobile friendly"; section 23.1.
- **Acceptance:** at 1440×900, 768×1024, 390×844, 320×568 and 844×390, act three open, at q = 0, 0.55 and 1: `document.documentElement.scrollWidth <= innerWidth` and `#nerd.scrollWidth <= #nerd.clientWidth`; at q = 0 all three beats are inside the viewport; at q = 1 the word, all chips and the status line are inside the viewport and chips are ≥ 44px tall. `grep -c "dvh" intro.html` stays 0. `env(safe-area-inset-bottom)` appears in the cue's CSS.
- **Edge cases:** rotating the phone mid-scroll re-measures geometry (R40); iOS URL-bar changes don't move the sticky stage (`svh`); hover-only styles stay under `@media (hover:hover)`.
- **Resources:** `intro.html` CSS.

### R48. Back, Forward and direct links work across all four states.
- **Source:** section 19.4; extends R27.
- **Acceptance:** (a) after R33, `history.back()`, wait 500ms: `location.hash === "#where"`, `#nerd.hidden === true`, `.fork-scene.inert === false`, `document.activeElement` is the passion prong, the fork's curtain stays hidden, and no `nerd-*`/`beat-*`/`clap-*` animation remains (`document.getAnimations().filter(a => /nerd|beat|clap|slice/.test(a.animationName)).length === 0`); (b) `history.forward()`: act three is open at q = 0 with no wipe (`nerd-wipe` absent) and all beats opacity "1" within 300ms; (c) direct load of `intro.html#nerd`: within 600ms act three is open at rest, act two is open underneath, `main.inert === true`, the R6 nudge stays hidden after 4500ms; (d) from `#passions-techie`, `history.back()` returns to `#nerd` with `#nerd-status` empty; (e) Back twice from `#nerd` reaches the pill scene with R27(b) passing.
- **Edge cases:** Back during the entry aborts it cleanly (act three hidden, no orphaned animations after 500ms); the router is idempotent, so a `popstate` plus `hashchange` pair for one navigation does one thing (anchor clicks fire both in Chromium [Spike2]); reloading on any of the four hashes restores that state.
- **Resources:** `intro.html` router (one `route()` called on load and on `popstate`).

### R49. Palette, fonts, script budget, file footprint, and nothing earlier regresses.
- **Source:** R31, R32; section 19.4.
- **Acceptance:** the R31 hex grep returns the same set as at 15e3e2a (**no new hex**); the Google Fonts URL is unchanged; `grep -cE "<script[^>]+src=" intro.html` = 0; the main inline script is under 330 lines; `grep -ci "preventDefault" intro.html` = 0; `git diff --name-only 15e3e2a..HEAD` lists only `intro.html`, `BACKLOG.md` and files under `docs/`. All acceptance checks of R1 to R9, R11 to R25 and R27 to R32 pass again, with the amendments in 19.4 (R26 and R30 apply to research and technology only; R31's script limit is 330).
- **Edge cases:** no new font, image, CSS or JS files; no third-party code; act two's own timings, skip and Back behavior are unchanged.
- **Resources:** `intro.html`; `index.html` (read-only).

### 24.1 Deployment and build

Unchanged from sections 8 and 18.1: **not Docker**, by the same justified exception (static GitHub Pages site, nothing to containerize, production deploy is a push to `main`, which stays forbidden). Local preview `python3 -m http.server 8000` from the repo root on `feature/intro-experience`. Demo URLs: `http://localhost:8000/intro.html#where` (then tap passion) and `http://localhost:8000/intro.html#nerd`. No build step. The build card may push `feature/intro-experience` to origin.

### 24.2 Flags for Nick (addendum 2)

1. **B1, copy.** You wrote `Nerd.👏` with no space and the others with a space. I gave all three the same small gap, and stacked the beats on three lines at every screen size. Only the "Nerd." period is green.
2. **B2, the page goes dark.** "Takes over the page" became: the word grows past the screen edges while the page flips from paper to ink with faint scanlines, then the word settles and the links appear on the dark screen. It is the first dark screen on the site.
3. **B3, glitch colors.** Ember and light green from your existing palette, not true RGB red and cyan. It reads more like misregistered print than a CRT. True RGB would mean two new colors.
4. **B4, stub copy.** "Techie is coming soon. Still nerding out on it." is placeholder text. Change freely.
5. **B5, the glitch only moves while you scroll.** When the visitor stops, the slices freeze, and the glitch fully clears once the links show. That is deliberate. A glitch that crackles on its own forever would break accessibility rules on flashing and on motion you can't stop.
6. **B6, "one page" means one layer inside `intro.html`.** The deep-dives will be one scrolling page with techie, gamer and photographer sections, opened from these links. If you'd rather it be its own file (`passions.html`), it's a three-href change and still one page.
7. **B7, real-device check.** Emoji and iOS momentum scroll inside the overlay are worth 2 minutes on your phone. Emulation can't prove either.

No new cost, services, infrastructure or recurring manual steps.

### 24.3 Feasibility (spike method) and risks

I ran a throwaway spike: one HTML page with the act-three layer, beats, claps, glitch, takeover and chips. I served it locally on port 8011 and measured it in Chromium over CDP at 1440×900, 390×844, 320×568 and 844×390, plus image checks of three screenshots. It lived in my scratch folder and is not in the repo. Every value it validated is written into sections 20 to 22 above.

| # | Given / When / Then | Verdict | Evidence |
|---|---|---|---|
| F10 | Given a `position:fixed; overflow-y:auto` layer with `scroll-timeline:--nerd block`, when its children (including `::before`/`::after`) use `animation-timeline:--nerd`, then they scrub with the layer's scroll. | VALIDATED | `getAnimations()` listed `nerd-bg`, `drop`, `takeover`, `scan`, `branch` on a `ScrollTimeline`; at q = 0.12 `--g` was 1.79px and `::before` transform `tx` −1.79; at q = 0.55 `tx` −7.68 and background `rgb(22,36,28)`. |
| F11 | Given `@property --g` / `--g-on`, when scroll keyframes animate them and use `var(--s-peak)` inside `transform`, then they interpolate. | VALIDATED | `--g-on` 0 → 0.373 → 1 → 0.3 across q (the 0.3 rest was then changed to 0); word width at q = 0.55: 1873px at 1440, 507 at 390, 1096 at 844, 416 at 320 (all ≥ viewport). |
| F12 | Given a Fraunces 800 word scaled 6.7×, when rendered at the takeover, then it stays sharp and reads as a glitch takeover. | VALIDATED | Image check: "Sharp… no obvious blur"; "Yes, particularly as a sliced, offset-layer glitch"; "Definitely" takes over the page. Found a visible scrollbar strip (now hidden, 20.1) and leftover glitch at rest (now cleared, 21.4). |
| F13 | Given 👏 after each beat, when rendered, then it shows in color and reads as a staccato beat. | PARTIAL | Image check: "all three clapping-hands emoji render in full color… strongly reads as a dramatic, staccato moment." Only proven on this Mac's emoji font (Flag B7). Beats measured too small at 390 (48px), so the size became `min(clamp(56px,16vw,128px),22svh)`. |
| F14 | Given three Plex Mono chips, when laid out at the four sizes, then they don't overlap and stay in view. | VALIDATED | No overlap and `scrollWidth` = viewport at all sizes; one row at 390 (x 31 to 359), two rows at 320. |
| F15 | Given the page's global `animation:none !important` reduced-motion rule, when the script runs a WAAPI opacity fade, then it still plays. And given a `#passions-*` anchor, when clicked, then the router can see it. | VALIDATED | Opacity at 200ms of a 400ms fade: 0.877. One click fired `popstate` then `hashchange`; a repeat click fired `popstate` again, so the router must be idempotent (R48). |

Risks:

- **Photosensitivity.** Mitigated by design (21.4, R45): ≤ 4 changes a second, nothing time-based while still, scrubbed dark flip, nothing at all under reduced motion. One residual risk: a visitor who flicks the wheel up and down very fast could scrub the paper/ink flip quickly. That is user-driven, it spans 60svh per direction, and it is accepted.
- **Safari text scaling.** Some engines rasterize a scaled text layer once and stretch it. Mitigated by forbidding `will-change` (R37). Real-device check is Flag B7.
- **Emoji on systems without a color emoji font** (old Linux) show an empty box. It is visual only, since the line is `aria-hidden` and screen readers get "I'm a nerd." Accepted.
- **Scroll inside an overlay** is less familiar than page scroll. Mitigated by the cue (21.5) and native keyboard scrolling from the focused heading.
- **Specificity fights between the entry and scroll animations** on the beats. Mitigated by blocking scroll during entry and letting the `is-entering` rules win until the end step (20.2).
- **Scope creep into the deep-dives.** This is the biggest practical risk for an AI builder. Sections 19.2, 19.3 and 24.4 rule it out explicitly.

### 24.4 Non-goals for addendum 2 (do not build)

- **Anything behind techie, gamer or photographer:** no `#passions` section, no content, images, tabs or subsections, no modals or drawers. A chip only goes to its hash and announces "coming soon" (R42).
- **Three separate routes, files or layers for the passions, ever.** The future deep-dive is one page (19.3).
- Any change to the `research` or `technology` prongs, act two's curtain or timings, the scroll intro, the nudge, or the blue pill.
- Tiling or repeating "nerd" across the screen, typewriter or scramble-text effects, sound, particles, canvas, WebGL, SVG filters, CRT bulge or a moving scanline.
- A glitch that runs on its own when the visitor isn't scrolling, a glitch on chip hover, or any flicker above the R45 rate.
- Drawn "branch" lines or SVG paths connecting the word to the chips, and any avatar appearance in act three.
- A visible exit or "straight to business" link in act three (same open question as Flag A6), a replay control, or persisting anything (cookies, storage) or analytics.
- Any change to `index.html`, the case-study pages, `resume.html`, `README.md`, `CNAME`, `AGENTS.md`, or new HTML, CSS, JS, image or font files. No JS libraries, CDN scripts or build tooling. No push to or merge into `main`, and no PR.

**Authorized boundaries (build card t_593e8d60):** edit `intro.html` on `feature/intro-experience` in `~/Documents/github/portfolio`; update `BACKLOG.md` rows for this work; commit and `git push origin feature/intro-experience`; run or reuse the local preview server on port 8000.

**Forbidden actions:** editing any other site file; pushing any other branch; committing to or merging into `main`; adding dependencies, files or services beyond the preview server.

### 24.5 Follow-ups (logged in BACKLOG.md, not requirements)

- **Passion deep-dives:** build techie, gamer and photographer as **one page** (`#passions`, three subsections), per 19.3. The router branch and stub lines are the only wiring to change.
- Optional: a glitch-on-hover touch for the chips, if Nick wants more life on the rest screen (would need its own flash-rate check).
- The research and technology prongs (already logged).

---

---

# Addendum 3: passion deep-dive backgrounds (techie, gamer, photographer) (card t_027c5838)

Added 2026-11-12 by product. Builds on `intro.html` at commit 560f493 (act three, with the three chips wired to `#passions-*` stubs). Same harness, tokens, fonts and conventions as sections 1 to 24 unless a line below says otherwise. Build card: t_24e05978 (assignee `design`). This addendum is sections 25 to 31 and requirements R50 to R65.

## 25. Source, scope, sequencing and what it changes

### 25.1 Source brief (Nick, verbatim, via card t_027c5838)

> Let's talk about how these passion screens will play out. Each the background should fill up with certain things. For techie we want a circuit board pattern/design to draw itself across the screen. For photography, I will provide photos to fill in the background as a messy collage that idly shuffles around. For gamer, I'd like it to fill in with a full screen loop of gifs of gameplay from some of my favorite games (sourced from the web). We will need to include a disclaimer that I don't own any of the background art on that one.
>
> Gamer list: borderlands, Pokemon series games, Fire emblem, Smash bros, Destiny, Baldur's gate.
>
> You source them. I don't have the time. I'll send photos in a later message.

Citation shorthand added: **[Nick-D]** = the brief above. **[Card4]** = card t_027c5838's body (scope, sequencing and its six required items). **[Spike3]** = the throwaway prototype I ran for this addendum; results in 31.3. **[WCAG]**, **[GIPHY-ToS]**, **[GitHub-DMCA]**, **[web.dev-video]** = sources listed under Research sources.

### 25.2 Scope and sequencing

| Background | Status | Depends on | Who builds it |
|---|---|---|---|
| Techie (circuit board draws itself) | **Buildable now** | nothing | build card t_24e05978 |
| Gamer (looping gameplay + disclaimer) | **Buildable now** | the build worker sources the clips. Nick delegated it: "You source them. I don't have the time." | build card t_24e05978 |
| Photographer (messy collage that shuffles) | **Mechanism buildable now. Real photos BLOCKED on Nick** ("I'll send photos in a later message") | Nick's photos | t_24e05978 builds the mechanism with clearly marked placeholder frames (R59). A follow-up card swaps in the real photos (R61). |

**In scope:** the `#passions` layer shell (one section, three subsections, a heading and one placeholder line in each so legibility can be tested), the three backgrounds, the gamer disclaimer and credits, one motion toggle, and routing the chips into the layer.

**Out of scope:** what Nick actually says about being a techie, gamer or photographer. Each panel carries an honest placeholder line until he writes it (Flag C4).

### 25.3 What this changes in sections 1 to 24

| Earlier decision | Change |
|---|---|
| R42: each chip is an honest stub that announces "coming soon" | **Replaced by R50.** The chips now open `#passions` at their subsection. The chip click announcement, the chips' `aria-describedby="nerd-soon"` and the `#nerd-soon` span are removed. The hrefs do not change (19.3 promised this). |
| R43: `git ls-files \| grep -ciE "techie\|gamer\|photographer\|passion"` = 0 | **Amended.** Files under `assets/passions/` are allowed. Still one page, still no new HTML, CSS or JS files. |
| R45: nothing in act three changes on its own | **Unchanged for act three.** Act four has continuous motion because Nick asked for it (shuffle, looping clips), so it meets WCAG 2.2.2 with a pause control instead (R53). |
| R48: router with four states | Same hash families. `#passions-*` now opens act four on top of act three instead of announcing. R48(d) still holds: Back from `#passions-techie` returns to `#nerd`. |
| R31 and R49: one inline script under 330 lines; no new files or images | **Amended.** The main inline script stays one block, under 345 lines (only its router branch and the removed stub lines change). Act four gets **one** second inline block, `<script id="passions-js">`, under 280 lines. So `intro.html` has exactly three `<script>` tags: head bootstrap, main, passions. Still no `src=` scripts and no libraries. Files under `assets/passions/` are allowed. |
| 24.4 non-goal: "Anything behind techie, gamer or photographer" | **Narrowed.** The shell and backgrounds are in scope. Written passion content stays out. |
| Section 1 palette and fonts | **Unchanged.** No new hex and no new font. Every color below is an existing token or an `rgba()` of one. |

### 25.4 Map to the card's six required items

| Card item | Decided in |
|---|---|
| 1. Layout: one shared page, swap vs stacked | 26.1, 26.2, 26.3, R50 |
| 2. Techie background | 27, R54, R55 |
| 3. Gamer background, disclaimer, sourcing, risk | 28, R56, R57, R58, Flag C1 |
| 4. Photographer background (pending photos) | 29, R59, R60, R61 |
| 5. Legibility, reduced motion, accessibility | 26.4, 26.5, 30.2, 30.3, R51, R53, R62, R63 |
| 6. Mobile and desktop | 30.1, R64 |

---

## 26. The shared page (card item 1)

### 26.1 Decision: three stacked subsections in one scrolling layer, each owning its background

| Option | Tradeoff |
|---|---|
| A. One container whose background swaps with the active passion (tabs or scroll-spy) | Needs a tab UI or a scroll-spy. All three hrefs would land on the same box. Mid-swap, two heavy backgrounds coexist. And it contradicts 19.3, which already fixed three subsections in order with their own ids. Rejected. |
| **B. Three stacked full-screen subsections in the one `#passions` layer, each with its own background** | Exactly the shape 19.3 locked and the chips already link to. Each background lives inside its own subsection, so it is only seen, and only runs, while that subsection is on screen. Scrolling down walks techie, then gamer, then photographer, and each background "fills up" as it arrives [Nick-D]. **Chosen.** |

One page, one layer, three subsections, three backgrounds. Only what is on screen animates (26.3).

### 26.2 Structure

```html
<!-- after </section> of #nerd, before the main inline script -->
<section class="act4" id="passions" aria-label="Passions" hidden>
  <button type="button" class="p-motion" id="passions-motion">Pause motion</button>

  <section class="passion techie" id="passions-techie" aria-labelledby="pt-title">
    <div class="p-bg" aria-hidden="true"><svg class="circuit" id="circuit" focusable="false"></svg></div>
    <div class="p-fore">
      <h2 class="p-title" id="pt-title" tabindex="-1">techie</h2>
      <p class="p-copy" data-placeholder-copy>More on this soon.</p>
    </div>
  </section>

  <section class="passion gamer" id="passions-gamer" aria-labelledby="pg-title">
    <div class="p-bg" aria-hidden="true">
      <div class="g-posters" id="g-posters"></div>   <!-- poster fallback: slow network, Save-Data, autoplay blocked, reduced motion -->
      <video class="g-clip" muted loop playsinline preload="none" disablepictureinpicture></video>
      <video class="g-clip" muted loop playsinline preload="none" disablepictureinpicture></video>
      <div class="g-dim"></div>
    </div>
    <div class="p-fore">
      <h2 class="p-title" id="pg-title" tabindex="-1">gamer</h2>
      <p class="p-copy" data-placeholder-copy>More on this soon.</p>
    </div>
    <p class="g-note" id="g-note">Game footage shown for fun. I don't own any of it. All rights belong to the games' developers and publishers.<span class="g-credit" id="g-credit" aria-hidden="true"></span><span class="vh" id="g-credits"></span></p>
  </section>

  <section class="passion photographer" id="passions-photographer" aria-labelledby="pp-title">
    <!-- TODO(photos): placeholder frames until Nick sends photos (PRD R61) -->
    <div class="p-bg" aria-hidden="true"><div class="ph-box" id="ph-box"></div></div>
    <div class="p-fore">
      <h2 class="p-title" id="pp-title" tabindex="-1">photographer</h2>
      <p class="p-copy" data-placeholder-copy>More on this soon.</p>
      <p class="ph-pending">Placeholder frames. Nick's photos are on the way.</p>
    </div>
  </section>
</section>
```

- **Layer:** `.act4 { position:fixed; inset:0; z-index:17; background-color:var(--ink); color:var(--card); overflow-y:auto; overscroll-behavior:contain; scrollbar-width:none; }`, `.act4::-webkit-scrollbar{display:none}`, `.act4[hidden]{display:none}`. z-index 17 sits above act three (16) and below the skip link (20). **The layer is never transformed**, because the motion toggle inside it is `position:fixed`.
- **Subsection:** `.passion { position:relative; min-height:100svh; overflow:clip; isolation:isolate; display:grid; grid-template-columns:minmax(0,1fr); place-items:center; padding:clamp(72px,10svh,120px) 0; }`. The `minmax(0,1fr)` column is required: without it the spike's panel grew past the right edge at 390 and 320 wide, because an auto grid track sizes to the panel's max-content width [Spike3].
- **Background slot:** `.p-bg { position:absolute; inset:0; z-index:0; pointer-events:none; }`.
- `.act4 :focus-visible { outline-color:var(--leaf); }`. The site's pine outline nearly disappears on ink.

### 26.3 Entry, routing and activation

- **Chip click:** the browser follows the fragment (no `preventDefault`, R31 stays at 0). The router (R48) sees `#passions-<p>` with a known `p` and: keeps act three open at its rest state underneath (as R42's direct load did), sets `act4.hidden = false`, sets `#nerd.inert = true`, sets `act4.scrollTop` to the target subsection's `offsetTop`, and focuses that subsection's `h2` with `preventScroll:true`. With motion allowed, act four fades in with a WAAPI opacity animation, 0 to 1 over 300ms. Act three's rest screen and act four are both ink, so it reads as the background filling in on the same dark page.
- **Direct load** of `intro.html#passions-gamer`: same as above with acts two and three open at rest underneath and no fade.
- **Unknown** `#passions-foo`: opens act four at the top (techie).
- **Back** from any `#passions-*` returns to `#nerd`: act four hidden, every timer cleared, both videos paused and emptied (`removeAttribute('src'); load()`, which frees the decoders), `#nerd.inert = false`, focus back on the chip that was used (`techie` after a direct load).
- **No hash changes while scrolling** between subsections. No history spam.
- **Activation:** one `IntersectionObserver` with `root: #passions` and `threshold: [0, 0.4]`. A subsection is **near** when its ratio is above 0 and **active** at 0.4 or more. Near starts its asset loading (gamer clip 0, photos later). Active starts its background. Dropping below 0.4 stops it. At a boundary two subsections can be active at once; never three. The router sets `act4.scrollTop` **before** the observer starts observing, so a direct load of `#passions-photographer` never briefly sees techie or gamer as near (R52).
- **Hidden tab:** on `visibilitychange` to hidden, pause the videos and the shuffle; resume on visible if still active and not paused by the visitor.

### 26.4 Foreground panel and legibility (all three)

| Part | Spec |
|---|---|
| `.p-fore` | `position:relative; z-index:2; width:max-content; max-width:min(40rem, calc(100% - 2*var(--pad))); padding:24px 28px; background-color:rgba(22,36,28,.86); border:1px solid rgba(200,211,190,.25);` Under 560px wide: `padding:16px 18px`. |
| `.p-title` | Fraunces 600, `font-variation-settings:"opsz" 144`, lowercase as Nick wrote them, `font-size:clamp(28px,8vw,80px); line-height:1; margin:0; color:var(--card);` `#pt-title:focus, #pg-title:focus, #pp-title:focus { outline:none }` (programmatic focus targets). |
| `.p-copy` | EB Garamond (the site's body voice) 19px, `line-height:1.5; margin:.6em 0 0; color:var(--card);` |

**Contrast, worked out:** `--card` text on the scrim composited over pure white, the worst pixel any background can put behind it, is **9.89:1**. Over pure ink it is 15.32:1. AA needs 4.5:1. So the text never depends on what the background is doing. The motion toggle and the gamer disclaimer sit on the same `.86` scrim, so they get the same floor. (WCAG relative-luminance math on the token values, run during the spike [Spike3].)

Per-background calming, on top of the scrim: techie traces at 42% opacity (27.3); gamer clips under a 55% ink overlay (28.2); photographer needs none beyond the panel, since the photos are the point.

### 26.5 The motion toggle (WCAG 2.2.2)

The gamer clips and the photo shuffle move on their own for more than five seconds next to other content, so WCAG 2.2.2 requires a way to pause them [WCAG]. One button covers the whole layer.

- `#passions-motion`, a `<button type="button">`. Its text swaps between **"Pause motion"** and **"Play motion"**, so its name always says what pressing it will do (no `aria-pressed`).
- Style: `position:fixed; top:calc(12px + env(safe-area-inset-top)); right:var(--pad); z-index:4; min-height:44px; padding:8px 14px; font-family:"IBM Plex Mono",monospace; font-weight:500; font-size:14px; color:var(--card); background-color:rgba(22,36,28,.86); border:1px solid var(--rule); border-radius:0;`
- **Paused:** both videos `pause()` and the rotation stops on the current clip; the photo shuffle stops; a techie draw in progress is finished at once (`finish()` on its animations). **Play** resumes from where things stopped.
- Initial state: "Pause motion" (playing) when motion is allowed. "Play motion" (paused) under reduced motion (30.2).
- Session only. Nothing is stored.
- First in act four's tab order.

---

## 27. Techie: a circuit board that draws itself (card item 2)

### 27.1 Decision: inline SVG traces generated once in vanilla JS, drawn by CSS `stroke-dashoffset`

| Option | Tradeoff |
|---|---|
| Canvas, traces drawn each frame | Needs a `requestAnimationFrame` loop, device-pixel-ratio scaling and its own reduced-motion branch. More code and CPU for the same picture. Rejected. |
| A hand-made SVG tile, repeated | Small and static, but the repeat shows, and a tile can't draw as one sweep across the screen. Rejected. |
| **Generated inline SVG, each trace a `<path pathLength="1">` animated from `stroke-dashoffset:1` to `0`** | No library and no per-frame JS: CSS does the drawing. Reduced motion simply skips the animation and the paths are already complete. Generation took 12ms at 1440×900 [Spike3]. **Chosen.** |

### 27.2 The generator (exact, validated in the spike)

Runs once each time act four opens, and again on a resize that changes width or height by more than 80px (debounced 250ms). After a resize while the board is already drawn, the new board appears drawn.

```js
function rng(s){ return function(){ s|=0; s=s+0x6D2B79F5|0; var t=Math.imul(s^s>>>15,1|s);
  t=t+Math.imul(t^t>>>7,61|t)^t; return ((t^t>>>14)>>>0)/4294967296; }; }   // mulberry32
function buildCircuit(svg, W, H){
  var c = W < 560 ? 22 : 28, cols = Math.ceil(W/c)+1, rows = Math.ceil(H/c)+1, r = rng(7), occ = {},
      N = Math.max(36, Math.min(140, Math.round(W*H/12000))), made = 0, tries = 0, out = [],
      D = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]];
  svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
  while (made < N && tries++ < 4*N){
    var x = Math.floor(r()*cols), y = Math.floor(r()*rows); if (occ[x+','+y]) continue;
    var dir = Math.floor(r()*4)*2, pts = [[x,y]], segs = 3 + Math.floor(r()*5); occ[x+','+y] = 1;
    for (var s = 0; s < segs; s++){
      var len = 2 + Math.floor(r()*5), ok = 0;
      for (var k = 0; k < len; k++){ var nx = x+D[dir][0], ny = y+D[dir][1];
        if (nx<0 || ny<0 || nx>=cols || ny>=rows || occ[nx+','+ny]) break; x = nx; y = ny; occ[x+','+y] = 1; ok = 1; }
      if (!ok) break; pts.push([x,y]);
      dir = (dir + (r()<.5 ? 1 : 7)) % 8; if (r()<.5) dir = (dir + (r()<.5 ? 1 : 7)) % 8;   // 45° or 90° bend
    }
    if (pts.length < 2) continue; made++;
    var d0 = Math.round(pts[0][0]*c/W*2200), t = 900 + Math.round(r()*600), e = pts[pts.length-1];
    out.push('<path pathLength="1" d="M' + pts.map(function(p){ return p[0]*c + ',' + p[1]*c; }).join('L') +
             '" style="--d:' + d0 + 'ms;--t:' + t + 'ms"/>');
    out.push('<circle r="3.5" cx="' + pts[0][0]*c + '" cy="' + pts[0][1]*c + '" style="--d:' + d0 + 'ms"/>');
    out.push('<circle r="3.5" cx="' + e[0]*c + '" cy="' + e[1]*c + '" style="--d:' + (d0+t-120) + 'ms"/>');
  }
  svg.innerHTML = out.join('');
}
```

`W` is `#passions`'s `clientWidth`, `H` is `innerHeight`. The seed is fixed (7), so the same viewport always gets the same board, which makes tests repeatable. The spike ran this logic without the retry loop and placed 72 traces at 1440×900 and 24 at 390×844; the `4*N` retry loop above only adds traces.

### 27.3 Visual direction

| Part | Spec |
|---|---|
| Board | `--ink` (act three's "terminal mode" carries on) |
| Traces | `fill:none; stroke:var(--leaf); stroke-width:1.5; opacity:.42; stroke-linecap:round; stroke-linejoin:round;` (`stroke-width:1.25` under 560px) |
| Pads | `fill:var(--ink); stroke:var(--moss); stroke-width:1.5; opacity:.7;` radius 3.5, one at each end of every trace |
| Geometry | 28px grid (22px under 560px), straight runs with 45° and 90° bends, the classic PCB routing look |
| Density | about one trace per 12,000 px², 36 to 140 traces. Image check at 1440×900: "Balanced overall… the pattern remains secondary to the heading"; at 390×844: "its overall density is reasonable, not too sparse" [Spike3] |
| Crossings | Diagonal runs may cross. Accepted: it's a decorative board, not a working netlist |

### 27.4 The draw

```css
@media (prefers-reduced-motion:no-preference){
  .techie .circuit path   { stroke-dasharray:1; stroke-dashoffset:1; }
  .techie .circuit circle { opacity:0; }
  .techie.is-drawing .circuit path   { animation:trace var(--t) cubic-bezier(.35,.1,.25,1) var(--d) forwards; }
  .techie.is-drawing .circuit circle { animation:pad-in 240ms ease-out var(--d) forwards; }
  .techie.is-drawn .circuit path     { stroke-dashoffset:0; }
  .techie.is-drawn .circuit circle   { opacity:.7; }
}
@keyframes trace  { to { stroke-dashoffset:0; } }
@keyframes pad-in { to { opacity:.7; } }
```

- **Sweep left to right:** each trace's delay is `round(x0 / W × 2200)` ms from its start point's x, duration 900 to 1500ms. The start pad pops with its trace, the end pad as the trace arrives. The board is complete by about 3.94s.
- **Trigger:** the first time techie becomes active in this open of act four, add `is-drawing`. At 3,800ms after that, plus the last `animationend` or a 4,500ms safety timeout, swap to `is-drawn` (holds the finished board with no running animations).
- **Looping: none.** It draws once per open, then holds still. No moving "signal pulses" and no redraw when scrolling back up. Closing act four (Back) and opening it again redraws. Why: Nick described one event, the board drawing "itself across the screen", and a still board is calmer behind content. The whole draw is under five seconds, so WCAG 2.2.2 doesn't require a pause for it, though the toggle still finishes it.
- **Spike:** at 0.2s, 16 traces were part-drawn; at 2s, 39 were complete; at 4s, all 72. Image check of the 1s frame: "Yes, it looks like a left-to-right drawing reveal" [Spike3].

---

## 28. Gamer: a full-screen loop of gameplay (card item 3)

### 28.1 Decision: looping silent MP4 clips, not GIF files

Nick said "gifs", meaning short silent looping clips. The files will be H.264 MP4s played by `<video muted loop playsinline>`. They look the same as a GIF, they are typically several times smaller (web.dev's example: a 3.7 MB GIF became a 551 KB MP4 [web.dev-video]), and unlike a GIF they can be paused from JS, which the motion toggle and reduced motion both need. Flag C2.

One format only. H.264 MP4 plays in every browser this site targets. A WebM second copy would roughly double the repo weight for a small transfer saving.

### 28.2 Layout: one clip fills the screen, rotating through the six games

| Option | Tradeoff |
|---|---|
| A mosaic of all six at once | Six video decodes at the same time on a phone, all six clips' bytes before anything shows, and a busy wall behind the text. Rejected. |
| **One clip fills the screen and crossfades to the next game every 7 seconds** | Literally "a full screen loop". At most two decoders (only during the 800ms crossfade). Bytes arrive one clip at a time. **Chosen.** |

- **Two** `<video class="g-clip">` elements (A and B), never six: `position:absolute; inset:0; width:100%; height:100%; object-fit:cover; opacity:0; transition:opacity 800ms ease;` and `.g-clip.is-on { opacity:1; }`.
- **Order:** Nick's order, then repeat: borderlands, pokemon, fire-emblem, smash-bros, destiny, baldurs-gate. A full cycle is 42 seconds.
- **Swap:** 5.5s into a clip's turn, the idle element gets the next clip's `src` with `preload="auto"`. At 7s, the script calls `play()` on it, adds `is-on`, removes `is-on` from the current one, and pauses the old one 800ms later. If the next clip isn't ready (`readyState < 3`) at 7s, the current clip keeps playing and the swap retries on the next 7s tick. Never a black frame.
- **Under the clips,** `.g-posters` shows the current clip's poster as a `background-image` (`background-size:cover`), so a slow network shows a still, not black.
- **Dim:** `.g-dim { position:absolute; inset:0; z-index:1; background-color:rgba(22,36,28,.55); }` above the clips. It calms the panel area and cuts any brightness swing in the footage by more than half (28.7).
- **A clip that fails** (`error` event) is dropped from the rotation for the session. If every clip fails, the section shows plain ink plus the disclaimer.
- **Clip list in code:** `var CLIPS = [{slug:'borderlands', title:'…', credit:'…'}, …]` in the passions script, filled from `SOURCES.md` (28.6).

### 28.3 Files and the performance budget

| Item | Spec |
|---|---|
| Path | `assets/passions/gamer/<slug>.mp4` and `assets/passions/gamer/<slug>.jpg`. Slugs: `borderlands`, `pokemon`, `fire-emblem`, `smash-bros`, `destiny`, `baldurs-gate` |
| Clip | H.264 MP4, **no audio track**, at most 960px wide (16:9 preferred), at most 30 fps, 3 to 8 seconds, loops cleanly or close to it, `+faststart` |
| Clip size | **≤ 900 KB each** |
| Poster | the clip's first frame as JPEG, same size, **≤ 60 KB** |
| Total | **≤ 5,760 KB** for all twelve files |
| Manifest | `assets/passions/gamer/SOURCES.md` (28.6) |

Conversion. ffmpeg with libx264 is on this Mac at `~/.hermes/tools/ffmpeg-9.0.1-darwin-arm64/ffmpeg` (checked during the spike):

```
ffmpeg -i <source.gif|source.mp4> -ss <start> -t 6 -an \
  -vf "fps=24,scale='min(960,iw)':-2:flags=lanczos" \
  -c:v libx264 -preset slow -crf 28 -pix_fmt yuv420p -movflags +faststart <slug>.mp4
ffmpeg -i <slug>.mp4 -frames:v 1 -q:v 5 <slug>.jpg
```

Over budget: raise `-crf` to 30, then 32; then shorten `-t`; then scale to 854 wide. Prefer sources at least 640px wide; smaller ones look soft at full screen (the dim helps hide it).

**Lazy loading:** no `src` or `poster` in the markup. Nothing under `assets/passions/gamer/` is requested until the gamer subsection is near (26.3). Then poster 0 and clip 0 load; later clips load one at a time, 1.5s before their turn. Opening `#passions-techie` and staying there fetches zero gamer bytes. A visitor who watches the full 42s cycle downloads at most about 5.8 MB.

**Save-Data:** if `navigator.connection && navigator.connection.saveData` is true, no video loads. The posters rotate on the same 7s schedule instead (at most about 360 KB).

**Autoplay blocked** (iOS Low Power Mode can block even muted autoplay): the `play()` rejection is caught, and the poster rotation runs instead. No uncaught error.

### 28.4 Disclaimer and credits (exact copy and placement)

Nick: "We will need to include a disclaimer that I don't own any of the background art on that one." In his voice, first person, exact text:

> Game footage shown for fun. I don't own any of it. All rights belong to the games' developers and publishers.

Straight apostrophes (U+0027), matching the rest of the intro. Flag C3.

A second line names the clip on screen, updated at each swap: `Now showing: <Game title> · <Developer> / <Publisher>`, built from `CLIPS[i].title` and `CLIPS[i].credit`. Example of the format only: `Now showing: Borderlands 3 · Gearbox Software / 2K`. The build worker fills the real title and credit for each clip it sources.

- **Placement:** `.g-note` sits bottom-left of the gamer subsection, over the footage: `position:absolute; left:var(--pad); bottom:calc(16px + env(safe-area-inset-bottom)); z-index:3; max-width:calc(100% - 2*var(--pad)); margin:0; padding:6px 10px; font-family:"IBM Plex Mono",monospace; font-weight:400; font-size:13px; line-height:1.45; color:var(--card); background-color:rgba(22,36,28,.86);`. `.g-credit { display:block; color:var(--rule); }`. Contrast at worst: 9.89:1 for the disclaimer, 6.69:1 for the `--rule` credit line.
- **Always visible** whenever the gamer background is on screen, in every state: playing, paused, reduced motion, Save-Data, autoplay blocked, or a failed clip.
- **Screen readers:** the disclaimer is plain text in reading order, after the panel. The rotating credit line is `aria-hidden` (an `aria-live` line would talk every 7 seconds). Instead, `#g-credits` (visually hidden) lists all six once: "Clips from: <title> (<credit>), …".
- Only in the gamer subsection. Never on techie or photographer.

### 28.5 Sourcing guidance (the build worker sources; Nick delegated it)

Preference order, for every game:

1. **The publisher's or developer's own channel on GIPHY.** Search the game's name on giphy.com. GIPHY shows the relevant channels at the top of search results [GIPHY-search]. Prefer an official, verified channel's uploads. Take the MP4 rendition if the page offers one, otherwise the GIF, and convert it (28.3).
2. **Official media files:** the publisher's press or media kit B-roll, or a trailer file it offers for download, where its stated terms allow that use. Trim 3 to 8 seconds.
3. **Last resort:** other GIPHY or Tenor uploads of real gameplay. Mark the row "official: no" in `SOURCES.md` and list it in the handoff.

**Never:** download from YouTube, Twitch or TikTok (their terms forbid it); use clips with a streamer's face-cam, overlay, watermark or caption text (that adds a second rights holder); use anime, TV or movie footage instead of gameplay; use anything with gore, nudity, or a GIPHY rating above PG; commit anything that fails the flash check (28.7). One clip per game. If a game can't be sourced cleanly within budget, ship its poster only (a still in the rotation) and say so in `SOURCES.md` and the handoff. Never swap in a different game without saying so.

| Game (Nick's word) | What to look for | Search terms to start with | Credit (confirm from the source) | Watch out for |
|---|---|---|---|---|
| borderlands | Shooting or looting in a bright, cel-shaded world | "Borderlands 3 gameplay", "Borderlands gameplay" | Gearbox Software / 2K | Gore; rapid muzzle flashes |
| Pokemon series games | An in-game battle or an overworld walk from a mainline game | "Pokemon Scarlet Violet gameplay", "Pokemon battle gameplay" | Game Freak / Nintendo, The Pokémon Company | Results are flooded with anime clips. Those are not gameplay; reject them |
| Fire emblem | Units moving on the tactical map, or a battle animation | "Fire Emblem Engage gameplay", "Fire Emblem Three Houses battle" | Intelligent Systems / Nintendo | Story cutscenes with subtitles; prefer gameplay |
| Smash bros | A fight on a stage with several fighters | "Super Smash Bros Ultimate gameplay" | Bandai Namco Studios, Sora Ltd. / Nintendo | Final Smash and hit-spark flashes: run the flash check |
| Destiny | A first-person firefight or a raid moment | "Destiny 2 gameplay" | Bungie | Super abilities and explosions flash |
| Baldur's gate | Party exploration or turn-based combat | "Baldur's Gate 3 gameplay" | Larian Studios | The game has nudity and gore; pick tame shots |

### 28.6 `SOURCES.md`, the takedown-ready manifest

`assets/passions/gamer/SOURCES.md` has one row per clip with these columns: `slug | game title | source page URL | uploader or channel | official (yes/no) | retrieved (date) | rating | clip KB | poster KB | flash check`. Under the table, the removal recipe: "To take a clip down, delete `<slug>.mp4`, `<slug>.jpg`, its row here and its entry in `CLIPS` in `intro.html`. The rotation skips missing clips." This is what makes a takedown a five-minute job (Flag C1).

### 28.7 Photosensitivity with someone else's footage

Game footage can flash: explosions, hit sparks, supers. WCAG 2.3.1 allows at most three flashes in any second [WCAG]. Every clip must pass this check before it is committed. The build card saves it as `docs/tools/flashcheck.py` and records each result in `SOURCES.md`:

```python
# flashcheck.py <clip.mp4>: whole-frame luma flash heuristic (a WCAG 2.3.1 general-flash proxy)
import re, subprocess, sys, os
FF = os.path.expanduser("~/.hermes/tools/ffmpeg-9.0.1-darwin-arm64/ffmpeg")
out = subprocess.run([FF, "-hide_banner", "-i", sys.argv[1], "-vf",
      "signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=-", "-f", "null", "-"],
      capture_output=True, text=True).stdout
t, y = [], []
for line in out.splitlines():
    m = re.search(r"pts_time:([\d.]+)", line)
    if m: t.append(float(m.group(1)))
    m = re.search(r"YAVG=([\d.]+)", line)
    if m: y.append(float(m.group(1)))
# a transition = a luma swing of at least 10% of full range (25.5 of 255) from the last extreme
ext, d, trans = y[0], 0, []
for ti, yi in zip(t, y):
    s = 1 if yi > ext else -1
    if s == d or d == 0:
        if abs(yi - ext) >= 25.5 and d == 0: trans.append(ti); d = s; ext = yi
        elif s == d: ext = yi
    elif abs(yi - ext) >= 25.5: trans.append(ti); d = s; ext = yi
# a flash = a pair of opposing transitions; count them in any 1 s window
worst = max([sum(1 for x in trans if a <= x < a + 1.0) for a in trans] or [0]) // 2
print(f"frames={len(y)} transitions={len(trans)} max_flashes_per_second={worst} {'PASS' if worst <= 3 else 'FAIL'}")
```

Spike: a synthetic 6 Hz black/white strobe scored 6 flashes per second, FAIL; a calm test pattern scored 0, PASS [Spike3]. Its limit: it averages the whole frame, so a small flashing area may not trip it. Three more layers cover that: the 55% dim overlay shrinks any brightness swing, the curation rule ("watch out for" column) rejects strobe-heavy shots, and the motion toggle and reduced motion (30.2) stop the footage.

### 28.8 Copyright risk, in plain words (Flag C1)

Nick owns this decision and asked for it, so the build goes ahead. He should still see the risk clearly before this reaches `main`.

- **Short clips are still copies.** Six loops of game footage committed to a public GitHub repo and served on nickpings.com are reproductions and public displays of the publishers' copyrighted work. Length doesn't change that.
- **A disclaimer is not a license.** It shows good faith and credits the owners. It doesn't grant any right to use the footage.
- **Fair use is a defense, not a permission.** It is weighed case by case after someone objects. A decorative background on a professional portfolio is not very "transformative", which is the factor that matters most. Short length and no harm to game sales help, but nothing guarantees the outcome. (This is a product risk note, not legal advice.)
- **GIPHY doesn't launder the rights.** GIPHY's own terms say content found there is generally for personal, non-commercial use within its services, and forbid copying and displaying it elsewhere without permission [GIPHY-ToS]. A job-hunting portfolio is arguably commercial-adjacent.
- **The realistic worst case is a DMCA notice to GitHub, not a lawsuit.** GitHub's published process: it forwards the notice and gives about **one business day** to remove the content; if nothing changes, it **disables the whole repository** [GitHub-DMCA]. For a GitHub Pages site, that takes nickpings.com down until it's fixed.
- **Half the list is Nintendo-family IP** (Pokémon, Fire Emblem, Smash). Nintendo and The Pokémon Company are widely reported to enforce their IP actively (assumption, not checked against case records).

Built-in mitigations: prefer publisher-uploaded clips (28.5), credit every clip on screen (28.4), keep a manifest with a five-minute removal recipe (28.6), and degrade gracefully when clips are deleted (28.2).

**A lower-risk alternative for later (not in this build):** footage Nick records from his own play sessions. Many publishers publish fan-content or video policies that allow sharing your own gameplay captures for non-commercial use, which is better footing than clips copied from other uploaders. It's still the publishers' artwork, so check each policy first. Logged in BACKLOG.

---

## 29. Photographer: a messy collage that idly shuffles (card item 4)

### 29.1 Status: the mechanism now, the photos later

**The real photos are BLOCKED on Nick** ("I'll send photos in a later message"). Build card t_24e05978 builds the whole mechanism with **placeholder frames that look like placeholders** and says so in its handoff. A follow-up card adds the photos (R61). Nothing on this card may look finished: **no stock or royalty-free stand-in photos.** The card allowed stand-ins as an option; I chose solid frames because a stand-in photo can be mistaken for Nick's own work, which is exactly the fake finish the card warns against.

### 29.2 Layout: scattered polaroids on a jittered grid

| Option | Tradeoff |
|---|---|
| A neat grid | Not "messy". Kept only as the reduced-motion state (30.2). |
| Fully random positions | Clumps and leaves holes. The spike's first version did exactly that: "top-heavy and locally clumped", with "substantial open areas" [Spike3]. Rejected. |
| **A jittered grid: one frame per cell, nudged up to ±20% of the cell, tilted up to ±8°, overlapping its neighbors** | Reads as a pile on a table but always covers the screen. Spike coverage 0.90 to 0.97 [Spike3]. **Chosen.** |

| Viewport | Grid | Frames |
|---|---|---|
| ≥ 900px wide | 5 × 3 | 15 |
| 560 to 899px | 4 × 3 | 12 |
| < 560px | 3 × 4 | 12 |
| `max-height:500px` (landscape phone) | 5 × 2 | 10 |

- Cell = subsection width ÷ columns by `innerHeight` ÷ rows. Frame width = `min(cellW × 1.1, cellH × 0.92)`. Frame shape 4:5, border included.
- Frame look (a polaroid with a deeper bottom lip): `.ph { position:absolute; left:0; top:0; width:var(--w); aspect-ratio:4/5; padding:8px 8px 28px; background-color:var(--card); box-shadow:0 6px 18px rgba(0,0,0,.35); transition:transform 1200ms cubic-bezier(.3,.7,.2,1); }`. Position and tilt are one inline `transform: translate(x,y) rotate(a)`.
- Jitter and tilt come from `rng(11)` (the same mulberry32 as 27.2), so a reload at the same size gives the same first layout.

### 29.3 The idle shuffle

- While photographer is active, motion is allowed and the visitor hasn't paused: **every 3,200ms, pick two frames at random and swap their cells.** Each gets a fresh nudge and tilt, both are raised to the top (`z-index` counter), and they glide to their new spots over 1,200ms (transform only).
- One swap at a time keeps it idle, not busy.
- Swapping cells, instead of re-randomizing positions, keeps every cell covered, so the collage never drifts into a clump. Spike, after 20, 40 and 60 swaps: coverage 0.94, 0.94, 0.90 at 1440×900 and 0.93, 0.91, 0.95 at 390×844 [Spike3].
- Stops when inactive, paused or reduced motion. Resumes from the current layout.

### 29.4 The placeholder scaffold (what t_24e05978 ships)

- In the passions script: `var PHOTOS = [];  // TODO(photos): fill from assets/passions/photos/ when Nick sends photos (PRD R61)`.
- While `PHOTOS` is empty, each frame's picture area is a solid fill cycling through existing tokens: `--pine`, `--moss`, `--pill-blue`, `--rec`, `--ink-soft`, `--muted`. Each frame's bottom lip has a label in IBM Plex Mono 11px, `--ink-soft`: `photo N · pending`. Each frame has `data-placeholder="true"`.
- The panel shows `.ph-pending`: "Placeholder frames. Nick's photos are on the way." (IBM Plex Mono 13px, `--rule`, 6.69:1 at worst on the scrim).
- The HTML comment `<!-- TODO(photos): … -->` sits in the subsection (26.2).
- The spike's image check: "Yes, very obvious" that these are placeholders [Spike3].

### 29.5 The real photos (follow-up card, BLOCKED on Nick)

- Files: `assets/passions/photos/01.jpg`, `02.jpg`, … in the order Nick wants them.
- Processing, on this Mac: iPhone HEIC first becomes JPEG with `sips -s format jpeg in.HEIC --out tmp.jpg`. Then
  `ffmpeg -i tmp.jpg -vf "scale='if(gt(iw,ih),min(1000,iw),-2)':'if(gt(iw,ih),-2,min(1000,ih))'" -q:v 4 -map_metadata -1 NN.jpg`
  resizes to a 1000px long edge and **drops all metadata, including GPS location**. Each file ≤ 160 KB (raise `-q:v` to 6 if over), total ≤ 2,400 KB.
- Markup: `<img src="assets/passions/photos/NN.jpg" alt="" decoding="async">` with `width:100%; height:100%; object-fit:cover;`, `src` set when photographer becomes near (26.3). `alt=""` because they're a background behind the panel. A captioned gallery is a separate follow-up.
- Fewer photos than frames: repeat them in order. More: the first N in manifest order.
- Remove every placeholder marker: `data-placeholder`, the `photo N · pending` labels, `.ph-pending` and both `TODO(photos)` comments.

---

## 30. Responsive and accessibility (card items 5 and 6)

### 30.1 Responsive

| Concern | Desktop (≥ 900px) | Mobile (< 560px) | Short screens (`max-height:500px`) |
|---|---|---|---|
| Subsection | full viewport height, background full-bleed | same | same |
| Panel | up to 40rem wide, padding 24/28 | full width minus `--pad`, padding 16/18 | same as width class; title floor 28px |
| Title | 80px | `8vw` (31px at 390, 28px floor at 320) | per width |
| Techie grid | 28px pitch, up to 140 traces | 22px pitch, stroke 1.25 | per width |
| Gamer clip | `object-fit:cover`, crops the 16:9 sides on tall screens | same (a portrait phone shows the middle third) | same |
| Disclaimer | bottom-left, 13px, wraps under `--pad` width | same, wraps to 3 to 4 lines | same; must not overlap the panel (R58) |
| Photo grid | 5 × 3 | 3 × 4 | 5 × 2 |
| Motion toggle | top-right, 44px tall | same, plus safe-area inset | same |
| Scrollbar | hidden | hidden | hidden |

`svh` only, never `dvh` (section 5). Touch scrolling of act four is native momentum scrolling with no gesture code.

### 30.2 Reduced motion

| Part | With `prefers-reduced-motion: reduce` |
|---|---|
| Act four entry | No fade. Appears in one cut. |
| Techie | No draw. The board is complete from the first frame: the dash rules only exist inside the motion-allowed query, and the page's global rule (`animation:none !important`) stops CSS animations anyway. |
| Gamer | **No autoplay at all.** `.g-posters` shows the six posters as a still grid (3 × 2 at 560px and wider, 2 × 3 below) under the same dim, with the disclaimer. The toggle reads "Play motion". Pressing it is the visitor's explicit opt-in and starts the one-clip rotation. Judgment call (the card asked): a GIF can't be paused from CSS, but a `<video>` can, so reduced motion gets stills instead of "loops anyway". |
| Photographer | No shuffle. Frames sit in a neat grid: no nudge, no tilt, centered in their cells, width `min(cellW, cellH × 0.8) × 0.9` so none overlap. |
| Live change | A `matchMedia` change listener applies the switch without a reload: playing clips pause and the posters show; the shuffle stops and the frames settle into the neat grid. |

### 30.3 Screen readers and keyboard

- Every background is inside `.p-bg[aria-hidden="true"]`. The SVG has `focusable="false"`. The videos have no `controls`, no `tabindex` and `disablepictureinpicture`. Nothing in a background is focusable or announced.
- Act four is a region named "Passions" with three level-2 headings: techie, gamer, photographer. On open, focus goes to the target subsection's heading.
- Tab order inside act four: the motion toggle, and nothing else (the panels have no links yet). The skip link stays reachable above everything.
- The disclaimer is read in order after the gamer panel. The credits list is read once (28.4).
- While act four is open, `main` and `#nerd` are `inert`. Back returns focus to the chip that opened it.

---

## 31. Requirements, deployment, flags, feasibility, non-goals

All requirements use the section 7 harness (local `python3 -m http.server 8000`, Chromium over CDP, the same desktop, mobile and reduced-motion emulation). Definitions: **"Open at X"** means a direct load of `http://localhost:8000/intro.html#passions-X`, then wait 800ms. **`L`** is `document.getElementById('passions')`. **"Scroll to Y"** means `L.scrollTop = document.getElementById('passions-Y').offsetTop`, then wait 600ms. **"Assets"** means `performance.getEntriesByType('resource').filter(e => /assets\/passions\//.test(e.name))`. Build and deployment for every requirement: **not Docker**, by the same justified exception as sections 8 and 24.1 (a static GitHub Pages site with nothing to containerize; production deploy is a push to `main`, which stays forbidden).

### R50. The chips open one `#passions` page with three stacked subsections; no new route, file or layer per passion.
- **Source:** [Nick-C] "Those passions should all be contained on one page."; [Card4] item 1; sections 19.3, 26.1 to 26.3.
- **Acceptance:** load `intro.html#nerd`, set q = 1 (R38 harness), set `window.__stay = 1`, click the `gamer` chip; within 1000ms: `location.hash === "#passions-gamer"`, `window.__stay === 1`, `L.hidden === false`, `document.querySelectorAll('section.act4').length === 1`, `L.querySelectorAll(':scope > section.passion')` has 3 elements with ids `passions-techie`, `passions-gamer`, `passions-photographer` in that order, `Math.abs(L.scrollTop - document.getElementById('passions-gamer').offsetTop) <= 2`, `document.activeElement.id === "pg-title"`, `document.getElementById('nerd').inert === true`, `getComputedStyle(L).zIndex === "17"`, `getComputedStyle(L).transform === "none"`, and every subsection's `offsetHeight >= innerHeight`. `grep -c 'id="nerd-soon"' intro.html` = 0; `grep -c "Still nerding out on it" intro.html` = 0; no chip has `aria-describedby`; `grep -oE 'href="#passions-[a-z]+"' intro.html | sort -u` returns exactly the three R42 hrefs; `git ls-files '*.html'` lists the same files as at 560f493.
- **Edge cases:** `#passions-foo` opens act four with `L.scrollTop === 0`; `history.back()` from `#passions-gamer` gives `location.hash === "#nerd"`, `L.hidden === true`, focus on the `gamer` chip, and no `<video>` in `L` with a `src` attribute; reloading on `#passions-photographer` reopens there; a Cmd-click on a chip opens a new tab in the direct-load state; zero `Runtime.exceptionThrown`.
- **Resources:** `intro.html` (markup, main router branch, passions script).

### R51. Every passion's heading and copy stay readable over its background on a shared scrim, at every size.
- **Source:** [Card4] item 5 "foreground text/chips must stay readable"; section 26.4.
- **Acceptance:** for each subsection: `.p-fore` computed `backgroundColor === "rgba(22, 36, 28, 0.86)"`; `.p-title` and `.p-copy` `color === "rgb(248, 250, 244)"`; `.p-title` `fontFamily` starts with `"Fraunces"`; `.passion` computed `gridTemplateColumns` is a single track (not `"none"`). At 1440×900, 390×844 and 320×568 after "Scroll to" each subsection: `.p-title.scrollWidth <= .p-title.clientWidth + 1`; the `.p-fore` rect has `left >= 0` and `right <= innerWidth`. The contrast floor is fixed by these values (9.89:1 worst case, section 26.4), so the computed-value checks are the test.
- **Edge cases:** a missing Fraunces falls back to Georgia and still fits at 320; the panel never takes the background's `pointer-events:none`; long placeholder copy wraps inside the panel.
- **Resources:** `intro.html` CSS.

### R52. Only on-screen backgrounds run, and nothing loads before its subsection is near.
- **Source:** [Card4] item 3 "lazy-load/defer-until-visible"; section 26.3, 28.3.
- **Acceptance:** motion allowed. Open at techie, wait 3000ms: Assets has 0 entries. Scroll to gamer, wait 1500ms: Assets includes `gamer/borderlands.mp4` and `gamer/borderlands.jpg` and no other `.mp4`; exactly one `L` video has `paused === false`. Scroll to photographer, wait 1000ms: every `L` video has `paused === true`. Scroll to techie, then record every `.ph` inline `transform`, wait 4000ms: unchanged. Open at photographer, wait 3000ms: Assets has no `gamer/` entry. `grep -cE "https?://[^\"' ]*(giphy|tenor|youtube|ytimg|twimg)" intro.html` = 0, and every media URL that act four requests is relative and starts with `assets/passions/`.
- **Edge cases:** a fast flick past gamer may start loading clip 0 but must leave every video paused within 1000ms; `document.visibilityState` hidden (CDP `Emulation.setFocusEmulationEnabled` plus a `visibilitychange` dispatch, or a background tab) pauses videos and the shuffle; at no time are more than two videos playing.
- **Resources:** passions script (IntersectionObserver, visibility handler).

### R53. One "Pause motion" control stops every self-moving background in act four.
- **Source:** [WCAG] 2.2.2; section 26.5.
- **Acceptance:** motion allowed. Open at gamer, wait 1500ms: `#passions-motion` is a `BUTTON` with `type="button"`, `textContent === "Pause motion"`, computed `position === "fixed"`, height ≥ 44px, and `document.elementFromPoint` at its center returns it at each of the three subsections. Click it: within 300ms every `L` video is paused and its text is `"Play motion"`. Scroll to photographer, record the `.ph` transforms, wait 4000ms: unchanged. Click again: within 4000ms at least one `.ph` transform changes and the text is `"Pause motion"`. Open at techie and click the toggle at t ≈ 800ms: within 200ms every `#circuit path` has `parseFloat(getComputedStyle(p).strokeDashoffset) === 0`. After the first Tab inside act four, `document.activeElement.id === "passions-motion"`.
- **Edge cases:** paused stays paused while scrolling between subsections; Enter and Space both toggle; reload resets to playing and `localStorage.length` and `document.cookie` are unchanged; the focus outline shows on `:focus-visible` (`outlineStyle !== "none"`).
- **Resources:** `intro.html` markup and passions script.

### R54. The techie background is a generated SVG circuit board: traces on a grid with 45° and 90° bends, a pad at each end, in leaf and moss on ink.
- **Source:** [Nick-D] "a circuit board pattern/design"; [Card4] item 2; sections 27.1 to 27.3.
- **Acceptance:** open at techie: `#circuit` is an inline `svg` inside `.p-bg[aria-hidden="true"]` with `viewBox === "0 0 " + L.clientWidth + " " + innerHeight`; `#circuit path` count is between 60 and 140 at 1440×900 and between 24 and 60 at 390×844; `#circuit circle` count is exactly twice the path count; every path has `pathLength="1"` and a `d` of the form `M x,y L x,y …` where every segment's `dx`, `dy` are both multiples of the grid pitch (28, or 22 under 560px) and are either axis-aligned or `|dx| === |dy|`; computed path `stroke === "rgb(207, 226, 166)"`, `opacity === "0.42"`, `strokeWidth === "1.5px"` (1.25px at 390); loading the same viewport twice gives an identical `#circuit` `innerHTML`; `performance.measure` around generation (`circuit-gen`) is under 50ms. `grep -cE "<canvas|<script[^>]+src=" intro.html` = 0.
- **Edge cases:** resizing from 1440×900 to 390×844 regenerates (`viewBox` changes, pitch becomes 22); 320×568 still gets at least 20 traces; a resize after the draw shows the new board complete, not undrawn.
- **Resources:** passions script (`buildCircuit`), `intro.html` CSS.

### R55. The board draws itself once, left to right, finishing in under 4 seconds, then holds still.
- **Source:** [Nick-D] "draw itself across the screen"; section 27.4.
- **Acceptance:** motion allowed, open at techie at t = 0 (read `strokeDashoffset` with `parseFloat`): at t ≈ 400ms at least 5 paths have an offset strictly between 0 and 1, and the mean start x of paths at offset 1 is greater than the mean start x of paths below 1 (left goes first); at t ≈ 4600ms every path's offset is 0, `#passions-techie` has class `is-drawn` and not `is-drawing`, and `document.getAnimations().filter(a => a.animationName === "trace").length === 0`. Scroll to gamer and back: no `trace` animation starts again. Back, then click the `techie` chip again: the draw runs again (`trace` animations exist at t ≈ 400ms).
- **Edge cases:** opening at gamer and scrolling up to techie starts the draw then, not at open; reduced motion is R62; the motion toggle finishes it (R53).
- **Resources:** `intro.html` CSS (`trace`, `pad-in`), passions script.

### R56. Six gameplay clips, one per game Nick listed, are sourced, documented and within budget.
- **Source:** [Nick-D] "gifs of gameplay from some of my favorite games (sourced from the web)… borderlands, Pokemon series games, Fire emblem, Smash bros, Destiny, Baldur's gate. You source them."; sections 28.3, 28.5 to 28.7.
- **Acceptance:** `assets/passions/gamer/` contains `borderlands`, `pokemon`, `fire-emblem`, `smash-bros`, `destiny`, `baldurs-gate` as both `.mp4` and `.jpg` (or `.jpg` only for a game documented as poster-only in `SOURCES.md`), plus `SOURCES.md`. For each `.mp4`: `ffmpeg -i <f> 2>&1` shows `Video: h264` and no `Audio:` line, a width ≤ 960 and a duration from 3 to 8 seconds; `stat -f%z` ≤ 921600. For each `.jpg`: `stat -f%z` ≤ 61440. `du -ck assets/passions/gamer/*.mp4 assets/passions/gamer/*.jpg | tail -1` ≤ 5760. `python3 docs/tools/flashcheck.py <f>` prints `PASS` for every `.mp4`. `SOURCES.md` has 6 data rows, each with a URL starting `https://`, an official `yes` or `no`, a retrieved date and a flash check of `PASS`, and contains the removal recipe line from 28.6. The build handoff lists every `official: no` row and every poster-only game.
- **Edge cases:** no file under `assets/` is over 1,000 KB (`find assets -size +1000k` prints nothing); no clip shows a streamer face-cam, watermark or anime footage (checked by an image look at each poster, noted in the handoff); a clip that fails the flash check is not committed.
- **Resources:** `assets/passions/gamer/`, `docs/tools/flashcheck.py`, web sourcing.

### R57. Gamer plays one full-screen clip at a time and crossfades to the next game every 7 seconds, in Nick's order.
- **Source:** [Nick-D] "a full screen loop of gifs of gameplay"; sections 28.1 to 28.3.
- **Acceptance:** motion allowed, 1440×900, open at gamer: within 1500ms exactly one `.g-clip.is-on`, it is playing, its `currentSrc` ends `borderlands.mp4`, its rect covers the subsection (width ≥ `innerWidth`, height ≥ `innerHeight`), and `objectFit === "cover"`, `muted === true`, `loop === true`, `playsInline === true`; `L.querySelectorAll('video').length === 2`; `.g-dim` `backgroundColor === "rgba(22, 36, 28, 0.55)"`. At t ≈ 8.5s the playing `is-on` clip is `pokemon.mp4` and `#g-credit` contains `CLIPS[1].title`. Sampling every 500ms for 45s: the `is-on` sequence follows `borderlands, pokemon, fire-emblem, smash-bros, destiny, baldurs-gate, borderlands`, and no sample has more than two playing videos. **Save-Data:** with `Page.addScriptToEvaluateOnNewDocument` defining `navigator.connection` as `{saveData:true}`, open at gamer and wait 9s: Assets has no `.mp4` and `#g-posters`'s `backgroundImage` has changed at least once. **Autoplay blocked:** with `HTMLMediaElement.prototype.play` stubbed to return `Promise.reject(new DOMException('', 'NotAllowedError'))`, open at gamer: a poster is visible and there are zero `Runtime.exceptionThrown`.
- **Edge cases:** a missing clip (served copy with one `.mp4` renamed) is skipped and the rotation continues with zero exceptions; a slow clip (CDP network throttling to "Slow 3G") never shows a black frame (the poster is under it); Back mid-crossfade leaves no playing video.
- **Resources:** passions script (`CLIPS`, rotation), `intro.html` CSS.

### R58. The gamer background always shows the exact disclaimer and names the game on screen.
- **Source:** [Nick-D] "We will need to include a disclaimer that I don't own any of the background art on that one."; [Card4] item 3; section 28.4.
- **Acceptance:** `#g-note`'s first text node is exactly `Game footage shown for fun. I don't own any of it. All rights belong to the games' developers and publishers.` (U+0027 apostrophes); `#g-note` is inside `#passions-gamer`, not inside `.p-bg` and has no `aria-hidden` ancestor; computed `fontFamily` starts with `"IBM Plex Mono"`, `fontSize === "13px"`, `color === "rgb(248, 250, 244)"`, `backgroundColor === "rgba(22, 36, 28, 0.86)"`. After "Scroll to gamer" at 1440×900, 768×1024, 390×844, 320×568 and 844×390: its rect is inside the viewport, does not intersect the `.p-fore` rect, and `elementFromPoint` at its center returns `#g-note` or a descendant, in each of these states: playing, paused (R53), reduced motion (R62), Save-Data (R57). `#g-credit` text starts with `Now showing: ` and has `aria-hidden="true"`; CDP `Accessibility.getFullAXTree` has a text node containing `I don't own any of it` and one containing all six `CLIPS` titles. `document.querySelectorAll('#passions-techie .g-note, #passions-photographer .g-note').length === 0`.
- **Edge cases:** no `aria-live` on `#g-note` or anything inside it; the disclaimer still shows when every clip has failed; the text wraps, never truncates (no `text-overflow`, no `overflow:hidden` on it).
- **Resources:** `intro.html` markup and CSS, passions script.

### R59. Photographer ships as a visibly marked placeholder scaffold until Nick's photos arrive.
- **Source:** [Nick-D] "I will provide photos… I'll send photos in a later message"; [Card4] "clearly mark it incomplete pending real photos"; section 29.4.
- **Acceptance:** `grep -c "TODO(photos)" intro.html` ≥ 2; the passions script contains `var PHOTOS = [];`. Open at photographer: 15 `.ph` frames at 1440×900, 12 at 390×844, 10 at 844×390; every frame has `data-placeholder="true"` and a label matching `/^photo \d+ · pending$/`; `#ph-box img` count is 0; `.ph-pending` is visible with text exactly `Placeholder frames. Nick's photos are on the way.`; each frame's fill color is one of the six token colors (`rgb(47, 91, 68)`, `rgb(126, 156, 96)`, `rgb(46, 74, 107)`, `rgb(176, 112, 58)`, `rgb(59, 82, 69)`, `rgb(110, 130, 112)`). `git ls-files assets/passions/photos` prints nothing. Assets has no `photos/` entry.
- **Edge cases:** no stock or royalty-free image is committed anywhere (`git diff --name-only 560f493..HEAD -- '*.jpg' '*.jpeg' '*.png' '*.webp'` lists only `assets/passions/gamer/*.jpg`); the build handoff says in words that photographer is a placeholder pending Nick's photos.
- **Resources:** `intro.html`, passions script.

### R60. The frames form a messy, overlapping collage that covers the screen and idly swaps two frames every 3.2 seconds.
- **Source:** [Nick-D] "a messy collage that idly shuffles around"; sections 29.2, 29.3.
- **Acceptance:** motion allowed, open at photographer: at least 80% of `.ph` frames have a nonzero rotation and every rotation is within ±8° (parsed from the computed matrix); every `.ph` has computed `transitionDuration === "1.2s"` and `transitionProperty === "transform"`. Coverage test (temporarily set `pointer-events:auto` on `#ph-box` and every `.ph`; sample a 12 × 8 grid of points across the subsection with `document.elementsFromPoint`): at least 0.85 of points hit a frame at t = 0, t = 10s and t = 30s, at 1440×900 and 390×844. Between t = 0 and t = 10s, from 4 to 8 frames change transform (about three swaps). `L.scrollWidth <= L.clientWidth` throughout. A reload at the same size gives the same initial transforms.
- **Edge cases:** the shuffle stops when the subsection is inactive, paused or the tab is hidden (R52, R53); a resize across 560 or 900 wide re-lays the grid with the new frame count; frames never cover the motion toggle or the panel (both have a higher `z-index`).
- **Resources:** passions script (collage, shuffle), `intro.html` CSS.

### R61. BLOCKED on Nick's photos (follow-up card, not t_24e05978): real photos replace the placeholders, resized and stripped of location data.
- **Source:** [Nick-D] "I will provide photos"; section 29.5.
- **Acceptance (once photos exist):** each `assets/passions/photos/NN.jpg` has a long edge ≤ 1000 (`sips -g pixelWidth -g pixelHeight`), size ≤ 163840 bytes, and `LC_ALL=C grep -c Exif <f>` = 0 (EXIF, which carries GPS, starts with the bytes `Exif`); `du -ck assets/passions/photos/*.jpg | tail -1` ≤ 2400; `PHOTOS` lists every file; open at photographer: every frame contains an `img` with `alt=""`, `decoding="async"`, computed `objectFit === "cover"` and `naturalWidth > 0`; `grep -cE "TODO\(photos\)|data-placeholder|ph-pending|· pending" intro.html` = 0; Assets has no `photos/` entry before photographer is near; R60's coverage test still passes.
- **Edge cases:** HEIC input converts via `sips` first; portrait and landscape both crop cleanly into the 4:5 frame; a corrupt file leaves its frame showing the card color with zero exceptions; fewer photos than frames repeat in order.
- **Resources:** `assets/passions/photos/`, passions script. Blocked until Nick sends photos.

### R62. Reduced motion: the board appears complete, the gamer clips don't autoplay, and the photos sit still in a neat grid.
- **Source:** [Card4] item 5; [WCAG] 2.2.2 and 2.3.1; section 30.2.
- **Acceptance:** with `prefers-reduced-motion: reduce` emulated. Open at techie: within 100ms every `#circuit path` offset is 0 and every `#circuit circle` opacity is `"0.7"`; `L.getAnimations({subtree:true})` contains no `CSSAnimation`; `getComputedStyle(L).opacity === "1"` at 50ms (no fade). Open at gamer and wait 5000ms: Assets has no `.mp4`; `#g-posters` shows 6 tiles (3 columns at 1440×900, 2 at 390×844); `.g-dim` present; `#passions-motion` text is `"Play motion"`; the disclaimer passes R58. Click the toggle: within 1500ms one video is playing. Open at photographer: every `.ph` rotation is 0, no two `.ph` rects overlap, and no `.ph` transform changes over 8000ms. Switching emulation from no-preference to reduce while gamer is playing pauses every video within 500ms and shows the posters.
- **Edge cases:** the skip link, Back and the R45 checks for act three still pass; no WAAPI animation in act four animates anything but `opacity`.
- **Resources:** `intro.html` CSS, passions script.

### R63. Screen readers and keyboard users get three clean headings, the disclaimer and the toggle, and nothing from the backgrounds.
- **Source:** [Card4] item 5; section 30.3.
- **Acceptance:** open at techie; CDP `Accessibility.getFullAXTree` has a `region` named `Passions`, three `heading` level 2 nodes named `techie`, `gamer`, `photographer`, a `button` named `Pause motion`, the disclaimer text, and no `video`, `image`, `graphics-document` or `svg`-role nodes from inside any `.p-bg`. `document.activeElement.id === "pt-title"`. Tab once: focus on `#passions-motion`. Shift+Tab repeatedly reaches the skip link, which `elementFromPoint` confirms is on top. While act four is open, `document.querySelector('main').inert === true` and `document.getElementById('nerd').inert === true`. After Back, focus is on the chip that opened act four.
- **Edge cases:** no element inside `.p-bg` is focusable (`L.querySelectorAll('.p-bg [tabindex], .p-bg a, .p-bg button, .p-bg video[controls]').length === 0`); VoiceOver reads the headings without "dimmed".
- **Resources:** `intro.html`.

### R64. All three backgrounds work at desktop, tablet, phone and landscape-phone sizes with no horizontal overflow.
- **Source:** [Card4] item 6; [Nick] original brief "desktop and mobile friendly"; section 30.1.
- **Acceptance:** at 1440×900, 768×1024, 390×844, 320×568 and 844×390, after "Scroll to" each subsection: `document.documentElement.scrollWidth <= innerWidth`, `L.scrollWidth <= L.clientWidth`, the subsection's `offsetHeight >= innerHeight`, the panel and the motion toggle are inside the viewport and don't intersect, and (gamer) the disclaimer is inside the viewport. `grep -c "dvh" intro.html` = 0. `env(safe-area-inset-bottom)` appears in the `.g-note` rule and `env(safe-area-inset-top)` in the `.p-motion` rule.
- **Edge cases:** rotating a phone mid-act regenerates the board and re-lays the collage; hover-only styles stay under `@media (hover:hover)`; iOS URL-bar changes don't resize the subsections (`svh`).
- **Resources:** `intro.html` CSS, passions script.

### R65. Palette, fonts, script budget and file footprint hold, and nothing earlier regresses.
- **Source:** R31, R49; section 25.3.
- **Acceptance:** the R31 hex grep returns the same set as at 560f493 (**no new hex**); the Google Fonts URL is unchanged; `grep -c "<script" intro.html` = 3 and `grep -cE "<script[^>]+src=" intro.html` = 0; the main inline script is under 345 lines and `<script id="passions-js">` is under 280 lines; `grep -ci "preventDefault" intro.html` = 0; `git diff --name-only 560f493..HEAD` lists only `intro.html`, `BACKLOG.md`, files under `docs/` and files under `assets/passions/`; `du -sk assets/passions` ≤ 5800 before photos. All acceptance checks of R1 to R41 and R44 to R49 pass again with the 25.3 amendments (R42 is replaced by R50; R43's file rule is amended).
- **Edge cases:** no new font, CSS or JS files; no third-party code or hotlinked media; act three's glitch, timings, Back behavior and reduced-motion layout are unchanged.
- **Resources:** `intro.html`; `index.html` (read-only).

### 31.1 Deployment and build

Unchanged from sections 8, 18.1 and 24.1: **not Docker**, by the same justified exception (static GitHub Pages site, nothing to containerize, production deploy is a push to `main`, which stays forbidden). Local preview `python3 -m http.server 8000` from the repo root on `feature/intro-experience`. Demo URLs: `http://localhost:8000/intro.html#passions-techie`, `#passions-gamer`, `#passions-photographer`, or `#nerd`, then scroll and tap a chip. No build step. Media conversion uses the ffmpeg already on this Mac (28.3); nothing new to install. The build card may push `feature/intro-experience` to origin.

### 31.2 Flags for Nick (addendum 3)

1. **C1, copyright risk on the gamer clips (the big one).** Short loops of game footage on a public site are copies of the publishers' work. Your disclaimer shows good faith but doesn't grant rights, and fair use is a case-by-case defense, not a permission. GIPHY's own terms limit its content to personal, non-commercial use. The realistic worst case is a DMCA notice to GitHub, which gives about one business day to remove the clips before it disables the whole repo, taking nickpings.com down. Half your list is Nintendo-family IP. The build goes ahead as you asked, with official-channel sourcing preferred, on-screen credits and a five-minute removal recipe. Worth deciding before this merges to `main`. A lower-risk path later: clips you record yourself (section 28.8).
2. **C2, "gifs" will be silent looping videos.** They look the same, they're several times smaller, and they can be paused, which accessibility needs.
3. **C3, disclaimer wording.** "Game footage shown for fun. I don't own any of it. All rights belong to the games' developers and publishers." Plus a "Now showing" credit line. Change freely.
4. **C4, placeholder copy.** Each passion panel says "More on this soon." until you write what you want there. The photographer collage shows labeled color frames until your photos arrive.
5. **C5, what to send for photos.** 10 to 15 photos fills the collage (15 show on a desktop). Any mix of portrait and landscape. Send originals: they'll be resized and stripped of location data before they go public.
6. **C6, a "Pause motion" button.** Act four has one, top right. Accessibility rules require a way to stop motion that runs more than five seconds. Reduced-motion visitors start paused.
7. **C7, weight.** About 5.8 MB of clips added to the repo, loaded only when someone scrolls to gamer, one clip at a time. About 2.4 MB more once photos land. No cost, no new services.
8. **C8, real-device check.** iPhone Low Power Mode can block autoplay (the posters show instead), and iOS Safari's handling of inline video in a scrolling overlay is worth two minutes on your phone. Emulation can't prove either.

No new cost, services, infrastructure or recurring manual steps.

### 31.3 Feasibility (spike method) and risks

I ran a throwaway spike: one HTML page with the `#passions` layer, three subsections, the circuit generator and draw, an A/B video rotation with test clips, and the jittered-grid collage with swap shuffle. I served it locally on port 8012 and measured it in headless Chromium 145 over CDP at 1440×900, 390×844 and 320×568, with image checks of five screenshots. I also tested ffmpeg encoding and the flash check on synthetic clips. It lived in my scratch folder and is not in the repo. Every value it validated is written into sections 26 to 29.

| # | Given / When / Then | Verdict | Evidence |
|---|---|---|---|
| F16 | Given the 27.2 generator, when run at 1440×900, then it builds a board fast and CSS draws it left to right in under 4s. | VALIDATED | Generation 12ms; 72 traces and 144 pads; complete traces at 0.2s / 2s / 4s: 0 / 39 / 72; image check of the 1s frame: "a left-to-right drawing reveal". |
| F17 | Given the board behind the scrim panel, when viewed at 1440×900 and 390×844, then it reads as a circuit board and the text stays readable. | VALIDATED | Image check: "Yes, clearly… stylized PCB traces with pads", density "balanced", heading "excellent readability". Found the mobile panel overflow, fixed with `grid-template-columns:minmax(0,1fr)` (26.2) and rechecked: panel inside 390 and 320. |
| F18 | Given two muted, looping, inline videos in a fixed scrolling layer with an IntersectionObserver rooted on it, when gamer scrolls in and out, then one clip plays, crossfades at 6 to 7s, and both pause off-screen. | VALIDATED (Chromium). PARTIAL for iOS Safari | Clip 0 playing at 1.5s with `readyState` 4; after the swap clip 1 playing and clip 0 paused at opacity 0; both paused after scrolling to photographer. iOS not tested (Flag C8). |
| F19 | Given the jittered grid and swap shuffle, when it runs 60 swaps, then coverage stays at least 0.85. | VALIDATED | Coverage 0.91 → 0.94, 0.94, 0.90 at 1440×900 and 0.97 → 0.93, 0.91, 0.95 at 390×844. The fully random first version clumped (image check), so it was replaced. |
| F20 | Given the `.86` ink scrim, when text sits over the brightest possible pixel, then contrast stays at AA or better. | VALIDATED | WCAG luminance math: `--card` 9.89:1, `--rule` 6.69:1, `--leaf` 7.47:1 on the scrim over white; `--card` alone on the `.55` dim over white would be only 3.53:1, which is why the text gets its own scrim. |
| F21 | Given `flashcheck.py`, when run on a 6 Hz strobe and a calm clip, then it fails the strobe and passes the calm clip. | VALIDATED as a heuristic; PARTIAL as a WCAG proof | Strobe: 6 flashes/s, FAIL. Calm: 0, PASS. Whole-frame average only (28.7). |
| F22 | Given real gameplay at 960×540, 6s, CRF 28, then it fits 900 KB. | PARTIAL | A synthetic 960×540 5s pattern encoded to 483 KB, a fractal one to 773 KB. Real high-motion gameplay may need CRF 30 to 32 or 854 wide (28.3). Proven only on the build card. |

Risks:

- **Copyright (Flag C1).** The biggest risk in this addendum, and the only one that could take the whole site down. Mitigated by sourcing order, credits, manifest and graceful removal; not removable while third-party footage is used.
- **Weight on phones.** Mitigated: nothing loads until gamer is near, one clip at a time, Save-Data gets posters only, Back frees the decoders.
- **Third-party flashing.** Mitigated by the flash check, the dim overlay, curation, the toggle and reduced motion. The check's whole-frame limit is accepted.
- **Source quality.** Many GIPHY GIFs are 480px wide and soft at full screen. The dim hides some of it; prefer 640px+ sources.
- **Placeholder shipped as final.** Mitigated by R59's visible labels and copy, and R61 being a separate, blocked card.
- **Scope creep into passion content.** Ruled out in 25.2 and 31.4.

### 31.4 Non-goals for addendum 3 (do not build)

- Written content about each passion beyond the one placeholder line per panel; links, galleries, captions, lightboxes or modals in act four.
- Tabs, a sub-nav, a scroll-spy, hash updates while scrolling, or any second layer, file or route for the passions.
- A mosaic of several clips at once; audio; video controls; GIFs as files; a WebM copy; hotlinking or embedding from GIPHY, Tenor, YouTube or any other host; a GIPHY API key or SDK.
- Stock or royalty-free stand-in photos; any photo of Nick's before he sends it; a photo upload UI.
- Moving "signal pulses", a looping redraw, or any interaction (hover, click, parallax) on the circuit board; canvas or WebGL.
- Persisting the motion toggle or anything else (cookies, storage); analytics.
- Any change to act three's glitch, timings or chips (other than removing the stub description), the fork, the pills, the scroll intro or the research and technology prongs.
- Any change to `index.html`, the case-study pages, `resume.html`, `README.md`, `CNAME`, `AGENTS.md`. No new HTML, CSS or JS files, libraries, CDN scripts or build tooling. No push to or merge into `main`, and no PR.

**Authorized boundaries (build card t_24e05978):** edit `intro.html` on `feature/intro-experience` in `~/Documents/github/portfolio`; add files under `assets/passions/gamer/` and save `docs/tools/flashcheck.py`; update `BACKLOG.md` rows for this work; web search and browser tools to source clips; the local ffmpeg for conversion; commit and `git push origin feature/intro-experience`; run or reuse the preview server on port 8000.

**Forbidden actions:** editing any other site file; adding photos or stock images; hotlinking media; pushing any other branch; committing to or merging into `main`; installing packages or adding services beyond the preview server.

### 31.5 Follow-ups (logged in BACKLOG.md, not requirements)

- **Photographer photos (BLOCKED on Nick):** swap the placeholder frames for Nick's photos per R61 once he sends them.
- **Passion content:** what Nick wants to say in each of the three panels.
- **Lower-risk gamer footage:** replace sourced clips with captures Nick records himself, after checking each publisher's fan-content policy (28.8).
- Optional: a captioned photo gallery behind the collage.

---

# Addendum 4: research branch, intro beat (affinity map) (card t_b6a0515b)

Added 2026-11-12 by product. Builds on `intro.html` at commit 845f15a (passion branch complete: act three, act four with all three backgrounds and Nick's photos). Same harness, tokens, fonts and conventions as sections 1 to 31 unless a line below says otherwise. Build card: t_f25a55e9 (assignee `design`). This addendum is sections 32 to 37 and requirements R66 to R79. Spec only: this card changes no code.

## 32. Source, scope and what it changes

### 32.1 Source brief (Nick, verbatim, via card t_b6a0515b)

> For research, we will break it down into three sections as well. Education, philosophy, and practice. We need an engaging and on theme (though probably more professional) way of guiding the user down those three paths.

Maestro offered three directions. Nick replied "1" to this one:

> Affinity map / corkboard assembly: sticky notes drift onto the screen and self-organize into three labeled clusters — Education, Philosophy, Practice — connected by string, like a live research synthesis board. This is strong because it's literally what Nick does for a living (UX research/affinity mapping) — it doubles as a subtle flex, not just a transition effect.

Citation shorthand added: **[Nick-E]** = Nick's brief above. **[Pick-1]** = the direction Nick chose. **[Card5]** = card t_b6a0515b's body (scope, the seven required items, done-when). **[Spike4]** = the throwaway prototype I ran for this addendum; results in 37.3.

### 32.2 Scope boundary: the three clusters are stubs

This pass builds **from the research prong up to and including three labeled, clickable-looking clusters**: the entry transition, the sticky-note assembly, the connecting thread, and the three cluster links `Education`, `Philosophy`, `Practice`. **Education, Philosophy and Practice are stubs for this pass. What is behind each cluster is out of scope for this pass.** No education, philosophy or practice content is specified or built here. Each cluster is an honest stub (R73), exactly as the passion branch's techie, gamer and photographer chips were before addendum 3 (R42). The content gets its own PRD addendum and build card later. The `technology` prong stays a stub (R26).

### 32.3 Do Education, Philosophy and Practice share one page? (decided here, flagged as D1)

Nick said "contained on one page" for the passions (19.3). He did not say it for research. **My recommendation: yes, one shared page, the same shape as `#passions`.**

| Option | Tradeoff |
|---|---|
| A. Three separate layers or routes, one per cluster | Three times the router, Back and focus code; three entry transitions to design; a visitor who wants all three has to bounce back to the board twice. Rejected. |
| **B. One page, three stacked subsections in Nick's order** | Education, then Philosophy, then Practice reads as one story (where I learned it, what I believe, how I do it). It reuses the exact act-four mechanics the passion branch already proved (one layer, one router branch, Back returns to the board). On a phone it is one continuous scroll. **Chosen.** |

Decided shape, so the links can be wired to their final targets today (same move as 19.3):

| Thing | Decision |
|---|---|
| The page | One future `<section id="findings">` in `intro.html`, after `#research`, using the fixed-layer pattern of act four (z-index 17). Built by a later card, not this one. |
| Its parts | Three subsections, ids `research-education`, `research-philosophy`, `research-practice`, in that order, on one scroll. |
| The links | Real `<a>` elements with `href="#research-education"`, `#research-philosophy`, `#research-practice`. Set **now** and never changed by the next card. |
| Routing | The `#research-` hash prefix is reserved now. Today the router answers it with the stub (R73). The next card changes only that router branch, adds `#findings`, and deletes the stub line and the `aria-describedby`. |

The container is `findings`, not `research-…`, so the reserved prefix only ever means "a subsection". If Nick prefers three separate pages, it is a three-href change. That is Flag D1, not a requirement.

### 32.4 What this changes in sections 1 to 31

| Earlier decision | Change |
|---|---|
| R26: research and technology prongs are stubs | **Narrowed.** `research` now starts the research beat (R66). `technology` stays a stub exactly as R26 says. The `research` prong loses `aria-describedby="fork-soon"`. |
| R30 and R33: research and technology carry "Coming soon." and write the R26 line | Now only `technology` does. R33's check "research and technology still have `aria-describedby`" reads "technology still has". |
| R27, R48, R50: router with `#where`, `#nerd`, `#passions-*` | Two more hash families: `#research` and `#research-*` (R78). Act two stays open underneath both. |
| R31, R49, R65: script budget | The main inline script changes by two lines (34.6) and stays under 345. A new **fourth** block, `<script id="research-js">`, under 200 lines, holds the research beat. So `grep -c "<script" intro.html` becomes **4** (R65 said 3). Still no `src=` scripts, no libraries. |
| R65: no new hex, same fonts | **Unchanged.** Every color below is an existing token or an `rgba()` of `--ink`. No new font family, no new weight request (EB Garamond italic 500 is already in the section 1 URL). |
| 18.4 and 24.4 non-goals ("anything a prong leads to") | Narrowed: the research prong's intro beat is in scope. Everything behind the three clusters stays a non-goal (37.4). |
| Section 7 harness server line | For this addendum, `python3 docs/tools/serve.py 8000` (the byte-range server the iOS clip fix introduced). `python3 -m http.server 8000` also works, since this beat loads no media. |

### 32.5 Map to the card's seven required items

| Card item | Decided in |
|---|---|
| 1. Entry transition, prong order, reuse of the wipe | 33.2, R66, R67 |
| 2. Assembly sequence: notes, drift, clustering, thread, final clickable state | 34, R69, R70, R71, R72 |
| 3. Tone and typography, concrete | 35, R68 |
| 4. Stub behavior | 36.1, R73, R74 |
| 5. Reduced motion | 36.3, R75 |
| 6. Mobile and desktop | 36.2, R76 |
| 7. Screen readers | 36.4, R77 |

---

## 33. Structure and entry

### 33.1 Structure

```html
<!-- after </section> of #passions, before the main inline script -->
<section class="act-research" id="research" aria-labelledby="research-title" hidden>
  <div class="board" id="board">
    <div class="board-head">
      <span class="board-meta" aria-hidden="true">Synthesis · 12 notes · 3 themes</span>
      <h2 id="research-title" tabindex="-1">Research, sorted<span class="dot">.</span></h2>
    </div>
    <div class="clusters" role="group" aria-labelledby="research-title">
      <a class="cluster" data-theme="education" href="#research-education" aria-describedby="board-soon">
        <span class="c-head"><span class="c-theme" aria-hidden="true">Theme 01</span><span class="c-label">Education<span class="c-arrow" aria-hidden="true">&rarr;</span></span></span>
        <span class="c-notes" aria-hidden="true">
          <span class="note"><span class="note-face">coursework</span></span>
          <span class="note"><span class="note-face">statistics</span></span>
          <span class="note"><span class="note-face">reading list</span></span>
          <span class="note"><span class="note-face">mentors</span></span>
        </span>
      </a>
      <a class="cluster" data-theme="philosophy" href="#research-philosophy" aria-describedby="board-soon">
        <span class="c-head"><span class="c-theme" aria-hidden="true">Theme 02</span><span class="c-label">Philosophy<span class="c-arrow" aria-hidden="true">&rarr;</span></span></span>
        <span class="c-notes" aria-hidden="true">
          <span class="note"><span class="note-face">ask why</span></span>
          <span class="note"><span class="note-face">evidence first</span></span>
          <span class="note"><span class="note-face">bias check</span></span>
          <span class="note"><span class="note-face">plain words</span></span>
        </span>
      </a>
      <a class="cluster" data-theme="practice" href="#research-practice" aria-describedby="board-soon">
        <span class="c-head"><span class="c-theme" aria-hidden="true">Theme 03</span><span class="c-label">Practice<span class="c-arrow" aria-hidden="true">&rarr;</span></span></span>
        <span class="c-notes" aria-hidden="true">
          <span class="note"><span class="note-face">interviews</span></span>
          <span class="note"><span class="note-face">usability tests</span></span>
          <span class="note"><span class="note-face">surveys</span></span>
          <span class="note"><span class="note-face">synthesis</span></span>
        </span>
      </a>
    </div>
    <p class="board-status" id="board-status" role="status" aria-live="polite"></p>
    <span class="vh" id="board-soon">Coming soon.</span>
    <svg class="threads" id="threads" aria-hidden="true" focusable="false"><path pathLength="1"/><path pathLength="1"/></svg>
  </div>
</section>
```

- **Each cluster is one link.** The whole cluster (header note plus its four notes) is the `<a>`, so the hit area is the whole group. Its accessible name is only the visible label (`Education`), because the theme number, the arrow and the four notes are all `aria-hidden` (36.4).
- **Layer:** `.act-research { position:fixed; inset:0; z-index:16; background-color:var(--paper); overflow-y:auto; overscroll-behavior:contain; }`, `.act-research[hidden]{display:none}`. z-index 16 is act three's tier: research and passion are sibling branches and are never open together. It sits above act two (15) and below the skip link (20). The layer only scrolls if a screen is too short for the board (it fits at every tested size, 37.3).
- **While open:** `main.inert = true` (already, from act two), act two stays un-hidden underneath with `.fork-scene.inert = true`. The page never sets `overflow:hidden` on `html`/`body` (R3).
- **State machine** (one variable in `research-js`): `closed → entering → open`, plus `open|entering → closed` on Back.
- **Class names are new and collision-free.** `grep` on 845f15a finds no existing `.board`, `.cluster`, `.note`, `.c-head` or `.threads` rule. (`.g-note` exists and is unrelated.) Keyframe names are new too: `research-wipe`, `note-drift`, `note-sort`, `head-stick`, `thread-draw`, `board-title-in`. Do not reuse `trace`, `pop` or `beat-in`.

### 33.2 Entry: a wipe in from the left (card item 1)

**Fork order, checked:** research is the **left-hand road** (17.3.2: "Left prong (research)"), and the prong row is `research`, `technology`, `passion`, left to right (R25). The avatar already looks left when research is chosen (17.3.3: `translate(-2px,0)`).

**Decision: the passion branch's wipe, mirrored.** Same single full-screen panel, same 700ms, same 120ms beat for the avatar's glance, same "heavy fly line" easing `cubic-bezier(.7,0,.2,1)`, same hem shadow, but the board slides in **from the left**, so the visitor literally takes the left road. No new transition technique: a wipe is already this intro's "you took a branch" move (20.2), and the curtain stays the red pill's moment.

Times are milliseconds from the research prong's activation (click, tap, Enter or Space). The full beat timeline is in 34.3.

| t (ms) | What happens | Technique |
|---|---|---|
| 0 | The existing prong handler sets `last='research'`, the avatar's `data-look="research"` and clears `#fork-status` (unchanged), then returns (34.6). `research-js` takes over: state `entering`, `history.pushState({act:'research'}, "", "#research")`, `L.hidden = false`, `L.scrollTop = 0`, `.fork-scene.inert = true`, `#board-status` cleared, `layout()` (34.5), `.clusters.inert = true`, class `is-entering` on `L`. | JS |
| 120 to 820 | **The wipe.** `.act-research.is-entering { animation: research-wipe 700ms cubic-bezier(.7,0,.2,1) 120ms both; box-shadow: 18px 0 36px -12px rgba(22,36,28,.45); overflow-y:hidden; }` (inside the motion query, 34.3) and `@keyframes research-wipe { from{transform:translateX(calc(-100% - 48px));} to{transform:none;} }`. The hem shadow sits on the **right**, the leading edge. | CSS |
| 820 | On `animationend` of `research-wipe`: focus moves to `#research-title` (`focus({preventScroll:true})`), so a screen reader says "Research, sorted., heading level 2" (R77). | JS |

- **No scrolling during the entry:** `overflow-y:hidden` on the layer while `is-entering` (not on `html`/`body`).
- **Skip (impatient visitors):** same rules as 17.2 and 20.2. From t = 400ms until the end step, a `pointerdown` on `L` or a `keydown` of Escape, Enter or Space calls `finish()` on every animation in `L.getAnimations({subtree:true})` whose timeline is the document timeline, then runs the end step on the next task (`setTimeout(…, 0)`, so Space doesn't also scroll). The 400ms arming delay stops the key that activated the prong from also skipping. Skip fires once.

---

## 34. The board: the affinity-map assembly (card item 2)

### 34.1 What the board is

A UX researcher's synthesis board as it actually looks in 2026: the dotted canvas of a digital whiteboard (FigJam, Miro), with the corkboard part carried by brass pins and one copper thread rather than a literal cork texture. That keeps it inside the site's palette and reads as a working tool, not a crime-show prop (Flag D5).

| Part | Spec |
|---|---|
| `.board` | `position:relative; min-height:100svh; overflow:clip; display:grid; grid-template-rows:auto auto auto; align-content:center; justify-items:center; padding:max(env(safe-area-inset-top), clamp(28px,7svh,80px)) var(--pad) calc(clamp(20px,4svh,40px) + env(safe-area-inset-bottom));` |
| Canvas texture | `background-image: radial-gradient(circle, rgba(22,36,28,.10) 1px, transparent 1.6px); background-size: 24px 24px; background-position: center;` on `--paper`. A dot every 24px, barely there. |
| Board meta (eyebrow) | `Synthesis · 12 notes · 3 themes`, `aria-hidden`. IBM Plex Mono 500, 12px, `letter-spacing:.14em`, `text-transform:uppercase`, `--ink-soft`, `margin:0 0 10px`. The label a whiteboard frame carries. |
| Title | `Research, sorted.` (`<h2 id="research-title">`), period `<span class="dot">` in `--moss`. Style in 35. |
| `.clusters` | `width:100%; max-width:1056px; display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:clamp(24px,3.4vw,48px); margin:clamp(28px,5svh,56px) 0 0;` |
| Status line | `.board-status { margin:16px 0 0; min-height:1.6em; text-align:center; font-style:italic; font-size:clamp(17px,1.6vw,19px); color:var(--ink-soft); }` (EB Garamond italic, same as `#fork-status`). |

### 34.2 The notes: twelve data notes, three header notes

Affinity mapping has two kinds of note: **data notes** (one observation each) and a **header note** written once a group forms. The board uses both.

**Data notes: exactly 12, four per theme, each with a short text fragment.** Not blank squares: blank squares read as a loading skeleton, and real fragments are what make it read as research (the "flex" in [Pick-1]). The fragments are generic method and mindset words, not claims about Nick's history. They are decorative and `aria-hidden`, and Nick can swap any of them (Flag D3).

| i | Theme | Text | Note color | Final tilt `R[i]` |
|---|---|---|---|---|
| 0 | Education | `coursework` | `--leaf` `#CFE2A6` | −2° |
| 1 | Education | `statistics` | `--leaf` | 1.5° |
| 2 | Education | `reading list` | `--leaf` | −1° |
| 3 | Education | `mentors` | `--leaf` | 2.5° |
| 4 | Philosophy | `ask why` | `--card` `#F8FAF4` | 1° |
| 5 | Philosophy | `evidence first` | `--card` | −2.5° |
| 6 | Philosophy | `bias check` | `--card` | 2° |
| 7 | Philosophy | `plain words` | `--card` | −1.5° |
| 8 | Practice | `interviews` | `--rule` `#C8D3BE` | −1° |
| 9 | Practice | `usability tests` | `--rule` | 2° |
| 10 | Practice | `surveys` | `--rule` | −2° |
| 11 | Practice | `synthesis` | `--rule` | 1° |

- **One color per theme**, three quiet tints of the site's own greens. During the scatter the colors are mixed, so the sort is legible as "like goes with like" (the whole point of affinity mapping).
- Note face: `.note-face { display:block; aspect-ratio:1/.82; padding:10px 12px; font-style:italic; font-weight:500; font-size:clamp(14px,1.25vw,18px); line-height:1.2; color:var(--ink); background-image:linear-gradient(to bottom, rgba(22,36,28,.06), rgba(22,36,28,0) 18%); box-shadow: inset 0 0 0 1px rgba(22,36,28,.08), 0 1px 1px rgba(22,36,28,.10), 0 8px 14px -10px rgba(22,36,28,.40); }` (EB Garamond, from `body`). The top gradient is the adhesive strip; the 1px inset line keeps the near-white Philosophy notes visible on paper.
- Color per theme: `.cluster[data-theme="education"] .note-face{background-color:var(--leaf)}`, `philosophy` → `var(--card)`, `practice` → `var(--rule)`.
- Final layout per cluster: `.c-notes { display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:12px; }` (2 × 2 under the header). Each `.note` carries `rotate: var(--r)` (its final tilt, set by `layout()`).
- Text contrast (WCAG math on the tokens): `--ink` on `--leaf` 11.57:1, on `--card` 15.32:1, on `--rule` 10.37:1.

**Header notes: 3, one per theme, pinned.** These are the clickable labels.

```css
.cluster{ position:relative; display:block; color:inherit; text-decoration:none;
  transition:transform .18s cubic-bezier(.22,.7,.2,1); -webkit-tap-highlight-color:transparent; }
.c-head{ position:relative; display:block; padding:20px 16px 14px; background-color:var(--pine); color:var(--card);
  box-shadow:0 1px 1px rgba(22,36,28,.12), 0 10px 18px -12px rgba(22,36,28,.5); transition:box-shadow .18s ease; }
.c-head::before{ content:""; position:absolute; left:50%; top:-5px; width:12px; height:12px; margin-left:-6px; border-radius:50%;
  background:radial-gradient(circle at 35% 35%, rgba(248,250,244,.65) 0 1.5px, transparent 2.5px), var(--rec);
  box-shadow:0 1px 2px rgba(22,36,28,.45); }                                   /* the brass pin */
.c-theme{ display:block; font-family:"IBM Plex Mono",monospace; font-size:11px; letter-spacing:.12em; text-transform:uppercase; color:var(--leaf); }
.c-label{ display:flex; justify-content:space-between; align-items:baseline; gap:8px; margin-top:4px;
  font-family:"Fraunces",Georgia,serif; font-weight:600; font-variation-settings:"opsz" 72;
  font-size:clamp(20px,2.1vw,28px); line-height:1.1; }
.c-arrow{ display:inline-block; font-family:"IBM Plex Mono",monospace; font-weight:500; font-size:.9em; color:var(--leaf);
  transition:transform .18s cubic-bezier(.22,.7,.2,1); }
@media (hover:hover){
  .cluster:hover{ transform:translateY(-3px); }
  .cluster:hover .c-head{ box-shadow:0 1px 1px rgba(22,36,28,.12), 0 16px 24px -14px rgba(22,36,28,.6); }
  .cluster:hover .c-arrow{ transform:translateX(3px); }
}
.cluster:focus-visible{ outline:2px solid var(--pine); outline-offset:6px; transform:translateY(-3px); }
.cluster:focus-visible .c-arrow{ transform:translateX(3px); }
.cluster:active{ transform:translateY(-1px); }
```

- Contrast: `--card` label on `--pine` 7.39:1; `--leaf` theme line and arrow on `--pine` 5.58:1; the pine header against paper 6.61:1 (WCAG 1.4.11 non-text contrast for the control's boundary).
- **Why it reads as clickable:** a solid, raised, high-contrast card with a right arrow, the whole group lifting on hover and on keyboard focus, the arrow nudging forward, `cursor:pointer` from the link. Touch screens have no hover, so the arrow carries the affordance there. An image check of the spike's final frame: "the right arrows suggest navigable cards" [Spike4].

### 34.3 The assembly sequence (exact timeline)

Five movements, all time-based (no scroll), all from the one click. Notes **drift in** unsorted, **hold** a beat as a messy brain dump, **sort** themselves into the three clusters, the header notes **stick on**, then the **thread draws** itself and the title lands.

| t (ms) | Movement | Spec |
|---|---|---|
| 120 to 820 | Wipe from the left | 33.2 |
| 900 to 2360 | **Drift in.** The 12 data notes float onto the board from off-screen, in `ORDER` (themes interleaved), one every 60ms. Each lands at its scatter spot with a long, soft landing and a small tilt settling out. | inner `.note-face`: `note-drift 800ms cubic-bezier(.16,.84,.3,1) var(--dd) both`; `--dd = 900 + ORDER.indexOf(i)*60` |
| 2360 to 2450 | **Hold.** Twelve mixed-color notes scattered across the board. The "before". | none |
| 2450 to 3445 | **Sort.** Each note glides from its scatter spot to its slot in its theme's 2 × 2 grid, Education first, then Philosophy, then Practice (80ms apart), notes within a theme 25ms apart. Smooth and deliberate, no bounce. | outer `.note`: `note-sort 760ms cubic-bezier(.6,0,.25,1) var(--sd) both`; `--sd = 2450 + floor(i/4)*80 + (i%4)*25` |
| 3000 to 3460 | **Name the themes.** Each header note sticks on above its group (a slight press: 1.08 to 1 scale, 6px drop, fade in), left to right, 110ms apart. | `.c-head`: `head-stick 240ms cubic-bezier(.2,.8,.3,1.1) var(--hd) both`; `--hd = 3000 + c*110` |
| 3400 to 3920 | **Connect them.** The copper thread draws itself pin to pin: Education to Philosophy, then Philosophy to Practice. | `thread-draw 400ms cubic-bezier(.35,.1,.25,1) var(--td) both`; `--td = 3400 + i*120` |
| 3700 to 4100 | **Title lands.** Board meta and `Research, sorted.` fade up 8px. | `.board-head`: `board-title-in 400ms cubic-bezier(.22,.7,.2,1) 3700ms both` |
| 4100 | **End step** (on `animationend` of `board-title-in`, or a 4700ms safety timeout, or a skip): `is-entering` removed, state `open`, `.clusters.inert = false`, focus stays on the title (moved there at 820). | JS |

The whole beat is 4.1 seconds, skippable from 0.4s (Flag D6). Nothing moves after the end step: no idle wobble, no looping, so WCAG 2.2.2 needs no pause control and there is nothing that can flash.

```css
/* === research branch (PRD 33-36) === */   /* ALL research CSS (34.1, 34.2, this block, 36.2) sits between this comment and the end marker */
@media (prefers-reduced-motion:no-preference){
  .act-research.is-entering{ animation:research-wipe 700ms cubic-bezier(.7,0,.2,1) 120ms both;
    box-shadow:18px 0 36px -12px rgba(22,36,28,.45); overflow-y:hidden; }               /* 33.2 */
  .act-research.is-entering .clusters{ pointer-events:none; }
  .act-research.is-entering .note       { animation:note-sort 760ms cubic-bezier(.6,0,.25,1) var(--sd) both; }
  .act-research.is-entering .note-face  { animation:note-drift 800ms cubic-bezier(.16,.84,.3,1) var(--dd) both; }
  .act-research.is-entering .c-head     { animation:head-stick 240ms cubic-bezier(.2,.8,.3,1.1) var(--hd) both; }
  .act-research.is-entering .threads path{ stroke-dasharray:1; stroke-dashoffset:1;
                             animation:thread-draw 400ms cubic-bezier(.35,.1,.25,1) var(--td) both; }
  .act-research.is-entering .board-head { animation:board-title-in 400ms cubic-bezier(.22,.7,.2,1) 3700ms both; }
}
@keyframes research-wipe{ from{ transform:translateX(calc(-100% - 48px)); } to{ transform:none; } }
@keyframes note-drift{ from{ translate:var(--dx) var(--dy); rotate:var(--dr); opacity:0; } to{ translate:0 0; rotate:0deg; opacity:1; } }
@keyframes note-sort { from{ translate:var(--sx) var(--sy); rotate:var(--sr); }            to{ translate:0 0; rotate:var(--r); } }
@keyframes head-stick{ from{ opacity:0; scale:1.08; translate:0 -6px; }                    to{ opacity:1; scale:1; translate:0 0; } }
@keyframes thread-draw{ to{ stroke-dashoffset:0; } }
@keyframes board-title-in{ from{ opacity:0; translate:0 8px; } to{ opacity:1; translate:0 0; } }
/* === end research branch === */
```

**Why two elements per note.** The outer `.note` owns the sort (scatter spot to slot), the inner `.note-face` owns the drift (off-screen to the scatter spot). Their translations add up, so each note drifts in, rests at its scatter spot (the outer's `backwards` fill holds it there until its sort starts), then sorts. Both use the individual `translate`/`rotate`/`scale` properties, never `transform`, so the cluster's hover and focus `transform` still works on top (the trap 17.3.4 and 22.1 already avoided).

**Base styles are the final state.** All from-states live only in keyframes with `both` fill inside the motion query. When `is-entering` is removed, or under reduced motion, or after a skip, the base CSS already shows every note in its slot with its final tilt, the headers and thread complete, the title visible.

### 34.4 The thread (connecting string)

- **What it connects:** the three header notes' pins, Education to Philosophy to Practice: two segments, one continuous thread. Not one string per note: 12 strings would be a detective wall, and an affinity map groups by proximity, not by string. The thread says "these three themes are one body of work".
- **Look:** `.threads { position:absolute; inset:0; width:100%; height:100%; pointer-events:none; z-index:3; overflow:visible; }` and `.threads path { fill:none; stroke:var(--rec); stroke-width:2; stroke-linecap:round; }` (`stroke-width:1.75` in the stacked layout, 36.2). Copper (`--rec` `#B0703A`, an existing token) reads as twine next to the brass pins; it is 3.42:1 on paper, so it is visible without shouting. It sits **above** the notes, so it rides over the pins like real string, and the geometry keeps it off all text (below).
- **It draws itself**, exactly like the techie board (27.4): each path has `pathLength="1"`, starts at `stroke-dasharray:1; stroke-dashoffset:1` and animates to 0. At rest there is no dash rule, so it is simply a complete line.
- **Geometry, computed by `layout()` (34.5) from layout boxes, never per frame:**
  - Pin points: in the row layout (3 columns), the top center of each header, `(x + w/2, y + 1)`; in the stacked layout (36.2), the header's top-left corner, `(x + 6, y + 6)`. The CSS pin sits on that point in both layouts.
  - Row layout: a hanging curve, `M a Q mid.x, max(a.y,b.y) + S  b` with sag `S = min(28px, 0.07 × distance)`. It crosses the header notes only in their top padding (deepest point 14px below the header top at 1440×900; the theme line starts 20px down) [Spike4].
  - Stacked layout: a curve that swings out into the left margin, `M a C (a.x − 32, a.y + h/3) (b.x − 32, b.y − h/3) b`, `h = b.y − a.y`. It runs down the gutter beside the notes and never crosses one; its leftmost point stays at x ≥ 4px [Spike4].
- **Measured from layout boxes** (`offsetLeft`/`offsetTop` up to `.board`), not `getBoundingClientRect`, so the wipe's and the notes' in-flight transforms never skew the pins.

### 34.5 `layout()`: the scatter and thread math (exact, validated in the spike)

Runs when the board opens (after `L.hidden = false`), on `document.fonts.ready`, and on `resize` (debounced 150ms). After a resize while open, the board simply re-lays out at rest (no replay). `rng` is the same mulberry32 as 27.2 (copy the three-line function into `research-js`; the passions copy is private to its IIFE). Fixed seed 5, so the same viewport always gets the same scatter, which keeps tests repeatable.

```js
var STACK = window.matchMedia('(max-width:699px) and (min-height:501px)');
var R     = [-2, 1.5, -1, 2.5,  1, -2.5, 2, -1.5,  -1, 2, -2, 1];   // final tilt (deg) per note i = 0..11
var ORDER = [0, 5, 10, 3, 6, 9, 1, 8, 11, 4, 2, 7];                 // drift-in order: themes interleaved
var SHUF  = [13, 2, 8, 10, 0, 11, 6, 4, 9, 3, 14, 5];               // scatter cell per note (15 cells, 12 used)
function pos(el){ var x = 0, y = 0; while(el && el !== board){ x += el.offsetLeft; y += el.offsetTop; el = el.offsetParent; } return {x:x, y:y}; }
function layout(){
  if(L.hidden) return;
  var W = board.clientWidth, H = board.clientHeight, stacked = STACK.matches, r = rng(5);
  var cols = stacked ? 3 : 5, rows = stacked ? 5 : 3;
  var padX = parseFloat(getComputedStyle(board).paddingLeft), cw = (W - 2*padX) / cols, ch = H * .76 / rows;
  Array.prototype.forEach.call(board.querySelectorAll('.note'), function(n, i){
    var p = pos(n), cx = p.x + n.offsetWidth/2, cy = p.y + n.offsetHeight/2, c = SHUF[i] % cols, rw = Math.floor(SHUF[i] / cols);
    var tx = padX + cw*(c + .5) + (r() - .5)*.8*cw, ty = H*.12 + ch*(rw + .5) + (r() - .5)*.8*ch;   // scatter spot
    var dx = tx - W/2, dy = ty - H/2, d = Math.max(1, Math.hypot(dx, dy)), k = .8 * Math.max(W, H);   // fly in along the ray from the center
    var s = n.style, f = n.firstElementChild.style;
    s.setProperty('--r',  R[i] + 'deg');
    s.setProperty('--sx', (tx - cx).toFixed(1) + 'px'); s.setProperty('--sy', (ty - cy).toFixed(1) + 'px');
    s.setProperty('--sr', (r()*16 - 8).toFixed(1) + 'deg');
    s.setProperty('--sd', (2450 + Math.floor(i/4)*80 + (i%4)*25) + 'ms');
    f.setProperty('--dx', (dx/d*k).toFixed(1) + 'px'); f.setProperty('--dy', (dy/d*k).toFixed(1) + 'px');
    f.setProperty('--dr', (r()*24 - 12).toFixed(1) + 'deg');
    f.setProperty('--dd', (900 + ORDER.indexOf(i)*60) + 'ms');
  });
  var heads = board.querySelectorAll('.c-head');
  var P = Array.prototype.map.call(heads, function(h, c){
    h.style.setProperty('--hd', (3000 + c*110) + 'ms');
    var p = pos(h); return stacked ? {x: p.x + 6, y: p.y + 6} : {x: p.x + h.offsetWidth/2, y: p.y + 1};
  });
  threads.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
  Array.prototype.forEach.call(threads.querySelectorAll('path'), function(path, i){
    var a = P[i], b = P[i + 1], d;
    if(!stacked){ var S = Math.min(28, .07 * Math.hypot(b.x - a.x, b.y - a.y));
      d = 'M' + a.x + ',' + a.y + ' Q' + (a.x + b.x)/2 + ',' + (Math.max(a.y, b.y) + S) + ' ' + b.x + ',' + b.y; }
    else { var t = (b.y - a.y) / 3;
      d = 'M' + a.x + ',' + a.y + ' C' + (a.x - 32) + ',' + (a.y + t) + ' ' + (b.x - 32) + ',' + (b.y - t) + ' ' + b.x + ',' + b.y; }
    path.setAttribute('d', d); path.style.setProperty('--td', (3400 + i*120) + 'ms');
  });
}
```

- **The scatter is a jittered 5 × 3 grid over the whole board** (3 × 5 when stacked), 12 of 15 cells used, each spot nudged up to ±40% of a cell. `SHUF` puts every theme's notes far apart, so the brain dump is visibly mixed. The spike's first version scattered over the cluster area only, on a 4 × 3 grid with ±15% jitter, and an image check called it "too much underlying spatial regularity… four fairly obvious vertical groupings"; this version was judged "an unsorted, mixed scatter rather than tidy columns" [Spike4].
- `--sx/--sy` are the scatter spot minus the note's final slot center, in px. The drift start `--dx/--dy` is 0.8 × the board's longer side along the ray from the board center, so every note enters from the nearest off-screen edge. `.board`'s `overflow:clip` hides them until they cross in.
- `R`, `ORDER`, `SHUF`, the seed and the draw order of `r()` (scatter x, scatter y, `--sr`, `--dr`) are the source of truth. Changing them changes the look; R70's checks are written against them.

### 34.6 Wiring into the existing scripts

`research-js` is a fourth inline block after `passions-js`. It owns the layer, `layout()`, the state machine, the skip, the cluster click handler and its own `route()` on `popstate`, `hashchange` and `load`, the same pattern `passions-js` uses. The **main** inline script changes in exactly two places:

1. Prong click handler: after `status.textContent = '';` add `if(n === 'research') return;` (the main handler still sets `last` and the avatar look; `research-js`'s own click listener on the same button, registered later, starts the beat). The `research` button loses `aria-describedby="fork-soon"` in the markup.
2. Router: `if(h === '#where') openDirect(); else close();` becomes `if(h === '#where' || /^#research(-|$)/.test(h)) openDirect(); else close();`, so act two stays open under the research layer on Back, Forward and direct loads.

Router behavior in `research-js` (idempotent, because one anchor click fires both `popstate` and `hashchange` [Spike2, F15]):

| Hash | Research layer |
|---|---|
| `#research` | If closed: open at rest (no wipe, no assembly, end-step state, focus `#research-title`). If open: clear `#board-status`, return focus to the last activated cluster if focus fell to `<body>` or the layer. |
| `#research-education`, `-philosophy`, `-practice` | If closed (direct load, new tab, Forward): open at rest and announce that cluster's stub line once. If open (a click just happened): leave it, no second announcement. |
| any other `#research-…` | Open at rest, no announcement. |
| anything else | If open: close (hidden, timers cleared, `is-entering` removed, `.fork-scene.inert = false`, status cleared, focus to the `research` prong). |

---

## 35. Tone and typography: "more professional", concretely (card item 3)

Passion was a nerd shouting (Fraunces 600 to 800 slamming in at 128px, emoji claps, an RGB-split glitch, the page flipping to ink, a game-menu chip). Research should sound like Nick at work: calm, evidence-led, precise. The concrete direction:

| Dimension | Passion branch (contrast) | Research branch (this spec) |
|---|---|---|
| Ground | Paper that flips to `--ink` "terminal mode", scanlines | `--paper` throughout, faint 24px dot grid. Stays light. No dark flip. |
| Display type | Fraunces 600 (beats) and 800 SOFT 50 (`Nerd.`), up to 128px, slammed in with overshoot | Title: Fraunces **500**, `clamp(30px,5vw,56px)`, `line-height:1.08`, `letter-spacing:-.015em`, `--ink`, `margin:0`, `text-wrap:balance`: exactly the `#where-title` voice. Labels: Fraunces **600**, `opsz 72`, **no SOFT/WONK axes** (crisp, not playful). |
| Body/annotation type | Emoji, glitch copies | EB Garamond italic **500** on the notes (a pen on a sticky note), EB Garamond italic on the status line (the site's narrator voice) |
| Technical type | Plex Mono game-menu chips with hard pixel shadows and a blinking caret | Plex Mono only as quiet metadata: the board eyebrow and `THEME 01/02/03`, 11 to 12px, wide tracking, uppercase. No chips, no caret, no `steps()` easing. |
| Palette | `--ink`, ember `rgb(196,84,58)`, `--leaf` glitch, `--pill-red`, `--pill-blue`, `--rule` | `--paper`, `--ink`, `--ink-soft`, `--pine` (headers), `--leaf` / `--card` / `--rule` (note tints), `--moss` (the period), `--rec` (pins and thread). **None** of `--pill-red`, `--pill-blue`, `--glow-ember`, `--glow-warm`. Greens only, plus one warm metal accent. |
| Motion character | Stepped, staccato, overshoot slams, glitch slices | Eased, continuous, a soft landing, one gentle sort, a single draw. Max overshoot is the 1.08 header press. No flicker, no steps, no shake. |
| Green-period signature | `Nerd.` | `Research, sorted.` (continues `welcome.`, `Nick.`, `Nerd.`) |

Copy: `Research, sorted.` is mine (Flag D2): three words that name the move the visitor just watched. The eyebrow `Synthesis · 12 notes · 3 themes` is the subtle flex Nick's pick asked for: it is how a real synthesis frame is labeled. Cluster labels are capitalized `Education`, `Philosophy`, `Practice` (the card's spelling, and the more formal register). The fork's prongs stay lowercase; the difference is deliberate (Flag D4).

---

## 36. Stubs, responsive, reduced motion and accessibility (card items 4 to 7)

### 36.1 Stub behavior (card item 4): the passion pattern, reused

**Decision: reuse the stub convention the passion chips used and Crit passed (22.3, R42), not the fork's button stub (R26).** Both are "coming soon" patterns; the passion one is the newer and fits this case exactly, because the content behind these links will also arrive later as one page (32.3), and real anchors wired to their final hrefs mean the next card only touches the router.

When a cluster is activated (click, tap, Enter):

1. The browser follows the fragment natively. The URL becomes `intro.html#research-practice` and a history entry is pushed. No element has that id, so nothing scrolls. **No `preventDefault`** (R31 stays at 0).
2. The cluster's own `click` handler clears `#board-status`, then on the next animation frame writes `<Label> is coming soon. Still synthesizing.` (`Education is…`, `Philosophy is…`, `Practice is…`). Clearing first makes a repeat click re-announce. Placeholder copy, Flag D7.
3. The router sees `#research-…` with the layer open and leaves it as it is.
4. Direct load or new tab: open at rest and announce once (34.6).

Each cluster has `aria-describedby="board-soon"` ("Coming soon."), the same reasoning as 17.3.4 and 22.3: real, enabled links, honestly described, no `aria-disabled`. Back from `#research-practice` returns to `#research` with the status cleared and focus on the Practice cluster.

### 36.2 Responsive (card item 6)

Three clusters side by side need about 700px. Below that, **stack them, all three visible at once**, not one at a time: a carousel or "one cluster per screen" would hide two of the three choices behind a swipe, which is the opposite of guiding someone down three paths, and it needs gesture code. Stacked, the whole board still fits one phone screen with nothing to scroll [Spike4].

| Concern | Row layout (≥ 700px wide, or any width with height ≤ 500px) | Stacked (`(max-width:699px) and (min-height:501px)`) |
|---|---|---|
| Clusters | 3 columns, `gap:clamp(24px,3.4vw,48px)`, max 1056px wide | 1 column, `gap:18px`, `max-width:480px` |
| Header note | `padding:20px 16px 14px`, label `clamp(20px,2.1vw,28px)` | `padding:14px 14px 10px`, label 22px |
| Data notes | 2 × 2 under the header, `gap:12px`, `aspect-ratio:1/.82`, text `clamp(14px,1.25vw,18px)` | **one row of 4** under the header, `gap:8px`, `margin-top:8px`, `aspect-ratio:1/.85`, `padding:6px 7px`, text 14px |
| Pin and thread | pin top center; hanging curve between pins | pin on the header's top-left corner (`.c-head::before{ left:0; top:0; margin-left:0; }`); thread swings down the left margin |
| Thread width | 2 | 1.75 |
| Scatter grid | 5 × 3 | 3 × 5 |

Extra rules:

- **Stacked and short** (`(max-width:699px) and (min-height:501px) and (max-height:700px)`, e.g. 375×667, 320×568): `.board{ padding-top:max(env(safe-area-inset-top),24px) }`, `.board-meta{ display:none }`, `.clusters{ gap:12px; margin-top:16px }`, `.c-head{ padding:10px 12px 8px }`.
- **Under 360px wide:** `.note-face{ font-size:12px; padding:5px 6px }`, `.board-status{ font-size:16px }`.
- **Landscape phones** (`max-height:500px`, any width): keep the row layout. `.board{ padding-top:max(env(safe-area-inset-top),16px); padding-bottom:calc(8px + env(safe-area-inset-bottom)) }`, `#research-title{ font-size:28px }`, `.board-meta{ margin-bottom:4px }`, `.clusters{ margin-top:12px }`, `.c-head{ padding:12px 12px 8px }`, `.c-label{ font-size:20px }`, `.c-notes{ gap:8px; margin-top:8px }`, `.note-face{ aspect-ratio:1/.56; padding:6px 8px; font-size:14px }`. Without this, a 667×375 phone would get the stacked layout and overflow by 185px [Spike4].
- Hover lift only under `@media (hover:hover)`. `svh` only, never `dvh`. Safe-area insets on the board padding. Touch targets: every cluster is at least 120px tall.

Spike measurements (rest state, status line filled with the longest stub line, `Philosophy is coming soon. Still synthesizing.`) [Spike4]:

| Viewport | Layout | Board fits without scrolling | Status line bottom | Note text overflow |
|---|---|---|---|---|
| 1440×900 | row | yes | 732 | none |
| 1024×768 | row | yes | 635 | none |
| 768×1024 | row | yes | 738 | none |
| 390×844 | stacked | yes | 737 | none |
| 375×667 | stacked, short | yes | 590 | none |
| 320×568 | stacked, short, < 360 | yes | 524 | none |
| 844×390 | row, landscape | yes | 351 | none |
| 667×375 | row, landscape | yes | 330 | none |

### 36.3 Reduced motion (card item 5)

With `prefers-reduced-motion: reduce`, consistent with act two (a cut) and act four (appears in one cut):

- **No wipe.** The board appears in one cut at t = 0, already assembled: notes in their slots with their small static tilts, header notes and pins in place, the thread complete, the title visible. No fade either (the card asks for "static/instant"; a tilt is a pose, not motion).
- **Focus goes to `#research-title` at once.** The end step runs immediately (no `animationend` to wait for).
- **How:** every animation rule is inside `@media (prefers-reduced-motion:no-preference)` (34.3), the page's global rule (`animation:none !important`) backs that up, and the base CSS is the final state. `layout()` still runs, because the final tilts (`--r`) and the thread `d` come from it.
- Hover lift and focus lift become instant state changes (the global rule shortens transitions to 0.01ms), the same as the prong chips.
- **Toggling the setting mid-entry** (the `change` event on the media query) calls the skip path: everything jumps to the assembled board.
- No-JS visitors: the layer is `hidden` and the research prong is a plain button, so nothing happens on click. Accepted, as for act two (17.5).

### 36.4 Screen readers and keyboard (card item 7)

The visual metaphor is decoration. Assistive tech should hear one heading and three choices, nothing else.

- **Clean announcement:** the region is named by `#research-title` ("Research, sorted."). The group of links is labelled by the same heading. Each link's name is exactly `Education`, `Philosophy` or `Practice`, with the description "Coming soon." A screen-reader user hears "Research, sorted., heading level 2", then "Education, link, Coming soon.", and so on.
- **Nothing decorative leaks:** the eyebrow, `Theme 01/02/03`, the arrows, all 12 note fragments (`.c-notes`) and the thread SVG are `aria-hidden="true"`. The pins are CSS pseudo-elements with empty content. No note text appears in any accessible name or in the AX tree.
- **Focus:** at 820ms (end of the wipe) to `#research-title` (programmatic, `#research-title:focus{outline:none}`, not interactive). While entering, `.clusters` is `inert` and has `pointer-events:none`, so Tab can't land on a moving link. After the end step, Tab goes `Education`, `Philosophy`, `Practice`. Focus rings: 2px `--pine`, 6px offset, plus the lift.
- **Status:** `#board-status` is `role="status"` `aria-live="polite"` and only speaks on a cluster activation.
- **Inert underneath:** `main.inert` and `.fork-scene.inert` while the layer is open. The skip link stays on top (z-index 20); Shift+Tab reaches it.
- **Back:** focus returns to the `research` prong on the fork (from `#research`), or to the last-used cluster (from `#research-…`).

---

## 37. Requirements, deployment, flags, feasibility, non-goals

All requirements use the section 7 harness with the 32.4 server line (`python3 docs/tools/serve.py 8000`), Chromium over CDP, the same desktop (1440×900), mobile (390×844, DPR 3) and reduced-motion emulation. Definitions:

- **"At the fork"**: load `http://localhost:8000/intro.html#where`, wait 600ms.
- **`L`** is `document.getElementById('research')`; **`B`** is `document.getElementById('board')`.
- **"Open the board"**: at the fork, click `.prong[data-prong="research"]`, wait 4600ms.
- **"Seek T"**: right after the click, `L.getAnimations({subtree:true}).forEach(a => { a.pause(); a.currentTime = T; })`, then wait two animation frames. Every research animation is created by the click, so they share t = 0 and `currentTime` includes each delay. Use seek, not wall-clock sampling, for mid-sequence checks: in the spike, headless Chromium's real-time frames lagged the animation clock by up to ~1.5s [Spike4].

Build and deployment for every requirement: **not Docker**, by the same justified exception as sections 8, 18.1, 24.1 and 31.1 (a static GitHub Pages site with nothing to containerize; production deploy is a push to `main`, which stays forbidden).

### R66. Activating the research prong starts the research beat in the same page: no navigation, the URL becomes `#research`, and technology stays a stub.
- **Source:** [Nick-E] "For research, we will break it down into three sections"; [Pick-1]; [Card5] item 1; sections 33.1, 34.6.
- **Acceptance:** at the fork, set `window.__stay = 1`, click the research prong; after 4600ms: `window.__stay === 1`, `location.pathname` ends in `/intro.html`, `location.hash === "#research"`, `L.hidden === false`, `document.querySelector('#where .fork-scene').inert === true`, `document.querySelector('main').inert === true`, avatar `.avatar` `dataset.look === "research"`, `#fork-status` is empty. The research prong has no `aria-describedby`; the technology prong still has `aria-describedby="fork-soon"` and clicking it still writes `Technology is coming soon. I'm still paving that road.` with `location.hash` staying `#where`. `#research` is outside `main` (`document.querySelector('main #research') === null`) and comes after `#passions` in the DOM. `getComputedStyle(L).zIndex === "16"`.
- **Edge cases:** double-click, or Enter then click, starts it once (`document.getAnimations().filter(a => a.animationName === "research-wipe").length <= 1` at all times); Enter and Space on the focused prong both start it; the prong can't be activated during act two's curtain (`.fork-scene` is inert); with no JS nothing happens and nothing breaks.
- **Resources:** `intro.html` markup, main script (two lines, 34.6), `research-js`.

### R67. The board wipes in from the left over 700ms after a 120ms beat, with the hem shadow on its right edge and a skip.
- **Source:** [Card5] item 1 "pick a consistent, directionally-appropriate transition (reuse the established wipe/curtain mechanics)"; section 33.2.
- **Acceptance:** motion allowed, 1440×900, at the fork click research at t = 0: (a) a `research-wipe` animation exists on `L` with `getTiming()` `duration 700`, `delay 120`, `easing "cubic-bezier(0.7, 0, 0.2, 1)"`; (b) Seek 450: `L`'s computed transform `tx` strictly between `−innerWidth − 48` and 0 (negative: it comes from the left); Seek 900: `tx === 0`; (c) on a fresh run in real time, by t ≈ 1500ms `document.activeElement.id === "research-title"`; (d) while `is-entering`, `getComputedStyle(L).boxShadow` starts with `rgba(22, 36, 28, 0.45) 18px 0px 36px -12px` (positive x: right edge) and `overflowY === "hidden"`; after the end step (t ≈ 4600ms) `L.classList.contains('is-entering') === false`. **Skip:** fresh run, at t ≈ 900ms dispatch `keydown` Escape on `document`; within 150ms `is-entering` is gone, every `.note` and `.note-face` computed `translate` is `none` or `0px`, and every `.threads path` has `strokeDashoffset` 0 or no dash array. A `keydown` at t ≈ 100ms does **not** skip.
- **Edge cases:** background tab during the entry: the 4700ms safety timeout runs the end step; resize mid-wipe still covers the screen; `document.documentElement.scrollWidth <= innerWidth` throughout (the off-screen start must not add page width); `grep -c "nerd-wipe" intro.html` is unchanged (passion's wipe is untouched).
- **Resources:** `intro.html` CSS (`research-wipe`), `research-js`.

### R68. The board reads professional and on-brand: paper with a dot grid, the eyebrow, and "Research, sorted." in the `#where-title` voice, using only greens and copper.
- **Source:** [Nick-E] "though probably more professional"; [Card5] item 3; section 35.
- **Acceptance:** open the board: `#research-title` is an `H2`, `textContent === "Research, sorted."`, computed `fontFamily` starts with `"Fraunces"`, `fontWeight === "500"`, `fontSize === "56px"` at 1440×900; `#research-title .dot` `color === "rgb(126, 156, 96)"`; `.board-meta` text matches `/^Synthesis · 12 notes · 3 themes$/` with `textTransform === "uppercase"` and `fontFamily` starting `"IBM Plex Mono"`; `#board` computed `backgroundImage` contains `radial-gradient` and `backgroundSize === "24px 24px"`, and `L` `backgroundColor === "rgb(234, 238, 228)"`. Palette check: for every element inside `L` (including `::before`), the computed `color`, `backgroundColor` and `stroke` are drawn only from `rgb(234, 238, 228)`, `rgb(248, 250, 244)`, `rgb(22, 36, 28)`, `rgb(59, 82, 69)`, `rgb(47, 91, 68)`, `rgb(126, 156, 96)`, `rgb(207, 226, 166)`, `rgb(200, 211, 190)`, `rgb(176, 112, 58)`, transparent, or `rgba(22, 36, 28, a)`; specifically none is `rgb(154, 59, 46)`, `rgb(46, 74, 107)` or `rgb(196, 84, 58)`. Nothing inside `L` has `fontVariationSettings` containing `"WONK" 1`. The research CSS block uses no stepped easing: `awk '/=== research branch \(PRD 33-36\) ===/,/=== end research branch ===/' intro.html | grep -c "steps("` = 0, and the same `awk` range is non-empty (`wc -l` ≥ 40).
- **Edge cases:** Fraunces blocked: Georgia fallback keeps the title on one or two balanced lines at 320 wide without overflow; the background never flips dark at any point in the sequence (`L` and `#board` background stay paper at Seek 0, 2400, 4300).
- **Resources:** `intro.html` CSS.

### R69. Twelve decorative data notes, four per theme, carry the exact fragments, tints and fonts in 34.2, and all of them are hidden from assistive tech.
- **Source:** [Pick-1] "sticky notes drift onto the screen"; [Card5] item 2 "how many, what do they show"; section 34.2.
- **Acceptance:** open the board: `B.querySelectorAll('.note').length === 12`, each with exactly one `.note-face` child; per cluster 4 notes, texts in order: Education `coursework`, `statistics`, `reading list`, `mentors`; Philosophy `ask why`, `evidence first`, `bias check`, `plain words`; Practice `interviews`, `usability tests`, `surveys`, `synthesis`. `.note-face` computed `backgroundColor` is `rgb(207, 226, 166)` (education), `rgb(248, 250, 244)` (philosophy), `rgb(200, 211, 190)` (practice); `fontFamily` starts `"EB Garamond"`, `fontStyle === "italic"`, `fontWeight === "500"`, `color === "rgb(22, 36, 28)"`. Every `.c-notes` has `aria-hidden="true"`. At rest each `.note`'s computed `rotate` equals `R[i]` from 34.5 (`-2deg`, `1.5deg`, … `1deg`). At every viewport in R76, no `.note-face` overflows (`scrollWidth <= clientWidth + 1` and `scrollHeight <= clientHeight + 1`).
- **Edge cases:** EB Garamond blocked: Georgia italic fallback still fits each face (same overflow check); the fragments are placeholder copy Nick can edit in the markup without touching the script (Flag D3); no note is focusable.
- **Resources:** `intro.html` markup and CSS.

### R70. The notes drift in unsorted, hold as a mixed scatter, then sort themselves into their three clusters, on the 34.3 timeline.
- **Source:** [Pick-1] "drift onto the screen and self-organize into three labeled clusters"; [Card5] item 2 "timing, physics-ish easing, stagger, how they cluster"; sections 34.3, 34.5.
- **Acceptance:** motion allowed. Timing: right after the click, `L.getAnimations({subtree:true})` contains 12 `note-drift` (duration 800, easing `cubic-bezier(0.16, 0.84, 0.3, 1)`, delays exactly `{900 + 60·k : k = 0..11}`, and note `i`'s delay is `900 + 60·ORDER.indexOf(i)`), 12 `note-sort` (duration 760, easing `cubic-bezier(0.6, 0, 0.25, 1)`, note `i`'s delay `2450 + 80·floor(i/4) + 25·(i%4)`), 3 `head-stick` (240, delays 3000/3110/3220), 2 `thread-draw` (400, delays 3400/3520), 1 `board-title-in` (400, delay 3700), 1 `research-wipe`: 31 in total. Geometry, at 1440×900 and at 390×844: **Seek 600**: every `.note-face` computed opacity is 0. **Seek 2400** (scatter): all 12 note-face centers are inside the viewport; for each theme, the diagonal of the bounding box of its 4 note centers is ≥ 0.35 × `Math.hypot(innerWidth, innerHeight)` (spike: 0.46 to 0.70); `.c-head` opacity < 0.05 for all three. **Seek 4300** (rest): every note's center lies inside its own `.cluster`'s bounding box, and all three `.c-head` have opacity > 0.95.
- **Edge cases:** reload at the same viewport gives identical `--sx/--sy/--dx/--dy` inline values on every note (seeded); resizing while open re-runs `layout()` and the board stays assembled; `B`'s `overflow` is `clip` so no note adds page or layer width at any seek time (`L.scrollWidth <= L.clientWidth`, `document.documentElement.scrollWidth <= innerWidth` at Seek 900, 1500, 2400, 3000); the outer/inner split uses individual properties (`grep -E "@keyframes note-(drift|sort)" -A1` shows `translate`/`rotate`, not `transform`).
- **Resources:** `intro.html` CSS keyframes, `research-js` (`layout()`, `R`, `ORDER`, `SHUF`).

### R71. The final board shows three pinned header notes labeled Education, Philosophy and Practice, in that order, and each whole cluster looks and behaves clickable.
- **Source:** [Nick-E] "Education, philosophy, and practice"; [Pick-1] "three labeled clusters"; [Card5] item 2 "reads as clickable"; section 34.2.
- **Acceptance:** open the board: `.clusters` has `role="group"` and `aria-labelledby="research-title"` and contains exactly three `a.cluster` with `data-theme` `education`, `philosophy`, `practice` in DOM order; their `.c-label` visible text (excluding the arrow) is `Education`, `Philosophy`, `Practice`; at 1440×900 they sit left to right (`left` strictly increasing, `top` within 2px), at 390×844 top to bottom (`top` strictly increasing, `left` within 2px). Each `.c-head` computed `backgroundColor === "rgb(47, 91, 68)"`, `.c-label` `fontFamily` starts `"Fraunces"`, `fontWeight === "600"`, `color === "rgb(248, 250, 244)"`; `.c-head::before` `backgroundColor` or `backgroundImage` includes `rgb(176, 112, 58)` and `borderRadius === "50%"`; each `.c-arrow` has `aria-hidden="true"` and text `→`. Each cluster's height ≥ 120px. Hover (CDP `mouseMoved` to a cluster's center, 1440×900): the cluster's computed transform has `ty === −3` and its `.c-arrow` transform `tx === 3`. Keyboard focus: `:focus-visible` shows `outlineStyle === "solid"`, `outlineColor === "rgb(47, 91, 68)"`, `outlineOffset === "6px"`. `cursor === "pointer"`.
- **Edge cases:** touch emulation shows no hover lift; no cluster box intersects another at any R76 viewport; the cluster's hover `transform` does not cancel the notes' tilts (each `.note` `rotate` unchanged while hovered).
- **Resources:** `intro.html` markup and CSS.

### R72. A copper thread draws itself pin to pin, Education to Philosophy to Practice, and never crosses note or label text.
- **Source:** [Pick-1] "connected by string"; [Card5] item 2 "the connecting string visual (color, style, does it draw itself)"; section 34.4.
- **Acceptance:** open the board: `#threads` is an `svg` with `aria-hidden="true"` inside `#board`, containing exactly 2 `path` elements, each with `pathLength="1"`, computed `stroke === "rgb(176, 112, 58)"`, `fill === "none"`, `strokeWidth` `2px` at 1440×900 and `1.75px` at 390×844; `viewBox === "0 0 " + B.clientWidth + " " + B.clientHeight`. Each path starts at its pin and ends at the next (path 0 start within 2px of the Education pin center, end within 2px of the Philosophy pin center; path 1 Philosophy to Practice; pin center = `.c-head` box top center + 1px at 1440×900, top-left + 6px at 390×844, from layout boxes). Draw: Seek 3300: both `strokeDashoffset` = 1; Seek 3600: path 0 strictly between 0 and 1; Seek 4300: both 0. Text safety, sampling 120 points along each path (`getPointAtLength`) at every R76 viewport: no point falls inside any `.note-face` box, and no point falls inside a `.c-head` box deeper than `parseFloat(getComputedStyle(cHead).paddingTop) − 4` px below its top edge; every point's x is ≥ 0 and ≤ `innerWidth`.
- **Edge cases:** resize from 1440×900 to 390×844 with the board open recomputes the `d` (stacked curve) and keeps the line complete; at rest no `stroke-dasharray` is applied (`getComputedStyle(path).strokeDasharray === "none"`); reduced motion shows both lines complete at t = 50ms.
- **Resources:** `intro.html` markup and CSS, `research-js` (`layout()`).

### R73. Each cluster is an honest stub: it goes to its final `#research-…` hash, announces "coming soon", and shows nothing else.
- **Source:** [Card5] item 4 "follow the same 'coming soon'-style pattern already established and Crit-verified"; [Card5] scope "Do NOT design what's behind Education/Philosophy/Practice yet"; section 36.1.
- **Acceptance:** open the board, set `window.__stay = 1`; for each cluster: `getAttribute('href')` is `#research-education`, `#research-philosophy`, `#research-practice` respectively; click it: within 300ms `location.hash` equals that href, `#board-status` (`role="status"`, `aria-live="polite"`) `textContent === "<Label> is coming soon. Still synthesizing."` (`Education`, `Philosophy`, `Practice`), `L.hidden === false`, `window.__stay === 1`, `document.getElementById('findings') === null`, and `document.querySelectorAll('section').length` is unchanged. Clicking the same cluster twice re-announces (status empty on the frame after the click, then refilled). Keyboard: focus a cluster, press Enter: same result. Each cluster has `aria-describedby="board-soon"`; `#board-soon` `textContent === "Coming soon."` and is visually hidden (bounding width ≤ 1px). No cluster has `aria-disabled`. `grep -ci "preventDefault" intro.html` = 0. Zero console errors and zero `Runtime.exceptionThrown` across the run.
- **Edge cases:** a direct load of `intro.html#research-philosophy` opens the board at rest (no wipe, `is-entering` never set) and announces `Philosophy is coming soon. Still synthesizing.` once; an unknown `#research-foo` opens the board at rest with no announcement; middle-click or Cmd-click opens the direct-load case in a new tab; the status line wraps inside the viewport at 320 wide (R76).
- **Resources:** `intro.html` markup, cluster click handler and router in `research-js`.

### R74. The future one-page shape is wired in now: all three links point into one page, never three routes, and the decision is recorded.
- **Source:** [Card5] "consider whether Education/Philosophy/Practice should also share one page, and make an explicit recommendation either way"; section 32.3 (product decision, Flag D1).
- **Acceptance:** `grep -oE 'href="#research-[a-z]+"' intro.html | sort -u` returns exactly the three hrefs in R73; `grep -cE 'href="[^"#]*(education|philosophy|practice)' intro.html` = 0; `git ls-files | grep -ciE "education|philosophy|practice"` = 0 (no new files); `grep -c "research-practice" docs/intro-experience-PRD.md` ≥ 1 (the 32.3 table exists); `BACKLOG.md` has an Open row for the research deep-dives containing `one page` and `#research-`.
- **Edge cases:** the router treats every `#research-` hash in one branch (not three); no element with id `findings` exists yet; the next card's diff should touch only that router branch, the new `#findings` section and the stub lines (verified on that card, not this one).
- **Resources:** `intro.html`, `BACKLOG.md`, this PRD.

### R75. With reduced motion, the board appears already assembled in one cut, nothing animates, and focus lands on the title.
- **Source:** [Card5] item 5 "notes appear already clustered, no motion"; section 36.3.
- **Acceptance:** with `prefers-reduced-motion: reduce` emulated, at the fork click research: within 100ms `L.hidden === false`, `L.classList.contains('is-entering') === false`, `document.activeElement.id === "research-title"`; at t = 50, 500 and 2000ms `L.getAnimations({subtree:true}).length === 0`; every note center is inside its own cluster box (as R70's rest check); every `.c-head` and `.board-head` opacity is `"1"`; both thread paths have `strokeDashoffset` 0 or `strokeDasharray === "none"`; each `.note` computed `rotate` equals `R[i]`; the R73 click check passes immediately. Switching emulation from no-preference to reduce at t ≈ 1500ms (mid-entry) lands the assembled board within 200ms with no `CSSAnimation` left in `L`.
- **Edge cases:** hover/focus lift still applies as an instant state change; skip link, Back and R29, R45 and R62 still pass; no WAAPI animation is created by `research-js` in any mode (`awk '/<script id="research-js">/,/<\/script>/' intro.html | grep -c "\.animate("` = 0).
- **Resources:** `intro.html` CSS, `research-js`.

### R76. The board fits one screen with no horizontal overflow at desktop, tablet, phone and landscape-phone sizes, stacking the clusters below 700px wide.
- **Source:** [Card5] item 6 "3 clusters side by side won't fit — stack vertically? One at a time?"; [Nick] original brief "desktop and mobile friendly"; section 36.2.
- **Acceptance:** at 1440×900, 1024×768, 768×1024, 390×844, 375×667, 320×568, 844×390 and 667×375, board open at rest, with `#board-status` showing the longest stub line (`Philosophy is coming soon. Still synthesizing.`): `document.documentElement.scrollWidth <= innerWidth`, `L.scrollWidth <= L.clientWidth`, `L.scrollHeight - L.clientHeight <= 1` (no scrolling needed), and the title, all three clusters and the status line are inside the viewport. `getComputedStyle(B.querySelector('.clusters')).gridTemplateColumns` has 3 tracks at 1440, 1024, 768, 844×390 and 667×375 and 1 track at 390, 375 and 320. At 390×844 each cluster's `.c-notes` shows 4 notes in one row (equal `top` within 4px). `.board-meta` is `display:none` at 375×667 and 320×568. `grep -c "dvh" intro.html` stays 0; `env(safe-area-inset-top)` and `env(safe-area-inset-bottom)` appear in the `.board` rule.
- **Edge cases:** rotating a phone with the board open re-lays out and redraws the thread (R72 resize edge); hover-only styles stay under `@media (hover:hover)`; iOS URL-bar changes don't shift the board (`svh`); every cluster ≥ 44px tall in both axes (it is ≥ 120px).
- **Resources:** `intro.html` CSS, `research-js` (`STACK`).

### R77. Screen-reader and keyboard users get one clean heading and three clean choices, with no sticky-note noise and no focus on moving or hidden content.
- **Source:** [Card5] item 7 "assistive tech gets a clean announcement of the three choices, not sticky-note visual noise"; section 36.4.
- **Acceptance:** keyboard only, at the fork: Tab to `research`, press Enter; by t ≈ 1500ms `document.activeElement.id === "research-title"`; while `is-entering`, `.clusters.inert === true` and `getComputedStyle(clusters).pointerEvents === "none"`; after the end step, Tab focuses `Education`, `Philosophy`, `Practice` in order; Shift+Tab from `Education` eventually focuses the skip link, which `elementFromPoint` confirms is on top. While open, `main.inert === true` and `.fork-scene.inert === true`. CDP `Accessibility.getFullAXTree`: a `region` named `Research, sorted.`; a `heading` level 2 with that name; a `group` with exactly three `link` nodes named exactly `Education`, `Philosophy`, `Practice`, each with description `Coming soon.`; a `status` node; and **no** AX node whose name contains any of the 12 note fragments, `Theme 0`, `Synthesis ·`, or `→`, and no `image`/`graphics-document` node from `#threads`.
- **Edge cases:** before the click, `#research` is `hidden` and absent from the AX tree; VoiceOver hears no "dimmed"; the visible focus ring shows on every cluster (`outlineStyle` not `none` on `:focus-visible`); the heading has no visible focus ring (`#research-title:focus` `outlineStyle === "none"`).
- **Resources:** `intro.html`.

### R78. Back, Forward and direct links work for `#research` and `#research-…`, and the passion branch's routing is unchanged.
- **Source:** sections 34.6, 32.4; extends R27, R48 and R50.
- **Acceptance:** (a) after R66, `history.back()`, wait 500ms: `location.hash === "#where"`, `L.hidden === true`, `.fork-scene.inert === false`, `document.activeElement` is the research prong, the curtain stays hidden, and `document.getAnimations().filter(a => /research-wipe|note-|head-stick|thread-draw|board-title/.test(a.animationName)).length === 0`; (b) `history.forward()`: the board is open at rest within 300ms with no `research-wipe` animation; (c) direct load of `intro.html#research`: within 600ms the board is open at rest, act two is open underneath (`#where.hidden === false`), `main.inert === true`, and the R6 nudge stays hidden after 4500ms; (d) from `#research-education`, `history.back()` returns to `#research` with `#board-status` empty and focus on the Education cluster; (e) Back twice from `#research` reaches the pill scene with R27(b) passing; (f) R48 and R50 pass unchanged (passion's four states), and opening `#nerd` or `#passions-gamer` never shows the research layer (`L.hidden === true`).
- **Edge cases:** Back during the entry aborts it cleanly (layer hidden, no orphaned research animations after 500ms); the router is idempotent across a `popstate` + `hashchange` pair; reloading on `#research` or any `#research-…` restores that state; `#researchfoo` (no hyphen) is not treated as research (act two closes per R27).
- **Resources:** main script router line, `research-js` router.

### R79. Palette, fonts, script budget and file footprint hold, and nothing earlier regresses.
- **Source:** R31, R49, R65; section 32.4.
- **Acceptance:** the R31 hex grep returns the same set as at 845f15a (**no new hex**); the Google Fonts URL is unchanged; `grep -c "<script" intro.html` = 4 and `grep -cE "<script[^>]+src=" intro.html` = 0; the main inline script is under 345 lines, `passions-js` under 280 lines, and `awk '/<script id="research-js">/,/<\/script>/' intro.html | wc -l` < 200; `grep -ci "preventDefault" intro.html` = 0; `git diff --name-only 845f15a..HEAD` lists only `intro.html`, `BACKLOG.md` and files under `docs/`; `git diff 845f15a..HEAD -- intro.html` touches the main script in at most the two places named in 34.6 (plus the research prong's `aria-describedby` removal in markup). All acceptance checks of R1 to R25, R27 to R41, R44 to R65 pass again, with the 32.4 amendments (R26 and R30 now apply to `technology` only; R33's describedby check applies to `technology` only; R65's script count is 4).
- **Edge cases:** no new font, image, CSS or JS files; no third-party code; act three's glitch and act four's backgrounds behave exactly as before; the passion prong still starts act three (R33).
- **Resources:** `intro.html`; `index.html` (read-only).

### 37.1 Deployment and build

Unchanged from sections 8, 18.1, 24.1 and 31.1: **not Docker**, by the same justified exception (static GitHub Pages site, nothing to containerize, production deploy is a push to `main`, which stays forbidden). Local preview `python3 docs/tools/serve.py 8000` from the repo root on `feature/intro-experience` (reuse the server on :8000 if it is already running). Demo URLs: `http://localhost:8000/intro.html#where` (then tap research) and `http://localhost:8000/intro.html#research` (the board at rest). No build step. The build card may push `feature/intro-experience` to origin. No ADR: one self-contained beat inside one file, cheap to reverse (section 4's reasoning).

### 37.2 Flags for Nick (addendum 4)

1. **D1, one shared page for Education, Philosophy and Practice.** You said this for the passions, not for research, so it's my call: one page, three sections in your order, like `#passions`. It reads as one story, reuses what's already built, and is one scroll on a phone. If you want three separate pages, the links change in three places.
2. **D2, the headline is "Research, sorted."** with the green period, plus a small label above it: "SYNTHESIS · 12 NOTES · 3 THEMES". My words. Change freely.
3. **D3, the sticky-note text is placeholder.** Generic method and mindset words (coursework, statistics, ask why, evidence first, interviews, usability tests…), deliberately not claims about your background. Swap in your own fragments any time; it's twelve words in the markup.
4. **D4, labels are capitalized:** Education, Philosophy, Practice. The fork's prongs are lowercase as you typed them. The capitals make the research board read a bit more formal. Say if you want them lowercase.
5. **D5, it's a whiteboard, not cork.** A dotted digital canvas (what a researcher actually synthesizes on now), with brass pins and one copper thread joining the three themes. No cork texture, no red conspiracy string. Notes are tinted in your site's greens, one tint per theme.
6. **D6, timing.** About 4 seconds end to end: notes drift in (1.5s), hold as a messy pile, sort themselves (1s), headers stick on, the thread draws, the title lands. Tap or press a key to skip.
7. **D7, stub copy.** "Practice is coming soon. Still synthesizing." is placeholder text.
8. **D8, real-device check.** Worth two minutes on your phone: the stacked layout and the thread down the left edge on a real iPhone. Emulation can't prove touch feel.

No new cost, services, infrastructure or recurring manual steps.

### 37.3 Feasibility (spike method) and risks

I ran a throwaway spike: one HTML page with the research layer, the board, the 12 notes plus 3 headers, `layout()`, the thread and the full animated sequence, served locally on port 8013 and measured in Chromium over CDP at eight viewports, with image checks of eleven screenshots (frames seeked to exact times). It lived in my scratch folder and is not in the repo. Every value it validated is written into sections 33 to 36.

| # | Given / When / Then | Verdict | Evidence |
|---|---|---|---|
| F23 | Given three clusters of 1 header + 4 notes, when laid out at 8 sizes from 1440×900 to 320×568 and 667×375, then the whole board plus the longest status line fits one screen with no overflow. | VALIDATED | `L` vertical and horizontal overflow 0 at all eight; status bottoms 732, 635, 738, 737, 590, 524, 351, 330 px. First pass failed twice: 320×568 overflowed by 47px (fixed by the stacked-and-short rules) and 667×375 by 185px (fixed by keeping the row layout on any screen ≤ 500px tall). No note text overflow anywhere. |
| F24 | Given the 34.4 thread geometry, when drawn on top of the notes, then it never crosses note text or header labels and stays on screen. | VALIDATED | 120-point sampling per path: 0 note hits at every size; deepest point inside a header 14px (theme line starts at 20px); leftmost x 4 to 5px in the stacked layout. The first stacked version (pin 20px in, 40px swing) crossed `coursework` and `ask why`; moving the pin to the corner and the swing to 32px fixed it. |
| F25 | Given an outer `.note` (sort) and inner `.note-face` (drift) using individual `translate`/`rotate` properties, when animated with the 34.3 delays, then it reads as an unsorted brain dump that then self-organizes into three clusters. | VALIDATED | Seek 2350: per-theme spread 0.46 to 0.70 of the viewport diagonal at 1440, 390, 320 and 844×390, all 12 centers on screen; Seek 4300: every note inside its own cluster. Image checks: scatter "an unsorted, mixed scatter rather than tidy columns"; final "a calm, professional synthesis board… three clearly labeled themes". The first scatter (4 × 3 over the cluster area, ±15%) was judged too regular and replaced. |
| F26 | Given two `pathLength="1"` paths, when `thread-draw` runs, then the thread draws itself and reads as string. | VALIDATED | `strokeDashoffset` at Seek 3300 / 3600 / 3800 / 4300: `[1,1]`, `[0.22,0.80]`, `[0,0.06]`, `[0,0]`. Image check: "the warm color, shallow sag, and circular attachment points make it read as a continuous physical thread". An earlier `--ink-soft` 1.5px version read as "a thin connecting rule", hence copper at 2px. |
| F27 | Given the stacked layout at 390 and 320 wide, when notes are 4 in a row, then the fragments stay legible. | PARTIAL | 14px (12px under 360) EB Garamond italic 500 fits every face with no overflow; an image check called it "readable, but borderline for comfortable scanning" at phone size. Acceptable because the notes are decoration and `aria-hidden`; the labels that matter are 22px. Real-device check is Flag D8. |

Risks:

- **Wall-clock timing tests are flaky in headless Chromium.** The spike's real-time screenshots trailed the animation clock by up to ~1.5s. Mitigated by defining "Seek T" and `getTiming()` checks (37 definitions, R67, R70, R72).
- **Hover transform vs. note animations:** handled by putting the entry animations on individual properties and the hover on `transform` of the cluster, and by `pointer-events:none` plus `inert` while entering.
- **Thread geometry depends on layout:** computed from layout boxes once per open and resize; a resize mid-entry re-runs `layout()`, which can make a note's scatter spot jump once. Accepted (rare, and the sequence is 4s).
- **Two scripts editing one router:** the main router gains one condition and `research-js` owns the rest, mirroring how `passions-js` coexists today. R78(f) re-checks passion routing.
- **Scope creep into the three sections:** the biggest practical risk for an AI builder. Sections 32.2, 32.3 and 37.4 rule it out.

### 37.4 Non-goals for addendum 4 (do not build)

- **Anything behind Education, Philosophy or Practice:** no `#findings` section, no content, no subsections, panels, modals, drawers, tooltips or expanding notes. A cluster only goes to its hash and announces "coming soon" (R73).
- Three separate routes, files or layers for the research sections (the future page is one page, 32.3).
- Any change to the `technology` prong (still a stub), act two's curtain or timings, the passion branch (acts three and four), the scroll intro, the nudge or the blue pill.
- More than 12 data notes, notes that are draggable or interactive, per-note links, per-note strings, a cork texture, red string, sound, particles, canvas, WebGL, SVG filters, a typewriter effect on the title, or any looping or idle animation after the end step.
- A visible exit or "straight to business" link on the board (same open question as Flag A6), a replay control, or persisting anything (cookies, storage) or analytics.
- New tokens or hex values, new font families or weights, `steps()` easing, the passion palette (`--pill-red`, `--pill-blue`, ember).
- Any change to `index.html`, the case-study pages, `resume.html`, `README.md`, `CNAME`, `AGENTS.md`, or new HTML, CSS, JS, image or font files. No JS libraries, CDN scripts or build tooling. No push to or merge into `main`, and no PR.

**Authorized boundaries (build card t_f25a55e9):** edit `intro.html` on `feature/intro-experience` in `~/Documents/github/portfolio` (markup, CSS, the two main-script lines in 34.6, and the new `research-js` block); update `BACKLOG.md` rows for this work; commit and `git push origin feature/intro-experience`; run or reuse the preview server on port 8000.

**Forbidden actions:** editing any other site file; pushing any other branch; committing to or merging into `main`; adding dependencies, files or services beyond the preview server.

### 37.5 Follow-ups (logged in BACKLOG.md, not requirements)

- **Research deep-dives:** build Education, Philosophy and Practice as **one page** (`#findings`, subsections `#research-education`, `#research-philosophy`, `#research-practice`), per 32.3, once Nick says what goes in each. Only the router branch and the stub lines change on the board.
- **Note fragments in Nick's words** (Flag D3).
- The **technology** prong (already logged).

---

## Research sources

- Josh W. Comeau, "Scroll-Driven Animations": https://www.joshwcomeau.com/animation/scroll-driven-animations/
- "Scroll-driven animations are Baseline at last" (Firefox 159, 2026-10-27; `overflow:clip` and shorthand pitfalls): https://dev.to/richicodes/scroll-driven-animations-are-baseline-at-last-3c8g
- Can I use, `animation-timeline: scroll()`: https://caniuse.com/mdn-css_properties_animation-timeline_scroll
- WCAG 2.2 Understanding 2.3.1, Three Flashes or Below Threshold: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html
- WCAG 2.2 Understanding 2.2.2, Pause, Stop, Hide: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
- MDN, `scroll-timeline` (named scroll progress timelines): https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-timeline
- MDN, `@property` (registered, animatable custom properties): https://developer.mozilla.org/en-US/docs/Web/CSS/@property
- MDN, `content` alternative text (`content: "x" / ""`): https://developer.mozilla.org/en-US/docs/Web/CSS/content
- GIPHY User Terms of Service (content generally for personal, non-commercial use within the Services; no copying or display elsewhere without permission) [GIPHY-ToS]: https://support.giphy.com/hc/en-us/articles/360020027752-GIPHY-User-Terms-of-Service
- GIPHY Help, "How to Find the Content You Want" (relevant channels shown at the top of search results) [GIPHY-search]: https://support.giphy.com/hc/en-us/articles/360019823451-How-to-Find-the-Content-You-Want
- GitHub Docs, DMCA Takedown Policy (about one business day to change content, else the repository is disabled) [GitHub-DMCA]: https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy
- web.dev, "Replace animated GIFs with video for faster page loads" (3.7 MB GIF to 551 KB MP4; `autoplay loop muted playsinline`) [web.dev-video]: https://web.dev/articles/replace-gifs-with-videos
- Chrome for Developers, Lighthouse "Use video formats for animated content": https://developer.chrome.com/docs/lighthouse/performance/efficient-animated-content
- MDN, individual transform properties `translate`, `rotate`, `scale` (they compose with `transform`; used for the note drift and sort): https://developer.mozilla.org/en-US/docs/Web/CSS/translate
- Skill: `tech-viability-and-platform-choice` (cheapest-first platform order: responsive web is sufficient here, no native app question; ADR proportionality; non-goals and edge cases).
