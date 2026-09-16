"""Figure 3 - a pair of opposites, and the distance from zero.

The same number line as Figure 2, with one pair of numbers marked: 5 and -5.
The two measuring arrows above the line have exactly the same length, which is
the whole message: a number and its opposite sit the same distance from zero,
one on each side. That shared length is the absolute value.

Run with:  python figures/fig_03_opposites.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # the positive number
ORANGE = "#E67E22"      # the negative number
GREY = "#78909C"        # zero and the line
INK = "#212121"

W, H = 12.8, 3.90
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LO, HI = -6, 6
LEFT, RIGHT = 1.20, W - 1.20
Y = 2.15                                   # the height of the line


def x_of(n):
    return LEFT + (n - LO) / (HI - LO) * (RIGHT - LEFT)


# the line with its ticks and labels
ax.annotate("", xy=(RIGHT + 0.55, Y), xytext=(LEFT - 0.55, Y),
            arrowprops=dict(arrowstyle="<|-|>", color=GREY, linewidth=2.0,
                            mutation_scale=22))
for n in range(LO, HI + 1):
    marked = n in (-5, 5)
    colour = GREY if n == 0 else (BLUE if n > 0 else ORANGE)
    ax.plot([x_of(n)] * 2, [Y - 0.18, Y + 0.18],
            color=colour, linewidth=2.6 if n == 0 else 1.6)
    ax.text(x_of(n), Y - 0.50, rf"${n}$", ha="center", va="center",
            fontsize=14 if not marked else 16, color=colour,
            fontweight="bold" if marked or n == 0 else "normal")

# the two marked points, drawn as filled circles so they stand out
for n, colour in ((-5, ORANGE), (5, BLUE)):
    ax.plot([x_of(n)], [Y], marker="o", markersize=13, color=colour, zorder=5)

# the two measuring arrows, both starting at zero, drawn at the same height
for n, colour, side in ((5, BLUE, "right"), (-5, ORANGE, "left")):
    ax.annotate("", xy=(x_of(n), Y + 0.62), xytext=(x_of(0), Y + 0.62),
                arrowprops=dict(arrowstyle="-|>", color=colour, linewidth=2.6,
                                mutation_scale=22))
    # the two short walls that show where the measurement starts and ends
    for end in (0, n):
        ax.plot([x_of(end)] * 2, [Y + 0.18, Y + 0.78],
                color=colour, linewidth=1.2, linestyle=(0, (3, 3)))
    ax.text(x_of(n / 2), Y + 0.98, "5 steps from zero", ha="center", va="center",
            fontsize=13.5, color=colour, fontweight="bold")

# the conclusion, written under the line
ax.text(x_of(-5), Y - 0.98, "the opposite of 5", ha="center", va="center",
        fontsize=13, color=ORANGE)
ax.text(x_of(5), Y - 0.98, r"the opposite of $-5$", ha="center", va="center",
        fontsize=13, color=BLUE)
ax.text(W / 2, 0.34,
        "Same distance, opposite directions. The distance is 5 for both.",
        ha="center", va="center", fontsize=14.5, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_opposites.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
