"""Figure 4 - four third-slices make one whole pizza and one third left over.

Each pizza is cut into 3 equal slices. We collect 4 slices.
Three of them rebuild one whole pizza; the fourth one is the leftover part.
Run with:  python figures/fig_04_four_thirds.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from pathlib import Path

WHOLE = "#2E86DE"    # blue   - the slices that build one full pizza
EXTRA = "#E67E22"    # orange - the one extra slice
REST = "#ECEFF1"     # grey   - empty places on the plate
EDGE = "white"


def draw_pizza(ax, center, radius, parts, taken, color):
    """Draw one round pizza cut into `parts` equal slices; fill the first `taken`."""
    step = 360.0 / parts
    for i in range(parts):
        start = 90.0 + i * step
        fill = color if i < taken else REST
        ax.add_patch(Wedge(center, radius, start, start + step,
                           facecolor=fill, edgecolor=EDGE, linewidth=2.5))


fig, ax = plt.subplots(figsize=(10.0, 5.4))
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-3.9, 3.9)
ax.set_ylim(-2.2, 2.0)

R = 1.3
draw_pizza(ax, (-2.0, 0.15), R, parts=3, taken=3, color=WHOLE)   # 3 of 3 slices: one whole
draw_pizza(ax, (2.0, 0.15), R, parts=3, taken=1, color=EXTRA)    # 1 of 3 slices: the leftover

ax.text(0.0, 0.15, r"$+$", ha="center", va="center",             # the plus sign in the middle
        fontsize=42, fontweight="bold", color="#212121")

ax.text(-2.0, 1.8, "3 slices of 3 make\none whole pizza", ha="center", va="center",
        fontsize=13, color="#455A64", fontweight="bold")
ax.text(2.0, 1.8, "1 slice of 3 is left", ha="center", va="center",
        fontsize=13, color="#455A64", fontweight="bold")

ax.text(-2.0, -1.75, r"$\mathbf{\frac{3}{3} = 1}$", ha="center", va="center",
        fontsize=28, color=WHOLE)
ax.text(2.0, -1.75, r"$\mathbf{\frac{1}{3}}$", ha="center", va="center",
        fontsize=28, color=EXTRA)

ax.set_title(r"4 slices of size $\frac{1}{3}$:  $\frac{4}{3} = 1\frac{1}{3}$",
             fontsize=19, fontweight="bold", pad=14)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_four_thirds.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
