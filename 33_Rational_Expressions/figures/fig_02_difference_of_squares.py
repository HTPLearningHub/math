"""Figure 2 - why 7^2 - 3^2 = (7 - 3)(7 + 3).

Left: a 7 by 7 square of unit squares. The 3 by 3 corner (top right) is cut
away and drawn as a dashed outline. What is left is an L shape made of two
rectangles: blue (4 wide, 7 tall) and orange (3 wide, 4 tall).
Right: the same two rectangles laid in one row. The blue one is turned on its
side (7 wide, 4 tall) and the orange one stands next to it (3 wide, 4 tall).
Together: a rectangle 10 wide and 4 tall, so 40 squares = 4 x 10.

Colours: blue and orange for the two pieces, grey dashed for the removed
corner, ink for labels.

Run with:  python figures/fig_02_difference_of_squares.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
BLUE = "#2E86DE"
ORANGE = "#E67E22"

a, b = 7, 3                                        # the two sides of the squares


def block(ax, x, y, w, h, col):
    """Draw a w-by-h rectangle of unit squares with its lower-left at (x, y)."""
    for i in range(w):
        for j in range(h):
            ax.add_patch(Rectangle((x + i, y + j), 1, 1, facecolor=col,
                                   alpha=0.30, edgecolor="white", lw=1.5))
    ax.add_patch(Rectangle((x, y), w, h, fill=False, edgecolor=col, lw=3))


fig, ax = plt.subplots(figsize=(16, 7.5))
ax.set_xlim(-1.6, 23.5)
ax.set_ylim(-2.4, 8.6)
ax.set_aspect("equal")                             # squares must look square
ax.axis("off")

# ---------- left: the square with a corner cut away ----------
block(ax, 0, 0, a - b, a, BLUE)                    # blue: 4 wide, 7 tall
block(ax, a - b, 0, b, a - b, ORANGE)              # orange: 3 wide, 4 tall
ax.add_patch(Rectangle((a - b, a - b), b, b, fill=False, edgecolor=GREY,
                       lw=2, ls="--"))             # the removed 3 by 3 corner
ax.text(a - b + b / 2, a - b + b / 2, "$3^{2} = 9$\ntaken\naway",
        ha="center", va="center", fontsize=14, color=GREY)

ax.text(a / 2, -0.8, "$7$", ha="center", fontsize=18, color=INK)       # bottom side
ax.text(-0.6, a / 2, "$7$", ha="center", va="center", fontsize=18, color=INK)
ax.text((a - b) / 2, a + 0.4, "$7 - 3 = 4$", ha="center", fontsize=16, color=BLUE)
ax.text(a + 0.35, (a - b) / 2, "$4$", va="center", fontsize=16, color=ORANGE)
ax.text(a + 0.35, a - b + b / 2, "$3$", va="center", fontsize=16, color=GREY)
ax.text(a / 2, -2.0, r"$7^{2} - 3^{2} = 49 - 9 = 40$ squares",
        ha="center", fontsize=17, color=INK)

# ---------- arrow between the two pictures ----------
ax.add_patch(FancyArrowPatch((8.4, 3.5), (10.6, 3.5), arrowstyle="-|>",
                             mutation_scale=30, color=GREY, lw=2.5))
ax.text(9.5, 4.1, "move the\npieces", ha="center", fontsize=13, color=GREY)

# ---------- right: the same pieces as one rectangle ----------
X = 11.5                                           # left edge of the new rectangle
block(ax, X, 0, a, a - b, BLUE)                    # blue turned: 7 wide, 4 tall
block(ax, X + a, 0, b, a - b, ORANGE)              # orange: 3 wide, 4 tall
ax.text(X + a / 2, a - b + 0.4, "$7$", ha="center", fontsize=16, color=BLUE)
ax.text(X + a + b / 2, a - b + 0.4, "$3$", ha="center", fontsize=16, color=ORANGE)
ax.annotate("", xy=(X, a - b + 1.5), xytext=(X + a + b, a - b + 1.5),
            arrowprops=dict(arrowstyle="<->", color=INK, lw=1.6))
ax.text(X + (a + b) / 2, a - b + 1.8, "$7 + 3 = 10$", ha="center",
        fontsize=17, color=INK)
ax.text(X + a + b + 0.35, (a - b) / 2, "$7 - 3 = 4$", va="center",
        fontsize=16, color=INK)
ax.text(X + (a + b) / 2, -2.0, r"$(7 - 3) \times (7 + 3) = 4 \times 10 = 40$ squares",
        ha="center", fontsize=17, color=INK)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_difference_of_squares.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_02_difference_of_squares.png")
