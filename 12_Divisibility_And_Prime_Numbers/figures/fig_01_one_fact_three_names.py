"""Figure 1 - one multiplication, three sentences.

The reader already knows the word *factor* from Chapter 6. What is new in
Chapter 12 is that *factor*, *divisible* and *multiple* are three ways of
saying the same single fact. If the reader does not see that, the rest of
the chapter reads as three separate topics instead of one.

Layout: the multiplication 2 x 5 = 10 sits in a box at the top. Three
arrows drop from it into three panels. Each panel prints the sentence in
green, the reason in grey, then the arithmetic that proves it in black.
Run with:  python figures/fig_01_one_fact_three_names.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

GREEN = "#1E8449"            # the chapter colour for "this divides exactly"
GREY = "#78909C"             # quiet labels and arrows
INK = "#212121"

W, H = 12.4, 5.90
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# ---------------------------------------------------------------- the title
ax.text(W / 2, H - 0.42, "One fact, said in three ways",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")

# --------------------------------------------------- the multiplication box
BW, BH = 4.30, 1.02                        # width and height of the top box
BX, BY = W / 2 - BW / 2, H - 2.10          # its bottom-left corner
ax.add_patch(FancyBboxPatch((BX, BY), BW, BH,
                            boxstyle="round,pad=0.05,rounding_size=0.16",
                            facecolor="#E8F5EC", edgecolor=GREEN, linewidth=2.1))
ax.text(W / 2, BY + BH / 2, r"$2 \times 5 = 10$", ha="center", va="center",
        fontsize=32, color=INK)

# ------------------------------------------------------------- three panels
PW, PH = 3.62, 1.98                        # width and height of one panel
COLS = (2.30, W / 2, W - 2.30)             # centre of each panel
TOP = BY - 0.72                            # top edge of all three panels

PANELS = [
    (r"$2$ is a $\bf{factor}$ of $10$",
     "because it multiplies up to it",
     r"$2 \times 5 = 10$"),
    (r"$10$ is $\bf{divisible}$ by $2$",
     "because the division is exact",
     r"$10 \div 2 = 5$, remainder $0$"),
    (r"$10$ is a $\bf{multiple}$ of $2$",
     "because it is in the counting list",
     r"$2, 4, 6, 8, \mathbf{10}, 12, \dots$"),
]

for cx, (headline, why, proof) in zip(COLS, PANELS):
    ax.add_patch(FancyBboxPatch((cx - PW / 2, TOP - PH), PW, PH,
                                boxstyle="round,pad=0.05,rounding_size=0.16",
                                facecolor="#FFFFFF", edgecolor=GREY, linewidth=1.6))
    ax.text(cx, TOP - 0.56, headline, ha="center", va="center",
            fontsize=16, color=GREEN)
    ax.text(cx, TOP - 1.10, why, ha="center", va="center",
            fontsize=13, color=GREY)
    ax.text(cx, TOP - 1.58, proof, ha="center", va="center",
            fontsize=16, color=INK)
    # an arrow from the bottom edge of the multiplication box into this panel
    ax.add_patch(FancyArrowPatch((W / 2, BY - 0.04), (cx, TOP + 0.02),
                                 connectionstyle="arc3,rad=0.0",
                                 arrowstyle="-|>", mutation_scale=17,
                                 linewidth=1.5, color=GREY))

# --------------------------------------------------------- the closing line
ax.text(W / 2, 0.42,
        "The three boxes do not claim three different things. "
        "They are one fact wearing three names.",
        ha="center", va="center", fontsize=14.5, color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_one_fact_three_names.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
