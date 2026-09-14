"""Figure 7 - why the decimal points, and not the ends, must be lined up.

Left panel: 2.3 and 1.45 pushed to the right so their last digits meet.
That puts 3 tenths in the same column as 5 hundredths. Those are parts of
different size, so the column cannot be added.
Right panel: 2.3 padded to 2.30, decimal points under each other. Now every
column holds parts of one size, and the sum is 3.75.

The axes fills the whole figure, so one unit on the axes is exactly one inch.
That lets the script place single characters by hand: at font size FS the
DejaVu Sans Mono character is FS/72 * 0.602 inches wide.
Run with:  python figures/fig_07_align_decimal_points.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

WRONG = "#C0392B"       # red   - the panel that must not be copied
RIGHT = "#1E8449"       # green - the panel that works
PAD = "#E67E22"         # orange - the zero that was added
INK = "#212121"         # near black - the digits
MONO = "DejaVu Sans Mono"   # a font where every character has the same width

W, H = 12.4, 5.6        # figure size in inches = size of the axes in units
FS = 27                 # font size of the digits
CH = FS / 72 * 0.602    # width of one character of the mono font, in units

fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])               # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0.6, H)


def digits(x_right, y, text, colour=INK):
    """Write mono-spaced text so that its last character ends at x_right."""
    ax.text(x_right, y, text, ha="right", va="center",
            fontsize=FS, family=MONO, color=colour)


ax.text(W / 2, 5.25, "Line up the decimal points, never the ends",
        ha="center", va="center", fontsize=18, fontweight="bold", color=INK)

# ----------------------------------------------------------------- left panel
ax.add_patch(FancyBboxPatch((0.35, 0.80), 5.3, 4.00,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor="#FDECEA", edgecolor=WRONG, linewidth=2.4))
ax.text(3.0, 4.45, "WRONG: the ends lined up", ha="center", va="center",
        fontsize=15, fontweight="bold", color=WRONG)

x_left = 3.6                                # last digit of every row ends here
ax.add_patch(Rectangle((x_left - CH, 2.55), CH, 1.50,   # the bad column, in red
                       facecolor="#F5B7B1", edgecolor=WRONG, linewidth=1.8, zorder=1))
digits(x_left, 3.70, " 2.3")                # the leading space pushes 2.3 to the right
digits(x_left, 2.90, "1.45")
ax.text(2.30, 2.90, "+", ha="center", va="center", fontsize=FS - 3, family=MONO, color=INK)
ax.plot([2.45, x_left + 0.12], [2.48, 2.48], color=INK, linewidth=2.0)

ax.annotate("$3$ tenths lands on top of $5$ hundredths.\n"
            "They are pieces of different size,\nso this column cannot be added.",
            xy=(x_left - CH / 2, 2.55), xytext=(2.85, 1.35),
            ha="center", va="center", fontsize=11, color=WRONG,
            arrowprops=dict(arrowstyle="-|>", color=WRONG, linewidth=1.8, mutation_scale=16))

# ---------------------------------------------------------------- right panel
ax.add_patch(FancyBboxPatch((6.75, 0.80), 5.3, 4.00,
                            boxstyle="round,pad=0.05,rounding_size=0.15",
                            facecolor="#E9F7EF", edgecolor=RIGHT, linewidth=2.4))
ax.text(9.4, 4.45, "RIGHT: the points lined up", ha="center", va="center",
        fontsize=15, fontweight="bold", color=RIGHT)

x_right = 10.05                             # last digit of every row ends here
digits(x_right - CH, 3.70, " 2.3")          # 2.3 without its new zero
ax.text(x_right - CH / 2, 3.70, "0", ha="center", va="center",   # the zero we added
        fontsize=FS, family=MONO, color=PAD)
digits(x_right, 2.90, "1.45")
ax.text(8.75, 2.90, "+", ha="center", va="center", fontsize=FS - 3, family=MONO, color=INK)
ax.plot([8.90, x_right + 0.12], [2.48, 2.48], color=INK, linewidth=2.0)
digits(x_right, 2.00, "3.75", colour=RIGHT)

# the name of each column, written downwards under the sum
for label, x in [("ones", x_right - 3.5 * CH),
                 ("tenths", x_right - 1.5 * CH),
                 ("hundredths", x_right - 0.5 * CH)]:
    ax.plot([x, x], [1.70, 1.56], color=RIGHT, linewidth=1.4)
    ax.text(x, 1.52, label, ha="right", va="top", rotation=45,
            fontsize=10.5, color=RIGHT, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_07_align_decimal_points.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
