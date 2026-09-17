"""Figure 4 - the multiplier has to reach every term inside the bracket.

Left, in green: two arrows leave the 4, one for each term, and the answer has
two products in it.

Right, in red: only one arrow leaves the 4. The 3 is never multiplied, so it
walks out of the bracket unchanged and the answer is wrong. The check at
x = 1 is printed under both, because the two answers differ by 9 there.

Vertical plan (y, from the top):
    5.45  the two headings
    4.85  the note about the arrows
    4.05  the top of the curved arrows (rad 0.55 over a 1.05 span)
    3.20  the expression itself
    2.20  the arrow down to the answer
    1.30  the answer card
    0.35  the check at x = 1

The terms of the expression are drawn as separate pieces at fixed offsets, so
the arrows and the dashed ring can aim at one piece. The offsets leave 0.35 of
clear space around the 3, which is what the ring needs.

Run with:  python figures/fig_04_reaching_every_term.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"        # the multiplying that the rule performs
GREEN = "#1E8449"
RED = "#C0392B"
GREY = "#78909C"
INK = "#212121"
TINT_GREEN = "#E8F5EC"
TINT_RED = "#FCEAE8"

W, H = 12.80, 5.75
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

Y_EXPR = 3.20
Y_ANS = 1.30

# offsets of the six pieces of "4 ( 2x + 3 )" from the centre of a panel
DX_FOUR, DX_OPEN, DX_TERM, DX_PLUS, DX_THREE, DX_CLOSE = (
    -1.50, -1.02, -0.40, 0.22, 0.82, 1.35)


def reach(cx, x_to):
    """A curved arrow from the multiplier up and over to one term."""
    ax.add_patch(FancyArrowPatch((cx + DX_FOUR, Y_EXPR + 0.36),
                                 (cx + x_to, Y_EXPR + 0.36),
                                 connectionstyle="arc3,rad=-0.55",
                                 arrowstyle="-|>", mutation_scale=18,
                                 linewidth=2.2, color=ORANGE, zorder=4))


def half(cx, heading, colour, tint, answer, check, note):
    ax.text(cx, 5.45, heading, ha="center", va="center", fontsize=20,
            color=colour, fontweight="bold")
    ax.text(cx, 4.85, note, ha="center", va="center", fontsize=15,
            color=colour)

    for dx, txt, size, col in ((DX_FOUR, r"$4$", 30, INK),
                               (DX_OPEN, r"$($", 30, GREY),
                               (DX_TERM, r"$2x$", 30, INK),
                               (DX_PLUS, r"$+$", 26, GREY),
                               (DX_THREE, r"$3$", 30, INK),
                               (DX_CLOSE, r"$)$", 30, GREY)):
        ax.text(cx + dx, Y_EXPR, txt, ha="center", va="center", fontsize=size,
                color=col, zorder=3)

    ax.add_patch(FancyArrowPatch((cx, Y_EXPR - 0.58), (cx, Y_ANS + 0.65),
                                 arrowstyle="-|>", mutation_scale=20,
                                 linewidth=2.0, color=GREY, zorder=2))
    ax.add_patch(FancyBboxPatch((cx - 1.55, Y_ANS - 0.55), 3.10, 1.10,
                                boxstyle="round,pad=0.05,rounding_size=0.15",
                                facecolor=tint, edgecolor=colour,
                                linewidth=2.4, zorder=3))
    ax.text(cx, Y_ANS, answer, ha="center", va="center", fontsize=27,
            color=INK, zorder=4)
    ax.text(cx, 0.35, check, ha="center", va="center", fontsize=16,
            color=colour, fontweight="bold")


# --------------------------------------------------------------- done right
LEFT = 3.10
half(LEFT, "every term is reached", GREEN, TINT_GREEN, r"$8x + 12$",
     r"at $x = 1$:  $20$", "two arrows leave the 4")
reach(LEFT, DX_TERM)
reach(LEFT, DX_THREE)

ax.plot([6.45, 6.45], [0.15, 5.10], color=GREY, linewidth=1.3,
        linestyle=(0, (4, 4)), zorder=1)

# --------------------------------------------------------------- done wrong
RIGHT = 9.45
half(RIGHT, "one term is missed", RED, TINT_RED, r"$8x + 3$",
     r"at $x = 1$:  $11$", "only one arrow leaves the 4")
reach(RIGHT, DX_TERM)

# a dashed ring round the term that was never multiplied
ax.add_patch(FancyBboxPatch((RIGHT + DX_THREE - 0.28, Y_EXPR - 0.36),
                            0.56, 0.74,
                            boxstyle="round,pad=0.03,rounding_size=0.10",
                            facecolor="none", edgecolor=RED, linewidth=2.0,
                            linestyle=(0, (3, 3)), zorder=4))
# the stroke across the wrong answer, matched to the width of that answer
ax.plot([RIGHT - 0.95, RIGHT + 0.95], [Y_ANS, Y_ANS], color=RED,
        linewidth=2.6, zorder=5)
ax.text(RIGHT + 2.30, Y_EXPR, "never\nmultiplied", ha="center", va="center",
        fontsize=15, color=RED, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_reaching_every_term.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_04_reaching_every_term.png")
