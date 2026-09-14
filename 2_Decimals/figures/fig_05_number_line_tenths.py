"""Figure 5 - the number line from 0 to 2, cut into tenths.

Between two whole numbers there are 10 equal steps. One step is 0.1.
Two points are marked: 0.1 (one tenth) and 1.1 (one whole and one tenth).
This is the same number line as in chapter 1, but cut into tenths.
Run with:  python figures/fig_05_number_line_tenths.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

SMALL = "#E67E22"     # orange - the point that is smaller than 1
BIG = "#2E86DE"       # blue   - the point that is bigger than 1
LINE = "#212121"      # near black - the number line itself
TICK = "#90A4AE"      # grey   - the short ticks for the tenths

fig, ax = plt.subplots(figsize=(13.0, 4.4))
ax.axis("off")
ax.set_xlim(-0.16, 2.16)
ax.set_ylim(-0.62, 0.95)

ax.plot([0, 2], [0, 0], color=LINE, linewidth=3.2, solid_capstyle="round")   # the line

for k in range(21):                                 # 21 marks: 0, 0.1, 0.2 ... 2.0
    x = k / 10
    whole = (k % 10 == 0)
    ax.plot([x, x], [-0.055, 0.055] if whole else [-0.032, 0.032],
            color=LINE if whole else TICK, linewidth=3.2 if whole else 1.8)
    if whole:
        ax.text(x, -0.17, str(k // 10), ha="center", va="top",
                fontsize=19, fontweight="bold", color=LINE)
    else:
        ax.text(x, -0.11, f"{x:.1f}", ha="center", va="top",
                fontsize=10.5, color="#607D8B", rotation=45)

ax.plot(0.1, 0, "o", markersize=15, color=SMALL, zorder=5)     # the point 0.1
ax.plot(1.1, 0, "o", markersize=15, color=BIG, zorder=5)       # the point 1.1

ax.annotate("$0.1$\none tenth\nof the way to 1",
            xy=(0.1, 0.06), xytext=(0.28, 0.72), ha="center", va="center",
            fontsize=12, color=SMALL, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#FDF0E3", edgecolor=SMALL, lw=2),
            arrowprops=dict(arrowstyle="-|>", color=SMALL, linewidth=2.0, mutation_scale=18))

ax.annotate("$1.1$\none whole\nand one tenth",
            xy=(1.1, 0.06), xytext=(1.30, 0.72), ha="center", va="center",
            fontsize=12, color=BIG, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#E8F1FC", edgecolor=BIG, lw=2),
            arrowprops=dict(arrowstyle="-|>", color=BIG, linewidth=2.0, mutation_scale=18))

ax.set_title("Between two whole numbers there are ten equal steps",
             fontsize=16, fontweight="bold", pad=8)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_number_line_tenths.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
