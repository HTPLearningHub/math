"""Figure 2 - what a solved equation looks like.

Two cards side by side. On the left the letter is still tied to a number;
on the right it stands alone. The whole of this chapter is the orange
arrow in between.

The left card is grey, not red: 4d = 20 is perfectly true. It is simply
not yet an answer. Only the finished form is green.

Vertical plan (y, top to bottom):
    3.85  heading
    2.30  the two cards (height 1.10)
    1.35  the label under each card
    0.45  closing note

Run with:  python figures/fig_02_isolating_the_variable.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"        # the move being made
GREEN = "#1E8449"         # the finished form
GREY = "#78909C"
INK = "#212121"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"
TINT_GREY = "#ECEFF1"

W, H = 10.80, 4.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.60, 3.85, "an equation is solved when the letter stands alone",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

CARD_Y, CARD_H = 2.30, 1.10
LEFT_X0, RIGHT_X0, CARD_W = 0.60, 6.60, 3.60

# the starting form: true, but not an answer yet
ax.add_patch(FancyBboxPatch((LEFT_X0, CARD_Y - CARD_H / 2), CARD_W, CARD_H,
                            boxstyle="round,pad=0.05,rounding_size=0.16",
                            facecolor=TINT_GREY, edgecolor=GREY,
                            linewidth=2.2, zorder=3))
ax.text(LEFT_X0 + CARD_W / 2, CARD_Y, r"$4d = 20$", ha="center", va="center",
        fontsize=30, color=INK, zorder=4)
ax.text(LEFT_X0 + CARD_W / 2, 1.35,
        r"$d$ is not alone - a $4$ is stuck to it",
        ha="center", va="center", fontsize=15, color=GREY)

# the move, named above its own arrow
ax.add_patch(FancyArrowPatch((LEFT_X0 + CARD_W + 0.35, CARD_Y),
                             (RIGHT_X0 - 0.35, CARD_Y),
                             arrowstyle="-|>", mutation_scale=22,
                             linewidth=2.8, color=ORANGE, zorder=5))
ax.add_patch(FancyBboxPatch((4.50, CARD_Y + 0.42), 1.80, 0.56,
                            boxstyle="round,pad=0.04,rounding_size=0.26",
                            facecolor=TINT_ORANGE, edgecolor=ORANGE,
                            linewidth=1.8, zorder=3))
ax.text(5.40, CARD_Y + 0.70, "isolate it", ha="center", va="center",
        fontsize=15, color=ORANGE, zorder=4)

# the finished form
ax.add_patch(FancyBboxPatch((RIGHT_X0, CARD_Y - CARD_H / 2), CARD_W, CARD_H,
                            boxstyle="round,pad=0.05,rounding_size=0.16",
                            facecolor=TINT_GREEN, edgecolor=GREEN,
                            linewidth=2.6, zorder=3))
ax.text(RIGHT_X0 + CARD_W / 2, CARD_Y, r"$d = 5$", ha="center", va="center",
        fontsize=30, color=INK, zorder=4)
ax.text(RIGHT_X0 + CARD_W / 2, 1.35,
        "the letter alone, and one number", ha="center", va="center",
        fontsize=15, color=GREEN)

ax.text(0.60, 0.45, "both lines say the same thing about the same number - "
        "only the second one says it plainly", ha="left", va="center",
        fontsize=15, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_isolating_the_variable.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_02_isolating_the_variable.png")
