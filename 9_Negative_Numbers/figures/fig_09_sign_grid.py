"""Figure 9 - the sign of the answer, for multiplying and dividing.

Four boxes, one for each pair of signs. Each box carries the sign of the
answer, the word for it, and the same two small sums done with that pair of
signs - one multiplication and one division - because the rule is identical
for both.

The red bar at the bottom is there because this grid gets misused: it says
nothing about adding or subtracting.
Run with:  python figures/fig_09_sign_grid.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # a positive answer
ORANGE = "#E67E22"      # a negative answer
GREY = "#78909C"        # headings
RED = "#C0392B"         # the warning
INK = "#212121"

W, H = 11.4, 6.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CELL_W, CELL_H = 3.65, 1.95                # the size of one box
X0, Y0 = 2.85, 3.35                        # the left edge and the top row's bottom edge


def cell(col, row, positive, mult, div):
    """Draw one box of the grid.

    col, row    0 or 1, counted from the top left
    positive    True when the answer comes out positive
    """
    x = X0 + col * (CELL_W + 0.25)
    y = Y0 - row * (CELL_H + 0.25)
    colour = BLUE if positive else ORANGE
    word = "positive" if positive else "negative"
    sign = r"$+$" if positive else r"$-$"

    ax.add_patch(FancyBboxPatch((x, y), CELL_W, CELL_H,
                                boxstyle="round,pad=0.03,rounding_size=0.14",
                                facecolor="white", edgecolor=colour, linewidth=2.2))
    ax.text(x + 0.60, y + CELL_H / 2 + 0.08, sign, ha="center", va="center",
            fontsize=44, color=colour, fontweight="bold")
    ax.text(x + 0.60, y + 0.32, word, ha="center", va="center",
            fontsize=12.5, color=colour, fontweight="bold")
    ax.text(x + 1.15, y + CELL_H - 0.62, mult, ha="left", va="center",
            fontsize=15.5, color=INK)
    ax.text(x + 1.15, y + 0.62, div, ha="left", va="center",
            fontsize=15.5, color=INK)


cell(0, 0, True,  r"$6 \times 3 = 18$",      r"$18 \div 3 = 6$")
cell(1, 0, False, r"$6 \times (-3) = -18$",  r"$18 \div (-3) = -6$")
cell(0, 1, False, r"$(-6) \times 3 = -18$",  r"$(-18) \div 3 = -6$")
cell(1, 1, True,  r"$(-6) \times (-3) = 18$", r"$(-18) \div (-3) = 6$")

# the headings for the two columns and the two rows
for col, text in enumerate(["second number is positive", "second number is negative"]):
    ax.text(X0 + col * (CELL_W + 0.25) + CELL_W / 2, 5.58, text,
            ha="center", va="center", fontsize=13.5, color=GREY, fontweight="bold")
for row, text in enumerate(["first number\nis positive", "first number\nis negative"]):
    ax.text(X0 - 0.30, Y0 - row * (CELL_H + 0.25) + CELL_H / 2, text,
            ha="right", va="center", fontsize=13.5, color=GREY,
            fontweight="bold", linespacing=1.5)

ax.text(W / 2, H - 0.30, r"The sign of the answer, for $\times$ and $\div$",
        ha="center", va="center", fontsize=17, color=INK, fontweight="bold")

# the warning bar
ax.add_patch(FancyBboxPatch((1.30, 0.22), W - 2.60, 0.72,
                            boxstyle="round,pad=0.03,rounding_size=0.14",
                            facecolor="#FDECEA", edgecolor=RED, linewidth=2.0))
ax.text(W / 2, 0.58,
        r"This grid is for multiplying and dividing only. "
        r"It says nothing about $+$ and $-$.",
        ha="center", va="center", fontsize=14, color=RED, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_09_sign_grid.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
