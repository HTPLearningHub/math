"""Figure 1 - adding two fractions that already have the same bottom number.

The whole point of this picture is that the cut marks never move. All four
bars are the same length and the first three are cut in exactly the same
places, so the shaded pieces are interchangeable. Adding is then nothing but
counting them: one piece plus three pieces is four pieces.

The fourth bar is the simplification check from Chapter 1, section 3.3 drawn
rather than calculated: cut the same bar into two, shade one, and the shaded
edge lands in the same place. The dashed drop line is what carries that.

Colours follow the Chapter 13 / 14 convention: blue is the first fraction,
orange the second, green the answer.

Run with:  python figures/fig_01_adding_eighths.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"             # the first fraction
ORANGE = "#E67E22"           # the second fraction
GREEN = "#1E8449"            # the answer
GREY = "#78909C"             # quiet labels and rules
INK = "#212121"

TINT = {BLUE: "#E9F2FC", ORANGE: "#FDF0E3", GREEN: "#E8F5EC"}

W, H = 11.00, 7.10
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BAR_X = 2.55                 # left edge of every bar
BAR_W = 6.60                 # every bar is exactly this long - that is the point
BAR_H = 0.76


def bar(y, pieces, shaded, colour, sign, label):
    """Draw one bar cut into `pieces` equal parts with the first `shaded` filled."""
    piece_w = BAR_W / pieces

    # the sign (+, = or nothing) sits in its own column on the far left
    if sign:
        ax.text(BAR_X - 1.80, y + BAR_H / 2, sign, ha="center", va="center",
                fontsize=30, color=INK)

    # the fraction that this bar shows
    ax.text(BAR_X - 0.88, y + BAR_H / 2, label, ha="center", va="center",
            fontsize=25, color=colour)

    for i in range(pieces):
        px = BAR_X + i * piece_w
        ax.add_patch(Rectangle((px, y), piece_w, BAR_H,
                               facecolor=TINT[colour] if i < shaded else "white",
                               edgecolor=colour if i < shaded else GREY,
                               linewidth=1.9 if i < shaded else 1.1,
                               zorder=2))

    # one outline round the whole bar, so the four bars read as one length
    ax.add_patch(Rectangle((BAR_X, y), BAR_W, BAR_H, facecolor="none",
                           edgecolor=INK, linewidth=1.6, zorder=3))

    # how many pieces are shaded, said in words to the right of the bar
    ax.text(BAR_X + BAR_W + 0.30, y + BAR_H / 2,
            f"{shaded} of the {pieces} pieces", ha="left", va="center",
            fontsize=13, color=GREY)

    return BAR_X + shaded * piece_w      # x of the shaded edge, for the drop line


ROW1, ROW2, ROW3, ROW4 = 5.12, 3.96, 2.56, 1.38

bar(ROW1, 8, 1, BLUE, "", r"$\frac{1}{8}$")
bar(ROW2, 8, 3, ORANGE, "+", r"$\frac{3}{8}$")

# a thin rule between the question and the answer
ax.plot([BAR_X - 2.10, BAR_X + BAR_W + 1.90], [ROW2 - 0.38, ROW2 - 0.38],
        color=GREY, linewidth=1.2, linestyle=(0, (4, 3)))

edge_eighths = bar(ROW3, 8, 4, GREEN, "=", r"$\frac{4}{8}$")
edge_half = bar(ROW4, 2, 1, GREEN, "", r"$\frac{1}{2}$")

# the drop line that shows 4/8 and 1/2 end in the same place
ax.plot([edge_eighths, edge_half], [ROW3, ROW4 + BAR_H],
        color=GREEN, linewidth=1.8, linestyle=(0, (3, 3)), zorder=4)
ax.text(edge_half + 0.18, (ROW3 + ROW4 + BAR_H) / 2, "same edge",
        ha="left", va="center", fontsize=12, color=GREEN)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.42,
        "Same size pieces, so adding is just counting them",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.86,
        "every bar is the same length, and the first three are cut in exactly "
        "the same places",
        ha="center", va="center", fontsize=13, color=GREY)

# ------------------------------------------------------------- the bottom line
ax.text(W / 2, 0.58,
        r"$1$ eighth $+$ $3$ eighths $=$ $4$ eighths",
        ha="center", va="center", fontsize=17, color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_adding_eighths.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
