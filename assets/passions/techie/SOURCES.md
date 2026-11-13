# techie: Snake demo

`snake.html` is the "built by my local AI setup" demo on `intro.html#passions-techie`.

## Where it came from
- Written by **Pi** (pi.dev coding agent CLI) running in the `pi-sandbox` Docker container on Nick's Mac, using **Strata** (local OpenAI-compatible model server on nick-server, model `qwen3.8-flash-next-gyro-gyro-m`). One prompt, card t_4b2a102b, 2026-11-13. Crit-passed as a standalone file (30,585 bytes, zero external references).
- The prompt asked for a single self-contained circuit-board Snake in the site's palette (`#16241C`, `#CFE2A6`, `#7E9C60`, `#F8FAF4`).

## What changed for the embed (card t_24928e8b, design)
Every edit is marked "embed addition" or "embed change" in the file. The game logic, renderer and look are Strata's.
- Transparent page background, so the host panel shows through.
- Fixed chrome sizes (12px type, no wrapping header or legend, short legend, no "/ pcb rev 21" sub-title), so the frame's height is its width + 86px (192px with the touch pad). `intro.html` sizes the iframe from those numbers before it loads.
- Touch pad (up/left/right/down, 48x44 hit areas) on touch-first devices (`(hover:none) and (pointer:coarse)`, or `?pad=1`), with "tap" wording in the overlays. When the host adds `.side` (phone held sideways), the pad sits beside the board.
- Board and overlay start a run on `click`, not `pointerdown`, so a finger that starts a page scroll on the board doesn't start a game. The board only blocks page scrolling (`touch-action:none`) while a run is going.
- `window.snake.steer('up'|'down'|'left'|'right')` added to the small embedder API.

## How the host keeps it polite (intro.html, passions-js)
- It's an `<iframe>`, same origin, `loading="lazy"`. Its key listener only hears keys while the frame has focus, so arrows and Space keep scrolling the page until someone clicks, taps or tabs into the game.
- Scrolling the frame under half out of view pauses the run and moves focus back to the techie heading. "Pause motion", hiding the tab, and leaving the passions layer also pause it.
