"""Figure 2 - multiplying 425 by 2 in columns, one column at a time.

Left panel: the finished piece of work. The small orange 1 above the tens
column is the carried ten, exactly the same kind of digit as the carried 1 of
Chapter 5, so it is drawn in the same colour and the same small size.

Right panel: the three steps that produced it, written in the order they are
done - ones first, then tens, then hundreds. Each step says what is
multiplied, what is written and what is carried, so the reader can match every
digit on the left to one line on the right. The four x positions are fixed by
hand (NUM_X, NAME_X, SUM_X, ACT_X) so that the three lines line up in four
straight columns; padding a string with spaces would not, because the maths is
not set in a mono-spaced font.

The axes fills the whole figure, so one unit on the axes is exactly one inch,
and single mono-spaced characters can be placed by hand: at font size FS a
DejaVu Sans Mono character is FS/72 * 0.602 inches wide.
Run with:  python figures/fig_02_one_digit_column.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # the number we are multiplying
ORANGE = "#E67E22"      # the piece that moves: the carried ten
GREY = "#78909C"
INK = "#212121"
MONO = "DejaVu Sans Mono"

W, H = 13.20, 4.30      # figure size in inches = size of the axes in units
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

FS = 34                             # font size of the digits
CH = FS / 72 * 0.602                # width of one mono character, in units
XR = 3.40                           # right end of every row of digits


def digits(y, text, colour=INK):
    """Write mono-spaced text so that its last character ends at XR."""
    ax.text(XR, y, text, ha="right", va="center",
            fontsize=FS, family=MONO, color=colour, zorder=3)


# ================================================================ left panel ==
ax.add_patch(FancyBboxPatch((0.35, 0.28), 3.80, 3.42,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor="#FAFAFA", edgecolor=GREY, linewidth=1.8))

# the carried ten, written small on top of the tens column
ax.text(XR - 1.5 * CH, 3.22, "1", ha="center", va="center",
        fontsize=17, family=MONO, color=ORANGE, fontweight="bold", zorder=3)

digits(2.70, "425", BLUE)                               # the number
digits(2.02, "  2")                                     # the single digit
ax.text(XR - 3.0 * CH, 2.02, r"$\times$", ha="right", va="center",
        fontsize=FS - 6, color=INK)
ax.plot([XR - 3.6 * CH, XR + 0.08], [1.64, 1.64], color=INK, linewidth=2.2)
digits(1.10, "850")                                     # the answer

ax.text(2.25, 0.62, r"$425 \times 2 = 850$", ha="center", va="center",
        fontsize=14, color=GREY, fontweight="bold")

# =============================================================== right panel ==
ax.add_patch(FancyBboxPatch((4.65, 0.28), 8.20, 3.42,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor="#FAFAFA", edgecolor=GREY, linewidth=1.8))
ax.text(8.75, 3.34, "the three steps, right to left",
        ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

NUM_X, NAME_X, SUM_X, ACT_X = 4.95, 5.35, 6.75, 9.05    # the four columns
STEPS = [
    (2.70, "1.", "ones", r"$5 \times 2 = 10$",
     r"write $0$,  carry $1$", ORANGE),
    (2.02, "2.", "tens", r"$(2 \times 2) + 1 = 5$",
     r"write $5$,  carry nothing", GREY),
    (1.34, "3.", "hundreds", r"$4 \times 2 = 8$",
     r"write $8$,  carry nothing", GREY),
]
for y, num, name, total, action, colour in STEPS:
    ax.text(NUM_X, y, num, ha="left", va="center",
            fontsize=15, color=GREY, fontweight="bold")
    ax.text(NAME_X, y, name + ":", ha="left", va="center", fontsize=15, color=INK)
    ax.text(SUM_X, y, total, ha="left", va="center", fontsize=15, color=INK)
    ax.text(ACT_X, y, action, ha="left", va="center",
            fontsize=15, color=colour, fontweight="bold")

CARRY_NOTE = ("the carried $1$ is one ten, so it joins the tens column" + "\n"
              + "after the multiplying, never before")
ax.text(8.75, 0.72, CARRY_NOTE,
        ha="center", va="center", fontsize=12.5, color=ORANGE, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_one_digit_column.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
