"""Figure 6 - all four measures drawn on one data set.

The same ten baseball values as figure 1, with the range, the mean, the
median and the mode marked on top of them.

The picture answers a question the four separate sections cannot: where do
these numbers actually sit? The range is a width and is drawn as a width. The
mean, the median and the mode are positions along the same line, and are
drawn as lines through the data.

Here the median and the mode are both 2, so they share one green line. That
is worth seeing: when nothing unusual has happened, the three middles land
close together. Figure 7 is the same picture after one unusual value arrives,
and there they do not.

Run with:  python figures/fig_06_four_measures.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"          # the data
ORANGE = "#E67E22"        # the mean, and the range
GREEN = "#1E8449"         # the median and the mode
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"

DATA = [0, 1, 1, 2, 2, 2, 3, 5, 5, 7]
LO, HI = min(DATA), max(DATA)
MEAN = sum(DATA) / len(DATA)               # 2.8
MEDIAN = 2                                 # the fifth and sixth values are both 2
MODE = 2                                   # 2 happens three times

W, H = 13.20, 7.05
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT, RIGHT = 1.45, W - 1.45
AXIS_Y = 2.35
STEP = (RIGHT - LEFT) / (HI - LO)
DOT_R = 0.26


def x_of(v):
    return LEFT + (v - LO) * STEP


# ------------------------------------------------------------- the number line
ax.plot([LEFT - 0.55, RIGHT + 0.55], [AXIS_Y, AXIS_Y], color=GREY,
        linewidth=2.0, zorder=2)
for v in range(LO, HI + 1):
    x = x_of(v)
    ax.plot([x, x], [AXIS_Y - 0.18, AXIS_Y], color=GREY, linewidth=1.6,
            zorder=2)
    ax.text(x, AXIS_Y - 0.48, str(v), ha="center", va="center", fontsize=15,
            color=GREY)

# -------------------------------------------------------------------- the dots
seen = {}
for v in DATA:
    level = seen.get(v, 0)
    seen[v] = level + 1
    cy = AXIS_Y + 0.48 + level * 0.60
    ax.add_patch(plt.Circle((x_of(v), cy), DOT_R, facecolor=TINT_BLUE,
                            edgecolor=BLUE, linewidth=2.2, zorder=4))

# ------------------------------------------- the median and the mode, together
gx = x_of(MEDIAN)
ax.plot([gx, gx], [AXIS_Y, 5.05], color=GREEN, linewidth=2.6,
        linestyle=(0, (6, 3)), zorder=1)
ax.text(gx - 0.18, 5.28, r"median and mode, both $= 2$",
        ha="right", va="center", fontsize=15, color=GREEN, fontweight="bold")

# ------------------------------------------------------------------- the mean
ox = x_of(MEAN)
ax.plot([ox, ox], [AXIS_Y, 5.72], color=ORANGE, linewidth=2.6,
        linestyle=(0, (6, 3)), zorder=1)
ax.text(ox + 0.18, 5.95, r"mean $= 2.8$", ha="left", va="center", fontsize=15,
        color=ORANGE, fontweight="bold")

# ------------------------------------------------------- the range, as a width
ARROW_Y = 1.25
ax.annotate("", xy=(x_of(HI), ARROW_Y), xytext=(x_of(LO), ARROW_Y),
            arrowprops=dict(arrowstyle="<->", color=ORANGE, linewidth=2.6),
            zorder=5)
for v in (LO, HI):
    ax.plot([x_of(v), x_of(v)], [ARROW_Y, AXIS_Y], color=ORANGE,
            linewidth=1.1, linestyle=(0, (3, 3)), zorder=3)
ax.text((x_of(LO) + x_of(HI)) / 2, ARROW_Y - 0.44, r"range $= 7$",
        ha="center", va="center", fontsize=16, color=ORANGE,
        fontweight="bold",
        bbox=dict(facecolor="white", edgecolor="none", pad=2))
ax.text(W / 2, ARROW_Y - 0.92,
        "a width, not a place - it is the only one of the four that is not a "
        "point on the line",
        ha="center", va="center", fontsize=13, color=GREY)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.36, "The same ten games, described four ways",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_06_four_measures.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
