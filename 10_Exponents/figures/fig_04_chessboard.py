"""Figure 4 - the chessboard from the legend, with the count on every square.

Square number n carries 2^(n-1) grains. The number itself is far too long to
print on a square, so the squares are shaded instead: the darker the square,
the more grains sit on it. The shade is taken from the exponent, n - 1, not
from the count, because the count runs to nineteen digits and any scale
built on it would leave sixty-three squares white.

The four row endings and the last square are listed on the right, because
those are the numbers the text quotes.
Run with:  python figures/fig_04_chessboard.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

PURPLE = "#8E44AD"
GREY = "#78909C"
INK = "#212121"

W, H = 12.6, 6.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")                     # the squares must stay square

CELL = 0.60                                # the side of one square, in inches
X0, Y_TOP = 0.55, 5.20                     # top-left corner of the board
shade = plt.get_cmap("Purples")

for n in range(1, 65):
    row, col = (n - 1) // 8, (n - 1) % 8
    x = X0 + col * CELL
    y = Y_TOP - (row + 1) * CELL
    # 0.10 keeps square 1 visible; 0.92 stops square 64 going pure black
    t = 0.10 + 0.82 * (n - 1) / 63
    ax.add_patch(Rectangle((x, y), CELL, CELL, facecolor=shade(t),
                           edgecolor="white", linewidth=1.4))
    # the exponent is short enough to print, so every square carries it
    ax.text(x + CELL / 2, y + CELL / 2, rf"$2^{{{n - 1}}}$",
            ha="center", va="center", fontsize=10.5,
            color="white" if t > 0.55 else INK)

ax.text(X0 + 4 * CELL, Y_TOP + 0.30, "What each square carries",
        ha="center", va="center", fontsize=15.5, color=INK, fontweight="bold")
ax.text(X0 + 4 * CELL, Y_TOP - 8 * CELL - 0.30,
        "one grain on the first square, then double it every square",
        ha="center", va="center", fontsize=13, color=GREY)

# the numbers the text quotes, listed beside the board
X_LIST = X0 + 8 * CELL + 0.65
ax.text(X_LIST, 5.28, "The squares worth stopping at",
        ha="left", va="center", fontsize=15.5, color=INK, fontweight="bold")

QUOTED = [("square 8, end of row 1", r"$2^{7} = 128$ grains"),
          ("square 16, end of row 2", r"$2^{15} = 32\,768$"),
          ("square 24, end of row 3", r"$2^{23} = 8\,388\,608$"),
          ("square 32, end of row 4", r"$2^{31} = 2\,147\,483\,648$"),
          ("square 64, the last one", r"$2^{63} = 9\,223\,372\,036\,854\,775\,808$")]

for k, (where, what) in enumerate(QUOTED):
    y = 4.62 - k * 0.86
    ax.text(X_LIST, y, where, ha="left", va="center", fontsize=12.5, color=GREY)
    ax.text(X_LIST, y - 0.34, what, ha="left", va="center",
            fontsize=14.5, color=PURPLE if k == 4 else INK,
            fontweight="bold" if k == 4 else "normal")

ax.text(X_LIST, 0.38,
        "Row 3 ends at eight million grains. Five rows still to go.",
        ha="left", va="center", fontsize=13.5, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_chessboard.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
