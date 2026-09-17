"""Figure 6 - the greatest common factor of two terms, read off the bricks.

Each term is broken into the pieces it is multiplied from. The pieces both
terms own are drawn first, in green, so they line up in the same two columns.
Whatever is left sits in the last column.

The green columns are the greatest common factor, 3x. The last column is what
goes inside the bracket. This is Chapter 14's brick picture with letters added
to it, and a letter behaves exactly like a prime: take it as often as the term
that has it least.

The brick columns are 1.50 apart and the bricks are 1.10 wide, so there is a
0.40 gap for the multiplication dot. A narrower gap swallows the dot.

Vertical plan (y, from the top):
    5.45  heading over the bricks
    4.40  row one, the bricks of 3x^2
    3.25  row two, the bricks of 6x
    2.28  the two column labels, clear of the green band's edge at 2.64
    1.95  the divider
    1.30  the finished line of maths
    0.88  the two underlines
    0.46  the two short labels

Run with:  python figures/fig_06_gcf_of_two_terms.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"
ORANGE = "#E67E22"
GREEN = "#1E8449"         # shared, and this chapter's answer
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"

W, H = 12.80, 5.90
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

COL = [4.30, 5.80, 7.30]  # the three brick columns
ROW = [4.40, 3.25]        # the two term rows
BW, BH = 1.10, 0.90       # brick width and height

# the green band behind the two shared columns, drawn before the bricks
ax.add_patch(FancyBboxPatch((COL[0] - BW / 2 - 0.16, ROW[1] - BH / 2 - 0.16),
                            (COL[1] - COL[0]) + BW + 0.32,
                            (ROW[0] - ROW[1]) + BH + 0.32,
                            boxstyle="round,pad=0.04,rounding_size=0.16",
                            facecolor=TINT_GREEN, edgecolor=GREEN,
                            linewidth=2.0, linestyle=(0, (5, 4)), zorder=1))


def brick(cx, cy, text, colour, tint):
    ax.add_patch(FancyBboxPatch((cx - BW / 2, cy - BH / 2), BW, BH,
                                boxstyle="round,pad=0.03,rounding_size=0.12",
                                facecolor=tint, edgecolor=colour,
                                linewidth=2.2, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=24, color=INK,
            zorder=4)


ax.text(6.00, 5.45, "break each term into the pieces it is multiplied from",
        ha="center", va="center", fontsize=19, color=INK, fontweight="bold")

# --------------------------------------------------- row one: 3x^2 = 3 . x . x
ax.text(2.30, ROW[0], r"$3x^{2}$", ha="right", va="center", fontsize=27,
        color=INK)
ax.text(3.05, ROW[0], r"$=$", ha="center", va="center", fontsize=24,
        color=GREY)
brick(COL[0], ROW[0], r"$3$", GREEN, TINT_GREEN)
brick(COL[1], ROW[0], r"$x$", GREEN, TINT_GREEN)
brick(COL[2], ROW[0], r"$x$", BLUE, TINT_BLUE)

# ----------------------------------------------------- row two: 6x = 2 . 3 . x
ax.text(2.30, ROW[1], r"$6x$", ha="right", va="center", fontsize=27,
        color=INK)
ax.text(3.05, ROW[1], r"$=$", ha="center", va="center", fontsize=24,
        color=GREY)
brick(COL[0], ROW[1], r"$3$", GREEN, TINT_GREEN)
brick(COL[1], ROW[1], r"$x$", GREEN, TINT_GREEN)
brick(COL[2], ROW[1], r"$2$", ORANGE, TINT_ORANGE)

# the dots that say the bricks are multiplied, not added
for cy in ROW:
    for i in range(2):
        # a drawn dot, not a mathtext one: \cdot renders far too small here
        ax.plot([(COL[i] + COL[i + 1]) / 2], [cy], marker="o", markersize=7,
                color=GREY, zorder=4)

ax.text((COL[0] + COL[1]) / 2, 2.28, "in both terms", ha="center",
        va="center", fontsize=16, color=GREEN)
ax.text(COL[2], 2.28, "in one only", ha="center", va="center", fontsize=16,
        color=GREY)

# --------------------------------------------------------- the finished line
ax.plot([0.60, W - 0.60], [1.95, 1.95], color=GREY, linewidth=1.2,
        linestyle=(0, (4, 4)), zorder=1)

ax.text(3.00, 1.30, r"$3x^{2} + 6x$", ha="center", va="center", fontsize=28,
        color=INK)
ax.text(5.05, 1.30, r"$=$", ha="center", va="center", fontsize=26, color=GREY)
ax.text(6.30, 1.30, r"$3x$", ha="center", va="center", fontsize=28,
        color=GREEN, fontweight="bold")
ax.text(8.15, 1.30, r"$(x + 2)$", ha="center", va="center", fontsize=28,
        color=INK)

ax.plot([5.85, 6.75], [0.88, 0.88], color=GREEN, linewidth=3.0)
ax.text(6.30, 0.46, "shared", ha="center", va="center", fontsize=15,
        color=GREEN)
ax.plot([7.25, 9.05], [0.88, 0.88], color=GREY, linewidth=3.0)
ax.text(8.15, 0.46, "left over", ha="center", va="center", fontsize=15,
        color=GREY)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_06_gcf_of_two_terms.png", dpi=170, facecolor="white",
            bbox_inches="tight")
print("saved", out / "fig_06_gcf_of_two_terms.png")
