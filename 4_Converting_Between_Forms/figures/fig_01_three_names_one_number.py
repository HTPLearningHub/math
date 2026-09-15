"""Figure 1 - three rulers, one point.

The three lines are the same line, measured with three different scales:
tenths (a fraction), decimals, and percent.
A single vertical marker cuts through all three at the same place,
so the reader can see that 3/10, 0.3 and 30% are one point, not three.
Run with:  python figures/fig_01_three_names_one_number.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

ORANGE = "#E67E22"   # percent
BLUE = "#2E86DE"     # fraction
SLATE = "#546E7A"    # decimal
MARK = "#C0392B"     # the marker that joins the three rulers
TEXT = "#37474F"

LEFT, RIGHT = 0.0, 10.0      # the drawing is 10 units wide and means 0 to 1
VALUE = 3.0                  # the point we mark: three tenths of the way along

fig, ax = plt.subplots(figsize=(11.4, 5.4))
ax.axis("off")
ax.set_xlim(-1.5, RIGHT + 1.3)
ax.set_ylim(-0.6, 5.2)


def ruler(y, colour, name, labels):
    """One horizontal ruler: a line, eleven ticks, and a label under every tick."""
    ax.plot([LEFT, RIGHT], [y, y], color=colour, linewidth=2.6,
            solid_capstyle="butt", zorder=2)
    for k, text in enumerate(labels):
        x = LEFT + k * (RIGHT - LEFT) / 10
        ax.plot([x, x], [y - 0.16, y + 0.16], color=colour, linewidth=1.8, zorder=2)
        ax.text(x, y - 0.46, text, ha="center", va="center",
                fontsize=11.5, color=colour)
    ax.text(LEFT - 0.45, y, name, ha="right", va="center",
            fontsize=14, color=colour, fontweight="bold")


# the fraction ruler: how many tenths of the whole
ruler(4.1, BLUE, "fraction",
      [r"$0$"] + [rf"$\frac{{{k}}}{{10}}$" for k in range(1, 10)] + [r"$1$"])

# the decimal ruler: the same marks written with a point
ruler(2.4, SLATE, "decimal",
      [f"{k / 10:.1f}" for k in range(11)])

# the percent ruler: the same marks written out of a hundred
ruler(0.7, ORANGE, "percent",
      [rf"${k * 10}\%$" for k in range(11)])

# One vertical line through all three rulers, at three tenths.
# It is drawn in pieces so that it never runs across a tick label.
for y0, y1 in [(0.70, 1.80), (2.08, 3.50), (3.78, 4.35)]:
    ax.plot([VALUE, VALUE], [y0, y1], color=MARK, linewidth=2.4,
            linestyle="--", zorder=3)
for y in (4.1, 2.4, 0.7):
    ax.plot([VALUE], [y], marker="o", markersize=10, color=MARK, zorder=4)

ax.text(VALUE, 4.95, r"one point   $\frac{3}{10} = 0.3 = 30\%$",
        ha="center", va="center", fontsize=15, color=MARK, fontweight="bold")

ax.set_title("The same amount, measured with three different scales",
             fontsize=17, fontweight="bold", pad=10)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_three_names_one_number.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
