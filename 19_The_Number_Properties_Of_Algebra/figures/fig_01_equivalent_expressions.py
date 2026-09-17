"""Figure 1 - two expressions that always agree.

One number goes in on the left. It travels down two different roads: through
4(2x + 3) and through 8x + 12. The two roads meet again on the right, because
whatever number went in, the same number comes out of both.

That is the whole meaning of the word "equivalent", and it is the test the
reader can always run: put a number in and compare.

Vertical plan (y, from the top):
    4.45  the two column headings
    3.55  the upper road: the box 4(2x + 3)
    2.55  the input ball, and the green output card (both centred)
    1.55  the lower road: the box 8x + 12
    0.55  the worked check at x = 2, under each box

Run with:  python figures/fig_01_equivalent_expressions.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from pathlib import Path

BLUE = "#2E86DE"          # the number going in
ORANGE = "#E67E22"        # a rule that does something to it
GREEN = "#1E8449"         # the value that comes out
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"

W, H = 12.80, 5.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

MID = 2.55                # the height the input and the output sit at
UPPER = 3.75              # the first road
LOWER = 1.35              # the second road


def card(cx, cy, w, h, text, face, edge, fontsize=27):
    """A rounded box with one piece of maths in the middle of it."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.05,rounding_size=0.16",
                                facecolor=face, edgecolor=edge,
                                linewidth=2.4, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize,
            color=INK, zorder=4)


def arrow(x0, y0, x1, y1, colour):
    """A plain arrow from one point to another, curved only if it climbs."""
    rad = 0.0 if abs(y1 - y0) < 0.01 else (0.18 if y1 > y0 else -0.18)
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1),
                                 connectionstyle=f"arc3,rad={rad}",
                                 arrowstyle="-|>", mutation_scale=22,
                                 linewidth=2.2, color=colour, zorder=2))


# ------------------------------------------------------- the number going in
ax.add_patch(Circle((1.45, MID), 0.62, facecolor=TINT_BLUE, edgecolor=BLUE,
                    linewidth=2.6, zorder=3))
ax.text(1.45, MID, r"$x$", ha="center", va="center", fontsize=30, color=INK,
        zorder=4)
ax.text(1.45, MID - 1.05, "any number", ha="center", va="center", fontsize=15,
        color=BLUE)
ax.text(1.45, MID - 1.45, "you like", ha="center", va="center", fontsize=15,
        color=BLUE)

# ------------------------------------------------------------- the two roads
arrow(2.15, MID + 0.25, 4.45, UPPER - 0.10, BLUE)
arrow(2.15, MID - 0.25, 4.45, LOWER + 0.10, BLUE)

card(6.05, UPPER, 3.05, 1.22, r"$4(2x + 3)$", TINT_ORANGE, ORANGE)
card(6.05, LOWER, 3.05, 1.22, r"$8x + 12$", TINT_ORANGE, ORANGE)

ax.text(6.05, UPPER + 1.00, "one way of writing the rule", ha="center",
        va="center", fontsize=15, color=GREY)
ax.text(6.05, LOWER - 1.00, "another way of writing the rule", ha="center",
        va="center", fontsize=15, color=GREY)

# the check at x = 2, tucked just inside each box's road
ax.text(6.05, UPPER - 0.92, r"at $x = 2$:   $4(7) = 28$", ha="center",
        va="center", fontsize=16, color=GREY)
ax.text(6.05, LOWER + 0.92, r"at $x = 2$:   $16 + 12 = 28$", ha="center",
        va="center", fontsize=16, color=GREY)

# ------------------------------------------------------ the roads meet again
arrow(7.65, UPPER - 0.10, 9.85, MID + 0.30, GREEN)
arrow(7.65, LOWER + 0.10, 9.85, MID - 0.30, GREEN)

card(11.15, MID, 2.55, 1.35, "the same\nnumber", TINT_GREEN, GREEN,
     fontsize=21)
ax.text(11.15, MID - 1.25, "every single time", ha="center", va="center",
        fontsize=15, color=GREEN, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_equivalent_expressions.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_01_equivalent_expressions.png")
