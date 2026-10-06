"""Figure 4 - a negative exponent on a fraction flips the fraction.

Top row: (2/3)^-2 -> (3/2)^2 -> 9/4, with an arrow labelled "flip it, the
minus sign is used up" and a second arrow labelled "square top and bottom".
Bottom row, under a dashed rule: the two answers people write instead,
each with a drawn cross beside it (a strike-through line lands in the middle
of a stacked fraction and makes it unreadable - see the Chapter 10 notes).

Colour convention:
    orange - the negative exponent, and the move it causes
    blue   - the result once the exponent is positive
    green  - the finished answer
    red    - the wrong answers
    grey   - arrow labels and the dashed rule

Horizontal plan (x): three expressions centred at 1.70, 6.30 and 10.90.
Vertical plan (y): heading 5.75, main row 4.20, rule 2.60, wrong row 1.30.

Run with:  python figures/fig_04_flip.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

ORANGE = "#E67E22"
BLUE = "#2E86DE"
GREEN = "#1E8449"
RED = "#C0392B"
GREY = "#78909C"
INK = "#212121"

W, H = 12.6, 6.2
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.30, 5.75, "a minus sign on the outside turns the fraction over",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

y = 4.10                                   # the main row
ax.text(1.70, y, r"$\left(\frac{2}{3}\right)^{-2}$", ha="center",
        va="center", fontsize=34, color=ORANGE)
ax.text(6.30, y, r"$\left(\frac{3}{2}\right)^{2}$", ha="center",
        va="center", fontsize=34, color=BLUE)
ax.text(10.90, y, r"$\frac{9}{4}$", ha="center", va="center",
        fontsize=38, color=GREEN)

# arrow 1 with its two-line label above it
ax.annotate("", xy=(5.10, y), xytext=(2.95, y),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2,
                            mutation_scale=22))
ax.text(4.02, y + 0.62, "flip it", ha="center", va="center", fontsize=14,
        color=ORANGE, fontweight="bold")
ax.text(4.02, y - 0.55, "the minus sign\nis used up", ha="center",
        va="center", fontsize=12, color=GREY, linespacing=1.2)

# arrow 2 with its label
ax.annotate("", xy=(10.20, y), xytext=(7.55, y),
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2,
                            mutation_scale=22))
ax.text(8.87, y + 0.62, "square top and bottom", ha="center",
        va="center", fontsize=14, color=BLUE, fontweight="bold")
ax.text(8.87, y - 0.50, r"$\frac{3^{2}}{2^{2}} = \frac{9}{4}$",
        ha="center", va="center", fontsize=16, color=GREY)

# dashed rule separating right from wrong
ax.plot([0.30, 12.30], [2.55, 2.55], color=GREY, lw=1.0, ls="--")
ax.text(0.30, 2.15, "not these:", ha="left", va="center", fontsize=14,
        color=RED, fontweight="bold")


def cross(xc, yc, r=0.22):
    """Draw a red X centred on (xc, yc)."""
    ax.plot([xc - r, xc + r], [yc - r, yc + r], color=RED, lw=3)
    ax.plot([xc - r, xc + r], [yc + r, yc - r], color=RED, lw=3)


# wrong answer 1: a negative number
ax.text(3.20, 1.15, r"$-\frac{4}{9}$", ha="center", va="center",
        fontsize=30, color=RED)
cross(4.15, 1.15)
ax.text(3.20, 0.25, "a negative exponent does not\nmake the answer negative",
        ha="center", va="center", fontsize=11.5, color=GREY, linespacing=1.2)

# wrong answer 2: flipped but the minus sign kept
ax.text(9.00, 1.15, r"$\left(\frac{3}{2}\right)^{-2}$", ha="center",
        va="center", fontsize=28, color=RED)
cross(10.20, 1.15)
ax.text(9.00, 0.25, "flipping uses the minus sign up;\nkeeping it flips back again",
        ha="center", va="center", fontsize=11.5, color=GREY, linespacing=1.2)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_flip.png", dpi=170, bbox_inches="tight",
            facecolor="white")
print("wrote", out / "fig_04_flip.png")
