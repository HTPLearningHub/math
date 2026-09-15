"""Figure 3 - whole numbers are lined up on the RIGHT, never on the left.

Left panel: 473 and 28 with their FIRST digits under each other. The 2 lands in
the hundreds column and the 8 in the tens column, so 28 is silently turned into
280 and the answer comes out as 753.
Right panel: the same two numbers with their LAST digits under each other. Ones
sit under ones, and the answer is 501.

Both panels carry the same column names under the answer, so the reader can see
exactly which column each digit fell into. Every arrow is routed through empty
space, so no line ever runs across a digit.

The axes fills the whole figure, so one unit on the axes is exactly one inch.
That lets the script place single characters by hand: at font size FS the
DejaVu Sans Mono character is FS/72 * 0.602 inches wide. Same trick as
Chapter 2's fig_07.
Run with:  python figures/fig_03_align_on_the_right.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

WRONG = "#C0392B"       # red   - the panel that must not be copied
RIGHT = "#1E8449"       # green - the panel that works
INK = "#212121"
MONO = "DejaVu Sans Mono"

W, H = 12.4, 5.9        # figure size in inches = size of the axes in units
FS = 27                 # font size of the digits
CH = FS / 72 * 0.602    # width of one character of the mono font, in units

Y_TOP = 4.05            # the first number
Y_BOT = 3.30            # the second number
Y_LINE = 2.90           # the horizontal line
Y_SUM = 2.40            # the answer

fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])               # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0.5, H)

ax.text(W / 2, 5.58, "Line up the last digits, never the first ones",
        ha="center", va="center", fontsize=18, fontweight="bold", color=INK)


def digits(x_right, y, text, colour=INK):
    """Write mono-spaced text so that its last character ends at x_right."""
    ax.text(x_right, y, text, ha="right", va="center",
            fontsize=FS, family=MONO, color=colour)


def column_names(x_right, colour):
    """Write hundreds / tens / ones under the three columns ending at x_right."""
    for label, n in [("hundreds", 2.5), ("tens", 1.5), ("ones", 0.5)]:
        x = x_right - n * CH
        ax.plot([x, x], [2.05, 1.92], color=colour, linewidth=1.4)
        ax.text(x, 1.88, label, ha="right", va="top", rotation=45,
                fontsize=10.5, color=colour, fontweight="bold")


def sum_line(x_right):
    """The horizontal line, and the plus sign to the left of the second row."""
    ax.text(x_right - 4.2 * CH, Y_BOT, "+", ha="right", va="center",
            fontsize=FS - 3, family=MONO, color=INK)
    ax.plot([x_right - 4.1 * CH, x_right + 0.10], [Y_LINE, Y_LINE],
            color=INK, linewidth=2.0)


# ----------------------------------------------------------------- left panel
ax.add_patch(FancyBboxPatch((0.35, 0.75), 5.3, 4.25,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor="#FDECEA", edgecolor=WRONG, linewidth=2.4))
ax.text(3.0, 4.70, "WRONG: lined up on the left", ha="center", va="center",
        fontsize=15, fontweight="bold", color=WRONG)

xl = 4.35                                   # right end of the three-digit rows
digits(xl, Y_TOP, "473")
digits(xl - CH, Y_BOT, "28")                # 28 pushed one character to the left
sum_line(xl)
digits(xl, Y_SUM, "753", colour=WRONG)
column_names(xl, WRONG)

# mark the 2, which has landed in the hundreds column
ax.add_patch(Rectangle((xl - 3 * CH, Y_BOT - 0.31), CH, 0.62,
                       facecolor="none", edgecolor=WRONG,
                       linewidth=1.8, linestyle=(0, (3, 2)), zorder=3))
ax.annotate("The $2$ has landed in\nthe hundreds column,\n"
            "so $28$ is being added\nas $280$.",
            xy=(xl - 3 * CH, Y_BOT), xytext=(1.75, Y_BOT),
            ha="center", va="center", fontsize=11, color=WRONG,
            arrowprops=dict(arrowstyle="-|>", color=WRONG, linewidth=1.8,
                            mutation_scale=16))

# ---------------------------------------------------------------- right panel
ax.add_patch(FancyBboxPatch((6.75, 0.75), 5.3, 4.25,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor="#E9F7EF", edgecolor=RIGHT, linewidth=2.4))
ax.text(9.4, 4.70, "RIGHT: lined up on the right", ha="center", va="center",
        fontsize=15, fontweight="bold", color=RIGHT)

xr = 10.40                                  # right end of every row
digits(xr, Y_TOP, "473")
digits(xr, Y_BOT, " 28")
sum_line(xr)
digits(xr, Y_SUM, "501", colour=RIGHT)
column_names(xr, RIGHT)

# no arrow is needed here: the column names below the answer already point
# at the columns, and an arrow would have to cross the digits to reach them
ax.text(8.15, Y_BOT + 0.10,
        "Ones under ones,\ntens under tens,\nhundreds under\nhundreds.",
        ha="center", va="center", fontsize=11, color=RIGHT)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_align_on_the_right.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
