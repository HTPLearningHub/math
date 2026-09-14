"""Figure 6 - the most common percentage mistake, drawn on two grids.

Left panel: what you get if you write 3% as 0.3. That is 30 squares, ten times
too many. Right panel: 3% really is 0.03, which is only 3 squares.
The two grids are identical, so the size of the mistake is easy to see.
Run with:  python figures/fig_06_three_percent_is_not_zero_point_three.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

WRONG = "#C0392B"    # red - the wrong method
RIGHT = "#1E8449"    # green - the right method
EMPTY = "#ECEFF1"    # light grey - the squares nobody took
GRID = "#B0BEC5"     # grey - the lines between small squares

N = 10               # 10 by 10 = 100 small squares in each grid

# one entry per panel: (heading, squares shaded, colour, the line under the grid)
PANELS = [
    ("WRONG", 30, WRONG, r"$0.3 = \frac{3}{10} = \frac{30}{100} = 30\%$"),
    ("RIGHT", 3, RIGHT, r"$3\% = \frac{3}{100} = 0.03$"),
]
SUBTITLES = [r"writing $3\%$ as $0.3$", r"writing $3\%$ as $0.03$"]

fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.8))

for ax, (heading, shaded, colour, line), subtitle in zip(axes, PANELS, SUBTITLES):
    ax.axis("off")
    ax.set_aspect("equal")              # the small squares must look square
    ax.set_xlim(-0.6, N + 0.6)
    ax.set_ylim(-2.9, N + 2.6)

    count = 0
    for row in range(N - 1, -1, -1):    # fill from the top row downwards
        for col in range(N):
            fill = colour if count < shaded else EMPTY
            ax.add_patch(Rectangle((col, row), 1, 1,
                                   facecolor=fill, edgecolor=GRID, linewidth=0.8))
            count += 1

    ax.add_patch(Rectangle((0, 0), N, N,
                           facecolor="none", edgecolor=colour, linewidth=2.8))

    ax.text(N / 2, N + 1.95, heading, ha="center", va="center",
            fontsize=17, color=colour, fontweight="bold")
    ax.text(N / 2, N + 0.85, subtitle, ha="center", va="center",
            fontsize=13, color="#37474F")
    ax.text(N / 2, -0.95, f"{shaded} squares out of 100",
            ha="center", va="center", fontsize=12.5, color="#37474F")
    ax.text(N / 2, -2.2, line, ha="center", va="center",
            fontsize=15, color=colour, fontweight="bold")

fig.suptitle(r"$3\%$ is not $0.3$ - it is ten times smaller",
             fontsize=18, fontweight="bold", y=1.02)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_06_three_percent_is_not_zero_point_three.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
