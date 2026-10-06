"""Figure 2 - the four FOIL products drawn as arcs on (x + 3)(x - 2).

The four terms x, +3, x, -2 sit on one line. First and Outer are arcs above
the line (both start at the first x); Inner and Last are arcs below (both
start at +3). Each arc carries its letter and its product. The bottom line
lists the four products and the collected answer.

Colours follow fig_01: blue First, orange Outer, teal Inner, purple Last,
green answer, grey labels.

Run with:  python figures/fig_02_foil_arcs.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
GREEN = "#1E8449"
BLUE, ORANGE, TEAL, PURPLE = "#2E86DE", "#E67E22", "#138D75", "#8E44AD"

fig, ax = plt.subplots(figsize=(13, 8.6))
ax.set_xlim(0, 13)
ax.set_ylim(-0.6, 8.6)
ax.set_aspect("equal")                             # arcs stay round
ax.axis("off")

Y = 4.6                                            # height of the terms line
a, b, c, d = 3.0, 5.2, 7.8, 10.0                   # x, +3, x, -2
for xp, t in ((a, r"$x$"), (b, r"$+\,3$"), (c, r"$x$"), (d, r"$-\,2$")):
    ax.text(xp, Y, t, ha="center", va="center", fontsize=34, color=INK)
# a grey bracket around each binomial
for xp, t in ((a - 0.8, "("), (b + 0.8, ")"), (c - 0.8, "("),
              (d + 0.8, ")")):
    ax.text(xp, Y, t, ha="center", va="center", fontsize=42, color=GREY)


def arc(x1, x2, up, height, col, label, left=False):
    """Half-ellipse from term x1 to term x2, above (up) or below the line.

    left=True puts the label to the left of the arc's lowest point, so it
    does not sit on top of a bigger arc drawn around it."""
    mid, w = (x1 + x2) / 2, x2 - x1
    y0 = Y + 0.45 if up else Y - 0.45            # start just off the text
    ax.add_patch(Arc((mid, y0), w, 2 * height,
                     theta1=0 if up else 180, theta2=180 if up else 360,
                     color=col, lw=3))
    ty = y0 + height + 0.35 if up else y0 - height - 0.35
    if left:                                     # label beside, not below
        mid, ty = x1 - 0.3, y0 - height
    ax.text(mid, ty, label, ha="right" if left else "center", va="center",
            fontsize=19,
            color=col, fontweight="bold")


arc(a, c, True, 1.0, BLUE, r"F  first:  $x \cdot x = x^{2}$")
arc(a, d, True, 2.3, ORANGE, r"O  outer:  $x \cdot (-2) = -2x$")
arc(b, c, False, 1.0, TEAL, r"I  inner:  $3 \cdot x = 3x$",
    left=True)
arc(b, d, False, 2.3, PURPLE, r"L  last:  $3 \cdot (-2) = -6$")

# --- the four products in a row, then the answer -----------------------------
yb = -0.2
parts = [(r"$x^{2}$", BLUE), (r"$-\,2x$", ORANGE), (r"$+\,3x$", TEAL),
         (r"$-\,6$", PURPLE)]
for xp, (t, col) in zip([2.3, 3.6, 5.0, 6.3], parts):
    ax.text(xp, yb, t, ha="center", va="center", fontsize=24, color=col,
            fontweight="bold")
ax.text(7.2, yb, r"$=$", ha="center", va="center", fontsize=24, color=INK)
ax.text(9.5, yb, r"$x^{2} + x - 6$", ha="center", va="center", fontsize=26,
        color=GREEN, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_foil_arcs.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_02_foil_arcs.png")
