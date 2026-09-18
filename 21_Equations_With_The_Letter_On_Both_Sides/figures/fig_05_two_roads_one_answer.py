"""Figure 5 - the choice of side changes the road, not the answer.

From 3 - 3x = 24x + 12 you may add 3x to both sides, which keeps the
letter on the right, or subtract 24x, which keeps it on the left. Both
roads are legal and both end at the same number. The figure exists to
make Chapter 20's central idea visible one last time: the solution was
already -1/3 before either road was chosen.

Horizontal plan (x):
    2.80  the left road (add 3x)
    5.40  the shared start, and the shared finish
    8.00  the right road (subtract 24x)

Vertical plan (y, top to bottom):
    5.80  heading
    5.05  the starting equation, in one grey card
    4.60 -> 4.05  the two arrows apart
    3.80  what each road does first
    3.20  the line after gathering the letters
    2.60  the line after gathering the numbers
    2.05  the last division
    1.85 -> 1.52  the two arrows back together
    0.95  the answer, in one green card
    0.18  closing note

Run with:  python figures/fig_05_two_roads_one_answer.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"        # the move being made
GREEN = "#1E8449"         # the finished line
GREY = "#78909C"
INK = "#212121"
TINT_GREEN = "#E8F5EC"
TINT_GREY = "#ECEFF1"

W, H = 10.80, 6.20
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT, MID, RIGHT = 2.80, 5.40, 8.00

ax.text(0.60, 5.80, "two roads out of one equation",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# the shared starting line: true, unfinished, so grey
ax.add_patch(FancyBboxPatch((MID - 2.20, 5.05 - 0.42), 4.40, 0.85,
                            boxstyle="round,pad=0.05,rounding_size=0.16",
                            facecolor=TINT_GREY, edgecolor=GREY,
                            linewidth=2.2, zorder=3))
ax.text(MID, 5.05, r"$3 - 3x = 24x + 12$", ha="center", va="center",
        fontsize=24, color=INK, zorder=4)

# apart
ax.add_patch(FancyArrowPatch((4.30, 4.60), (LEFT, 4.05), arrowstyle="-|>",
                             mutation_scale=18, linewidth=2.2, color=ORANGE))
ax.add_patch(FancyArrowPatch((6.50, 4.60), (RIGHT, 4.05), arrowstyle="-|>",
                             mutation_scale=18, linewidth=2.2, color=ORANGE))

# each road, three lines deep
ROADS = (
    (LEFT, r"add $3x$ to both sides", r"$3 = 27x + 12$", r"$-9 = 27x$",
     r"divide by $27$"),
    (RIGHT, r"subtract $24x$ from both sides", r"$3 - 27x = 12$",
     r"$-27x = 9$", r"divide by $-27$"),
)
for xpos, move, line_one, line_two, last in ROADS:
    ax.text(xpos, 3.80, move, ha="center", va="center",
            fontsize=14, color=ORANGE)
    ax.text(xpos, 3.20, line_one, ha="center", va="center",
            fontsize=20, color=INK)
    ax.text(xpos, 2.60, line_two, ha="center", va="center",
            fontsize=20, color=INK)
    ax.text(xpos, 2.05, last, ha="center", va="center",
            fontsize=14, color=GREY)

# back together
ax.add_patch(FancyArrowPatch((LEFT, 1.85), (4.60, 1.52), arrowstyle="-|>",
                             mutation_scale=18, linewidth=2.2, color=ORANGE,
                             zorder=2))
ax.add_patch(FancyArrowPatch((RIGHT, 1.85), (6.20, 1.52), arrowstyle="-|>",
                             mutation_scale=18, linewidth=2.2, color=ORANGE,
                             zorder=2))

# the one answer
ax.add_patch(FancyBboxPatch((MID - 1.30, 0.95 - 0.42), 2.60, 0.85,
                            boxstyle="round,pad=0.05,rounding_size=0.16",
                            facecolor=TINT_GREEN, edgecolor=GREEN,
                            linewidth=2.6, zorder=3))
ax.text(MID, 0.95, r"$x = -\frac{1}{3}$", ha="center", va="center",
        fontsize=24, color=INK, zorder=4)

ax.text(0.60, 0.18, "the number was never in doubt - only the route to "
        "writing it down plainly", ha="left", va="center",
        fontsize=15, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_05_two_roads_one_answer.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_05_two_roads_one_answer.png")
