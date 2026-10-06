"""Figure 1 - a power of a fraction, drawn as an area.

The rule (a/b)^n = a^n / b^n is new in this chapter. The cleanest picture of
it is Chapter 16's crossing cuts: a square of side 2/3 sits inside a whole
square of side 1. Cutting each side into thirds makes 3 x 3 = 9 small
squares in the whole, and 2 x 2 = 4 of them are shaded. So (2/3)^2 = 4/9,
and the reader can see that the top was squared (2 x 2 shaded) and the
bottom was squared (3 x 3 in the whole) separately.

Colour convention (Chapters 10 and 24):
    blue   - the top of the fraction, and the shaded part it counts
    orange - the bottom of the fraction, and the whole it counts
    grey   - quiet labels and measuring arrows
    ink    - the outline of the whole square and the main equations

Horizontal plan (x): the square runs 1.00 - 5.80; the text column starts
    at 7.00.
Vertical plan (y): the square runs 0.70 - 5.50; the heading is at 6.45.

Run with:  python figures/fig_01_power_of_a_fraction.py
"""

import matplotlib
matplotlib.use("Agg")                      # draw to a file, never to a window
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"                           # the top of the fraction
BLUE_T = "#D6E9FA"                         # pale blue fill for the shaded cells
ORANGE = "#E67E22"                         # the bottom of the fraction
GREY = "#78909C"                           # quiet labels and arrows
INK = "#212121"                            # main text

W, H = 13.0, 7.0                           # canvas size in inches = data units
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # let the axes fill the whole figure
ax.axis("off")                             # no ticks or frame
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")                     # a square must look square

# heading across the top
ax.text(0.40, 6.55, "the exponent goes to the top and to the bottom",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

ox, oy, S = 1.00, 0.70, 4.80               # lower-left corner and side of the whole
c = S / 3                                  # side of one small square

# the nine small squares; the bottom-left 2 x 2 block is the shaded part
for i in range(3):                         # i counts columns from the left
    for j in range(3):                     # j counts rows from the bottom
        shaded = i < 2 and j < 2
        ax.add_patch(Rectangle(
            (ox + i * c, oy + j * c), c, c,
            facecolor=BLUE_T if shaded else "white",
            edgecolor=BLUE if shaded else ORANGE,
            linewidth=1.6, zorder=1))

# the outline of the whole square, drawn last so it sits on top
ax.add_patch(Rectangle((ox, oy), S, S, fill=False, edgecolor=INK,
                       linewidth=2.6, zorder=3))

# measuring arrow under the shaded block: its width is 2/3
ax.annotate("", xy=(ox, oy - 0.30), xytext=(ox + 2 * c, oy - 0.30),
            arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.6))
ax.text(ox + c, oy - 0.62, r"$\frac{2}{3}$", ha="center", va="center",
        fontsize=21, color=BLUE)

# measuring arrow left of the shaded block: its height is 2/3
ax.annotate("", xy=(ox - 0.30, oy), xytext=(ox - 0.30, oy + 2 * c),
            arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.6))
ax.text(ox - 0.68, oy + c, r"$\frac{2}{3}$", ha="center", va="center",
        fontsize=21, color=BLUE)

# measuring arrow over the whole square: its side is 1
ax.annotate("", xy=(ox, oy + S + 0.28), xytext=(ox + S, oy + S + 0.28),
            arrowprops=dict(arrowstyle="<->", color=GREY, lw=1.4))
ax.text(ox + S / 2, oy + S + 0.55, "1 whole", ha="center", va="center",
        fontsize=14, color=GREY)

# the text column on the right
tx = 7.00
ax.text(tx, 5.20, r"$\left(\frac{2}{3}\right)^{2} = \frac{2}{3} \times \frac{2}{3}$",
        ha="left", va="center", fontsize=26, color=INK)

ax.text(tx, 3.95, r"tops:  $2 \times 2 = 4$", ha="left", va="center",
        fontsize=20, color=BLUE)
ax.text(tx + 0.25, 3.45, "the shaded squares", ha="left", va="center",
        fontsize=13.5, color=GREY)

ax.text(tx, 2.70, r"bottoms:  $3 \times 3 = 9$", ha="left", va="center",
        fontsize=20, color=ORANGE)
ax.text(tx + 0.25, 2.20, "the squares in the whole", ha="left",
        va="center", fontsize=13.5, color=GREY)

ax.text(tx, 1.05, r"$\left(\frac{2}{3}\right)^{2} = \frac{2^{2}}{3^{2}} = \frac{4}{9}$",
        ha="left", va="center", fontsize=28, color=INK)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)                   # create assets/ if it is missing
fig.savefig(out / "fig_01_power_of_a_fraction.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_01_power_of_a_fraction.png")
