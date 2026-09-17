"""Figure 7 - what one very large value does to each measure.

The fireworks data: eight quiet days (seven of them with no fireworks at all,
one with a single firework) and July 4 with 500.

The number line is drawn to scale, so 500 really is that far away. Eight of
the nine days are packed into the far left of the picture, and the mean is
marked out on its own in empty space, where no day ever was. That gap IS the
lesson, and drawing it to scale is the only way to show it.

The median and the mode stay with the eight quiet days, because neither of
them cares how far away the ninth day is - only that it is last.

The one unusual value is drawn in purple. Purple is used nowhere else in this
chapter and is not the book's colour for a wrong answer: 500 is not a
mistake, it really happened.

Run with:  python figures/fig_07_one_big_value.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"          # the ordinary days
PURPLE = "#8E44AD"        # the one unusual value
ORANGE = "#E67E22"        # the mean
GREEN = "#1E8449"         # the median and the mode
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_PURPLE = "#F2E7F7"

QUIET = [0, 0, 0, 0, 0, 0, 0, 1]           # eight ordinary days
BIG = 500                                   # July 4
DATA = QUIET + [BIG]
MEAN = sum(DATA) / len(DATA)                # 55.666...

W, H = 13.20, 7.05
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT, RIGHT = 1.30, W - 1.15
AXIS_Y = 3.15
HI = 520.0                                  # a little room past 500


def x_of(v):
    """Position on the page of a value between 0 and 520, drawn to scale."""
    return LEFT + (v / HI) * (RIGHT - LEFT)


# ------------------------------------------------------------- the number line
ax.plot([LEFT - 0.30, RIGHT + 0.20], [AXIS_Y, AXIS_Y], color=GREY,
        linewidth=2.0, zorder=2)
for v in (0, 100, 200, 300, 400, 500):
    x = x_of(v)
    ax.plot([x, x], [AXIS_Y - 0.18, AXIS_Y], color=GREY, linewidth=1.6,
            zorder=2)
    # the 0 label steps aside, because the green marker runs through x = 0
    ax.text(x - 0.26 if v == 0 else x, AXIS_Y - 0.48, str(v), ha="center",
            va="center", fontsize=14, color=GREY)
ax.text((LEFT + RIGHT) / 2, AXIS_Y - 0.95, "fireworks in one day",
        ha="center", va="center", fontsize=13, color=GREY)

# --------------------------------------------- the eight quiet days, in a stack
for j in range(len(QUIET)):
    ax.add_patch(plt.Circle((x_of(0), AXIS_Y + 0.26 + j * 0.26), 0.125,
                            facecolor=TINT_BLUE, edgecolor=BLUE,
                            linewidth=1.8, zorder=4))
ax.text(x_of(0) - 0.15, 5.62,
        "eight quiet days\nseven with $0$, one with $1$", ha="left",
        va="center", fontsize=13, color=BLUE)

# ------------------------------------------------------------- July 4, far away
ax.add_patch(plt.Circle((x_of(BIG), AXIS_Y + 0.34), 0.24,
                        facecolor=TINT_PURPLE, edgecolor=PURPLE,
                        linewidth=2.6, zorder=4))
ax.text(x_of(BIG), AXIS_Y + 1.05, "July $4$\n$500$ fireworks", ha="center",
        va="center", fontsize=13, color=PURPLE, fontweight="bold")

# --------------------------------------------------- the mean, out on its own
mx = x_of(MEAN)
ax.plot([mx, mx], [0.60, 4.10], color=ORANGE, linewidth=2.6,
        linestyle=(0, (6, 3)), zorder=3)
ax.text(mx + 0.20, 4.35, r"mean $\approx 55.67$", ha="left", va="center",
        fontsize=15, color=ORANGE, fontweight="bold")

# -------------------------------------------- the median and the mode, unmoved
ax.plot([x_of(0), x_of(0)], [1.55, AXIS_Y], color=GREEN, linewidth=2.6,
        linestyle=(0, (6, 3)), zorder=3)
ax.text(x_of(0) + 0.22, 1.35,
        r"median $= 0$ and mode $= 0$ - both stay with the quiet days",
        ha="left", va="center", fontsize=14, color=GREEN, fontweight="bold",
        bbox=dict(facecolor="white", edgecolor="none", pad=2), zorder=6)

# the drag: from where the days actually are, out to where the mean landed
ax.annotate("", xy=(mx, 0.78), xytext=(x_of(0), 0.78),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, linewidth=2.6))
ax.text(mx + 0.28, 0.78,
        "one value dragged the mean out to here - no day was ever $55.67$",
        ha="left", va="center", fontsize=13, color=ORANGE)

# -------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.36, "One unusual value moves the mean, and nothing else",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.76,
        "the line is drawn to scale, so the empty space between the days and "
        "the mean is real",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_07_one_big_value.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
