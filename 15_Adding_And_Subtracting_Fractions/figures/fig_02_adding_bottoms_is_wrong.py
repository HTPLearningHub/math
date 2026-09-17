"""Figure 2 - why you may not add the bottom numbers.

The commonest mistake in the whole topic is 1/3 + 1/4 = 2/7. The cheapest
way to kill it is not a rule but a picture: put 2/7 on the same bar as 1/3
and it is visibly *shorter*. You added something positive and the amount got
smaller, which is impossible.

The dashed red line is the whole argument. It starts at the right-hand edge
of the 1/3 bar and drops past the 2/7 bar, so the reader can see that the
wrong answer does not even reach the first fraction, never mind the sum.

The bottom bar is the correct answer, 7/12, drawn on a bar of the same
length so it can be compared with the other three by eye.

Colours: blue is the first fraction, orange the second, red the wrong
answer (the Chapter 14 meaning of red - the thing that fails), green the
correct answer.

Run with:  python figures/fig_02_adding_bottoms_is_wrong.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"             # the first fraction
ORANGE = "#E67E22"           # the second fraction
GREEN = "#1E8449"            # the right answer
RED = "#C0392B"              # the wrong answer
GREY = "#78909C"
INK = "#212121"

TINT = {BLUE: "#E9F2FC", ORANGE: "#FDF0E3", GREEN: "#E8F5EC", RED: "#FCEAE8"}

W, H = 11.40, 7.90
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BAR_X = 2.30                 # left edge of every bar
BAR_W = 6.30                 # all four bars are this long
BAR_H = 0.74


def bar(y, pieces, shaded, colour, label, note):
    """Draw one bar cut into `pieces` parts with the first `shaded` filled."""
    piece_w = BAR_W / pieces

    ax.text(BAR_X - 0.85, y + BAR_H / 2, label, ha="center", va="center",
            fontsize=24, color=colour)

    for i in range(pieces):
        px = BAR_X + i * piece_w
        ax.add_patch(Rectangle((px, y), piece_w, BAR_H,
                               facecolor=TINT[colour] if i < shaded else "white",
                               edgecolor=colour if i < shaded else GREY,
                               linewidth=1.9 if i < shaded else 1.1,
                               zorder=2))

    ax.add_patch(Rectangle((BAR_X, y), BAR_W, BAR_H, facecolor="none",
                           edgecolor=INK, linewidth=1.5, zorder=3))

    ax.text(BAR_X + BAR_W + 0.28, y + BAR_H / 2, note, ha="left", va="center",
            fontsize=13, color=colour if colour in (RED, GREEN) else GREY)

    return BAR_X + shaded * piece_w      # x of the shaded edge


ROW1, ROW2, ROW3, ROW4 = 5.44, 4.38, 2.96, 1.32

edge_third = bar(ROW1, 3, 1, BLUE, r"$\frac{1}{3}$", "one third,  about $0.333$")
bar(ROW2, 4, 1, ORANGE, r"$\frac{1}{4}$", "one quarter,  $0.25$")

# a rule that separates the question from the two candidate answers
ax.plot([BAR_X - 1.35, BAR_X + BAR_W + 2.55], [ROW2 - 0.40, ROW2 - 0.40],
        color=GREY, linewidth=1.2, linestyle=(0, (4, 3)))

edge_wrong = bar(ROW3, 7, 2, RED, r"$\frac{2}{7}$", "about $0.286$ - smaller!")
bar(ROW4, 12, 7, GREEN, r"$\frac{7}{12}$", "about $0.583$")

# the dashed line down from the edge of 1/3, carried through the wrong answer:
# the red shading stops before it, which is the whole argument
ax.plot([edge_third, edge_third], [ROW1, ROW1 + BAR_H + 0.26], color=BLUE,
        linewidth=1.6, linestyle=(0, (3, 3)), zorder=4)
ax.plot([edge_third, edge_third], [ROW1, ROW3], color=BLUE, linewidth=1.6,
        linestyle=(0, (3, 3)), zorder=4)
ax.text(edge_third, ROW1 + BAR_H + 0.42, "where one third ends",
        ha="center", va="center", fontsize=12, color=BLUE)

# the sentence that names what the reader has just seen, in the gap between
# the wrong answer and the right one
ax.text(W / 2, (ROW3 + ROW4 + BAR_H) / 2,
        "the wrong answer ends to the LEFT of the fraction it started from",
        ha="center", va="center", fontsize=13, color=RED)

# the label that names the mistake, sitting beside the red bar
ax.text(BAR_X - 1.62, ROW3 + BAR_H / 2, "wrong", ha="center", va="center",
        fontsize=13, color=RED, fontweight="bold", rotation=90)
ax.text(BAR_X - 1.62, ROW4 + BAR_H / 2, "right", ha="center", va="center",
        fontsize=13, color=GREEN, fontweight="bold", rotation=90)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.42,
        "Adding the bottom numbers makes the amount go down",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.86,
        "adding a positive amount can never leave you with less than you "
        "started with",
        ha="center", va="center", fontsize=13, color=GREY)

# ------------------------------------------------------------- the bottom line
ax.text(W / 2, 0.70, r"$\frac{1}{3} + \frac{1}{4} = \frac{2}{7}$  is impossible",
        ha="center", va="center", fontsize=17, color=RED)
ax.text(W / 2, 0.22,
        "a bigger bottom number means smaller pieces, not a bigger amount",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_02_adding_bottoms_is_wrong.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
