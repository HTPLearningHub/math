"""Figure 5 - two roads to 64^(2/3), and why the root goes first.

Upper road (green): take the cube root first, 64 -> 4, then square, 4 -> 16.
Lower road (grey): square first, 64 -> 4 096, then the cube root, 4 096 -> 16.
Both arrive at 16. The upper road never leaves the perfect-square and
perfect-cube tables of Chapter 24; the lower road passes through a number
whose cube root nobody knows by heart. The middle card on each road is drawn
at a size that hints at the size of the number.

Colour convention:
    orange - a root step (Chapter 24: the radical sign and the backward direction)
    blue   - a power step (Chapter 24: the forward direction)
    green  - the recommended road and the shared answer
    grey   - the longer road's label

Horizontal plan (x): cards at 1.30, 5.60 and 9.90; the road labels sit on
    the far left above each road.
Vertical plan (y): heading 6.30; upper road 4.55; lower road 1.55.

Run with:  python figures/fig_05_two_roads.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

ORANGE = "#E67E22"
BLUE = "#2E86DE"
GREEN = "#1E8449"
GREEN_T = "#F1F9F4"
GREY = "#78909C"
GREY_T = "#F2F4F5"
INK = "#212121"

W, H = 12.4, 6.8
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.30, 6.35, r"two roads to $64^{\frac{2}{3}}$, and both arrive at $16$",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")


def card(xc, yc, text, w, edge, fill, size=24):
    """A rounded card of width w centred on (xc, yc) holding text."""
    h = 1.05
    ax.add_patch(FancyBboxPatch(
        (xc - w / 2, yc - h / 2), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.15",
        facecolor=fill, edgecolor=edge, linewidth=2.0, zorder=1))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=size,
            color=INK, zorder=2)


def step(x0, x1, yc, colour, label):
    """An arrow from x0 to x1 at height yc, with its label above it."""
    ax.annotate("", xy=(x1, yc), xytext=(x0, yc),
                arrowprops=dict(arrowstyle="-|>", color=colour, lw=2.2,
                                mutation_scale=22))
    ax.text((x0 + x1) / 2, yc + 0.45, label, ha="center", va="center",
            fontsize=14, color=colour, fontweight="bold")


# the upper road: root first
yu = 4.55
ax.text(0.30, yu + 1.05, "root first  (the easy road)", ha="left",
        va="center", fontsize=15, color=GREEN, fontweight="bold")
card(1.30, yu, r"$64$", 1.40, GREEN, GREEN_T)
step(2.10, 4.95, yu, ORANGE, r"cube root:  $4 \times 4 \times 4 = 64$")
card(5.60, yu, r"$4$", 1.10, GREEN, GREEN_T)
step(6.25, 9.15, yu, BLUE, r"square:  $4 \times 4 = 16$")
card(9.90, yu, r"$16$", 1.40, GREEN, GREEN_T)

# the lower road: power first
yl = 1.55
ax.text(0.30, yl + 1.05, "power first  (the hard road)", ha="left",
        va="center", fontsize=15, color=GREY, fontweight="bold")
card(1.30, yl, r"$64$", 1.40, GREY, GREY_T)
step(2.10, 4.35, yl, BLUE, r"square:  $64 \times 64$")
card(5.60, yl, r"$4\,096$", 2.40, GREY, GREY_T)
step(6.90, 9.15, yl, ORANGE, "cube root:  ?")
card(9.90, yl, r"$16$", 1.40, GREEN, GREEN_T)

ax.text(5.60, yl - 0.95,
        r"which number times itself three times is $4\,096$?  "
        r"Not one you know by heart.",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_05_two_roads.png", dpi=170, bbox_inches="tight",
            facecolor="white")
print("wrote", out / "fig_05_two_roads.png")
