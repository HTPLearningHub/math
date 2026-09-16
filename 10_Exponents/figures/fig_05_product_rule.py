"""Figure 5 - why multiplying two powers adds the exponents.

Two boxes of x's are pushed together into one box. Nothing is taken away and
nothing is added, so the x's in the big box can only be the x's from the two
small boxes counted together: 2 + 3 = 5.

The figure never says "add the exponents" as an instruction. It shows the
counting, and lets the reader see that adding is the only thing that happens.
Run with:  python figures/fig_05_product_rule.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # the first power
ORANGE = "#E67E22"      # the second power
PURPLE = "#8E44AD"      # the exponent, and the count
GREY = "#78909C"
INK = "#212121"

W, H = 12.0, 5.75
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

SLOT = 0.56                                 # the width given to one x


def box(cx, cy, count, colour, label):
    """Draw `count` x's in a row inside a tinted box, with a label above it."""
    width = count * SLOT + 0.34
    ax.add_patch(FancyBboxPatch((cx - width / 2, cy - 0.40), width, 0.80,
                                boxstyle="round,pad=0.03,rounding_size=0.12",
                                facecolor=colour + "22", edgecolor=colour,
                                linewidth=1.8))
    for k in range(count):
        x = cx - (count - 1) * SLOT / 2 + k * SLOT
        ax.text(x, cy, r"$x$", ha="center", va="center", fontsize=21, color=INK)
    ax.text(cx, cy + 0.72, label, ha="center", va="center",
            fontsize=21, color=colour, fontweight="bold")
    ax.text(cx, cy - 0.74, f"{count} of them", ha="center", va="center",
            fontsize=13, color=GREY)
    return width


# the top row: two separate boxes, multiplied together
Y_TOP = 4.05
w1 = box(2.55, Y_TOP, 2, BLUE, r"$x^{2}$")
ax.text(4.35, Y_TOP, r"$\times$", ha="center", va="center", fontsize=28, color=INK)
w2 = box(6.35, Y_TOP, 3, ORANGE, r"$x^{3}$")

# the arrow down: the boxes are taken away, the x's are not
ax.annotate("", xy=(W / 2 - 1.3, 2.10), xytext=(W / 2 - 1.3, 2.90),
            arrowprops=dict(arrowstyle="-|>", color=GREY, linewidth=2.0,
                            mutation_scale=18))
ax.text(W / 2 - 1.05, 2.50, "push them into one box",
        ha="left", va="center", fontsize=14, color=GREY)

# the bottom row: one box, and the count
Y_BOT = 1.35
box(3.45, Y_BOT, 5, PURPLE, r"$x^{5}$")
ax.text(6.55, Y_BOT, r"$2 + 3 = 5$", ha="left", va="center",
        fontsize=23, color=PURPLE, fontweight="bold")
ax.text(6.55, Y_BOT - 0.74, "so the answer is $x$ five times over",
        ha="left", va="center", fontsize=13.5, color=GREY)

ax.text(W / 2, H - 0.30, r"$x^{2} \times x^{3} = x^{5}$",
        ha="center", va="center", fontsize=24, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_product_rule.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
