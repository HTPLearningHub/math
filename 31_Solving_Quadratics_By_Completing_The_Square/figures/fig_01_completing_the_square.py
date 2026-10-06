"""Figure 1 - why the method is called "completing the square".

Three panels for the expression x^2 + 6x:
  left   - a blue x by x square and one orange strip, 6 wide and x long;
  middle - the strip cut in half: two 3 by x strips placed on the top and on
           the right of the square; the top-right corner is empty (red, dashed);
  right  - the corner filled with a green 3 by 3 square (area 9); the whole
           shape is now one square with side x + 3.

Colours: blue x^2, orange the x-strips, green the added corner, red missing.

Run with:  python figures/fig_01_completing_the_square.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

INK = "#212121"
BLUE = "#2E86DE"
ORANGE = "#E67E22"
GREEN = "#1E8449"
RED = "#C0392B"

X = 5.0                                            # length drawn for x
H = 3.0                                            # length drawn for 3 (half of 6)

fig, axes = plt.subplots(1, 3, figsize=(18, 7))


def box(ax, x0, y0, w, h, col, txt, dashed=False, alpha=0.18):
    """One rectangle with its area written in the middle."""
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=col if not dashed else "white",
                           alpha=1 if dashed else alpha, edgecolor=col, lw=2.5,
                           linestyle="--" if dashed else "-"))
    ax.text(x0 + w / 2, y0 + h / 2, txt, ha="center", va="center",
            fontsize=22, color=col, fontweight="bold")


def setup(ax, title):
    """Same limits on every panel, equal scale so squares look square."""
    ax.set_xlim(-1.4, 13.2)
    ax.set_ylim(-2.1, 9.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=19, color=INK, pad=8)


# --- left: x^2 and one long strip 6x ----------------------------------------
ax = axes[0]
setup(ax, r"$x^{2} + 6x$")
box(ax, 0, 0, X, X, BLUE, r"$x^{2}$")
box(ax, X + 0.6, 0, 2 * H, X, ORANGE, r"$6x$")
ax.text(X / 2, -0.7, r"$x$", ha="center", fontsize=20, color=INK)
ax.text(-0.6, X / 2, r"$x$", va="center", fontsize=20, color=INK)
ax.text(X + 0.6 + H, -0.7, r"$6$", ha="center", fontsize=20, color=INK)

# --- middle: the strip cut in two halves, corner missing --------------------
ax = axes[1]
setup(ax, r"cut $6x$ into $3x + 3x$")
box(ax, 0, 0, X, X, BLUE, r"$x^{2}$")
box(ax, X, 0, H, X, ORANGE, r"$3x$")              # right strip, 3 wide
box(ax, 0, X, X, H, ORANGE, r"$3x$")              # top strip, 3 tall
box(ax, X, X, H, H, RED, r"$?$", dashed=True)     # the empty corner
ax.text(X / 2, -0.7, r"$x$", ha="center", fontsize=20, color=INK)
ax.text(X + H / 2, -0.7, r"$3$", ha="center", fontsize=20, color=INK)
ax.text(-0.6, X / 2, r"$x$", va="center", fontsize=20, color=INK)
ax.text(-0.6, X + H / 2, r"$3$", va="center", fontsize=20, color=INK)
ax.text(X + H + 0.4, X + H / 2, "missing\ncorner", va="center",
        fontsize=16, color=RED)

# --- right: corner added, one complete square --------------------------------
ax = axes[2]
setup(ax, r"add $3 \times 3 = 9$:  $x^{2} + 6x + 9 = (x + 3)^{2}$")
box(ax, 0, 0, X, X, BLUE, r"$x^{2}$")
box(ax, X, 0, H, X, ORANGE, r"$3x$")
box(ax, 0, X, X, H, ORANGE, r"$3x$")
box(ax, X, X, H, H, GREEN, r"$9$", alpha=0.3)
ax.add_patch(Rectangle((0, 0), X + H, X + H, fill=False,
                       edgecolor=INK, lw=3.5))     # outline of the big square
ax.annotate("", xy=(X + H, -0.9), xytext=(0, -0.9),
            arrowprops=dict(arrowstyle="<->", color=INK, lw=1.8))
ax.text((X + H) / 2, -1.75, r"side $x + 3$", ha="center", fontsize=18,
        color=INK)
ax.annotate("", xy=(X + H + 0.6, X + H), xytext=(X + H + 0.6, 0),
            arrowprops=dict(arrowstyle="<->", color=INK, lw=1.8))
ax.text(X + H + 0.9, (X + H) / 2, r"side $x + 3$", va="center",
        fontsize=18, color=INK, rotation=90)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_completing_the_square.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_01_completing_the_square.png")
