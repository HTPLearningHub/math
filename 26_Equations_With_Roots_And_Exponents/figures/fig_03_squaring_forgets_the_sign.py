"""Figure 3 - squaring both sides can turn a false equation into a true one.

Left panel: two different numbers, 3 (blue) and -3 (orange), each sent through
"square it" into the same card, 9. The false statement 3 = -3 becomes the true
statement 9 = 9. Squaring forgets the sign (Chapter 24, section 2.1).

Right panel: the equation sqrt(2x + 1) = -3 worked one line at a time. Squaring
gives 2x + 1 = 9, so x = 4. The check in the original equation gives
sqrt(9) = 3, not -3, so x = 4 is a stranger the squaring let in. A red cross is
drawn beside the check, never on top of it (the Chapter 10 lesson).

Colour convention:
    blue   - a positive number
    orange - its negative partner (Chapter 9's "far side of zero")
    green  - a statement that is true
    red    - a statement that is false, and the rejected answer
    grey   - quiet labels

Run with:  python figures/fig_03_squaring_forgets_the_sign.py
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
GREEN = "#1E8449"
GREEN_T = "#E8F5EC"
RED = "#C0392B"
GREY = "#78909C"
INK = "#212121"

W, H = 13.4, 7.4                                   # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def card(xc, yc, text, edge, fill, w=1.40, h=1.05, size=24):
    """A rounded card of width w centred on (xc, yc) holding text."""
    ax.add_patch(FancyBboxPatch(
        (xc - w / 2, yc - h / 2), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.15",
        facecolor=fill, edgecolor=edge, linewidth=2.0, zorder=1))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=size,
            color=INK, zorder=2)


# ================================================================ left panel
ax.text(0.30, 6.85, "squaring forgets the sign", ha="left", va="center",
        fontsize=18, color=INK, fontweight="bold")

card(1.50, 5.30, r"$3$", BLUE, BLUE_T)             # the positive number
card(4.70, 5.30, r"$-3$", ORANGE, ORANGE_T)        # its negative partner
ax.text(3.10, 5.30, r"$\neq$", ha="center", va="center", fontsize=26,
        color=RED)                                 # they are different

card(3.10, 2.20, r"$9$", GREEN, GREEN_T)           # the shared square

# two arrows meeting in the one card; labels sit in the gap between them
ax.annotate("", xy=(2.85, 2.80), xytext=(1.60, 4.72),
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.4,
                            mutation_scale=22))
ax.annotate("", xy=(3.35, 2.80), xytext=(4.60, 4.72),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.4,
                            mutation_scale=22))
ax.text(3.10, 4.05, "square\nboth", ha="center", va="center",
        fontsize=13, color=GREY)

ax.text(0.30, 1.05, r"$3 = -3$ is false.", ha="left", va="center",
        fontsize=15, color=RED)
ax.text(0.30, 0.50, r"$9 = 9$ is true.", ha="left", va="center",
        fontsize=15, color=GREEN)

# a dashed divider between the two panels
ax.plot([6.30, 6.30], [0.30, 7.05], color=GREY, lw=1.2, ls=(0, (5, 4)))

# =============================================================== right panel
x0 = 6.80                                          # left edge of the right panel
ax.text(x0, 6.85, "so a wrong answer can slip in", ha="left", va="center",
        fontsize=18, color=INK, fontweight="bold")

lines = [
    (r"$\sqrt{2x + 1} = -3$", INK, "the equation"),
    (r"$2x + 1 = 9$", INK, "square both sides"),
    (r"$2x = 8$", INK, r"subtract $1$"),
    (r"$x = 4$", INK, r"divide by $2$"),
]
y = 5.85
for maths, colour, why in lines:                   # one step per line
    ax.text(x0 + 0.10, y, maths, ha="left", va="center", fontsize=20,
            color=colour)
    ax.text(x0 + 3.55, y, why, ha="left", va="center", fontsize=13,
            color=GREY)
    y -= 0.95

# the check, in red, with a drawn cross placed beside it
yc = y - 0.25
ax.text(x0 + 0.10, yc, r"check:  $\sqrt{2(4) + 1} = \sqrt{9} = 3$",
        ha="left", va="center", fontsize=18, color=RED)
ax.text(x0 + 0.10, yc - 0.70, r"but the right side is $-3$, and $3 \neq -3$",
        ha="left", va="center", fontsize=15, color=RED)
cx, cy, r = x0 + 5.85, yc, 0.20                    # cross centre and half size
ax.plot([cx - r, cx + r], [cy - r, cy + r], color=RED, lw=3)
ax.plot([cx - r, cx + r], [cy + r, cy - r], color=RED, lw=3)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_squaring_forgets_the_sign.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_03_squaring_forgets_the_sign.png")
