"""Figure 3 - the four inequalities, all with the same boundary number.

The source drew three number lines with three different boundaries (3, 4
and -6), which hides the thing the reader needs to see. Here all four use
the boundary 3, so the only differences left on the page are the two that
matter: which way the arrow points, and whether the circle is hollow or
filled.

Reading order is deliberate: the two strict ones first, then the two
non-strict ones, so the circle changes once, halfway down, instead of
alternating. Each group is labelled once, above it - labelling every line
would repeat the same sentence four times.

Horizontal plan (x): one shared scale, -2 to 8 mapped to 2.55 to 10.95,
so one unit is 0.84 of an inch. The label for each line sits at x = 0.50,
left of the axis, so the four labels form a column.

The axis overhangs its last tick by 0.78, and the green ray stops 0.42
past the last tick. That gap is on purpose: it leaves the green arrowhead
visible instead of hiding it under the black one, and the arrowhead is
what says the solution set never ends.

Vertical plan (y, top to bottom):
    5.95  heading
    5.45  what the first group has in common
    4.85  line 1,  x > 3
    3.85  line 2,  x < 3
    3.20  divider between strict and non-strict
    2.75  what the second group has in common
    2.15  line 3,  x >= 3
    1.15  line 4,  x <= 3
    0.30  closing note

Run with:  python figures/fig_03_the_four_graphs.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

GREEN = "#1E8449"         # the solution set, as everywhere in this chapter
GREY = "#78909C"
INK = "#212121"

W, H = 12.20, 6.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

X0, X1 = 2.55, 10.95      # where -2 and 8 land on the page
V0, V1 = -2.0, 8.0
BOUND = 3.0               # every line in this figure turns at 3
OVERHANG = 0.78           # how far the axis runs past its last tick
RAY_END = 0.42            # how far the green ray runs past its last tick


def px(value):
    """Turn a number on the line into a position on the page."""
    return X0 + (X1 - X0) * (value - V0) / (V1 - V0)


def graph(y, label, direction, closed):
    """Draw one labelled number line with its solution ray.

    direction: +1 for a ray going right, -1 for a ray going left.
    closed:    True draws a filled circle, False a hollow one.
    """
    # the label, left of the axis, in a column with the other three
    ax.text(0.50, y, label, ha="left", va="center", fontsize=21,
            color=INK, fontweight="bold")

    # the axis, with a tick and a number at every whole number
    ax.annotate("", xy=(X1 + OVERHANG, y), xytext=(X0 - OVERHANG, y),
                arrowprops=dict(arrowstyle="<|-|>", linewidth=1.6,
                                color=INK))
    for value in range(int(V0), int(V1) + 1):
        ax.plot([px(value), px(value)], [y - 0.09, y + 0.09],
                linewidth=1.4, color=INK)
        ax.text(px(value), y - 0.33, str(value), ha="center", va="center",
                fontsize=10.5, color=GREY)

    # the ray, stopping short of the black arrowhead so that its own
    # arrowhead can be seen
    end = X1 + RAY_END if direction > 0 else X0 - RAY_END
    ax.annotate("", xy=(end, y), xytext=(px(BOUND), y),
                arrowprops=dict(arrowstyle="-|>", linewidth=5.0,
                                color=GREEN, mutation_scale=17), zorder=4)

    # the circle at the boundary: filled means the boundary is included
    if closed:
        ax.plot([px(BOUND)], [y], marker="o", markersize=14, color=GREEN,
                zorder=6)
    else:
        ax.plot([px(BOUND)], [y], marker="o", markersize=14,
                markerfacecolor="white", markeredgecolor=GREEN,
                markeredgewidth=2.8, zorder=6)


ax.text(0.50, 5.95, "one boundary, four answers",
        ha="left", va="center", fontsize=20, color=INK, fontweight="bold")

ax.text(0.50, 5.45,
        "strict  ($>$ and $<$)  -  hollow circle, the boundary is left out",
        ha="left", va="center", fontsize=13.5, color=GREEN,
        fontweight="bold")
graph(4.85, r"$x > 3$", +1, False)
graph(3.85, r"$x < 3$", -1, False)

ax.plot([0.40, W - 0.40], [3.20, 3.20], linewidth=1.0, color=GREY,
        linestyle=(0, (4, 4)), zorder=1)

ax.text(0.50, 2.75,
        "not strict  ($\\geq$ and $\\leq$)  -  filled circle, "
        "the boundary is included",
        ha="left", va="center", fontsize=13.5, color=GREEN,
        fontweight="bold")
graph(2.15, r"$x \geq 3$", +1, True)
graph(1.15, r"$x \leq 3$", -1, True)

ax.text(0.50, 0.30,
        "the arrow follows the open side of the symbol; "
        "the circle follows whether the symbol carries a line under it",
        ha="left", va="center", fontsize=12.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_the_four_graphs.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_03_the_four_graphs.png")
