"""Figure 2 - Method 1, the two factor lists, with the answer ringed.

The source prints the two lists of factors as text inside a bullet point,
which makes the reader hunt for the matches. Drawing them as two rows of
tiles in shared columns puts each shared factor directly above its twin, so
the eye finds 1, 2, 3 and 6 without reading anything.

A column where only one of the two numbers has a factor is left as an empty
dashed slot rather than closed up. That is the whole point of the picture:
24 has factors at 4, 8, 12 and 24 where 18 has nothing, and those are the
columns that cannot win.

Run with:  python figures/fig_02_two_factor_lists_18_24.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"             # factors of 18
ORANGE = "#E67E22"           # factors of 24
GREEN = "#1E8449"            # a factor of both
GREY = "#78909C"
INK = "#212121"

W, H = 13.40, 4.75
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CW, CH, GAP = 0.94, 0.78, 0.13             # tile width, tile height, space between
LEFT = 2.55                                # left edge of the first tile

F18 = [1, 2, 3, 6, 9, 18]
F24 = [1, 2, 3, 4, 6, 8, 12, 24]
COLS = sorted(set(F18) | set(F24))         # every number that is a factor of either
COMMON = sorted(set(F18) & set(F24))       # 1, 2, 3, 6

Y18 = 2.72                                 # bottom edge of the row for 18
Y24 = 1.42                                 # bottom edge of the row for 24


def draw_row(values, y, colour, fill, title, subtitle):
    """Draw one row. Every column of COLS gets a tile or an empty dashed slot."""
    ax.text(LEFT - 0.32, y + CH / 2 + 0.17, title, ha="right", va="center",
            fontsize=16, color=colour, fontweight="bold")
    ax.text(LEFT - 0.32, y + CH / 2 - 0.20, subtitle, ha="right", va="center",
            fontsize=12, color=GREY)

    for i, v in enumerate(COLS):
        x = LEFT + i * (CW + GAP)
        if v not in values:                            # this number is not a factor
            ax.add_patch(FancyBboxPatch((x, y), CW, CH,
                                        boxstyle="round,pad=0.02,rounding_size=0.11",
                                        facecolor="white", edgecolor="#CFD8DC",
                                        linewidth=1.2, linestyle=(0, (3, 3))))
            continue
        shared = v in COMMON
        ax.add_patch(FancyBboxPatch((x, y), CW, CH,
                                    boxstyle="round,pad=0.02,rounding_size=0.11",
                                    facecolor="#E8F5EC" if shared else fill,
                                    edgecolor=GREEN if shared else colour,
                                    linewidth=2.4 if shared else 1.6))
        ax.text(x + CW / 2, y + CH / 2, str(v), ha="center", va="center",
                fontsize=19 if shared else 17,
                color=GREEN if shared else colour,
                fontweight="bold" if shared else "normal")


draw_row(F18, Y18, BLUE, "#E9F2FC", "factors of 18", "six of them")
draw_row(F24, Y24, ORANGE, "#FDF0E3", "factors of 24", "eight of them")

# ----------------------- a dashed green column joining every factor they share
for v in COMMON:
    x = LEFT + COLS.index(v) * (CW + GAP) + CW / 2
    ax.plot([x, x], [Y24, Y18 + CH], color=GREEN, linewidth=1.4,
            linestyle=(0, (4, 3)), zorder=0)

# ------------------------------------------- the two labels under the two rows
x1 = LEFT + COLS.index(1) * (CW + GAP) + CW / 2
x6 = LEFT + COLS.index(6) * (CW + GAP) + CW / 2

ax.plot([x1, x1], [Y24 - 0.12, Y24 - 0.50], color=GREY, linewidth=1.6)
ax.text(x1, Y24 - 0.80, "always shared", ha="center", va="center",
        fontsize=13, color=GREY)
ax.text(x1, Y24 - 1.12, "1 divides every number", ha="center", va="center",
        fontsize=12, color=GREY)

ax.plot([x6, x6], [Y24 - 0.12, Y24 - 0.50], color=GREEN, linewidth=1.8)
ax.text(x6, Y24 - 0.80, "the greatest", ha="center", va="center",
        fontsize=15, color=GREEN, fontweight="bold")
ax.text(x6, Y24 - 1.12, "common factor", ha="center", va="center",
        fontsize=15, color=GREEN, fontweight="bold")

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.40, "The factors of 18 and the factors of 24",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.84,
        "four numbers are in both rows; the last one is the answer - "
        "an empty slot means that number is not a factor",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_two_factor_lists_18_24.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
