"""Figure 1 - a root is the operation that undoes a power.

The chapter opens by saying that every operation in the book so far has
had an "undo", and that exponentiation (Chapter 10) has never been given
one. This figure is the picture of that sentence, in the one place where
squaring is something you can actually see: a square.

Left panel:  a square whose side is 5 units, cut into 25 small squares.
             Going from the side to the number of small squares is
             squaring. Going back is taking the square root.
Right panel: the same two journeys with no picture at all - two cards
             and two arrows, one in each direction.

Colour convention for the chapter, carried on from Chapters 10 and 23:
    blue   - the number we start from, and the forward direction
    orange - the root, and the backward direction
    grey   - quiet labels and rules

Horizontal plan (x): left panel 0.40-5.90, right panel 6.20-12.60.
    The 5x5 grid of small squares runs 1.60-4.70, each cell 0.62 wide.
    In the right panel the "5" card sits at 7.55 and the "25" card at
    11.25, and both arrows run between 8.25 and 10.55.

Vertical plan (y, top to bottom):
    6.00  figure heading
    5.55  top of both panels
    5.05  "25 small squares in it" over the grid
    4.45  top row of the grid (the grid runs down to 1.35)
    0.95  "the side is 5" under the grid
    0.45  bottom of both panels
    In the right panel: 4.55 the forward label, 4.05 the forward arrow,
    3.10 the two cards, 2.15 the backward arrow, 1.65 the backward label,
    0.85 the closing sentence.

Run with:  python figures/fig_01_undoing_a_power.py
"""

import matplotlib
matplotlib.use("Agg")                       # draw to a file, never to a window
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"        # the forward journey: squaring
ORANGE = "#E67E22"      # the backward journey: the root
GREY = "#78909C"        # quiet labels
INK = "#212121"         # ordinary text
BLUE_T = "#E9F2FC"      # pale blue fill
ORANGE_T = "#FDF0E3"    # pale orange fill

W, H = 13.00, 6.40
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])               # the axes fill the whole canvas
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def panel(x_left, x_right, colour):
    """The rounded outline behind one half of the figure."""
    ax.add_patch(FancyBboxPatch(
        (x_left, 0.45), x_right - x_left, 5.10,
        boxstyle="round,pad=0.0,rounding_size=0.18",
        facecolor="white", edgecolor=colour, linewidth=1.8, zorder=0))


def card(x, y, text, edge, fill, fontsize=26):
    """A rounded box holding one number."""
    ax.text(x, y, text, ha="center", va="center", fontsize=fontsize,
            color=INK, zorder=3,
            bbox=dict(boxstyle="round,pad=0.42", facecolor=fill,
                      edgecolor=edge, linewidth=2.0))


ax.text(0.40, 6.00,
        "squaring turns a side into an area; a square root turns the "
        "area back into the side",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# =============================================================== left panel
panel(0.40, 5.90, BLUE)

CELL = 0.62                                  # the width of one small square
X0, Y0 = 1.60, 1.35                          # bottom-left corner of the grid

ax.text(3.15, 5.05, "a square with a side of $5$",
        ha="center", va="center", fontsize=16, color=INK, fontweight="bold")

# the 25 small squares, drawn one at a time so the grid lines are visible
for row in range(5):
    for col in range(5):
        ax.add_patch(Rectangle(
            (X0 + col * CELL, Y0 + row * CELL), CELL, CELL,
            facecolor=BLUE_T, edgecolor=BLUE, linewidth=1.2, zorder=1))

# the measuring label under the grid
ax.annotate("", xy=(X0 + 5 * CELL, 1.08), xytext=(X0, 1.08),
            arrowprops=dict(arrowstyle="<|-|>", linewidth=1.5, color=BLUE))
ax.text(3.15, 0.78, "the side is $5$", ha="center", va="center",
        fontsize=15, color=BLUE, fontweight="bold")

# the measuring label to the left of the grid
ax.annotate("", xy=(1.32, Y0 + 5 * CELL), xytext=(1.32, Y0),
            arrowprops=dict(arrowstyle="<|-|>", linewidth=1.5, color=BLUE))
ax.text(1.00, 2.90, "$5$", ha="center", va="center", fontsize=15,
        color=BLUE, fontweight="bold")

# the count, written inside the grid area but above it so nothing is hidden
ax.text(3.15, 4.75, "it holds $25$ small squares", ha="center", va="center",
        fontsize=14, color=GREY)

# ============================================================== right panel
panel(6.20, 12.60, ORANGE)

card(7.55, 3.10, "$5$", BLUE, BLUE_T)
card(11.25, 3.10, "$25$", ORANGE, ORANGE_T)

# forward: squaring
ax.add_patch(FancyArrowPatch((8.25, 4.05), (10.55, 4.05),
                             arrowstyle="-|>", mutation_scale=24,
                             linewidth=3.0, color=BLUE, zorder=2))
ax.text(9.40, 4.58, "square it", ha="center", va="center", fontsize=16,
        color=BLUE, fontweight="bold")
ax.text(9.40, 3.72, "$5^{2} = 5 \\times 5 = 25$", ha="center", va="center",
        fontsize=15, color=BLUE)

# backward: the square root
ax.add_patch(FancyArrowPatch((10.55, 2.15), (8.25, 2.15),
                             arrowstyle="-|>", mutation_scale=24,
                             linewidth=3.0, color=ORANGE, zorder=2))
ax.text(9.40, 2.52, "$\\sqrt{25} = 5$", ha="center", va="center",
        fontsize=15, color=ORANGE)
ax.text(9.40, 1.68, "take the square root", ha="center", va="center",
        fontsize=16, color=ORANGE, fontweight="bold")

ax.text(9.40, 0.85, "the two arrows cancel each other out",
        ha="center", va="center", fontsize=13.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_undoing_a_power.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_01_undoing_a_power.png")
