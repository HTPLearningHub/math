"""Figure 3 - why the two pairs share a level.

The source states that M and D are equal, and that A and S are equal, but
it never says why. The reason is that each pair is one operation wearing
two coats: a subtraction is an addition of the opposite (Chapter 9), and a
division is a multiplication by the reciprocal (Chapter 10).

Two panels, one per pair. The left half of each panel is the way the sum is
written; the right half is the same sum with the disguise removed.
Run with:  python figures/fig_03_one_operation.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"            # level 3
SLATE = "#546E7A"           # level 4
GREY = "#78909C"
INK = "#212121"

W, H = 11.6, 7.55
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

PANEL_X, PANEL_W, PANEL_H = 0.95, 9.70, 1.92
ROWS = (H - 1.18, H - 3.45)          # top edge of the upper / lower panel

PANELS = [
    (SLATE, "#ECEFF1", "Level 4",
     r"$10 - 4$", r"$10 + (-4)$",
     "a subtraction is an addition of the opposite",
     "so + and - are the same operation"),
    (BLUE, "#EAF2FC", "Level 3",
     r"$12 \div 3$", r"$12 \times \frac{1}{3}$",
     "a division is a multiplication by the reciprocal",
     r"so $\times$ and $\div$ are the same operation"),
]

for top, (edge, tint, level, written, undisguised, why, closing) in zip(ROWS, PANELS):
    cy = top - PANEL_H / 2
    ax.add_patch(FancyBboxPatch((PANEL_X, top - PANEL_H), PANEL_W, PANEL_H,
                                boxstyle="round,pad=0.04,rounding_size=0.15",
                                facecolor=tint, edgecolor=edge, linewidth=1.8))
    # the level tag, small, in the top-left corner of the panel
    ax.text(PANEL_X + 0.30, top - 0.32, level, ha="left", va="center",
            fontsize=13, color=edge, fontweight="bold")
    # the sum as it is normally written
    ax.text(PANEL_X + 2.05, cy - 0.16, written, ha="center", va="center",
            fontsize=30, color=INK)
    ax.text(PANEL_X + 2.05, cy + 0.66, "how it is written",
            ha="center", va="center", fontsize=12.5, color=GREY)
    # the arrow between the two halves, with the reason written above it
    ax.add_patch(FancyArrowPatch((PANEL_X + 3.35, cy - 0.16),
                                 (PANEL_X + 5.55, cy - 0.16),
                                 arrowstyle="-|>", mutation_scale=20,
                                 color=edge, linewidth=2.0))
    ax.text(PANEL_X + 4.45, cy + 0.42, "means the same as",
            ha="center", va="center", fontsize=13, color=edge)
    # the same sum with the disguise removed
    ax.text(PANEL_X + 6.95, cy - 0.16, undisguised, ha="center", va="center",
            fontsize=30, color=edge)
    ax.text(PANEL_X + 6.95, cy + 0.66, "what it really is",
            ha="center", va="center", fontsize=12.5, color=GREY)
    # the sentence this panel proves, along the bottom of the panel
    ax.text(PANEL_X + PANEL_W / 2, top - PANEL_H + 0.30, why,
            ha="center", va="center", fontsize=14.5, color=INK)

ax.text(W / 2, H - 0.45, "Each pair is one operation wearing two coats",
        ha="center", va="center", fontsize=19.5, color=INK, fontweight="bold")
ax.text(W / 2, 1.42,
        "Two operations that are really one operation cannot take turns.",
        ha="center", va="center", fontsize=15, color=INK)
ax.text(W / 2, 0.92,
        "They sit on the same level, and the left one goes first.",
        ha="center", va="center", fontsize=16.5, color=INK, fontweight="bold")
ax.text(W / 2, 0.40,
        r"$10 - 4 + 2 = 8$          $12 \div 3 \times 2 = 8$",
        ha="center", va="center", fontsize=17, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_one_operation.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
