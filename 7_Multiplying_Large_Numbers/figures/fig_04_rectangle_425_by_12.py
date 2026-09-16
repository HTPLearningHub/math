"""Figure 4 - 425 x 12 drawn as a rectangle, cut into the two partial products.

This is the Chapter 6 area model applied to the two rows of the standard
algorithm. The rectangle is 425 wide and 12 tall, so its area is the answer we
want. Cutting it at height 10 produces exactly the two rows of the written
method: the tall blue piece is 425 x 10 = 4250 and the short orange piece is
425 x 2 = 850.

A word about scale. The two heights are drawn in the true proportion, 10 to 2,
so the blue piece really is five times as tall as the orange one. The width is
deliberately squashed: 425 units beside 12 units would be a hair-thin ribbon
on the page, and nothing written in it could be read. The picture says so at
the bottom, and so does the caption in the chapter.

Three height marks are drawn on the left, not two: 10 for the blue piece, 2
for the orange one, and 12 for the pair of them together. The outer mark is
what makes the cut look like a cut rather than like two unrelated boxes.

Colours match figure 3: blue for the row that comes from the tens digit of 12,
orange for the row that comes from the ones digit.
Run with:  python figures/fig_04_rectangle_425_by_12.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"
BLUE_FILL = "#EAF2FB"
ORANGE = "#E67E22"
ORANGE_FILL = "#FDF0E3"
GREY = "#78909C"
INK = "#212121"

# The drawing box, in figure units. 4.25 units of height stand for a height of
# 10 and 0.85 units for a height of 2, so the two heights keep their true
# proportion of five to one.
X0, X1 = 2.05, 9.55                 # left and right edge of the rectangle
Y0 = 1.55                           # bottom edge
H_ORANGE = 0.85                     # stands for a height of 2
H_BLUE = 4.25                       # stands for a height of 10
Y_TOP = Y0 + H_ORANGE + H_BLUE      # top edge

W, H = 12.20, 7.60                  # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# ---- the two pieces of the rectangle ----------------------------------------
ax.add_patch(Rectangle((X0, Y0), X1 - X0, H_ORANGE,
                       facecolor=ORANGE_FILL, edgecolor=ORANGE, linewidth=2.4))
ax.add_patch(Rectangle((X0, Y0 + H_ORANGE), X1 - X0, H_BLUE,
                       facecolor=BLUE_FILL, edgecolor=BLUE, linewidth=2.4))

MID = (X0 + X1) / 2
ax.text(MID, Y0 + H_ORANGE + H_BLUE / 2, r"$425 \times 10 = 4250$",
        ha="center", va="center", fontsize=26, color=BLUE, fontweight="bold")
ax.text(MID, Y0 + H_ORANGE / 2, r"$425 \times 2 = 850$",
        ha="center", va="center", fontsize=20, color=ORANGE, fontweight="bold")


# ---- the height of each piece, and of the pair, marked on the left ----------
def height_mark(x, y_lo, y_hi, label, colour, fontsize):
    """Draw a vertical bar with two end ticks, and name the height beside it."""
    ax.plot([x, x], [y_lo, y_hi], color=colour, linewidth=2.2)
    for y in (y_lo, y_hi):
        ax.plot([x - 0.10, x + 0.10], [y, y], color=colour, linewidth=2.2)
    ax.text(x - 0.20, (y_lo + y_hi) / 2, label, ha="right", va="center",
            fontsize=fontsize, color=colour, fontweight="bold")


height_mark(X0 - 0.40, Y0 + H_ORANGE, Y_TOP, r"$10$", BLUE, 21)
height_mark(X0 - 0.40, Y0, Y0 + H_ORANGE, r"$2$", ORANGE, 21)
height_mark(X0 - 1.25, Y0, Y_TOP, r"height $12$", INK, 17)

# ---- the width, marked underneath -------------------------------------------
y = Y0 - 0.42
ax.plot([X0, X1], [y, y], color=INK, linewidth=2.0)
for x in (X0, X1):
    ax.plot([x, x], [y - 0.10, y + 0.10], color=INK, linewidth=2.0)
ax.text(MID, y - 0.30, r"width $425$", ha="center", va="top",
        fontsize=19, color=INK, fontweight="bold")

# ---- the arithmetic that reads the picture ----------------------------------
ax.add_patch(FancyBboxPatch((9.95, Y0 + 1.70), 2.00, 2.05,
                            boxstyle="round,pad=0.06,rounding_size=0.14",
                            facecolor="#FAFAFA", edgecolor=GREY, linewidth=1.8))
ax.text(10.95, Y0 + 3.30, "the whole\nrectangle", ha="center", va="center",
        fontsize=13.5, color=GREY, fontweight="bold")
ax.text(10.95, Y0 + 2.66, r"$4250$", ha="center", va="center",
        fontsize=18, color=BLUE, fontweight="bold")
ax.text(10.95, Y0 + 2.26, r"$+\ \ 850$", ha="center", va="center",
        fontsize=18, color=ORANGE, fontweight="bold")
ax.plot([10.35, 11.55], [Y0 + 2.06, Y0 + 2.06], color=INK, linewidth=1.8)
ax.text(10.95, Y0 + 1.86, r"$5100$", ha="center", va="center",
        fontsize=18, color=INK, fontweight="bold")

# ---- the two sentences that carry the whole point ---------------------------
ax.text(MID, Y_TOP + 0.62,
        "one rectangle, cut in two: the pieces must add back up to the whole",
        ha="center", va="center", fontsize=19, color=INK, fontweight="bold")
ax.text(MID, Y_TOP + 0.24,
        "so the two rows of the written method are the two pieces of this cut",
        ha="center", va="center", fontsize=14.5, color=GREY, fontweight="bold")
ax.text(MID, 0.22,
        "the two heights are in their true proportion; the width is drawn short,"
        " so that the picture fits on the page",
        ha="center", va="center", fontsize=12.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_rectangle_425_by_12.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
