"""Figure 7 - where the formula for the number of factors comes from.

The source gives d(N) = (e1+1)(e2+1)... as a rule to memorise. The rule is
really a counting argument, and the grid makes the argument visible: 20 is
2^2 x 5, so building a factor of 20 means choosing how many 2's to take
(none, one or two - three choices) and how many 5's to take (none or one -
two choices). Three rows times two columns is six cells, and the six cells
hold the six factors of 20, each exactly once.

That also explains the "+1" that the reader always forgets: the extra
choice is taking *none* of that prime, which is the row and column marked
with a power of zero.
Run with:  python figures/fig_07_factor_grid_20.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

GREEN = "#1E8449"            # a factor of 20
PURPLE = "#8E44AD"           # the powers, as in Chapter 10
GREY = "#78909C"
INK = "#212121"

W, H = 10.60, 7.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CW, CH = 2.30, 1.18                        # width and height of one cell
GAP = 0.14                                 # space between cells
ROWS = [(0, 1), (1, 2), (2, 4)]            # exponent of 2, and 2 to that power
COLS = [(0, 1), (1, 5)]                    # exponent of 5, and 5 to that power

GRID_W = len(COLS) * CW + (len(COLS) - 1) * GAP
LEFT = (W - GRID_W) / 2 + 0.85             # pushed right, to leave room for labels
TOP = H - 2.05                             # top edge of the first row of cells

# ------------------------------------------------------- the column headings
for j, (e5, p5) in enumerate(COLS):
    x = LEFT + j * (CW + GAP)
    ax.text(x + CW / 2, TOP + 0.52, rf"take $5^{{{e5}}} = {p5}$",
            ha="center", va="center", fontsize=15, color=PURPLE)
    ax.text(x + CW / 2, TOP + 0.20,
            "no 5 at all" if e5 == 0 else "one 5",
            ha="center", va="center", fontsize=12, color=GREY)

# ---------------------------------------------- the row headings and the cells
for i, (e2, p2) in enumerate(ROWS):
    y = TOP - (i + 1) * CH - i * GAP
    ax.text(LEFT - 0.28, y + CH / 2 + 0.13, rf"take $2^{{{e2}}} = {p2}$",
            ha="right", va="center", fontsize=15, color=PURPLE)
    ax.text(LEFT - 0.28, y + CH / 2 - 0.20,
            "no 2 at all" if e2 == 0 else ("one 2" if e2 == 1 else "two 2's"),
            ha="right", va="center", fontsize=12, color=GREY)

    for j, (e5, p5) in enumerate(COLS):
        x = LEFT + j * (CW + GAP)
        ax.add_patch(FancyBboxPatch((x, y), CW, CH,
                                    boxstyle="round,pad=0.02,rounding_size=0.12",
                                    facecolor="#E8F5EC", edgecolor=GREEN,
                                    linewidth=1.8))
        ax.text(x + CW / 2, y + CH - 0.38, rf"${p2} \times {p5}$",
                ha="center", va="center", fontsize=15, color=GREY)
        ax.text(x + CW / 2, y + 0.36, str(p2 * p5),
                ha="center", va="center", fontsize=25, color=GREEN,
                fontweight="bold")

# ------------------------------------------------------------- the counting
BOT = TOP - len(ROWS) * CH - (len(ROWS) - 1) * GAP
ax.text(W / 2, BOT - 0.52,
        "3 choices for the 2's, 2 choices for the 5's, so 6 cells - and 6 factors",
        ha="center", va="center", fontsize=15, color=INK)
ax.text(W / 2, BOT - 1.06, r"$d(20) = (2+1) \times (1+1) = 3 \times 2 = 6$",
        ha="center", va="center", fontsize=22, color=PURPLE)
ax.text(W / 2, BOT - 1.58, r"factors of $20 = \{1,\, 2,\, 4,\, 5,\, 10,\, 20\}$",
        ha="center", va="center", fontsize=17, color=GREEN)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.40, r"Building every factor of $20 = 2^{2} \times 5$",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.86, "pick some of the 2's, pick some of the 5's, multiply",
        ha="center", va="center", fontsize=14, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_07_factor_grid_20.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
