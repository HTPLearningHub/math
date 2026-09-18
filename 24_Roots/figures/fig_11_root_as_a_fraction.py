"""Figure 11 - which number goes on top and which goes underneath.

Turning a root into a fractional exponent is easy to state and easy to get
backwards, and getting it backwards gives a completely different number.
The figure makes the rule physical: the index travels along the lower
path and lands underneath, the power travels along the upper path and
lands on top.

The two arcs are deliberately routed on opposite sides. If both were drawn
straight they would cross, and a crossing is exactly the wrong picture for
a rule about which number goes where.

Colour convention:
    blue   - the base
    purple - the index, as in Chapter 10 and figure 3
    green  - the power inside the root
    red    - the version with the two numbers swapped

Horizontal plan (x): the radical sits between 2.30 and 4.30, the equals
    sign at 6.40, and the fractional exponent around 8.20-8.95. The red
    panel at the bottom runs 3.55 to 9.45.

Vertical plan (y, top to bottom):
    6.20  figure heading
    5.15  the label on the upper arc
    3.95  the bar of the radical, and the numerator
    3.20  the base line of both expressions
    1.85  the label on the lower arc, which sags no further than 2.33
    1.55  top of the red panel (bottom 0.50)

Run with:  python figures/fig_11_root_as_a_fraction.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # the base
PURPLE = "#8E44AD"      # the index
GREEN = "#1E8449"       # the power inside the root
RED = "#C0392B"         # the swapped version
ORANGE = "#E67E22"      # the radical sign
GREY = "#78909C"
INK = "#212121"
RED_T = "#FBEAE8"

W, H = 13.00, 6.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.40, 6.20,
        "the index goes underneath and the power goes on top - never the "
        "other way round",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# ------------------------------------------------- the root, drawn by hand
ax.plot([2.30, 2.58, 2.88, 4.15], [3.52, 2.80, 3.88, 3.88],
        linewidth=3.6, color=ORANGE, solid_capstyle="round",
        solid_joinstyle="round", zorder=2)
ax.text(2.48, 3.82, "$3$", ha="center", va="center", fontsize=18,
        color=PURPLE, fontweight="bold", zorder=3)
ax.text(3.35, 3.25, "$x$", ha="center", va="center", fontsize=34,
        color=BLUE, style="italic", zorder=3)
ax.text(3.80, 3.60, "$5$", ha="center", va="center", fontsize=19,
        color=GREEN, fontweight="bold", zorder=3)

ax.text(6.40, 3.25, "$=$", ha="center", va="center", fontsize=30, color=INK)

# --------------------------------------------- the same thing as a power
ax.text(8.15, 3.20, "$x$", ha="center", va="center", fontsize=34,
        color=BLUE, style="italic", zorder=3)
ax.plot([8.52, 9.00], [3.62, 3.62], linewidth=2.0, color=INK, zorder=3)
ax.text(8.76, 3.92, "$5$", ha="center", va="center", fontsize=19,
        color=GREEN, fontweight="bold", zorder=3)
ax.text(8.76, 3.33, "$3$", ha="center", va="center", fontsize=19,
        color=PURPLE, fontweight="bold", zorder=3)

# --------------------------------------------------------- the two journeys
# the power: over the top
ax.add_patch(FancyArrowPatch((4.35, 4.18), (8.62, 4.18),
                             connectionstyle="arc3,rad=-0.30",
                             arrowstyle="-|>", mutation_scale=20,
                             linewidth=2.6, color=GREEN, zorder=1))
ax.text(6.35, 5.15, "the power travels over the top",
        ha="center", va="center", fontsize=15, color=GREEN,
        fontweight="bold")

# the index: underneath
ax.add_patch(FancyArrowPatch((2.48, 2.55), (8.62, 3.10),
                             connectionstyle="arc3,rad=0.16",
                             arrowstyle="-|>", mutation_scale=20,
                             linewidth=2.6, color=PURPLE, zorder=1))
ax.text(5.55, 1.85, "the index travels underneath",
        ha="center", va="center", fontsize=15, color=PURPLE,
        fontweight="bold")

# ---------------------------------------------------- the swapped version
ax.add_patch(FancyBboxPatch(
    (3.55, 0.50), 5.90, 1.05,
    boxstyle="round,pad=0.0,rounding_size=0.16",
    facecolor=RED_T, edgecolor=RED, linewidth=1.8, zorder=0))
ax.text(6.50, 1.22, r"$x^{\frac{3}{5}}$ is a different number: it means "
                    r"$\sqrt[5]{x^{3}}$",
        ha="center", va="center", fontsize=16, color=RED, zorder=2)
ax.text(6.50, 0.76, "swapping the two numbers changes the question",
        ha="center", va="center", fontsize=13, color=GREY, style="italic",
        zorder=2)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_11_root_as_a_fraction.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_11_root_as_a_fraction.png")
