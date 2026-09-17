"""Figure 2 - how to move the two parts of a subtraction safely.

Top row: 4x - 7 is rewritten as 4x + (-7), and only then are the two terms
swapped. The result, -7 + 4x, is correct.

Bottom row: the mistake. Swapping the two symbols and leaving the minus sign
where it was gives 7 - 4x, which is a different number. The check at x = 3 is
printed under both, because that is how a reader can catch it.

Vertical plan (y, from the top):
    6.05  heading of the safe row
    5.35  the labels on the two step arrows
    4.55  the three cards of the safe row
    3.50  the check at x = 3, under each card
    2.95  the divider
    2.55  heading of the wrong row
    2.08  the label on its step arrow
    1.30  the two cards of the wrong row
    0.42  the check at x = 3

The arrow labels sit ABOVE the cards, never beside them: the cards are wide
and the gaps between them are narrow, so a label placed level with the arrow
lands on top of a card.

Run with:  python figures/fig_02_moving_a_subtraction.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"
GREEN = "#1E8449"
RED = "#C0392B"
GREY = "#78909C"
INK = "#212121"
TINT_GREY = "#ECEFF1"
TINT_GREEN = "#E8F5EC"
TINT_RED = "#FCEAE8"

W, H = 12.80, 6.40
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CARD_H = 1.05


def card(cx, cy, w, text, face, edge, fontsize=26):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - CARD_H / 2), w, CARD_H,
                                boxstyle="round,pad=0.05,rounding_size=0.15",
                                facecolor=face, edgecolor=edge,
                                linewidth=2.4, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize,
            color=INK, zorder=4)


def step_arrow(x0, x1, y, label, label_y, colour=ORANGE):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>",
                                 mutation_scale=22, linewidth=2.2,
                                 color=colour, zorder=2))
    ax.text((x0 + x1) / 2, label_y, label, ha="center", va="center",
            fontsize=15, color=colour)


# ------------------------------------------------------------ the safe route
Y_TOP = 4.55
ax.text(0.30, 6.05, "the safe way to swap them", ha="left", va="center",
        fontsize=20, color=GREEN, fontweight="bold")

card(1.85, Y_TOP, 2.55, r"$4x - 7$", TINT_GREY, GREY)
step_arrow(3.30, 5.00, Y_TOP, "the minus belongs to the 7", 5.35)
card(6.55, Y_TOP, 3.00, r"$4x + (-7)$", TINT_GREY, GREY)
step_arrow(8.20, 9.40, Y_TOP, "now swap", 5.35)
card(10.90, Y_TOP, 3.00, r"$-7 + 4x$", TINT_GREEN, GREEN)

for cx, colour, bold in ((1.85, GREY, "normal"), (6.55, GREY, "normal"),
                         (10.90, GREEN, "bold")):
    ax.text(cx, 3.50, r"at $x = 3$:  $5$", ha="center", va="center",
            fontsize=16, color=colour, fontweight=bold)

ax.plot([0.30, W - 0.30], [2.95, 2.95], color=GREY, linewidth=1.2,
        linestyle=(0, (4, 4)), zorder=1)

# ----------------------------------------------------------- the wrong route
Y_LOW = 1.30
ax.text(0.30, 2.55, "the mistake: leaving the sign where it was", ha="left",
        va="center", fontsize=20, color=RED, fontweight="bold")

card(1.85, Y_LOW, 2.55, r"$4x - 7$", TINT_GREY, GREY)
step_arrow(3.30, 5.00, Y_LOW, "swap the two symbols", 2.05, colour=RED)
card(6.55, Y_LOW, 3.00, r"$7 - 4x$", TINT_RED, RED)
# the stroke is as wide as the maths it crosses out, and no wider
ax.plot([5.72, 7.38], [Y_LOW, Y_LOW], color=RED, linewidth=2.6, zorder=5)

ax.text(6.55, 0.42, r"at $x = 3$:  $-5$", ha="center", va="center",
        fontsize=16, color=RED, fontweight="bold")
ax.text(10.30, Y_LOW, "a different number,\nso a different expression",
        ha="center", va="center", fontsize=16, color=RED, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_moving_a_subtraction.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_02_moving_a_subtraction.png")
