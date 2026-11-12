# Gamer background clips: sources (takedown-ready manifest)

Six silent looping H.264 clips (plus a JPEG poster each) behind the `gamer` subsection of `intro.html` (act four, `#passions-gamer`). PRD sections 28.3 to 28.8, requirement R56. None of this footage is Nick's. The page shows the disclaimer "Game footage shown for fun. I don't own any of it. All rights belong to the games' developers and publishers." plus a "Now showing" credit for each clip.

Sourced 2026-11-12 by the design build card (t_24e05978). Conversion: the ffmpeg recipe in PRD 28.3 (no audio, at most 960 wide, 24 fps, `+faststart`, CRF 23 or 24; posters are frame 1 at `-q:v 5`). Every clip passed `python3 docs/tools/flashcheck.py <clip>` before it was committed, and every clip was checked by eye (frame strips) for face-cams, uploader watermarks, caption text, anime footage, gore and nudity.

| slug | game title | source page URL | uploader or channel | official (yes/no) | retrieved (date) | rating | clip KB | poster KB | flash check |
|---|---|---|---|---|---|---|---|---|---|
| borderlands | Borderlands 3 | https://giphy.com/gifs/xbox-gamescom-ix-inside-xbox-gM6VrJEwKnw1To4WRe | Xbox (verified GIPHY channel, @xbox) | yes (platform partner's channel, not Gearbox/2K) | 2026-11-12 | GIPHY pg | 641 | 56 | PASS (0 flashes/s) |
| pokemon | Pokémon Legends: Z-A | https://giphy.com/gifs/pokemon-battle-pokemonlegendsza-lumiosecity-E3WisBaRTDUIIDgQP9 | Pokémon (verified GIPHY channel, @pokemon) | yes | 2026-11-12 | GIPHY g | 621 | 59 | PASS (0 flashes/s) |
| fire-emblem | Fire Emblem Engage | https://tenor.com/view/fire-emblem-intelligent-systems-fantasy-game-alear-nintendo-switch-gif-12861340895003823266 | Tenor user Juks_Fanterisen | no | 2026-11-12 | not rated on Tenor; checked by eye, no gore or nudity | 646 | 21 | PASS (0 flashes/s) |
| smash-bros | Super Smash Bros. Ultimate | https://tenor.com/view/super-smash-bros-smash-bros-ultimate-brawl-melee-sephiroth-gif-19833631 | Tenor user Sapir12 | no | 2026-11-12 | not rated on Tenor; checked by eye, no gore or nudity | 753 | 37 | PASS (0 flashes/s) |
| destiny | Destiny 2: Beyond Light | https://tenor.com/view/destiny-destiny2-beyond-light-warlock-titan-gif-17896487 | Tenor user luke_zielke | no | 2026-11-12 | not rated on Tenor; checked by eye, no gore or nudity | 615 | 27 | PASS (1 flash/s) |
| baldurs-gate | Baldur's Gate 3 | https://giphy.com/gifs/larianstudios-larian-baldurs-gate-3-bg3-9r8vYpXxiZmWOxUAEi | Larian Studios (verified GIPHY channel, @larianstudios) | yes | 2026-11-12 | GIPHY g | 568 | 33 | PASS (0 flashes/s) |

Total for the twelve files: 4,352 KB (`du -ck *.mp4 *.jpg`), against a budget of 5,760 KB.

To take a clip down, delete `<slug>.mp4`, `<slug>.jpg`, its row here and its entry in `CLIPS` in `intro.html`. The rotation skips missing clips.

## Sourcing notes (why each pick)

- **borderlands:** the official Borderlands GIPHY channel only has trailer and character shots (with a big "BORDERLANDS 3" logo), no gameplay. This Xbox upload is real Borderlands 3 gameplay (a vehicle firefight, HUD visible). It carries a small "#INSIDEXBOX" mark in the top-right corner; I left it in rather than crop out the uploader's branding. Source is 1080 wide, scaled to 960.
- **pokemon:** official channel, Legends: Z-A overworld (a trainer and Chikorita on a Lumiose street). Trimmed to the first 6 s, before the clip cuts to a staged camera shot.
- **fire-emblem:** no clean Fire Emblem gameplay exists on an official GIPHY channel (searches return fan art, anime-style edits and news graphics). This Tenor upload is Engage's own tactical map, attack forecast and battle, with no added text. Source is only 498 wide, so it is soft at full screen; the 55% dim hides most of that. Trimmed to 8 s.
- **smash-bros:** the Nintendo-tagged GIPHY Smash clips are under 1 s and tiny. This Tenor upload is a clean Ultimate match (Sephiroth vs. Captain Falcon), no gamertags or face-cam. Trimmed to 3.5 s so it ends before the finishing-hit zoom and "GAME!" banner (the brightest part).
- **destiny:** every official Bungie GIPHY clip is a trailer, emote, armor showcase or has promo text over it ("TWILIGHT ARSENAL / NEW VOID SUPER", plus a "PRE-ALPHA FOOTAGE" watermark). This Tenor upload is clean first-person combat. The source is 2.3 s, so the file is that loop played twice (4.6 s) to meet the 3 to 8 s rule.
- **baldurs-gate:** official Larian channel, party exploration along a stream with the normal HUD. GIPHY's 1080 rendition of this upload returns a "content not available" card, so the clip uses the 480-wide rendition (soft at full screen).

Clips at or under 640 wide (fire-emblem, smash-bros, destiny, baldurs-gate) are worth replacing with sharper footage later, ideally Nick's own captures (PRD 28.8, logged in BACKLOG).
