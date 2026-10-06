"""Figure 2 - why (3 + 2)^2 is not 3^2 + 2^2.

A square of side 3 + 2 = 5 holds 25 small squares. Cut each side at 3, and
the square falls into four pieces: a 3 x 3 square, a 2 x 2 square, and two
3 x 2 strips. The wrong answer 3^2 + 2^2 = 13 counts only the two squares.
The two strips, 6 + 6 = 12, are what it forgets. This is the Chapter 6
rectangle (section 3) used twice.

Colour convention:
    blue   - the two squares that the wrong answer does count
    orange - the two strips that the wrong answer forgets
    green  - the correct general statement at the bottom of the text column
    grey   - the grid of small squares, measuring labels

Horizontal plan (x): the big square runs 0.90 - 5.40; text from 6.40.
Vertical plan (y): the big square runs 0.60 - 5.10; heading at 6.15.

Run with:  python figures/fig_02_square_of_a_sum.py
"""

import matplotlib
matplotlib.use("Agg")                      # draw to a file, never to a window
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"                           # the two squares
BLUE_T = "#D6E9FA"
ORANGE = "#E67E22"                         # the two forgotten strips
ORANGE_T = "#FCE5CF"
GREEN = "#1E8449"                          # the correct general rule
GREY = "#78909C"
INK = "#212121"

W, H = 13.0, 6.6
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")                     # squares must look square

ax.text(0.40, 6.15, "squaring a sum makes four pieces, not two",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

ox, oy, u = 0.90, 0.60, 0.90               # lower-left corner and one small square
a, b = 3, 2                                # the two parts of each side
top = oy + (a + b) * u                     # y of the top edge

# the four pieces: (x_left, y_bottom, width, height, fill, edge, label)
# columns: a then b, left to right; rows: a then b, top to bottom
pieces = [
    (ox, top - a * u, a * u, a * u, BLUE_T, BLUE, r"$3^{2} = 9$"),
    (ox + a * u, top - a * u, b * u, a * u, ORANGE_T, ORANGE,
     r"$3 \times 2$" + "\n" + r"$= 6$"),
    (ox, oy, a * u, b * u, ORANGE_T, ORANGE, r"$3 \times 2 = 6$"),
    (ox + a * u, oy, b * u, b * u, BLUE_T, BLUE, r"$2^{2} = 4$"),
]
for x0, y0, w, h, fill, edge, label in pieces:
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=fill, edgecolor="none",
                           zorder=0))

# the grid of 25 small squares, so they can be counted
for k in range(a + b + 1):
    ax.plot([ox + k * u, ox + k * u], [oy, top], color=GREY, lw=0.6, zorder=1)
    ax.plot([ox, ox + (a + b) * u], [oy + k * u, oy + k * u], color=GREY,
            lw=0.6, zorder=1)

# the piece outlines and labels, on top of the grid
for x0, y0, w, h, fill, edge, label in pieces:
    ax.add_patch(Rectangle((x0, y0), w, h, fill=False, edgecolor=edge,
                           linewidth=2.4, zorder=2))
    ax.text(x0 + w / 2, y0 + h / 2, label, ha="center", va="center",
            fontsize=17, color=edge, fontweight="bold", zorder=3,
            linespacing=1.3,
            bbox=dict(facecolor="white", edgecolor="none", pad=2, alpha=0.85))

# side labels along the top: 3 then 2
ax.text(ox + a * u / 2, top + 0.30, "3", ha="center", va="center",
        fontsize=17, color=INK)
ax.text(ox + a * u + b * u / 2, top + 0.30, "2", ha="center", va="center",
        fontsize=17, color=INK)
# side labels down the left: 3 then 2
ax.text(ox - 0.30, top - a * u / 2, "3", ha="center", va="center",
        fontsize=17, color=INK)
ax.text(ox - 0.30, oy + b * u / 2, "2", ha="center", va="center",
        fontsize=17, color=INK)

# the text column
tx = 6.40
ax.text(tx, 4.85, r"the whole square:  $(3 + 2)^{2} = 5^{2} = 25$",
        ha="left", va="center", fontsize=18, color=INK)
ax.text(tx, 3.95, r"the blue squares:  $3^{2} + 2^{2} = 9 + 4 = 13$",
        ha="left", va="center", fontsize=18, color=BLUE)
ax.text(tx, 3.05, r"the orange strips:  $6 + 6 = 12$",
        ha="left", va="center", fontsize=18, color=ORANGE)
ax.text(tx, 2.15, r"together:  $13 + 12 = 25$",
        ha="left", va="center", fontsize=18, color=INK)
ax.plot([tx, tx + 6.2], [1.55, 1.55], color=GREY, lw=1.0, ls="--")
ax.text(tx, 0.95, r"$(a + b)^{2} = a^{2} + 2ab + b^{2}$",
        ha="left", va="center", fontsize=24, color=GREEN)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_square_of_a_sum.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_02_square_of_a_sum.png")
