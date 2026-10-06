"""Figure 3 - a binomial times a trinomial: every term meets every term.

Top: the two terms of (x + 2y) as cards. Middle: the three terms of
(3x - y - 4) as cards. Blue arrows go from x to each of the three, orange
arrows from 2y to each of the three: 2 x 3 = 6 arrows, 6 products. Bottom:
the six products in two coloured rows, then the answer after collecting
-xy + 6xy = 5xy.

In this figure blue means "came from x" and orange "came from 2y".
Green answer, grey labels.

Run with:  python figures/fig_03_every_term.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
GREEN = "#1E8449"
BLUE = ("#2E86DE", "#E9F2FC")
ORANGE = ("#E67E22", "#FDF0E3")
PLAIN = ("#78909C", "#F4F6F7")

W, H = 13.0, 9.4                                   # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def card(xc, yc, text, col, w=1.7, h=0.9, size=24):
    """A rounded card centred on (xc, yc)."""
    ax.add_patch(FancyBboxPatch(
        (xc - w / 2, yc - h / 2), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.14",
        facecolor=col[1], edgecolor=col[0], linewidth=2.4, zorder=2))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=size,
            color=INK, zorder=3)


# --- the two factors ---------------------------------------------------------
Y1, Y2 = 8.3, 5.0                                  # heights of the two rows
top = [(4.5, r"$x$", BLUE), (8.5, r"$+\,2y$", ORANGE)]
mid = [(3.5, r"$3x$"), (6.5, r"$-\,y$"), (9.5, r"$-\,4$")]
ax.text(0.3, Y1, "binomial\n2 terms", ha="left", va="center", fontsize=14,
        color=GREY, fontweight="bold")
ax.text(0.3, Y2, "trinomial\n3 terms", ha="left", va="center", fontsize=14,
        color=GREY, fontweight="bold")
for xc, t, col in top:
    card(xc, Y1, t, col)
for xc, t in mid:
    card(xc, Y2, t, PLAIN)

# arrows: each top card goes to each middle card
for xt, _, col in top:
    for xm, _ in mid:
        ax.annotate("", xy=(xm, Y2 + 0.5), xytext=(xt, Y1 - 0.5),
                    arrowprops=dict(arrowstyle="-|>", color=col[0], lw=2.0,
                                    mutation_scale=18, alpha=0.8,
                                    shrinkA=0, shrinkB=0))
ax.text(W - 0.2, (Y1 + Y2) / 2, r"$2 \times 3 = 6$" + "\narrows",
        ha="right", va="center", fontsize=16, color=GREY)

# --- the six products, one row per term of the binomial ----------------------
Y3, Y4 = 3.1, 2.0
ax.text(0.3, Y3, "from  x", ha="left", va="center", fontsize=15,
        color=BLUE[0], fontweight="bold")
ax.text(0.3, Y4, "from  2y", ha="left", va="center", fontsize=15,
        color=ORANGE[0], fontweight="bold")
row1 = [r"$3x^{2}$", r"$-\,xy$", r"$-\,4x$"]
row2 = [r"$+\,6xy$", r"$-\,2y^{2}$", r"$-\,8y$"]
for (xm, _), t1, t2 in zip(mid, row1, row2):
    ax.text(xm, Y3, t1, ha="center", va="center", fontsize=24,
            color=BLUE[0], fontweight="bold")
    ax.text(xm, Y4, t2, ha="center", va="center", fontsize=24,
            color=ORANGE[0], fontweight="bold")
ax.plot([2.2, 10.8], [1.35, 1.35], color=GREY, lw=1.5)  # line above answer
ax.text(6.5, 0.65, r"$3x^{2} + 5xy - 2y^{2} - 4x - 8y$",
        ha="center", va="center", fontsize=26, color=GREEN,
        fontweight="bold")
ax.text(W - 0.2, 2.55, r"$-xy + 6xy = 5xy$", ha="right", va="center",
        fontsize=15, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_every_term.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_03_every_term.png")
