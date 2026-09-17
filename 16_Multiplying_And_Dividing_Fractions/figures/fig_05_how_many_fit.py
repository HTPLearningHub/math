"""Figure 5 - division asks "how many of these fit into that?".

Three whole bars, drawn end to end, each cut into quarters. Every quarter is
numbered, so the reader counts 12 instead of being told 12.

This is the picture that makes dividing by a fraction stop being strange.
Nobody is surprised that 12 quarters fit into 3 wholes, and that is exactly
what 3 divided by 1/4 means. The answer is larger than the number we started
from because the thing we are counting is smaller than one whole - and the
figure says so in one line at the bottom.

The three wholes have thick blue edges and the quarter cuts are orange, so
the two different-sized things in the question never get mixed up.

Run with:  python figures/fig_05_how_many_fit.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"             # the thing being shared out: 3 wholes
ORANGE = "#E67E22"           # the piece we are counting: one quarter
GREEN = "#1E8449"            # the answer: how many pieces there were
GREY = "#78909C"
INK = "#212121"

TINT = {BLUE: "#E9F2FC", ORANGE: "#FDF0E3"}

WHOLES = 3                   # 3 whole bars
PARTS = 4                    # each cut into quarters

W, H = 13.20, 5.70
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

STRIP_X = 0.95                       # left edge of the first whole
STRIP_W = W - 2 * STRIP_X            # the three wholes together
UNIT = STRIP_W / WHOLES              # the width of one whole
PIECE = UNIT / PARTS                 # the width of one quarter
BAR_Y, BAR_H = 2.45, 1.30

count = 0
for k in range(WHOLES):
    ux = STRIP_X + k * UNIT

    # the quarters inside this whole, numbered as they are drawn
    for j in range(PARTS):
        px = ux + j * PIECE
        ax.add_patch(Rectangle((px, BAR_Y), PIECE, BAR_H,
                               facecolor=TINT[ORANGE], edgecolor=ORANGE,
                               linewidth=1.8, zorder=2))
        count += 1
        ax.text(px + PIECE / 2, BAR_Y + BAR_H / 2, str(count), ha="center",
                va="center", fontsize=17, color=GREEN, fontweight="bold",
                zorder=4)

    # the edge of the whole itself, drawn last so it sits on top
    ax.add_patch(Rectangle((ux, BAR_Y), UNIT, BAR_H, facecolor="none",
                           edgecolor=BLUE, linewidth=3.0, zorder=5))
    ax.text(ux + UNIT / 2, BAR_Y + BAR_H + 0.34, f"whole number {k + 1}",
            ha="center", va="center", fontsize=13, color=BLUE)

# the tick marks and labels 0, 1, 2, 3 under the strip
for k in range(WHOLES + 1):
    x = STRIP_X + k * UNIT
    ax.plot([x, x], [BAR_Y - 0.30, BAR_Y], color=GREY, linewidth=1.4, zorder=3)
    ax.text(x, BAR_Y - 0.56, str(k), ha="center", va="center", fontsize=14,
            color=GREY)

# one quarter, named, with a short bracket under the very first piece
ax.plot([STRIP_X, STRIP_X + PIECE], [BAR_Y - 1.02, BAR_Y - 1.02],
        color=ORANGE, linewidth=2.4, zorder=3)
ax.plot([STRIP_X, STRIP_X], [BAR_Y - 1.02, BAR_Y - 0.86], color=ORANGE,
        linewidth=2.4, zorder=3)
ax.plot([STRIP_X + PIECE, STRIP_X + PIECE], [BAR_Y - 1.02, BAR_Y - 0.86],
        color=ORANGE, linewidth=2.4, zorder=3)
ax.text(STRIP_X + PIECE + 0.22, BAR_Y - 1.02,
        r"one piece, $\frac{1}{4}$ of a whole", ha="left", va="center",
        fontsize=14, color=ORANGE)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.42,
        "How many quarters fit into three wholes?",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.84,
        "count the numbered pieces - that counting IS the division",
        ha="center", va="center", fontsize=13, color=GREY)

# ------------------------------------------------------------- the bottom line
ax.text(W / 2, 0.74, r"$3 \div \frac{1}{4} = 12$", ha="center", va="center",
        fontsize=23, color=GREEN)
ax.text(W / 2, 0.26,
        "the piece is smaller than one whole, so the answer is bigger than "
        "the number we started from",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_05_how_many_fit.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
