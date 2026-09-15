"""Figure 6 - what an 8.25% sales tax adds to a price of 50.

The blue bar is the price on the label: 50.
The orange piece is the tax, 4.13, which is added on top of it.
The two together are what you actually hand over: 54.13.
The picture is drawn to scale, so the reader can see how small 8.25% is.
Run with:  python figures/fig_06_sales_tax_bar.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

PRICE_COLOUR = "#2E86DE"   # blue - the price on the label
TAX_COLOUR = "#E67E22"     # orange - the tax added on top
FRAME = "#546E7A"
TEXT = "#37474F"

PRICE = 50.0
TAX = 4.13
SCALE = 0.20               # 1 money unit is 0.20 drawing units, so 50 is 10 wide
BOTTOM, TOP = 1.3, 2.9

fig, ax = plt.subplots(figsize=(11.2, 4.8))
ax.axis("off")
ax.set_xlim(-0.7, (PRICE + TAX) * SCALE + 1.5)
ax.set_ylim(-1.5, 4.6)

price_w = PRICE * SCALE
tax_w = TAX * SCALE

# the price, then the tax stuck on the end of it
ax.add_patch(Rectangle((0, BOTTOM), price_w, TOP - BOTTOM,
                       facecolor=PRICE_COLOUR, edgecolor="none"))
ax.add_patch(Rectangle((price_w, BOTTOM), tax_w, TOP - BOTTOM,
                       facecolor=TAX_COLOUR, edgecolor="none"))
ax.add_patch(Rectangle((0, BOTTOM), price_w + tax_w, TOP - BOTTOM,
                       facecolor="none", edgecolor=FRAME, linewidth=2.2))
ax.plot([price_w, price_w], [BOTTOM, TOP], color="#FFFFFF", linewidth=2.6)

# what is written inside the blue part
ax.text(price_w / 2, (BOTTOM + TOP) / 2 + 0.22, "the price on the label",
        ha="center", va="center", fontsize=14, color="#FFFFFF", fontweight="bold")
ax.text(price_w / 2, (BOTTOM + TOP) / 2 - 0.38, r"$50.00$   $(100\%)$",
        ha="center", va="center", fontsize=14, color="#FFFFFF")

# the tax piece is too narrow for text, so label it from above
ax.annotate(r"tax $8.25\%$" "\n" r"$4.13$",
            xy=(price_w + tax_w / 2, TOP + 0.05),
            xytext=(price_w + tax_w / 2 + 0.85, TOP + 1.15),
            ha="center", va="center", fontsize=14, color=TAX_COLOUR,
            fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color=TAX_COLOUR, linewidth=2.0))

# the total you actually pay, measured under the whole bar
ax.annotate("", xy=(0, BOTTOM - 0.35), xytext=(price_w + tax_w, BOTTOM - 0.35),
            arrowprops=dict(arrowstyle="<->", color=FRAME, linewidth=1.8))
ax.text((price_w + tax_w) / 2, BOTTOM - 0.95,
        r"you hand over $54.13$", ha="center", va="center",
        fontsize=15, color=FRAME, fontweight="bold")

ax.set_title("A sales tax is added on top of the price",
             fontsize=17, fontweight="bold", pad=10)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_sales_tax_bar.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
