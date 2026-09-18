"""Figure 5 - hunting for the square root of 2.

The source says only that the square root of 2 is about 1.41421356 and
that the digits never stop. That is a claim the reader has to take on
trust. This figure replaces trust with a method: pick two numbers, square
them both, and see that 2 falls between the two answers. Then do it again
in the gap you have just found.

Three rows, each one a zoom of the row above:
    1 and 2        ->  1 and 4        ->  the root is between 1 and 2
    1.4 and 1.5    ->  1.96 and 2.25  ->  between 1.4 and 1.5
    1.41 and 1.42  ->  1.9881, 2.0164 ->  between 1.41 and 1.42

Every number here was checked with Python before it was drawn.

Colour convention:
    blue   - the squares of the two end numbers
    green  - where the root actually is
    grey   - the end numbers themselves, and the closing note

Horizontal plan (x): each row's line runs 2.20 to 8.60, so the whole gap
    of that row is 6.40 wide. The conclusion for the row is left-aligned
    at 8.95. The green dot sits at 4.85, 3.11 and 4.90 from top to bottom.

Vertical plan (y, top to bottom):
    6.85  figure heading
    5.75  row 1 (its squares at 6.15, its numbers at 5.33)
    3.95  row 2
    2.15  row 3
    0.72  the closing sentence

Run with:  python figures/fig_05_trapping_root_two.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # the squares of the end numbers
GREEN = "#1E8449"       # the root we are hunting
GREY = "#78909C"
INK = "#212121"

W, H = 13.00, 7.20
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

X0, X1 = 2.20, 8.60     # the two ends of every row's line
ROOT_2 = 1.41421356     # the value the three rows are closing in on

ax.text(0.40, 6.85,
        "squaring two numbers tells you where the root of $2$ must be, "
        "and the gap can always be made smaller",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

rows = [
    # y,   low,   high,  low^2 text, high^2 text, conclusion
    (5.75, 1.0,   2.0,   "$1^{2} = 1$",       "$2^{2} = 4$",
     r"so $\sqrt{2}$ is between $1$ and $2$"),
    (3.95, 1.4,   1.5,   "$1.4^{2} = 1.96$",  "$1.5^{2} = 2.25$",
     r"so $\sqrt{2}$ is between $1.4$ and $1.5$"),
    (2.15, 1.41,  1.42,  "$1.41^{2} = 1.9881$", "$1.42^{2} = 2.0164$",
     r"so $\sqrt{2}$ is between $1.41$ and $1.42$"),
]

for y, low, high, low_sq, high_sq, verdict in rows:
    # the line itself, with a solid stop at each end
    ax.plot([X0, X1], [y, y], linewidth=2.0, color=INK, zorder=1)
    for x in (X0, X1):
        ax.plot([x, x], [y - 0.16, y + 0.16], linewidth=2.4, color=INK,
                zorder=1)

    # the two end numbers, under the line
    ax.text(X0, y - 0.42, "$%s$" % ("%g" % low), ha="center", va="center",
            fontsize=15, color=INK, fontweight="bold")
    ax.text(X1, y - 0.42, "$%s$" % ("%g" % high), ha="center", va="center",
            fontsize=15, color=INK, fontweight="bold")

    # their squares, above the line, with the verdict on each
    ax.text(X0, y + 0.40, low_sq, ha="center", va="center", fontsize=14,
            color=BLUE)
    ax.text(X0, y + 0.74, "too small", ha="center", va="center",
            fontsize=11.5, color=GREY, style="italic")
    ax.text(X1, y + 0.40, high_sq, ha="center", va="center", fontsize=14,
            color=BLUE)
    ax.text(X1, y + 0.74, "too big", ha="center", va="center",
            fontsize=11.5, color=GREY, style="italic")

    # where the root really is, on this row's scale
    x_root = X0 + (X1 - X0) * (ROOT_2 - low) / (high - low)
    ax.plot([x_root], [y], marker="o", markersize=14, color=GREEN, zorder=4)
    ax.text(x_root, y - 0.46, r"$\sqrt{2}$", ha="center", va="center",
            fontsize=16, color=GREEN, fontweight="bold")

    # the sentence this row proves
    ax.text(8.95, y, verdict, ha="left", va="center", fontsize=14.5,
            color=INK)

ax.text(6.50, 0.72,
        r"keep going and the digits never stop and never repeat: "
        r"$\sqrt{2} = 1.41421356\ldots$",
        ha="center", va="center", fontsize=15, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_05_trapping_root_two.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_05_trapping_root_two.png")
