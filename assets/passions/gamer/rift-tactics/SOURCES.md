# gamer: Rift Tactics mission demo

`mission.mp4` is the boxed "my own game, in progress" demo on `intro.html#passions-gamer`. Unlike the six background clips one folder up (see `../SOURCES.md`), this footage is Nick's: Rift Tactics is his own side project (repo `~/Documents/github/rift-tactics`).

## Where it came from
- Captured by card t_a34fb333 (pi-ops), 2026-11-13: the current `main` build on the iOS Simulator (iPhone 16), recorded with `xcrun simctl io recordVideo --codec=h264`. A throwaway, uncommitted XCUITest played the mission with real taps (select, move, attack through the real combat forecast, Seal), no test-menu shortcuts.
- Mission m02, "Seal the Anchor". Won in 9 turns, 2 units lost. Starts on Player Phase, Turn 1 and ends on the real Victory screen.
- Trimmed and encoded with `ffmpeg -an -c:v libx264 -crf 26 -vf scale=720:-2 -movflags +faststart`: H.264, no audio track, 720x1562 (portrait), 72.6 s, 4,741,994 bytes.
- Flash check: `python3 docs/tools/flashcheck.py assets/passions/gamer/rift-tactics/mission.mp4` gives `frames=1741 transitions=1 max_flashes_per_second=0 PASS` (run by the capture card and again by its reviewer).

## Embed (card t_e7a41e17, design)
- `poster.jpg` is frame 1 (`-frames:v 1 -q:v 5`), so the still matches where the loop starts.
- The clip uses the gamer rotation's switches: it gets a `src` only when the gamer section is near, plays only while gamer is on screen in video mode, pauses with "Pause motion", a hidden tab or leaving the passions layer, and shows only its poster under reduced motion (until "Play motion") or Save-Data. If autoplay is blocked, it goes through the same `gUnlock` gesture recovery as the background clips.
- To swap in a newer capture: replace `mission.mp4` and `poster.jpg`, re-run the flash check, and update the mission line in the caption (`.g-meta`) and this file.
