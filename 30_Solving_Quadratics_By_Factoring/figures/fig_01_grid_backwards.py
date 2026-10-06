"""Figure 1 - factoring x^2 + 7x + 10 is filling the FOIL grid backwards.

Left panel: the 2 by 2 grid of Chapter 29, fig_01, but with only the corner
boxes known (x^2 and 10). The two side numbers are question marks, and the
two middle boxes are question marks that must add up to 7x.
Right panel: the same grid filled in with 5 and 2: boxes x^2, 2x, 5x, 10.
Below each grid: the two conditions (multiply to 10, add to 7).

Colours follow Chapter 29: blue First, orange Outer, teal Inner, purple
Last; green for the found answer, red for the unknowns, grey labels.

Run with:  python figures/fig_01_grid_backwards.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
GREEN = "#1E8449"
RED = "#C0392B"
BLUE, ORANGE, TEAL, PURPLE = "#2E86DE", "#E67E22", "#138D75", "#8E44AD"

fig, axes = plt.subplots(1, 2, figsize=(14, 7.4))


def grid(ax, side_top, side_left, cells, title, side_col):
    """Draw one 2 by 2 grid.

    side_top / side_left: the two terms written along the top / left edge.
    cells: four (text, colour) pairs in the order First, Outer, Inner, Last.
    side_col: colour of the first and of the second side term.
    """
    ax.set_xlim(-1.4, 4.4)
    ax.set_ylim(-2.2, 4.4)
    ax.set_aspect("equal")                         # boxes stay square
    ax.axis("off")
    ax.set_title(title, fontsize=20, color=INK, pad=6)
    pos = [(0, 1), (1, 1), (0, 0), (1, 0)]         # F, O, I, L; row 1 = top
    for (cx, cy), (txt, col) in zip(pos, cells):
        ax.add_patch(Rectangle((cx * 1.6, cy * 1.6), 1.6, 1.6,
                               facecolor=col, alpha=0.15,
                               edgecolor=col, lw=2.5))
        ax.text(cx * 1.6 + 0.8, cy * 1.6 + 0.8, txt, ha="center",
                va="center", fontsize=24, color=col, fontweight="bold")
    for i, t in enumerate(side_top):               # second bracket, on top
        ax.text(i * 1.6 + 0.8, 3.55, t, ha="center", va="center",
                fontsize=24, color=side_col[i])
    for i, t in enumerate(side_left):              # first bracket, on left
        ax.text(-0.65, (1 - i) * 1.6 + 0.8, t, ha="center", va="center",
                fontsize=24, color=side_col[i])


# --- left: what we are given -------------------------------------------------
grid(axes[0], [r"$x$", r"$?$"], [r"$x$", r"$?$"],
     [(r"$x^{2}$", BLUE), (r"$?$", RED), (r"$?$", RED), (r"$10$", PURPLE)],
     r"Given:  $x^{2} + 7x + 10$", [INK, RED])
axes[0].text(1.6, -0.7, r"the two middle boxes must add to $7x$",
             ha="center", va="center", fontsize=16, color=RED)
axes[0].text(1.6, -1.45, r"the two side numbers must multiply to $10$",
             ha="center", va="center", fontsize=16, color=RED)

# --- right: the grid filled in ----------------------------------------------
grid(axes[1], [r"$x$", r"$+2$"], [r"$x$", r"$+5$"],
     [(r"$x^{2}$", BLUE), (r"$2x$", ORANGE), (r"$5x$", TEAL),
      (r"$10$", PURPLE)],
     r"Found:  $(x + 5)(x + 2)$", [INK, GREEN])
axes[1].text(1.6, -0.7, r"$2x + 5x = 7x$   and   $5 \times 2 = 10$",
             ha="center", va="center", fontsize=16, color=GREEN)
axes[1].text(1.6, -1.45, r"so  $x^{2} + 7x + 10 = (x + 5)(x + 2)$",
             ha="center", va="center", fontsize=16, color=GREEN,
             fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_grid_backwards.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_01_grid_backwards.png")
