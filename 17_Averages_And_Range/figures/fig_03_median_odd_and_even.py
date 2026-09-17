"""Figure 3 - the median, with an odd and with an even number of values.

Two ordered strips of cards. The upper strip holds five values, so one card
sits exactly in the middle and that card IS the median. The lower strip holds
ten values, so no single card is in the middle - two are - and the median is
the mean of those two.

The picture is built to make one thing obvious: the median is chosen by its
POSITION, not by its size. The position numbers are printed under every card,
and the counts on each side of the middle are written out ("2 below,
2 above"), because that balance is the whole definition.

The two strips use the same card width, so the reader can see that an even
number of cards simply has no single middle.

Run with:  python figures/fig_03_median_odd_and_even.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"          # ordinary values
ORANGE = "#E67E22"        # the two middle values, when there are two
GREEN = "#1E8449"         # the median
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"

ODD = [2, 3, 5, 7, 10]
EVEN = [0, 1, 1, 2, 2, 2, 3, 5, 5, 7]

W, H = 13.20, 9.10
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT, RIGHT = 1.00, W - 1.00
SLOT = (RIGHT - LEFT) / 10           # one card slot, fixed by the longer strip
CARD_W = SLOT * 0.80
CARD_H = 1.02


def draw_strip(values, base, middles):
    """Draw one row of cards, centred, and return each card's centre x."""
    total = len(values) * SLOT
    start = (W - total) / 2
    centres = []
    for i, v in enumerate(values):
        cx = start + i * SLOT + SLOT / 2
        centres.append(cx)
        hot = i in middles
        ax.add_patch(FancyBboxPatch(
            (cx - CARD_W / 2, base), CARD_W, CARD_H,
            boxstyle="round,pad=0,rounding_size=0.12",
            facecolor=TINT_ORANGE if hot else TINT_BLUE,
            edgecolor=ORANGE if hot else BLUE,
            linewidth=3.0 if hot else 2.0, zorder=3))
        ax.text(cx, base + CARD_H / 2, str(v), ha="center", va="center",
                fontsize=20, color=ORANGE if hot else BLUE,
                fontweight="bold", zorder=4)
        ax.text(cx, base - 0.32, f"{i + 1}", ha="center", va="center",
                fontsize=12, color=GREY, zorder=4)
    return centres


# ============================================================ odd: five values
BASE_A = 6.15
cx_a = draw_strip(ODD, BASE_A, middles={2})
# the middle card of an odd strip is the answer, so recolour it green
ax.add_patch(FancyBboxPatch((cx_a[2] - CARD_W / 2, BASE_A), CARD_W, CARD_H,
                            boxstyle="round,pad=0,rounding_size=0.12",
                            facecolor=TINT_GREEN, edgecolor=GREEN,
                            linewidth=3.2, zorder=5))
ax.text(cx_a[2], BASE_A + CARD_H / 2, "5", ha="center", va="center",
        fontsize=20, color=GREEN, fontweight="bold", zorder=6)

ax.text(W / 2, BASE_A + CARD_H + 0.92, "an odd number of values",
        ha="center", va="center", fontsize=17, color=INK, fontweight="bold")
ax.text(W / 2, BASE_A + CARD_H + 0.52,
        "five cards, so one card sits exactly in the middle",
        ha="center", va="center", fontsize=13, color=GREY)

# the two counts that make the middle the middle
ax.annotate("", xy=(cx_a[0] - CARD_W / 2, BASE_A - 0.70),
            xytext=(cx_a[2] - CARD_W / 2, BASE_A - 0.70),
            arrowprops=dict(arrowstyle="<->", color=GREY, linewidth=1.6))
ax.annotate("", xy=(cx_a[2] + CARD_W / 2, BASE_A - 0.70),
            xytext=(cx_a[4] + CARD_W / 2, BASE_A - 0.70),
            arrowprops=dict(arrowstyle="<->", color=GREY, linewidth=1.6))
ax.text((cx_a[0] + cx_a[2]) / 2 - CARD_W / 2, BASE_A - 1.02,
        "two values below", ha="center", va="center", fontsize=12, color=GREY)
ax.text((cx_a[2] + cx_a[4]) / 2 + CARD_W / 2, BASE_A - 1.02,
        "two values above", ha="center", va="center", fontsize=12, color=GREY)
ax.text(cx_a[4] + CARD_W, BASE_A + CARD_H / 2, r"median $= 5$", ha="left",
        va="center", fontsize=17, color=GREEN, fontweight="bold")

# ========================================================== even: ten values
BASE_B = 2.55
cx_b = draw_strip(EVEN, BASE_B, middles={4, 5})
ax.text(W / 2, BASE_B + CARD_H + 0.92, "an even number of values",
        ha="center", va="center", fontsize=17, color=INK, fontweight="bold")
ax.text(W / 2, BASE_B + CARD_H + 0.52,
        "ten cards, so no card is in the middle - two cards share the place",
        ha="center", va="center", fontsize=13, color=GREY)

# the two middle cards are joined and taken down to their own mean
mid_x = (cx_b[4] + cx_b[5]) / 2
ax.plot([cx_b[4], cx_b[4]], [BASE_B - 0.52, BASE_B - 0.80], color=ORANGE,
        linewidth=2.0, zorder=3)
ax.plot([cx_b[5], cx_b[5]], [BASE_B - 0.52, BASE_B - 0.80], color=ORANGE,
        linewidth=2.0, zorder=3)
ax.plot([cx_b[4], cx_b[5]], [BASE_B - 0.80, BASE_B - 0.80], color=ORANGE,
        linewidth=2.0, zorder=3)
ax.annotate("", xy=(mid_x, BASE_B - 1.32), xytext=(mid_x, BASE_B - 0.80),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, linewidth=2.2))
ax.text(mid_x + 0.22, BASE_B - 1.06, "take the mean of these two", ha="left",
        va="center", fontsize=12, color=ORANGE)

ax.add_patch(FancyBboxPatch((mid_x - 2.05, BASE_B - 2.24), 4.10, 0.86,
                            boxstyle="round,pad=0,rounding_size=0.16",
                            facecolor=TINT_GREEN, edgecolor=GREEN,
                            linewidth=2.4, zorder=3))
ax.text(mid_x, BASE_B - 1.81, r"$\frac{2 + 2}{2} = 2$", ha="center",
        va="center", fontsize=20, color=GREEN, zorder=4)
ax.text(mid_x + 2.30, BASE_B - 1.81, r"median $= 2$", ha="left", va="center",
        fontsize=17, color=GREEN, fontweight="bold")

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.36, "The median is a position, not a size",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_03_median_odd_and_even.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
