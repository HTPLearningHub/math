"""Figure 3 - Method 2, why you take the shorter stack.

The source gives a comparison table and the instruction "take the minimum
number of times". A table of exponents does not show *why* the minimum is
the right choice, and taking the maximum instead is the commonest mistake
(it quietly produces the LCM).

Here each prime gets its own group, and inside the group the two numbers get
a stack of tiles: one tile for every time that prime appears. The tiles that
*both* stacks reach are green, and the tiles above that line are drawn
hollow, because only one of the two numbers has them. A dashed line marks
the height both stacks reach, so "take the minimum" becomes "take the green
height", which is something the reader can see rather than remember.

The pair 24 and 108 was chosen because each number is the shorter one once:
108 wins the prime 2 and 24 wins the prime 3. Neither number is simply "the
small one".

Run with:  python figures/fig_03_min_powers_24_108.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"             # comes from 24
ORANGE = "#E67E22"           # comes from 108
GREEN = "#1E8449"            # a tile both numbers have - what the GCF takes
PURPLE = "#8E44AD"           # the exponent form, as in Chapter 10
GREY = "#78909C"
INK = "#212121"

W, H = 10.20, 6.58
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

TW, TH = 1.05, 0.62          # one tile
TGAP = 0.10                  # space between stacked tiles
COLGAP = 0.16                # space between the two columns of a group
GROUPGAP = 1.70              # space between two prime groups
BASE = 2.85                  # the floor every stack stands on

# prime, how many times it is in 24, how many times it is in 108
GROUPS = [(2, 3, 2), (3, 1, 3)]

GW = 2 * TW + COLGAP                                   # width of one group
TOTAL = len(GROUPS) * GW + (len(GROUPS) - 1) * GROUPGAP
LEFT = (W - TOTAL) / 2


def stack(x, count, shared, colour, fill, prime):
    """Draw one column of tiles. The bottom `shared` of them are green."""
    for k in range(count):
        y = BASE + k * (TH + TGAP)
        if k < shared:
            ax.add_patch(FancyBboxPatch((x, y), TW, TH,
                                        boxstyle="round,pad=0.02,rounding_size=0.10",
                                        facecolor="#E8F5EC", edgecolor=GREEN,
                                        linewidth=2.0))
            ax.text(x + TW / 2, y + TH / 2, str(prime), ha="center", va="center",
                    fontsize=19, color=GREEN, fontweight="bold")
        else:                                  # only this number owns this tile
            ax.add_patch(FancyBboxPatch((x, y), TW, TH,
                                        boxstyle="round,pad=0.02,rounding_size=0.10",
                                        facecolor="white", edgecolor=colour,
                                        linewidth=1.4, linestyle=(0, (3, 3))))
            ax.text(x + TW / 2, y + TH / 2, str(prime), ha="center", va="center",
                    fontsize=19, color=colour)


for g, (prime, c24, c108) in enumerate(GROUPS):
    gx = LEFT + g * (GW + GROUPGAP)
    keep = min(c24, c108)

    # ------------------------------------------------ the heading of the group
    ax.text(gx + GW / 2, 5.38, f"how many {prime}'s?", ha="center", va="center",
            fontsize=15, color=INK, fontweight="bold")

    stack(gx, c24, keep, BLUE, "#E9F2FC", prime)
    stack(gx + TW + COLGAP, c108, keep, ORANGE, "#FDF0E3", prime)

    # ------------------------- the line both stacks reach, and what it is called
    ytop = BASE + keep * (TH + TGAP) - TGAP / 2
    ax.plot([gx - 0.30, gx + GW + 0.30], [ytop, ytop], color=GREEN,
            linewidth=1.6, linestyle=(0, (5, 3)), zorder=3)
    ax.text(gx + GW + 0.36, ytop, "both\nreach here", ha="left", va="center",
            fontsize=11, color=GREEN)

    # ------------------------------ what each column is, and how tall it stands
    for x, count, colour, who in ((gx, c24, BLUE, "24"),
                                  (gx + TW + COLGAP, c108, ORANGE, "108")):
        ax.text(x + TW / 2, BASE - 0.28, f"in {who}", ha="center", va="center",
                fontsize=13, color=colour, fontweight="bold")
        word = "time" if count == 1 else "times"        # "1 time", not "1 times"
        ax.text(x + TW / 2, BASE - 0.58, f"{count} {word}", ha="center",
                va="center", fontsize=12, color=GREY)

    # ---------------------------------------------- what this group contributes
    ax.add_patch(FancyBboxPatch((gx, BASE - 1.62), GW, 0.72,
                                boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor="#E8F5EC", edgecolor=GREEN,
                                linewidth=2.0))
    ax.text(gx + GW / 2, BASE - 1.26, rf"take ${prime}^{{{keep}}}$",
            ha="center", va="center", fontsize=18, color=GREEN,
            fontweight="bold")

# -------------------------------------------------------- the answer at the foot
ax.text(W / 2, 0.40, r"$\mathrm{GCF}(24,\, 108) = 2^{2} \times 3 = 4 \times 3 = 12$",
        ha="center", va="center", fontsize=21, color=PURPLE)

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.40,
        r"$24 = 2^{3} \times 3$   and   $108 = 2^{2} \times 3^{3}$",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.86,
        "for each prime, keep the shorter stack - a hollow tile is one that only "
        "one number has",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_min_powers_24_108.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
