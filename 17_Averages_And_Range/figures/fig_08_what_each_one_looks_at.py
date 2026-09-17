"""Figure 8 - the same nine days, seen the way each measure sees them.

Three panels, one per measure, all showing the fireworks data.

The mean panel draws every value at its true height, so the 500 fills the
panel and the other eight bars are flat lines you can barely see. The median
panel throws the heights away and keeps only the order, so all nine days
become identical cards. The mode panel throws the order away and keeps only
the counts, so the picture becomes three stacks.

Put side by side, the three panels explain figure 7 instead of merely
repeating it. A measure can only be moved by the part of the data it
actually looks at, and only the mean looks at how big a value is.

The measure's own colour is used for the thing it pays attention to; the
parts it ignores are drawn in grey.

Run with:  python figures/fig_08_what_each_one_looks_at.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"
PURPLE = "#8E44AD"        # the one unusual value, as in figure 7
ORANGE = "#E67E22"        # the mean
GREEN = "#1E8449"         # the median and the mode
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"
TINT_PURPLE = "#F2E7F7"
TINT_GREY = "#ECEFF1"

ORDERED = [0, 0, 0, 0, 0, 0, 0, 1, 500]     # the nine days, smallest first

W, H = 13.40, 6.85
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

PAN_W = 4.10                 # width of one panel
GAP = 0.45
PAN_X = [0.35, 0.35 + PAN_W + GAP, 0.35 + 2 * (PAN_W + GAP)]
BASE = 1.60                  # the ground inside every panel
DRAW_H = 2.75                # how tall a full-height drawing may be


def panel_head(x0, colour, name, looks_at):
    """The two heading lines that sit above one panel."""
    ax.text(x0 + PAN_W / 2, 5.38, name, ha="center", va="center", fontsize=18,
            color=colour, fontweight="bold")
    ax.text(x0 + PAN_W / 2, 4.98, looks_at, ha="center", va="center",
            fontsize=13, color=GREY)


def panel_foot(x0, colour, line):
    """The one-line conclusion under a panel."""
    ax.text(x0 + PAN_W / 2, 0.55, line, ha="center", va="center", fontsize=13,
            color=colour)


# ======================================================== panel 1: the mean
x0 = PAN_X[0]
panel_head(x0, ORANGE, "the mean", "looks at how big every value is")
slot = PAN_W / 9
bar_w = slot * 0.58
for i, v in enumerate(ORDERED):
    bx = x0 + i * slot + (slot - bar_w) / 2
    h = (v / 500) * DRAW_H
    edge = PURPLE if v == 500 else BLUE
    face = TINT_PURPLE if v == 500 else TINT_BLUE
    if h < 0.05:
        ax.plot([bx, bx + bar_w], [BASE, BASE], color=edge, linewidth=2.6,
                zorder=3)
    else:
        ax.add_patch(Rectangle((bx, BASE), bar_w, h, facecolor=face,
                               edgecolor=edge, linewidth=2.2, zorder=3))
ax.plot([x0, x0 + PAN_W], [BASE, BASE], color=GREY, linewidth=1.6, zorder=2)
ax.text(x0 + PAN_W / 2, BASE - 0.36, "each day, drawn at its true size",
        ha="center", va="center", fontsize=12, color=GREY)
panel_foot(x0, ORANGE, "so one huge value moves it")

# ====================================================== panel 2: the median
x0 = PAN_X[1]
panel_head(x0, GREEN, "the median", "looks only at the order")
card = slot * 0.58
card_y = BASE + 0.95
for i, v in enumerate(ORDERED):
    cx = x0 + i * slot + slot / 2
    if i == 4:
        edge, face = GREEN, TINT_GREEN
    elif v == 500:
        edge, face = PURPLE, TINT_PURPLE
    else:
        edge, face = GREY, TINT_GREY
    ax.add_patch(FancyBboxPatch((cx - card / 2, card_y), card, card,
                                boxstyle="round,pad=0,rounding_size=0.06",
                                facecolor=face, edgecolor=edge,
                                linewidth=2.6 if i == 4 else 2.0, zorder=3))
    ax.text(cx, card_y - 0.30, str(i + 1), ha="center", va="center",
            fontsize=11, color=GREY)
mid_x = x0 + 4 * slot + slot / 2
ax.annotate("", xy=(mid_x, card_y + card + 0.14),
            xytext=(mid_x, card_y + card + 0.72),
            arrowprops=dict(arrowstyle="-|>", color=GREEN, linewidth=2.2))
ax.text(mid_x, card_y + card + 0.98, "the fifth card", ha="center",
        va="center", fontsize=13, color=GREEN, fontweight="bold")
ax.text(x0 + PAN_W / 2, BASE - 0.36, "every day is just one place in the row",
        ha="center", va="center", fontsize=12, color=GREY)
panel_foot(x0, GREEN, "so it does not matter how far away the last one is")

# ======================================================== panel 3: the mode
x0 = PAN_X[2]
panel_head(x0, GREEN, "the mode", "looks only at how often")
groups = [("0", 7), ("1", 1), ("500", 1)]
gslot = PAN_W / 3
box = 0.30
for k, (name, n) in enumerate(groups):
    cx = x0 + k * gslot + gslot / 2
    edge = GREEN if n == 7 else (PURPLE if name == "500" else GREY)
    face = TINT_GREEN if n == 7 else (TINT_PURPLE if name == "500"
                                      else TINT_GREY)
    for j in range(n):
        ax.add_patch(Rectangle((cx - box / 2, BASE + j * (box + 0.05)), box,
                               box, facecolor=face, edgecolor=edge,
                               linewidth=2.2, zorder=3))
    ax.text(cx, BASE - 0.36, name, ha="center", va="center", fontsize=13,
            color=edge, fontweight="bold" if n == 7 else "normal")
ax.plot([x0, x0 + PAN_W], [BASE, BASE], color=GREY, linewidth=1.6, zorder=2)
ax.text(x0 + gslot / 2, BASE + 7 * (box + 0.05) + 0.32, "seven days",
        ha="center", va="center", fontsize=13, color=GREEN, fontweight="bold")
panel_foot(x0, GREEN, "so a day that happened once counts once")

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.34, "Each measure looks at a different part of the data",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.72,
        "the same nine days every time - only what the measure pays attention "
        "to has changed",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_08_what_each_one_looks_at.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
