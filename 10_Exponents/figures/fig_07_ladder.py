"""Figure 7 - the ladder of powers of two, walked downwards past zero.

Going up the ladder doubles. So going down the ladder halves, and it can
carry on halving for ever. Follow it down and it walks through 2^0 = 1 and
straight on into the negative exponents without anything unusual happening.

This is the picture behind both the zero rule and the negative rule. The
chapter uses it twice: once in section 6 for 2^0 = 1, and again in section 7
for the rows below it.

Two layout traps, both hit on the first attempt: the dashed rule must stop
before the column of "half it" arrows or it strikes straight through one of
them, and the shaded panel must end well above the closing sentence.
Run with:  python figures/fig_07_ladder.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path
from fractions import Fraction

BLUE = "#2E86DE"        # a positive exponent
ORANGE = "#E67E22"      # a negative exponent
GREY = "#78909C"        # the exponent zero, and quiet labels
INK = "#212121"

W, H = 9.90, 6.75
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ROWS = [4, 3, 2, 1, 0, -1, -2, -3]         # the exponent, one less each row
TOP, STEP = 5.60, 0.62                     # the first row, and the gap between rows
X_TERM, X_EQ, X_VAL = 3.55, 4.15, 4.60     # the three columns of the table
X_ARROW = 6.05                             # the column of "half it" arrows
X_NOTE = 7.30                              # the column of side notes


def y_of(k):
    """The height of row number k, counting from zero at the top."""
    return TOP - k * STEP


def written(e):
    """The value of 2 to the power e, as a LaTeX string: whole, or a fraction."""
    v = Fraction(2) ** e
    return rf"${v}$" if v.denominator == 1 else rf"$\frac{{1}}{{{v.denominator}}}$"


# the line between the exponents the reader already understands and the new ones,
# which is also the top edge of the shaded panel below it
y_split = (y_of(4) + y_of(5)) / 2

# a pale panel behind the rows whose exponent is below zero
ax.add_patch(FancyBboxPatch((2.60, y_of(7) - 0.31), 3.00, y_split - y_of(7) + 0.31,
                            boxstyle="round,pad=0.03,rounding_size=0.12",
                            facecolor="#FDF0E3", edgecolor="none"))

for k, e in enumerate(ROWS):
    y = y_of(k)
    colour = GREY if e == 0 else (BLUE if e > 0 else ORANGE)
    ax.text(X_TERM, y, rf"$2^{{{e}}}$", ha="right", va="center",
            fontsize=21, color=colour, fontweight="bold")
    ax.text(X_EQ, y, r"$=$", ha="center", va="center", fontsize=19, color=INK)
    ax.text(X_VAL, y, written(e), ha="left", va="center",
            fontsize=21, color=colour, fontweight="bold")

    # the step from this value to the next one down, drawn between the two rows
    if k < len(ROWS) - 1:
        ax.annotate("", xy=(X_ARROW, y - STEP + 0.20), xytext=(X_ARROW, y - 0.20),
                    arrowprops=dict(arrowstyle="-|>", color=GREY, linewidth=1.6,
                                    mutation_scale=13))
        ax.text(X_ARROW + 0.21, y - STEP / 2, "half it", ha="left", va="center",
                fontsize=12.5, color=GREY)

ax.plot([2.45, 5.75], [y_split] * 2, color=INK, linewidth=1.4,
        linestyle=(0, (6, 4)))

# the remarks the rows on either side of the split are there to earn
ax.text(2.40, y_of(4), r"$2^{0}$ is not nothing.", ha="right", va="center",
        fontsize=14, color=INK, fontweight="bold")
ax.text(X_NOTE, y_of(1), "every step down\nhalves the value",
        ha="left", va="center", fontsize=13, color=BLUE, linespacing=1.5)
ax.text(X_NOTE, y_of(6), "and it just keeps\non halving",
        ha="left", va="center", fontsize=13, color=ORANGE, linespacing=1.5)

ax.text(W / 2, H - 0.32, "Walk down the ladder and nothing special happens at zero",
        ha="center", va="center", fontsize=17, color=INK, fontweight="bold")
ax.text(W / 2, 0.40,
        r"Halving $1$ gives $\frac{1}{2}$, so $2^{-1}$ has to be $\frac{1}{2}$.",
        ha="center", va="center", fontsize=16, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_07_ladder.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
