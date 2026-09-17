"""Figure 5 - the whole method on one page.

Everything in this chapter is one question and two answers to it. The
question is "do the two fractions already have the same bottom number?". If
they do, there is one step. If they do not, two steps are added at the front
to make them match, and then it is the same one step again.

Drawing it as a flow makes that visible: the left branch is *extra work*,
not a different method. Both paths arrive at exactly the same box.

Colours: blue is the question, orange is the extra work the left branch
costs, green is the part that every problem has.

Run with:  python figures/fig_05_the_whole_method.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
from pathlib import Path

BLUE = "#2E86DE"             # the question
ORANGE = "#E67E22"           # the two extra steps
GREEN = "#1E8449"            # the steps every problem has
GREY = "#78909C"
INK = "#212121"

TINT = {BLUE: "#E9F2FC", ORANGE: "#FDF0E3", GREEN: "#E8F5EC", GREY: "#ECEFF1"}

W, H = 14.20, 11.00
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CX, LX = 10.20, 3.70          # the main column and the left branch
BW, BH = 5.80, 1.05          # every box is the same size

Y_START = 9.30
Y_ASK = 7.55
Y_LCD = 5.65
Y_REWRITE = 4.20
Y_COMBINE = 2.70
Y_SIMPLIFY = 1.35
Y_DONE = 0.38


def box(cx, cy, colour, title, body, w=BW, h=BH):
    """Draw one rounded step box with a bold line and a quiet line under it."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.14",
                                facecolor=TINT[colour], edgecolor=colour,
                                linewidth=2.0, zorder=3))
    ax.text(cx, cy + 0.17, title, ha="center", va="center",
            fontsize=14, color=INK, fontweight="bold", zorder=4)
    ax.text(cx, cy - 0.22, body, ha="center", va="center",
            fontsize=12, color=GREY, zorder=4)


def arrow(x1, y1, x2, y2):
    """A plain straight arrow between two points."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=GREY, linewidth=2.0,
                                shrinkA=0, shrinkB=0), zorder=2)


def elbow(x1, y1, x2, y2, horizontal_first):
    """An arrow that turns one corner, so the branch stays out of the column."""
    if horizontal_first:
        ax.plot([x1, x2], [y1, y1], color=GREY, linewidth=2.0, zorder=2)
        arrow(x2, y1, x2, y2)
    else:
        ax.plot([x1, x1], [y1, y2], color=GREY, linewidth=2.0, zorder=2)
        arrow(x1, y2, x2, y2)


# --------------------------------------------------------------- the start box
box(CX, Y_START, GREY, "two fractions to add or subtract",
    r"for example $\frac{1}{3} + \frac{1}{4}$")
arrow(CX, Y_START - BH / 2, CX, Y_ASK + 0.90)

# ------------------------------------------------------- the one question asked
diamond = Polygon([(CX, Y_ASK + 0.88), (CX + 2.90, Y_ASK),
                   (CX, Y_ASK - 0.88), (CX - 2.90, Y_ASK)],
                  closed=True, facecolor=TINT[BLUE], edgecolor=BLUE,
                  linewidth=2.0, zorder=3)
ax.add_patch(diamond)
ax.text(CX, Y_ASK + 0.14, "same bottom number?", ha="center", va="center",
        fontsize=14, color=INK, fontweight="bold", zorder=4)
ax.text(CX, Y_ASK - 0.28, "this is the only question there is",
        ha="center", va="center", fontsize=12, color=GREY, zorder=4)

# ------------------------------------------------ the NO branch, down the left
elbow(CX - 2.90, Y_ASK, LX, Y_LCD + BH / 2, horizontal_first=True)
ax.text(CX - 3.60, Y_ASK + 0.30, "no", ha="center", va="center",
        fontsize=15, color=ORANGE, fontweight="bold")

box(LX, Y_LCD, ORANGE, "1.  find the least common denominator",
    "the LCM of the two bottom numbers")
arrow(LX, Y_LCD - BH / 2, LX, Y_REWRITE + BH / 2)

box(LX, Y_REWRITE, ORANGE, "2.  rewrite both fractions",
    "multiply each top and bottom by the same number")

# the left branch rejoins the main column at the very next box
elbow(LX, Y_REWRITE - BH / 2, CX - BW / 2, Y_COMBINE, horizontal_first=False)

# ----------------------------------------------------- the YES branch, straight
arrow(CX, Y_ASK - 0.88, CX, Y_COMBINE + BH / 2)
ax.text(CX + 0.24, Y_ASK - 1.32, "yes", ha="left", va="center",
        fontsize=15, color=GREEN, fontweight="bold")

# ---------------------------------------------- the part every problem shares
box(CX, Y_COMBINE, GREEN, "3.  add or subtract the top numbers",
    "the bottom number is copied down, never added")
arrow(CX, Y_COMBINE - BH / 2, CX, Y_SIMPLIFY + BH / 2)

box(CX, Y_SIMPLIFY, GREEN, "4.  simplify the answer",
    "divide top and bottom by their greatest common factor")
arrow(CX, Y_SIMPLIFY - BH / 2, CX, Y_DONE + 0.30)

ax.add_patch(FancyBboxPatch((CX - 1.30, Y_DONE - 0.28), 2.60, 0.56,
                            boxstyle="round,pad=0.02,rounding_size=0.26",
                            facecolor=GREEN, edgecolor=GREEN, linewidth=2.0,
                            zorder=3))
ax.text(CX, Y_DONE, "finished", ha="center", va="center", fontsize=15,
        color="white", fontweight="bold", zorder=4)

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.40,
        "One question, and the same last two steps either way",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.80,
        "the orange boxes are extra work, not a different method - both "
        "paths end in the same green box",
        ha="center", va="center", fontsize=13, color=GREY)

# a quiet label for the branch, placed under the two orange boxes
ax.text(LX, 2.00, "these two steps only make the pieces",
        ha="center", va="center", fontsize=12.5, color=ORANGE)
ax.text(LX, 1.62, "the same size. They add nothing.",
        ha="center", va="center", fontsize=12.5, color=ORANGE)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_05_the_whole_method.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
