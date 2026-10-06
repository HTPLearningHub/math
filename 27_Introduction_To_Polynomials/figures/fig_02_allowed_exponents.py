"""Figure 2 - which exponents a polynomial may use.

A number line of exponents from -3 to 4. The whole numbers 0, 1, 2, 3, 4
are green filled dots: a polynomial may use them, and the arrow says the list
goes on. The negative whole numbers and two fractions (1/2 and 3/2) are red
crosses: a polynomial may not use them. Under three of the red marks a small
label shows what that exponent hides: a letter under a fraction bar, or a
root (Chapter 10, section 7 and Chapter 24, section 7).

Colour convention:
    green  - allowed
    red    - not allowed
    grey   - the line and quiet labels

Run with:  python figures/fig_02_allowed_exponents.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from pathlib import Path

GREEN = "#1E8449"
RED = "#C0392B"
GREY = "#78909C"
INK = "#212121"

fig, ax = plt.subplots(figsize=(12.5, 4.6))
ax.axis("off")
ax.set_xlim(-3.9, 5.1)
ax.set_ylim(-2.2, 1.9)

# the number line itself, with an arrow head on the right
ax.annotate("", xy=(4.95, 0), xytext=(-3.6, 0),
            arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.8,
                            mutation_scale=20))
for k in range(-3, 5):                             # a tick and a number under it
    ax.plot([k, k], [-0.10, 0.10], color=GREY, lw=1.5)
    ax.text(k, -0.38, rf"${k}$", ha="center", va="center", fontsize=16,
            color=INK)
ax.text(0.5, -0.38, r"$\frac{1}{2}$", ha="center", va="center", fontsize=16,
        color=INK)                                 # the two fractions get labels too
ax.text(1.5, -0.38, r"$\frac{3}{2}$", ha="center", va="center", fontsize=16,
        color=INK)

# allowed exponents: whole numbers, drawn as green dots
for k in range(0, 5):
    ax.plot(k, 0, "o", ms=15, color=GREEN, zorder=3)
ax.text(4.55, 0.42, r"$\ldots$ and on", ha="center", va="center",
        fontsize=14, color=GREEN)


def cross(xc, r=0.13):
    """A red X centred on (xc, 0)."""
    ax.plot([xc - r, xc + r], [-r, r], color=RED, lw=3, zorder=3)
    ax.plot([xc - r, xc + r], [r, -r], color=RED, lw=3, zorder=3)


# not allowed: negative whole numbers and fractions
for xc in (-3, -2, -1, 0.5, 1.5):
    cross(xc)

# the headings above the two groups
ax.text(2.0, 1.15, "allowed: the whole numbers", ha="center", va="center",
        fontsize=17, color=GREEN, fontweight="bold")
ax.text(-2.0, 1.15, "not allowed", ha="center", va="center",
        fontsize=17, color=RED, fontweight="bold")
ax.text(1.0, 0.62, r"the fractions in between are not allowed either",
        ha="center", va="center", fontsize=12, color=RED)

# what a forbidden exponent hides, written under the line
ax.text(-2, -1.20, r"$x^{-2} = \frac{1}{x^{2}}$", ha="center", va="center",
        fontsize=18, color=RED)
ax.text(-1, -1.85, r"$x^{-1} = \frac{1}{x}$", ha="center", va="center",
        fontsize=18, color=RED)
ax.text(0.5, -1.20, r"$x^{\frac{1}{2}} = \sqrt{x}$", ha="center",
        va="center", fontsize=18, color=RED)
ax.text(-3.75, -1.55, "letter under a\nfraction bar", ha="left",
        va="center", fontsize=11, color=GREY)
ax.text(1.25, -1.20, "letter under\na root", ha="left", va="center",
        fontsize=11, color=GREY)

ax.text(4.95, -0.80, r"exponent of $x$", ha="right", va="center",
        fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_allowed_exponents.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_02_allowed_exponents.png")
