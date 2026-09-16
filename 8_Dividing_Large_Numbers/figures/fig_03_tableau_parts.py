"""Figure 3 - the parts of the division bracket, using 624 divided by 3.

Three numbers, three places to write them: the divisor outside on the left,
the dividend inside, and the quotient growing along the top. The place names
are printed as column headings above everything, because the single most
important habit in long division is keeping each quotient digit directly above
the dividend digit it came from.

The labels are attached with arrows that come in from the outside of the
tableau, so no arrow crosses a digit or the bracket itself.

Font note: the digits are set in DejaVu Sans, NOT in a mono-spaced font. The
mono-spaced zero is drawn with a dot inside it, and this whole chapter turns on
the reader seeing a plain, ordinary zero. Each digit is positioned by hand, so
nothing is lost by dropping the mono-spacing.
Run with:  python figures/fig_03_tableau_parts.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # the quotient - the answer being built
GREY = "#78909C"
INK = "#212121"
FONT = "DejaVu Sans"    # a plain, unmarked zero

W, H = 11.6, 5.10
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

FS = 44                              # font size of every digit
COLS = [4.95, 5.73, 6.51]            # x centre of the hundreds / tens / ones column
BAR_Y = 3.62                         # the horizontal line of the bracket
Y_DIV = 3.15                         # the dividend digits sit here
Y_QUO = 4.12                         # the quotient digits sit here
X_BAR = 4.56                         # the vertical line of the bracket
X_END = 6.92                         # right end of the horizontal line

# ---- the bracket itself -----------------------------------------------------
ax.plot([X_BAR, X_END], [BAR_Y, BAR_Y], color=INK, linewidth=2.6)
ax.plot([X_BAR, X_BAR], [BAR_Y, 2.62], color=INK, linewidth=2.6)

# ---- the three numbers ------------------------------------------------------
ax.text(4.22, Y_DIV, "3", ha="center", va="center",
        fontsize=FS, family=FONT, color=INK)
for x, d in zip(COLS, "624"):
    ax.text(x, Y_DIV, d, ha="center", va="center",
            fontsize=FS, family=FONT, color=INK)
for x, d in zip(COLS, "208"):
    ax.text(x, Y_QUO, d, ha="center", va="center",
            fontsize=FS, family=FONT, color=BLUE, fontweight="bold")

# ---- the place names, printed above everything as column headings -----------
for x, place in zip(COLS, ["hundreds", "tens", "ones"]):
    ax.text(x, 4.86, place, ha="center", va="center",
            fontsize=12.5, color=GREY, fontweight="bold")
ax.plot([COLS[0] - 0.44, COLS[2] + 0.44], [4.62, 4.62],
        color=GREY, linewidth=1.1)


# ---- the three labels, each pulled out to the side of the tableau -----------
def label(text, detail, tx, ty, ax_pt, ay_pt, align, colour):
    """Write a name and its one-line meaning, joined to the tableau by an arrow."""
    ax.annotate("", xy=(ax_pt, ay_pt), xytext=(tx, ty),
                arrowprops=dict(arrowstyle="-|>", color=colour, linewidth=2.0,
                                mutation_scale=16))
    dx = 0.16 if align == "left" else -0.16
    ax.text(tx + dx, ty + 0.17, text, ha=align, va="center",
            fontsize=17, color=colour, fontweight="bold")
    ax.text(tx + dx, ty - 0.23, detail, ha=align, va="center",
            fontsize=13, color=INK)


label("quotient", "the answer, built one digit at a time",
      7.48, 4.28, 6.84, 4.16, "left", BLUE)
label("dividend", "the total you are splitting up",
      7.48, 3.05, 6.84, 3.13, "left", INK)
label("divisor", "how many equal parts you make",
      3.66, 2.50, 4.08, 2.90, "right", INK)

# ---- the sentence that ties the picture together ----------------------------
ax.text(W / 2, 1.28, "The divisor stands outside.  The dividend sits inside."
                     "  The quotient grows along the top.",
        ha="center", va="center", fontsize=15.5, color=INK, fontweight="bold")
ax.text(W / 2, 0.70, "Every quotient digit is written directly above the "
                     "dividend digit it belongs to, so the columns stay honest.",
        ha="center", va="center", fontsize=14, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_tableau_parts.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
