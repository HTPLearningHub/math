"""Figure 1 - the place value chart carried to the left, past the hundreds.

Chapter 2 drew the chart from hundreds down to thousandths. This one walks the
other way: ones, tens, hundreds, thousands, with the digits of 1293 inside the
boxes and the value each digit stands for written underneath.

Run with:  python figures/fig_01_place_value_thousands.py
"""

import matplotlib
matplotlib.use("Agg")               # draw to a file, never to a screen
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # the boxes and the digits
ORANGE = "#E67E22"      # the "ten times bigger" arrow
INK = "#212121"         # near black - ordinary text
MONO = "DejaVu Sans Mono"

# the four places, written right to left the way the reader will read them
PLACES = [("Thousands", "1", "1000"),
          ("Hundreds", "2", "200"),
          ("Tens", "9", "90"),
          ("Ones", "3", "3")]

BOX_W, BOX_H = 2.3, 1.5             # size of one place box, in inches
GAP = 0.30                          # space between two boxes

fig, ax = plt.subplots(figsize=(11.2, 5.2))
ax.axis("off")
ax.set_xlim(0, 11.2)
ax.set_ylim(0, 5.2)
ax.set_aspect("equal")              # squares must look like squares

total_w = len(PLACES) * BOX_W + (len(PLACES) - 1) * GAP
x0 = (11.2 - total_w) / 2           # centre the whole row of boxes
y0 = 1.75                           # bottom edge of the boxes

for i, (name, digit, value) in enumerate(PLACES):
    x = x0 + i * (BOX_W + GAP)
    # the box itself
    ax.add_patch(FancyBboxPatch((x, y0), BOX_W, BOX_H,
                                boxstyle="round,pad=0.02,rounding_size=0.10",
                                facecolor="#EAF2FB", edgecolor=BLUE, linewidth=2.2))
    # the name of the place, above the box
    ax.text(x + BOX_W / 2, y0 + BOX_H + 0.22, name, ha="center", va="bottom",
            fontsize=13, fontweight="bold", color=BLUE)
    # the digit of 1293 that lives in this place
    ax.text(x + BOX_W / 2, y0 + BOX_H / 2, digit, ha="center", va="center",
            fontsize=40, family=MONO, color=INK)
    # what that digit is actually worth
    ax.text(x + BOX_W / 2, y0 - 0.30, f"worth ${value}$", ha="center", va="top",
            fontsize=13, color=INK)

# the arrow along the top: every step to the LEFT is ten times bigger
y_arrow = y0 + BOX_H + 0.95
ax.annotate("", xy=(x0 - 0.05, y_arrow), xytext=(x0 + total_w + 0.05, y_arrow),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, linewidth=2.6,
                            mutation_scale=22))
ax.text(x0 + total_w / 2, y_arrow + 0.18, r"one step left $= \times 10$",
        ha="center", va="bottom", fontsize=15, fontweight="bold", color=ORANGE)

# the number itself, written out under the boxes
ax.text(11.2 / 2, 0.70, r"$1\,293$", ha="center", va="center",
        fontsize=30, family=MONO, color=BLUE)
ax.text(11.2 / 2, 0.22, "the four digits read together", ha="center", va="center",
        fontsize=12, color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_place_value_thousands.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
