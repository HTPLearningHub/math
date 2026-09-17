"""Figure 4 - an expression is a phrase; an equation is a sentence.

Left: the expression 3x + 2 on a plain card. There is nothing to agree or
disagree with. It is a recipe waiting for a number.

Right: the equation y = 2x + 1 drawn as a level balance. The equals sign is
the pivot, and the claim the equation makes is exactly that the two pans hold
the same amount.

The balance is drawn again, three times, in fig_08, so the two figures teach
the same picture rather than two different ones.

Run with:  python figures/fig_04_expression_and_equation.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
from pathlib import Path

BLUE = "#2E86DE"          # variables
ORANGE = "#E67E22"        # fixed numbers
GREEN = "#1E8449"         # the claim that the two sides match
GREY = "#78909C"
INK = "#212121"
TINT_GREY = "#ECEFF1"
TINT_GREEN = "#E8F5EC"

W, H = 12.80, 5.70
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def balance(cx, base, half, left_text, right_text, beam_colour=GREEN):
    """A level pair of scales centred at cx, standing on the line y = base."""
    # the stand
    ax.add_patch(Polygon([[cx - 0.55, base], [cx + 0.55, base],
                          [cx, base + 0.95]],
                         closed=True, facecolor=TINT_GREY, edgecolor=GREY,
                         linewidth=1.8, zorder=2))
    ax.plot([cx - 0.95, cx + 0.95], [base, base], color=GREY, linewidth=2.4,
            zorder=2)
    # the beam across the top, level because the two sides are equal
    beam_y = base + 1.00
    ax.plot([cx - half, cx + half], [beam_y, beam_y], color=beam_colour,
            linewidth=3.4, zorder=3)
    for side in (-1, 1):
        x = cx + side * half
        ax.plot([x, x], [beam_y, beam_y + 0.34], color=GREY, linewidth=1.8,
                zorder=3)
        # the pan: a shallow tray the load sits in
        ax.plot([x - 0.58, x + 0.58], [beam_y + 0.34, beam_y + 0.34],
                color=GREY, linewidth=3.0, zorder=3)
    ax.text(cx - half, beam_y + 0.85, left_text, ha="center", va="center",
            fontsize=26, color=INK, zorder=4)
    ax.text(cx + half, beam_y + 0.85, right_text, ha="center", va="center",
            fontsize=26, color=INK, zorder=4)
    # the pivot dot, and the equals sign sitting over it between the loads
    ax.plot([cx], [beam_y], marker="o", markersize=9, color=beam_colour,
            zorder=4)
    ax.text(cx, beam_y + 0.85, r"$=$", ha="center", va="center", fontsize=24,
            color=beam_colour, fontweight="bold", zorder=4)


# ------------------------------------------------------------- the expression
ax.text(3.20, H - 0.45, "an expression", ha="center", va="center",
        fontsize=21, color=GREY, fontweight="bold")
ax.add_patch(FancyBboxPatch((3.20 - 1.75, 2.85), 3.50, 1.25,
                            boxstyle="round,pad=0.06,rounding_size=0.16",
                            facecolor=TINT_GREY, edgecolor=GREY,
                            linewidth=2.2, zorder=3))
ax.text(3.20, 3.48, r"$3x + 2$", ha="center", va="center", fontsize=30,
        color=INK, zorder=4)
ax.text(3.20, 2.35, "no equals sign", ha="center", va="center", fontsize=16,
        color=GREY)
ax.text(3.20, 1.85, "so nothing is claimed", ha="center", va="center",
        fontsize=16, color=GREY)
ax.text(3.20, 1.15, "it only waits for a number", ha="center", va="center",
        fontsize=15, color=GREY, style="italic")

# the divider
ax.plot([6.55, 6.55], [0.55, H - 0.95], color=GREY, linewidth=1.3,
        linestyle=(0, (4, 4)), zorder=1)

# --------------------------------------------------------------- the equation
ax.text(9.75, H - 0.45, "an equation", ha="center", va="center",
        fontsize=21, color=GREEN, fontweight="bold")
balance(9.75, 1.70, 1.95, r"$y$", r"$2x + 1$")
ax.text(9.75, 1.15, "the two sides hold the same amount",
        ha="center", va="center", fontsize=15, color=GREEN, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_expression_and_equation.png", dpi=170,
            facecolor="white")
print("saved", out / "fig_04_expression_and_equation.png")
