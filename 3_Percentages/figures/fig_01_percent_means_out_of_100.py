"""Figure 1 - what the word "percent" means.

One whole square is cut into 100 equal small squares. 25 of them are shaded.
So the shaded part is 25 out of 100, which is exactly what "25 percent" means.
The picture is the definition: a percent is a small square in a grid of 100.
Run with:  python figures/fig_01_percent_means_out_of_100.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

TAKEN = "#E67E22"    # orange - the squares that belong to the percentage
EMPTY = "#ECEFF1"    # light grey - the squares nobody took
GRID = "#B0BEC5"     # grey - the thin lines between small squares
FRAME = "#546E7A"    # dark grey - the outline of the one whole
BLUE = "#2E86DE"     # blue - the label of the whole

N = 10               # 10 rows by 10 columns = 100 small squares
SHADED = 25          # how many small squares are shaded

fig, ax = plt.subplots(figsize=(8.6, 6.4))
ax.axis("off")
ax.set_aspect("equal")            # the small squares must look square
ax.set_xlim(-0.6, N + 8.2)
ax.set_ylim(-1.6, N + 1.0)

# draw the 100 small squares, filling them from the top-left, row by row
count = 0
for row in range(N - 1, -1, -1):          # start at the top row
    for col in range(N):                  # move left to right
        fill = TAKEN if count < SHADED else EMPTY
        ax.add_patch(Rectangle((col, row), 1, 1,
                               facecolor=fill, edgecolor=GRID, linewidth=0.9))
        count += 1

# the outline that says "this is one whole"
ax.add_patch(Rectangle((0, 0), N, N,
                       facecolor="none", edgecolor=FRAME, linewidth=2.6))

# the text block on the right, explaining the three ways to say the same thing
ax.text(N + 0.9, N - 1.0, "25 small squares are shaded",
        ha="left", va="center", fontsize=14, color=TAKEN, fontweight="bold")
ax.text(N + 0.9, N - 2.6, r"$25$ out of $100$",
        ha="left", va="center", fontsize=15, color="#37474F")
ax.text(N + 0.9, N - 4.2, r"$= \frac{25}{100}$",
        ha="left", va="center", fontsize=19, color="#37474F")
ax.text(N + 0.9, N - 6.0, r"$= 0.25$",
        ha="left", va="center", fontsize=19, color="#37474F")
ax.text(N + 0.9, N - 7.8, r"$= 25\%$",
        ha="left", va="center", fontsize=22, color=TAKEN, fontweight="bold")

# the label under the grid
ax.text(N / 2, -0.9, r"the whole square $= 100$ small squares $= 100\%$",
        ha="center", va="center", fontsize=14, color=BLUE, fontweight="bold")

ax.set_title("Percent means: how many out of one hundred",
             fontsize=17, fontweight="bold", pad=12)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_percent_means_out_of_100.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
