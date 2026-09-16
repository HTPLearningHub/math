"""Figure 2 - the factors of 20 come in pairs, and the pairs meet in the middle.

Two things have to be visible at once:
  * every factor has a partner, and the two partners multiply to 20;
  * walking up from 1, the partners come towards you, and once they cross
    there is nothing new left to find.

Layout: the numbers 1 to 20 in a row of cells. Factors are filled green,
everything else is a pale outline. Three arcs above the row join the three
pairs, each labelled with its multiplication. A dashed line marks half of
20, which is where the source's halfway rule tells you to stop, and a
shorter orange marker sits between 4 and 5, which is where the pairs
actually cross.
Run with:  python figures/fig_02_factor_pairs.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Arc
from pathlib import Path

GREEN = "#1E8449"            # a factor
GREY = "#78909C"             # not a factor, and quiet labels
ORANGE = "#E67E22"           # the crossing point
INK = "#212121"

N = 20
FACTORS = [1, 2, 4, 5, 10, 20]
PAIRS = [(1, 20), (2, 10), (4, 5)]

W, H = 12.4, 6.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CELL = 0.555                              # width of one number cell
CH = 0.62                                 # height of one number cell
LEFT = (W - N * CELL) / 2                 # left edge of the whole row
ROW_Y = 1.62                              # bottom edge of the row of cells


def cx(n):
    """Centre of the cell that holds the number n."""
    return LEFT + (n - 0.5) * CELL


# -------------------------------------------------------- the row of numbers
for n in range(1, N + 1):
    is_factor = n in FACTORS
    ax.add_patch(FancyBboxPatch((cx(n) - CELL / 2 + 0.03, ROW_Y), CELL - 0.06, CH,
                                boxstyle="round,pad=0.01,rounding_size=0.07",
                                facecolor="#E8F5EC" if is_factor else "#FFFFFF",
                                edgecolor=GREEN if is_factor else "#D8DEE1",
                                linewidth=1.8 if is_factor else 1.1))
    ax.text(cx(n), ROW_Y + CH / 2, str(n), ha="center", va="center",
            fontsize=14 if is_factor else 12,
            color=GREEN if is_factor else "#B0BEC5",
            fontweight="bold" if is_factor else "normal")

# ------------------------------------------------------------- the three arcs
# The arcs are drawn tallest first so the widest pair sits furthest from the row.
ARC_TOP = ROW_Y + CH                      # arcs start just above the cells
for (a, b), height in zip(PAIRS, (3.10, 1.94, 0.86)):
    left, right = cx(a), cx(b)
    ax.add_patch(Arc(((left + right) / 2, ARC_TOP), right - left, 2 * height,
                     theta1=0, theta2=180, edgecolor=GREEN, linewidth=1.9))
    ax.text((left + right) / 2, ARC_TOP + height + 0.20,
            rf"${a} \times {b} = 20$", ha="center", va="center",
            fontsize=15, color=GREEN)

# ----------------------------------------------- half of 20, the halfway rule
half_x = cx(10) + CELL / 2                # the right-hand edge of the cell 10
ax.plot([half_x, half_x], [ROW_Y - 0.72, ROW_Y - 0.10],
        linestyle=(0, (4, 3)), linewidth=1.5, color=GREY)
ax.text(half_x, ROW_Y - 0.96, "half of 20", ha="center", va="center",
        fontsize=12.5, color=GREY)
ax.text(half_x, ROW_Y - 1.26, "nothing beyond here is a factor,\nexcept 20 itself",
        ha="center", va="center", fontsize=11.5, color=GREY)

# ------------------------------------------------ where the two ends meet
cross_x = cx(4) + CELL / 2                # between the cells 4 and 5
ax.plot([cross_x, cross_x], [ROW_Y - 0.50, ROW_Y - 0.10],
        linestyle=(0, (4, 3)), linewidth=1.7, color=ORANGE)
ax.text(cross_x, ROW_Y - 0.74, "the pairs cross here", ha="center", va="center",
        fontsize=12.5, color=ORANGE)
ax.text(cross_x, ROW_Y - 1.04, "4 and 5 are partners, so\nthe walk up can stop",
        ha="center", va="center", fontsize=11.5, color=ORANGE)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.40, "The factors of 20, and the pairs they make",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_factor_pairs.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
