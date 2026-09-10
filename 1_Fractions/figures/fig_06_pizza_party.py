"""Figure 6 - 30 slices of size one eighth, laid out as whole pizzas.

Three pizzas are complete (24 slices). The fourth pizza holds the last 6 slices.
That is why 30 eighths is the same as 3 whole pizzas and three quarters of one.
Run with:  python figures/fig_06_pizza_party.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from pathlib import Path

WHOLE = "#2E86DE"    # blue   - a pizza that is completely used
EXTRA = "#E67E22"    # orange - the slices left over on the last pizza
REST = "#ECEFF1"     # grey   - the empty places on the last pizza
EDGE = "white"


def draw_pizza(ax, center, radius, parts, taken, color):
    """Draw one round pizza cut into `parts` equal slices; fill the first `taken`."""
    step = 360.0 / parts
    for i in range(parts):
        start = 90.0 + i * step
        fill = color if i < taken else REST
        ax.add_patch(Wedge(center, radius, start, start + step,
                           facecolor=fill, edgecolor=EDGE, linewidth=2.2))


fig, ax = plt.subplots(figsize=(12.0, 4.4))
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-1.4, 11.0)
ax.set_ylim(-2.4, 1.9)

R = 1.15                                                   # radius of every pizza
positions = [0.0, 3.2, 6.4, 9.6]                           # where the four pizzas stand
filled = [8, 8, 8, 6]                                      # slices used on each pizza
colors = [WHOLE, WHOLE, WHOLE, EXTRA]                      # last pizza gets the other colour
notes = [r"$\frac{8}{8} = 1$", r"$\frac{8}{8} = 1$", r"$\frac{8}{8} = 1$",
         r"$\frac{6}{8} = \frac{3}{4}$"]

for x, taken, color, note in zip(positions, filled, colors, notes):
    draw_pizza(ax, (x, 0.0), R, parts=8, taken=taken, color=color)
    ax.text(x, 1.55, f"{taken} slices", ha="center", va="center",
            fontsize=13, fontweight="bold", color="#455A64")
    ax.text(x, -1.95, note, ha="center", va="center",
            fontsize=20, fontweight="bold", color=color)

ax.set_title(r"30 slices of size $\frac{1}{8}$:  $\frac{30}{8} = 3\frac{3}{4}$ pizzas",
             fontsize=19, fontweight="bold", pad=12)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_pizza_party.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
