"""Figure 4 - the order of operations, and the order of undoing.

Two columns holding the same four levels. The left column is Chapter 11's
order, used when you work a value out. The right column is that same list
read from the bottom up, which is the order you undo things in.

The numbers beside the boxes carry the ordering, so no arrows are needed
and the columns can sit close together.

Vertical plan (y, top to bottom):
    5.70  the two column headings
    4.70  row 1 (box height 0.78)
    3.70  row 2
    2.70  row 3
    1.70  row 4
    0.60  closing note

Run with:  python figures/fig_04_the_order_turned_round.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

ORANGE = "#E67E22"        # undoing - the move being made
GREY = "#78909C"          # working a value out - the older skill
INK = "#212121"
TINT_ORANGE = "#FDF0E3"
TINT_GREY = "#ECEFF1"

W, H = 10.70, 6.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BOX_W, BOX_H = 4.00, 0.78
LEFT_X0, RIGHT_X0 = 0.85, 6.20
ROWS_Y = [4.70, 3.70, 2.70, 1.70]

LEVELS = ["brackets", "exponents", "multiply and divide", "add and subtract"]

ax.text(LEFT_X0 + BOX_W / 2, 5.70, "to work a value out",
        ha="center", va="center", fontsize=18, color=GREY,
        fontweight="bold")
ax.text(RIGHT_X0 + BOX_W / 2, 5.70, "to undo, and find the letter",
        ha="center", va="center", fontsize=18, color=ORANGE,
        fontweight="bold")

for i, y in enumerate(ROWS_Y):
    # left column: Chapter 11's order, top to bottom
    ax.add_patch(FancyBboxPatch((LEFT_X0, y - BOX_H / 2), BOX_W, BOX_H,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=TINT_GREY, edgecolor=GREY,
                                linewidth=2.0, zorder=3))
    ax.text(LEFT_X0 + BOX_W / 2, y, LEVELS[i], ha="center", va="center",
            fontsize=18, color=INK, zorder=4)
    ax.text(LEFT_X0 - 0.32, y, str(i + 1), ha="center", va="center",
            fontsize=17, color=GREY, fontweight="bold")

    # right column: the same list, bottom to top
    ax.add_patch(FancyBboxPatch((RIGHT_X0, y - BOX_H / 2), BOX_W, BOX_H,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=TINT_ORANGE, edgecolor=ORANGE,
                                linewidth=2.0, zorder=3))
    ax.text(RIGHT_X0 + BOX_W / 2, y, LEVELS[len(LEVELS) - 1 - i],
            ha="center", va="center", fontsize=18, color=INK, zorder=4)
    ax.text(RIGHT_X0 - 0.32, y, str(i + 1), ha="center", va="center",
            fontsize=17, color=ORANGE, fontweight="bold")

ax.text(0.53, 0.60, "the same four levels both times - the right-hand list "
        "is the left-hand list read from the bottom up",
        ha="left", va="center", fontsize=15, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_the_order_turned_round.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_04_the_order_turned_round.png")
