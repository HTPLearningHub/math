"""Figure 1 - the question the whole chapter answers.

The source mentions a scheduling problem in one line of its introduction and
then never draws it. It is the best motivation the chapter has, because the
reader can see the answer before any method is taught: two buses leave at the
same moment, one every 6 minutes and one every 9 minutes, and the picture
shows the first minute at which both are at the stop again.

Two timelines, one per bus. Blue marks belong to the 6-minute bus, orange
marks to the 9-minute bus. Where a mark appears on both lines the minute is
a common multiple, so it gets a green band; the first green band is ringed,
because that is the least common multiple.
Run with:  python figures/fig_01_two_buses.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"             # the first number, 6, and everything that belongs to it
ORANGE = "#E67E22"           # the second number, 9
GREEN = "#1E8449"            # a minute that belongs to both
GREY = "#78909C"
INK = "#212121"

W, H = 11.40, 5.40
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

T0 = 1.95                                  # x of minute 0
T_END = W - 0.55                           # x of the right-hand end of a timeline
MAX_MIN = 57                               # the last minute drawn
SCALE = (T_END - T0) / MAX_MIN             # inches per minute

Y_A = 3.42                                 # the 6-minute bus line
Y_B = 2.05                                 # the 9-minute bus line

MULT_A = [m for m in range(6, MAX_MIN + 1, 6)]
MULT_B = [m for m in range(9, MAX_MIN + 1, 9)]
COMMON = sorted(set(MULT_A) & set(MULT_B))

# ------------------------------------- green bands behind the shared minutes
# the first one is drawn with a thicker edge, because it is the answer
for m in COMMON:
    x = T0 + m * SCALE
    ax.add_patch(FancyBboxPatch((x - 0.30, Y_B - 0.62), 0.60, (Y_A - Y_B) + 1.24,
                                boxstyle="round,pad=0.01,rounding_size=0.10",
                                facecolor="#E8F5EC", edgecolor=GREEN,
                                linewidth=3.0 if m == 18 else 1.4, zorder=1))

# --------------------------------------------------------- the two timelines
for y, colour, marks, label, every in (
        (Y_A, BLUE, MULT_A, "Bus A", 6),
        (Y_B, ORANGE, MULT_B, "Bus B", 9)):
    ax.plot([T0, T_END], [y, y], color=GREY, linewidth=1.6, zorder=2)
    ax.text(T0 - 0.32, y + 0.20, label, ha="right", va="center",
            fontsize=15, color=colour, fontweight="bold")
    ax.text(T0 - 0.32, y - 0.20, f"every {every} min", ha="right", va="center",
            fontsize=12, color=GREY)
    # minute 0: both buses are at the stop, so it is drawn grey, not coloured
    ax.plot([T0], [y], marker="o", markersize=9, color="white",
            markeredgecolor=GREY, markeredgewidth=2, zorder=3)
    for m in marks:
        x = T0 + m * SCALE
        shared = m in COMMON
        ax.plot([x], [y], marker="o", markersize=13 if shared else 10,
                color=GREEN if shared else colour, zorder=3)
        ax.text(x, y + (0.40 if y == Y_A else -0.44), str(m),
                ha="center", va="center", fontsize=12,
                color=GREEN if shared else colour,
                fontweight="bold" if shared else "normal")

ax.text(T0, Y_A + 0.40, "0", ha="center", va="center", fontsize=12, color=GREY)
ax.text(T0, Y_B - 0.48, "both leave", ha="center", va="center",
        fontsize=11, color=GREY)

# ------------------------- the answer, written straight under the first band
x18 = T0 + 18 * SCALE
ax.plot([x18, x18], [Y_B - 0.70, 1.22], color=GREEN, linewidth=1.6,
        linestyle=(0, (4, 3)), zorder=1)
ax.text(x18, 1.00, "18 minutes", ha="center", va="center",
        fontsize=19, color=GREEN, fontweight="bold")
ax.text(x18, 0.56, "the first minute that is on both lines",
        ha="center", va="center", fontsize=13, color=GREEN)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.42, "Two buses leave together. When are they together again?",
        ha="center", va="center", fontsize=19, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.86,
        "minutes 18, 36 and 54 are on both lines - 18 is the smallest",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_two_buses.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
