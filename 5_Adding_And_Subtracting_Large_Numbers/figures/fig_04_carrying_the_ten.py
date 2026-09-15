"""Figure 4 - what carrying actually does, and where the two digits go.

Left panel: the tens column of 1293 + 2614 makes 9 tens + 1 ten = 10 tens. Ten
tens do not fit in a column that holds one digit, so they are traded for one
hundred, and nothing is left behind in the tens.
Right panel: the same two results written in the right places - the traded
hundred as a small carried 1 on top of the hundreds column, and the 0 in the
tens column of the answer. Both of those digits are orange, and so is the name
of the tens column, so the eye can follow them without any extra arrows.

Orange is the colour this book uses for the piece that moves, so the traded
hundred, the carried 1 and the 0 are all orange.

The axes fills the whole figure, so one unit on the axes is exactly one inch,
and single mono-spaced characters can be placed by hand: at font size FS a
DejaVu Sans Mono character is FS/72 * 0.602 inches wide.
Run with:  python figures/fig_04_carrying_the_ten.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # the tens we already have
BLUE_FILL = "#EAF2FB"
ORANGE = "#E67E22"      # the piece that moves, and the digits it becomes
ORANGE_FILL = "#FDF0E3"
GREY = "#78909C"
GREY_FILL = "#ECEFF1"
INK = "#212121"
MONO = "DejaVu Sans Mono"

W, H = 13.0, 5.0        # figure size in inches = size of the axes in units
Y_BOTTOM = 1.20         # the drawing starts here, so H units still equal H inches
FS = 26                 # font size of the digits in the right panel
CH = FS / 72 * 0.602    # width of one mono character, in units

fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(Y_BOTTOM, Y_BOTTOM + H)

# ============================================================== left panel ===
ax.add_patch(FancyBboxPatch((0.40, 1.40), 5.30, 4.35,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor="#FAFAFA", edgecolor=GREY, linewidth=1.8))
ax.text(3.05, 5.45, "Ten tens will not fit in one column",
        ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

SIZE = 0.36                         # side of one ten-token
BAND = 4.20                         # the ten tokens are squeezed into this width
X0 = 0.95
gap = (BAND - 10 * SIZE) / 9
for i in range(10):
    x = X0 + i * (SIZE + gap)
    ax.add_patch(FancyBboxPatch((x, 4.75 - SIZE / 2), SIZE, SIZE,
                                boxstyle="round,pad=0.01,rounding_size=0.04",
                                facecolor=BLUE_FILL, edgecolor=BLUE, linewidth=1.5))
    ax.text(x + SIZE / 2, 4.75, "10", ha="center", va="center",
            fontsize=8.5, color=BLUE)
ax.text(3.05, 4.35, r"$9$ tens $+$ $1$ ten $=$ $10$ tens",
        ha="center", va="top", fontsize=13, color=BLUE, fontweight="bold")

ax.annotate("", xy=(3.05, 3.45), xytext=(3.05, 4.02),
            arrowprops=dict(arrowstyle="-|>", color=INK, linewidth=2.0,
                            mutation_scale=18))

# the two things the ten tens turn into
BOX = 0.85
for cx, fill, edge, label, caption in [
        (1.95, ORANGE_FILL, ORANGE, "100", "one hundred:\ncarry it left"),
        (4.15, GREY_FILL, GREY, "0", "no tens left:\nwrite $0$ here")]:
    ax.add_patch(FancyBboxPatch((cx - BOX / 2, 2.95 - BOX / 2), BOX, BOX,
                                boxstyle="round,pad=0.01,rounding_size=0.07",
                                facecolor=fill, edgecolor=edge, linewidth=2.2))
    ax.text(cx, 2.95, label, ha="center", va="center",
            fontsize=15, color=edge, fontweight="bold")
    ax.text(cx, 2.38, caption, ha="center", va="top",
            fontsize=11.5, color=edge, fontweight="bold")

# ============================================================= right panel ===
ax.add_patch(FancyBboxPatch((6.70, 1.40), 5.90, 4.35,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor="#FAFAFA", edgecolor=GREY, linewidth=1.8))
ax.text(9.65, 5.45, "where those two digits go",
        ha="center", va="center", fontsize=15, fontweight="bold", color=INK)

XR = 9.45                           # right end of every row of digits
tens_x = XR - 1.5 * CH              # centre of the tens column
hund_x = XR - 2.5 * CH              # centre of the hundreds column

# no shading behind the tens column: any band wide enough to see would also
# touch the digits beside it. The orange 0 and the orange column name are enough.


def digits(y, text, colour=INK):
    """Write mono-spaced text so that its last character ends at XR."""
    ax.text(XR, y, text, ha="right", va="center",
            fontsize=FS, family=MONO, color=colour, zorder=3)


ax.text(hund_x, 4.80, "1", ha="center", va="center",        # the carried hundred
        fontsize=15, family=MONO, color=ORANGE, fontweight="bold", zorder=3)
digits(4.20, "1293")
digits(3.55, "2614")
ax.text(XR - 5.0 * CH, 3.55, "+", ha="right", va="center",
        fontsize=FS - 3, family=MONO, color=INK)
ax.plot([XR - 4.9 * CH, XR + 0.10], [3.15, 3.15], color=INK, linewidth=2.0)
# the answer is written one character at a time, each centred on its own column,
# so that the 0 can be orange without any risk of two glyphs overlapping
for char, n in [("3", 3.5), ("9", 2.5), ("0", 1.5), ("7", 0.5)]:
    ax.text(XR - n * CH, 2.65, char, ha="center", va="center", fontsize=FS,
            family=MONO, color=ORANGE if char == "0" else INK, zorder=3)

# the name of each column, written downwards under the answer
for label, n in [("thousands", 3.5), ("hundreds", 2.5), ("tens", 1.5), ("ones", 0.5)]:
    x = XR - n * CH
    colour = ORANGE if label == "tens" else GREY
    ax.plot([x, x], [2.28, 2.16], color=colour, linewidth=1.4)
    ax.text(x, 2.12, label, ha="right", va="top", rotation=45,
            fontsize=10, color=colour, fontweight="bold")

ax.text(11.25, 4.80, "the traded hundred, written\nsmall on top of the\nhundreds column",
        ha="center", va="center", fontsize=11.5, color=ORANGE)
ax.text(11.25, 2.75, "the $0$ that was left\nin the tens column",
        ha="center", va="center", fontsize=11.5, color=ORANGE)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_carrying_the_ten.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
