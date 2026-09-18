"""Figure 2 - why "3 less than 2g" is written 2g - 3 and never 3 - 2g.

The phrase reads left to right in English but the subtraction runs the
other way. The picture puts the two readings side by side and then
settles the argument with a number the reader can check in their head:
"3 less than 10" is plainly 7, and only one of the two readings gives 7.

Horizontal plan (x):
    0.55 - 5.05   the wrong column (red)
    5.75 - 10.25  the right column (green)
    5.40          the thin divider between them

Vertical plan (y, top to bottom):
    6.15  heading
    5.45  the phrase being translated, once, centred
    4.50  the two headings of the columns
    3.72  the two readings, large
    3.44  the strike-through, on the left only
    3.02  what each reading starts from
    2.10  "try it with a number you know" band
    1.48  the number version of each reading
    0.86  the verdict under each
    0.22  closing note

Run with:  python figures/fig_02_less_than_turns_round.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

GREEN = "#1E8449"         # the correct reading
RED = "#C0392B"           # the reading that reverses the subtraction
GREY = "#78909C"
INK = "#212121"
TINT_GREEN = "#E8F5EC"
TINT_RED = "#FCEAE8"
TINT_GREY = "#ECEFF1"

W, H = 10.80, 6.55
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.55, 6.15, "\"less than\" is read backwards",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# the phrase itself, on a quiet card, because it is the thing in dispute
ax.add_patch(FancyBboxPatch((3.35, 5.45 - 0.34), 4.10, 0.68,
                            boxstyle="round,pad=0.05,rounding_size=0.14",
                            facecolor=TINT_GREY, edgecolor=GREY,
                            linewidth=1.8, zorder=3))
ax.text(5.40, 5.45, '"$3$ less than $2g$"',
        ha="center", va="center", fontsize=17, color=INK, zorder=4)

# the divider, so the two readings never look like one line of working
ax.plot([5.40, 5.40], [0.70, 4.85], linewidth=1.4, color=GREY,
        linestyle=(0, (4, 4)), zorder=1)

# (centre x, colour, tint, column heading, the reading, where it starts)
COLUMNS = (
    (2.80, RED, TINT_RED, "the reading people write first",
     r"$3 - 2g$", "starts at $3$ and takes $2g$ away"),
    (8.00, GREEN, TINT_GREEN, "the reading that is right",
     r"$2g - 3$", "starts at $2g$ and takes $3$ away"),
)
for xc, colour, tint, heading, reading, starts in COLUMNS:
    ax.text(xc, 4.50, heading, ha="center", va="center", fontsize=13,
            color=colour)
    ax.add_patch(FancyBboxPatch((xc - 1.70, 3.72 - 0.42), 3.40, 0.84,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=tint, edgecolor=colour,
                                linewidth=2.2, zorder=3))
    ax.text(xc, 3.72, reading, ha="center", va="center", fontsize=21,
            color=INK, zorder=4)
    ax.text(xc, 3.02, starts, ha="center", va="center", fontsize=13,
            color=GREY)

# only the left reading is struck out, and the stroke matches its width
ax.plot([2.80 - 0.62, 2.80 + 0.62], [3.70, 3.74], linewidth=2.6,
        color=RED, solid_capstyle="round", zorder=5)

# the band that settles it: swap the letter for a number you can check
ax.add_patch(FancyBboxPatch((0.55, 2.10 - 0.27), 9.70, 0.54,
                            boxstyle="round,pad=0.05,rounding_size=0.14",
                            facecolor=TINT_GREY, edgecolor=GREY,
                            linewidth=1.6, zorder=2))
ax.text(5.40, 2.10, "put a number you already know in place of $2g$: "
        "\"$3$ less than $10$\" is $7$", ha="center", va="center",
        fontsize=14.5, color=INK, zorder=4)

# the same two readings, now in plain arithmetic, with the verdict below
NUMBERS = (
    (2.80, RED, r"$3 - 10 = -7$", "not $7$"),
    (8.00, GREEN, r"$10 - 3 = 7$", "this is the one"),
)
for xc, colour, line, verdict in NUMBERS:
    ax.text(xc, 1.48, line, ha="center", va="center", fontsize=18,
            color=colour)
    ax.text(xc, 0.86, verdict, ha="center", va="center", fontsize=13,
            color=colour)

ax.text(0.55, 0.22, "the base comes first in the subtraction, whatever "
        "order the english puts the words in", ha="left", va="center",
        fontsize=13.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_less_than_turns_round.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_02_less_than_turns_round.png")
