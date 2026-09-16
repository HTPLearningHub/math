"""Figure 2 - the apple piles, the picture the whole chapter is built on.

Top: five piles with seven apples in each pile. Counting them one way gives
5 x 7 = 35.

Bottom: exactly the same apples, with every pile split into a group of 3 and a
group of 4. Now there are five groups of 3 (15 apples) and five groups of 4
(20 apples), and 15 + 20 = 35 again.

Nothing was added and nothing was taken away between the two panels. That is
why 5 x (3 + 4) and (5 x 3) + (5 x 4) must give the same number.

Run with:  python figures/fig_02_apple_piles.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"          # the first 3 apples of every pile
BLUE_FILL = "#EAF2FB"
ORANGE = "#E67E22"        # the other 4 apples of every pile
ORANGE_FILL = "#FDF0E3"
INK = "#212121"

PILES = 5                 # how many piles
PER_PILE = 7              # apples in one pile
LEFT_GROUP = 3            # the pile is split into 3 ...
RIGHT_GROUP = 4           # ... and 4

STEP = 0.66               # distance between two apple centres
R = 0.23                  # radius of one apple
SPLIT_GAP = 0.80          # extra space between the two groups, bottom panel
X0 = 1.15                 # x of the first apple in every row

W, H = 12.0, 10.2

fig, ax = plt.subplots(figsize=(W, H))
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")                       # apples must stay round


def row_y(panel_top, i):
    """y of pile number i (0 = the top pile) in a panel starting at panel_top."""
    return panel_top - i * STEP


def band(x_lo, x_hi, y_hi, y_lo, edge, fill):
    """A soft rectangle drawn behind a block of apples."""
    pad = 0.30
    ax.add_patch(FancyBboxPatch(
        (x_lo - pad, y_lo - pad), (x_hi - x_lo) + 2 * pad, (y_hi - y_lo) + 2 * pad,
        boxstyle="round,pad=0.02,rounding_size=0.20",
        facecolor=fill, edgecolor=edge, linewidth=1.8, zorder=1))


# ---------------------------------------------------------------- top panel
TOP = 9.25
ax.text(0.15, TOP + 0.85, "Five piles, seven apples in each pile",
        ha="left", va="center", fontsize=17, fontweight="bold", color=INK)

x_last = X0 + (PER_PILE - 1) * STEP
band(X0, x_last, row_y(TOP, 0), row_y(TOP, PILES - 1), BLUE, BLUE_FILL)
for i in range(PILES):
    for j in range(PER_PILE):
        ax.add_patch(Circle((X0 + j * STEP, row_y(TOP, i)), R,
                            facecolor=BLUE, edgecolor="none", zorder=3))

ax.text(x_last + 1.30, (row_y(TOP, 0) + row_y(TOP, PILES - 1)) / 2,
        r"$5 \times 7 = 35$ apples", ha="left", va="center",
        fontsize=19, color=INK)

# ------------------------------------------------------------- bottom panel
BOT = 4.45
ax.text(0.15, BOT + 0.95, "The same apples, every pile split into 3 and 4",
        ha="left", va="center", fontsize=17, fontweight="bold", color=INK)

x_blue_hi = X0 + (LEFT_GROUP - 1) * STEP
x_or_lo = x_blue_hi + STEP + SPLIT_GAP
x_or_hi = x_or_lo + (RIGHT_GROUP - 1) * STEP

band(X0, x_blue_hi, row_y(BOT, 0), row_y(BOT, PILES - 1), BLUE, BLUE_FILL)
band(x_or_lo, x_or_hi, row_y(BOT, 0), row_y(BOT, PILES - 1), ORANGE, ORANGE_FILL)

for i in range(PILES):
    y = row_y(BOT, i)
    for j in range(LEFT_GROUP):
        ax.add_patch(Circle((X0 + j * STEP, y), R,
                            facecolor=BLUE, edgecolor="none", zorder=3))
    for j in range(RIGHT_GROUP):
        ax.add_patch(Circle((x_or_lo + j * STEP, y), R,
                            facecolor=ORANGE, edgecolor="none", zorder=3))

# the two sub-totals, written under their own block
y_label = row_y(BOT, PILES - 1) - 0.95
ax.text((X0 + x_blue_hi) / 2, y_label, r"$5 \times 3 = 15$",
        ha="center", va="center", fontsize=17, color=BLUE, fontweight="bold")
ax.text((x_or_lo + x_or_hi) / 2, y_label, r"$5 \times 4 = 20$",
        ha="center", va="center", fontsize=17, color=ORANGE, fontweight="bold")
ax.text((x_blue_hi + x_or_lo) / 2, y_label, "+",
        ha="center", va="center", fontsize=20, color=INK)

ax.text(x_or_hi + 1.30, (row_y(BOT, 0) + row_y(BOT, PILES - 1)) / 2,
        r"$15 + 20 = 35$ apples", ha="left", va="center",
        fontsize=19, color=INK)

ax.text(W / 2, 0.25,
        "Same apples, same total. Only the grouping changed.",
        ha="center", va="center", fontsize=14, style="italic", color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_apple_piles.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
