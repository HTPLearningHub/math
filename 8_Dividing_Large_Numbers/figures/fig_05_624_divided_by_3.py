"""Figure 5 - the finished tableau for 624 divided by 3, coloured by step.

The left half is the piece of paper: exactly what the reader writes, nothing
added. The right half names the three turns of the loop and, inside each turn,
the four steps in order.

Every written thing carries the colour of the step that produced it, using the
same four colours as figure 4: blue for a quotient digit (Divide), orange for a
product (Multiply), purple for a difference (Subtract), green for a digit that
has just been brought down (Bring down). Read the colours down the page and you
are reading the loop going round.

The axes fills the whole figure, so one unit on the axes is exactly one inch.
Digits are set in DejaVu Sans and placed by hand, column by column; the
mono-spaced zero is avoided because it is drawn with a dot inside it.
Run with:  python figures/fig_05_624_divided_by_3.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # Divide   - a digit of the quotient
ORANGE = "#E67E22"      # Multiply - a product written underneath
PURPLE = "#8E44AD"      # Subtract - what is left after taking the product away
GREEN = "#1E8449"       # Bring down - a digit fetched from the dividend
GREY = "#78909C"
INK = "#212121"
FONT = "DejaVu Sans"    # a plain, unmarked zero

W, H = 11.4, 7.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

FS = 30                             # font size of every digit in the tableau
C = [2.62, 3.22, 3.82]              # x centre of the hundreds / tens / ones column
X_BAR, X_END = 1.88, 4.18           # the vertical and horizontal lines of the bracket
HALF = 0.28                         # half the width of one column, for the rules


def digit(col, y, ch, colour):
    """Write one digit in the given column of the tableau."""
    ax.text(C[col], y, ch, ha="center", va="center",
            fontsize=FS, family=FONT, color=colour)


def minus(col, y):
    """Write the subtraction sign to the left of the given column."""
    ax.text(C[col] - 0.44, y, r"$-$", ha="center", va="center",
            fontsize=FS - 4, color=INK)


def rule(col_from, col_to, y):
    """Draw the short line under the numbers that are being subtracted."""
    ax.plot([C[col_from] - HALF, C[col_to] + HALF], [y, y],
            color=INK, linewidth=1.8)


# ---- the bracket, the divisor, the dividend and the quotient ----------------
ax.plot([X_BAR, X_END], [6.48, 6.48], color=INK, linewidth=2.4)
ax.plot([X_BAR, X_BAR], [6.48, 1.88], color=INK, linewidth=2.4)
ax.text(1.54, 6.02, "3", ha="center", va="center",
        fontsize=FS, family=FONT, color=INK)
for col, ch in enumerate("624"):
    digit(col, 6.02, ch, INK)
for col, ch in enumerate("208"):
    ax.text(C[col], 6.90, ch, ha="center", va="center",
            fontsize=FS, family=FONT, color=BLUE, fontweight="bold")

# ---- turn 1: the hundreds ---------------------------------------------------
minus(0, 5.40); digit(0, 5.40, "6", ORANGE)         # 2 x 3 = 6
rule(0, 0, 5.10)
digit(0, 4.72, "0", PURPLE)                         # 6 - 6 = 0
digit(1, 4.72, "2", GREEN)                          # bring the 2 down

# ---- turn 2: the tens -------------------------------------------------------
minus(1, 4.10); digit(1, 4.10, "0", ORANGE)         # 0 x 3 = 0
rule(1, 1, 3.80)
digit(1, 3.42, "2", PURPLE)                         # 2 - 0 = 2
digit(2, 3.42, "4", GREEN)                          # bring the 4 down

# ---- turn 3: the ones -------------------------------------------------------
minus(1, 2.80); digit(1, 2.80, "2", ORANGE); digit(2, 2.80, "4", ORANGE)
rule(1, 2, 2.50)
digit(2, 2.12, "0", PURPLE)                         # 24 - 24 = 0, nothing left
# the label sits directly under the last digit, clear of the commentary column
ax.text(C[2], 1.62, "nothing left over", ha="center", va="center",
        fontsize=12.5, color=PURPLE, fontweight="bold")

# ---- the running commentary, one block per turn of the loop -----------------
TX = 5.30                           # where every line of commentary starts


def turn(top, heading, lines):
    """Write the heading of one turn of the loop and its four steps."""
    ax.text(TX, top, heading, ha="left", va="center",
            fontsize=15.5, color=INK, fontweight="bold")
    ax.plot([TX, TX + 5.55], [top - 0.20, top - 0.20], color=GREY, linewidth=1.0)
    for i, (text, colour) in enumerate(lines):
        ax.text(TX + 0.10, top - 0.52 - i * 0.34, text, ha="left", va="center",
                fontsize=13.5, color=colour)


turn(7.05, "Turn 1 - the hundreds", [
    (r"Divide:  $3$ fits into $6$ exactly $2$ times", BLUE),
    (r"Multiply:  $2 \times 3 = 6$", ORANGE),
    (r"Subtract:  $6 - 6 = 0$", PURPLE),
    (r"Bring down:  the $2$", GREEN)])

turn(4.95, "Turn 2 - the tens", [
    (r"Divide:  $3$ does not fit into $2$, so write $0$", BLUE),
    (r"Multiply:  $0 \times 3 = 0$", ORANGE),
    (r"Subtract:  $2 - 0 = 2$", PURPLE),
    (r"Bring down:  the $4$, making $24$", GREEN)])

turn(2.85, "Turn 3 - the ones", [
    (r"Divide:  $3$ fits into $24$ exactly $8$ times", BLUE),
    (r"Multiply:  $8 \times 3 = 24$", ORANGE),
    (r"Subtract:  $24 - 24 = 0$", PURPLE),
    ("Nothing left to bring down. Finished.", INK)])

# ---- the answer -------------------------------------------------------------
ax.text(W / 2, 0.52, r"$624 \div 3 = 208$", ha="center", va="center",
        fontsize=22, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_624_divided_by_3.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
