"""Figure 4 - one whole square cut into 100 small squares.

One small square is one hundredth (0.01).
One full column of ten small squares is one tenth (0.1), and it is also 10
hundredths - the picture shows that 0.1 and 0.10 are the same amount.
Run with:  python figures/fig_04_hundredths_grid.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

ONE_HUNDREDTH = "#E67E22"   # orange - the single small square
ONE_TENTH = "#2E86DE"       # blue   - the full column of ten small squares
EMPTY = "#FFFFFF"           # white  - the squares nobody took
GRID = "#B0BEC5"            # light grey - the lines of the grid
FRAME = "#546E7A"           # grey   - the outline of the whole square

N = 10                      # 10 rows and 10 columns, so 100 small squares

fig, ax = plt.subplots(figsize=(7.4, 7.0))
ax.axis("off")
ax.set_aspect("equal")      # the small squares must really look square
ax.set_xlim(-0.4, N + 3.9)
ax.set_ylim(-1.1, N + 0.9)

for row in range(N):
    for col in range(N):
        if col == 0 and row == N - 1:        # top-left square: one hundredth
            fill = ONE_HUNDREDTH
        elif col == 2:                       # the third column: one tenth
            fill = ONE_TENTH
        else:
            fill = EMPTY
        ax.add_patch(Rectangle((col, row), 1, 1,
                               facecolor=fill, edgecolor=GRID, linewidth=1.0))

ax.add_patch(Rectangle((0, 0), N, N,          # the outline of the one whole
                       facecolor="none", edgecolor=FRAME, linewidth=2.6))

# arrow pointing at the single orange square
ax.annotate(r"$1$ small square" "\n" r"$= \frac{1}{100} = 0.01$",
            xy=(0.5, N - 0.5), xytext=(N + 0.6, N - 0.4),
            ha="left", va="center", fontsize=13, color=ONE_HUNDREDTH, fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color=ONE_HUNDREDTH, linewidth=2.0, mutation_scale=22))

# arrow pointing at the blue column
ax.annotate(r"$10$ small squares" "\n" r"$= \frac{10}{100} = \frac{1}{10} = 0.1$",
            xy=(2.5, N / 2), xytext=(N + 0.6, N / 2),
            ha="left", va="center", fontsize=13, color=ONE_TENTH, fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color=ONE_TENTH, linewidth=2.0, mutation_scale=22))

ax.text(N / 2, -0.55, r"the whole square $= \frac{100}{100} = 1$",
        ha="center", va="center", fontsize=14, color=FRAME, fontweight="bold")

ax.set_title("One whole, cut into 100 equal squares", fontsize=16, fontweight="bold", pad=10)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_hundredths_grid.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
