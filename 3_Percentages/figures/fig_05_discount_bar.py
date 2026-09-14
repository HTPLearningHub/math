"""Figure 5 - a 30% discount on a price of 120, drawn as one bar.

The whole bar is the full price: 120 money units, which is 100%.
The orange piece on the right is the 30% the shop takes off, which is 36.
The blue piece on the left is the 70% you still pay, which is 84.
The scale under the bar lets the reader read any percentage off the picture.
Run with:  python figures/fig_05_discount_bar.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

PAID = "#2E86DE"     # blue - the part you still pay
CUT = "#E67E22"      # orange - the part taken off
FRAME = "#546E7A"    # dark grey - outlines and the scale
TEXT = "#37474F"     # normal text

FULL = 10.0          # the whole bar is 10 units long and means 100%
PAY = 7.0            # 70% of the bar
BOTTOM, TOP = 1.1, 2.5

fig, ax = plt.subplots(figsize=(11.0, 4.6))
ax.axis("off")
ax.set_xlim(-0.7, FULL + 0.7)
ax.set_ylim(-1.5, 4.3)

# the two pieces of the bar
ax.add_patch(Rectangle((0, BOTTOM), PAY, TOP - BOTTOM, facecolor=PAID, edgecolor="none"))
ax.add_patch(Rectangle((PAY, BOTTOM), FULL - PAY, TOP - BOTTOM, facecolor=CUT, edgecolor="none"))
ax.add_patch(Rectangle((0, BOTTOM), FULL, TOP - BOTTOM,
                       facecolor="none", edgecolor=FRAME, linewidth=2.2))
ax.plot([PAY, PAY], [BOTTOM, TOP], color="#FFFFFF", linewidth=2.6)

# what each piece is worth, written inside it
ax.text(PAY / 2, (BOTTOM + TOP) / 2 + 0.18, r"you pay $70\%$",
        ha="center", va="center", fontsize=15, color="#FFFFFF", fontweight="bold")
ax.text(PAY / 2, (BOTTOM + TOP) / 2 - 0.36, r"$84$",
        ha="center", va="center", fontsize=15, color="#FFFFFF")
ax.text((PAY + FULL) / 2, (BOTTOM + TOP) / 2 + 0.18, r"$30\%$ off",
        ha="center", va="center", fontsize=15, color="#FFFFFF", fontweight="bold")
ax.text((PAY + FULL) / 2, (BOTTOM + TOP) / 2 - 0.36, r"$36$",
        ha="center", va="center", fontsize=15, color="#FFFFFF")

# the line above that shows the whole bar is the full price
ax.annotate("", xy=(0, 3.1), xytext=(FULL, 3.1),
            arrowprops=dict(arrowstyle="<->", color=FRAME, linewidth=1.8))
ax.text(FULL / 2, 3.45, r"the full price $= 120 = 100\%$",
        ha="center", va="center", fontsize=14, color=FRAME, fontweight="bold")

# the percentage scale under the bar, one tick every 10%
for k in range(11):
    x = k * FULL / 10
    ax.plot([x, x], [BOTTOM - 0.12, BOTTOM - 0.32], color=FRAME, linewidth=1.4)
    ax.text(x, BOTTOM - 0.62, f"{k * 10}", ha="center", va="center",
            fontsize=10.5, color=FRAME)
ax.text(FULL / 2, BOTTOM - 1.22, "percent of the full price",
        ha="center", va="center", fontsize=12.5, color=FRAME)

ax.set_title("A 30% discount on a price of 120", fontsize=17, fontweight="bold", pad=8)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_discount_bar.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
