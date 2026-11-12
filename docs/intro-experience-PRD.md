# PRD: Intro experience (scroll-driven walkthrough)

- **Project:** portfolio (nickpings.com), static HTML/CSS/JS, no build step, hosted on GitHub Pages
- **Branch:** `feature/intro-experience` (pushing this branch to origin is allowed as a backup, per Nick via Maestro 2026-11-12; GitHub Pages builds only from `main`. Never push to or merge into `main` without Nick's explicit approval.)
- **Card:** t_94229c29 (PRD). Build card: t_48cb87aa (assignee `design`)
- **Author:** product, 2026-11-12
- **Status:** Draft for Crit review, then Nick's approval
- **davinci-prd skill:** not installed on this Mac. Sections written by hand to the same structure.
- **Addendum (2026-11-12):** sections 13 to 18 and requirements R16 to R32 add the pill-scene polish and the "indulge me" continuation (fork scene). Card t_fb2bf2d9 (PRD addendum), build card t_4749555c (assignee `design`). Where the addendum changes an earlier decision (R10, the section 11 non-goal about "indulge me", the section 4 JS budget, the R14 palette), it says so in section 13.3. Sections 1 to 12 are otherwise unchanged.

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

## Research sources

- Josh W. Comeau, "Scroll-Driven Animations": https://www.joshwcomeau.com/animation/scroll-driven-animations/
- "Scroll-driven animations are Baseline at last" (Firefox 159, 2026-10-27; `overflow:clip` and shorthand pitfalls): https://dev.to/richicodes/scroll-driven-animations-are-baseline-at-last-3c8g
- Can I use, `animation-timeline: scroll()`: https://caniuse.com/mdn-css_properties_animation-timeline_scroll
- Skill: `tech-viability-and-platform-choice` (cheapest-first platform order: responsive web is sufficient here, no native app question; ADR proportionality; non-goals and edge cases).
