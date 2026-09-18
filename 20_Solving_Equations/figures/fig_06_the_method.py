"""Figure 6 - the whole method, including the loop.

Four boxes left to right, and one arrow that goes back. The loop is the
part a flat list of steps cannot show: you keep asking the same question
until the letter is alone, and only then do you check.

The return arrow is routed underneath the row, so the gap below the boxes
has to be left empty down to about y = 1.30.

Vertical plan (y, top to bottom):
    4.25  heading
    3.85  the "yes" label, clear of the box tops at 3.50
    2.95  the row of boxes (height 1.10, so 2.40 to 3.50)
    1.45  the lowest point of the return arrow
    1.15  the "no" label under it
    0.35  closing note

Run with:  python figures/fig_06_the_method.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # the question about the letter
ORANGE = "#E67E22"        # the move being made
GREEN = "#1E8449"         # the finished answer
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"

W, H = 11.80, 4.80
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.40, 4.25, "the method, from the first line to the check",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

BOX_Y, BOX_H, BOX_W = 2.95, 1.10, 2.40
X0 = [0.40, 3.20, 6.00, 8.80]

BOXES = [
    ("what has been done\nto the letter?", BLUE, TINT_BLUE),
    ("undo the last one,\non both sides", ORANGE, TINT_ORANGE),
    ("is the letter\nalone now?", BLUE, TINT_BLUE),
    ("put the answer back\nin and check", GREEN, TINT_GREEN),
]

for x0, (label, edge, face) in zip(X0, BOXES):
    ax.add_patch(FancyBboxPatch((x0, BOX_Y - BOX_H / 2), BOX_W, BOX_H,
                                boxstyle="round,pad=0.05,rounding_size=0.16",
                                facecolor=face, edgecolor=edge,
                                linewidth=2.2, zorder=3))
    ax.text(x0 + BOX_W / 2, BOX_Y, label, ha="center", va="center",
            fontsize=15, color=INK, zorder=4, linespacing=1.5)

# the three forward arrows, drawn in the 0.40 gaps between boxes
for x0 in X0[:-1]:
    ax.add_patch(FancyArrowPatch((x0 + BOX_W + 0.06, BOX_Y),
                                 (x0 + BOX_W + 0.34, BOX_Y),
                                 arrowstyle="-|>", mutation_scale=17,
                                 linewidth=2.2, color=GREY, zorder=5))

ax.text(X0[3] - 0.20, 3.85, "yes", ha="center", va="center", fontsize=15,
        color=GREEN, fontweight="bold")

# the return arrow: out of the bottom of box 3, round and back into box 1
ax.add_patch(FancyArrowPatch((X0[2] + BOX_W / 2, BOX_Y - BOX_H / 2 - 0.05),
                             (X0[0] + BOX_W / 2, BOX_Y - BOX_H / 2 - 0.05),
                             connectionstyle="arc,angleA=-90,angleB=-90,"
                                             "armA=75,armB=75,rad=18",
                             arrowstyle="-|>", mutation_scale=17,
                             linewidth=2.2, color=ORANGE, zorder=5))
ax.text((X0[0] + X0[2] + BOX_W) / 2, 1.15, "no - go round again",
        ha="center", va="center", fontsize=15, color=ORANGE,
        fontweight="bold")

ax.text(0.40, 0.35, "a one-step equation goes round the loop once; a "
        "two-step equation goes round it twice", ha="left", va="center",
        fontsize=15, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_06_the_method.png", dpi=170, facecolor="white",
            bbox_inches="tight")
print("saved", out / "fig_06_the_method.png")
