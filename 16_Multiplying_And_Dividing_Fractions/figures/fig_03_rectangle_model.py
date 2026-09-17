"""Figure 3 - the rectangle that proves top times top over bottom times bottom.

Three copies of the same square. The square is one whole.

Panel 1: three vertical cuts' worth of columns, two of them blue. That is
2/3 of the square.
Panel 2: the same square cut into two rows, one of them orange. That is 1/2
of the square.
Panel 3: both sets of cuts at once. Now the square holds 3 x 2 = 6 equal
cells, and the piece that is blue AND orange is 2 x 1 = 2 of them.

That is the whole rule, and it is a proof rather than an illustration: the
bottom numbers multiply because the two sets of cuts cross, and the top
numbers multiply because the kept columns cross the kept rows.

The x and y scales are equal (the axes span exactly the figure size in
inches), so a square really is square and the areas can be trusted.

Colours: blue is the first fraction, orange the second, green the overlap,
which is the answer.

Run with:  python figures/fig_03_rectangle_model.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"             # the first fraction, 2/3
ORANGE = "#E67E22"           # the second fraction, 1/2
GREEN = "#1E8449"            # the overlap, which is the answer
GREY = "#78909C"
INK = "#212121"

TINT = {BLUE: "#CFE2F8", ORANGE: "#FBDDBC", GREEN: "#BFE3CA"}

COLS, ROWS = 3, 2            # 3 columns for thirds, 2 rows for halves
SQ = 2.70                    # the side of the whole square
CW = SQ / COLS               # width of one column
RH = SQ / ROWS               # height of one row

W, H = 13.60, 7.70
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

SQ_Y = 2.85                  # bottom edge of every square
GAP = 1.70                   # room for the x and = signs between the squares
LEFT = (W - 3 * SQ - 2 * GAP) / 2

P1 = LEFT
P2 = LEFT + SQ + GAP
P3 = LEFT + 2 * (SQ + GAP)


def outline(px):
    """The black edge of the whole square - this is the one whole."""
    ax.add_patch(Rectangle((px, SQ_Y), SQ, SQ, facecolor="none",
                           edgecolor=INK, linewidth=2.0, zorder=6))


def column_cuts(px, colour=GREY, width=1.2):
    """The two vertical lines that make three columns."""
    for i in range(1, COLS):
        x = px + i * CW
        ax.plot([x, x], [SQ_Y, SQ_Y + SQ], color=colour, linewidth=width,
                zorder=5)


def row_cuts(px, colour=GREY, width=1.2):
    """The one horizontal line that makes two rows."""
    for j in range(1, ROWS):
        y = SQ_Y + j * RH
        ax.plot([px, px + SQ], [y, y], color=colour, linewidth=width, zorder=5)


def heading(px, title, under, colour):
    """The bold line above a square and the quiet line under that."""
    ax.text(px + SQ / 2, SQ_Y + SQ + 0.78, title, ha="center", va="center",
            fontsize=15, color=colour, fontweight="bold")
    ax.text(px + SQ / 2, SQ_Y + SQ + 0.38, under, ha="center", va="center",
            fontsize=12.5, color=GREY)


def footing(px, maths, words, colour):
    """The fraction under a square, and the sentence under that."""
    ax.text(px + SQ / 2, SQ_Y - 0.58, maths, ha="center", va="center",
            fontsize=21, color=colour)
    ax.text(px + SQ / 2, SQ_Y - 1.18, words, ha="center", va="center",
            fontsize=12.5, color=GREY)


def sign(px, text):
    """The x or = that sits between two squares."""
    ax.text(px, SQ_Y + SQ / 2, text, ha="center", va="center",
            fontsize=32, color=INK)


# ------------------------------------------------ panel 1: two columns of three
ax.add_patch(Rectangle((P1, SQ_Y), 2 * CW, SQ, facecolor=TINT[BLUE],
                       edgecolor="none", zorder=2))
column_cuts(P1)
outline(P1)
heading(P1, "two columns of three", "cut from top to bottom", BLUE)
footing(P1, r"$\frac{2}{3}$", "of the square is blue", BLUE)

sign(P1 + SQ + GAP / 2, r"$\times$")

# ---------------------------------------------------- panel 2: one row of two
ax.add_patch(Rectangle((P2, SQ_Y + RH), SQ, RH, facecolor=TINT[ORANGE],
                       edgecolor="none", zorder=2))
row_cuts(P2)
outline(P2)
heading(P2, "one row of two", "cut from side to side", ORANGE)
footing(P2, r"$\frac{1}{2}$", "of the square is orange", ORANGE)

sign(P2 + SQ + GAP / 2, "=")

# ------------------------------------------- panel 3: both sets of cuts at once
# the blue columns and the orange row first, so the overlap can go on top
ax.add_patch(Rectangle((P3, SQ_Y), 2 * CW, SQ, facecolor=TINT[BLUE],
                       edgecolor="none", zorder=2))
ax.add_patch(Rectangle((P3, SQ_Y + RH), SQ, RH, facecolor=TINT[ORANGE],
                       edgecolor="none", alpha=0.75, zorder=3))
# the two cells that are blue AND orange
ax.add_patch(Rectangle((P3, SQ_Y + RH), 2 * CW, RH, facecolor=TINT[GREEN],
                       edgecolor=GREEN, linewidth=2.4, zorder=4))
column_cuts(P3)
row_cuts(P3)
outline(P3)
heading(P3, "both cuts together", "the square now holds $6$ equal cells", GREEN)
footing(P3, r"$\frac{2}{6} = \frac{1}{3}$",
        "$2$ cells are blue and orange at once", GREEN)

# the arithmetic that the third panel is a picture of
ax.text(W / 2, 1.00,
        r"$\frac{2}{3} \times \frac{1}{2}"
        r" = \frac{2 \times 1}{3 \times 2} = \frac{2}{6} = \frac{1}{3}$",
        ha="center", va="center", fontsize=22, color=INK)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.42,
        "Two sets of cuts cross, and that is why the numbers multiply",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.84,
        "$3$ columns crossed by $2$ rows make $3 \\times 2 = 6$ cells; "
        "$2$ kept columns crossed by $1$ kept row make $2 \\times 1 = 2$ cells",
        ha="center", va="center", fontsize=13, color=GREY)

# ------------------------------------------------------------- the bottom line
ax.text(W / 2, 0.34,
        "the bottom numbers multiply because the cuts cross; the top numbers "
        "multiply for exactly the same reason",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_03_rectangle_model.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
