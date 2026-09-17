"""Figure 7 - going backwards means undoing the steps in the opposite order.

Top lane: the forward machine of fig_05. 4 goes in, is doubled, has 1 added,
and 9 comes out.

Bottom lane: the same machine walked from right to left. The arrows point the
other way, and each orange box holds the *opposite* operation: take 1 away,
then halve. The order is reversed too, and that is the part readers get
wrong, so the two lanes are drawn one above the other with the operations in
mirrored columns.

Run with:  python figures/fig_07_the_machine_backwards.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # the number of hours you watched
ORANGE = "#E67E22"        # what the rule does
GREEN = "#1E8449"         # the number we know, and the answer found
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"

W, H = 13.00, 5.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

COLS = [1.80, 5.00, 8.30, 11.50]
Y_FWD = 3.85
Y_BACK = 1.40


def box(cx, cy, w, h, text, face, edge, fontsize=22, weight="normal",
        tcolour=INK):
    """One rounded box with centred text."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.06,rounding_size=0.15",
                                facecolor=face, edgecolor=edge,
                                linewidth=2.2, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize,
            color=tcolour, fontweight=weight, zorder=4)


def arrow(x1, x2, y, colour):
    """A horizontal arrow from x1 to x2 - right to left if x2 < x1."""
    ax.add_patch(FancyArrowPatch((x1, y), (x2, y), arrowstyle="-|>",
                                 mutation_scale=19, color=colour,
                                 linewidth=2.1, zorder=2))


# ----------------------------------------------------------- forwards, known
ax.text(0.28, H - 0.40, "forwards: you know your hours",
        ha="left", va="center", fontsize=19, color=GREY, fontweight="bold")
box(COLS[0], Y_FWD, 1.70, 0.92, r"$4$", TINT_BLUE, BLUE, fontsize=25)
box(COLS[1], Y_FWD, 2.35, 0.92, r"$\times\, 2$", TINT_ORANGE, ORANGE)
box(COLS[2], Y_FWD, 2.35, 0.92, r"$+\, 1$", TINT_ORANGE, ORANGE)
box(COLS[3], Y_FWD, 1.70, 0.92, r"$9$", TINT_GREEN, GREEN, fontsize=25)
arrow(COLS[0] + 0.93, COLS[1] - 1.27, Y_FWD, GREY)
arrow(COLS[1] + 1.27, COLS[2] - 1.27, Y_FWD, GREY)
arrow(COLS[2] + 1.27, COLS[3] - 0.93, Y_FWD, GREY)

# ---------------------------------------------------------- backwards, asked
ax.text(0.28, 0.40, "backwards: you know Bobo's hours",
        ha="left", va="center", fontsize=19, color=GREEN, fontweight="bold")
box(COLS[3], Y_BACK, 1.70, 0.92, r"$9$", TINT_GREEN, GREEN, fontsize=25)
box(COLS[2], Y_BACK, 2.35, 0.92, r"$-\, 1$", TINT_ORANGE, ORANGE)
box(COLS[1], Y_BACK, 2.35, 0.92, r"$\div\, 2$", TINT_ORANGE, ORANGE)
box(COLS[0], Y_BACK, 1.70, 0.92, r"$4$", TINT_BLUE, BLUE, fontsize=25,
    weight="bold", tcolour=BLUE)
arrow(COLS[3] - 0.93, COLS[2] + 1.27, Y_BACK, GREEN)
arrow(COLS[2] - 1.27, COLS[1] + 1.27, Y_BACK, GREEN)
arrow(COLS[1] - 1.27, COLS[0] + 0.93, Y_BACK, GREEN)
# the number that sits between the two undoing steps, on the arrow itself
ax.text((COLS[1] + COLS[2]) / 2, Y_BACK + 0.38, r"$8$", ha="center",
        va="center", fontsize=19, color=GREEN, fontweight="bold")

# the two pairs of matching boxes, joined so the undoing is visible
for c in (COLS[1], COLS[2]):
    ax.plot([c, c], [Y_BACK + 0.50, Y_FWD - 0.50], color=ORANGE,
            linewidth=1.3, linestyle=(0, (3, 4)), zorder=1)
ax.text(COLS[1], (Y_FWD + Y_BACK) / 2 - 0.02, "undone second", ha="center",
        va="center", fontsize=13.5, color=ORANGE,
        bbox=dict(boxstyle="round,pad=0.24", facecolor="white",
                  edgecolor="none"), zorder=2)
ax.text(COLS[2], (Y_FWD + Y_BACK) / 2 - 0.02, "undone first", ha="center",
        va="center", fontsize=13.5, color=ORANGE,
        bbox=dict(boxstyle="round,pad=0.24", facecolor="white",
                  edgecolor="none"), zorder=2)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_07_the_machine_backwards.png", dpi=170,
            facecolor="white")
print("saved", out / "fig_07_the_machine_backwards.png")
