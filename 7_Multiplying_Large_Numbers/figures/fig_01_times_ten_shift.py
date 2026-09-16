"""Figure 1 - why multiplying by ten looks like "writing a zero on the end".

Top row: the number 14 sitting in its two places, tens and ones.
Bottom row: the same two digits after every one of them has been pushed one
place to the left, which is what multiplying by ten does. The ones place is
then empty, and an orange 0 is put there to hold it open, so the digits cannot
slide back.

The point of the picture is that the 0 is not "added to the number". It is the
mark that says "no ones left", exactly like the place-holding zero of
Chapter 2, section 3.3.

Colours follow the book: blue for digits that were already there, orange for
the piece that moves or appears, grey for the labels.
Run with:  python figures/fig_01_times_ten_shift.py
"""

import matplotlib
matplotlib.use("Agg")                     # draw to a file, never to a window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"                          # digits that were already there
BLUE_FILL = "#EAF2FB"
ORANGE = "#E67E22"                        # the zero that appears
ORANGE_FILL = "#FDF0E3"
GREY = "#78909C"
GREY_FILL = "#ECEFF1"
INK = "#212121"

W, H = 11.0, 5.4                          # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])             # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BOXW, BOXH = 1.30, 1.10                   # one place-value box
COLS = ["hundreds", "tens", "ones"]       # left to right, biggest place first
CX = [4.55, 6.15, 7.75]                   # centre of each column
Y_TOP = 3.80                              # centre of the top row of boxes
Y_BOT = 1.35                              # centre of the bottom row of boxes


def box(cx, cy, text, edge, fill):
    """Draw one place-value box with one digit inside it."""
    ax.add_patch(FancyBboxPatch((cx - BOXW / 2, cy - BOXH / 2), BOXW, BOXH,
                                boxstyle="round,pad=0.02,rounding_size=0.10",
                                facecolor=fill, edgecolor=edge, linewidth=2.2))
    ax.text(cx, cy, text, ha="center", va="center",
            fontsize=30, color=edge, fontweight="bold")


# ---- the column names, written once, above everything -----------------------
for cx, name in zip(CX, COLS):
    ax.text(cx, 4.95, name, ha="center", va="center",
            fontsize=13, color=GREY, fontweight="bold")

# ---- top row: 14, with an empty hundreds box --------------------------------
box(CX[0], Y_TOP, "", GREY, GREY_FILL)    # 14 has no hundreds
box(CX[1], Y_TOP, "1", BLUE, BLUE_FILL)
box(CX[2], Y_TOP, "4", BLUE, BLUE_FILL)
ax.text(3.55, Y_TOP, r"$14$", ha="right", va="center",
        fontsize=24, color=INK, fontweight="bold")

# ---- the two arrows: every digit moves one place to the left ----------------
for src, dst in [(CX[1], CX[0]), (CX[2], CX[1])]:
    ax.annotate("", xy=(dst, Y_BOT + BOXH / 2 + 0.06),
                xytext=(src, Y_TOP - BOXH / 2 - 0.06),
                arrowprops=dict(arrowstyle="-|>", color=BLUE, linewidth=2.4,
                                mutation_scale=20,
                                connectionstyle="arc3,rad=0.18"))
ax.text(8.75, 2.58, "every digit moves\none place to the left",
        ha="left", va="center", fontsize=13, color=BLUE, fontweight="bold")

# ---- bottom row: 140, with the orange place holder --------------------------
box(CX[0], Y_BOT, "1", BLUE, BLUE_FILL)
box(CX[1], Y_BOT, "4", BLUE, BLUE_FILL)
box(CX[2], Y_BOT, "0", ORANGE, ORANGE_FILL)
ax.text(3.55, Y_BOT, r"$140$", ha="right", va="center",
        fontsize=24, color=INK, fontweight="bold")
ax.text(8.75, Y_BOT, "no ones are left,\nso a $0$ holds the place",
        ha="left", va="center", fontsize=13, color=ORANGE, fontweight="bold")

# ---- the label on the left, saying what happened between the rows -----------
ax.text(0.55, 2.58, r"$\times\, 10$", ha="left", va="center",
        fontsize=26, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_times_ten_shift.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
