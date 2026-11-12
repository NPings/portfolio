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
