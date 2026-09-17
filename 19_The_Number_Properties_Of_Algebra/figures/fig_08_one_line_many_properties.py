"""Figure 8 - one expression, five lines, and the property behind each line.

The staircase descends from 3(2x + 5) - 4(x - 1) + 0 down to 2x + 19. Every
step down is one permitted move, and the orange pill on the right names it.

Drawn as a staircase rather than a list so that the reader sees the work
shrinking: each line is shorter than the one above it, and the last line is
the shortest expression that still means the same thing.

The rows are 1.15 apart and the cards are 0.72 tall, which leaves a gap of
0.43 between two cards. The small step arrow is drawn in that gap. With the
rows any closer the cards touch and the arrow disappears behind them.

Vertical plan (y, one row per line, from the top):
    6.45  heading
    5.50  line 1  3(2x + 5) - 4(x - 1) + 0
    4.35  line 2  3(2x + 5) - 4(x - 1)          additive identity
    3.20  line 3  6x + 15 - 4x + 4              distributive property
    2.05  line 4  (6x - 4x) + (15 + 4)          commutative, associative
    0.90  line 5  2x + 19                       like terms collected
    0.18  the closing note

Run with:  python figures/fig_08_one_line_many_properties.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"        # the name of the move being made
GREEN = "#1E8449"         # the finished line
GREY = "#78909C"
INK = "#212121"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"
TINT_GREY = "#ECEFF1"

W, H = 12.80, 6.90
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.40, 6.45, "one expression, and the property behind every step",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

CARD_H = 0.72
PILL_X, PILL_W = 8.10, 4.25   # every pill starts here, so they line up

# (maths, y, left edge of its card, card width, property name or None)
LINES = [
    (r"$3(2x + 5) - 4(x - 1) + 0$", 5.50, 0.45, 5.35, None),
    (r"$3(2x + 5) - 4(x - 1)$", 4.35, 0.95, 4.60, "additive identity"),
    (r"$6x + 15 - 4x + 4$", 3.20, 1.45, 3.90, "distributive property"),
    (r"$(6x - 4x) + (15 + 4)$", 2.05, 1.95, 4.20, "commutative, associative"),
    (r"$2x + 19$", 0.90, 2.45, 2.35, "like terms collected"),
]

for i, (maths, y, x0, w, prop) in enumerate(LINES):
    last = (i == len(LINES) - 1)
    ax.add_patch(FancyBboxPatch((x0, y - CARD_H / 2), w, CARD_H,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=TINT_GREEN if last else TINT_GREY,
                                edgecolor=GREEN if last else GREY,
                                linewidth=2.4 if last else 2.0, zorder=3))
    ax.text(x0 + w / 2, y, maths, ha="center", va="center", fontsize=23,
            color=INK, zorder=4)

    if prop is not None:
        # the step down, drawn in the clear gap between two cards
        ax.add_patch(FancyArrowPatch((x0 + 0.45, y + 0.80),
                                     (x0 + 0.45, y + 0.44),
                                     arrowstyle="-|>", mutation_scale=17,
                                     linewidth=2.2, color=ORANGE, zorder=5))
        ax.add_patch(FancyBboxPatch((PILL_X, y - 0.28), PILL_W, 0.56,
                                    boxstyle="round,pad=0.04,"
                                             "rounding_size=0.26",
                                    facecolor=TINT_ORANGE, edgecolor=ORANGE,
                                    linewidth=1.8, zorder=3))
        ax.text(PILL_X + PILL_W / 2, y, prop, ha="center", va="center",
                fontsize=16, color=ORANGE, zorder=4)

ax.text(0.40, 0.18, "every line below the first is a different way of writing "
        "the first one", ha="left", va="center", fontsize=15, color=GREY,
        style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_08_one_line_many_properties.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_08_one_line_many_properties.png")
