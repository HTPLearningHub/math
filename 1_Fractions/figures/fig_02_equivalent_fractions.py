"""Figure 2 - two pizzas that give you the same amount of food.

Left: one pizza cut into 8 slices, 2 slices taken.
Right: one pizza of the same size cut into 4 slices, 1 slice taken.
The blue area and the orange area are equal, so the two fractions are equal.
Run with:  python figures/fig_02_equivalent_fractions.py
"""

import matplotlib
matplotlib.use("Agg")                                     # save to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from pathlib import Path

FIRST = "#2E86DE"    # blue   - the left pizza
SECOND = "#E67E22"   # orange - the right pizza
REST = "#ECEFF1"     # grey   - the slices nobody took
EDGE = "white"       # the cut lines


def draw_pizza(ax, center, radius, parts, taken, color):
    """Draw one round pizza cut into `parts` equal slices; fill the first `taken`."""
    step = 360.0 / parts                                  # degrees in one slice
    for i in range(parts):
        start = 90.0 + i * step                           # start the first cut at the top
        fill = color if i < taken else REST               # taken slices get the strong colour
        ax.add_patch(Wedge(center, radius, start, start + step,
                           facecolor=fill, edgecolor=EDGE, linewidth=2.5))


fig, ax = plt.subplots(figsize=(10.0, 5.6))
ax.set_aspect("equal")                                    # both pizzas must stay round
ax.axis("off")
ax.set_xlim(-3.9, 3.9)
ax.set_ylim(-2.3, 2.0)

R = 1.35                                                  # both pizzas have the same size
draw_pizza(ax, (-2.1, 0.1), R, parts=8, taken=2, color=FIRST)
draw_pizza(ax, (2.1, 0.1), R, parts=4, taken=1, color=SECOND)

ax.text(0.0, 0.1, r"$=$", ha="center", va="center",       # the equals sign in the middle
        fontsize=44, fontweight="bold", color="#212121")

ax.text(-2.1, 1.85, "cut into 8 slices, take 2",          # what happened on the left
        ha="center", va="center", fontsize=13, color="#455A64", fontweight="bold")
ax.text(2.1, 1.85, "cut into 4 slices, take 1",           # what happened on the right
        ha="center", va="center", fontsize=13, color="#455A64", fontweight="bold")

ax.text(-2.1, -1.85, r"$\mathbf{\frac{2}{8}}$", ha="center", va="center",
        fontsize=34, color=FIRST)                         # the left fraction
ax.text(2.1, -1.85, r"$\mathbf{\frac{1}{4}}$", ha="center", va="center",
        fontsize=34, color=SECOND)                        # the right fraction

ax.set_title("The same amount of pizza, written in two ways",
             fontsize=17, fontweight="bold", pad=14)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_equivalent_fractions.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
