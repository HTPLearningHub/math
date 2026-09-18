"""Figure 10 - the four cases, in one grid.

The source gives this as a six-row comparison table, which is accurate but
asks the reader to hold two variables in their head at once. A two-by-two
grid says the same thing in a shape the eye can read: the index across one
direction, the sign of the radicand across the other.

One cell is red, and that is the whole point of the figure - there is
exactly one combination that has no answer among the numbers this book
uses.

Colour convention:
    green - this combination has an answer
    red   - this combination has no real answer
    grey  - the extra line under each verdict

Horizontal plan (x): the row labels are centred at 1.30; the left column
    runs 2.30-7.35 (centre 4.82) and the right column 7.45-12.50
    (centre 9.97).

Vertical plan (y, top to bottom):
    6.70  figure heading
    6.15  the two column headings
    5.85  top of the first row of cells (bottom 3.35)
    5.10  its example, 4.45 its verdict, 3.95 its note
    3.05  top of the second row of cells (bottom 0.55)
    2.30  its example, 1.65 its verdict, 1.15 its note

Run with:  python figures/fig_10_which_roots_exist.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

GREEN = "#1E8449"       # there is an answer
RED = "#C0392B"         # there is no real answer
GREY = "#78909C"
INK = "#212121"
GREEN_T = "#F1F9F4"
RED_T = "#FCF0EE"

W, H = 13.00, 7.05
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.40, 6.70,
        "one of these four boxes is the only place where a root runs out "
        "of numbers",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# the two column headings
ax.text(4.82, 6.15, "the number inside is positive", ha="center",
        va="center", fontsize=15.5, color=INK, fontweight="bold")
ax.text(9.97, 6.15, "the number inside is negative", ha="center",
        va="center", fontsize=15.5, color=INK, fontweight="bold")

# the two row labels
ax.text(1.30, 4.60, "even index\n$2, 4, 6, \\ldots$", ha="center",
        va="center", fontsize=15.5, color=INK, fontweight="bold",
        linespacing=1.6)
ax.text(1.30, 1.80, "odd index\n$3, 5, 7, \\ldots$", ha="center",
        va="center", fontsize=15.5, color=INK, fontweight="bold",
        linespacing=1.6)

cells = [
    # x_left, y_bottom, colour, fill, example, verdict, note
    (2.30, 3.35, GREEN, GREEN_T, r"$\sqrt{9} = 3$", "there is an answer",
     r"and the equation $x^{2} = 9$ has two: $3$ and $-3$"),
    (7.45, 3.35, RED, RED_T, r"$\sqrt{-9}$", "no real answer",
     "nothing multiplied by itself gives a negative"),
    (2.30, 0.55, GREEN, GREEN_T, r"$\sqrt[3]{27} = 3$",
     "one answer, and it is positive",
     r"$(-3)^{3}$ is $-27$, so it does not compete"),
    (7.45, 0.55, GREEN, GREEN_T, r"$\sqrt[3]{-27} = -3$",
     "one answer, and it is negative",
     "an odd count of minus signs stays negative"),
]

for x_left, y_bottom, colour, fill, example, verdict, note in cells:
    ax.add_patch(FancyBboxPatch(
        (x_left, y_bottom), 5.05, 2.50,
        boxstyle="round,pad=0.0,rounding_size=0.18",
        facecolor=fill, edgecolor=colour, linewidth=2.0, zorder=0))

    centre = x_left + 5.05 / 2
    ax.text(centre, y_bottom + 1.75, example, ha="center", va="center",
            fontsize=25, color=INK, zorder=2)
    ax.text(centre, y_bottom + 1.10, verdict, ha="center", va="center",
            fontsize=15, color=colour, fontweight="bold", zorder=2)
    ax.text(centre, y_bottom + 0.60, note, ha="center", va="center",
            fontsize=12.5, color=GREY, zorder=2)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_10_which_roots_exist.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_10_which_roots_exist.png")
