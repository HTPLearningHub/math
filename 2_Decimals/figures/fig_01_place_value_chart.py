"""Figure 1 - the place value chart, from hundreds down to thousandths.

One box per place. The whole-number places are blue, the decimal point is grey,
the fraction places are orange. Two arrows show the base-10 rule:
one step left multiplies by 10, one step right divides by 10.
Run with:  python figures/fig_01_place_value_chart.py
"""

import matplotlib
matplotlib.use("Agg")                      # draw to a file, never to a window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

WHOLE = "#2E86DE"       # blue   - the places left of the point
PART = "#E67E22"        # orange - the places right of the point
POINT = "#546E7A"       # grey   - the decimal point itself
WHOLE_FILL = "#E8F1FC"  # pale blue fill
PART_FILL = "#FDF0E3"   # pale orange fill
POINT_FILL = "#ECEFF1"  # pale grey fill

# one tuple per box: (name, decimal value, the same value as a fraction, edge, fill)
boxes = [
    ("Hundreds", r"$100$", "", WHOLE, WHOLE_FILL),
    ("Tens", r"$10$", "", WHOLE, WHOLE_FILL),
    ("Ones", r"$1$", "", WHOLE, WHOLE_FILL),
    ("decimal\npoint", r"$\mathbf{.}$", "", POINT, POINT_FILL),
    ("Tenths", r"$0.1$", r"$=\frac{1}{10}$", PART, PART_FILL),
    ("Hundredths", r"$0.01$", r"$=\frac{1}{100}$", PART, PART_FILL),
    ("Thousandths", r"$0.001$", r"$=\frac{1}{1000}$", PART, PART_FILL),
]

W, H, GAP = 1.55, 1.25, 0.14               # box width, box height, gap between boxes

fig, ax = plt.subplots(figsize=(13.0, 4.8))
ax.axis("off")
ax.set_xlim(-0.5, len(boxes) * (W + GAP) + 0.3)
ax.set_ylim(-1.30, 1.95)
ax.set_aspect("equal")                     # the boxes must keep their shape

for i, (name, value, as_fraction, edge, fill) in enumerate(boxes):
    x = i * (W + GAP)
    ax.add_patch(FancyBboxPatch((x, 0), W, H,                       # the box itself
                                boxstyle="round,pad=0.02,rounding_size=0.08",
                                linewidth=2.4, edgecolor=edge, facecolor=fill))
    ax.text(x + W / 2, 0.93, name, ha="center", va="center",        # the name of the place
            fontsize=11, fontweight="bold", color=edge)
    ax.text(x + W / 2, 0.56, value, ha="center", va="center",       # the value of the place
            fontsize=14, color="#212121")
    if as_fraction:                                                 # only the small places
        ax.text(x + W / 2, 0.22, as_fraction, ha="center", va="center",
                fontsize=13, color="#212121")

left_end = -0.25                           # where the two arrows start and stop
right_end = len(boxes) * (W + GAP) - GAP + 0.25

# arrow above the boxes: reading the chart from right to left multiplies by 10
ax.annotate("", xy=(left_end, 1.50), xytext=(right_end, 1.50),
            arrowprops=dict(arrowstyle="-|>", color=WHOLE, linewidth=2.6))
ax.text((left_end + right_end) / 2, 1.66,
        r"one step to the left: $\times\, 10$  (ten times bigger)",
        ha="center", va="bottom", fontsize=13, fontweight="bold", color=WHOLE)

# arrow under the boxes: reading the chart from left to right divides by 10
ax.annotate("", xy=(right_end, -0.32), xytext=(left_end, -0.32),
            arrowprops=dict(arrowstyle="-|>", color=PART, linewidth=2.6))
ax.text((left_end + right_end) / 2, -0.50,
        r"one step to the right: $\div\, 10$  (ten times smaller)",
        ha="center", va="top", fontsize=13, fontweight="bold", color=PART)

ax.set_title("The same chart on both sides of the decimal point",
             fontsize=17, fontweight="bold", pad=12)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_place_value_chart.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
