"""Figure 2 - the two parts of a power, named.

The reader has never seen a small raised number before, so this figure does
one job only: say which part is the base and which part is the exponent, and
show what the pair of them is short for.

5 is drawn large and 3 small and raised, exactly as they appear in the text,
so the reader can match the picture to the page. The two names sit on
opposite sides at different heights, because a label placed under the base
runs straight into the summary line along the bottom.
Run with:  python figures/fig_02_anatomy.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # the base
PURPLE = "#8E44AD"      # the exponent
GREY = "#78909C"        # quiet labels
INK = "#212121"

W, H = 11.2, 5.55
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch, so every number below is inches
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CX, Y = 5.45, 3.30                          # where the big 5 sits, and its middle height

# the term itself: a large base with a small raised exponent beside it
ax.text(CX, Y, "5", ha="center", va="center", fontsize=86,
        color=BLUE, fontweight="bold")
ax.text(CX + 0.72, Y + 0.60, "3", ha="center", va="center", fontsize=48,
        color=PURPLE, fontweight="bold")

# the base, named on the left
ax.annotate("", xy=(CX - 0.42, Y - 0.30), xytext=(CX - 1.70, Y - 0.72),
            arrowprops=dict(arrowstyle="-|>", color=BLUE, linewidth=2.2,
                            mutation_scale=18))
ax.text(CX - 1.85, Y - 0.72, "base", ha="right", va="center",
        fontsize=21, color=BLUE, fontweight="bold")
ax.text(CX - 1.85, Y - 1.13, "the number that\ngets multiplied",
        ha="right", va="top", fontsize=14.5, color=INK, linespacing=1.45)

# the exponent, named on the right
ax.annotate("", xy=(CX + 0.98, Y + 0.85), xytext=(CX + 2.05, Y + 1.32),
            arrowprops=dict(arrowstyle="-|>", color=PURPLE, linewidth=2.2,
                            mutation_scale=18))
ax.text(CX + 2.20, Y + 1.32, "exponent", ha="left", va="center",
        fontsize=21, color=PURPLE, fontweight="bold")
ax.text(CX + 2.20, Y + 0.91, "how many times\nto multiply it",
        ha="left", va="top", fontsize=14.5, color=INK, linespacing=1.45)

# what the whole thing is short for, along the bottom
ax.plot([0.75, W - 0.75], [1.02] * 2, color=GREY, linewidth=1.2,
        linestyle=(0, (5, 4)))
ax.text(W / 2, 0.55,
        r"$5^{3} \; = \; 5 \times 5 \times 5 \; = \; 125$",
        ha="center", va="center", fontsize=25, color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_anatomy.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
