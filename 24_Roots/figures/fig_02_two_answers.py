"""Figure 2 - why the equation x squared = 9 has two answers.

Everything strange about square roots comes from one fact the reader
already owns from Chapter 9 section 5.2: a negative times a negative is
positive. So two different numbers, one on each side of zero, land on the
same square. The figure shows the two journeys arriving at the same card.

This is the figure the chapter points back to whenever a reader forgets
the negative solution, which is the commonest mistake in the topic.

Colour convention:
    blue   - the positive number and its journey
    orange - the negative number and its journey (Chapter 9's colour for
             the far side of zero)
    green  - the number both of them land on

Horizontal plan (x): the number line runs 1.20-11.80 and carries the
    values -4 to 4, so one unit is 1.325 wide. -3 sits at 2.525 and
    3 sits at 10.475. The card sits in the middle, at 6.50.

Vertical plan (y, top to bottom):
    6.05  figure heading
    5.05  the card holding 9
    3.72  the label for the orange journey
    3.05  the label for the blue journey
    2.90  the top of the two curved arrows
    2.00  the number line
    1.62  the numbers under the line
    0.52  the closing sentence

Run with:  python figures/fig_02_two_answers.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"        # the positive answer
ORANGE = "#E67E22"      # the negative answer
GREEN = "#1E8449"       # the number they both reach
GREY = "#78909C"
INK = "#212121"
GREEN_T = "#E8F5EC"

W, H = 13.00, 6.45
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

X_LEFT, X_RIGHT = 1.20, 11.80               # the ends of the number line
V_LOW, V_HIGH = -4, 4                       # the numbers at those ends
Y_LINE = 2.00                               # the height of the number line


def px(value):
    """Turn a number into a position on the page."""
    return X_LEFT + (X_RIGHT - X_LEFT) * (value - V_LOW) / (V_HIGH - V_LOW)


ax.text(0.40, 6.05,
        "two different numbers have the same square, because a negative "
        "times a negative is positive",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# ---------------------------------------------------------- the number line
ax.annotate("", xy=(X_RIGHT + 0.30, Y_LINE), xytext=(X_LEFT - 0.30, Y_LINE),
            arrowprops=dict(arrowstyle="<|-|>", linewidth=1.7, color=INK))

for value in range(V_LOW, V_HIGH + 1):
    ax.plot([px(value), px(value)], [Y_LINE - 0.11, Y_LINE + 0.11],
            linewidth=1.5, color=INK)
    if value in (-3, 3):
        continue                             # these two get their own label
    ax.text(px(value), Y_LINE - 0.40, "$%d$" % value, ha="center",
            va="center", fontsize=12, color=GREY)

# the two numbers the figure is about, drawn as big coloured dots
for value, colour in ((-3, ORANGE), (3, BLUE)):
    ax.plot([px(value)], [Y_LINE], marker="o", markersize=16, color=colour,
            zorder=5)
    ax.text(px(value), Y_LINE - 0.44, "$%d$" % value, ha="center",
            va="center", fontsize=15, color=colour, fontweight="bold")

# ------------------------------------------------------------- the two arcs
# Each arc leaves a dot, rises, and points at the bottom of the card.
ax.add_patch(FancyArrowPatch((px(-3), Y_LINE + 0.28), (6.50 - 0.55, 4.62),
                             connectionstyle="arc3,rad=-0.28",
                             arrowstyle="-|>", mutation_scale=22,
                             linewidth=3.0, color=ORANGE, zorder=3))
ax.add_patch(FancyArrowPatch((px(3), Y_LINE + 0.28), (6.50 + 0.55, 4.62),
                             connectionstyle="arc3,rad=0.28",
                             arrowstyle="-|>", mutation_scale=22,
                             linewidth=3.0, color=BLUE, zorder=3))

# The two labels sit in the empty middle column, stacked. An earlier
# version put each one beside its own arc, and the arc ran straight
# through the text - the same lesson as Chapter 10's fig_03.
ax.text(6.50, 3.72, r"$(-3) \times (-3) = 9$", ha="center", va="center",
        fontsize=17, color=ORANGE, fontweight="bold")
ax.text(6.50, 3.05, r"$3 \times 3 = 9$", ha="center", va="center",
        fontsize=17, color=BLUE, fontweight="bold")

# ---------------------------------------------------------------- the card
ax.text(6.50, 5.05, "$9$", ha="center", va="center", fontsize=30, color=INK,
        zorder=4,
        bbox=dict(boxstyle="round,pad=0.45", facecolor=GREEN_T,
                  edgecolor=GREEN, linewidth=2.2))

ax.text(6.50, 0.52,
        "so $x^{2} = 9$ has two answers, and the book writes them "
        r"together as $x = \pm 3$",
        ha="center", va="center", fontsize=15, color=INK)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_two_answers.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_02_two_answers.png")
