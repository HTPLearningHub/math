"""Figure 1 - why the order of two factors does not matter.

One grid of fifteen dots is drawn twice. On the left the grid is read as five
rows of three; on the right the very same grid is read as three columns of
five. Nothing is added and nothing is taken away between the two panels - only
the way we group the dots changes. That is the whole reason 5 x 3 and 3 x 5
give the same answer.

Colour convention of the book: blue = the pieces that are already there,
orange = the piece that moves or the second way of seeing it.

Run with:  python figures/fig_01_rows_of_dots.py
"""

import matplotlib
matplotlib.use("Agg")                       # no window, just write the file
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"          # the rows, on the left panel
BLUE_FILL = "#EAF2FB"
ORANGE = "#E67E22"        # the columns, on the right panel
ORANGE_FILL = "#FDF0E3"
INK = "#212121"

ROWS, COLS = 5, 3         # the grid is the same in both panels
STEP = 0.78               # distance between the centres of two dots
R = 0.20                  # radius of one dot

W, H = 12.0, 7.4          # figure size in inches

fig, ax = plt.subplots(figsize=(W, H))
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")                      # dots must stay round

Y_TOP = 5.30                                # y of the top row of dots


def dot_xy(panel_x, r, c):
    """Centre of the dot in row r, column c, for a panel centred on panel_x."""
    x0 = panel_x - (COLS - 1) * STEP / 2     # left-hand column
    return x0 + c * STEP, Y_TOP - r * STEP


def draw_panel(panel_x, group_by, edge, fill, title, formula):
    """Draw the 5 x 3 grid once, with a band drawn around each row or column."""
    pad = 0.30                               # space between a dot and its band

    if group_by == "row":
        for r in range(ROWS):                # one band per row: 5 bands of 3
            x_lo, y = dot_xy(panel_x, r, 0)
            x_hi, _ = dot_xy(panel_x, r, COLS - 1)
            ax.add_patch(FancyBboxPatch(
                (x_lo - pad, y - pad), (x_hi - x_lo) + 2 * pad, 2 * pad,
                boxstyle="round,pad=0.02,rounding_size=0.18",
                facecolor=fill, edgecolor=edge, linewidth=1.8, zorder=1))
    else:
        for c in range(COLS):                # one band per column: 3 bands of 5
            x, y_hi = dot_xy(panel_x, 0, c)
            _, y_lo = dot_xy(panel_x, ROWS - 1, c)
            ax.add_patch(FancyBboxPatch(
                (x - pad, y_lo - pad), 2 * pad, (y_hi - y_lo) + 2 * pad,
                boxstyle="round,pad=0.02,rounding_size=0.18",
                facecolor=fill, edgecolor=edge, linewidth=1.8, zorder=1))

    for r in range(ROWS):                    # the fifteen dots themselves
        for c in range(COLS):
            x, y = dot_xy(panel_x, r, c)
            ax.add_patch(Circle((x, y), R, facecolor=edge, edgecolor="none",
                                zorder=3))

    ax.text(panel_x, Y_TOP + 0.85, title, ha="center", va="center",
            fontsize=16, fontweight="bold", color=edge)
    ax.text(panel_x, Y_TOP - (ROWS - 1) * STEP - 0.95, formula, ha="center",
            va="center", fontsize=18, color=INK)


ax.text(W / 2, H - 0.32, "The same 15 dots, counted in two ways",
        ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

draw_panel(3.30, "row", BLUE, BLUE_FILL,
           "5 rows of 3", r"$5 \times 3 = 15$")
draw_panel(8.70, "col", ORANGE, ORANGE_FILL,
           "3 columns of 5", r"$3 \times 5 = 15$")

# the equals sign between the two panels, on the line of the formulas
ax.text(W / 2, Y_TOP - (ROWS - 1) * STEP - 0.95, "=", ha="center", va="center",
        fontsize=24, color=INK)

ax.text(W / 2, 0.35,
        "Turning the picture does not add or remove a single dot.",
        ha="center", va="center", fontsize=13, style="italic", color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_rows_of_dots.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
