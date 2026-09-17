"""Figure 6 - a variable is a slot, and substituting is dropping a number in.

Top: the expression 3x + 2, with the x drawn as an empty dashed slot rather
than as a mysterious letter. This is the whole idea of evaluating: the letter
is a hole in the expression, and every value you choose fills the same hole.

Bottom: the same slot filled three times, with 1, 2 and 3, and the value that
comes out each time. The brackets around the filled number are drawn because
writing them is the habit that stops 3x from being read as 34.

Vertical layout, from the top down, so nothing lands on anything else:
  5.30  the expression with the empty slot
  4.45  the "x is the slot" pointer sits above it, at 6.05
  3.95  the dashed divider
  3.50  the heading of the lower half
  2.50  the three filled slots
  0.95  the three values
  0.25  the closing line

Run with:  python figures/fig_06_the_slot.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from pathlib import Path

BLUE = "#2E86DE"          # the variable and the value dropped into it
GREEN = "#1E8449"         # the value of the expression
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_GREEN = "#E8F5EC"

VALUES = [1, 2, 3]
RESULTS = [5, 8, 11]                   # 3*1+2, 3*2+2, 3*3+2

W, H = 12.60, 6.55
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# ============================================== the expression with the slot
Y_TOP = 5.30
ax.text(W / 2 - 1.55, Y_TOP, r"$3$", ha="center", va="center", fontsize=34,
        color=INK)
# the slot itself: a dashed empty box where the letter is
ax.add_patch(Rectangle((W / 2 - 1.28, Y_TOP - 0.46), 0.92, 0.92,
                       facecolor=TINT_BLUE, edgecolor=BLUE, linewidth=2.4,
                       linestyle=(0, (4, 3)), zorder=3))
ax.text(W / 2 + 0.55, Y_TOP, r"$+\; 2$", ha="center", va="center",
        fontsize=34, color=INK)
ax.text(W / 2 - 0.82, Y_TOP + 0.78, r"$x$ is the slot", ha="center",
        va="center", fontsize=17, color=BLUE, fontweight="bold")
ax.text(W / 2, Y_TOP - 0.90, r"the expression $3x + 2$", ha="center",
        va="center", fontsize=15, color=GREY, style="italic")

# a quiet line between the two halves
ax.plot([0.55, W - 0.55], [3.95, 3.95], color=GREY, linewidth=1.2,
        linestyle=(0, (4, 4)), zorder=1)

# ==================================================== the slot filled, thrice
COLS = [2.35, 6.30, 10.25]
Y_FILL = 2.50
Y_RESULT = 0.95
ax.text(0.55, 3.50, "the same slot, filled three times", ha="left",
        va="center", fontsize=17, color=BLUE, fontweight="bold")

for cx, v, r in zip(COLS, VALUES, RESULTS):
    ax.text(cx - 1.05, Y_FILL, r"$3$", ha="center", va="center", fontsize=27,
            color=INK)
    # the filled slot, now a solid box holding a real number
    ax.add_patch(FancyBboxPatch((cx - 0.79, Y_FILL - 0.37), 0.74, 0.74,
                                boxstyle="round,pad=0.04,rounding_size=0.10",
                                facecolor=TINT_BLUE, edgecolor=BLUE,
                                linewidth=2.2, zorder=3))
    ax.text(cx - 0.42, Y_FILL, f"${v}$", ha="center", va="center",
            fontsize=25, color=BLUE, zorder=4)
    # the brackets that must be written when a number replaces a letter
    ax.text(cx - 0.92, Y_FILL, r"$($", ha="center", va="center", fontsize=30,
            color=GREY, zorder=4)
    ax.text(cx + 0.09, Y_FILL, r"$)$", ha="center", va="center", fontsize=30,
            color=GREY, zorder=4)
    ax.text(cx + 0.78, Y_FILL, r"$+\; 2$", ha="center", va="center",
            fontsize=27, color=INK)
    # down to the value
    ax.add_patch(FancyArrowPatch((cx, Y_FILL - 0.62), (cx, Y_RESULT + 0.48),
                                 arrowstyle="-|>", mutation_scale=17,
                                 color=GREY, linewidth=1.8, zorder=2))
    ax.add_patch(FancyBboxPatch((cx - 0.80, Y_RESULT - 0.42), 1.60, 0.84,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=TINT_GREEN, edgecolor=GREEN,
                                linewidth=2.3, zorder=3))
    ax.text(cx, Y_RESULT, f"${r}$", ha="center", va="center", fontsize=25,
            color=GREEN, fontweight="bold", zorder=4)

ax.text(W / 2, 0.22, "one expression, one slot, three values",
        ha="center", va="center", fontsize=14.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_06_the_slot.png", dpi=170, facecolor="white")
print("saved", out / "fig_06_the_slot.png")
