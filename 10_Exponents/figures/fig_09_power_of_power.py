"""Figure 9 - why a power raised to a power multiplies the exponents.

(x^4)^2 is two copies of x^4, so it is two rows with four x's in each row.
Laid out as a rectangle, the question "how many x's altogether" is the
Chapter 6 area question, and the answer is 4 x 2 = 8. Nobody has to be told
to multiply; a rectangle of x's cannot be counted any other way.

The right-hand panel puts the wrong answer beside the right one, because the
whole mistake is confusing this rule with the one in section 4.
Run with:  python figures/fig_09_power_of_power.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # the inner power, the one that fills a row
PURPLE = "#8E44AD"      # the outer power, the one that counts the rows
GREY = "#78909C"
RED = "#C0392B"
INK = "#212121"

W, H = 11.4, 5.05
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

INNER, OUTER = 4, 2                        # (x^4)^2: four in a row, two rows
CW, CH = 0.74, 0.80                        # the size of one cell of the rectangle
X0, Y0 = 1.85, 1.72                        # the bottom-left corner of the rectangle

for r in range(OUTER):
    for c in range(INNER):
        x = X0 + c * CW
        y = Y0 + r * CH
        ax.add_patch(Rectangle((x, y), CW, CH, facecolor="#EAF2FC",
                               edgecolor=BLUE, linewidth=1.4))
        ax.text(x + CW / 2, y + CH / 2, r"$x$", ha="center", va="center",
                fontsize=20, color=INK)
    # name each row on its left, so the two rows are visibly two copies
    ax.text(X0 - 0.22, Y0 + r * CH + CH / 2, r"$x^{4}$", ha="right", va="center",
            fontsize=19, color=BLUE, fontweight="bold")

RIGHT = X0 + INNER * CW
TOPY = Y0 + OUTER * CH

# how many in a row, measured along the top
ax.annotate("", xy=(RIGHT, TOPY + 0.30), xytext=(X0, TOPY + 0.30),
            arrowprops=dict(arrowstyle="<|-|>", color=BLUE, linewidth=1.6,
                            mutation_scale=13))
ax.text((X0 + RIGHT) / 2, TOPY + 0.62, "four x's in a row",
        ha="center", va="center", fontsize=14, color=BLUE)

# how many rows, measured down the right-hand side
ax.annotate("", xy=(RIGHT + 0.32, Y0), xytext=(RIGHT + 0.32, TOPY),
            arrowprops=dict(arrowstyle="<|-|>", color=PURPLE, linewidth=1.6,
                            mutation_scale=13))
ax.text(RIGHT + 0.48, (Y0 + TOPY) / 2, "two rows,\nbecause the\nouter power is 2",
        ha="left", va="center", fontsize=13, color=PURPLE, linespacing=1.5)

ax.text((X0 + RIGHT) / 2, Y0 - 0.48, r"$4 \times 2 = 8$ x's altogether",
        ha="center", va="center", fontsize=18, color=INK, fontweight="bold")

# the right answer and the wrong one, side by side
PANEL_X = 7.55
ax.add_patch(FancyBboxPatch((PANEL_X, 1.52), 3.35, 1.98,
                            boxstyle="round,pad=0.05,rounding_size=0.14",
                            facecolor="#F6F8FA", edgecolor=GREY, linewidth=1.3))
ax.text(PANEL_X + 1.68, 3.14, "so which is it?", ha="center", va="center",
        fontsize=14, color=GREY, fontweight="bold")
ax.text(PANEL_X + 1.68, 2.56, r"$(x^{4})^{2} = x^{4 \times 2} = x^{8}$",
        ha="center", va="center", fontsize=19, color=INK, fontweight="bold")
ax.text(PANEL_X + 1.68, 1.94, r"not  $x^{4 + 2} = x^{6}$",
        ha="center", va="center", fontsize=17, color=RED)

ax.text(W / 2, H - 0.32, r"$(x^{4})^{2}$ is two copies of $x^{4}$, written out as a rectangle",
        ha="center", va="center", fontsize=17, color=INK, fontweight="bold")
ax.text(W / 2, 0.36,
        "Adding is for two powers multiplied together. This is one power, taken twice.",
        ha="center", va="center", fontsize=14.5, color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_09_power_of_power.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
