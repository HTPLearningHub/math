"""Figure 3 - one twelve-cell grid holds thirds and quarters at the same time.

This is the picture that makes the least common denominator obvious instead
of being a rule to remember. A rectangle with 3 rows and 4 columns has 12
cells. One row is one third of it. One column is one quarter of it. So the
same 12 cells can measure both fractions, and once both are measured in
cells, adding them is counting cells.

The third grid deliberately does not overlap the two shadings: the blue
cells fill the top row and the orange cells continue straight after them, so
the reader can count 4 + 3 = 7 without wondering whether a cell was used
twice. That is honest, because the two fractions are being laid side by side,
not laid on top of each other.

Colours: blue is the first fraction, orange the second, and the answer is
written in green underneath.

Run with:  python figures/fig_03_grid_thirds_quarters.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"             # the first fraction, 1/3
ORANGE = "#E67E22"           # the second fraction, 1/4
GREEN = "#1E8449"            # the answer
GREY = "#78909C"
INK = "#212121"

TINT = {BLUE: "#CFE2F8", ORANGE: "#FBDDBC"}

COLS, ROWS = 4, 3            # 4 columns and 3 rows, so 12 cells
CELL = 0.80                  # cells are square, so the picture cannot mislead
GRID_W = COLS * CELL
GRID_H = ROWS * CELL

W, H = 14.40, 6.75
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

GRID_Y = 2.30                # bottom edge of every grid
GAP = 1.55                   # room for the + and = signs between the grids
LEFT = (W - 3 * GRID_W - 2 * GAP) / 2


def grid(px, filled, heading, under, count_line, count_colour):
    """Draw one 4 x 3 grid. `filled` maps a cell number (0..11) to a colour."""
    for r in range(ROWS):
        for c in range(COLS):
            n = r * COLS + c                       # cells are numbered left to
            x = px + c * CELL                      # right, top row first
            y = GRID_Y + (ROWS - 1 - r) * CELL
            colour = filled.get(n)
            ax.add_patch(Rectangle((x, y), CELL, CELL,
                                   facecolor=TINT[colour] if colour else "white",
                                   edgecolor=colour if colour else GREY,
                                   linewidth=1.8 if colour else 1.0,
                                   zorder=2))

    # one outline round the whole rectangle - this is the "one whole"
    ax.add_patch(Rectangle((px, GRID_Y), GRID_W, GRID_H, facecolor="none",
                           edgecolor=INK, linewidth=1.8, zorder=3))

    ax.text(px + GRID_W / 2, GRID_Y + GRID_H + 0.74, heading,
            ha="center", va="center", fontsize=15, color=INK, fontweight="bold")
    ax.text(px + GRID_W / 2, GRID_Y + GRID_H + 0.32, under,
            ha="center", va="center", fontsize=12.5, color=GREY)
    ax.text(px + GRID_W / 2, GRID_Y - 0.45, count_line,
            ha="center", va="center", fontsize=20, color=count_colour)


def sign(px, text):
    """The + or = that sits between two grids."""
    ax.text(px, GRID_Y + GRID_H / 2, text, ha="center", va="center",
            fontsize=34, color=INK)


G1 = LEFT
G2 = LEFT + GRID_W + GAP
G3 = LEFT + 2 * (GRID_W + GAP)

# one row out of three rows is one third, and a row holds 4 of the 12 cells
grid(G1, {0: BLUE, 1: BLUE, 2: BLUE, 3: BLUE},
     "one row of three", "so this is one third",
     r"$\frac{1}{3} = \frac{4}{12}$", BLUE)

sign(G1 + GRID_W + GAP / 2, "+")

# one column out of four columns is one quarter, and it holds 3 of the 12 cells
grid(G2, {0: ORANGE, 4: ORANGE, 8: ORANGE},
     "one column of four", "so this is one quarter",
     r"$\frac{1}{4} = \frac{3}{12}$", ORANGE)

sign(G2 + GRID_W + GAP / 2, "=")

# the two sets of cells laid side by side, never on top of each other
grid(G3, {0: BLUE, 1: BLUE, 2: BLUE, 3: BLUE,
          4: ORANGE, 5: ORANGE, 6: ORANGE},
     "the cells put together", "4 blue cells and 3 orange ones",
     r"$\frac{7}{12}$", GREEN)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.42,
        "One grid of twelve cells measures thirds and quarters at once",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.86,
        "3 rows and 4 columns give 12 cells: a row is one third of the "
        "rectangle, a column is one quarter of it",
        ha="center", va="center", fontsize=13, color=GREY)

# ------------------------------------------------------------- the bottom line
ax.text(W / 2, 1.15, r"$4$ cells $+$ $3$ cells $=$ $7$ cells, out of $12$",
        ha="center", va="center", fontsize=17, color=INK)
ax.text(W / 2, 0.65,
        "the cells are all the same size, so they can simply be counted",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_03_grid_thirds_quarters.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
