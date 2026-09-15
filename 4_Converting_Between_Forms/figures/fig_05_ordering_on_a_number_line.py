"""Figure 5 - four numbers in four different forms, put in order.

The line is a percent scale, zoomed in on the small stretch from 59% to 63%.
Each of the four numbers is marked at its own place, with the form it
was given in above the line and its percent value below it.
Once they all sit on one scale, the order is simply left to right.
Run with:  python figures/fig_05_ordering_on_a_number_line.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"     # fraction
SLATE = "#546E7A"    # decimal and the line itself
ORANGE = "#E67E22"   # percent
TEXT = "#37474F"

LO, HI = 59.0, 63.0          # the ends of the zoomed percent scale
Y = 0.0                      # the height of the line

# each value: percent position, the label as it was given, its colour,
# and how far up the label sits (staggered so labels never touch)
VALUES = [
    (60.0, r"$\frac{3}{5}$", BLUE, 1.55),
    (61.5, r"$61.5\%$", ORANGE, 2.45),
    (62.0, r"$0.62$", SLATE, 1.55),
    (62.5, r"$\frac{5}{8}$", BLUE, 2.45),
]

fig, ax = plt.subplots(figsize=(11.6, 4.8))
ax.axis("off")
ax.set_xlim(LO - 0.45, HI + 0.45)
ax.set_ylim(-1.9, 3.5)

# the scale itself, with a tick every half percent
ax.plot([LO, HI], [Y, Y], color=SLATE, linewidth=2.6, solid_capstyle="butt")
tick = LO
while tick <= HI + 1e-9:
    big = abs(tick - round(tick)) < 1e-9
    ax.plot([tick, tick], [Y - (0.16 if big else 0.09), Y + (0.16 if big else 0.09)],
            color=SLATE, linewidth=1.8 if big else 1.2)
    if big:
        ax.text(tick, Y - 0.48, f"{int(tick)}%", ha="center", va="center",
                fontsize=12, color=SLATE)
    tick += 0.5
ax.text((LO + HI) / 2, Y - 1.15, "everything measured on one percent scale",
        ha="center", va="center", fontsize=13, color=SLATE)

# the four values, each on its own stalk above the line
for x, given, colour, height in VALUES:
    ax.plot([x, x], [Y + 0.08, height - 0.30], color=colour,
            linewidth=1.8, linestyle="--")
    ax.plot([x], [Y], marker="o", markersize=11, color=colour)
    ax.text(x, height + 0.12, given, ha="center", va="center",
            fontsize=18, color=colour,
            bbox=dict(boxstyle="round,pad=0.26", facecolor="#FFFFFF",
                      edgecolor=colour, linewidth=1.8))
    # the percent value, on a white patch so the dashed stalk does not cross it
    ax.text(x, height - 0.62, f"{x}%".replace(".0%", "%"),
            ha="center", va="center", fontsize=11.5, color=colour,
            bbox=dict(boxstyle="round,pad=0.16", facecolor="#FFFFFF",
                      edgecolor="none"))

# the direction of the answer
ax.annotate("", xy=(HI - 0.15, -1.62), xytext=(LO + 0.15, -1.62),
            arrowprops=dict(arrowstyle="-|>", color=TEXT, linewidth=2.0))
ax.text((LO + HI) / 2, -1.62, "  smallest to biggest  ", ha="center", va="center",
        fontsize=12.5, color=TEXT, fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.22", facecolor="#FFFFFF", edgecolor="none"))

ax.set_title("Four numbers, four forms, one scale",
             fontsize=17, fontweight="bold", pad=10)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_ordering_on_a_number_line.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
