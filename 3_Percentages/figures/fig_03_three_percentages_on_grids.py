"""Figure 3 - 50%, 80% and 3% drawn on three identical grids of 100 squares.

Every grid is the same whole. Only the number of shaded squares changes.
The picture makes the size of each percentage easy to see, and it shows why
3% is a very small amount while 80% is almost everything.
Run with:  python figures/fig_03_three_percentages_on_grids.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

TAKEN = "#E67E22"    # orange - the shaded squares
EMPTY = "#ECEFF1"    # light grey - the squares nobody took
GRID = "#B0BEC5"     # grey - the lines between small squares
FRAME = "#546E7A"    # dark grey - the outline of one whole

N = 10               # each grid is 10 by 10 = 100 small squares

# one entry per grid: (how many squares are shaded, the label under the grid)
PANELS = [
    (50, r"$50\% = \frac{50}{100} = \frac{1}{2} = 0.50$"),
    (80, r"$80\% = \frac{80}{100} = \frac{4}{5} = 0.80$"),
    (3,  r"$3\% = \frac{3}{100} = 0.03$"),
]

fig, axes = plt.subplots(1, 3, figsize=(12.6, 5.0))

for ax, (shaded, label) in zip(axes, PANELS):
    ax.axis("off")
    ax.set_aspect("equal")               # small squares must look square
    ax.set_xlim(-0.5, N + 0.5)
    ax.set_ylim(-2.6, N + 0.9)

    count = 0
    for row in range(N - 1, -1, -1):     # fill from the top row downwards
        for col in range(N):
            fill = TAKEN if count < shaded else EMPTY
            ax.add_patch(Rectangle((col, row), 1, 1,
                                   facecolor=fill, edgecolor=GRID, linewidth=0.8))
            count += 1

    ax.add_patch(Rectangle((0, 0), N, N,
                           facecolor="none", edgecolor=FRAME, linewidth=2.4))

    ax.text(N / 2, -0.85, f"{shaded} squares out of 100",
            ha="center", va="center", fontsize=12, color="#37474F")
    ax.text(N / 2, -2.0, label,
            ha="center", va="center", fontsize=15, color=TAKEN, fontweight="bold")

fig.suptitle("The same whole, three different percentages",
             fontsize=17, fontweight="bold", y=0.99)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_three_percentages_on_grids.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
