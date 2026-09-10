"""Figure 5 - where proper and improper fractions sit on the number line.

The line runs from 0 to 2 and is cut into thirds.
A proper fraction sits before 1. An improper fraction sits at 1 or after it.
Run with:  python figures/fig_05_number_line.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

PROPER = "#2E86DE"    # blue   - the proper fraction
IMPROPER = "#E67E22"  # orange - the improper fraction
LINE = "#212121"      # near black - the number line itself

fig, ax = plt.subplots(figsize=(11.0, 4.2))
ax.axis("off")
ax.set_xlim(-0.18, 2.18)
ax.set_ylim(-0.75, 1.15)

ax.plot([0, 2], [0, 0], color=LINE, linewidth=3.5, solid_capstyle="round")  # the line

for whole in [0, 1, 2]:                                   # tall ticks for the whole numbers
    ax.plot([whole, whole], [-0.11, 0.11], color=LINE, linewidth=3.5)
    ax.text(whole, -0.30, str(whole), ha="center", va="top",
            fontsize=20, fontweight="bold", color=LINE)

thirds = [1 / 3, 2 / 3, 4 / 3, 5 / 3]                     # short ticks for the thirds
labels = [r"$\frac{1}{3}$", r"$\frac{2}{3}$", r"$\frac{4}{3}$", r"$\frac{5}{3}$"]
for x, label in zip(thirds, labels):
    ax.plot([x, x], [-0.07, 0.07], color="#90A4AE", linewidth=2.5)
    ax.text(x, -0.30, label, ha="center", va="top", fontsize=15, color="#607D8B")

ax.plot(2 / 3, 0, "o", markersize=17, color=PROPER, zorder=5)      # the point 2/3
ax.plot(4 / 3, 0, "o", markersize=17, color=IMPROPER, zorder=5)    # the point 4/3

ax.annotate("proper fraction\n" + r"$\frac{2}{3}$ is between 0 and 1",
            xy=(2 / 3, 0.10), xytext=(2 / 3, 0.92), ha="center", va="center",
            fontsize=13, color=PROPER, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#E8F1FC", edgecolor=PROPER, lw=2),
            arrowprops=dict(arrowstyle="->", color=PROPER, linewidth=2.2))

ax.annotate("improper fraction\n" + r"$\frac{4}{3} = 1\frac{1}{3}$ is between 1 and 2",
            xy=(4 / 3, 0.10), xytext=(1.62, 0.92), ha="center", va="center",
            fontsize=13, color=IMPROPER, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.45", facecolor="#FDF0E3", edgecolor=IMPROPER, lw=2),
            arrowprops=dict(arrowstyle="->", color=IMPROPER, linewidth=2.2))

ax.set_title("Fractions live on the number line, like every other number",
             fontsize=17, fontweight="bold", pad=10)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_number_line.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
