"""Figure 3 - 3 slices of an 8-slice pizza against 3 slices of a 10-slice pizza.

Both plates hold 3 slices, but the slices on the left are bigger,
so the left plate holds more pizza.
Run with:  python figures/fig_03_comparing_fractions.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from pathlib import Path

FIRST = "#2E86DE"    # blue   - the 8-slice pizza
SECOND = "#E67E22"   # orange - the 10-slice pizza
REST = "#ECEFF1"     # grey   - slices nobody took
EDGE = "white"


def draw_pizza(ax, center, radius, parts, taken, color):
    """Draw one round pizza cut into `parts` equal slices; fill the first `taken`."""
    step = 360.0 / parts
    for i in range(parts):
        start = 90.0 + i * step
        fill = color if i < taken else REST
        ax.add_patch(Wedge(center, radius, start, start + step,
                           facecolor=fill, edgecolor=EDGE, linewidth=2.5))


fig, ax = plt.subplots(figsize=(10.0, 5.6))
ax.set_aspect("equal")                                    # equal sizes must stay equal
ax.axis("off")
ax.set_xlim(-3.9, 3.9)
ax.set_ylim(-2.3, 2.0)

R = 1.35                                                  # the two pizzas are the same size
draw_pizza(ax, (-2.1, 0.1), R, parts=8, taken=3, color=FIRST)
draw_pizza(ax, (2.1, 0.1), R, parts=10, taken=3, color=SECOND)

ax.text(0.0, 0.1, r"$>$", ha="center", va="center",       # the "greater than" sign
        fontsize=44, fontweight="bold", color="#212121")

ax.text(-2.1, 1.85, "8 slices in the pizza:\nbig slices", ha="center", va="center",
        fontsize=13, color="#455A64", fontweight="bold")
ax.text(2.1, 1.85, "10 slices in the pizza:\nsmall slices", ha="center", va="center",
        fontsize=13, color="#455A64", fontweight="bold")

ax.text(-2.1, -1.9, r"$\mathbf{\frac{3}{8}}$", ha="center", va="center",
        fontsize=34, color=FIRST)
ax.text(2.1, -1.9, r"$\mathbf{\frac{3}{10}}$", ha="center", va="center",
        fontsize=34, color=SECOND)

ax.set_title("Same number of slices, different slice size",
             fontsize=17, fontweight="bold", pad=14)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_comparing_fractions.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
