"""Figure 3 - the standard algorithm for 425 x 12, with its two partial products.

The whole chapter is in this picture. The bottom number 12 is made of a 2 in
the ones place and a 1 in the tens place, so the work splits into two rows:
425 x 2 and 425 x 10. Each row is coloured to match the digit that produced
it, blue for the ones digit and orange for the tens digit, so the reader can
see which digit is responsible for which row.

The orange 0 at the end of the second row is the place holder. It is the digit
the whole method stands on, so it is written in a larger size than the rest of
its row and is named by the arrow on the right.

The axes fills the whole figure, so one unit on the axes is exactly one inch,
and single mono-spaced characters can be placed by hand: at font size FS a
DejaVu Sans Mono character is FS/72 * 0.602 inches wide.
Run with:  python figures/fig_03_two_partial_products.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # everything that comes from the ones digit of 12
ORANGE = "#E67E22"      # everything that comes from the tens digit of 12
GREY = "#78909C"
INK = "#212121"
MONO = "DejaVu Sans Mono"

W, H = 10.30, 5.20      # figure size in inches = size of the axes in units
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

FS = 34                             # font size of the digits
CH = FS / 72 * 0.602                # width of one mono character, in units
XR = 3.45                           # right end of every row of digits
LX = 4.05                           # where the explanation beside a row starts

ax.add_patch(FancyBboxPatch((0.35, 0.30), 9.60, 4.55,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor="#FAFAFA", edgecolor=GREY, linewidth=1.8))


def digits(y, text, colour=INK):
    """Write mono-spaced text so that its last character ends at XR."""
    ax.text(XR, y, text, ha="right", va="center",
            fontsize=FS, family=MONO, color=colour, zorder=3)


def note(y, text, colour):
    """Write the sentence that belongs to the row at height y."""
    ax.text(LX, y, text, ha="left", va="center",
            fontsize=15, color=colour, fontweight="bold")


# ---- the two numbers being multiplied ---------------------------------------
digits(4.32, "425")
# 12 is written one character at a time, so each digit can carry its own colour
for char, n, colour in [("1", 1.5, ORANGE), ("2", 0.5, BLUE)]:
    ax.text(XR - n * CH, 3.64, char, ha="center", va="center", fontsize=FS,
            family=MONO, color=colour, fontweight="bold", zorder=3)
ax.text(XR - 3.2 * CH, 3.64, r"$\times$", ha="right", va="center",
        fontsize=FS - 6, color=INK)
ax.plot([XR - 4.0 * CH, XR + 0.08], [3.24, 3.24], color=INK, linewidth=2.2)

# ---- first partial product: 425 x 2 -----------------------------------------
digits(2.80, "850", BLUE)
note(2.80, r"$425 \times 2 = 850$", BLUE)

# ---- second partial product: 425 x 10, with the place holder ----------------
for char, n in [("4", 3.5), ("2", 2.5), ("5", 1.5)]:
    ax.text(XR - n * CH, 1.96, char, ha="center", va="center", fontsize=FS,
            family=MONO, color=ORANGE, zorder=3)
ax.text(XR - 0.5 * CH, 1.96, "0", ha="center", va="center", fontsize=FS + 8,
        family=MONO, color=ORANGE, fontweight="bold", zorder=3)
ax.text(XR - 4.6 * CH, 1.96, "+", ha="right", va="center",
        fontsize=FS - 6, family=MONO, color=INK)
note(1.96, r"$425 \times 10 = 4250$", ORANGE)

# the arrow that names the place holder. It comes in from the lower right,
# through empty page: it crosses neither a digit nor the line under the rows.
ax.annotate("", xy=(XR - 0.5 * CH + 0.06, 1.76), xytext=(4.62, 1.54),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, linewidth=2.0,
                            mutation_scale=16))
ax.text(4.74, 1.50, "the place holder", ha="left", va="center",
        fontsize=14, color=ORANGE, fontweight="bold")

# ---- the sum of the two rows ------------------------------------------------
ax.plot([XR - 4.6 * CH, XR + 0.08], [1.52, 1.52], color=INK, linewidth=2.2)
digits(1.08, "5100")
note(1.08, r"$850 + 4250 = 5100$", INK)

ax.text(5.15, 0.62, "two rows, because the bottom number has two digits"
                    " - and they are added, not multiplied",
        ha="center", va="center", fontsize=13, color=GREY, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_two_partial_products.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
