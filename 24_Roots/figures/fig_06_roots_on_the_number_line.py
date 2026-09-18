"""Figure 6 - where roots sit on the number line.

The source drew this with text characters, which the book does not allow,
and which in any case could not place the irrational roots anywhere near
their real positions. Here every dot is at its true value.

Above the line: the roots of perfect squares, which land exactly on a
mark. Below the line: three roots that do not, each with the decimal that
never ends.

Numbers used, all checked with Python:
    sqrt(2)  = 1.41421356...
    sqrt(8)  = 2.82842712...
    sqrt(27) = 5.19615242...

Colour convention:
    blue   - a root that lands on a whole number
    orange - a root that lands between two whole numbers
    grey   - the ticks and the legend

Horizontal plan (x): the line runs 1.00 to 11.80 and carries 0 to 6, so
    one unit is 1.80 wide. The three orange dots fall at 3.545, 6.091
    and 10.353.

Vertical plan (y, top to bottom):
    4.45  figure heading
    3.85  the labels for the perfect-square roots
    3.30  the number line
    2.95  the whole numbers under the ticks
    2.40  the labels for the three other roots
    2.02  their decimal values
    1.05  the two-line legend

Run with:  python figures/fig_06_roots_on_the_number_line.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # a root that lands on a mark
ORANGE = "#E67E22"      # a root that lands between marks
GREY = "#78909C"
INK = "#212121"

W, H = 13.00, 4.95
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

X0, X1 = 1.00, 11.80    # the two ends of the drawn line
V0, V1 = 0, 6           # the numbers at those ends
Y = 3.30                # the height of the line


def px(value):
    """Turn a number into a position on the page."""
    return X0 + (X1 - X0) * (value - V0) / (V1 - V0)


ax.text(0.40, 4.45,
        "a few roots land exactly on a whole number; almost all of them "
        "land somewhere in between",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# ------------------------------------------------------------- the line
ax.annotate("", xy=(X1 + 0.32, Y), xytext=(X0 - 0.32, Y),
            arrowprops=dict(arrowstyle="<|-|>", linewidth=1.7, color=INK))

for value in range(V0, V1 + 1):
    ax.plot([px(value), px(value)], [Y - 0.13, Y + 0.13], linewidth=1.6,
            color=INK, zorder=1)
    ax.text(px(value), Y - 0.35, "$%d$" % value, ha="center", va="center",
            fontsize=13, color=GREY)

# ------------------------------------- the roots that land on a whole number
for value in range(1, V1 + 1):
    ax.plot([px(value)], [Y], marker="o", markersize=13, color=BLUE,
            zorder=4)
    ax.text(px(value), 3.85, r"$\sqrt{%d}$" % (value * value), ha="center",
            va="center", fontsize=16, color=BLUE, fontweight="bold")

# ------------------------------------------ the roots that land in between
for radicand, value, decimal in ((2, 1.41421356, "$1.414\\ldots$"),
                                 (8, 2.82842712, "$2.828\\ldots$"),
                                 (27, 5.19615242, "$5.196\\ldots$")):
    x = px(value)
    ax.plot([x], [Y], marker="o", markersize=13, color=ORANGE, zorder=5)
    # a short dashed drop, so the eye joins the dot to its label
    ax.plot([x, x], [Y - 0.18, 2.62], linewidth=1.3, color=ORANGE,
            linestyle=(0, (3, 3)), zorder=2)
    ax.text(x, 2.40, r"$\sqrt{%d}$" % radicand, ha="center", va="center",
            fontsize=16, color=ORANGE, fontweight="bold")
    ax.text(x, 2.02, decimal, ha="center", va="center", fontsize=12.5,
            color=ORANGE)

# --------------------------------------------------------------- the legend
ax.text(6.50, 1.32, "above the line: the root of a perfect square",
        ha="center", va="center", fontsize=13.5, color=BLUE)
ax.text(6.50, 0.95,
        "below the line: a root whose decimal never stops and never repeats",
        ha="center", va="center", fontsize=13.5, color=ORANGE)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_06_roots_on_the_number_line.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_06_roots_on_the_number_line.png")
