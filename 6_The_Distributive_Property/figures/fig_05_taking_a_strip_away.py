"""Figure 5 - distributing across a subtraction, drawn as a strip taken away.

The rectangle is 5 tall and 10 wide, so it holds 5 x 10 = 50 squares. To find
5 x (10 - 2) we make the rectangle two columns narrower. The grey strip on the
right is what leaves: 5 x 2 = 10 squares. What stays is 50 - 10 = 40.

Seeing it this way explains why the minus sign has to survive the distribution.
The strip is taken away once for every row, that is 5 times, so the amount that
leaves is 5 x 2 and not 2.

Run with:  python figures/fig_05_taking_a_strip_away.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"          # the part that stays
BLUE_FILL = "#D6E7F8"
GREY = "#78909C"          # the strip that is taken away
GREY_FILL = "#ECEFF1"
GRID = "#FFFFFF"
INK = "#212121"

HEIGHT = 5                # rows
WHOLE = 10                # the width we start from
TAKEN = 2                 # the width we take away
KEPT = WHOLE - TAKEN

X_LO, X_HI = -3.6, 13.6
Y_LO, Y_HI = -5.2, 8.2

W = 10.0
H = W * (Y_HI - Y_LO) / (X_HI - X_LO)        # one unit stays one square

fig, ax = plt.subplots(figsize=(W, H))
ax.axis("off")
ax.set_xlim(X_LO, X_HI)
ax.set_ylim(Y_LO, Y_HI)
ax.set_aspect("equal")

# --- the part that stays, and the strip that goes -------------------------
ax.add_patch(Rectangle((0, 0), KEPT, HEIGHT, facecolor=BLUE_FILL,
                       edgecolor="none", zorder=1))
ax.add_patch(Rectangle((KEPT, 0), TAKEN, HEIGHT, facecolor=GREY_FILL,
                       edgecolor=GREY, linewidth=0, hatch="//", zorder=1))

for x in range(1, WHOLE):                    # the unit squares
    ax.plot([x, x], [0, HEIGHT], color=GRID, linewidth=0.9, zorder=2)
for y in range(1, HEIGHT):
    ax.plot([0, WHOLE], [y, y], color=GRID, linewidth=0.9, zorder=2)

ax.add_patch(Rectangle((0, 0), KEPT, HEIGHT, facecolor="none",
                       edgecolor=BLUE, linewidth=2.4, zorder=3))
ax.add_patch(Rectangle((KEPT, 0), TAKEN, HEIGHT, facecolor="none",
                       edgecolor=GREY, linewidth=2.4, zorder=3))

ax.text(KEPT / 2, HEIGHT / 2, "40", ha="center", va="center",
        fontsize=30, fontweight="bold", color=BLUE, zorder=4)
ax.text(KEPT + TAKEN / 2, HEIGHT / 2, "10", ha="center", va="center",
        fontsize=20, fontweight="bold", color="#455A64", zorder=4,
        bbox=dict(boxstyle="round,pad=0.25", facecolor="white",
                  edgecolor=GREY, linewidth=1.0))

# --- the height, on the left ----------------------------------------------
ax.annotate("", xy=(-0.55, HEIGHT), xytext=(-0.55, 0),
            arrowprops=dict(arrowstyle="<|-|>", color=INK, linewidth=1.6,
                            mutation_scale=12))
ax.text(-1.70, HEIGHT / 2, "height\n5", ha="center", va="center",
        fontsize=13, color=INK)

# --- the whole width, above -----------------------------------------------
ax.annotate("", xy=(WHOLE, HEIGHT + 0.75), xytext=(0, HEIGHT + 0.75),
            arrowprops=dict(arrowstyle="<|-|>", color=INK, linewidth=1.6,
                            mutation_scale=12))
ax.text(WHOLE / 2, HEIGHT + 1.10, r"start with width 10:  $5 \times 10 = 50$",
        ha="center", va="bottom", fontsize=15, color=INK)

ax.text(WHOLE / 2, 7.7, "Take two columns away from the rectangle",
        ha="center", va="center", fontsize=17, fontweight="bold", color=INK)

# --- the two pieces of the width, below -----------------------------------
for lo, hi, label, colour in [(0, KEPT, "8 columns stay", BLUE),
                              (KEPT, WHOLE, "2 go", GREY)]:
    ax.annotate("", xy=(hi, -0.75), xytext=(lo, -0.75),
                arrowprops=dict(arrowstyle="<|-|>", color=colour, linewidth=1.6,
                                mutation_scale=12))
    ax.text((lo + hi) / 2, -1.25, label, ha="center", va="top",
            fontsize=13, color=colour, fontweight="bold")

ax.text(KEPT / 2, -2.55, r"$5 \times 8 = 40$", ha="center", va="center",
        fontsize=15, color=BLUE, fontweight="bold")
ax.text(KEPT + TAKEN / 2 + 0.9, -2.55, r"$5 \times 2 = 10$", ha="center",
        va="center", fontsize=15, color="#455A64", fontweight="bold")

ax.text(WHOLE / 2, -4.4, r"$5 \times (10 - 2) \;=\; 50 - 10 \;=\; 40$",
        ha="center", va="center", fontsize=19, color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_taking_a_strip_away.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
