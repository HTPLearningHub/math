"""Figure 6 - borrowing when the column next door is a zero (5042 - 2678).

The ones column has already borrowed, so the number now sits as
5 thousands, 0 hundreds, 3 tens, 12 ones. The tens column needs a hundred, but
the hundreds column is empty, so the trade has to be done in two steps:
first a thousand becomes ten hundreds, then one of those hundreds becomes
ten tens.

Each row of the table is the whole number re-packed. Cells that changed since
the row above are orange, the colour this book uses for the piece that moves.
No arrows are drawn between cells: the rows are close together and any arrow
would have to cross a digit.

Run with:  python figures/fig_06_borrowing_across_a_zero.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # a value that did not change in this step
BLUE_FILL = "#EAF2FB"
ORANGE = "#E67E22"      # a value that changed in this step
ORANGE_FILL = "#FDF0E3"
GREY = "#78909C"        # the empty column
GREY_FILL = "#ECEFF1"
INK = "#212121"

W, H = 13.0, 5.8
Y_BOTTOM = 0.40

HEADERS = ["Thousands", "Hundreds", "Tens", "Ones"]
COL_W, CELL_H = 1.55, 0.80
X0 = 1.00                           # left edge of the table

# one entry per row: the four values, which of them are new, the explanation
ROWS = [
    (["5", "0", "3", "12"], set(),
     "The ones column has already borrowed:\n"
     r"$4$ tens became $3$ tens and $2$ ones became $12$." "\n"
     "Now the tens column needs a hundred,\n"
     "but the hundreds column is empty."),
    (["4", "10", "3", "12"], {0, 1},
     "So go one place further left.\n"
     r"Take $1$ thousand and change it" "\n"
     r"into $10$ hundreds."),
    (["4", "9", "13", "12"], {1, 2},
     r"Now take $1$ of those hundreds" "\n"
     r"and change it into $10$ tens." "\n"
     r"The tens column has $13$, and $13 - 7$ can be done."),
]

fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(Y_BOTTOM, Y_BOTTOM + H)

ax.text(W / 2, 5.90, r"$5042$ re-packed in two steps, so that the tens can borrow",
        ha="center", va="center", fontsize=17, fontweight="bold", color=INK)

# the column headers
for c, name in enumerate(HEADERS):
    ax.text(X0 + (c + 0.5) * COL_W, 5.12, name, ha="center", va="center",
            fontsize=12.5, fontweight="bold", color=INK)

for r, (values, changed, note) in enumerate(ROWS):
    y = 4.35 - r * 1.20             # centre line of this row of cells
    for c, value in enumerate(values):
        x = X0 + c * COL_W
        if c in changed:
            edge, fill = ORANGE, ORANGE_FILL
        elif value == "0":
            edge, fill = GREY, GREY_FILL
        else:
            edge, fill = BLUE, BLUE_FILL
        ax.add_patch(FancyBboxPatch((x + 0.06, y - CELL_H / 2), COL_W - 0.12, CELL_H,
                                    boxstyle="round,pad=0.01,rounding_size=0.08",
                                    facecolor=fill, edgecolor=edge, linewidth=2.0))
        ax.text(x + COL_W / 2, y, value, ha="center", va="center",
                fontsize=22, color=edge, fontweight="bold")
    # the sentence that explains this row
    ax.text(7.75, y, note, ha="left", va="center", fontsize=12, color=INK)

# say the empty column out loud, under the grey cell
ax.text(X0 + 1.5 * COL_W, 4.35 - CELL_H / 2 - 0.08, "empty",
        ha="center", va="top", fontsize=10.5, color=GREY, fontweight="bold")

ax.text(W / 2, 1.00, r"$4000 + 900 + 130 + 12 = 5042$",
        ha="center", va="center", fontsize=15, color=INK)
ax.text(W / 2, 0.60, "Every row is the same number. Only the packing changed.",
        ha="center", va="center", fontsize=13, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_borrowing_across_a_zero.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
