"""Figure 1 - the parts of one polynomial.

The polynomial 6x^4 - 3x^2 + 8x - 5 is cut into its four terms. Each term
sits on its own card, with its sign attached (Chapter 21, section 1.2).
Under every card two labels say what the card holds: its coefficient and the
exponent of x. The 1 on 8x and the 0 on -5 are the invisible ones, so they
are drawn in a lighter colour. A green line at the bottom picks the largest
exponent: that is the degree.

Colour convention (as in Chapters 24-26):
    blue   - a term that carries x
    orange - the constant term
    purple - an exponent
    green  - the answer we read off (the degree)
    grey   - quiet labels

Run with:  python figures/fig_01_anatomy.py
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
PURPLE_L = "#C39BD3"                               # light purple: an invisible exponent
GREEN = "#1E8449"
GREY = "#78909C"
INK = "#212121"

W, H = 12.6, 6.4                                   # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def card(xc, yc, text, edge, fill, w=2.30, h=1.15, size=28):
    """A rounded card of width w centred on (xc, yc) holding text."""
    ax.add_patch(FancyBboxPatch(
        (xc - w / 2, yc - h / 2), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.15",
        facecolor=fill, edgecolor=edge, linewidth=2.2, zorder=1))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=size,
            color=INK, zorder=2)


# the whole polynomial on one line at the top
ax.text(W / 2, 5.85, r"$6x^{4} - 3x^{2} + 8x - 5$", ha="center",
        va="center", fontsize=32, color=INK)
ax.text(W / 2, 5.15, "cut at every plus and minus sign: four terms",
        ha="center", va="center", fontsize=14, color=GREY)

# (term, coefficient label, exponent label, exponent is invisible?, constant?)
terms = [
    (r"$6x^{4}$", r"coefficient  $6$", r"exponent  $4$", False, False),
    (r"$-3x^{2}$", r"coefficient  $-3$", r"exponent  $2$", False, False),
    (r"$+8x$", r"coefficient  $8$", r"exponent  $1$  ($x = x^{1}$)", True, False),
    (r"$-5$", "constant term", r"exponent  $0$  (no $x$)", True, True),
]
xs = [1.75, 4.80, 7.85, 10.90]                     # card centres, evenly spaced
for xc, (t, coef, expo, hidden, const) in zip(xs, terms):
    edge, fill = (ORANGE, ORANGE_T) if const else (BLUE, BLUE_T)
    card(xc, 3.95, t, edge, fill)                  # the term itself
    ax.text(xc, 2.95, coef, ha="center", va="center", fontsize=14,
            color=ORANGE if const else BLUE)       # what multiplies x
    ax.text(xc, 2.45, expo, ha="center", va="center", fontsize=14,
            color=PURPLE_L if hidden else PURPLE)  # the power on x

# a thin rule, then the degree read off from the exponent labels
ax.plot([0.60, W - 0.60], [1.75, 1.75], color=GREY, lw=1.0, ls=(0, (5, 4)))
ax.text(W / 2, 1.15,
        r"exponents  $4,\ 2,\ 1,\ 0$:   the largest is $4$,   so the degree is $4$",
        ha="center", va="center", fontsize=18, color=GREEN)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_anatomy.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_01_anatomy.png")
