"""Figure 4 - the most common mistake, drawn as a picture.

Both panels show the same rectangle: 3 tall and 4 + 5 = 9 wide, so 27 squares.

Left (green, correct): the 3 is multiplied by both terms. 12 squares plus
15 squares, and every square in the rectangle is counted.

Right (red, wrong): the 3 is multiplied by the 4 only, and then the 5 is
simply added on. That counts 12 squares plus 5 squares = 17, and leaves the
10 grey squares out of the answer. The grey squares are exactly what the
mistake loses: 27 - 17 = 10.

Colour convention: red = the wrong method, green = the right one, exactly as
in Chapter 2 figure 7 and Chapter 5 figure 3. Grey = a piece that is missing.

Run with:  python figures/fig_04_forgetting_a_piece.py
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
GREY = "#78909C"
GREY_FILL = "#ECEFF1"
RED = "#C0392B"           # the wrong method
GREEN = "#1E8449"         # the right method
GRID = "#FFFFFF"
INK = "#212121"

HEIGHT = 3                # height of the rectangle
PART_A = 4                # first term inside the brackets
PART_B = 5                # second term inside the brackets
WIDTH = PART_A + PART_B

LEFT_X = 0.0              # left edge of the correct panel
RIGHT_X = 13.0            # left edge of the wrong panel

X_LO, X_HI = -1.2, 23.2
Y_LO, Y_HI = -4.2, 6.6

W = 12.0
H = W * (Y_HI - Y_LO) / (X_HI - X_LO)        # one unit stays one square

fig, ax = plt.subplots(figsize=(W, H))
ax.axis("off")
ax.set_xlim(X_LO, X_HI)
ax.set_ylim(Y_LO, Y_HI)
ax.set_aspect("equal")


def block(x0, y0, w, h, face, edge, hatch=None):
    """One filled block with its own outline, drawn on top of the fill.

    When a hatch is asked for, the patch is given an edge colour so that the
    hatch lines come out grey instead of the matplotlib default black, which
    is far too heavy to write a label on top of.
    """
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=face, edgecolor=edge,
                           linewidth=0, hatch=hatch, zorder=1))
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor="none", edgecolor=edge,
                           linewidth=2.2, zorder=3))


def unit_grid(x0, y0, w, h, colour=GRID):
    """Thin lines that cut a block into single squares, so they can be counted."""
    for i in range(1, w):
        ax.plot([x0 + i, x0 + i], [y0, y0 + h], color=colour, linewidth=0.9,
                zorder=2)
    for j in range(1, h):
        ax.plot([x0, x0 + w], [y0 + j, y0 + j], color=colour, linewidth=0.9,
                zorder=2)


def widths(x0, colour_a, colour_b):
    """The two width arrows above a panel, one per term."""
    for lo, hi, label, colour in [(0, PART_A, "4", colour_a),
                                  (PART_A, WIDTH, "5", colour_b)]:
        ax.annotate("", xy=(x0 + hi, HEIGHT + 0.7),
                    xytext=(x0 + lo, HEIGHT + 0.7),
                    arrowprops=dict(arrowstyle="<|-|>", color=colour,
                                    linewidth=1.5, mutation_scale=11))
        ax.text(x0 + (lo + hi) / 2, HEIGHT + 1.05, label, ha="center",
                va="bottom", fontsize=14, color=colour, fontweight="bold")


# --------------------------------------------------------- the right way
block(LEFT_X, 0, PART_A, HEIGHT, BLUE_FILL, BLUE)
unit_grid(LEFT_X, 0, PART_A, HEIGHT)
block(LEFT_X + PART_A, 0, PART_B, HEIGHT, ORANGE_FILL, ORANGE)
unit_grid(LEFT_X + PART_A, 0, PART_B, HEIGHT)

ax.text(LEFT_X + PART_A / 2, HEIGHT / 2, "12", ha="center", va="center",
        fontsize=22, fontweight="bold", color=BLUE, zorder=4)
ax.text(LEFT_X + PART_A + PART_B / 2, HEIGHT / 2, "15", ha="center",
        va="center", fontsize=22, fontweight="bold", color=ORANGE, zorder=4)
widths(LEFT_X, BLUE, ORANGE)

ax.text(LEFT_X + WIDTH / 2, 5.9, "Right: multiply the 3 by both terms",
        ha="center", va="center", fontsize=15, fontweight="bold", color=GREEN)
ax.text(LEFT_X + WIDTH / 2, -1.3,
        r"$(3 \times 4) + (3 \times 5) = 12 + 15 = 27$",
        ha="center", va="center", fontsize=15, color=INK)
ax.text(LEFT_X + WIDTH / 2, -2.8, "Every square is counted.",
        ha="center", va="center", fontsize=14, color=GREEN, style="italic")

# ------------------------------------------------------- the common mistake
block(RIGHT_X, 0, PART_A, HEIGHT, BLUE_FILL, BLUE)
unit_grid(RIGHT_X, 0, PART_A, HEIGHT)
# only the bottom row of the second piece was counted: five single squares
block(RIGHT_X + PART_A, 0, PART_B, 1, ORANGE_FILL, ORANGE)
unit_grid(RIGHT_X + PART_A, 0, PART_B, 1)
# the ten squares the mistake never counts
block(RIGHT_X + PART_A, 1, PART_B, HEIGHT - 1, GREY_FILL, GREY, hatch="//")
unit_grid(RIGHT_X + PART_A, 1, PART_B, HEIGHT - 1, colour="#FFFFFF")

ax.text(RIGHT_X + PART_A / 2, HEIGHT / 2, "12", ha="center", va="center",
        fontsize=22, fontweight="bold", color=BLUE, zorder=4)
ax.text(RIGHT_X + PART_A + PART_B / 2, 0.5, "5", ha="center", va="center",
        fontsize=18, fontweight="bold", color=ORANGE, zorder=4)
ax.text(RIGHT_X + PART_A + PART_B / 2, 2.0, "10 squares\nnever counted",
        ha="center", va="center", fontsize=12, color="#455A64",
        fontweight="bold", zorder=4,
        bbox=dict(boxstyle="round,pad=0.32", facecolor="white",
                  edgecolor=GREY, linewidth=1.0))
widths(RIGHT_X, BLUE, ORANGE)

ax.text(RIGHT_X + WIDTH / 2, 5.9, "Wrong: the 3 never reaches the 5",
        ha="center", va="center", fontsize=15, fontweight="bold", color=RED)
ax.text(RIGHT_X + WIDTH / 2, -1.3, r"$(3 \times 4) + 5 = 12 + 5 = 17$",
        ha="center", va="center", fontsize=15, color=INK)
ax.text(RIGHT_X + WIDTH / 2, -2.8, "Ten squares are lost.",
        ha="center", va="center", fontsize=14, color=RED, style="italic")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_forgetting_a_piece.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
