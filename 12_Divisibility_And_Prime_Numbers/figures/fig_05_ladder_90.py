"""Figure 5 - the ladder method for 90.

The ladder is the second way of breaking a number into primes, and it is
the one the reader will use for a large number, because it never asks for
a factor pair to be guessed. Like the tree, it is a layout, so the picture
has to show where each number is written.

Layout: the primes you divide by run down the left of a vertical rule, and
the number that is left runs down the right. Each row sits under a short
horizontal rule, which is the line the reader draws after each division.
The last row holds a 1, and a green band says that this is the signal to
stop. The left-hand column is then read downwards to give the answer.
Run with:  python figures/fig_05_ladder_90.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

GREEN = "#1E8449"            # the primes you divide by, and the finish
BLUE = "#2E86DE"             # the number that is still being broken up
GREY = "#78909C"
PURPLE = "#8E44AD"           # the exponent form, as in Chapter 10
INK = "#212121"

# (prime you divide by, the number standing on that row)
ROWS = [(2, 90), (3, 45), (3, 15), (5, 5), (None, 1)]

W, H = 10.20, 7.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

XLINE = 4.85                               # the vertical rule of the ladder
XDIV = XLINE - 0.55                        # where a divisor is written
XNUM = XLINE + 0.62                        # where the running number is written
RH = 0.86                                  # height of one row
TOP = H - 1.40                             # top of the first row

# the vertical rule, down as far as the last division
ax.plot([XLINE, XLINE], [TOP - (len(ROWS) - 1) * RH, TOP],
        linewidth=2.0, color=GREY)

for i, (prime, number) in enumerate(ROWS):
    y = TOP - i * RH                       # top edge of this row
    cy = y - RH / 2                        # middle of this row
    # the number that is left on this row
    is_last = number == 1
    ax.text(XNUM, cy, str(number), ha="center", va="center",
            fontsize=26, color=GREEN if is_last else BLUE, fontweight="bold")
    if prime is not None:
        ax.text(XDIV, cy, str(prime), ha="center", va="center",
                fontsize=26, color=GREEN, fontweight="bold")
        # the line the reader draws under the row after dividing
        ax.plot([XLINE, XNUM + 0.70], [y - RH, y - RH],
                linewidth=1.6, color=GREY)
        # what the row says, in words, on the right
        ax.text(XNUM + 1.10, cy, rf"${number} \div {prime} = {number // prime}$",
                ha="left", va="center", fontsize=15, color=GREY)

# ------------------------------------------------- the two column headings
ax.text(XDIV, TOP + 0.30, "divide by", ha="center", va="center",
        fontsize=12.5, color=GREEN)
ax.text(XDIV, TOP + 0.02, "a prime", ha="center", va="center",
        fontsize=12.5, color=GREEN)
ax.text(XNUM, TOP + 0.30, "what is", ha="center", va="center",
        fontsize=12.5, color=BLUE)
ax.text(XNUM, TOP + 0.02, "left", ha="center", va="center",
        fontsize=12.5, color=BLUE)

# --------------------------------------- the arrow that says "read this column"
bottom = TOP - (len(ROWS) - 1) * RH - RH / 2
ax.add_patch(FancyArrowPatch((XDIV - 0.95, TOP - 0.20), (XDIV - 0.95, bottom + 0.20),
                             arrowstyle="-|>", mutation_scale=18,
                             linewidth=1.7, color=GREEN))
ax.text(XDIV - 1.15, (TOP + bottom) / 2, "read this column\nwhen you finish",
        ha="right", va="center", fontsize=12.5, color=GREEN)

# ------------------------------------------------------ the "stop here" note
ax.text(XNUM + 1.10, bottom, "a 1 is left, so there is\nnothing more to divide",
        ha="left", va="center", fontsize=13, color=GREEN)

# ------------------------------------------------------------- the answer
ax.plot([0.90, W - 0.90], [1.42, 1.42], linewidth=1.3, color="#D8DEE1")
ax.text(W / 2, 1.02, r"$90 = 2 \times 3 \times 3 \times 5$",
        ha="center", va="center", fontsize=22, color=INK)
ax.text(W / 2, 0.44, r"$90 = 2 \times 3^{2} \times 5$",
        ha="center", va="center", fontsize=25, color=PURPLE)

ax.text(W / 2, H - 0.36, "The ladder method for 90",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_ladder_90.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
