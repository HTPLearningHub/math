"""Figure 3 - clearing a fraction, and where the brackets come from.

The bar under 2x - 6 divides that whole expression by 4. Multiplying both
sides by 4 undoes it on the left. On the right the multiplication has to
reach the whole side, and the only way to write that is with brackets -
which is the step readers leave out.

The brackets get their own orange highlight, because they are the point.

Horizontal plan (x):
    3.00  the left side
    5.40  the equals sign
    7.70  the right side  (the 4 at 6.80, the bracket at 7.95)

Vertical plan (y, top to bottom):
    4.60  heading
    3.70  the equation as it arrives
    3.22  the label that says the move is the same on both sides
    2.90  the two orange pills, joined by a dashed line
    2.60 -> 2.00  the two arrows down
    1.65  the equation with no fraction left
    0.85  what happened on each side
    0.25  closing note

Run with:  python figures/fig_03_clearing_the_fraction.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"        # the move being made
GREY = "#78909C"
INK = "#212121"
TINT_ORANGE = "#FDF0E3"

W, H = 10.80, 5.00
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT, MID, RIGHT = 3.00, 5.40, 7.70

ax.text(0.60, 4.60, "the bar divides, so multiply both sides by what is "
        "under it", ha="left", va="center", fontsize=19, color=INK,
        fontweight="bold")

# the equation as it arrives
ax.text(LEFT, 3.70, r"$\frac{2x - 6}{4}$", ha="center", va="center",
        fontsize=28, color=INK)
ax.text(MID, 3.70, r"$=$", ha="center", va="center", fontsize=26, color=INK)
ax.text(RIGHT, 3.70, r"$x - 4$", ha="center", va="center",
        fontsize=26, color=INK)

# the move, once under each side
ax.text(MID, 3.22, "the same move on both sides", ha="center", va="center",
        fontsize=13, color=GREY)
ax.plot([LEFT + 0.55, RIGHT - 0.55], [2.90, 2.90], linestyle=(0, (4, 4)),
        linewidth=1.6, color=ORANGE, zorder=2)
for xpos in (LEFT, RIGHT):
    ax.add_patch(FancyBboxPatch((xpos - 0.55, 2.60), 1.10, 0.60,
                                boxstyle="round,pad=0.04,rounding_size=0.28",
                                facecolor=TINT_ORANGE, edgecolor=ORANGE,
                                linewidth=2.0, zorder=3))
    ax.text(xpos, 2.90, r"$\times\,4$", ha="center", va="center",
            fontsize=19, color=ORANGE, zorder=4)
    ax.add_patch(FancyArrowPatch((xpos, 2.60), (xpos, 2.00),
                                 arrowstyle="-|>", mutation_scale=20,
                                 linewidth=2.6, color=ORANGE, zorder=5))

# the result. the bracket is highlighted because it is the whole lesson
ax.add_patch(FancyBboxPatch((7.95 - 0.80, 1.65 - 0.38), 1.60, 0.76,
                            boxstyle="round,pad=0.04,rounding_size=0.14",
                            facecolor=TINT_ORANGE, edgecolor=ORANGE,
                            linewidth=2.2, zorder=2))
ax.text(LEFT, 1.65, r"$2x - 6$", ha="center", va="center",
        fontsize=26, color=INK, zorder=4)
ax.text(MID, 1.65, r"$=$", ha="center", va="center", fontsize=26, color=INK)
ax.text(6.80, 1.65, r"$4$", ha="center", va="center",
        fontsize=26, color=INK, zorder=4)
ax.text(7.95, 1.65, r"$(x - 4)$", ha="center", va="center",
        fontsize=26, color=INK, zorder=4)

# what happened in each column
ax.text(LEFT, 0.85, r"the $4$ underneath is gone", ha="center", va="center",
        fontsize=14, color=GREY)
ax.text(7.70, 0.85, "the whole side is multiplied, so it needs brackets",
        ha="center", va="center", fontsize=14, color=ORANGE)

ax.text(0.60, 0.25, r"without the brackets, $4 \times x - 4$ multiplies only "
        r"the $x$ - a different equation, with a different answer",
        ha="left", va="center", fontsize=14, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_clearing_the_fraction.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_03_clearing_the_fraction.png")
