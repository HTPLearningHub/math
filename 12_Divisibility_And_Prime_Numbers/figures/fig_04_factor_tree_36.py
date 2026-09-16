"""Figure 4 - the factor tree for 36.

A factor tree is a layout, not an idea, so the picture has to show the
layout exactly as the reader should write it: the number on top, two
branches under it, and a branch that stops as soon as its number is prime.

Colour carries the rule. Blue means composite - this one still has to be
split. Green means prime - this one is finished and stays where it is. The
reader's job is therefore very simple to state: keep going until no blue
circle is left.

The tree is pushed to the right of the canvas, not centred, because the
three level labels live down the left-hand side and the first version had
them sitting on top of the leftmost circle.
Run with:  python figures/fig_04_factor_tree_36.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from pathlib import Path

GREEN = "#1E8449"            # prime - this branch stops here
BLUE = "#2E86DE"             # composite - this one splits again
GREY = "#78909C"
PURPLE = "#8E44AD"           # the exponent form, as in Chapter 10
INK = "#212121"

R = 0.42                                   # radius of a node
W, H = 10.60, 6.60
CX = 6.15                                  # centre line of the tree
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")                     # circles must stay circles

# node: (x, y, value, is_prime)
NODES = {
    "top":  (CX, 5.20, 36, False),
    "l":    (CX - 1.75, 3.90, 4, False),
    "r":    (CX + 1.75, 3.90, 9, False),
    "ll":   (CX - 2.70, 2.60, 2, True),
    "lr":   (CX - 0.80, 2.60, 2, True),
    "rl":   (CX + 0.80, 2.60, 3, True),
    "rr":   (CX + 2.70, 2.60, 3, True),
}
EDGES = [("top", "l"), ("top", "r"),
         ("l", "ll"), ("l", "lr"), ("r", "rl"), ("r", "rr")]

# the branches are drawn first, so the circles cover their ends
for a, b in EDGES:
    xa, ya, _, _ = NODES[a]
    xb, yb, _, _ = NODES[b]
    ax.plot([xa, xb], [ya, yb], linewidth=1.8, color=GREY, zorder=1)

for x, y, value, is_prime in NODES.values():
    colour = GREEN if is_prime else BLUE
    ax.add_patch(Circle((x, y), R, facecolor="#E8F5EC" if is_prime else "#E9F2FC",
                        edgecolor=colour, linewidth=2.1, zorder=2))
    ax.text(x, y, str(value), ha="center", va="center", zorder=3,
            fontsize=21, color=colour, fontweight="bold")
    if is_prime:
        # a prime node is finished, and the picture says so under it
        ax.text(x, y - R - 0.28, "prime", ha="center", va="center",
                fontsize=11.5, color=GREEN)

# ----------------------------------------------------- what each level means
ax.text(0.25, 5.20, "start with the number", ha="left", va="center",
        fontsize=12.5, color=GREY)
ax.text(0.25, 3.90, "split it into any\nfactor pair you like",
        ha="left", va="center", fontsize=12.5, color=GREY)
ax.text(0.25, 2.60, "keep splitting until\nno blue circle is left",
        ha="left", va="center", fontsize=12.5, color=GREY)

# ------------------------------------------ the answer, read off the bottom row
ax.plot([1.20, W - 1.20], [1.70, 1.70], linewidth=1.3, color="#D8DEE1")
ax.text(W / 2, 1.28, r"$36 = 2 \times 2 \times 3 \times 3$",
        ha="center", va="center", fontsize=22, color=INK)
ax.text(W / 2, 0.66, r"$36 = 2^{2} \times 3^{2}$",
        ha="center", va="center", fontsize=25, color=PURPLE)

ax.text(W / 2, H - 0.36, "A factor tree for 36",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_factor_tree_36.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
