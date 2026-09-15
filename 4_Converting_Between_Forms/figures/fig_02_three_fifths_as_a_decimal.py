"""Figure 2 - why 3/5 is 0.6.

The whole bar is one. It is cut into five equal parts.
Each part is worth 0.2, because five lots of 0.2 make 1.0.
Three of the parts are shaded, and 0.2 + 0.2 + 0.2 = 0.6.
Run with:  python figures/fig_02_three_fifths_as_a_decimal.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

TAKEN = "#E67E22"    # orange - the three parts we take
LEFT_OVER = "#ECEFF1"  # pale grey - the parts nobody takes
FRAME = "#546E7A"    # outlines and the scale
TEXT = "#37474F"

PARTS = 5            # the bottom number of the fraction
SHADED = 3           # the top number of the fraction
WIDTH = 10.0         # the whole bar is 10 units wide and means 1
BOTTOM, TOP = 1.2, 2.8

fig, ax = plt.subplots(figsize=(11.0, 4.8))
ax.axis("off")
ax.set_xlim(-0.6, WIDTH + 0.6)
ax.set_ylim(-1.6, 4.4)

step = WIDTH / PARTS

# the five equal parts, the first three of them shaded
for k in range(PARTS):
    colour = TAKEN if k < SHADED else LEFT_OVER
    ax.add_patch(Rectangle((k * step, BOTTOM), step, TOP - BOTTOM,
                           facecolor=colour, edgecolor=FRAME, linewidth=1.8))
    # every part is worth two tenths, so write that inside it
    inside = "#FFFFFF" if k < SHADED else TEXT
    ax.text(k * step + step / 2, (BOTTOM + TOP) / 2 + 0.22, r"$\frac{1}{5}$",
            ha="center", va="center", fontsize=17, color=inside)
    ax.text(k * step + step / 2, (BOTTOM + TOP) / 2 - 0.42, r"$0.2$",
            ha="center", va="center", fontsize=15, color=inside)

# the outline of the whole bar, so the reader sees it is one whole
ax.add_patch(Rectangle((0, BOTTOM), WIDTH, TOP - BOTTOM,
                       facecolor="none", edgecolor=FRAME, linewidth=2.6))

# the line above: the whole bar is 1
ax.annotate("", xy=(0, 3.4), xytext=(WIDTH, 3.4),
            arrowprops=dict(arrowstyle="<->", color=FRAME, linewidth=1.8))
ax.text(WIDTH / 2, 3.78, r"one whole $= 1.0$",
        ha="center", va="center", fontsize=14, color=FRAME, fontweight="bold")

# the line below the shaded part: what the three parts add up to
ax.annotate("", xy=(0, 0.85), xytext=(SHADED * step, 0.85),
            arrowprops=dict(arrowstyle="<->", color=TAKEN, linewidth=2.2))
ax.text(SHADED * step / 2, 0.30,
        r"$0.2 + 0.2 + 0.2 = 0.6$",
        ha="center", va="center", fontsize=16, color=TAKEN, fontweight="bold")
ax.text(SHADED * step / 2, -0.35, r"so $\frac{3}{5} = 0.6$",
        ha="center", va="center", fontsize=17, color=TEXT)

ax.set_title("Three fifths of one whole", fontsize=17, fontweight="bold", pad=8)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_three_fifths_as_a_decimal.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
