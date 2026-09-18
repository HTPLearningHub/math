"""Figure 9 - why even roots and odd roots behave differently.

The whole even/odd story rests on one pattern the reader met in Chapter 9
section 5.2: minus signs cancel in pairs. Multiply a negative number by
itself an even number of times and every minus has a partner, so the
answer is positive. Do it an odd number of times and one minus is left
over, so the answer is negative.

Once that pattern is on the page, the two rules about roots read straight
off it: a negative radicand can only be reached by an odd index, and a
positive radicand raised to an even index can be reached from both sides.

Five rows, one per power of -2, each written out in full so the minus
signs can be counted rather than trusted.

Colour convention:
    blue   - a positive answer (an even count of minus signs)
    orange - a negative answer (an odd count)
    grey   - the band behind every other row, and the closing lines

Horizontal plan (x): the power is left-aligned at 0.95, the product at
    2.55, the answer at 9.35, and the verdict word is centred at 11.60.
    The shading bands run 0.60 to 12.45.

Vertical plan (y, top to bottom):
    6.05  figure heading
    5.15  row 1, then 4.35, 3.55, 2.75 and 1.95
    1.15  the first closing line
    0.62  the second closing line

Run with:  python figures/fig_09_sign_pattern.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"        # a positive answer
ORANGE = "#E67E22"      # a negative answer
GREY = "#78909C"
INK = "#212121"
BAND = "#F4F6F8"        # the pale band behind every other row

W, H = 13.00, 6.45
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.40, 6.05,
        "minus signs cancel in pairs, so the count of them decides the sign",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

for n in range(1, 6):
    y = 5.15 - (n - 1) * 0.80

    # a pale band behind every other row, so the eye keeps its place
    if n % 2 == 0:
        ax.add_patch(Rectangle((0.60, y - 0.34), 11.85, 0.68,
                               facecolor=BAND, edgecolor="none", zorder=0))

    answer = (-2) ** n
    colour = ORANGE if answer < 0 else BLUE
    verdict = "odd" if n % 2 == 1 else "even"

    # the power itself
    ax.text(0.95, y, r"$(-2)^{%d}$" % n, ha="left", va="center",
            fontsize=18, color=INK, zorder=2)

    # the same thing written out, so the minus signs can be counted
    written = r" \times ".join([r"(-2)"] * n)
    ax.text(2.55, y, "$= %s$" % written, ha="left", va="center",
            fontsize=16, color=GREY, zorder=2)

    # the answer, coloured by its sign
    ax.text(9.35, y, "$= %d$" % answer, ha="left", va="center", fontsize=18,
            color=colour, fontweight="bold", zorder=2)

    # how many minus signs there were
    ax.text(11.60, y, "%s number of\nminus signs" % verdict, ha="center",
            va="center", fontsize=12, color=colour, linespacing=1.35,
            zorder=2)

ax.text(6.50, 1.15,
        "an $\\mathbf{even}$ count: every minus has a partner, they cancel, "
        "and the answer is positive",
        ha="center", va="center", fontsize=14.5, color=BLUE)
ax.text(6.50, 0.62,
        "an $\\mathbf{odd}$ count: one minus is left with no partner, "
        "and the answer is negative",
        ha="center", va="center", fontsize=14.5, color=ORANGE)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_09_sign_pattern.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_09_sign_pattern.png")
