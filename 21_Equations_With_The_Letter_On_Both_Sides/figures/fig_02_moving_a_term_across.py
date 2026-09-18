"""Figure 2 - one move turns a two-sided equation into a one-sided one.

The same term is taken away from each side. On the left four x less one x
leaves three x; on the right one x less one x leaves nothing at all. That
second column is the whole reason the move is worth making.

The result card is grey, not green: 3x + 3 = -6 is true but not an answer.
That is Chapter 20's colour convention and it is kept here.

Horizontal plan (x):
    3.10  the left side of the equation
    5.40  the equals sign
    7.70  the right side

Vertical plan (y, top to bottom):
    4.30  heading
    3.55  the equation, as two expressions and an equals sign
    3.22  the label that says the move is the same on both sides
    2.85  the two orange pills, joined by a dashed line
    2.10  the two arrows down (2.55 -> 1.95)
    1.60  the result, in two grey cards
    0.80  what happened on each side
    0.25  closing note

Run with:  python figures/fig_02_moving_a_term_across.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"        # the move being made
GREY = "#78909C"
INK = "#212121"
TINT_ORANGE = "#FDF0E3"
TINT_GREY = "#ECEFF1"

W, H = 10.80, 4.75
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT, MID, RIGHT = 3.10, 5.40, 7.70

ax.text(0.60, 4.30, "take the same term off each side",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# the starting equation
ax.text(LEFT, 3.55, r"$4x + 3$", ha="center", va="center",
        fontsize=28, color=INK)
ax.text(MID, 3.55, r"$=$", ha="center", va="center", fontsize=28, color=INK)
ax.text(RIGHT, 3.55, r"$x - 6$", ha="center", va="center",
        fontsize=28, color=INK)

# the move, written once under each side, with a dashed line saying that
# the two pills hold exactly the same thing
ax.text(MID, 3.22, "the same move on both sides", ha="center", va="center",
        fontsize=13, color=GREY)
ax.plot([LEFT + 0.55, RIGHT - 0.55], [2.85, 2.85], linestyle=(0, (4, 4)),
        linewidth=1.6, color=ORANGE, zorder=2)
for xpos in (LEFT, RIGHT):
    ax.add_patch(FancyBboxPatch((xpos - 0.55, 2.55), 1.10, 0.60,
                                boxstyle="round,pad=0.04,rounding_size=0.28",
                                facecolor=TINT_ORANGE, edgecolor=ORANGE,
                                linewidth=2.0, zorder=3))
    ax.text(xpos, 2.85, r"$-\,x$", ha="center", va="center",
            fontsize=20, color=ORANGE, zorder=4)
    # 0.60 of run, which is enough for the shaft to be drawn
    ax.add_patch(FancyArrowPatch((xpos, 2.55), (xpos, 1.95),
                                 arrowstyle="-|>", mutation_scale=20,
                                 linewidth=2.6, color=ORANGE, zorder=5))

# the result: true, but not finished, so grey
for xpos, piece, width in ((LEFT, r"$3x + 3$", 2.40),
                           (RIGHT, r"$-6$", 2.40)):
    ax.add_patch(FancyBboxPatch((xpos - width / 2, 1.60 - 0.45), width, 0.90,
                                boxstyle="round,pad=0.05,rounding_size=0.16",
                                facecolor=TINT_GREY, edgecolor=GREY,
                                linewidth=2.2, zorder=3))
    ax.text(xpos, 1.60, piece, ha="center", va="center",
            fontsize=26, color=INK, zorder=4)
ax.text(MID, 1.60, r"$=$", ha="center", va="center", fontsize=26, color=INK)

# what actually happened in each column
ax.text(LEFT, 0.80, r"four $x$ less one $x$ leaves three $x$", ha="center",
        va="center", fontsize=14, color=GREY)
ax.text(RIGHT, 0.80, r"one $x$ less one $x$ leaves nothing", ha="center",
        va="center", fontsize=14, color=ORANGE)

ax.text(0.60, 0.25, "the letter has gone from the right - and this is the "
        "shape Chapter 20 already solves", ha="left", va="center",
        fontsize=15, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_moving_a_term_across.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_02_moving_a_term_across.png")
