"""Figure 6 - why 5 - (-2) is 7.

A subtraction asks how far apart two numbers are. Here the two numbers sit on
opposite sides of zero, so the gap between them is the two steps up to zero
plus the five steps after it. Seven steps in total - more than the five you
started with, which is exactly why subtracting a negative makes a number grow.

The gap is drawn twice: once whole on the upper bracket, once in its two
pieces on the lower brackets.
Run with:  python figures/fig_06_subtracting_a_negative.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # positive numbers
ORANGE = "#E67E22"      # negative numbers
GREY = "#78909C"        # zero and the line
PURPLE = "#8E44AD"      # the whole gap
INK = "#212121"

W, H = 12.0, 4.25
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LO, HI = -3, 6
LEFT, RIGHT = 1.30, W - 1.30
Y = 1.45                                   # the height of the line


def x_of(n):
    return LEFT + (n - LO) / (HI - LO) * (RIGHT - LEFT)


# the line, its ticks and its labels
ax.annotate("", xy=(RIGHT + 0.50, Y), xytext=(LEFT - 0.50, Y),
            arrowprops=dict(arrowstyle="<|-|>", color=GREY, linewidth=1.9,
                            mutation_scale=21))
for n in range(LO, HI + 1):
    colour = GREY if n == 0 else (BLUE if n > 0 else ORANGE)
    ax.plot([x_of(n)] * 2, [Y - 0.17, Y + 0.17],
            color=colour, linewidth=2.6 if n == 0 else 1.5)
    ax.text(x_of(n), Y - 0.48, rf"${n}$", ha="center", va="center",
            fontsize=14, color=colour,
            fontweight="bold" if n in (-2, 5) else "normal")

# the two numbers of the subtraction
ax.plot([x_of(-2)], [Y], marker="o", markersize=13, color=ORANGE, zorder=5)
ax.plot([x_of(5)], [Y], marker="o", markersize=13, color=BLUE, zorder=5)


def bracket(a, b, height, colour, label, lw=2.2, fs=14):
    """Draw a measuring bracket from a to b at the given height."""
    ya = Y + height
    ax.plot([x_of(a), x_of(b)], [ya, ya], color=colour, linewidth=lw)
    for end in (a, b):
        ax.plot([x_of(end)] * 2, [ya - 0.13, ya + 0.13], color=colour, linewidth=lw)
    ax.text(x_of((a + b) / 2), ya + 0.30, label, ha="center", va="center",
            fontsize=fs, color=colour, fontweight="bold")


# the gap in its two pieces, then the same gap as one whole
bracket(-2, 0, 0.55, ORANGE, "2 steps", lw=1.9, fs=13)
bracket(0, 5, 0.55, BLUE, "5 steps", lw=1.9, fs=13)
bracket(-2, 5, 1.45, PURPLE, "7 steps in all")

# the thin dashed walls that join the points to the top bracket
for n in (-2, 5):
    ax.plot([x_of(n)] * 2, [Y + 0.20, Y + 1.42],
            color=PURPLE, linewidth=1.0, linestyle=(0, (3, 3)), zorder=1)

ax.text(W / 2, H - 0.30, r"$5 - (-2)$ asks: how far is it from $-2$ up to $5$?",
        ha="center", va="center", fontsize=16, color=INK, fontweight="bold")
ax.text(W / 2, 0.36, r"$2 + 5 = 7$, so $5 - (-2) = 7$",
        ha="center", va="center", fontsize=16, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_subtracting_a_negative.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
