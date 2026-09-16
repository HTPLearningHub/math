"""Figure 2 - the number line, continued to the left of zero.

The reader has already seen a number line in Chapter 1 and Chapter 2, but it
always started at zero. This one keeps going. Everything left of zero is drawn
in orange, everything right of zero in blue, and zero itself in grey, because
zero belongs to neither side.

The bottom arrow carries the rule the rest of the chapter depends on: the line
grows from small on the left to large on the right, all the way across.
Run with:  python figures/fig_02_number_line.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # positive numbers
ORANGE = "#E67E22"      # negative numbers
GREY = "#78909C"        # zero, and the line itself
PALE_B = "#EAF2FC"      # light blue band
PALE_O = "#FDF0E3"      # light orange band
INK = "#212121"

W, H = 13.0, 4.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LO, HI = -6, 6                             # the numbers that get a tick
LEFT, RIGHT = 1.05, W - 1.05               # where the drawn line starts and ends
Y = 2.30                                   # the height of the line itself


def x_of(n):
    """Turn a number into a position in inches along the line."""
    return LEFT + (n - LO) / (HI - LO) * (RIGHT - LEFT)


STEP = (RIGHT - LEFT) / (HI - LO)          # the distance between two whole numbers

# the two coloured bands, drawn first so everything else sits on top of them
ax.add_patch(FancyBboxPatch((x_of(LO) - 0.34, Y - 0.62), 6 * STEP + 0.34, 1.62,
                            boxstyle="round,pad=0.02,rounding_size=0.12",
                            facecolor=PALE_O, edgecolor="none"))
ax.add_patch(FancyBboxPatch((x_of(0), Y - 0.62), 6 * STEP + 0.34, 1.62,
                            boxstyle="round,pad=0.02,rounding_size=0.12",
                            facecolor=PALE_B, edgecolor="none"))

# the line, with an arrowhead at each end: it never stops in either direction
ax.annotate("", xy=(RIGHT + 0.62, Y), xytext=(LEFT - 0.62, Y),
            arrowprops=dict(arrowstyle="<|-|>", color=GREY, linewidth=2.0,
                            mutation_scale=22))

for n in range(LO, HI + 1):
    colour = GREY if n == 0 else (BLUE if n > 0 else ORANGE)
    size = 2.6 if n == 0 else 1.8
    ax.plot([x_of(n)] * 2, [Y - 0.20, Y + 0.20],
            color=colour, linewidth=size, solid_capstyle="round")
    ax.text(x_of(n), Y - 0.52, rf"${n}$", ha="center", va="center",
            fontsize=15, color=colour,
            fontweight="bold" if n == 0 else "normal")

# the names of the two halves, written inside their own band
ax.text(x_of(-3), Y + 0.72, "negative numbers", ha="center", va="center",
        fontsize=15.5, color=ORANGE, fontweight="bold")
ax.text(x_of(-3), Y + 0.36, "less than zero", ha="center", va="center",
        fontsize=12.5, color=ORANGE)
ax.text(x_of(3), Y + 0.72, "positive numbers", ha="center", va="center",
        fontsize=15.5, color=BLUE, fontweight="bold")
ax.text(x_of(3), Y + 0.36, "greater than zero", ha="center", va="center",
        fontsize=12.5, color=BLUE)

# zero gets its own label above the line, with a short arrow down to the tick
ax.annotate("", xy=(x_of(0), Y + 0.26), xytext=(x_of(0), Y + 1.30),
            arrowprops=dict(arrowstyle="-|>", color=GREY, linewidth=1.8,
                            mutation_scale=16))
ax.text(x_of(0), Y + 1.48, "zero: neither one nor the other",
        ha="center", va="center", fontsize=13, color=GREY, fontweight="bold")

# the rule of the whole chapter, along the bottom
ax.annotate("", xy=(RIGHT + 0.40, 0.72), xytext=(LEFT - 0.40, 0.72),
            arrowprops=dict(arrowstyle="-|>", color=INK, linewidth=2.2,
                            mutation_scale=22))
ax.text(LEFT - 0.40, 1.06, "smaller", ha="left", va="center",
        fontsize=14, color=INK, fontweight="bold")
ax.text(RIGHT + 0.40, 1.06, "larger", ha="right", va="center",
        fontsize=14, color=INK, fontweight="bold")
ax.text(W / 2, 0.34, "the further right, the greater the number",
        ha="center", va="center", fontsize=13, color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_number_line.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
