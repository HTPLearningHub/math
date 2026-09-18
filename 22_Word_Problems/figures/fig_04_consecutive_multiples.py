"""Figure 4 - consecutive multiples of 3 against consecutive whole numbers.

The mistake this figure exists to prevent is writing the three brothers'
ages as x, x+1, x+2. Two number lines, drawn to the same scale and placed
one above the other, make the difference impossible to miss: the gaps in
the upper line are three times the gaps in the lower one.

The upper line carries both readings of each point - the letter version
above and the number version below - because the whole trick of the
method is that those two are the same thing.

Horizontal plan (x): one shared scale, 0 to 18 mapped to 1.05 to 10.35,
so one unit is 0.5167 of an inch. The lower line uses the same map, so
the two are honestly comparable.

Vertical plan (y, top to bottom):
    5.55  heading
    4.90  the letters x, x+3, x+6
    4.42  the +3 hops
    4.00  the upper number line
    3.52  the numbers 9, 12, 15
    3.05  the label of the upper line
    2.22  the one label for all three grey points
    1.86  the bracket over the cluster
    1.50  the lower number line
    1.14  the numbers under the lower line
    0.60  the label of the lower line
    0.18  closing note

Run with:  python figures/fig_04_consecutive_multiples.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # the three quantities the problem asks about
ORANGE = "#E67E22"        # the step from one to the next
GREY = "#78909C"          # the line the story is not about
INK = "#212121"

W, H = 12.40, 5.95
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

X0, X1 = 1.05, 10.35      # where 0 and 18 land on the page
UNITS = 18.0


def px(value):
    """Turn a number on the line into a position on the page."""
    return X0 + (X1 - X0) * value / UNITS


ax.text(0.55, 5.55, "multiples of $3$ step by $3$, not by $1$",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# ---------------------------------------------------------------- upper
# the line itself, with a tick at every multiple of 3
ax.annotate("", xy=(X1 + 0.35, 4.00), xytext=(X0 - 0.30, 4.00),
            arrowprops=dict(arrowstyle="-|>", linewidth=2.0, color=INK))
for value in range(0, 19, 3):
    ax.plot([px(value), px(value)], [3.90, 4.10], linewidth=1.8,
            color=INK)
    if value not in (9, 12, 15):
        ax.text(px(value), 3.60, str(value), ha="center", va="center",
                fontsize=11.5, color=GREY)

# the three ages: a filled dot, the letter above, the number below
AGES = ((9, r"$x$"), (12, r"$x + 3$"), (15, r"$x + 6$"))
for value, letters in AGES:
    ax.plot([px(value)], [4.00], marker="o", markersize=12, color=BLUE,
            zorder=4)
    ax.text(px(value), 4.90, letters, ha="center", va="center",
            fontsize=17, color=BLUE)
    ax.text(px(value), 3.52, str(value), ha="center", va="center",
            fontsize=15, color=BLUE, fontweight="bold")

# a hop from each age to the next, labelled with the size of the step
for start in (9, 12):
    ax.add_patch(FancyArrowPatch((px(start), 4.42),
                                 (px(start + 3), 4.42),
                                 connectionstyle="arc3,rad=-0.45",
                                 arrowstyle="-|>", mutation_scale=14,
                                 linewidth=2.0, color=ORANGE, zorder=3))
    ax.text(px(start + 1.5), 4.60, r"$+\,3$", ha="center", va="center",
            fontsize=13, color=ORANGE)

ax.text(0.55, 3.05, "three consecutive multiples of $3$  -  this is what "
        "the problem says", ha="left", va="center", fontsize=13.5,
        color=BLUE)

# ---------------------------------------------------------------- lower
ax.annotate("", xy=(X1 + 0.35, 1.50), xytext=(X0 - 0.30, 1.50),
            arrowprops=dict(arrowstyle="-|>", linewidth=2.0, color=INK))
for value in range(0, 19, 3):
    ax.plot([px(value), px(value)], [1.40, 1.60], linewidth=1.8,
            color=INK)
    ax.text(px(value), 1.14, str(value), ha="center", va="center",
            fontsize=11.5, color=GREY)

# the same starting point, but stepping by one: the wrong reading.
# the three points are far too close together to label one by one at
# this scale - which is exactly the thing worth seeing - so one bracket
# names all three at once
for value in (9, 10, 11):
    ax.plot([px(value)], [1.50], marker="o", markersize=10, color=GREY,
            zorder=4)

# a plain bracket over the cluster: a lid with a tick down at each end
ax.plot([px(9), px(11)], [1.86, 1.86], linewidth=1.8, color=GREY)
ax.plot([px(9), px(9)], [1.86, 1.72], linewidth=1.8, color=GREY)
ax.plot([px(11), px(11)], [1.86, 1.72], linewidth=1.8, color=GREY)
ax.plot([px(10), px(10)], [1.86, 2.00], linewidth=1.8, color=GREY)

ax.text(px(10), 2.22, r"$x$,  $x + 1$,  $x + 2$", ha="center",
        va="center", fontsize=15, color=GREY)
ax.text(px(11) + 0.45, 1.86, r"each step is only $+\,1$", ha="left",
        va="center", fontsize=12.5, color=GREY)

ax.text(0.55, 0.60, "three consecutive whole numbers  -  a different "
        "thing, and much closer together", ha="left", va="center",
        fontsize=13.5, color=GREY)

ax.text(0.55, 0.18, "both lines are drawn to the same scale, so the "
        "three grey dots really are that crowded",
        ha="left", va="center", fontsize=12.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_consecutive_multiples.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_04_consecutive_multiples.png")
