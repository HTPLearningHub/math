"""Figure 2 - why the reciprocal power undoes a fractional exponent.

Upper row (blue, forward): the exponent 3/2 applied to 4. Its bottom, 2, is a
square root: 4 -> 2. Its top, 3, is a cube: 2 -> 8. So 4^(3/2) = 8.

Lower row (orange, backward): undo it, last step first. The cube is undone by
a cube root: 8 -> 2. The square root is undone by a square: 2 -> 4. A cube
root then a square is the exponent 2/3 (Chapter 25, section 5). So the undoing
power is 3/2 turned upside down.

Below a dashed rule, the same fact in one line: 3/2 x 2/3 = 1.

Colour convention, as in fig_01:
    blue   - the forward direction
    orange - the backward direction
    green  - the start and end value, and the closing fact
    purple - the two exponents, as in Chapter 10 (purple = exponent)
    grey   - quiet labels

Run with:  python figures/fig_02_reciprocal_power.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"
BLUE_T = "#E9F2FC"
ORANGE = "#E67E22"
ORANGE_T = "#FDF0E3"
GREEN = "#1E8449"
GREEN_T = "#E8F5EC"
PURPLE = "#8E44AD"                                 # exponents
GREY = "#78909C"
INK = "#212121"

W, H = 12.6, 8.0                                   # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.30, 7.45, r"to undo the power $\frac{3}{2}$, raise to the power $\frac{2}{3}$",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")


def card(xc, yc, text, edge, fill, w=1.40):
    """A rounded card of width w centred on (xc, yc) holding text."""
    h = 1.05
    ax.add_patch(FancyBboxPatch(
        (xc - w / 2, yc - h / 2), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.15",
        facecolor=fill, edgecolor=edge, linewidth=2.0, zorder=1))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=24,
            color=INK, zorder=2)


def step(x0, x1, yc, colour, label, sub):
    """An arrow from x0 to x1 at height yc, a bold label above, a check below."""
    ax.annotate("", xy=(x1, yc), xytext=(x0, yc),
                arrowprops=dict(arrowstyle="-|>", color=colour, lw=2.4,
                                mutation_scale=24))
    ax.text((x0 + x1) / 2, yc + 0.45, label, ha="center", va="center",
            fontsize=15, color=colour, fontweight="bold")
    ax.text((x0 + x1) / 2, yc - 0.42, sub, ha="center", va="center",
            fontsize=12.5, color=GREY)


# ---------------------------------------------------------- the forward row
yf = 5.50
ax.text(0.30, yf + 1.05, r"forward: the power $\frac{3}{2}$",
        ha="left", va="center", fontsize=15, color=BLUE, fontweight="bold")
ax.text(4.60, yf + 1.05, r"bottom $2$ = square root,  top $3$ = cube",
        ha="left", va="center", fontsize=14, color=PURPLE)
card(1.40, yf, r"$4$", GREEN, GREEN_T)
step(2.20, 5.40, yf, BLUE, "square root", r"$2 \times 2 = 4$")
card(6.20, yf, r"$2$", BLUE, BLUE_T)
step(7.00, 10.20, yf, BLUE, "cube", r"$2 \times 2 \times 2 = 8$")
card(11.00, yf, r"$8$", BLUE, BLUE_T)

# ---------------------------------------------------------- the backward row
yb = 2.55
ax.text(0.30, yb + 1.05, r"backward: the power $\frac{2}{3}$",
        ha="left", va="center", fontsize=15, color=ORANGE, fontweight="bold")
ax.text(4.60, yb + 1.05, r"bottom $3$ = cube root,  top $2$ = square",
        ha="left", va="center", fontsize=14, color=PURPLE)
card(11.00, yb, r"$8$", ORANGE, ORANGE_T)
step(10.20, 7.00, yb, ORANGE, "cube root", r"undoes the cube")
card(6.20, yb, r"$2$", ORANGE, ORANGE_T)
step(5.40, 2.20, yb, ORANGE, "square", r"undoes the square root")
card(1.40, yb, r"$4$", GREEN, GREEN_T)

# ---------------------------------------------------- the closing fact
ax.plot([0.30, W - 0.30], [1.15, 1.15], color=GREY, lw=1.2, ls=(0, (5, 4)))
ax.text(W / 2, 0.55,
        r"each step swaps its job, so the fraction turns over:   "
        r"$\frac{3}{2} \times \frac{2}{3} = 1$",
        ha="center", va="center", fontsize=16, color=GREEN)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_reciprocal_power.png", dpi=170, bbox_inches="tight",
            facecolor="white")
print("wrote", out / "fig_02_reciprocal_power.png")
