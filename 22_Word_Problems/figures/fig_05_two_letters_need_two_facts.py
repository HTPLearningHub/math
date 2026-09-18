"""Figure 5 - one fact leaves a whole list; the second fact picks one row.

Readers meeting two letters for the first time often assume the first
sentence of the story already pins both of them down. It does not. Every
row of this table obeys j = r + 6, and they cannot all be the answer.

The third column is the second fact being tested on each row, and exactly
one row reaches 68. That row is the answer, and the picture says why it is
the answer rather than simply announcing it.

Horizontal plan (x), three columns inside a table 6.90 wide from 1.70:
    2.55   r
    4.25   j
    6.75   2r + 3j
    8.95   the left edge of the note beside the winning row

Vertical plan (y, top to bottom):
    6.35  heading
    5.65  the two facts, side by side
    4.85  the column headings
    4.52  the rule under the headings
    4.15  first row, then every 0.52 downwards
        4.15  r = 1
        3.63  r = 2
        3.11  r = 3
        2.59  the vertical dots
        2.07  r = 9
        1.55  r = 10   <- the winning row
        1.03  r = 11
    0.35  closing note

Run with:  python figures/fig_05_two_letters_need_two_facts.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"          # the first fact, and everything it allows
GREEN = "#1E8449"         # the second fact, and the row it picks
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_GREEN = "#E8F5EC"

W, H = 10.60, 6.80
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.55, 6.35, "two letters need two facts",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# the two facts, stated once each, in their own colours
FACTS = (
    (1.70, BLUE, TINT_BLUE, r"fact 1:   $j = r + 6$"),
    (5.95, GREEN, TINT_GREEN, r"fact 2:   $2r + 3j = 68$"),
)
for left, colour, tint, text in FACTS:
    ax.add_patch(FancyBboxPatch((left, 5.65 - 0.32), 3.10, 0.64,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=tint, edgecolor=colour,
                                linewidth=2.2, zorder=3))
    ax.text(left + 1.55, 5.65, text, ha="center", va="center",
            fontsize=15, color=INK, zorder=4)

# the three column headings, and the small print under them
COLS = ((2.55, r"$r$", BLUE), (4.25, r"$j$", BLUE),
        (6.75, r"$2r + 3j$", GREEN))
for xc, head, colour in COLS:
    ax.text(xc, 4.85, head, ha="center", va="center", fontsize=16,
            color=colour)
ax.text(3.40, 4.52, "every pair fact 1 allows", ha="center", va="center",
        fontsize=11.5, color=GREY)
ax.text(6.75, 4.52, "what fact 2 gives", ha="center", va="center",
        fontsize=11.5, color=GREY)

ax.plot([1.70, 8.60], [4.30, 4.30], linewidth=1.6, color=GREY)

# the rows: r, j = r + 6, and 2r + 3j worked out. only one reaches 68
ROWS = ((4.15, 1, 7, 23), (3.63, 2, 8, 28), (3.11, 3, 9, 33),
        (2.07, 9, 15, 63), (1.55, 10, 16, 68), (1.03, 11, 17, 73))
for ypos, r_value, j_value, total in ROWS:
    winner = total == 68
    if winner:
        # the answer gets a band behind it, so it is found by eye
        ax.add_patch(FancyBboxPatch((1.80, ypos - 0.24), 6.70, 0.48,
                                    boxstyle="round,pad=0.03,"
                                             "rounding_size=0.10",
                                    facecolor=TINT_GREEN, edgecolor=GREEN,
                                    linewidth=2.0, zorder=2))
    colour = GREEN if winner else GREY
    weight = "bold" if winner else "normal"
    ax.text(2.55, ypos, str(r_value), ha="center", va="center",
            fontsize=14.5, color=colour, fontweight=weight, zorder=4)
    ax.text(4.25, ypos, str(j_value), ha="center", va="center",
            fontsize=14.5, color=colour, fontweight=weight, zorder=4)
    ax.text(6.75, ypos, str(total), ha="center", va="center",
            fontsize=14.5, color=colour, fontweight=weight, zorder=4)

# the gap in the middle of the list, so nobody thinks it stops at three
for ydot in (2.72, 2.59, 2.46):
    ax.plot([2.55], [ydot], marker="o", markersize=2.6, color=GREY)
    ax.plot([4.25], [ydot], marker="o", markersize=2.6, color=GREY)
    ax.plot([6.75], [ydot], marker="o", markersize=2.6, color=GREY)

ax.text(8.95, 1.55, "only this row\nobeys both facts", ha="left",
        va="center", fontsize=12.5, color=GREEN, linespacing=1.5)

ax.text(0.55, 0.35, "the first fact ties the two letters together. it "
        "does not say which pair. that is the second fact's job",
        ha="left", va="center", fontsize=13.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_05_two_letters_need_two_facts.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_05_two_letters_need_two_facts.png")
