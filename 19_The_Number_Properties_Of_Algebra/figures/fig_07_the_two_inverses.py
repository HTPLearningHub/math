"""Figure 7 - the two ways of cancelling a number.

Top: adding the opposite. A walk of five steps to the right, then five steps
back to the left, lands on zero. That is Chapter 9's number-line walk used to
show that a + (-a) = 0.

Bottom: multiplying by the reciprocal. Five unit squares, and one fifth of
five squares is one square. That is a * (1/a) = 1.

The two rows share a layout on purpose: an amount on the left, an orange
operation, and the identity element in green.

The number line starts at x = 2.40 so that "back at zero" fits to the left of
it, and one step is only 0.95 wide so that the line ends well before the two
formulas at x = 10.70. The arc over a 4.75 span with rad 0.30 rises about
0.71, so the arc labels sit 1.38 above and below the line.

Vertical plan (y, from the top):
    6.15  heading of the top row
    5.68  the "+5" label, above the top of the arc at 5.23
    4.30  the number line
    2.92  the "+(-5)" label, below the bottom of the arc at 3.37
    2.50  the divider
    2.20  heading of the bottom row
    1.95  the upper formula
    1.10  the bottom edge of the squares
    0.95  the "take one fifth" label, under the arrow
    0.72  the labels under the squares
    0.55  the lower formula

Run with:  python figures/fig_07_the_two_inverses.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
from pathlib import Path

BLUE = "#2E86DE"          # the amount you start with
ORANGE = "#E67E22"        # the thing that undoes it
GREEN = "#1E8449"         # where you land: 0, or 1
GREY = "#78909C"
INK = "#212121"
TINT_GREEN = "#E8F5EC"
TINT_BLUE = "#E9F2FC"

W, H = 12.80, 6.50
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# ======================================================= top: the opposite
ax.text(0.40, 6.15, "adding the opposite lands you on zero", ha="left",
        va="center", fontsize=19, color=GREEN, fontweight="bold")

LINE_Y = 4.30
X0, STEP = 2.40, 0.95     # the position of 0, and the width of one unit
ax.plot([X0 - 0.70, X0 + 6.4 * STEP], [LINE_Y, LINE_Y], color=GREY,
        linewidth=2.0, zorder=2)
for n in range(0, 7):
    x = X0 + n * STEP
    ax.plot([x, x], [LINE_Y - 0.13, LINE_Y + 0.13], color=GREY, linewidth=1.8,
            zorder=2)
    ax.text(x, LINE_Y - 0.44, str(n), ha="center", va="center", fontsize=15,
            color=GREY)

# out to 5, above the line
ax.add_patch(FancyArrowPatch((X0, LINE_Y + 0.20),
                             (X0 + 5 * STEP, LINE_Y + 0.20),
                             connectionstyle="arc3,rad=-0.30",
                             arrowstyle="-|>", mutation_scale=22,
                             linewidth=2.6, color=BLUE, zorder=3))
ax.text(X0 + 2.5 * STEP, LINE_Y + 1.38, r"$+5$", ha="center", va="center",
        fontsize=22, color=BLUE)

# and back to 0, below the line
ax.add_patch(FancyArrowPatch((X0 + 5 * STEP, LINE_Y - 0.20),
                             (X0, LINE_Y - 0.20),
                             connectionstyle="arc3,rad=-0.30",
                             arrowstyle="-|>", mutation_scale=22,
                             linewidth=2.6, color=ORANGE, zorder=3))
ax.text(X0 + 2.5 * STEP, LINE_Y - 1.38, r"$+\,(-5)$", ha="center",
        va="center", fontsize=22, color=ORANGE)

ax.plot([X0], [LINE_Y], marker="o", markersize=13, color=GREEN, zorder=5)
ax.text(X0 - 0.85, LINE_Y + 0.35, "back\nat zero", ha="right", va="center",
        fontsize=15, color=GREEN, fontweight="bold")

ax.text(10.70, LINE_Y + 0.60, r"$5 + (-5) = 0$", ha="center", va="center",
        fontsize=27, color=INK)
ax.text(10.70, LINE_Y - 0.60, r"$a + (-a) = 0$", ha="center", va="center",
        fontsize=27, color=GREEN)

ax.plot([0.40, W - 0.40], [2.50, 2.50], color=GREY, linewidth=1.2,
        linestyle=(0, (4, 4)), zorder=1)

# ==================================================== bottom: the reciprocal
ax.text(0.40, 2.20, "multiplying by the reciprocal lands you on one",
        ha="left", va="center", fontsize=19, color=GREEN, fontweight="bold")

SQ, BOT = 0.72, 1.10      # the side of one unit square, and its bottom edge
for i in range(5):
    ax.add_patch(Rectangle((1.05 + i * (SQ + 0.10), BOT), SQ, SQ,
                           facecolor=TINT_BLUE, edgecolor=BLUE,
                           linewidth=2.0, zorder=3))
ax.text(1.05 + 2 * (SQ + 0.10) + SQ / 2, BOT - 0.38, r"$5$", ha="center",
        va="center", fontsize=19, color=BLUE)

ax.add_patch(FancyArrowPatch((5.55, BOT + SQ / 2), (7.05, BOT + SQ / 2),
                             arrowstyle="-|>", mutation_scale=22,
                             linewidth=2.4, color=ORANGE, zorder=3))
# the label goes UNDER the arrow: the bottom heading runs to about x = 7.0
ax.text(6.30, 0.95, r"take $\frac{1}{5}$ of it", ha="center", va="center",
        fontsize=17, color=ORANGE)

ax.add_patch(Rectangle((7.45, BOT), SQ, SQ, facecolor=TINT_GREEN,
                       edgecolor=GREEN, linewidth=2.4, zorder=3))
ax.text(7.45 + SQ / 2, BOT - 0.38, r"$1$", ha="center", va="center",
        fontsize=19, color=GREEN, fontweight="bold")

ax.text(10.70, 1.95, r"$5 \times \frac{1}{5} = 1$", ha="center", va="center",
        fontsize=25, color=INK)
ax.text(10.70, 0.85, r"$a \times \frac{1}{a} = 1 \;\;(a \neq 0)$",
        ha="center", va="center", fontsize=25, color=GREEN)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_07_the_two_inverses.png", dpi=170, facecolor="white",
            bbox_inches="tight")
print("saved", out / "fig_07_the_two_inverses.png")
