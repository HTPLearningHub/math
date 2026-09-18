"""Figure 2 - how to decide whether the circle is hollow or filled.

The rule "hollow for > and <, filled for >= and <=" is easy to state and
easy to forget. The test behind it never has to be remembered, because it
is one line of arithmetic: put the boundary number itself into the
inequality and see whether the statement comes out true.

Two panels, one per symbol, built from exactly the same five rows so the
reader's eye compares row against row:

    the inequality  ->  the boundary put in  ->  true or false
                    ->  the verdict          ->  the circle it produces

The tick and the cross are drawn as line segments, not as characters, so
the figure does not depend on the font carrying those glyphs.

Horizontal plan (x): two panels of equal width, 0.45 to 5.85 and 6.15 to
11.55, each with its contents centred on 3.15 and 8.85.

Vertical plan (y, top to bottom):
    5.90  heading
    5.45  top of both panels
    4.95  the inequality
    4.32  what the test is
    3.72  the boundary number put in
    3.00  the tick or the cross
    2.38  the verdict
    1.68  a short piece of number line with the circle on it
    1.32  the boundary number under it
    0.98  what the circle is called
    0.75  bottom of both panels
    0.28  closing note

Run with:  python figures/fig_02_which_circle.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

GREEN = "#1E8449"         # the boundary belongs to the solution set
RED = "#C0392B"           # the boundary does not
GREY = "#78909C"
INK = "#212121"
GREEN_T = "#E8F5EC"
RED_T = "#FCEAE8"

W, H = 12.00, 6.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def panel(x_left, x_right, colour, tint):
    """The rounded background of one panel."""
    ax.add_patch(FancyBboxPatch(
        (x_left, 0.75), x_right - x_left, 4.70,
        boxstyle="round,pad=0.0,rounding_size=0.18",
        facecolor=tint, edgecolor=colour, linewidth=1.8, zorder=0))


def cross(cx, cy, size, colour):
    """A cross drawn from two strokes - no font glyph involved."""
    ax.plot([cx - size, cx + size], [cy - size, cy + size],
            linewidth=4.5, color=colour, solid_capstyle="round", zorder=3)
    ax.plot([cx - size, cx + size], [cy + size, cy - size],
            linewidth=4.5, color=colour, solid_capstyle="round", zorder=3)


def tick(cx, cy, size, colour):
    """A tick drawn from two strokes, for the same reason."""
    ax.plot([cx - size, cx - size * 0.15], [cy + size * 0.05, cy - size],
            linewidth=4.5, color=colour, solid_capstyle="round", zorder=3)
    ax.plot([cx - size * 0.15, cx + size * 1.05],
            [cy - size, cy + size * 0.95],
            linewidth=4.5, color=colour, solid_capstyle="round", zorder=3)


def circle_on_line(cx, cy, colour, filled):
    """A short piece of number line carrying the resulting circle."""
    ax.plot([cx - 1.30, cx + 1.30], [cy, cy], linewidth=1.8, color=INK,
            zorder=1)
    ax.plot([cx, cx], [cy - 0.11, cy + 0.11], linewidth=1.5, color=INK,
            zorder=1)
    if filled:
        ax.plot([cx], [cy], marker="o", markersize=19, color=colour,
                zorder=4)
    else:
        ax.plot([cx], [cy], marker="o", markersize=19,
                markerfacecolor="white", markeredgecolor=colour,
                markeredgewidth=3.4, zorder=4)
    ax.text(cx, cy - 0.36, r"$3$", ha="center", va="center", fontsize=13,
            color=GREY)


ax.text(0.45, 5.90,
        "the circle is not a rule to remember - it is the answer to a question",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# ------------------------------------------------------------ left panel
panel(0.45, 5.85, RED, RED_T)
ax.text(3.15, 4.95, r"$x > 3$", ha="center", va="center", fontsize=25,
        color=INK, fontweight="bold")
ax.text(3.15, 4.32, "put the boundary number in:", ha="center",
        va="center", fontsize=13.5, color=GREY)
ax.text(3.15, 3.72, r"$3 > 3$", ha="center", va="center", fontsize=22,
        color=INK)
cross(3.15, 3.00, 0.22, RED)
ax.text(3.15, 2.38, "false - $3$ is not greater than itself",
        ha="center", va="center", fontsize=13.5, color=RED,
        fontweight="bold")
circle_on_line(3.15, 1.68, RED, filled=False)
ax.text(3.15, 0.98, "hollow circle", ha="center", va="center",
        fontsize=14, color=RED, fontweight="bold")

# ----------------------------------------------------------- right panel
panel(6.15, 11.55, GREEN, GREEN_T)
ax.text(8.85, 4.95, r"$x \geq 3$", ha="center", va="center", fontsize=25,
        color=INK, fontweight="bold")
ax.text(8.85, 4.32, "put the boundary number in:", ha="center",
        va="center", fontsize=13.5, color=GREY)
ax.text(8.85, 3.72, r"$3 \geq 3$", ha="center", va="center", fontsize=22,
        color=INK)
tick(8.85, 3.00, 0.22, GREEN)
ax.text(8.85, 2.38, "true - $3$ is equal to itself",
        ha="center", va="center", fontsize=13.5, color=GREEN,
        fontweight="bold")
circle_on_line(8.85, 1.68, GREEN, filled=True)
ax.text(8.85, 0.98, "filled circle", ha="center", va="center",
        fontsize=14, color=GREEN, fontweight="bold")

ax.text(0.45, 0.28,
        "$\\geq$ is true when either half is true, and \"equal to\" is the "
        "half that saves the boundary number",
        ha="left", va="center", fontsize=12.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_which_circle.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_02_which_circle.png")
