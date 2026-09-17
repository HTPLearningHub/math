"""Figure 2 - the mean is what everyone gets when the total is shared equally.

Two rows of ten bars. The top row is what really happened: 0, 1, 1, 2, 2, 2,
3, 5, 5, 7 hits. The bottom row is the same total handed out again, but this
time in ten equal amounts.

This is the "why" of the mean, and it is the reason the rule is "add, then
divide". Adding collects the whole pile. Dividing shares the pile out. The
orange dashed line sits at 2.8 in both rows, so the reader can see the tall
bars in the top row being cut down to fill the short ones.

The total 28 is printed under both rows, because the one thing that must not
change when you share something out is how much there is.

Run with:  python figures/fig_02_mean_is_equal_sharing.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"          # what actually happened
GREEN = "#1E8449"         # the mean, the answer
ORANGE = "#E67E22"        # the level everything is cut down to
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_GREEN = "#E8F5EC"

DATA = [0, 1, 1, 2, 2, 2, 3, 5, 5, 7]
TOTAL = sum(DATA)                    # 28
N = len(DATA)                        # 10
MEAN = TOTAL / N                     # 2.8

W, H = 13.20, 8.45
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT, RIGHT = 1.05, W - 0.75
SLOT = (RIGHT - LEFT) / N            # one game's share of the width
BAR_W = SLOT * 0.70
UNIT = 0.340                         # page height of one hit
TOP_BASE = 4.35                      # baseline of the upper row
BOT_BASE = 1.35                      # baseline of the lower row


def draw_row(base, heights, edge, face, label_colour):
    """Draw one row of ten bars standing on the line y = base."""
    for i, v in enumerate(heights):
        x = LEFT + i * SLOT + (SLOT - BAR_W) / 2
        if v > 0:
            ax.add_patch(Rectangle((x, base), BAR_W, v * UNIT,
                                   facecolor=face, edgecolor=edge,
                                   linewidth=2.0, zorder=3))
        else:
            # a game with no hits still gets a slot, drawn as a flat dash
            ax.plot([x, x + BAR_W], [base, base], color=edge, linewidth=3.0,
                    zorder=3)
        txt = str(v) if float(v).is_integer() else f"{v}"
        ax.text(x + BAR_W / 2, base - 0.34, txt, ha="center", va="center",
                fontsize=13, color=label_colour)
    # the ground the bars stand on
    ax.plot([LEFT - 0.25, RIGHT + 0.10], [base, base], color=GREY,
            linewidth=1.8, zorder=2)


# --------------------------------------------------------------- the upper row
draw_row(TOP_BASE, DATA, BLUE, TINT_BLUE, GREY)
ax.text(LEFT - 0.25, TOP_BASE + 7 * UNIT + 0.45, "what actually happened",
        ha="left", va="center", fontsize=17, color=BLUE, fontweight="bold")
ax.text(LEFT - 0.25, TOP_BASE - 0.80,
        r"ten games, $28$ hits altogether", ha="left", va="center",
        fontsize=14, color=GREY)

# --------------------------------------------------------------- the lower row
draw_row(BOT_BASE, [MEAN] * N, GREEN, TINT_GREEN, GREY)
ax.text(LEFT - 0.25, BOT_BASE + MEAN * UNIT + 0.45,
        "the same hits, shared out equally",
        ha="left", va="center", fontsize=17, color=GREEN, fontweight="bold")
ax.text(LEFT - 0.25, BOT_BASE - 0.80,
        r"still ten games, still $28$ hits - so each share is $2.8$",
        ha="left", va="center", fontsize=14, color=GREY)

# ------------------------------------------- the level line, drawn in both rows
for base in (TOP_BASE, BOT_BASE):
    y = base + MEAN * UNIT
    ax.plot([LEFT - 0.25, RIGHT + 0.10], [y, y], color=ORANGE, linewidth=2.2,
            linestyle=(0, (5, 4)), zorder=6)
ax.text(RIGHT + 0.14, TOP_BASE + MEAN * UNIT, r"$2.8$", ha="left",
        va="center", fontsize=15, color=ORANGE, fontweight="bold")
ax.text(RIGHT + 0.14, BOT_BASE + MEAN * UNIT, r"$2.8$", ha="left",
        va="center", fontsize=15, color=ORANGE, fontweight="bold")

# -------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.38, "The mean is an equal share",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.78,
        "the part of each tall bar that sticks above the orange line is "
        "exactly what the short bars are missing",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_02_mean_is_equal_sharing.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
