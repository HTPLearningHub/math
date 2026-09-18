"""Figure 4 - why adding is safe and multiplying by a negative is not.

This is the most important figure in the chapter. The source states the
flipping rule and gives one numerical example of it, but it never shows
why its neighbour - adding the same number to both sides - needs no flip.
The reason is visible and needs no words: the two arrows.

Left panel:  add 5 to both sides.      1 -> 6 and 2 -> 7.
             The two arrows are parallel. Nothing overtakes anything.
Right panel: multiply both sides by -1. 1 -> -1 and 2 -> -2.
             The two arrows cross. The order has been reversed.

"The arrows cross" and "the symbol must turn round" are the same fact.

Each panel carries its own scale, because the two operations move the
numbers different distances; the panels are the same width on the page,
so the geometry of the arrows is what the eye compares, not the spacing
of the ticks. The scale of each panel is printed on it.

Horizontal plan (x): panels 0.40-6.35 and 6.65-12.60. Inside the left
panel the axis runs 0 to 8 across 0.95-5.80; inside the right panel it
runs -3 to 3 across 7.20-12.05. Both axes are 4.85 wide.

Vertical plan (y, top to bottom):
    6.50  figure heading
    6.05  top of both panels
    5.62  the operation being done
    4.95  the statement we start from
    4.32  the "before" number line
    3.98  the numbers under it
    3.30  the one arrow label per panel (arrows run 4.12 -> 2.57)
    2.35  the "after" number line
    2.01  the numbers under it
    1.35  the statement we end with
    0.72  the verdict
    0.45  bottom of both panels
    0.14  closing note

Run with:  python figures/fig_04_slide_or_turn_round.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # the numbers as they started
ORANGE = "#E67E22"        # the operation, and where it sends them
GREEN = "#1E8449"         # the true statement at the end
RED = "#C0392B"           # the statement that would be false
GREY = "#78909C"
INK = "#212121"
BLUE_T = "#E9F2FC"
GREEN_T = "#E8F5EC"
GREY_T = "#ECEFF1"

W, H = 13.00, 6.90
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

Y_BEFORE = 4.32           # the upper number line in both panels
Y_AFTER = 2.35            # the lower number line in both panels


def make_scale(x_left, x_right, v_low, v_high):
    """Return a function mapping a number to a position inside one panel."""
    def px(value):
        return x_left + (x_right - x_left) * (value - v_low) / (v_high - v_low)
    return px


def panel_box(x_left, x_right, colour):
    """The rounded background of one panel."""
    ax.add_patch(FancyBboxPatch(
        (x_left, 0.45), x_right - x_left, 5.60,
        boxstyle="round,pad=0.0,rounding_size=0.18",
        facecolor="white", edgecolor=colour, linewidth=1.8, zorder=0))


def axis(px, y, v_low, v_high, marked, colour):
    """One number line, with the marked numbers drawn as coloured dots."""
    ax.annotate("", xy=(px(v_high) + 0.28, y), xytext=(px(v_low) - 0.28, y),
                arrowprops=dict(arrowstyle="<|-|>", linewidth=1.6,
                                color=INK), zorder=1)
    for value in range(int(v_low), int(v_high) + 1):
        ax.plot([px(value), px(value)], [y - 0.09, y + 0.09],
                linewidth=1.4, color=INK, zorder=1)
        if value not in marked:
            ax.text(px(value), y - 0.34, str(value), ha="center",
                    va="center", fontsize=10.5, color=GREY)
    for value in marked:
        ax.plot([px(value)], [y], marker="o", markersize=13, color=colour,
                zorder=5)
        ax.text(px(value), y - 0.34, str(value), ha="center", va="center",
                fontsize=12.5, color=colour, fontweight="bold")


def card(x, y, text, edge, fill, fontsize=20):
    """A rounded box carrying one statement."""
    ax.text(x, y, text, ha="center", va="center", fontsize=fontsize,
            color=INK, zorder=3,
            bbox=dict(boxstyle="round,pad=0.38", facecolor=fill,
                      edgecolor=edge, linewidth=1.7))


def move(x_from, x_to):
    """One thick arrow from the upper line down to the lower line."""
    ax.add_patch(FancyArrowPatch(
        (x_from, Y_BEFORE - 0.20), (x_to, Y_AFTER + 0.22),
        arrowstyle="-|>", mutation_scale=22, linewidth=3.2,
        color=ORANGE, shrinkA=0, shrinkB=0, zorder=4))


ax.text(0.40, 6.50,
        "one of these operations keeps the order of the two numbers, "
        "and one reverses it",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# ============================================================ left panel
panel_box(0.40, 6.35, BLUE)
L = make_scale(0.95, 5.80, 0.0, 8.0)

ax.text(3.37, 5.62, "add $5$ to both sides", ha="center", va="center",
        fontsize=17, color=INK, fontweight="bold")
card(3.37, 4.95, r"$1 < 2$", BLUE, BLUE_T)
axis(L, Y_BEFORE, 0, 8, (1, 2), BLUE)

move(L(1), L(6))
move(L(2), L(7))
# the label sits left of both arrow paths, and clear of the tick numbers
ax.text(1.70, 3.30, r"$+5$ on both", ha="center", va="center", fontsize=15,
        color=ORANGE, fontweight="bold")

axis(L, Y_AFTER, 0, 8, (6, 7), BLUE)
card(3.37, 1.35, r"$6 < 7$", GREEN, GREEN_T)
ax.text(3.37, 0.72, "the arrows are parallel - the order is kept",
        ha="center", va="center", fontsize=13.5, color=GREEN,
        fontweight="bold")

# =========================================================== right panel
panel_box(6.65, 12.60, ORANGE)
R = make_scale(7.20, 12.05, -3.0, 3.0)

ax.text(9.62, 5.62, r"multiply both sides by $-1$", ha="center",
        va="center", fontsize=17, color=INK, fontweight="bold")
card(9.62, 4.95, r"$1 < 2$", BLUE, BLUE_T)
axis(R, Y_BEFORE, -3, 3, (1, 2), BLUE)

move(R(1), R(-1))
move(R(2), R(-2))
# left of the point where the arrows cross, so the crossing stays clear
ax.text(8.15, 3.30, r"$\times (-1)$ on both", ha="center", va="center",
        fontsize=15, color=ORANGE, fontweight="bold")

axis(R, Y_AFTER, -3, 3, (-1, -2), ORANGE)

# the statement most readers write first, and why it cannot stand
ax.text(8.30, 1.35, r"$-1 < -2$", ha="center", va="center", fontsize=17,
        color=RED)
ax.plot([7.76, 8.84], [1.35, 1.35], linewidth=2.4, color=RED, zorder=4)
card(10.95, 1.35, r"$-1 > -2$", GREEN, GREEN_T, fontsize=17)

ax.text(9.62, 0.72, "the arrows cross - the order is reversed",
        ha="center", va="center", fontsize=13.5, color=ORANGE,
        fontweight="bold")

ax.text(0.40, 0.14,
        "the scales of the two panels are different, because the two "
        "operations move the numbers different distances; "
        "what to compare is the pair of arrows",
        ha="left", va="center", fontsize=12, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_slide_or_turn_round.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_04_slide_or_turn_round.png")
