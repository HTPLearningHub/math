"""Figure 5 - what forgetting the place holder actually costs.

Left panel, in red: the second row written as 425 instead of 4250. Right
panel, in green: the same work done properly. The two answers are 1275 and
5100.

The red answer is not a small slip. Without the zero, the 1 in 12 is treated
as one instead of ten, so the question silently becomes 425 x 3 - and
425 x 3 = 1275 is exactly the wrong answer. The line at the bottom of the red
panel says so, because that is the sentence that makes the mistake stick.

Red for the wrong method and green for the right one is the same pair used in
Chapter 2 figure 7 and Chapter 5 figure 3.

The axes fills the whole figure, so one unit on the axes is exactly one inch,
and single mono-spaced characters can be placed by hand: at font size FS a
DejaVu Sans Mono character is FS/72 * 0.602 inches wide.
Run with:  python figures/fig_05_missing_zero.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

RED = "#C0392B"         # the wrong method
RED_FILL = "#FDEDEC"
GREEN = "#1E8449"       # the right method
GREEN_FILL = "#EAF6EE"
ORANGE = "#E67E22"      # the place holder itself
GREY = "#78909C"
INK = "#212121"
MONO = "DejaVu Sans Mono"

W, H = 12.40, 5.00      # figure size in inches = size of the axes in units
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

FS = 30                             # font size of the digits
CH = FS / 72 * 0.602                # width of one mono character, in units


def panel(x0, colour, fill, heading, second_row, answer, verdict, moral,
          holder=False):
    """Draw one of the two panels. Everything inside it is placed from x0."""
    ax.add_patch(FancyBboxPatch((x0, 0.35), 5.55, 4.20,
                                boxstyle="round,pad=0.05,rounding_size=0.15",
                                facecolor=fill, edgecolor=colour, linewidth=2.0))
    ax.text(x0 + 2.78, 4.15, heading, ha="center", va="center",
            fontsize=15.5, fontweight="bold", color=colour)

    xr = x0 + 2.35                  # right end of every row of digits here

    def row(y, text, col=INK):
        ax.text(xr, y, text, ha="right", va="center",
                fontsize=FS, family=MONO, color=col, zorder=3)

    row(3.55, " 425")
    row(2.95, "  12")
    ax.text(xr - 4.1 * CH, 2.95, r"$\times$", ha="right", va="center",
            fontsize=FS - 5, color=INK)
    ax.plot([xr - 4.7 * CH, xr + 0.08], [2.62, 2.62], color=INK, linewidth=2.0)

    row(2.22, " 850")
    # The second row is the row where the two panels differ, so it is written
    # one character at a time, right aligned. That way the place holder can be
    # orange and larger without any glyph being printed on top of another one.
    for i, char in enumerate(reversed(second_row)):
        is_holder = holder and i == 0
        ax.text(xr - (i + 0.5) * CH, 1.60, char, ha="center", va="center",
                fontsize=FS + 6 if is_holder else FS, family=MONO,
                color=ORANGE if is_holder else colour,
                fontweight="bold" if is_holder else "normal", zorder=3)
    ax.text(xr - 4.7 * CH, 1.60, "+", ha="right", va="center",
            fontsize=FS - 5, family=MONO, color=INK)
    ax.plot([xr - 4.7 * CH, xr + 0.08], [1.26, 1.26], color=INK, linewidth=2.0)
    row(0.86, answer, colour)

    ax.text(xr + 0.55, 1.60, verdict, ha="left", va="center",
            fontsize=13.5, color=colour, fontweight="bold")
    ax.text(x0 + 2.78, 0.62, moral, ha="center", va="center",
            fontsize=13, color=colour, fontweight="bold")


panel(0.30, RED, RED_FILL, "wrong: the place holder was forgotten",
      " 425", "1275",
      "only $425$ here,\nso the $1$ was\ncounted as one,\nnot as ten",
      r"this is really $425 \times 3$, not $425 \times 12$")

panel(6.55, GREEN, GREEN_FILL, "right: the place holder is there",
      "4250", "5100",
      "$4250$ here, because\nthe $1$ in $12$ means\nten $425$s",
      r"$425 \times 12 = 5100$", holder=True)

ax.text(6.20, 0.10, "one missing digit, and the answer is out by $3825$",
        ha="center", va="center", fontsize=13, color=GREY, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_missing_zero.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
