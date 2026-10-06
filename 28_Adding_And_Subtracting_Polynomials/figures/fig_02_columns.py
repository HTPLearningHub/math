"""Figure 2 - adding two polynomials in columns.

One column per exponent: x^4, x^3, x^2, x, plain numbers. Each column is
tinted in the colour of its exponent (same colours as fig_01).
Row 1: 0x^4 + 4x^3 + 2x^2 - 6x + 9   (0x^4 is a place holder, grey dashed)
Row 2: x^4 + 0x^3 - 3x^2 + 6x - 4    (0x^3 is a place holder, grey dashed)
Under the line: x^4 + 4x^3 - x^2 + 0x + 5, where 0x is grey and struck out.
Below: the answer in green.

Run with:  python figures/fig_02_columns.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

INK = "#212121"
GREY = "#90A4AE"
GREEN = "#1E8449"
# exponent -> (edge colour, light fill), as in fig_01
COL = {
    4: ("#8E44AD", "#F3EAF8"),
    3: ("#2E86DE", "#E9F2FC"),
    2: ("#138D75", "#E6F5F1"),
    1: ("#B7950B", "#FBF5DE"),
    0: ("#E67E22", "#FDF0E3"),
}

W, H = 13.0, 7.4                                   # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

exps = [4, 3, 2, 1, 0]                             # one column per exponent
xs = [3.2, 5.2, 7.2, 9.2, 11.2]                    # column centres
CW = 1.8                                           # column width
heads = [r"$x^{4}$", r"$x^{3}$", r"$x^{2}$", r"$x$", "number"]

# tinted column strips, so each column reads as one kind of piece
for e, xc in zip(exps, xs):
    ax.add_patch(Rectangle((xc - CW / 2, 1.55), CW, 5.25,
                           facecolor=COL[e][1], edgecolor="none", zorder=0))

YH, Y1, Y2, Y3 = 6.35, 5.2, 4.0, 2.35              # header and three rows
for e, xc, h in zip(exps, xs, heads):
    ax.text(xc, YH, h, ha="center", va="center", fontsize=20,
            color=COL[e][0], fontweight="bold")

ax.text(0.3, Y1, "first", ha="left", va="center", fontsize=15,
        color=GREY, fontweight="bold")
ax.text(0.3, Y2, "second", ha="left", va="center", fontsize=15,
        color=GREY, fontweight="bold")
ax.text(0.3, Y3, "sum", ha="left", va="center", fontsize=15,
        color=GREY, fontweight="bold")
ax.text(1.75, Y2, r"$+$", ha="center", va="center", fontsize=26, color=INK)


def cell(xc, yc, text, placeholder=False, struck=False):
    """Write one term in a column. A place holder gets a dashed grey box."""
    colour = GREY if (placeholder or struck) else INK
    if placeholder:
        ax.add_patch(FancyBboxPatch(
            (xc - 0.72, yc - 0.36), 1.44, 0.72,
            boxstyle="round,pad=0.0,rounding_size=0.12",
            facecolor="white", edgecolor=GREY, linewidth=1.8,
            linestyle=(0, (4, 3)), zorder=2))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=24,
            color=colour, zorder=3)
    if struck:                                     # a zero term disappears
        ax.plot([xc - 0.5, xc + 0.5], [yc - 0.25, yc + 0.25],
                color=GREY, lw=2.2, zorder=4)


row1 = [(r"$0x^{4}$", True), (r"$+4x^{3}$", False), (r"$+2x^{2}$", False),
        (r"$-6x$", False), (r"$+9$", False)]
row2 = [(r"$x^{4}$", False), (r"$0x^{3}$", True), (r"$-3x^{2}$", False),
        (r"$+6x$", False), (r"$-4$", False)]
row3 = [(r"$x^{4}$", False), (r"$+4x^{3}$", False), (r"$-x^{2}$", False),
        (r"$0x$", True), (r"$+5$", False)]

for xc, (t, p) in zip(xs, row1):
    cell(xc, Y1, t, placeholder=p)
for xc, (t, p) in zip(xs, row2):
    cell(xc, Y2, t, placeholder=p)
for xc, (t, s) in zip(xs, row3):
    cell(xc, Y3, t, struck=s)

# the line under the second row, as in column addition of numbers
ax.plot([xs[0] - CW / 2, xs[-1] + CW / 2], [3.25, 3.25], color=INK, lw=2.0)

# small notes for the place holders
ax.text(xs[0], Y1 + 0.62, "place holder", ha="center", va="center",
        fontsize=11, color=GREY)
ax.text(xs[1], Y2 - 0.62, "place holder", ha="center", va="center",
        fontsize=11, color=GREY)
ax.text(xs[3], Y3 - 0.62, "equals 0, so it goes", ha="center", va="center",
        fontsize=11, color=GREY)

# the answer
ax.text(W / 2 + 0.6, 0.85, r"answer:  $x^{4} + 4x^{3} - x^{2} + 5$",
        ha="center", va="center", fontsize=22, color=GREEN,
        fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_columns.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_02_columns.png")
