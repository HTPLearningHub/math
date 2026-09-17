"""Figure 1 - multiplying by a whole number changes the count, not the piece.

Four bars of exactly the same length. The argument the reader has to see is
an argument about *edges*, so every bar must be the same length and the cuts
must line up.

Bar A is where we start: one eighth.
Bar B is the right answer: two eighths - twice as much.
Bar C is the mistake: 2/16, made by doubling the bottom number as well. Its
shaded part ends at exactly the same place as bar A's, so nothing was
doubled at all. That is the whole reason the mistake is a mistake, and it is
visible rather than asserted.
Bar D shows that the right answer, 2/8, is one quarter.

Colours: blue is where we start, green is the right answer, red is the wrong
one (the Chapter 14 and 15 meaning of red - the thing that fails).

Run with:  python figures/fig_01_two_slices.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"             # the fraction we start from
GREEN = "#1E8449"            # the right answer
RED = "#C0392B"              # the wrong answer
GREY = "#78909C"
INK = "#212121"

TINT = {BLUE: "#E9F2FC", GREEN: "#E8F5EC", RED: "#FCEAE8"}

W, H = 11.40, 8.10
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

    # one outline round the whole bar - this is the "one whole"
    ax.add_patch(Rectangle((BAR_X, y), BAR_W, BAR_H, facecolor="none",
                           edgecolor=INK, linewidth=1.5, zorder=3))

    ax.text(BAR_X + BAR_W + 0.28, y + BAR_H / 2, note, ha="left", va="center",
            fontsize=13, color=colour if colour in (RED, GREEN) else GREY)

    return BAR_X + shaded * piece_w      # x of the shaded edge


ROW1, ROW2, ROW3, ROW4 = 5.70, 4.50, 3.06, 1.42

edge_start = bar(ROW1, 8, 1, BLUE, r"$\frac{1}{8}$", "one slice")
edge_right = bar(ROW2, 8, 2, GREEN, r"$\frac{2}{8}$", "two slices - twice as much")

# a rule that separates the correct doubling from the mistake below it
ax.plot([BAR_X - 1.35, BAR_X + BAR_W + 2.55], [ROW2 - 0.42, ROW2 - 0.42],
        color=GREY, linewidth=1.2, linestyle=(0, (4, 3)))

edge_wrong = bar(ROW3, 16, 2, RED, r"$\frac{2}{16}$",
                 "the bottom was doubled too")
bar(ROW4, 4, 1, GREEN, r"$\frac{1}{4}$", "the same edge as $\\frac{2}{8}$")

# the dashed blue line: where one eighth ends. The red bar stops there too,
# which means the mistake changed nothing at all.
ax.plot([edge_start, edge_start], [ROW3, ROW1 + BAR_H + 0.26], color=BLUE,
        linewidth=1.6, linestyle=(0, (3, 3)), zorder=4)
ax.text(edge_start, ROW1 + BAR_H + 0.42, "where one eighth ends",
        ha="center", va="center", fontsize=12, color=BLUE)

# the dashed green line: the right answer and one quarter end together
ax.plot([edge_right, edge_right], [ROW4, ROW2], color=GREEN,
        linewidth=1.6, linestyle=(0, (3, 3)), zorder=4)

# the sentence that names what the reader has just seen, placed in the gap
# between the wrong bar and the bar below it
# the white bbox lets the sentence sit on top of the green dashed line
# instead of being cut in half by it
ax.text(W / 2, (ROW3 + ROW4 + BAR_H) / 2,
        "the red shading ends where the FIRST bar ended - nothing was doubled",
        ha="center", va="center", fontsize=13, color=RED, zorder=5,
        bbox=dict(facecolor="white", edgecolor="none", pad=3.0))

ax.text(BAR_X - 1.62, ROW3 + BAR_H / 2, "wrong", ha="center", va="center",
        fontsize=13, color=RED, fontweight="bold", rotation=90)
ax.text(BAR_X - 1.62, ROW2 + BAR_H / 2, "right", ha="center", va="center",
        fontsize=13, color=GREEN, fontweight="bold", rotation=90)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.42,
        "Taking two slices does not make the slices smaller",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.86,
        "the cuts in the first three bars are the same width - only the "
        "number of shaded pieces changes",
        ha="center", va="center", fontsize=13, color=GREY)

# ------------------------------------------------------------- the bottom line
ax.text(W / 2, 0.72,
        r"$\frac{1}{8} \times 2 = \frac{2}{8} = \frac{1}{4}$,"
        r"   and $\frac{2}{16}$ is still just $\frac{1}{8}$",
        ha="center", va="center", fontsize=17, color=INK)
ax.text(W / 2, 0.24,
        "the whole number multiplies the top only, because the piece keeps "
        "its size",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_01_two_slices.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
