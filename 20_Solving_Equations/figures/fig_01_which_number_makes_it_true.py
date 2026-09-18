"""Figure 1 - an equation is a question, and only one number answers it.

Four candidate numbers are dropped into x + 2 = 5 one at a time. Three of
them make the left side something other than 5; one of them makes it 5.
That one number is the solution.

Drawn as four identical rows so that the only thing that changes down the
figure is the number in the blue card. The reader's eye compares rows.

Vertical plan (y, top to bottom):
    6.35  heading
    5.20  row 1   x = 1
    4.10  row 2   x = 2
    3.00  row 3   x = 3      <- the solution, green
    1.90  row 4   x = 4
    0.70  closing note

Run with:  python figures/fig_01_which_number_makes_it_true.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # the number being tried
GREEN = "#1E8449"         # the number that works
RED = "#C0392B"           # a number that does not work
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_GREEN = "#E8F5EC"
TINT_GREY = "#ECEFF1"

W, H = 9.20, 6.80
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.50, 6.35, r"which number makes  $x + 2 = 5$  true?",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

CARD_H = 0.80
XC_X0, XC_W = 0.50, 1.90        # the blue "x = n" card
WORK_X0, WORK_W = 3.30, 2.90    # the grey/green working card
VERDICT_X = 6.55                # left edge of the verdict text

# (value, y, the arithmetic line, the verdict, does it work)
ROWS = [
    (1, 5.20, r"$1 + 2 = 3$", r"not $5$", False),
    (2, 4.10, r"$2 + 2 = 4$", r"not $5$", False),
    (3, 3.00, r"$3 + 2 = 5$", r"this is $5$", True),
    (4, 1.90, r"$4 + 2 = 6$", r"not $5$", False),
]

for value, y, work, verdict, ok in ROWS:
    # the candidate value, always drawn in blue: this is the number going in
    ax.add_patch(FancyBboxPatch((XC_X0, y - CARD_H / 2), XC_W, CARD_H,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=TINT_BLUE, edgecolor=BLUE,
                                linewidth=2.0, zorder=3))
    ax.text(XC_X0 + XC_W / 2, y, rf"$x = {value}$", ha="center", va="center",
            fontsize=22, color=INK, zorder=4)

    # the short arrow into the working card
    ax.add_patch(FancyArrowPatch((XC_X0 + XC_W + 0.14, y),
                                 (WORK_X0 - 0.14, y),
                                 arrowstyle="-|>", mutation_scale=16,
                                 linewidth=2.0, color=GREY, zorder=5))

    # the working card, green only on the row that succeeds
    ax.add_patch(FancyBboxPatch((WORK_X0, y - CARD_H / 2), WORK_W, CARD_H,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=TINT_GREEN if ok else TINT_GREY,
                                edgecolor=GREEN if ok else GREY,
                                linewidth=2.4 if ok else 2.0, zorder=3))
    ax.text(WORK_X0 + WORK_W / 2, y, work, ha="center", va="center",
            fontsize=22, color=INK, zorder=4)

    ax.text(VERDICT_X, y, verdict, ha="left", va="center", fontsize=18,
            color=GREEN if ok else RED,
            fontweight="bold" if ok else "normal", zorder=4)

ax.text(0.50, 0.70, "only one number answers the question - that number is "
        "called the solution", ha="left", va="center", fontsize=15,
        color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_which_number_makes_it_true.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_01_which_number_makes_it_true.png")
