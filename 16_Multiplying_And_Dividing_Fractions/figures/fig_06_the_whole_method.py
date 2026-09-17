"""Figure 6 - multiplying and dividing are one method, not two.

The flow has exactly one question in it: is this a division? If it is, one
box is added at the front - flip the second fraction - and from that point
on the work is identical. Every path ends in the same two green boxes.

Drawing it this way makes the chapter's claim visible: division is not a
second procedure to learn. It is multiplication with one extra move.

The layout is the Chapter 15 flow with the branch on the other side, so the
two chapters can be compared page to page. The box width was measured from
the longest line of text rather than guessed, which is the lesson Chapter 15
left behind.

Colours: grey is the setting up, blue is the question, orange is the one
extra step a division costs, green is what every problem shares.

Run with:  python figures/fig_06_the_whole_method.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
from pathlib import Path

BLUE = "#2E86DE"             # the question
ORANGE = "#E67E22"           # the extra step a division costs
GREEN = "#1E8449"            # the steps every problem has
GREY = "#78909C"
INK = "#212121"

TINT = {BLUE: "#E9F2FC", ORANGE: "#FDF0E3", GREEN: "#E8F5EC", GREY: "#ECEFF1"}

W, H = 14.60, 11.20
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CX, RX = 4.55, 10.70          # the main column and the branch on the right
BW, BH = 6.30, 1.05          # every box is the same size

Y_START = 9.55
Y_WRITE = 7.95
Y_ASK = 6.20
Y_FLIP = 4.35
Y_MULT = 2.70
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
box(CX, Y_START, GREY, "two numbers, times or divided",
    r"for example $\frac{2}{5} \div \frac{3}{4}$")
arrow(CX, Y_START - BH / 2, CX, Y_WRITE + BH / 2)

# ------------------------------------------------ the step that never changes
box(CX, Y_WRITE, GREY, "write every whole number over $1$",
    r"$2$ becomes $\frac{2}{1}$, and nothing else changes")
arrow(CX, Y_WRITE - BH / 2, CX, Y_ASK + 0.90)

# ------------------------------------------------------- the one question asked
diamond = Polygon([(CX, Y_ASK + 0.88), (CX + 3.15, Y_ASK),
                   (CX, Y_ASK - 0.88), (CX - 3.15, Y_ASK)],
                  closed=True, facecolor=TINT[BLUE], edgecolor=BLUE,
                  linewidth=2.0, zorder=3)
ax.add_patch(diamond)
ax.text(CX, Y_ASK + 0.14, "is it a division?", ha="center", va="center",
        fontsize=14, color=INK, fontweight="bold", zorder=4)
ax.text(CX, Y_ASK - 0.28, "this is the only question there is",
        ha="center", va="center", fontsize=12, color=GREY, zorder=4)

# ------------------------------------------------ the YES branch, out to the right
elbow(CX + 3.15, Y_ASK, RX, Y_FLIP + BH / 2, horizontal_first=True)
ax.text(CX + 3.85, Y_ASK + 0.30, "yes", ha="center", va="center",
        fontsize=15, color=ORANGE, fontweight="bold")

box(RX, Y_FLIP, ORANGE, "flip the second fraction over",
    r"and write $\times$ where the $\div$ was")

# the branch rejoins the main column at the very next box
elbow(RX, Y_FLIP - BH / 2, CX + BW / 2, Y_MULT, horizontal_first=False)

# ----------------------------------------------------- the NO branch, straight
arrow(CX, Y_ASK - 0.88, CX, Y_MULT + BH / 2)
ax.text(CX - 0.24, Y_ASK - 1.32, "no", ha="right", va="center",
        fontsize=15, color=GREEN, fontweight="bold")

# ---------------------------------------------- the part every problem shares
box(CX, Y_MULT, GREEN, "multiply the tops, multiply the bottoms",
    "no common bottom number is ever needed")
arrow(CX, Y_MULT - BH / 2, CX, Y_SIMPLIFY + BH / 2)

box(CX, Y_SIMPLIFY, GREEN, "simplify the answer",
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
        "One question, and the same three steps either way",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.80,
        "a division costs one orange box and nothing else - after it, the "
        "work is a multiplication",
        ha="center", va="center", fontsize=13, color=GREY)

# A quiet label for the branch. It sits BELOW the horizontal join at
# y = Y_MULT, because above it the elbow arrow runs straight through the text.
ax.text(RX, 1.95, "this one box is the whole difference", ha="center",
        va="center", fontsize=12.5, color=ORANGE)
ax.text(RX, 1.57, "between the two operations", ha="center", va="center",
        fontsize=12.5, color=ORANGE)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_06_the_whole_method.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
