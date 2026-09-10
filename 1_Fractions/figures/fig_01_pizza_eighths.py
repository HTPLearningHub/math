"""Figure 1 - one pizza cut into 8 equal slices, with 2 slices taken.

Shows where the two numbers of a fraction come from:
the top number counts the slices we take, the bottom number counts all the slices.
Run with:  python figures/fig_01_pizza_eighths.py
"""

import matplotlib                      # the drawing library
matplotlib.use("Agg")                  # "Agg" = write to a file, do not open a window
import matplotlib.pyplot as plt        # the short name everybody uses for plotting
from matplotlib.patches import Wedge   # a Wedge is one pie slice
import numpy as np                     # only used for cos/sin of the slice angles
from pathlib import Path               # builds the output path in a safe way

TAKEN = "#2E86DE"    # blue  - the slices we take
REST = "#ECEFF1"     # grey  - the slices that stay on the plate
EDGE = "white"       # white - the cut lines between the slices


def draw_pizza(ax, center, radius, parts, taken, color):
    """Draw one round pizza cut into `parts` equal slices; fill the first `taken`."""
    step = 360.0 / parts                                  # how many degrees one slice covers
    for i in range(parts):                                # one Wedge object per slice
        start = 90.0 + i * step                           # the first cut points straight up
        end = start + step                                # each slice ends one step further
        fill = color if i < taken else REST               # first `taken` slices get the colour
        ax.add_patch(Wedge(center, radius, start, end,    # the slice itself
                           facecolor=fill, edgecolor=EDGE, linewidth=2.5))


fig, ax = plt.subplots(figsize=(9.0, 6.2))                # one picture, one drawing area
ax.set_aspect("equal")                                    # circles must stay round
ax.axis("off")                                            # no axes, no ticks - this is a picture
ax.set_xlim(-3.4, 3.4)                                    # leave room left and right for labels
ax.set_ylim(-2.6, 2.4)                                    # leave room below for the fraction

R = 1.35                                                  # radius of the pizza
draw_pizza(ax, (0.0, 0.35), R, parts=8, taken=2, color=TAKEN)

step = 360.0 / 8                                          # 45 degrees per slice
for i in range(8):                                        # write 1..8 inside the slices
    mid = np.radians(90.0 + (i + 0.5) * step)             # angle of the middle of slice i
    x = 0.0 + 0.72 * R * np.cos(mid)                      # put the number at 72% of the radius
    y = 0.35 + 0.72 * R * np.sin(mid)
    ax.text(x, y, str(i + 1), ha="center", va="center",
            fontsize=13, fontweight="bold",
            color="white" if i < 2 else "#607D8B")        # white on blue, grey-blue on grey

first_mid = np.radians(90.0 + 0.5 * step)                 # middle of slice number 1
ax.annotate("we take 2 slices,\nso the top number is 2",  # label for the numerator
            xy=(0.85 * R * np.cos(first_mid), 0.35 + 0.85 * R * np.sin(first_mid)),
            xytext=(-3.2, 1.9), ha="left", va="center", fontsize=13, color=TAKEN,
            fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=TAKEN, linewidth=2.0))

edge_angle = np.radians(-40.0)                            # a point on the rim, lower right
ax.annotate("the whole pizza is 8 equal slices,\nso the bottom number is 8",
            xy=(1.02 * R * np.cos(edge_angle), 0.35 + 1.02 * R * np.sin(edge_angle)),
            xytext=(3.2, -1.1), ha="right", va="center", fontsize=13, color="#455A64",
            fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="#455A64", linewidth=2.0))

ax.text(0.0, -2.15, r"$\mathbf{\frac{2}{8}}$ of the pizza",  # the fraction itself, big
        ha="center", va="center", fontsize=30, fontweight="bold", color="#212121")
ax.set_title("One pizza, 8 equal slices, 2 slices taken",
             fontsize=17, fontweight="bold", pad=12)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_pizza_eighths.png"
fig.savefig(out, dpi=200, bbox_inches="tight")            # sharp image, no white border
print("saved:", out)                                      # so we can see it worked
