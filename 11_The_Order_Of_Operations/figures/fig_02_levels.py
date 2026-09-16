"""Figure 2 - the four levels of priority, top to bottom.

The acronym PEMDAS has six letters, and readers count six levels. There are
four. This figure is the correction: it draws one bar per level, and the
bars for the two shared levels hold two operations side by side inside one
bar, with no divider between them.

The colours run warm at the top and cool at the bottom, so the eye reads
the tower as a fall in priority even before it reads the words.
Run with:  python figures/fig_02_levels.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"          # level 1, grouping
PURPLE = "#8E44AD"          # level 2, exponents (the Chapter 10 colour)
BLUE = "#2E86DE"            # level 3, multiply and divide
SLATE = "#546E7A"           # level 4, add and subtract
GREY = "#78909C"
INK = "#212121"

W, H = 11.8, 8.15
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BAR_X, BAR_W = 2.05, 8.05   # left edge and width of every bar
BAR_H = 1.18                # height of one bar
GAP = 0.30                  # vertical gap between two bars
TOP_Y = H - 1.72            # top edge of the first bar

LEVELS = [
    ("1", ORANGE, "#FBEEE0", "P", "Brackets",
     r"$(\;)\qquad [\;]\qquad \{\;\}$", "innermost pair first"),
    ("2", PURPLE, "#F3EAF8", "E", "Exponents",
     r"$a^{b}$", "left to right"),
    ("3", BLUE, "#EAF2FC", "M  D", "Multiply and divide",
     r"$\times \qquad \div$", "one level, left to right"),
    ("4", SLATE, "#ECEFF1", "A  S", "Add and subtract",
     r"$+ \qquad -$", "one level, left to right"),
]

for i, (num, edge, tint, letters, name, symbols, how) in enumerate(LEVELS):
    y = TOP_Y - i * (BAR_H + GAP)                     # top edge of this bar
    cy = y - BAR_H / 2                                # middle of this bar
    ax.add_patch(FancyBboxPatch((BAR_X, y - BAR_H), BAR_W, BAR_H,
                                boxstyle="round,pad=0.03,rounding_size=0.14",
                                facecolor=tint, edgecolor=edge, linewidth=1.9))
    # the level number, outside the bar on the left
    ax.text(BAR_X - 0.30, cy, f"Level {num}", ha="right", va="center",
            fontsize=14, color=GREY)
    # the PEMDAS letter(s) in a solid tab at the left end of the bar
    ax.add_patch(FancyBboxPatch((BAR_X + 0.16, y - BAR_H + 0.17),
                                1.52, BAR_H - 0.34,
                                boxstyle="round,pad=0.02,rounding_size=0.10",
                                facecolor=edge, edgecolor="none"))
    ax.text(BAR_X + 0.92, cy, letters, ha="center", va="center",
            fontsize=25, color="white", fontweight="bold")
    # the name of the level, and under it how to work inside it
    ax.text(BAR_X + 2.02, cy + 0.23, name, ha="left", va="center",
            fontsize=18, color=INK, fontweight="bold")
    ax.text(BAR_X + 2.02, cy - 0.30, how, ha="left", va="center",
            fontsize=13.5, color=GREY)
    # the symbols that belong to this level, at the right end
    ax.text(BAR_X + BAR_W - 0.42, cy, symbols, ha="right", va="center",
            fontsize=23, color=edge)

# ---- the arrow that says which way priority falls -----------------------
ARROW_X = BAR_X + BAR_W + 0.62
ax.add_patch(FancyArrowPatch((ARROW_X, TOP_Y - 0.12),
                             (ARROW_X, TOP_Y - 3 * (BAR_H + GAP) - BAR_H + 0.12),
                             arrowstyle="-|>", mutation_scale=22,
                             color=GREY, linewidth=2.0))
ax.text(ARROW_X + 0.22, (TOP_Y - 3 * (BAR_H + GAP) - BAR_H / 2), "do these last",
        ha="left", va="center", fontsize=12.5, color=GREY, rotation=90)
ax.text(ARROW_X + 0.22, TOP_Y - BAR_H / 2, "do these first",
        ha="left", va="center", fontsize=12.5, color=GREY, rotation=90)

# ---- title and the sentence the figure exists for -----------------------
ax.text(W / 2, H - 0.45, "Four levels, not six",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.95,
        "Levels 3 and 4 each hold two operations that are worth exactly the same",
        ha="center", va="center", fontsize=14, color=GREY)
ax.text(W / 2, 0.36,
        r"$\times$ does not beat $\div$, and $+$ does not beat $-$."
        "  Inside one level, the left one goes first.",
        ha="center", va="center", fontsize=16, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_levels.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
