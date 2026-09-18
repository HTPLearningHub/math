"""Figure 4 - where the words "perfect square" come from.

The reader is asked to learn the first ten perfect squares, so it is
worth showing that the name is not decoration. A perfect square is a
count of dots that can be arranged into a square with nothing left over,
and its square root is the length of the side of that square.

Five squares are drawn, from 1 dot to 25 dots. Under each one there are
two lines: the power going forwards, and the root coming back.

Colour convention:
    blue   - the dots and the forward statement (squaring)
    orange - the backward statement (the root)
    grey   - the closing note

Horizontal plan (x): the five squares are centred at 1.60, 3.70, 5.95,
    8.45 and 11.20, with a dot every 0.42 in both directions, so the
    widest block (5 dots across) is 1.68 wide and clears its neighbour.

Vertical plan (y, top to bottom):
    4.85  figure heading
    3.63  the top row of the tallest square
    1.95  the bottom row of every square (they are all bottom-aligned)
    1.45  the squaring line, in blue
    0.95  the root line, in orange
    0.35  the closing note

Run with:  python figures/fig_04_perfect_squares.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # the dots, and squaring
ORANGE = "#E67E22"      # taking the root
GREY = "#78909C"
INK = "#212121"

W, H = 13.00, 5.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

STEP = 0.42             # the distance from one dot to the next
Y_BOTTOM = 1.95         # every square stands on this line

ax.text(0.40, 4.85,
        "a perfect square is a pile of dots that makes a square, and its "
        "root is the side of that square",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

for side, centre in ((1, 1.60), (2, 3.70), (3, 5.95), (4, 8.45),
                     (5, 11.20)):
    # the left-hand edge of this block, so that it is centred on "centre"
    x_start = centre - (side - 1) * STEP / 2

    for row in range(side):
        for col in range(side):
            ax.plot([x_start + col * STEP], [Y_BOTTOM + row * STEP],
                    marker="o", markersize=13, color=BLUE, zorder=2)

    # forwards: side, squared, gives the count of dots
    ax.text(centre, 1.45, "$%d^{2} = %d$" % (side, side * side),
            ha="center", va="center", fontsize=16, color=BLUE,
            fontweight="bold")
    # backwards: the count of dots, rooted, gives the side
    ax.text(centre, 0.95, r"$\sqrt{%d} = %d$" % (side * side, side),
            ha="center", va="center", fontsize=16, color=ORANGE,
            fontweight="bold")

ax.text(6.50, 0.35,
        "$2$, $3$, $5$, $6$, $7$ and $8$ dots cannot be arranged this way, "
        "so they are not perfect squares",
        ha="center", va="center", fontsize=13.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_perfect_squares.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_04_perfect_squares.png")
