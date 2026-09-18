"""Figure 1 - an equation gives one number, an inequality gives a whole stretch.

This is the opening figure of the chapter, and its only job is to make the
difference between the two questions impossible to miss. Both lines are
drawn to the same scale and placed one above the other, so the reader is
comparing two answers to almost the same question, not two pictures.

Upper line:  x + 2 = 5  -> one filled green dot at 3, and nothing else.
Lower line:  x + 2 < 5  -> a hollow circle at 3 and a thick green ray
                           running left towards the end of the line.

Two of the numbers inside the solution set (0.5 and -1.5) are named under
the lower line, in green, among the whole numbers. They are there to stop
the reader assuming a solution set holds only whole numbers.

Horizontal plan (x): one shared scale, -3 to 8 mapped to 2.20 to 11.30,
so one unit is 0.827 of an inch. The axis overhangs its last tick by 0.78
and the green ray stops 0.42 past it, so the green arrowhead stays clear
of the black one - that arrowhead is what says the answer never ends.

Vertical plan (y, top to bottom):
    5.62  heading
    4.92  the upper statement, on a card
    4.05  the upper number line
    3.70  the numbers under it
    3.22  what the upper answer is
    2.42  the lower statement, on a card
    1.55  the lower number line
    1.20  the whole numbers under the line
    1.02  the two numbers from inside the answer that are not whole
    0.62  what the lower answer is
    0.16  closing note

Run with:  python figures/fig_01_one_answer_or_many.py
"""

import matplotlib
matplotlib.use("Agg")                       # no window, just a file
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"          # the question being asked
GREEN = "#1E8449"         # the answer
GREY = "#78909C"          # the line itself, and quiet labels
INK = "#212121"
BLUE_T = "#E9F2FC"
GREEN_T = "#E8F5EC"

W, H = 12.60, 6.00
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])               # fill the whole canvas
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

X0, X1 = 2.20, 11.30      # where -3 and 8 land on the page
V0, V1 = -3.0, 8.0        # the range of numbers the line shows
OVERHANG = 0.78           # how far the axis runs past its last tick
RAY_END = 0.42            # how far the green ray runs past its last tick


def px(value):
    """Turn a number on the line into a position on the page."""
    return X0 + (X1 - X0) * (value - V0) / (V1 - V0)


def number_line(y):
    """Draw one axis with a tick and a label at every whole number."""
    ax.annotate("", xy=(X1 + OVERHANG, y), xytext=(X0 - OVERHANG, y),
                arrowprops=dict(arrowstyle="<|-|>", linewidth=1.8,
                                color=INK))
    for value in range(int(V0), int(V1) + 1):
        ax.plot([px(value), px(value)], [y - 0.10, y + 0.10],
                linewidth=1.5, color=INK)
        ax.text(px(value), y - 0.35, str(value), ha="center", va="center",
                fontsize=11.5, color=GREY)


def card(x, y, text, edge, fill, fontsize=19):
    """A rounded box carrying one statement, centred on (x, y)."""
    ax.text(x, y, text, ha="center", va="center", fontsize=fontsize,
            color=INK, zorder=3,
            bbox=dict(boxstyle="round,pad=0.42", facecolor=fill,
                      edgecolor=edge, linewidth=1.8))


ax.text(0.55, 5.62, "the same two sides, two different signs between them",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# ------------------------------------------------------------ upper line
card(1.55, 4.92, r"$x + 2 = 5$", BLUE, BLUE_T)
number_line(4.05)

# exactly one number works, so exactly one dot is drawn
ax.plot([px(3)], [4.05], marker="o", markersize=15, color=GREEN, zorder=5)
ax.text(px(3), 4.55, r"$x = 3$", ha="center", va="center", fontsize=16,
        color=GREEN, fontweight="bold")

ax.text(0.55, 3.22, "one number, and no other", ha="left", va="center",
        fontsize=15, color=GREEN, fontweight="bold")

# a faint divider between the two halves of the figure
ax.plot([0.45, W - 0.45], [2.85, 2.85], linewidth=1.0, color=GREY,
        linestyle=(0, (4, 4)), zorder=1)

# ------------------------------------------------------------ lower line
card(1.55, 2.42, r"$x + 2 < 5$", BLUE, BLUE_T)
number_line(1.55)

# the solution set: a thick ray from 3 leftwards, stopping short of the
# black arrowhead so that its own arrowhead can be seen
ax.annotate("", xy=(X0 - RAY_END, 1.55), xytext=(px(3), 1.55),
            arrowprops=dict(arrowstyle="-|>", linewidth=5.5, color=GREEN,
                            mutation_scale=17), zorder=4)
# the hollow circle says 3 itself is not one of the answers
ax.plot([px(3)], [1.55], marker="o", markersize=15,
        markerfacecolor="white", markeredgecolor=GREEN,
        markeredgewidth=3.0, zorder=6)
ax.text(px(3), 2.05, r"$x < 3$", ha="center", va="center", fontsize=16,
        color=GREEN, fontweight="bold")

# two numbers from inside the answer that are not whole numbers; they sit
# in the row of tick labels, in the gaps between them, and in green
for value, label in ((-1.5, r"$-1.5$"), (0.5, r"$0.5$")):
    ax.plot([px(value)], [1.55], marker="o", markersize=8, color=GREEN,
            zorder=5)
    ax.text(px(value), 1.02, label, ha="center", va="center", fontsize=11,
            color=GREEN, fontweight="bold")

ax.text(0.55, 0.62, "every number along the green arrow, and it never ends",
        ha="left", va="center", fontsize=15, color=GREEN, fontweight="bold")

ax.text(0.55, 0.16,
        "changing one sign changes the answer from a single point "
        "into an endless stretch of the line",
        ha="left", va="center", fontsize=12.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_one_answer_or_many.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_01_one_answer_or_many.png")
