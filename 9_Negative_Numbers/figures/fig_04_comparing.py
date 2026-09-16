"""Figure 4 - comparing two negative numbers.

The picture answers one question: which is greater, -5 or -2? The rule is read
straight off the line - the number further right is the greater one - and the
money labels under the two points say why that agrees with common sense.

The two boxes at the bottom set the wrong answer beside the right one, because
this is the single commonest mistake with negative numbers.
Run with:  python figures/fig_04_comparing.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # positive numbers
ORANGE = "#E67E22"      # negative numbers, and the two marked points
GREY = "#78909C"        # zero and the line
GREEN = "#1E8449"       # the right answer
RED = "#C0392B"         # the wrong answer
INK = "#212121"

W, H = 12.4, 4.40
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LO, HI = -7, 2
LEFT, RIGHT = 1.30, W - 1.30
Y = 3.05                                   # the height of the line


def x_of(n):
    return LEFT + (n - LO) / (HI - LO) * (RIGHT - LEFT)


ax.annotate("", xy=(RIGHT + 0.55, Y), xytext=(LEFT - 0.55, Y),
            arrowprops=dict(arrowstyle="<|-|>", color=GREY, linewidth=2.0,
                            mutation_scale=22))
for n in range(LO, HI + 1):
    colour = GREY if n == 0 else (BLUE if n > 0 else ORANGE)
    ax.plot([x_of(n)] * 2, [Y - 0.18, Y + 0.18],
            color=colour, linewidth=2.6 if n == 0 else 1.6)
    ax.text(x_of(n), Y - 0.50, rf"${n}$", ha="center", va="center",
            fontsize=14, color=colour,
            fontweight="bold" if n in (-5, -2, 0) else "normal")

# the two numbers being compared
for n in (-5, -2):
    ax.plot([x_of(n)], [Y], marker="o", markersize=14, color=ORANGE, zorder=5)

# the move from the smaller number to the greater one, drawn above the line
ax.annotate("", xy=(x_of(-2), Y + 0.66), xytext=(x_of(-5), Y + 0.66),
            arrowprops=dict(arrowstyle="-|>", color=INK, linewidth=2.6,
                            mutation_scale=22))
for n in (-5, -2):
    ax.plot([x_of(n)] * 2, [Y + 0.18, Y + 0.82],
            color=INK, linewidth=1.1, linestyle=(0, (3, 3)))
ax.text(x_of(-3.5), Y + 1.02, "further right, so greater", ha="center",
        va="center", fontsize=14, color=INK, fontweight="bold")

# what the two numbers mean in money
ax.text(x_of(-5), Y - 1.00, "you owe 5", ha="center", va="center",
        fontsize=13, color=ORANGE, fontweight="bold")
ax.text(x_of(-2), Y - 1.00, "you owe 2", ha="center", va="center",
        fontsize=13, color=ORANGE, fontweight="bold")
ax.text(x_of(-3.5), Y - 1.42, "owing less is being better off",
        ha="center", va="center", fontsize=13, color=INK)

# the wrong answer and the right one, side by side
def verdict(x0, colour, word, statement, reason):
    ax.add_patch(FancyBboxPatch((x0, 0.22), 5.20, 1.02,
                                boxstyle="round,pad=0.04,rounding_size=0.14",
                                facecolor="white", edgecolor=colour, linewidth=2.2))
    ax.text(x0 + 0.34, 0.73, word, ha="left", va="center",
            fontsize=14, color=colour, fontweight="bold")
    ax.text(x0 + 1.72, 0.73, statement, ha="left", va="center",
            fontsize=17, color=colour)
    ax.text(x0 + 2.76, 0.73, reason, ha="left", va="center",
            fontsize=12.5, color=INK)


verdict(0.55, RED, "wrong:", r"$-5 > -2$", "because 5 is bigger than 2")
verdict(6.45, GREEN, "right:", r"$-2 > -5$", "because it lies further right")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_comparing.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
