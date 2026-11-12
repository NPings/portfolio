# PRD: Intro experience (scroll-driven walkthrough)

- **Project:** portfolio (nickpings.com), static HTML/CSS/JS, no build step, hosted on GitHub Pages
- **Branch:** `feature/intro-experience` (pushing this branch to origin is allowed as a backup, per Nick via Maestro 2026-11-12; GitHub Pages builds only from `main`. Never push to or merge into `main` without Nick's explicit approval.)
- **Card:** t_94229c29 (PRD). Build card: t_48cb87aa (assignee `design`)
- **Author:** product, 2026-11-12
- **Status:** Draft for Crit review, then Nick's approval
- **davinci-prd skill:** not installed on this Mac. Sections written by hand to the same structure.

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

- Anything behind "indulge me" beyond the R10 stub line (no new page, no scenes, no experience or work-philosophy content yet).
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

## Research sources

- Josh W. Comeau, "Scroll-Driven Animations": https://www.joshwcomeau.com/animation/scroll-driven-animations/
- "Scroll-driven animations are Baseline at last" (Firefox 159, 2026-10-27; `overflow:clip` and shorthand pitfalls): https://dev.to/richicodes/scroll-driven-animations-are-baseline-at-last-3c8g
- Can I use, `animation-timeline: scroll()`: https://caniuse.com/mdn-css_properties_animation-timeline_scroll
- Skill: `tech-viability-and-platform-choice` (cheapest-first platform order: responsive web is sufficient here, no native app question; ADR proportionality; non-goals and edge cases).
