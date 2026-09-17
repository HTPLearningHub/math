"""Figure 4 - why the data has to be put in order before you look for a middle.

The same five numbers twice. In the upper row they are in the order they were
written down, and the card that happens to sit in the middle of the LIST is
10. In the lower row they have been sorted, and the card in the middle of the
ORDER is 5.

Both rows hold exactly the same five values, so the reader can see that
sorting did not change the data - it only changed which card the middle
position points at. That is the whole reason the rule says "order first".

The wrong card is red and crossed through; the right one is green. Red is the
book's colour for a wrong answer and is used here for nothing else.

Run with:  python figures/fig_04_order_first.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"
RED = "#C0392B"           # the wrong answer
GREEN = "#1E8449"         # the right answer
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_RED = "#FCEAE8"
TINT_GREEN = "#E8F5EC"

AS_WRITTEN = [7, 2, 10, 3, 5]
IN_ORDER = [2, 3, 5, 7, 10]

W, H = 13.20, 6.90
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

SLOT = 1.55
CARD_W, CARD_H = 1.24, 1.16
START = (W - 5 * SLOT) / 2 - 1.55     # pushed left to leave room for the note


def draw_row(values, base, hot_index, hot_edge, hot_face):
    """Draw five cards; the card at hot_index gets its own colour."""
    for i, v in enumerate(values):
        cx = START + i * SLOT + SLOT / 2
        hot = i == hot_index
        ax.add_patch(FancyBboxPatch(
            (cx - CARD_W / 2, base), CARD_W, CARD_H,
            boxstyle="round,pad=0,rounding_size=0.14",
            facecolor=hot_face if hot else TINT_BLUE,
            edgecolor=hot_edge if hot else BLUE,
            linewidth=3.2 if hot else 2.0, zorder=3))
        ax.text(cx, base + CARD_H / 2, str(v), ha="center", va="center",
                fontsize=22, color=hot_edge if hot else BLUE,
                fontweight="bold", zorder=6)
        ax.text(cx, base - 0.32, f"{i + 1}", ha="center", va="center",
                fontsize=12, color=GREY, zorder=4)
    return START + hot_index * SLOT + SLOT / 2


# ------------------------------------------------------- the list as written
BASE_A = 4.10
hot_a = draw_row(AS_WRITTEN, BASE_A, 2, RED, TINT_RED)
ax.text(START, BASE_A + CARD_H + 0.50, "the numbers as they were written down",
        ha="left", va="center", fontsize=16, color=INK, fontweight="bold")
# a cross through the wrong card
ax.plot([hot_a - CARD_W / 2 + 0.16, hot_a + CARD_W / 2 - 0.16],
        [BASE_A + 0.16, BASE_A + CARD_H - 0.16], color=RED, linewidth=2.2,
        alpha=0.8, zorder=5)
ax.plot([hot_a - CARD_W / 2 + 0.16, hot_a + CARD_W / 2 - 0.16],
        [BASE_A + CARD_H - 0.16, BASE_A + 0.16], color=RED, linewidth=2.2,
        alpha=0.8, zorder=5)
ax.text(START + 5 * SLOT + 0.35, BASE_A + CARD_H / 2,
        "the middle of the\nlist is $10$\n\nthis is not the median",
        ha="left", va="center", fontsize=14, color=RED)

# --------------------------------------------------------- put them in order
ax.annotate("", xy=(START + 2.5 * SLOT, BASE_A - 1.15),
            xytext=(START + 2.5 * SLOT, BASE_A - 0.62),
            arrowprops=dict(arrowstyle="-|>", color=GREY, linewidth=2.2))
ax.text(START + 2.5 * SLOT + 0.28, BASE_A - 0.89,
        "put them in order, smallest first", ha="left", va="center",
        fontsize=14, color=GREY)

# ------------------------------------------------------------ the sorted list
BASE_B = 0.69
hot_b = draw_row(IN_ORDER, BASE_B, 2, GREEN, TINT_GREEN)
ax.text(START, BASE_B + CARD_H + 0.50, "the same numbers, in order",
        ha="left", va="center", fontsize=16, color=INK, fontweight="bold")
ax.text(START + 5 * SLOT + 0.35, BASE_B + CARD_H / 2,
        "the middle of the\norder is $5$\n\nmedian $= 5$", ha="left",
        va="center", fontsize=14, color=GREEN)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.36, "Order the data first, or the middle lies",
        ha="center", va="center", fontsize=21, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.76,
        "both rows hold the same five values - sorting changed only which "
        "card the middle position points at",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_04_order_first.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
