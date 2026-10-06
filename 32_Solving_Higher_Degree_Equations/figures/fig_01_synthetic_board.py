"""Figure 1 - the synthetic division board.

Divides x^4 + x^3 - 11x^2 - 5x + 30 by (x - 2). The top row holds the
coefficients, the middle row holds "2 times the bottom number to the left",
the bottom row holds the sums. Arrows show the three moves: bring down,
multiply by 2, add. The last bottom number (the remainder) is boxed in green.

Colours: slate for the given coefficients, orange for the multiply move and
the middle row, blue for the bottom row (the new polynomial), green for the
remainder.

Run with:  python figures/fig_01_synthetic_board.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
SLATE = "#5D6D7E"                                  # numbers we are given
ORANGE = "#E67E22"                                 # multiply move, middle row
BLUE = "#2E86DE"                                   # bottom row = new polynomial
GREEN = "#1E8449"                                  # remainder

c = 2                                              # the number we test
top = [1, 1, -11, -5, 30]                          # coefficients of the quartic
bottom = [top[0]]                                  # first one is brought down
middle = [None]                                    # nothing above the first sum
for a in top[1:]:                                  # multiply, then add
    m = c * bottom[-1]
    middle.append(m)
    bottom.append(a + m)
# bottom is now [1, 3, -5, -15, 0]

heads = [r"$x^{4}$", r"$x^{3}$", r"$x^{2}$", r"$x$", "number"]

X = [2.0, 4.0, 6.0, 8.0, 10.0]                     # column centres
Y_HEAD, Y_TOP, Y_MID, Y_BOT = 5.6, 4.6, 3.2, 1.6   # row heights

fig, ax = plt.subplots(figsize=(13, 7.6))
ax.set_xlim(-0.6, 12.6)
ax.set_ylim(-1.3, 6.3)
ax.axis("off")

def num(v):                                        # proper minus sign
    return rf"${v}$" if v >= 0 else rf"$-{abs(v)}$"

# column headers: which power each column belongs to
for x0, h in zip(X, heads):
    ax.text(x0, Y_HEAD, h, ha="center", va="center", fontsize=17, color=GREY)

# the corner: the tested number and the two lines of the board
ax.text(0.45, Y_TOP, num(c), ha="center", va="center", fontsize=28,
        color=ORANGE, fontweight="bold")
ax.plot([1.0, 1.0], [Y_TOP + 0.6, Y_MID - 0.6], color=INK, lw=2.5)   # upright
ax.plot([1.0, 11.0], [Y_MID - 0.6, Y_MID - 0.6], color=INK, lw=2.5)  # floor

# top row: the given coefficients
for x0, v in zip(X, top):
    ax.text(x0, Y_TOP, num(v), ha="center", va="center", fontsize=26,
            color=SLATE)

# middle row: c times the bottom number one column to the left
for x0, v in zip(X[1:], middle[1:]):
    ax.text(x0, Y_MID, num(v), ha="center", va="center", fontsize=24,
            color=ORANGE)

# bottom row: the sums
for i, (x0, v) in enumerate(zip(X, bottom)):
    col = GREEN if i == len(X) - 1 else BLUE
    ax.text(x0, Y_BOT, num(v), ha="center", va="center", fontsize=26,
            color=col, fontweight="bold")
ax.add_patch(FancyBboxPatch((X[-1] - 0.55, Y_BOT - 0.42), 1.1, 0.84,
                            boxstyle="round,pad=0.05", fill=False,
                            edgecolor=GREEN, lw=2.5))       # remainder box

# move 1: bring the first coefficient straight down
ax.add_patch(FancyArrowPatch((X[0] - 0.35, Y_TOP - 0.35),
                             (X[0] - 0.35, Y_BOT + 0.35),
                             arrowstyle="-|>", mutation_scale=20,
                             color=BLUE, lw=2, ls="--"))
ax.text(0.85, Y_MID - 0.1, "bring\ndown", ha="right",
        va="center", fontsize=13, color=BLUE)      # left of the upright line

# move 2: every bottom number, times 2, goes up into the next column
for i in range(len(X) - 1):
    ax.add_patch(FancyArrowPatch((X[i] + 0.3, Y_BOT + 0.3),
                                 (X[i + 1] - 0.45, Y_MID - 0.25),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=ORANGE, lw=1.8))
ax.text((X[0] + X[1]) / 2 + 0.05, (Y_BOT + Y_MID) / 2 - 0.05,
        r"$\times 2$", ha="center", va="center", fontsize=15, color=ORANGE,
        bbox=dict(facecolor="white", edgecolor="none", pad=1))

# move 3: add each column (top + middle = bottom), shown once, in the x^2 column
ax.add_patch(FancyArrowPatch((X[2] + 0.8, Y_TOP - 0.2),
                             (X[2] + 0.8, Y_MID - 0.5),   # stop above floor
                             arrowstyle="-|>", mutation_scale=16,
                             color=SLATE, lw=1.5))
ax.text(X[2] + 0.9, (Y_TOP + Y_MID) / 2 + 0.1, "add", ha="left",
        va="center", fontsize=13, color=SLATE)

# what the bottom row means
ax.plot([X[0] - 0.3, X[3] + 0.4], [0.75, 0.75], color=BLUE, lw=2)
ax.text((X[0] + X[3]) / 2, 0.25,
        r"new polynomial:  $x^{3} + 3x^{2} - 5x - 15$",
        ha="center", va="center", fontsize=17, color=BLUE)
ax.text((X[0] + X[3]) / 2, -0.35, "(one degree lower: start at $x^{3}$)",
        ha="center", va="center", fontsize=13, color=BLUE)
ax.text(X[-1], 0.55, "remainder", ha="center", va="center", fontsize=15,
        color=GREEN, fontweight="bold")
ax.text(X[-1], 0.0, r"$0$, so $x = 2$" + "\nis a solution", ha="center",
        va="center", fontsize=13, color=GREEN)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_synthetic_board.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_01_synthetic_board.png")
