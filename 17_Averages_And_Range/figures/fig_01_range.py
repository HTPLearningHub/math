"""Figure 1 - the range is the width of the data.

The ten baseball values drawn as a dot plot above a number line, with the
smallest and the largest value picked out, and an orange double arrow running
between them.

The point of the picture is that the range is a DISTANCE. The arrow has two
ends and the reader can see that it stretches from one end of the data to the
other. That is why the rule is a subtraction: a distance on a number line is
always the right-hand number minus the left-hand number.

Every value gets its own dot, so the reader also meets the data set that the
whole chapter uses, before any calculation happens.

Run with:  python figures/fig_01_range.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"          # the data values
ORANGE = "#E67E22"        # the range itself
GREY = "#78909C"          # the axis and quiet labels
INK = "#212121"
TINT_BLUE = "#E9F2FC"

DATA = [0, 1, 1, 2, 2, 2, 3, 5, 5, 7]
LO, HI = min(DATA), max(DATA)

W, H = 13.20, 6.35
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT, RIGHT = 1.45, W - 1.45          # where value 0 and value 7 sit
AXIS_Y = 2.55                          # height of the number line
STEP = (RIGHT - LEFT) / (HI - LO)      # width of one unit
DOT_R = 0.28                           # radius of one dot


def x_of(v):
    """Turn a data value into a position on the page."""
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
ax.text(W / 2, AXIS_Y - 0.98, "hits in one game", ha="center", va="center",
        fontsize=13, color=GREY)

# -------------------------------------------------------------------- the dots
# stack equal values on top of each other, so the picture also shows how often
# each value happened
seen = {}
for v in DATA:
    level = seen.get(v, 0)
    seen[v] = level + 1
    cy = AXIS_Y + 0.52 + level * 0.66
    edge = ORANGE if v in (LO, HI) else BLUE
    face = "#FDF0E3" if v in (LO, HI) else TINT_BLUE
    ax.add_patch(plt.Circle((x_of(v), cy), DOT_R, facecolor=face,
                            edgecolor=edge, linewidth=2.4, zorder=4))

# name the two values the range is built from
ax.text(x_of(LO), AXIS_Y + 1.50, "smallest\n$0$", ha="center", va="bottom",
        fontsize=14, color=ORANGE, fontweight="bold")
ax.text(x_of(HI), AXIS_Y + 1.50, "largest\n$7$", ha="center", va="bottom",
        fontsize=14, color=ORANGE, fontweight="bold")

# ------------------------------------------------------- the range, as an arrow
ARROW_Y = 0.88
ax.annotate("", xy=(x_of(HI), ARROW_Y), xytext=(x_of(LO), ARROW_Y),
            arrowprops=dict(arrowstyle="<->", color=ORANGE, linewidth=3.0),
            zorder=5)
# thin drop lines joining the arrow ends to the number line
for v in (LO, HI):
    ax.plot([x_of(v), x_of(v)], [ARROW_Y, AXIS_Y], color=ORANGE,
            linewidth=1.2, linestyle=(0, (3, 3)), zorder=3)
ax.text((x_of(LO) + x_of(HI)) / 2, ARROW_Y - 0.44,
        r"$\mathrm{range} = 7 - 0 = 7$", ha="center", va="center", fontsize=19,
        color=ORANGE, fontweight="bold",
        bbox=dict(facecolor="white", edgecolor="none", pad=2))

# ------------------------------------------------------------------- the titles
ax.text(W / 2, H - 0.40, "The range is the width of the data",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.82,
        "one dot for each of the ten games - the arrow runs from the smallest "
        "value to the largest",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_range.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
