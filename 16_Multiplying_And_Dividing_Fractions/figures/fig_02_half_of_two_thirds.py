"""Figure 2 - "half OF two thirds" is a picture before it is a sum.

Three bars of the same length, one under the other.

Row 1: the bar cut into thirds with two shaded blue. That is 2/3.
Row 2: the same two thirds, with an orange line down the middle of the
shaded stretch. The left half is kept (orange); the right half is given away
(pale, dashed). That is half OF it.
Row 3: the bar cut into thirds again with one shaded green - and the orange
region of row 2 ends at exactly the same place.

The point of the figure is that nobody has to be told the answer. The orange
region and the green region end at the same x, so 1/2 of 2/3 is 1/3, and the
reader saw it rather than being told it.

Every cut line is drawn *after* the shading and with a higher zorder, so the
reader can always count the pieces. In the first version the shading covered
the middle cut of row 1 and the bar stopped looking like thirds.

Colours: blue is the fraction we start with, orange is the second fraction
doing its work, green is the answer.

Run with:  python figures/fig_02_half_of_two_thirds.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"             # the fraction we take a part of
ORANGE = "#E67E22"           # the part we take
GREEN = "#1E8449"            # the answer
GREY = "#78909C"
INK = "#212121"

TINT = {BLUE: "#E9F2FC", ORANGE: "#FDF0E3", GREEN: "#E8F5EC"}

W, H = 11.40, 7.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BAR_X = 2.65                 # left edge of every bar
BAR_W = 5.90                 # all three bars are this long
BAR_H = 0.86

ROW1, ROW2, ROW3 = 5.05, 3.45, 1.60

THIRD = BAR_W / 3
TWO_THIRDS_END = BAR_X + 2 * THIRD      # where 2/3 of the bar ends
HALF_OF_IT = BAR_X + THIRD              # halfway along that shaded stretch


def shade(y, x_from, x_to, colour, dashed=False):
    """Fill one stretch of a bar between two x values."""
    ax.add_patch(Rectangle((x_from, y), x_to - x_from, BAR_H,
                           facecolor=TINT[colour], edgecolor=colour,
                           linewidth=1.6 if dashed else 2.0,
                           linestyle=(0, (4, 3)) if dashed else "solid",
                           alpha=0.45 if dashed else 1.0, zorder=2))


def frame(y, pieces):
    """Draw the cut lines and the outline, on top of whatever was shaded."""
    piece_w = BAR_W / pieces
    for i in range(1, pieces):
        x = BAR_X + i * piece_w
        ax.plot([x, x], [y, y + BAR_H], color=GREY, linewidth=1.2, zorder=4)
    ax.add_patch(Rectangle((BAR_X, y), BAR_W, BAR_H, facecolor="none",
                           edgecolor=INK, linewidth=1.6, zorder=5))


def label(y, text, colour, size=25):
    """The big fraction that names the row, to the left of the bar."""
    ax.text(BAR_X - 1.05, y + BAR_H / 2, text, ha="center", va="center",
            fontsize=size, color=colour)


def note(y, text, colour, dy=0.0):
    """The quiet sentence to the right of the bar."""
    ax.text(BAR_X + BAR_W + 0.30, y + BAR_H / 2 + dy, text, ha="left",
            va="center", fontsize=13, color=colour)


# ------------------------------------------------- row 1: the two thirds we own
shade(ROW1, BAR_X, TWO_THIRDS_END, BLUE)
frame(ROW1, 3)
label(ROW1, r"$\frac{2}{3}$", BLUE)
note(ROW1, "we start with two thirds", GREY)

# ------------------------------------- row 2: that stretch, cut down the middle
shade(ROW2, BAR_X, HALF_OF_IT, ORANGE)                 # the half we keep
shade(ROW2, HALF_OF_IT, TWO_THIRDS_END, BLUE, True)    # the half we give away
frame(ROW2, 3)
# the orange cut itself - the one new line in the whole figure
ax.plot([HALF_OF_IT, HALF_OF_IT], [ROW2 - 0.24, ROW2 + BAR_H + 0.24],
        color=ORANGE, linewidth=2.8, zorder=6)
ax.text(HALF_OF_IT, ROW2 + BAR_H + 0.44, "cut the blue stretch in two here",
        ha="center", va="center", fontsize=12.5, color=ORANGE)
label(ROW2, r"$\frac{1}{2}$ of it", ORANGE, size=22)
note(ROW2, "keep the orange half,", ORANGE, dy=0.18)
note(ROW2, "give the pale half away", GREY, dy=-0.22)

# -------------------------------------------------- row 3: the answer, in thirds
shade(ROW3, BAR_X, BAR_X + THIRD, GREEN)
frame(ROW3, 3)
label(ROW3, r"$\frac{1}{3}$", GREEN)
note(ROW3, "which is exactly one third", GREEN)

# the dashed green line: the kept half and one third end at the same place
ax.plot([HALF_OF_IT, HALF_OF_IT], [ROW3, ROW2], color=GREEN, linewidth=1.6,
        linestyle=(0, (3, 3)), zorder=6)
ax.text(HALF_OF_IT + 0.14, (ROW3 + ROW2 + BAR_H) / 2 - 0.10,
        "the same edge", ha="left", va="center", fontsize=12.5, color=GREEN,
        zorder=7, bbox=dict(facecolor="white", edgecolor="none", pad=2.5))

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.42, 'The word "of" is the word "times"',
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.84,
        "every bar is the same length, and every bar is cut into the same "
        "three parts",
        ha="center", va="center", fontsize=13, color=GREY)

# ------------------------------------------------------------- the bottom line
ax.text(W / 2, 0.72,
        r"$\frac{1}{2}$ of $\frac{2}{3}$  $=$  "
        r"$\frac{1}{2} \times \frac{2}{3}$  $=$  $\frac{1}{3}$",
        ha="center", va="center", fontsize=19, color=INK)
ax.text(W / 2, 0.24,
        "multiplying by a number smaller than one leaves you with less than "
        "you had",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_02_half_of_two_thirds.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
