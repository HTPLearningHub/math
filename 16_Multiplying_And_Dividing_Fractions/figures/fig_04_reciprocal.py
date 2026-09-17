"""Figure 4 - turning a fraction upside down, and why the product is 1.

Two halves.

The top half shows the swap itself on three examples: a fraction, a unit
fraction, and a whole number written over 1. Two curved arrows cross between
the top number and the bottom number, so the reader sees that nothing is
added or taken away - the two numbers simply change places.

The bottom half is the reason a fraction times its reciprocal is 1. The same
two numbers appear on top and underneath, so the answer is a number divided
by itself, and Chapter 1 already showed that this is one whole. The bar of
twelve cells, completely shaded, is that one whole.

Colours: blue is the fraction we start from, orange its reciprocal, green
the answer.

Run with:  python figures/fig_04_reciprocal.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"             # the fraction we start from
ORANGE = "#E67E22"           # its reciprocal
GREEN = "#1E8449"            # the answer, which is always 1
GREY = "#78909C"
INK = "#212121"

TINT = {BLUE: "#E9F2FC", ORANGE: "#FDF0E3", GREEN: "#E8F5EC"}

W, H = 12.60, 9.40
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def swap(cx, cy, top, bottom, caption):
    """One example of the flip: the fraction, two curved arrows, the flip."""
    # the fraction we start from, inside a pale blue card
    ax.add_patch(FancyBboxPatch((cx - 2.10, cy - 0.76), 1.50, 1.52,
                                boxstyle="round,pad=0.02,rounding_size=0.14",
                                facecolor=TINT[BLUE], edgecolor=BLUE,
                                linewidth=2.0, zorder=2))
    ax.text(cx - 1.35, cy + 0.34, top, ha="center", va="center", fontsize=23,
            color=INK, zorder=4)
    ax.plot([cx - 1.83, cx - 0.87], [cy, cy], color=INK, linewidth=1.8,
            zorder=4)
    ax.text(cx - 1.35, cy - 0.38, bottom, ha="center", va="center",
            fontsize=23, color=INK, zorder=4)

    # the two curved arrows that carry each number to the other place
    ax.add_patch(FancyArrowPatch((cx - 0.48, cy + 0.36), (cx + 1.18, cy - 0.40),
                                 connectionstyle="arc3,rad=-0.42",
                                 arrowstyle="-|>", mutation_scale=17,
                                 color=ORANGE, linewidth=2.0, zorder=5))
    ax.add_patch(FancyArrowPatch((cx - 0.48, cy - 0.40), (cx + 1.18, cy + 0.36),
                                 connectionstyle="arc3,rad=0.42",
                                 arrowstyle="-|>", mutation_scale=17,
                                 color=ORANGE, linewidth=2.0, zorder=5))

    # the reciprocal, inside a pale orange card
    ax.add_patch(FancyBboxPatch((cx + 1.32, cy - 0.76), 1.50, 1.52,
                                boxstyle="round,pad=0.02,rounding_size=0.14",
                                facecolor=TINT[ORANGE], edgecolor=ORANGE,
                                linewidth=2.0, zorder=2))
    ax.text(cx + 2.07, cy + 0.34, bottom, ha="center", va="center",
            fontsize=23, color=INK, zorder=4)
    ax.plot([cx + 1.59, cx + 2.55], [cy, cy], color=INK, linewidth=1.8,
            zorder=4)
    ax.text(cx + 2.07, cy - 0.38, top, ha="center", va="center", fontsize=23,
            color=INK, zorder=4)

    ax.text(cx + 3.05, cy, caption, ha="left", va="center", fontsize=12.5,
            color=GREY)


# --------------------------------------------------------- the three examples
ax.text(W / 2, H - 0.42, "A reciprocal is the same two numbers, swapped over",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.84,
        "nothing is added and nothing is thrown away - the top number goes "
        "underneath and the bottom number comes up",
        ha="center", va="center", fontsize=13, color=GREY)

LEFT = 2.95
swap(LEFT, 7.30, "3", "4", "an ordinary fraction")
swap(LEFT, 5.32, "1", "5", "a fraction with $1$ on top")
swap(LEFT, 3.34, "2", "1", "a whole number, written over $1$")

# the quiet line that names the third row's trick
ax.text(LEFT + 3.05, 2.88, r"because $2 = \frac{2}{1}$", ha="left",
        va="center", fontsize=12.5, color=ORANGE)

# a rule that separates the swap from the reason
ax.plot([0.90, W - 0.90], [2.20, 2.20], color=GREY, linewidth=1.2,
        linestyle=(0, (4, 3)))

# ------------------------------------- the bar of twelve cells: why it makes 1
BAR_X, BAR_W, BAR_H, BAR_Y = 4.40, 4.20, 0.52, 0.82
for i in range(12):
    ax.add_patch(Rectangle((BAR_X + i * BAR_W / 12, BAR_Y), BAR_W / 12, BAR_H,
                           facecolor=TINT[GREEN], edgecolor=GREEN,
                           linewidth=1.5, zorder=2))
ax.add_patch(Rectangle((BAR_X, BAR_Y), BAR_W, BAR_H, facecolor="none",
                       edgecolor=INK, linewidth=1.6, zorder=3))
ax.text(BAR_X + BAR_W + 0.28, BAR_Y + BAR_H / 2,
        "all $12$ of the $12$ pieces  $=$  one whole", ha="left", va="center",
        fontsize=13, color=GREEN)
ax.text(BAR_X - 0.28, BAR_Y + BAR_H / 2, r"$\frac{12}{12}$", ha="right",
        va="center", fontsize=21, color=GREEN)

ax.text(W / 2, 1.70,
        r"$\frac{3}{4} \times \frac{4}{3}"
        r" = \frac{3 \times 4}{4 \times 3} = \frac{12}{12} = 1$",
        ha="center", va="center", fontsize=21, color=INK)

ax.text(W / 2, 0.30,
        "the same two numbers end up on top and underneath, so the answer is "
        "always one whole",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_04_reciprocal.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
