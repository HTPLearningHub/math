"""Figure 6 - 0.5 against 0.125, on two bars of the same length.

Both bars are one whole and both are cut into ten tenths.
0.5 fills five tenths. 0.125 does not even fill two tenths.
So the number with more digits after the point is the smaller one.
Run with:  python figures/fig_06_compare_decimals.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BIGGER = "#2E86DE"    # blue   - the bigger number, 0.5
SMALLER = "#E67E22"   # orange - the smaller number, 0.125
EMPTY = "#ECEFF1"     # pale grey - the part that is not filled
GRID = "#B0BEC5"      # light grey - the tenth lines
FRAME = "#546E7A"     # grey   - the outline of the bar

BAR_W, BAR_H = 10.0, 1.15                # one whole is 10 units wide on the picture

# one tuple per bar: (value, y position, colour, the words under the bar)
bars = [
    (0.5, 1.75, BIGGER, r"$0.5$ fills $5$ tenths"),
    (0.125, 0.0, SMALLER, r"$0.125$ does not fill $2$ tenths"),
]

fig, ax = plt.subplots(figsize=(11.5, 4.6))
ax.axis("off")
ax.set_xlim(-2.9, BAR_W + 0.6)
ax.set_ylim(-0.95, 3.55)

for value, y, colour, caption in bars:
    ax.add_patch(Rectangle((0, y), BAR_W, BAR_H, facecolor=EMPTY, edgecolor="none"))
    ax.add_patch(Rectangle((0, y), BAR_W * value, BAR_H, facecolor=colour, edgecolor="none"))
    for k in range(1, 10):                                  # the ten tenths
        ax.plot([k, k], [y, y + BAR_H], color=GRID, linewidth=1.1)
    ax.add_patch(Rectangle((0, y), BAR_W, BAR_H,
                           facecolor="none", edgecolor=FRAME, linewidth=2.2))
    ax.text(-0.4, y + BAR_H / 2, f"${value}$", ha="right", va="center",
            fontsize=20, fontweight="bold", color=colour)
    ax.text(BAR_W / 2, y - 0.28, caption, ha="center", va="top",
            fontsize=13, color=colour, fontweight="bold")

# the line that shows where 0.125 stops, carried up to the other bar
ax.plot([BAR_W * 0.125, BAR_W * 0.125], [0, 1.75 + BAR_H],
        color=SMALLER, linewidth=1.6, linestyle=(0, (5, 4)))

ax.text(-2.75, 3.18, r"both bars are the same whole, cut into ten tenths",
        ha="left", va="center", fontsize=12.5, color=FRAME)

ax.set_title(r"More digits after the point does not mean a bigger number",
             fontsize=16, fontweight="bold", pad=10)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_compare_decimals.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
