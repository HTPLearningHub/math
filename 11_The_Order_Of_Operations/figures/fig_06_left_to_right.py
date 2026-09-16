"""Figure 6 - the two traps inside a shared level.

Both rows show the same failure: the reader treats the two operations on a
level as though one of them outranked the other, because M comes before D
in the acronym and A comes before S. Each row puts the correct working
beside the invented working and prints both answers.

The wrong column carries a ringed bracket that is not in the expression.
That ring is the whole point: doing the right-hand operation first is the
same as inserting a bracket nobody wrote.
Run with:  python figures/fig_06_left_to_right.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

GREEN = "#1E8449"
RED = "#C0392B"
BLUE = "#2E86DE"             # level 3
SLATE = "#546E7A"            # level 4
GREY = "#78909C"
INK = "#212121"

W, H = 12.4, 6.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ROW_TOP = (H - 1.30, H - 3.62)            # top edge of the two rows
RH = 2.05                                 # height of one row
BOX_W = 4.68                              # width of one working box
BOX_X = (2.60, 7.52)                      # left edge of the correct / wrong box

ROWS = [
    (BLUE, "Level 3", r"$12 \div 3 \times 2$",
     "M comes before D in the acronym, so multiply first",
     [r"$12 \div 3 = 4$", r"$4 \times 2 = 8$"], r"$8$",
     [r"$3 \times 2 = 6$", r"$12 \div 6 = 2$"], r"$2$",
     r"$12 \div (3 \times 2)$"),
    (SLATE, "Level 4", r"$10 - 4 + 2$",
     "A comes before S in the acronym, so add first",
     [r"$10 - 4 = 6$", r"$6 + 2 = 8$"], r"$8$",
     [r"$4 + 2 = 6$", r"$10 - 6 = 4$"], r"$4$",
     r"$10 - (4 + 2)$"),
]

for top, (lvl_col, lvl, expr, myth, ok_steps, ok_ans,
          bad_steps, bad_ans, invented) in zip(ROW_TOP, ROWS):
    # `myth` is the misconception this row kills; it is written into the
    # chapter text beside the figure rather than onto the picture, which has
    # no room for a third line of prose per row
    cy = top - RH / 2
    # the expression, on the left, with its level tag above it
    ax.text(1.25, cy + 0.55, lvl, ha="center", va="center",
            fontsize=13, color=lvl_col, fontweight="bold")
    ax.text(1.25, cy - 0.05, expr, ha="center", va="center",
            fontsize=25, color=INK)

    for x, (edge, tint, head, steps, ans, tag) in zip(
            BOX_X,
            [(GREEN, "#E8F5EC", "left to right - correct", ok_steps, ok_ans,
              "no bracket needed, and none was invented"),
             (RED, "#FBECEA", "right one first - wrong", bad_steps, bad_ans,
              "really means " + invented)]):
        ax.add_patch(FancyBboxPatch((x, top - RH + 0.10), BOX_W, RH - 0.20,
                                    boxstyle="round,pad=0.04,rounding_size=0.15",
                                    facecolor=tint, edgecolor=edge, linewidth=1.8))
        ax.text(x + 0.28, top - 0.42, head, ha="left", va="center",
                fontsize=13.5, color=edge, fontweight="bold")
        ax.text(x + 0.28, cy - 0.05, steps[0], ha="left", va="center",
                fontsize=18, color=INK)
        ax.text(x + 1.85, cy - 0.05, steps[1], ha="left", va="center",
                fontsize=18, color=INK)
        ax.text(x + BOX_W - 0.34, cy - 0.05, ans, ha="right", va="center",
                fontsize=27, color=edge, fontweight="bold")
        # the closing line of each box. keep it short - a longer one runs
        # out of the box on the right
        ax.text(x + 0.28, top - RH + 0.46, tag,
                ha="left", va="center", fontsize=13, color=edge)

ax.text(W / 2, H - 0.42, "The acronym is not a queue",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.90,
        "PEMDAS lists six letters, but M and D take turns, and so do A and S",
        ha="center", va="center", fontsize=13.5, color=GREY)
ax.text(W / 2, 0.42,
        "Inside one level there is no ranking. Whichever operation you meet "
        "first as you read left to right is the one you do.",
        ha="center", va="center", fontsize=15, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_left_to_right.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
