"""Figure 5 - the mode is the tallest stack.

The ten baseball values sorted into stacks, one stack per value. Each game is
one square, so the height of a stack is exactly how many times that value
happened.

The mode is found by looking, not by calculating, and the picture is built to
say that. The tallest stack is green; every other stack is blue. The two
values that never happened (4 and 6) keep their place on the axis with an
empty dash, so the reader can see that a stack of height zero is still a
possible value.

The height of each stack is written above it, which is the frequency table in
the chapter, drawn instead of listed.

Run with:  python figures/fig_05_mode.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path
from collections import Counter

BLUE = "#2E86DE"
GREEN = "#1E8449"         # the mode
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_GREEN = "#E8F5EC"

DATA = [0, 1, 1, 2, 2, 2, 3, 5, 5, 7]
COUNT = Counter(DATA)
LO, HI = min(DATA), max(DATA)
TOP = max(COUNT.values())                  # 3, the frequency of the mode
MODE = [v for v in COUNT if COUNT[v] == TOP][0]

W, H = 13.20, 6.45
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT, RIGHT = 1.35, W - 1.35
SLOT = (RIGHT - LEFT) / (HI - LO + 1)      # one column per possible value
BOX = SLOT * 0.62                          # one game, drawn as a square
BASE = 1.32                                # the ground the stacks stand on

for k, v in enumerate(range(LO, HI + 1)):
    cx = LEFT + k * SLOT + SLOT / 2
    n = COUNT.get(v, 0)
    edge = GREEN if v == MODE else BLUE
    face = TINT_GREEN if v == MODE else TINT_BLUE

    if n == 0:
        # a value that never happened still owns its place on the axis
        ax.plot([cx - BOX / 2, cx + BOX / 2], [BASE + 0.13, BASE + 0.13],
                color=GREY, linewidth=2.4, linestyle=(0, (4, 3)), zorder=3)
    for j in range(n):
        ax.add_patch(Rectangle((cx - BOX / 2, BASE + j * (BOX + 0.07)), BOX,
                               BOX, facecolor=face, edgecolor=edge,
                               linewidth=2.4, zorder=3))

    # how many times this value happened
    ax.text(cx, BASE + max(n, 1) * (BOX + 0.07) + 0.26, str(n), ha="center",
            va="center", fontsize=15,
            color=GREEN if v == MODE else GREY,
            fontweight="bold" if v == MODE else "normal")
    # the value itself, under the axis
    ax.text(cx, BASE - 0.44, str(v), ha="center", va="center", fontsize=17,
            color=GREEN if v == MODE else GREY,
            fontweight="bold" if v == MODE else "normal")

# the ground line and the two axis names
ax.plot([LEFT - 0.20, RIGHT + 0.20], [BASE, BASE], color=GREY, linewidth=2.0,
        zorder=2)
ax.text(W / 2, BASE - 0.96, "hits in one game", ha="center", va="center",
        fontsize=14, color=GREY)
ax.text(LEFT - 0.62, BASE + 1.55, "how many\ngames", ha="center",
        va="center", fontsize=13, color=GREY, rotation=90)

# the arrow that names the tallest stack
mode_x = LEFT + (MODE - LO) * SLOT + SLOT / 2
mode_top = BASE + TOP * (BOX + 0.07) + 0.60
ax.annotate("", xy=(mode_x, mode_top), xytext=(mode_x + 2.35, mode_top + 0.72),
            arrowprops=dict(arrowstyle="-|>", color=GREEN, linewidth=2.4,
                            connectionstyle="arc3,rad=0.18"))
ax.text(mode_x + 2.50, mode_top + 0.78,
        r"the tallest stack, so $\mathrm{mode} = 2$", ha="left", va="center",
        fontsize=17, color=GREEN, fontweight="bold")

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.36, "The mode is counted, not calculated",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.76,
        "one square for each of the ten games - the stack that is tallest "
        "names the mode",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_mode.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
