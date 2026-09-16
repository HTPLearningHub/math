"""Figure 3 - the area model: a rectangle 5 tall and 34 wide, cut at 30.

The rectangle is drawn to scale, one small square = one unit of area, so the
reader can in principle count the squares. Cutting the rectangle once, at
width 30, does not change how many squares there are. That is the distributive
property seen as a picture:

    5 x (30 + 4)  =  (5 x 30) + (5 x 4)  =  150 + 20  =  170

Blue is the first piece of the width, orange is the second piece - the same
two colours as Figure 2, so the reader can see it is the same idea.

Run with:  python figures/fig_03_area_model.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"
BLUE_FILL = "#D6E7F8"
ORANGE = "#E67E22"
ORANGE_FILL = "#FBE0C4"
GRID = "#FFFFFF"          # the square grid is drawn in white, over the fill
INK = "#212121"

HEIGHT = 5                # height of the rectangle
PART_A = 30               # first piece of the width
PART_B = 4                # second piece of the width
WIDTH = PART_A + PART_B

X_LO, X_HI = -5.2, 37.0   # drawing area, in the same units as the squares
Y_LO, Y_HI = -4.4, 8.6

W = 12.0
H = W * (Y_HI - Y_LO) / (X_HI - X_LO)        # keeps one unit square really square

fig, ax = plt.subplots(figsize=(W, H))
ax.axis("off")
ax.set_xlim(X_LO, X_HI)
ax.set_ylim(Y_LO, Y_HI)
ax.set_aspect("equal")                       # squares must be square

# --- the two pieces of the rectangle --------------------------------------
ax.add_patch(Rectangle((0, 0), PART_A, HEIGHT, facecolor=BLUE_FILL,
                       edgecolor="none", zorder=1))
ax.add_patch(Rectangle((PART_A, 0), PART_B, HEIGHT, facecolor=ORANGE_FILL,
                       edgecolor="none", zorder=1))

# --- the unit squares, so the area can be counted -------------------------
for x in range(1, WIDTH):
    ax.plot([x, x], [0, HEIGHT], color=GRID, linewidth=0.8, zorder=2)
for y in range(1, HEIGHT):
    ax.plot([0, WIDTH], [y, y], color=GRID, linewidth=0.8, zorder=2)

# --- the outlines: outer box, and the single cut --------------------------
ax.add_patch(Rectangle((0, 0), PART_A, HEIGHT, facecolor="none",
                       edgecolor=BLUE, linewidth=2.4, zorder=3))
ax.add_patch(Rectangle((PART_A, 0), PART_B, HEIGHT, facecolor="none",
                       edgecolor=ORANGE, linewidth=2.4, zorder=3))

# --- the big number inside each piece -------------------------------------
ax.text(PART_A / 2, HEIGHT / 2, "150", ha="center", va="center",
        fontsize=30, fontweight="bold", color=BLUE, zorder=4)
ax.text(PART_A + PART_B / 2, HEIGHT / 2, "20", ha="center", va="center",
        fontsize=20, fontweight="bold", color=ORANGE, zorder=4)

# --- the height, marked on the left ---------------------------------------
ax.annotate("", xy=(-0.6, HEIGHT), xytext=(-0.6, 0),
            arrowprops=dict(arrowstyle="<|-|>", color=INK, linewidth=1.6,
                            mutation_scale=12))
ax.text(-1.9, HEIGHT / 2, "height\n5", ha="center", va="center",
        fontsize=14, color=INK)

# --- the two widths, marked above -----------------------------------------
for x_lo, x_hi, label, colour in [(0, PART_A, "width 30", BLUE),
                                  (PART_A, WIDTH, "width 4", ORANGE)]:
    ax.annotate("", xy=(x_hi, 6.0), xytext=(x_lo, 6.0),
                arrowprops=dict(arrowstyle="<|-|>", color=colour, linewidth=1.6,
                                mutation_scale=12))
    ax.text((x_lo + x_hi) / 2, 6.6, label, ha="center", va="bottom",
            fontsize=14, color=colour, fontweight="bold")

ax.text(WIDTH / 2, 8.2, "One rectangle, cut into two pieces",
        ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

# --- the two products, written under their own piece ----------------------
ax.text(PART_A / 2, -1.5, r"$5 \times 30 = 150$", ha="center", va="center",
        fontsize=16, color=BLUE, fontweight="bold")
ax.text(PART_A + PART_B / 2, -1.5, r"$5 \times 4 = 20$", ha="center", va="center",
        fontsize=16, color=ORANGE, fontweight="bold")

ax.text(WIDTH / 2, -3.5, r"$5 \times (30 + 4) \;=\; 150 + 20 \;=\; 170$",
        ha="center", va="center", fontsize=19, color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_area_model.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
