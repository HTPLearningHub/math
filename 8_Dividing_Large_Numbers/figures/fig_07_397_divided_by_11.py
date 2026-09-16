"""Figure 7 - a two-digit divisor: 397 divided by 11.

Two things are new here and both are in the picture.

First, 11 does not fit into the single digit 3, so the first working number is
the first TWO digits, 39. The dashed blue box marks them. The quotient digit
that comes out of that step is written above the SECOND of the two digits, the
9, which is why the answer has two digits and not three.

Second, nobody knows the eleven times table by heart the way they know the
threes. The strip along the bottom is the fix: count up in elevens until you
pass the working number, and the last one you did not pass is the digit you
want. 33 and 66 are the two the division actually uses.

Step colours are the same four as figure 4.
Run with:  python figures/fig_07_397_divided_by_11.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # Divide   - a digit of the quotient
ORANGE = "#E67E22"      # Multiply - a product written underneath
PURPLE = "#8E44AD"      # Subtract - what is left after taking the product away
GREEN = "#1E8449"       # Bring down - a digit fetched from the dividend
GREY = "#78909C"
INK = "#212121"
FONT = "DejaVu Sans"    # a plain, unmarked zero

W, H = 11.8, 7.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

FS = 30
C = [2.72, 3.32, 3.92]              # x centre of the hundreds / tens / ones column
X_BAR, X_END = 1.78, 4.28
HALF = 0.28


def digit(col, y, ch, colour):
    ax.text(C[col], y, ch, ha="center", va="center",
            fontsize=FS, family=FONT, color=colour)


def minus(col, y):
    ax.text(C[col] - 0.44, y, r"$-$", ha="center", va="center",
            fontsize=FS - 4, color=INK)


def rule(col_from, col_to, y):
    ax.plot([C[col_from] - HALF, C[col_to] + HALF], [y, y],
            color=INK, linewidth=1.8)


# ---- the bracket, the divisor, the dividend, the quotient -------------------
ax.plot([X_BAR, X_END], [6.28, 6.28], color=INK, linewidth=2.4)
ax.plot([X_BAR, X_BAR], [6.28, 2.98], color=INK, linewidth=2.4)
ax.text(1.28, 5.82, "11", ha="center", va="center",
        fontsize=FS, family=FONT, color=INK)
for col, ch in enumerate("397"):
    digit(col, 5.82, ch, INK)
# the quotient has only two digits: nothing at all is written above the 3
for col, ch in [(1, "3"), (2, "6")]:
    ax.text(C[col], 6.72, ch, ha="center", va="center",
            fontsize=FS, family=FONT, color=BLUE, fontweight="bold")

# the dashed box round the first working number, 39
ax.add_patch(FancyBboxPatch((C[0] - 0.32, 5.82 - 0.34),
                            (C[1] + 0.32) - (C[0] - 0.32), 0.68,
                            boxstyle="round,pad=0.02,rounding_size=0.08",
                            facecolor="none", edgecolor=BLUE,
                            linewidth=1.8, linestyle=(0, (4, 3))))

# ---- turn 1: the first two digits, 39 ---------------------------------------
minus(0, 5.20); digit(0, 5.20, "3", ORANGE); digit(1, 5.20, "3", ORANGE)
rule(0, 1, 4.90)
digit(1, 4.52, "6", PURPLE)
digit(2, 4.52, "7", GREEN)

# ---- turn 2: the ones -------------------------------------------------------
minus(1, 3.90); digit(1, 3.90, "6", ORANGE); digit(2, 3.90, "6", ORANGE)
rule(1, 2, 3.60)
digit(2, 3.22, "1", PURPLE)
ax.text(C[2] + 0.42, 3.22, "remainder", ha="left", va="center",
        fontsize=12.5, color=PURPLE, fontweight="bold")

# ---- the running commentary -------------------------------------------------
TX = 5.55


def turn(top, heading, lines):
    ax.text(TX, top, heading, ha="left", va="center",
            fontsize=15.5, color=INK, fontweight="bold")
    ax.plot([TX, TX + 5.90], [top - 0.20, top - 0.20], color=GREY, linewidth=1.0)
    for i, (text, colour) in enumerate(lines):
        ax.text(TX + 0.10, top - 0.52 - i * 0.34, text, ha="left", va="center",
                fontsize=13.5, color=colour)


turn(7.05, "Turn 1 - the first two digits", [
    (r"Divide:  $11$ does not fit into $3$, so take $39$", BLUE),
    (r"$\qquad\quad\,$ $11$ fits into $39$ three times", BLUE),
    (r"Multiply:  $3 \times 11 = 33$", ORANGE),
    (r"Subtract:  $39 - 33 = 6$", PURPLE),
    (r"Bring down:  the $7$, making $67$", GREEN)])

turn(4.72, "Turn 2 - the ones", [
    (r"Divide:  $11$ fits into $67$ six times", BLUE),
    (r"Multiply:  $6 \times 11 = 66$", ORANGE),
    (r"Subtract:  $67 - 66 = 1$", PURPLE),
    (r"No digits left. The $1$ is the remainder.", INK)])

ax.text(TX, 2.78, "The answer has two digits, not three: nothing goes above "
                  "the $3$.",
        ha="left", va="center", fontsize=13, color=GREY, fontweight="bold")

# ---- the eleven times table, counted up along the bottom --------------------
ax.text(W / 2, 2.14, "How to find each quotient digit: count up in elevens",
        ha="center", va="center", fontsize=14, color=INK, fontweight="bold")

BW, BG = 0.90, 0.12                 # box width and gap
x = W / 2 - (9 * BW + 8 * BG) / 2
for n in range(1, 10):
    used = n in (3, 6)              # 33 and 66 are the two this division needs
    ax.add_patch(FancyBboxPatch((x, 1.06), BW, 0.62,
                                boxstyle="round,pad=0.02,rounding_size=0.10",
                                facecolor="#FDF2E4" if used else "#FAFAFA",
                                edgecolor=ORANGE if used else GREY,
                                linewidth=2.0 if used else 1.2))
    ax.text(x + BW / 2, 1.37, str(11 * n), ha="center", va="center",
            fontsize=16 if used else 14.5,
            color=ORANGE if used else INK,
            fontweight="bold" if used else "normal")
    ax.text(x + BW / 2, 0.80, f"{n}", ha="center", va="center",
            fontsize=11.5, color=ORANGE if used else GREY, fontweight="bold")
    x += BW + BG
ax.text(W / 2 - (9 * BW + 8 * BG) / 2 - 0.12, 0.80, "times:",
        ha="right", va="center", fontsize=11.5, color=GREY, fontweight="bold")

ax.text(W / 2, 0.28, r"$397 \div 11 = 36$ remainder $1$",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_07_397_divided_by_11.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
