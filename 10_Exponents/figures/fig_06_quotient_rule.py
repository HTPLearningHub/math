"""Figure 6 - why dividing two powers subtracts the exponents.

Five x's over three x's. Each x on the bottom cancels one x on the top,
exactly as in Chapter 1 section 3.3, and the grey strokes show which pairs
went. Two x's are left standing on the top, and 5 - 3 = 2 is a description
of what happened, not a rule imposed on it.

The 1 under the bar is drawn on purpose: the bottom does not vanish, it
becomes 1, and a reader who does not see that will think the fraction has
lost its denominator.
Run with:  python figures/fig_06_quotient_rule.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # what is left standing
PURPLE = "#8E44AD"      # the count
GREY = "#78909C"        # the cancelled pairs
INK = "#212121"

W, H = 11.8, 5.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

SLOT = 0.62                                 # the width given to one x
CX = 3.85                                   # the middle of the fraction
Y_BAR = 2.85                                # the height of the fraction bar
Y_UP, Y_DOWN = Y_BAR + 0.62, Y_BAR - 0.62   # the two rows of x's

TOP, BOTTOM = 5, 3                          # x^5 over x^3


def row(count, y, start, survivors=0):
    """Draw `count` x's in a row, centred on `start`, and return their x positions.

    The last `survivors` of them are drawn blue, because they are the ones no
    x underneath can cancel. Each x is drawn once, in its final colour: an x
    drawn black and then painted over shows its black edges at print size.
    """
    xs = [start - (count - 1) * SLOT / 2 + k * SLOT for k in range(count)]
    for k, x in enumerate(xs):
        lives = k >= count - survivors
        ax.text(x, y, r"$x$", ha="center", va="center", fontsize=24,
                color=BLUE if lives else INK,
                fontweight="bold" if lives else "normal")
    return xs


xs_top = row(TOP, Y_UP, CX, survivors=TOP - BOTTOM)
xs_bot = row(BOTTOM, Y_DOWN, CX)

# the fraction bar, long enough for the wider of the two rows
half = max(TOP, BOTTOM) * SLOT / 2 + 0.22
ax.plot([CX - half, CX + half], [Y_BAR] * 2, color=INK, linewidth=2.2)

# strike out the pairs that cancel, one stroke per pair, and join them up
for k in range(BOTTOM):
    for x, y in ((xs_top[k], Y_UP), (xs_bot[k], Y_DOWN)):
        ax.plot([x - 0.17, x + 0.17], [y - 0.17, y + 0.17],
                color=GREY, linewidth=2.0)
    ax.plot([xs_top[k], xs_bot[k]], [Y_UP - 0.26, Y_DOWN + 0.26],
            color=GREY, linewidth=1.0, linestyle=(0, (2, 3)))

ax.text(CX, Y_UP + 0.70, "five x's on top", ha="center", va="center",
        fontsize=13.5, color=GREY)
ax.text(CX, Y_DOWN - 0.70, "three x's underneath", ha="center", va="center",
        fontsize=13.5, color=GREY)

# what is left, written out as a fraction with a 1 underneath
X_RES = 7.35
ax.text(X_RES - 0.55, Y_BAR, r"$=$", ha="center", va="center", fontsize=26, color=INK)
ax.text(X_RES + 0.45, Y_UP, r"$x \times x$", ha="center", va="center",
        fontsize=24, color=BLUE, fontweight="bold")
ax.text(X_RES + 0.45, Y_DOWN, r"$1$", ha="center", va="center",
        fontsize=24, color=INK)
ax.plot([X_RES - 0.35, X_RES + 1.25], [Y_BAR] * 2, color=INK, linewidth=2.2)
ax.text(X_RES + 2.05, Y_BAR, r"$=\; x^{2}$", ha="left", va="center",
        fontsize=26, color=BLUE, fontweight="bold")
ax.text(X_RES + 0.45, Y_DOWN - 0.70, "nothing is left underneath,\nso the bottom is 1",
        ha="center", va="top", fontsize=12.5, color=GREY, linespacing=1.5)

# the heading and the counting sentence
ax.text(W / 2, H - 0.34, r"$\dfrac{x^{5}}{x^{3}} = x^{2}$",
        ha="center", va="center", fontsize=24, color=INK)
ax.text(W / 2, 0.38,
        r"Three pairs cancelled, so $5 - 3 = 2$ are left standing.",
        ha="center", va="center", fontsize=16, color=PURPLE, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_quotient_rule.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
