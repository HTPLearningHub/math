"""Figure 3 - two whole pizzas and three extra slices, written as 2.3.

Every pizza is cut into 10 equal slices, because 10 slices is what makes the
tenths place work. The first two pizzas are eaten whole, the third one gives
only 3 slices. Together: 2 ones and 3 tenths, which is 2.3.
Run with:  python figures/fig_03_pizza_two_point_three.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from pathlib import Path

TAKEN = "#2E86DE"       # blue   - a slice that is taken
LEFT = "#ECEFF1"        # pale grey - a slice nobody took
CRUST = "#546E7A"       # grey   - the line around every slice
ONES = "#2E86DE"        # blue   - the label for the whole pizzas
TENTHS = "#E67E22"      # orange - the label for the extra slices

SLICES = 10             # every pizza is cut into 10 equal slices
R = 1.0                 # radius of one pizza

# one entry per pizza: centre, how many of its 10 slices are taken, colour of those slices
pizzas = [((0.0, 0.0), 10, TAKEN), ((2.6, 0.0), 10, TAKEN), ((5.2, 0.0), 3, TENTHS)]

fig, ax = plt.subplots(figsize=(11.0, 4.6))
ax.axis("off")
ax.set_aspect("equal")                  # a pizza must stay round
ax.set_xlim(-1.5, 6.7)
ax.set_ylim(-2.35, 1.9)

for (cx, cy), taken, taken_colour in pizzas:
    for k in range(SLICES):
        start = 90 - (k + 1) * 360 / SLICES        # slices go clockwise from the top
        end = 90 - k * 360 / SLICES
        colour = taken_colour if k < taken else LEFT
        ax.add_patch(Wedge((cx, cy), R, start, end,
                           facecolor=colour, edgecolor=CRUST, linewidth=1.6))

ax.text(0.0, -1.45, "1 whole pizza", ha="center", va="center",
        fontsize=13, fontweight="bold", color=ONES)
ax.text(2.6, -1.45, "1 whole pizza", ha="center", va="center",
        fontsize=13, fontweight="bold", color=ONES)
ax.text(5.2, -1.45, "3 slices out of 10", ha="center", va="center",
        fontsize=13, fontweight="bold", color=TENTHS)

# the reading of the picture, under the three pizzas
ax.text(1.3, -2.1, r"$2$ ones", ha="center", va="center",
        fontsize=15, fontweight="bold", color=ONES)
ax.text(5.2, -2.1, r"$3$ tenths $= \frac{3}{10}$", ha="center", va="center",
        fontsize=15, fontweight="bold", color=TENTHS)

ax.text(2.6, 1.55, r"$2\frac{3}{10} \;=\; \mathbf{2.3}$", ha="center", va="center",
        fontsize=22, color="#212121")

ax.set_title("Two whole pizzas and three tenths of a pizza",
             fontsize=16, fontweight="bold", pad=4)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_pizza_two_point_three.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
