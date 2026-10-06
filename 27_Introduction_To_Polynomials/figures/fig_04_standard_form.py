"""Figure 4 - putting a polynomial into standard form.

Top row: 4 + 3x^2 - 7x as three cards, with the exponent of each term under
it (0, 2, 1). Bottom row: the same three cards in standard form,
3x^2 - 7x + 4, with exponents 2, 1, 0. Arrows show where each card went.
The minus sign stays on the -7x card the whole way (Chapter 19, section 2.4).
On the right, both rows are evaluated at x = 2 and give the same answer, 2.

Colour convention (as in fig_01):
    blue   - a term that carries x
    orange - the constant term
    purple - an exponent
    green  - the check that agrees
    grey   - quiet labels

Run with:  python figures/fig_04_standard_form.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"
BLUE_T = "#E9F2FC"
ORANGE = "#E67E22"
ORANGE_T = "#FDF0E3"
PURPLE = "#8E44AD"
GREEN = "#1E8449"
GREY = "#78909C"
INK = "#212121"

W, H = 13.4, 6.2                                   # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def card(xc, yc, text, edge, fill, w=1.75, h=1.05, size=26):
    """A rounded card of width w centred on (xc, yc) holding text."""
    ax.add_patch(FancyBboxPatch(
        (xc - w / 2, yc - h / 2), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.15",
        facecolor=fill, edgecolor=edge, linewidth=2.2, zorder=2))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=size,
            color=INK, zorder=3)


xs = [1.90, 4.30, 6.70]                            # three card positions
YT, YB = 4.55, 1.55                                # top row and bottom row

# (text, exponent, is constant?) for each row, left to right
top = [(r"$4$", 0, True), (r"$+3x^{2}$", 2, False), (r"$-7x$", 1, False)]
bottom = [(r"$3x^{2}$", 2, False), (r"$-7x$", 1, False), (r"$+4$", 0, True)]

ax.text(0.30, YT + 1.05, "as written", ha="left", va="center", fontsize=15,
        color=GREY, fontweight="bold")
ax.text(0.30, YB - 1.25, "standard form: largest exponent first",
        ha="left", va="center", fontsize=15, color=GREY, fontweight="bold")

for row, y in ((top, YT), (bottom, YB)):
    for xc, (t, e, const) in zip(xs, row):
        edge, fill = (ORANGE, ORANGE_T) if const else (BLUE, BLUE_T)
        card(xc, y, t, edge, fill)
        ax.text(xc, y - 0.78, rf"exponent ${e}$", ha="center", va="center",
                fontsize=12, color=PURPLE)

# arrows from each top card to where it lands in the bottom row
moves = [(0, 2, ORANGE), (1, 0, BLUE), (2, 1, BLUE)]   # (from slot, to slot, colour)
for a, b, colour in moves:
    ax.annotate("", xy=(xs[b], YB + 0.58), xytext=(xs[a], YT - 0.95),
                arrowprops=dict(arrowstyle="-|>", color=colour, lw=2.0,
                                mutation_scale=20, alpha=0.8))

# the check on the right: both rows give the same number at x = 2
ax.plot([8.05, 8.05], [0.40, 5.90], color=GREY, lw=1.0, ls=(0, (5, 4)))
x0 = 8.35
ax.text(x0, 5.55, r"check with $x = 2$", ha="left", va="center",
        fontsize=16, color=INK, fontweight="bold")
ax.text(x0, 4.70, r"$4 + 3(2)^{2} - 7(2)$", ha="left", va="center",
        fontsize=17, color=INK)
ax.text(x0, 4.05, r"$= 4 + 12 - 14 = 2$", ha="left", va="center",
        fontsize=17, color=GREEN)
ax.text(x0, 1.95, r"$3(2)^{2} - 7(2) + 4$", ha="left", va="center",
        fontsize=17, color=INK)
ax.text(x0, 1.30, r"$= 12 - 14 + 4 = 2$", ha="left", va="center",
        fontsize=17, color=GREEN)
ax.text(x0, 3.00, "same value: only the order changed",
        ha="left", va="center", fontsize=13, color=GREEN)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_standard_form.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_04_standard_form.png")
