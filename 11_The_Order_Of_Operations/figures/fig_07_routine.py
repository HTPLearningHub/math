"""Figure 7 - the routine, drawn as a loop rather than a list.

A plain list of four levels lets the reader believe that each level is
visited once. It is not. After any single operation the expression has
changed, so the search starts again at the top - which is what makes a
bracket inside a bracket work without a separate rule.

The four level boxes run down the left. "No" carries on down. "Yes" leaves
to the right, does one operation, and the long arrow on the right carries
the reader back to the top box.
Run with:  python figures/fig_07_routine.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"
PURPLE = "#8E44AD"
BLUE = "#2E86DE"
SLATE = "#546E7A"
GREEN = "#1E8449"
GREY = "#78909C"
INK = "#212121"

W, H = 12.2, 8.25
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BX, BW, BH = 0.85, 4.35, 1.00        # left edge, width and height of a question box
TOP = H - 1.42                       # top edge of the first question box
GAP = 0.44                           # vertical gap between two question boxes
ACT_X, ACT_W = 6.30, 4.05            # left edge and width of an action box
LOOP_X = W - 0.52                    # the x of the long return arrow

STEPS = [
    (ORANGE, "#FBEEE0", "Any brackets left?",
     "Work inside the innermost pair"),
    (PURPLE, "#F3EAF8", "Any exponents left?",
     "Work out the leftmost power"),
    (BLUE, "#EAF2FC", r"Any $\times$ or $\div$ left?",
     "Do the leftmost of the two"),
    (SLATE, "#ECEFF1", r"Any $+$ or $-$ left?",
     "Do the leftmost of the two"),
]

centres = []
for i, (edge, tint, question, action) in enumerate(STEPS):
    y = TOP - i * (BH + GAP)
    cy = y - BH / 2
    centres.append(cy)
    # the question
    ax.add_patch(FancyBboxPatch((BX, y - BH), BW, BH,
                                boxstyle="round,pad=0.04,rounding_size=0.15",
                                facecolor=tint, edgecolor=edge, linewidth=1.9))
    ax.text(BX + BW / 2, cy, question, ha="center", va="center",
            fontsize=17, color=INK, fontweight="bold")
    # the "yes" arrow leaving to the right, and what it leads to
    ax.add_patch(FancyArrowPatch((BX + BW + 0.06, cy), (ACT_X - 0.10, cy),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=edge, linewidth=1.8))
    ax.text((BX + BW + ACT_X) / 2, cy + 0.20, "yes", ha="center", va="bottom",
            fontsize=12.5, color=edge, fontweight="bold")
    ax.add_patch(FancyBboxPatch((ACT_X, cy - BH / 2 + 0.06), ACT_W, BH - 0.12,
                                boxstyle="round,pad=0.03,rounding_size=0.13",
                                facecolor="white", edgecolor=edge,
                                linewidth=1.5, linestyle="--"))
    ax.text(ACT_X + ACT_W / 2, cy, action, ha="center", va="center",
            fontsize=14.5, color=edge)
    # the "no" arrow carrying on down to the next question
    if i < len(STEPS) - 1:
        ax.add_patch(FancyArrowPatch((BX + BW / 2, y - BH - 0.04),
                                     (BX + BW / 2, y - BH - GAP + 0.04),
                                     arrowstyle="-|>", mutation_scale=16,
                                     color=GREY, linewidth=1.6))
        ax.text(BX + BW / 2 + 0.16, y - BH - GAP / 2, "no", ha="left",
                va="center", fontsize=12, color=GREY)

# ---- the return arrow: one operation done, start again at the top -------
ax.add_patch(FancyArrowPatch((ACT_X + ACT_W + 0.10, centres[-1]),
                             (LOOP_X, centres[-1]),
                             arrowstyle="-", color=GREY, linewidth=1.7))
ax.add_patch(FancyArrowPatch((LOOP_X, centres[-1]), (LOOP_X, centres[0]),
                             arrowstyle="-", color=GREY, linewidth=1.7))
ax.add_patch(FancyArrowPatch((LOOP_X, centres[0]), (ACT_X + ACT_W + 0.10, centres[0]),
                             arrowstyle="-", color=GREY, linewidth=1.7))
ax.add_patch(FancyArrowPatch((BX + BW / 2, TOP + 0.62), (BX + BW / 2, TOP + 0.06),
                             arrowstyle="-|>", mutation_scale=18,
                             color=GREY, linewidth=1.7))
ax.add_patch(FancyArrowPatch((LOOP_X, centres[0]), (LOOP_X, TOP + 0.62),
                             arrowstyle="-", color=GREY, linewidth=1.7))
ax.add_patch(FancyArrowPatch((LOOP_X, TOP + 0.62), (BX + BW / 2 + 0.02, TOP + 0.62),
                             arrowstyle="-", color=GREY, linewidth=1.7))
ax.text(LOOP_X - 0.30, (centres[0] + centres[-1]) / 2,
        "rewrite the whole line, then start again at the top",
        ha="center", va="center", fontsize=13, color=GREY, rotation=90)

# ---- the end of the routine --------------------------------------------
END_Y = centres[-1] - BH / 2 - 1.05
ax.add_patch(FancyArrowPatch((BX + BW / 2, centres[-1] - BH / 2 - 0.04),
                             (BX + BW / 2, END_Y + 0.28),
                             arrowstyle="-|>", mutation_scale=16,
                             color=GREY, linewidth=1.6))
ax.text(BX + BW / 2 + 0.16, centres[-1] - BH / 2 - 0.45, "no", ha="left",
        va="center", fontsize=12, color=GREY)
ax.add_patch(FancyBboxPatch((BX, END_Y - 0.38), BW, 0.76,
                            boxstyle="round,pad=0.04,rounding_size=0.14",
                            facecolor="#E8F5EC", edgecolor=GREEN, linewidth=1.9))
ax.text(BX + BW / 2, END_Y, "one number left - that is the answer",
        ha="center", va="center", fontsize=14.5, color=GREEN, fontweight="bold")

ax.text(W / 2, H - 0.42, "One operation at a time, then look again from the top",
        ha="center", va="center", fontsize=19, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_07_routine.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
