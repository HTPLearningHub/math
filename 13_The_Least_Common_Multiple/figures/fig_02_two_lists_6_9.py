"""Figure 2 - Method 1, the two lists, with the answer ringed.

The source prints the two lists of multiples as bold text inside a sentence,
which makes the reader hunt for the matches. Drawing them as two rows of
tiles puts the shared numbers in the same columns, so the eye finds 18, 36
and 54 without reading anything.

The figure also carries the chapter's first warning: 54 is 6 x 9, it really
is in both rows, and it is still the wrong answer. It is drawn green like
the other shared numbers and labelled, so the reader sees that "common" and
"least" are two different words.
Run with:  python figures/fig_02_two_lists_6_9.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"             # multiples of 6
ORANGE = "#E67E22"           # multiples of 9
GREEN = "#1E8449"            # a number in both rows
GREY = "#78909C"
INK = "#212121"

W, H = 12.60, 4.95
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CW, CH, GAP = 0.94, 0.78, 0.13             # tile width, tile height, space between
LEFT = 2.30                                # left edge of the first tile
SLOTS = 9                                  # how many tile positions each row has

MULT_6 = [6 * i for i in range(1, SLOTS + 1)]           # 6 .. 54
MULT_9 = [9 * i for i in range(1, 7)]                   # 9 .. 54
COMMON = sorted(set(MULT_6) & set(MULT_9))              # 18, 36, 54

Y6 = 2.95                                  # bottom edge of the row of 6's
Y9 = 1.65                                  # bottom edge of the row of 9's


def draw_row(values, y, colour, title, subtitle):
    """Draw one row of tiles. A value in both lists is drawn green."""
    ax.text(LEFT - 0.30, y + CH / 2 + 0.17, title, ha="right", va="center",
            fontsize=16, color=colour, fontweight="bold")
    ax.text(LEFT - 0.30, y + CH / 2 - 0.20, subtitle, ha="right", va="center",
            fontsize=12, color=GREY)
    for i, v in enumerate(values):
        x = LEFT + i * (CW + GAP)
        shared = v in COMMON
        ax.add_patch(FancyBboxPatch((x, y), CW, CH,
                                    boxstyle="round,pad=0.02,rounding_size=0.11",
                                    facecolor="#E8F5EC" if shared else "white",
                                    edgecolor=GREEN if shared else colour,
                                    linewidth=2.4 if shared else 1.6))
        ax.text(x + CW / 2, y + CH / 2, str(v), ha="center", va="center",
                fontsize=19 if shared else 17,
                color=GREEN if shared else colour,
                fontweight="bold" if shared else "normal")
    # the three dots that say the list never stops
    ax.text(LEFT + len(values) * (CW + GAP) + 0.16, y + CH / 2, r"$\dots$",
            ha="left", va="center", fontsize=20, color=GREY)


draw_row(MULT_6, Y6, BLUE, "multiples of 6", "count in sixes")

# the row of 9's is drawn into the same columns as the row of 6's, so that a
# shared number sits directly under its twin
ax.text(LEFT - 0.30, Y9 + CH / 2 + 0.17, "multiples of 9", ha="right",
        va="center", fontsize=16, color=ORANGE, fontweight="bold")
ax.text(LEFT - 0.30, Y9 + CH / 2 - 0.20, "count in nines", ha="right",
        va="center", fontsize=12, color=GREY)
for v in MULT_9:
    slot = MULT_6.index(v) if v in MULT_6 else (v / 6) - 1   # 9, 27 and 45 sit between
    x = LEFT + slot * (CW + GAP)
    shared = v in COMMON
    ax.add_patch(FancyBboxPatch((x, Y9), CW, CH,
                                boxstyle="round,pad=0.02,rounding_size=0.11",
                                facecolor="#E8F5EC" if shared else "white",
                                edgecolor=GREEN if shared else ORANGE,
                                linewidth=2.4 if shared else 1.6))
    ax.text(x + CW / 2, Y9 + CH / 2, str(v), ha="center", va="center",
            fontsize=19 if shared else 17,
            color=GREEN if shared else ORANGE,
            fontweight="bold" if shared else "normal")
ax.text(LEFT + SLOTS * (CW + GAP) + 0.16, Y9 + CH / 2, r"$\dots$",
        ha="left", va="center", fontsize=20, color=GREY)

# --------------------------- a green column behind each number that is shared
for v in COMMON:
    x = LEFT + MULT_6.index(v) * (CW + GAP)
    ax.plot([x + CW / 2, x + CW / 2], [Y9, Y6 + CH], color=GREEN,
            linewidth=1.4, linestyle=(0, (4, 3)), zorder=0)

# --------------------------------------------- the two labels under the tiles
x18 = LEFT + MULT_6.index(18) * (CW + GAP) + CW / 2
x54 = LEFT + MULT_6.index(54) * (CW + GAP) + CW / 2

ax.plot([x18, x18], [Y9 - 0.12, Y9 - 0.52], color=GREEN, linewidth=1.6)
ax.text(x18, Y9 - 0.82, "the least", ha="center", va="center",
        fontsize=15, color=GREEN, fontweight="bold")
ax.text(x18, Y9 - 1.16, "common multiple", ha="center", va="center",
        fontsize=15, color=GREEN, fontweight="bold")

ax.plot([x54, x54], [Y9 - 0.12, Y9 - 0.52], color=GREY, linewidth=1.6)
ax.text(x54, Y9 - 0.82, r"$6 \times 9 = 54$", ha="center", va="center",
        fontsize=15, color=GREY)
ax.text(x54, Y9 - 1.16, "common, but not the least", ha="center", va="center",
        fontsize=13, color=GREY)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.40, "The multiples of 6 and the multiples of 9",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.84, "three numbers are in both rows; the first one is the answer",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_two_lists_6_9.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
