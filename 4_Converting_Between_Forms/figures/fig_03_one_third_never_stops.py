"""Figure 3 - why one third never stops as a decimal.

Dividing 1 by 3 lands in a loop: every step leaves 1 behind,
that 1 becomes 10 of the next smaller piece, and the same step starts again.
The two boxes and the two curved arrows are that loop.
On the right, the answer grows by one 3 at every turn of the loop.
Run with:  python figures/fig_03_one_third_never_stops.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"   # the step that produces a digit
SLATE = "#546E7A"    # the step that trades the leftover down
TEXT = "#37474F"
MARK = "#C0392B"     # the leftover that never goes away

fig, ax = plt.subplots(figsize=(11.6, 5.6))
ax.axis("off")
ax.set_xlim(-0.4, 13.9)
ax.set_ylim(0, 6.2)


def box(cx, cy, lines, colour, w=6.6, h=1.5):
    """One rounded box with two lines of text inside it."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.12,rounding_size=0.25",
                                facecolor="#FFFFFF", edgecolor=colour, linewidth=2.8))
    ax.text(cx, cy + 0.30, lines[0], ha="center", va="center",
            fontsize=14.5, color=colour, fontweight="bold")
    ax.text(cx, cy - 0.34, lines[1], ha="center", va="center",
            fontsize=14.5, color=TEXT)


# the two steps of the loop
box(3.9, 4.6, ["share $10$ pieces between $3$",
               r"each gets $3$, and $1$ is left over"], ORANGE)
box(3.9, 1.5, ["the leftover $1$ moves one place right",
               r"it becomes $10$ smaller pieces"], SLATE)

# the two curved arrows that close the loop
ax.add_patch(FancyArrowPatch((1.1, 3.95), (1.1, 2.15), arrowstyle="-|>",
                             mutation_scale=22, linewidth=2.4, color=MARK,
                             connectionstyle="arc3,rad=0.42"))
ax.add_patch(FancyArrowPatch((6.7, 2.15), (6.7, 3.95), arrowstyle="-|>",
                             mutation_scale=22, linewidth=2.4, color=MARK,
                             connectionstyle="arc3,rad=0.42"))
ax.text(0.25, 3.05, "always\n$1$ left", ha="center", va="center",
        fontsize=12, color=MARK, fontweight="bold")
ax.text(7.65, 3.05, "start\nagain", ha="center", va="center",
        fontsize=12, color=MARK, fontweight="bold")

# the answer growing, one turn of the loop at a time
ax.text(10.7, 5.25, "the answer after", ha="center", va="center",
        fontsize=13, color=TEXT)
for k, (turn, value) in enumerate([("turn 1", r"$0.3$"),
                                   ("turn 2", r"$0.33$"),
                                   ("turn 3", r"$0.333$"),
                                   ("turn 4", r"$0.3333$")]):
    y = 4.55 - k * 0.72
    ax.text(9.7, y, turn, ha="right", va="center", fontsize=12.5, color=SLATE)
    ax.text(10.05, y, value, ha="left", va="center", fontsize=15, color=TEXT)
ax.text(10.7, 1.45, r"$\ldots$ and it never stops",
        ha="center", va="center", fontsize=13, color=TEXT)
ax.text(10.7, 0.72, r"$\frac{1}{3} = 0.\overline{3}$",
        ha="center", va="center", fontsize=21, color=ORANGE, fontweight="bold")

ax.set_title(r"Dividing $1$ by $3$ goes round in a circle",
             fontsize=17, fontweight="bold", pad=8)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_one_third_never_stops.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
