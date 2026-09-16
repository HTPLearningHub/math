"""Figure 1 - multiplication repeats an addition, a power repeats a multiplication.

The two sides are built the same way on purpose: the same two numbers, 2 and
3, doing the same two jobs. Blue is always the number that gets used. Purple
is always the count of how many times it gets used.

The point the reader must see is that the two numbers swap places. In 3 x 2
the count is written first; in 2^3 the count is written last, up in the
corner. Same pair of jobs, opposite order.

Note: mathtext cannot colour one digit inside a string, so the short form on
each side is drawn digit by digit, not as one expression.
Run with:  python figures/fig_01_repeated.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # the number that gets used
PURPLE = "#8E44AD"      # how many times it gets used
GREY = "#78909C"        # quiet labels and the divider
INK = "#212121"

W, H = 12.2, 5.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT, RIGHT = W * 0.25, W * 0.75           # the middle of each half
Y_TERM = 3.38                              # the height of the short form on both sides


def panel(cx, heading, spelled, answer, tint):
    """Draw the parts that are identical on both sides: strip, words, answer."""
    ax.add_patch(FancyBboxPatch((cx - 2.55, 4.24), 5.10, 0.62,
                                boxstyle="round,pad=0.02,rounding_size=0.14",
                                facecolor=tint, edgecolor="none"))
    ax.text(cx, 4.55, heading, ha="center", va="center",
            fontsize=16.5, color=INK, fontweight="bold")
    ax.text(cx, 2.38, spelled, ha="center", va="center", fontsize=15, color=GREY)
    ax.text(cx, 1.42, answer, ha="center", va="center", fontsize=26, color=INK)


panel(LEFT, "Multiplication is repeated addition",
      "add the 2, three times",
      r"$2 + 2 + 2 \; = \; 6$", "#EAF2FC")

panel(RIGHT, "A power is repeated multiplication",
      "multiply the 2, three times",
      r"$2 \times 2 \times 2 \; = \; 8$", "#F3EAF8")

# the short form on the left: count, times sign, number
ax.text(LEFT - 0.62, Y_TERM, "3", ha="center", va="center",
        fontsize=44, color=PURPLE, fontweight="bold")
ax.text(LEFT, Y_TERM, r"$\times$", ha="center", va="center",
        fontsize=34, color=INK)
ax.text(LEFT + 0.62, Y_TERM, "2", ha="center", va="center",
        fontsize=44, color=BLUE, fontweight="bold")

# the short form on the right: number, then the count raised into the corner
ax.text(RIGHT - 0.28, Y_TERM, "2", ha="center", va="center",
        fontsize=44, color=BLUE, fontweight="bold")
ax.text(RIGHT + 0.16, Y_TERM + 0.30, "3", ha="center", va="center",
        fontsize=26, color=PURPLE, fontweight="bold")

# the divider between the two halves
ax.plot([W / 2] * 2, [0.95, 4.90], color=GREY, linewidth=1.1,
        linestyle=(0, (4, 4)))

# the key, and the sentence that the whole figure exists to say
ax.text(W / 2, 0.58,
        "blue = the number being used        purple = how many times",
        ha="center", va="center", fontsize=14, color=GREY)
ax.text(W / 2, 0.20,
        "The count is written first in a multiplication, and last in a power.",
        ha="center", va="center", fontsize=15, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_repeated.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
