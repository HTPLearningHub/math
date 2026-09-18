"""Figure 7 - two ways of splitting 72, and why only one of them finishes.

The method is "pull out a perfect square". The step everybody gets wrong
is pulling out a perfect square that is not the biggest one: the answer is
not wrong, it is unfinished, and the figure has to show that difference
rather than assert it.

Left panel:  72 = 36 x 2, the largest perfect square. Done in one pass.
Right panel: 72 = 4 x 18. Also legal, also true, but 18 still hides a 9,
             so a second pass is needed - and it arrives at the same answer.

Both columns end at 6 root 2, which is the point: the destination is the
same, only the number of passes changes.

Colour convention:
    blue   - the working
    green  - a finished answer
    red    - an answer that is not finished yet
    grey   - the notes

Horizontal plan (x): left panel 0.40-6.30 with its column centred at
    3.35; right panel 6.70-12.60 with its column centred at 9.65.

Vertical plan (y, top to bottom):
    7.40  figure heading
    6.80  top of both panels
    6.35  the sub-heading of each panel
    5.65  step 1        4.35  step 3
    5.00  step 2        3.70  step 4
    3.00  the verdict badge
    2.35  the note that the right-hand column is not done (right only)
    1.70  its second pass (right only)
    1.10  its final answer (right only)
    0.55  bottom of both panels
    0.20  the closing sentence

Run with:  python figures/fig_07_simplifying_root_72.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # the working
GREEN = "#1E8449"       # a finished answer
RED = "#C0392B"         # an answer still carrying a perfect square
GREY = "#78909C"
INK = "#212121"
GREEN_T = "#E8F5EC"
RED_T = "#FBEAE8"

W, H = 13.00, 7.80
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def panel(x_left, x_right, colour):
    """The rounded outline behind one column of working."""
    ax.add_patch(FancyBboxPatch(
        (x_left, 0.55), x_right - x_left, 6.25,
        boxstyle="round,pad=0.0,rounding_size=0.18",
        facecolor="white", edgecolor=colour, linewidth=1.8, zorder=0))


def badge(x, y, text, edge, fill):
    """A rounded box carrying the verdict of a column."""
    ax.text(x, y, text, ha="center", va="center", fontsize=17, color=INK,
            zorder=3,
            bbox=dict(boxstyle="round,pad=0.40", facecolor=fill,
                      edgecolor=edge, linewidth=1.9))


ax.text(0.40, 7.40,
        "both splits of $72$ are legal; only the one that takes the "
        "largest perfect square finishes in one go",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# ================================================================ left panel
panel(0.40, 6.30, GREEN)
ax.text(3.35, 6.35, "take the largest perfect square, $36$", ha="center",
        va="center", fontsize=15.5, color=INK, fontweight="bold")

for y, line in ((5.65, r"$\sqrt{72}$"),
                (5.00, r"$= \sqrt{36 \times 2}$"),
                (4.35, r"$= \sqrt{36} \times \sqrt{2}$"),
                (3.70, r"$= 6\sqrt{2}$")):
    ax.text(3.35, y, line, ha="center", va="center", fontsize=21,
            color=BLUE)

badge(3.35, 3.00, r"finished - $2$ is not a perfect square", GREEN, GREEN_T)

# =============================================================== right panel
panel(6.70, 12.60, RED)
ax.text(9.65, 6.35, "take a smaller perfect square, $4$", ha="center",
        va="center", fontsize=15.5, color=INK, fontweight="bold")

for y, line in ((5.65, r"$\sqrt{72}$"),
                (5.00, r"$= \sqrt{4 \times 18}$"),
                (4.35, r"$= \sqrt{4} \times \sqrt{18}$"),
                (3.70, r"$= 2\sqrt{18}$")):
    ax.text(9.65, y, line, ha="center", va="center", fontsize=21,
            color=BLUE)

badge(9.65, 3.00, r"not finished - $18 = 9 \times 2$", RED, RED_T)

ax.text(9.65, 2.35, "so go round once more:", ha="center", va="center",
        fontsize=14, color=GREY, style="italic")
ax.text(9.65, 1.72, r"$2\sqrt{18} = 2 \times \sqrt{9} \times \sqrt{2}$",
        ha="center", va="center", fontsize=19, color=BLUE)
ax.text(9.65, 1.10, r"$= 2 \times 3 \times \sqrt{2} = 6\sqrt{2}$",
        ha="center", va="center", fontsize=19, color=GREEN)

ax.text(6.50, 0.20,
        "the two columns end on the same number, so the smaller split is "
        "not wrong - it is just slower",
        ha="center", va="center", fontsize=13.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_07_simplifying_root_72.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_07_simplifying_root_72.png")
