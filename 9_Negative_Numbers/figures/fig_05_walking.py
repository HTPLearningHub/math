"""Figure 5 - adding is walking along the line.

Two number lines, one calculation each. A plus sign sends you to the right and
a minus sign sends you to the left, and the size of the number is how far you
go. The purple arrow is the walk; the hollow circle is where you start and the
filled circle is where you finish.

Panel one starts on the positive side and ends there. Panel two starts on the
negative side and crosses zero, which is the step that surprises people.
Run with:  python figures/fig_05_walking.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # positive numbers
ORANGE = "#E67E22"      # negative numbers
GREY = "#78909C"        # zero and the line
PURPLE = "#8E44AD"      # the walk
INK = "#212121"

W, H = 12.6, 5.75
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LO, HI = -6, 6
LEFT, RIGHT = 1.45, W - 1.00


def x_of(n):
    return LEFT + (n - LO) / (HI - LO) * (RIGHT - LEFT)


def line(y, start, move, end, title, note):
    """Draw one number line with one walk on it.

    start   the number you begin at
    move    how far you walk; negative means to the left
    end     the number you land on
    """
    ax.text(LEFT - 0.35, y + 1.30, title, ha="left", va="center",
            fontsize=17, color=INK, fontweight="bold")

    ax.annotate("", xy=(RIGHT + 0.45, y), xytext=(LEFT - 0.45, y),
                arrowprops=dict(arrowstyle="<|-|>", color=GREY, linewidth=1.8,
                                mutation_scale=20))
    for n in range(LO, HI + 1):
        colour = GREY if n == 0 else (BLUE if n > 0 else ORANGE)
        ax.plot([x_of(n)] * 2, [y - 0.16, y + 0.16],
                color=colour, linewidth=2.4 if n == 0 else 1.4)
        ax.text(x_of(n), y - 0.45, rf"${n}$", ha="center", va="center",
                fontsize=12.5, color=colour)

    # one small purple hop for every single step of the walk
    step = 1 if move > 0 else -1
    for k in range(abs(move)):
        a, b = start + k * step, start + (k + 1) * step
        ax.annotate("", xy=(x_of(b), y + 0.62), xytext=(x_of(a), y + 0.62),
                    arrowprops=dict(arrowstyle="-|>", color=PURPLE, linewidth=2.0,
                                    mutation_scale=15))
    ax.text(x_of((start + end) / 2), y + 0.92, note, ha="center", va="center",
            fontsize=13.5, color=PURPLE, fontweight="bold")

    # start hollow, finish filled
    ax.plot([x_of(start)], [y], marker="o", markersize=13, markerfacecolor="white",
            markeredgecolor=INK, markeredgewidth=2.0, zorder=5)
    ax.plot([x_of(end)], [y], marker="o", markersize=13,
            color=BLUE if end > 0 else ORANGE, zorder=5)
    ax.text(x_of(start), y - 0.92, "start", ha="center", va="center",
            fontsize=12.5, color=INK)
    ax.text(x_of(end), y - 0.92, "finish", ha="center", va="center",
            fontsize=12.5, color=BLUE if end > 0 else ORANGE, fontweight="bold")


line(3.95, 5, -2, 3, r"$5 + (-2) = 3$", "2 steps to the left")
line(1.62, -4, 9, 5, r"$-4 + 9 = 5$", "9 steps to the right")

ax.text(W / 2, 0.24,
        "A negative number pulls you left. A positive number pushes you right.",
        ha="center", va="center", fontsize=14, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_walking.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
