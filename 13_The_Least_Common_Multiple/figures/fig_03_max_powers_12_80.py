"""Figure 3 - Method 2, why you take the taller stack.

The source gives a comparison table and the instruction "take the maximum
number of times". A table of exponents does not show *why* the maximum is
the right choice, and taking the minimum instead is the commonest mistake.

Here each prime gets its own group, and inside the group the two numbers get
a stack of tiles: one tile for every time that prime appears. The stacks
stand side by side, so "take the maximum" becomes "take the taller stack",
which is something the reader can see rather than remember. A prime that is
missing from a number gets an empty dashed tile, so zero is drawn too.
Run with:  python figures/fig_03_max_powers_12_80.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"             # comes from 12
ORANGE = "#E67E22"           # comes from 80
GREEN = "#1E8449"            # what the LCM takes
PURPLE = "#8E44AD"           # the exponent form, as in Chapter 10
GREY = "#78909C"
INK = "#212121"

W, H = 10.60, 7.10
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

TW, TH = 1.05, 0.62          # one tile
TGAP = 0.10                  # space between stacked tiles
COLGAP = 0.16                # space between the two columns of a group
GROUPGAP = 1.00              # space between two prime groups
BASE = 2.60                  # the floor every stack stands on

# prime, how many times it is in 12, how many times it is in 80
GROUPS = [(2, 2, 4), (3, 1, 0), (5, 0, 1)]

GW = 2 * TW + COLGAP                                   # width of one group
TOTAL = len(GROUPS) * GW + (len(GROUPS) - 1) * GROUPGAP
LEFT = (W - TOTAL) / 2


def stack(x, count, colour, fill, prime):
    """Draw one column of `count` tiles standing on BASE. Zero gets a ghost."""
    if count == 0:
        ax.add_patch(FancyBboxPatch((x, BASE), TW, TH,
                                    boxstyle="round,pad=0.02,rounding_size=0.10",
                                    facecolor="white", edgecolor=GREY,
                                    linewidth=1.4, linestyle=(0, (3, 3))))
        ax.text(x + TW / 2, BASE + TH / 2, "none", ha="center", va="center",
                fontsize=13, color=GREY)
        return
    for k in range(count):
        y = BASE + k * (TH + TGAP)
        ax.add_patch(FancyBboxPatch((x, y), TW, TH,
                                    boxstyle="round,pad=0.02,rounding_size=0.10",
                                    facecolor=fill, edgecolor=colour,
                                    linewidth=1.8))
        ax.text(x + TW / 2, y + TH / 2, str(prime), ha="center", va="center",
                fontsize=19, color=colour, fontweight="bold")


for g, (prime, c12, c80) in enumerate(GROUPS):
    gx = LEFT + g * (GW + GROUPGAP)

    # ------------------------------------------------ the heading of the group
    ax.text(gx + GW / 2, 5.95, f"how many {prime}'s?", ha="center", va="center",
            fontsize=15, color=INK, fontweight="bold")

    stack(gx, c12, BLUE, "#E9F2FC", prime)
    stack(gx + TW + COLGAP, c80, ORANGE, "#FDF0E3", prime)

    # ------------------------------------------- what each column is, and its count
    for x, count, colour, who in ((gx, c12, BLUE, "12"),
                                  (gx + TW + COLGAP, c80, ORANGE, "80")):
        ax.text(x + TW / 2, BASE - 0.28, f"in {who}", ha="center", va="center",
                fontsize=13, color=colour, fontweight="bold")
        word = "time" if count == 1 else "times"        # "1 time", not "1 times"
        ax.text(x + TW / 2, BASE - 0.58, f"{count} {word}", ha="center",
                va="center", fontsize=12, color=GREY)

    # ------------------------------------------------ the winner of the group
    best = max(c12, c80)
    ax.add_patch(FancyBboxPatch((gx, BASE - 1.62), GW, 0.72,
                                boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor="#E8F5EC", edgecolor=GREEN,
                                linewidth=2.0))
    ax.text(gx + GW / 2, BASE - 1.26, rf"take ${prime}^{{{best}}}$",
            ha="center", va="center", fontsize=18, color=GREEN,
            fontweight="bold")

# -------------------------------------------------------- the answer at the foot
ax.text(W / 2, 0.66, r"$\mathrm{LCM}(12,\, 80) = 2^{4} \times 3 \times 5"
                     r" = 16 \times 15 = 240$",
        ha="center", va="center", fontsize=21, color=PURPLE)

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.40, r"$12 = 2^{2} \times 3$   and   $80 = 2^{4} \times 5$",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.86, "for each prime, keep the taller stack - never the shorter one",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_max_powers_12_80.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
