"""Figure 6 - multiplying by splitting the number into its places.

345 is broken into 300 + 40 + 5, which is nothing more than the place value
split of Chapter 5. Each piece is multiplied by 6 on its own, and the three
answers are added at the end:

    6 x 345 = (6 x 300) + (6 x 40) + (6 x 5) = 1800 + 240 + 30 = 2070

This is a flow diagram, not an area model, because the three widths (300, 40
and 5) are far too different in size to draw side by side to scale - the 5
would be thinner than the line around it.

Three parts need three colours. Blue and orange are the chapter's usual pair;
purple is the third, used here and nowhere else.

Run with:  python figures/fig_06_place_value_split.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE, BLUE_FILL = "#2E86DE", "#EAF2FB"        # the hundreds
ORANGE, ORANGE_FILL = "#E67E22", "#FDF0E3"    # the tens
PURPLE, PURPLE_FILL = "#8E44AD", "#F4EAF8"    # the ones
INK = "#212121"

# one entry per place: the part, the product, its colours
PARTS = [(300, 1800, BLUE, BLUE_FILL),
         (40, 240, ORANGE, ORANGE_FILL),
         (5, 30, PURPLE, PURPLE_FILL)]

XC = [2.55, 6.00, 9.45]       # centre of each column
BW, BH = 2.45, 1.05           # box width and height
Y_TOP_BOX = 5.05              # bottom edge of the upper row of boxes
Y_LOW_BOX = 2.95              # bottom edge of the lower row of boxes

W, H = 12.0, 7.6

fig, ax = plt.subplots(figsize=(W, H))
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")


def box(xc, y_bottom, text, edge, fill, fontsize):
    """One rounded box with a number in it, centred on xc."""
    ax.add_patch(FancyBboxPatch((xc - BW / 2, y_bottom), BW, BH,
                                boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor=fill, edgecolor=edge, linewidth=2.2))
    ax.text(xc, y_bottom + BH / 2, text, ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color=edge)


ax.text(W / 2, 7.25, "Split 345 into its places, then multiply each place",
        ha="center", va="center", fontsize=18, fontweight="bold", color=INK)
ax.text(W / 2, 6.45, r"$345 = 300 + 40 + 5$", ha="center", va="center",
        fontsize=18, color=INK)

for xc, (part, product, edge, fill) in zip(XC, PARTS):
    box(xc, Y_TOP_BOX, str(part), edge, fill, 24)

    # the arrow that carries the piece down into its own multiplication
    ax.annotate("", xy=(xc, Y_LOW_BOX + BH + 0.10),
                xytext=(xc, Y_TOP_BOX - 0.10),
                arrowprops=dict(arrowstyle="-|>", color=edge, linewidth=2.2,
                                mutation_scale=18))
    ax.text(xc + 0.28, (Y_TOP_BOX + Y_LOW_BOX + BH) / 2, r"$\times 6$",
            ha="left", va="center", fontsize=15, color=edge)

    box(xc, Y_LOW_BOX, str(product), edge, fill, 24)

# the plus signs that join the three answers
for x in [(XC[0] + XC[1]) / 2, (XC[1] + XC[2]) / 2]:
    ax.text(x, Y_LOW_BOX + BH / 2, "+", ha="center", va="center",
            fontsize=26, color=INK)

ax.text(W / 2, 1.85, r"$1800 + 240 + 30 = 2070$", ha="center", va="center",
        fontsize=20, color=INK)
ax.text(W / 2, 0.85, r"$6 \times 345 = 2070$", ha="center", va="center",
        fontsize=22, fontweight="bold", color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_place_value_split.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
