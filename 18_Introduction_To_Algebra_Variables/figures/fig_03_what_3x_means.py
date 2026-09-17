"""Figure 3 - what 3x means, and the two things it does not mean.

The green half shows the truth: 3x is three copies of x laid end to end, so
when x = 4 it is 4 + 4 + 4 = 12.

The red half shows the two readings people invent. Reading the 3 and the x as
an addition gives 7. Gluing the digits together gives 34. Both are crossed
through, and the true value 12 is printed under them so the size of the error
is visible.

Red is used only for the wrong readings, as in Chapter 17's fig_04.

Run with:  python figures/fig_03_what_3x_means.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

BLUE = "#2E86DE"          # the variable x
GREEN = "#1E8449"         # the correct reading
RED = "#C0392B"           # the wrong readings
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_GREEN = "#E8F5EC"
TINT_RED = "#FCEAE8"

W, H = 12.80, 6.00
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# ------------------------------------------------------------ the top heading
ax.text(W / 2, H - 0.40, r"$3x$   when   $x = 4$", ha="center", va="center",
        fontsize=26, color=INK, fontweight="bold")

# ============================================================== the green side
ax.text(3.30, H - 1.20, "what it means", ha="center", va="center",
        fontsize=20, color=GREEN, fontweight="bold")

# three copies of x, drawn as three equal blue blocks side by side
BLOCK_W, BLOCK_H = 1.45, 0.90
Y_BLOCKS = 3.35
GAP = 0.40                             # room for the plus signs
START = 3.30 - (3 * BLOCK_W + 2 * GAP) / 2
for i in range(3):
    x = START + i * (BLOCK_W + GAP)
    ax.add_patch(Rectangle((x, Y_BLOCKS), BLOCK_W, BLOCK_H,
                           facecolor=TINT_BLUE, edgecolor=BLUE,
                           linewidth=2.2, zorder=3))
    ax.text(x + BLOCK_W / 2, Y_BLOCKS + BLOCK_H / 2, r"$x$", ha="center",
            va="center", fontsize=23, color=BLUE, zorder=4)
    ax.text(x + BLOCK_W / 2, Y_BLOCKS - 0.34, r"$4$", ha="center",
            va="center", fontsize=18, color=GREY, zorder=4)
    if i < 2:
        ax.text(x + BLOCK_W + GAP / 2, Y_BLOCKS + BLOCK_H / 2, r"$+$",
                ha="center", va="center", fontsize=20, color=GREY, zorder=5)

ax.text(3.30, Y_BLOCKS - 1.05, r"$4 + 4 + 4$", ha="center", va="center",
        fontsize=22, color=INK)
ax.add_patch(FancyBboxPatch((3.30 - 0.95, Y_BLOCKS - 2.10), 1.90, 0.80,
                            boxstyle="round,pad=0.05,rounding_size=0.14",
                            facecolor=TINT_GREEN, edgecolor=GREEN,
                            linewidth=2.4, zorder=3))
ax.text(3.30, Y_BLOCKS - 1.70, r"$12$", ha="center", va="center",
        fontsize=26, color=GREEN, fontweight="bold", zorder=4)

# the divider
ax.plot([6.55, 6.55], [0.55, H - 0.95], color=GREY, linewidth=1.3,
        linestyle=(0, (4, 4)), zorder=1)

# ================================================================ the red side
ax.text(9.65, H - 1.20, "what it does not mean", ha="center", va="center",
        fontsize=20, color=RED, fontweight="bold")

# the third number is half the width of the stroke, so each stroke matches
# the width of the wrong answer it crosses out
WRONG = [(r"$3 + 4 = 7$", "adding instead of multiplying", 1.00),
         (r"$34$", "gluing the two digits together", 0.48)]
Y_WRONG = [3.90, 2.20]
for (text, why, half), y in zip(WRONG, Y_WRONG):
    ax.add_patch(FancyBboxPatch((9.65 - 1.70, y - 0.42), 3.40, 0.84,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=TINT_RED, edgecolor=RED,
                                linewidth=2.2, zorder=3))
    ax.text(9.65, y, text, ha="center", va="center", fontsize=23, color=RED,
            zorder=4)
    # one stroke through the wrong answer
    ax.plot([9.65 - half, 9.65 + half], [y - 0.13, y + 0.13], color=RED,
            linewidth=2.2, zorder=5)
    ax.text(9.65, y - 0.68, why, ha="center", va="center", fontsize=14,
            color=GREY)

ax.text(9.65, 1.05, "a number beside a letter is always a multiplication",
        ha="center", va="center", fontsize=14.5, color=RED, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_what_3x_means.png", dpi=170, facecolor="white")
print("saved", out / "fig_03_what_3x_means.png")
