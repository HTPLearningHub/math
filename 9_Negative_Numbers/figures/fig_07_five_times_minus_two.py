"""Figure 7 - multiplying by a negative number, as repeated addition.

Chapter 6 defined multiplication as repeated addition, and nothing about that
changes here. Five lots of -2 means five jumps of two steps to the left, and
five jumps of two steps land you at -10. That is the whole reason a positive
times a negative comes out negative.

Every jump is the same size and the same direction, which is what makes the
row of orange arrows worth looking at.
Run with:  python figures/fig_07_five_times_minus_two.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # positive numbers
ORANGE = "#E67E22"      # negative numbers, and the jumps
GREY = "#78909C"        # zero and the line
INK = "#212121"

W, H = 12.6, 3.75
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LO, HI = -11, 1
LEFT, RIGHT = 1.10, W - 1.10
Y = 1.55                                   # the height of the line


def x_of(n):
    return LEFT + (n - LO) / (HI - LO) * (RIGHT - LEFT)


ax.annotate("", xy=(RIGHT + 0.45, Y), xytext=(LEFT - 0.45, Y),
            arrowprops=dict(arrowstyle="<|-|>", color=GREY, linewidth=1.9,
                            mutation_scale=21))
for n in range(LO, HI + 1):
    colour = GREY if n == 0 else (BLUE if n > 0 else ORANGE)
    ax.plot([x_of(n)] * 2, [Y - 0.17, Y + 0.17],
            color=colour, linewidth=2.6 if n == 0 else 1.5)
    ax.text(x_of(n), Y - 0.48, rf"${n}$", ha="center", va="center",
            fontsize=13, color=colour,
            fontweight="bold" if n in (0, -10) else "normal")

# five jumps of two steps to the left, one after the other
for k in range(5):
    a, b = -2 * k, -2 * (k + 1)
    ax.annotate("", xy=(x_of(b) + 0.03, Y + 0.58), xytext=(x_of(a) - 0.03, Y + 0.58),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, linewidth=2.4,
                                mutation_scale=20))
    ax.text(x_of(a - 1), Y + 0.86, r"$-2$", ha="center", va="center",
            fontsize=13.5, color=ORANGE, fontweight="bold")
    ax.text(x_of(a - 1), Y + 1.20, f"jump {k + 1}", ha="center", va="center",
            fontsize=11.5, color=GREY)

# where you start and where you land
ax.plot([x_of(0)], [Y], marker="o", markersize=13, markerfacecolor="white",
        markeredgecolor=INK, markeredgewidth=2.0, zorder=5)
ax.plot([x_of(-10)], [Y], marker="o", markersize=13, color=ORANGE, zorder=5)
ax.text(x_of(0), Y - 0.88, "start at zero", ha="center", va="center",
        fontsize=12.5, color=INK)
ax.text(x_of(-10), Y - 0.88, "finish", ha="center", va="center",
        fontsize=12.5, color=ORANGE, fontweight="bold")

ax.text(W / 2, H - 0.28, r"$5 \times (-2)$ means: add $-2$ five times",
        ha="center", va="center", fontsize=16.5, color=INK, fontweight="bold")
ax.text(W / 2, 0.30, r"$(-2) + (-2) + (-2) + (-2) + (-2) = -10$",
        ha="center", va="center", fontsize=16, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_07_five_times_minus_two.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
