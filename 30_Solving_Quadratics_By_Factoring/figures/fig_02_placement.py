"""Figure 2 - when a is not 1, where a number sits changes the middle term.

Two rows. Both rows use the same pieces: 3x and x in front, the numbers -1
and 2 behind, but in swapped places. Arcs show the Outer product (orange,
above) and the Inner product (teal, below). On the right: their sum, green
with a tick if it is +5x, red with a cross if not.

Row 1: (3x - 1)(x + 2) -> outer 6x, inner -x, sum +5x  (correct)
Row 2: (3x + 2)(x - 1) -> outer -3x, inner 2x, sum -x  (wrong)

Run with:  python figures/fig_02_placement.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
GREEN = "#1E8449"
RED = "#C0392B"
ORANGE, TEAL = "#E67E22", "#138D75"

fig, ax = plt.subplots(figsize=(14, 8.4))
ax.set_xlim(0, 15)
ax.set_ylim(-0.2, 9)
ax.set_aspect("equal")                             # arcs stay round
ax.axis("off")

ax.text(7.5, 8.6, r"Target:  $3x^{2} + 5x - 2$   (the middle must be $+5x$)",
        ha="center", va="center", fontsize=20, color=INK)


def row(Y, terms, outer, inner, total, ok):
    """One pair of brackets on the line y = Y, with Outer and Inner arcs."""
    xs = [1.4, 3.2, 5.4, 7.0]                      # x-positions of 4 terms
    for xp, t in zip(xs, terms):
        ax.text(xp, Y, t, ha="center", va="center", fontsize=28, color=INK)
    for xp, t in ((0.6, "("), (3.95, ")"), (4.65, "("), (7.8, ")")):
        ax.text(xp, Y, t, ha="center", va="center", fontsize=34, color=GREY)
    # Outer arc: first term of bracket 1 to last term of bracket 2, above
    mid, w = (xs[0] + xs[3]) / 2, xs[3] - xs[0]
    ax.add_patch(Arc((mid, Y + 0.4), w, 1.8, theta1=0, theta2=180,
                     color=ORANGE, lw=3))
    ax.text(mid, Y + 1.65, "outer:  " + outer, ha="center", va="center",
            fontsize=17, color=ORANGE, fontweight="bold")
    # Inner arc: last term of bracket 1 to first term of bracket 2, below
    mid, w = (xs[1] + xs[2]) / 2, xs[2] - xs[1]
    ax.add_patch(Arc((mid, Y - 0.4), w, 1.4, theta1=180, theta2=360,
                     color=TEAL, lw=3))
    ax.text(mid, Y - 1.45, "inner:  " + inner, ha="center", va="center",
            fontsize=17, color=TEAL, fontweight="bold")
    # the sum on the right, with a tick or a cross
    col = GREEN if ok else RED
    mark = r"$\checkmark$" if ok else r"$\times$"
    ax.text(11.6, Y, total + "   " + mark, ha="center", va="center",
            fontsize=22, color=col, fontweight="bold")


row(5.6, [r"$3x$", r"$-\,1$", r"$x$", r"$+\,2$"],
    r"$3x \cdot 2 = 6x$", r"$-1 \cdot x = -x$",
    r"$6x - x = +5x$", True)
row(1.6, [r"$3x$", r"$+\,2$", r"$x$", r"$-\,1$"],
    r"$3x \cdot (-1) = -3x$", r"$2 \cdot x = 2x$",
    r"$-3x + 2x = -x$", False)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_placement.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_02_placement.png")
