"""Figure 5 - terms can only be counted together when they count the same thing.

Left panel: 6x - 4x. Six identical blue blocks, each one worth x. Four of them
are taken away (drawn hollow and dashed), and two blocks are left, so the
answer is 2x. Nothing had to be known about x for that to work.

Right panel: 2x + 3. Two blue blocks worth x and three small orange squares
worth 1 each. They are not the same object, so there is no single count. The
two wrong answers, 5x and 5, are struck through.

Vertical plan (y, from the top):
    4.95  the two panel headings
    3.20  the bottom edge of the row of blocks (they are 0.95 tall)
    2.80  the labels under the blocks
    2.10  the line of maths, or "there is no single count"
    1.15  the answer, or the two struck-out wrong answers
    0.30  the note under each panel

Both headings are kept short so that neither reaches the dashed divider at
x = 6.55.

Run with:  python figures/fig_05_like_terms.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

BLUE = "#2E86DE"          # a term carrying the letter x
ORANGE = "#E67E22"        # a plain number
GREEN = "#1E8449"
RED = "#C0392B"
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"
TINT_RED = "#FCEAE8"

W, H = 12.80, 5.40
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

Y_BLOCK = 3.20            # the bottom edge of every block
BH, BW = 0.95, 0.72       # block height and width


def x_block(cx, taken=False):
    """One block worth x. A taken block is hollow with a dashed outline."""
    ax.add_patch(FancyBboxPatch((cx - BW / 2, Y_BLOCK), BW, BH,
                                boxstyle="round,pad=0.02,rounding_size=0.10",
                                facecolor="white" if taken else TINT_BLUE,
                                edgecolor=GREY if taken else BLUE,
                                linewidth=2.0,
                                linestyle=(0, (3, 3)) if taken else "solid",
                                zorder=3))
    ax.text(cx, Y_BLOCK + BH / 2, r"$x$", ha="center", va="center",
            fontsize=22, color=GREY if taken else INK, zorder=4)


def one_square(cx):
    """One small orange square worth 1."""
    s = 0.52
    ax.add_patch(Rectangle((cx - s / 2, Y_BLOCK + (BH - s) / 2), s, s,
                           facecolor=TINT_ORANGE, edgecolor=ORANGE,
                           linewidth=2.0, zorder=3))
    ax.text(cx, Y_BLOCK + BH / 2, r"$1$", ha="center", va="center",
            fontsize=15, color=INK, zorder=4)


def answer_card(cx, w, text, colour, tint, half_stroke=None):
    ax.add_patch(FancyBboxPatch((cx - w / 2, 1.15 - 0.48), w, 0.96,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=tint, edgecolor=colour,
                                linewidth=2.4, zorder=3))
    ax.text(cx, 1.15, text, ha="center", va="center", fontsize=27, color=INK,
            zorder=4)
    if half_stroke is not None:
        # each stroke is as wide as the answer it crosses out, and no wider
        ax.plot([cx - half_stroke, cx + half_stroke], [1.15, 1.15],
                color=colour, linewidth=2.6, zorder=5)


# ------------------------------------------------- left: like terms, joinable
ax.text(3.20, 4.95, "like terms can be joined", ha="center", va="center",
        fontsize=19, color=GREEN, fontweight="bold")

for i in range(6):
    x_block(0.95 + i * 0.92, taken=(i >= 2))
ax.text(4.17, 4.45, "four are taken away", ha="center", va="center",
        fontsize=15, color=GREY)
ax.text(3.25, 2.80, r"$6x$ to start with", ha="center", va="center",
        fontsize=15, color=BLUE)

ax.text(3.20, 2.10, r"$6x - 4x = (6 - 4)\,x$", ha="center", va="center",
        fontsize=26, color=INK)
answer_card(3.20, 2.10, r"$2x$", GREEN, TINT_GREEN)
ax.text(3.20, 0.30, "the letter never changed, only the count", ha="center",
        va="center", fontsize=15, color=GREEN, style="italic")

ax.plot([6.55, 6.55], [0.10, 4.60], color=GREY, linewidth=1.3,
        linestyle=(0, (4, 4)), zorder=1)

# --------------------------------------------- right: unlike terms, stuck
ax.text(9.70, 4.95, "unlike terms cannot", ha="center", va="center",
        fontsize=19, color=RED, fontweight="bold")

for i in range(2):
    x_block(7.55 + i * 0.92)
ax.text(9.30, Y_BLOCK + BH / 2, r"$+$", ha="center", va="center", fontsize=24,
        color=GREY)
for i in range(3):
    one_square(10.00 + i * 0.66)

ax.text(8.01, 2.80, r"$2x$", ha="center", va="center", fontsize=18,
        color=BLUE)
ax.text(10.66, 2.80, r"$3$", ha="center", va="center", fontsize=18,
        color=ORANGE)

ax.text(9.70, 2.10, "there is no single count", ha="center", va="center",
        fontsize=19, color=RED)
answer_card(8.60, 1.60, r"$5x$", RED, TINT_RED, half_stroke=0.44)
answer_card(10.80, 1.60, r"$5$", RED, TINT_RED, half_stroke=0.30)
ax.text(9.70, 0.30, r"$2x + 3$ is already as short as it gets", ha="center",
        va="center", fontsize=15, color=RED, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_05_like_terms.png", dpi=170, facecolor="white",
            bbox_inches="tight")
print("saved", out / "fig_05_like_terms.png")
