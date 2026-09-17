"""Figure 5 - an equation is a machine: the rule on top, one number below it.

Top lane: the rule y = 2x + 1 broken into the two things it actually does, in
the order it does them. Multiply by 2 first, add 1 second.

Bottom lane: the same machine with the number 4 walking through it. 4 becomes
8 inside the first box and 9 inside the second, so the output is 9.

The two lanes are lined up column by column on purpose: every orange box in
the rule has exactly one number underneath it. That is what "the order of
operations decides the order of the machine" looks like.

Run with:  python figures/fig_05_the_machine.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # the input
ORANGE = "#E67E22"        # the operations the rule performs
GREEN = "#1E8449"         # the output
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"

W, H = 13.00, 5.40
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# the four column centres: input, first operation, second operation, output
COLS = [1.85, 5.00, 8.30, 11.45]
Y_RULE = 3.70                          # the lane that shows the rule
Y_NUM = 1.55                           # the lane that shows one number


def box(cx, cy, w, h, text, face, edge, fontsize=22, weight="normal",
        tcolour=INK):
    """One rounded box with centred text."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.06,rounding_size=0.15",
                                facecolor=face, edgecolor=edge,
                                linewidth=2.2, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize,
            color=tcolour, fontweight=weight, zorder=4)


def arrow(x1, x2, y, colour):
    """A horizontal arrow from x1 to x2 along the line y."""
    ax.add_patch(FancyArrowPatch((x1, y), (x2, y), arrowstyle="-|>",
                                 mutation_scale=19, color=colour,
                                 linewidth=2.1, zorder=2))


# ------------------------------------------------------------------ headings
ax.text(0.28, H - 0.40, r"the rule   $y = 2x + 1$", ha="left", va="center",
        fontsize=20, color=ORANGE, fontweight="bold")
ax.text(0.28, 0.42, r"one number through it:   $x = 4$", ha="left",
        va="center", fontsize=20, color=BLUE, fontweight="bold")

# ------------------------------------------------------------- the rule lane
box(COLS[0], Y_RULE, 1.85, 0.95, r"$x$", TINT_BLUE, BLUE, fontsize=26)
box(COLS[1], Y_RULE, 2.45, 0.95, r"$\times\, 2$", TINT_ORANGE, ORANGE)
box(COLS[2], Y_RULE, 2.45, 0.95, r"$+\, 1$", TINT_ORANGE, ORANGE)
box(COLS[3], Y_RULE, 1.85, 0.95, r"$y$", TINT_GREEN, GREEN, fontsize=26)
arrow(COLS[0] + 1.00, COLS[1] - 1.32, Y_RULE, GREY)
arrow(COLS[1] + 1.32, COLS[2] - 1.32, Y_RULE, GREY)
arrow(COLS[2] + 1.32, COLS[3] - 1.00, Y_RULE, GREY)
ax.text(COLS[0], Y_RULE + 0.78, "input", ha="center", va="center",
        fontsize=15, color=BLUE)
ax.text(COLS[1], Y_RULE + 0.78, "first", ha="center", va="center",
        fontsize=15, color=ORANGE)
ax.text(COLS[2], Y_RULE + 0.78, "second", ha="center", va="center",
        fontsize=15, color=ORANGE)
ax.text(COLS[3], Y_RULE + 0.78, "output", ha="center", va="center",
        fontsize=15, color=GREEN)

# ----------------------------------------------------------- the number lane
box(COLS[0], Y_NUM, 1.85, 0.95, r"$4$", TINT_BLUE, BLUE, fontsize=26)
box(COLS[1], Y_NUM, 2.45, 0.95, r"$4 \times 2 = 8$", TINT_ORANGE, ORANGE,
    fontsize=19)
box(COLS[2], Y_NUM, 2.45, 0.95, r"$8 + 1 = 9$", TINT_ORANGE, ORANGE,
    fontsize=19)
box(COLS[3], Y_NUM, 1.85, 0.95, r"$9$", TINT_GREEN, GREEN, fontsize=26,
    weight="bold", tcolour=GREEN)
arrow(COLS[0] + 1.00, COLS[1] - 1.32, Y_NUM, BLUE)
arrow(COLS[1] + 1.32, COLS[2] - 1.32, Y_NUM, BLUE)
arrow(COLS[2] + 1.32, COLS[3] - 1.00, Y_NUM, GREEN)

# the dotted columns that tie each rule box to the number under it
for cx in COLS:
    ax.plot([cx, cx], [Y_NUM + 0.52, Y_RULE - 0.52], color=GREY,
            linewidth=1.1, linestyle=(0, (2, 4)), zorder=1)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_05_the_machine.png", dpi=170, facecolor="white")
print("saved", out / "fig_05_the_machine.png")
