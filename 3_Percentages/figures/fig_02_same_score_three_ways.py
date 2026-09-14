"""Figure 2 - three quiz scores with different totals are the same proportion.

9 out of 10, 18 out of 20 and 450 out of 500 look like three different scores.
Each bar is the same length, because each bar is one whole quiz.
Only the number of pieces changes. The shaded part stops at the same place
every time, and that place is 90 out of 100 - that is, 90 percent.
Run with:  python figures/fig_02_same_score_three_ways.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

TAKEN = "#E67E22"     # orange - the points the student earned
EMPTY = "#ECEFF1"     # light grey - the points the student lost
LINE = "#B0BEC5"      # grey - the lines between the pieces
FRAME = "#546E7A"     # dark grey - the outline of one whole quiz
BLUE = "#2E86DE"      # blue - the 90 percent marker

# one row per quiz: (label, points earned, points in total, draw the lines?)
ROWS = [
    ("Quiz A", 9, 10, True),
    ("Quiz B", 18, 20, True),
    ("Quiz C", 450, 500, False),     # 500 lines would be too thin to see
    ("Out of 100", 90, 100, True),   # the standard bar everyone compares against
]

BAR_H = 0.62          # how tall one bar is
GAP = 1.0             # distance from one bar to the next

fig, ax = plt.subplots(figsize=(10.4, 5.4))
ax.axis("off")
ax.set_xlim(-0.62, 1.26)
ax.set_ylim(-0.95, len(ROWS) * GAP + 0.25)

for i, (label, part, whole, draw_lines) in enumerate(ROWS):
    y = (len(ROWS) - 1 - i) * GAP          # the first row goes on top
    frac = part / whole                    # how much of the bar is shaded

    ax.add_patch(Rectangle((0, y), 1, BAR_H, facecolor=EMPTY, edgecolor="none"))
    ax.add_patch(Rectangle((0, y), frac, BAR_H, facecolor=TAKEN, edgecolor="none"))

    if draw_lines:                         # one thin line between neighbouring pieces
        width = 0.8 if whole <= 20 else 0.35   # 100 pieces need much thinner lines
        for k in range(1, whole):
            ax.plot([k / whole, k / whole], [y, y + BAR_H],
                    color=LINE, linewidth=width, zorder=3)
    else:                                  # say in words what is too small to draw
        ax.text(0.45, y + BAR_H / 2, "500 tiny pieces",
                ha="center", va="center", fontsize=11, color="#FFFFFF", style="italic")

    ax.add_patch(Rectangle((0, y), 1, BAR_H,
                           facecolor="none", edgecolor=FRAME, linewidth=1.8, zorder=4))

    ax.text(-0.60, y + BAR_H / 2, label, ha="left", va="center",
            fontsize=12.5, color="#37474F", fontweight="bold")
    ax.text(-0.13, y + BAR_H / 2, rf"$\frac{{{part}}}{{{whole}}}$",
            ha="center", va="center", fontsize=17, color="#37474F")
    ax.text(1.03, y + BAR_H / 2, r"$90\%$", ha="left", va="center",
            fontsize=15, color=TAKEN, fontweight="bold")

# the dashed line that shows every bar stops in the same place
top = (len(ROWS) - 1) * GAP + BAR_H
ax.plot([0.9, 0.9], [-0.52, top + 0.12], color=BLUE,
        linewidth=2.2, linestyle="--", zorder=5)
ax.text(0.82, -0.72, r"every bar stops here: $\frac{90}{100} = 90\%$",
        ha="center", va="center", fontsize=12.5, color=BLUE, fontweight="bold")

ax.set_title("Different totals, one proportion", fontsize=17, fontweight="bold", pad=12)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_same_score_three_ways.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
