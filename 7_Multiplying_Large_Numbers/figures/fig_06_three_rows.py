"""Figure 6 - a three-digit multiplier: 213 x 124, and its three rows.

Every digit of the bottom number makes one row, and each row is pushed one
place further to the left than the row above it. That push is written as zeros
on the right-hand end: none for the ones digit, one for the tens digit, two
for the hundreds digit.

Each row is drawn in the colour of the digit that produced it - blue for ones,
orange for tens, purple for hundreds - and the place-holding zeros are bold,
so the staircase they build is the first thing the eye sees.

Purple is the book's third-part colour, introduced in Chapter 6 figure 6 for a
three-way split. This is a three-way split too, so it is the same colour.

The axes fills the whole figure, so one unit on the axes is exactly one inch,
and single mono-spaced characters can be placed by hand: at font size FS a
DejaVu Sans Mono character is FS/72 * 0.602 inches wide.
Run with:  python figures/fig_06_three_rows.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # the ones digit of 124, and the row it makes
ORANGE = "#E67E22"      # the tens digit, and its row
PURPLE = "#8E44AD"      # the hundreds digit, and its row
GREY = "#78909C"
INK = "#212121"
MONO = "DejaVu Sans Mono"

W, H = 11.90, 5.60      # figure size in inches = size of the axes in units
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

FS = 30                             # font size of the digits
CH = FS / 72 * 0.602                # width of one mono character, in units
XR = 3.30                           # right end of every row of digits
LX = 4.10                           # where the sentence beside a row starts
ZX = 7.75                           # where the "how many zeros" note starts

ax.add_patch(FancyBboxPatch((0.35, 0.30), 11.20, 4.95,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor="#FAFAFA", edgecolor=GREY, linewidth=1.8))


def row(y, text, colour=INK, bold_tail=0):
    """Write a row of digits right aligned at XR.

    The last `bold_tail` characters are the place-holding zeros, so they are
    drawn bold. Every character is placed on its own column, which is why no
    glyph ever has to be printed on top of another one.
    """
    for i, char in enumerate(reversed(text)):
        ax.text(XR - (i + 0.5) * CH, y, char, ha="center", va="center",
                fontsize=FS, family=MONO, color=colour,
                fontweight="bold" if i < bold_tail else "normal", zorder=3)


# ---- the two numbers being multiplied ---------------------------------------
row(4.72, "213")
for char, n, colour in [("1", 2.5, PURPLE), ("2", 1.5, ORANGE), ("4", 0.5, BLUE)]:
    ax.text(XR - n * CH, 4.10, char, ha="center", va="center", fontsize=FS,
            family=MONO, color=colour, fontweight="bold", zorder=3)
ax.text(XR - 4.2 * CH, 4.10, r"$\times$", ha="right", va="center",
        fontsize=FS - 5, color=INK)
ax.plot([XR - 5.2 * CH, XR + 0.08], [3.72, 3.72], color=INK, linewidth=2.2)

# ---- the three partial products ---------------------------------------------
ROWS = [
    (3.24, "852", BLUE, 0, r"$213 \times 4 = 852$", "no zeros"),
    (2.56, "4260", ORANGE, 1, r"$213 \times 20 = 4260$", "one zero"),
    (1.88, "21300", PURPLE, 2, r"$213 \times 100 = 21300$", "two zeros"),
]
for y, text, colour, tail, formula, zeros in ROWS:
    row(y, text, colour, tail)
    ax.text(LX, y, formula, ha="left", va="center",
            fontsize=15, color=colour, fontweight="bold")
    ax.text(ZX, y, zeros, ha="left", va="center",
            fontsize=15, color=colour, fontweight="bold")
ax.text(XR - 5.6 * CH, 1.88, "+", ha="right", va="center",
        fontsize=FS - 5, family=MONO, color=INK)

# ---- the sum of the three rows ----------------------------------------------
ax.plot([XR - 5.6 * CH, XR + 0.08], [1.50, 1.50], color=INK, linewidth=2.2)
row(1.04, "26412")
ax.text(LX, 1.04, r"$852 + 4260 + 21300 = 26412$", ha="left", va="center",
        fontsize=15, color=INK, fontweight="bold")

ax.text(5.95, 0.58, "three digits in the bottom number, so three rows"
                    " - and each one steps one place further left",
        ha="center", va="center", fontsize=13, color=GREY, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_three_rows.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
