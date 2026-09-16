"""Figure 6 - two different trees for 90, and one set of primes.

This is the picture for the Fundamental Theorem of Arithmetic. The reader
has to see that the two trees really are different - different first split,
different shape, different depth - and that the green circles at the ends
of the branches are nevertheless the same four numbers.

So the two panels are deliberately not symmetrical. Path A splits into a
pair of composites and finishes in two levels. Path B peels one prime off
at a time and needs three. The collected primes are printed *below* each
panel rather than inside it: Path B's deepest branch reaches the floor of
its panel, and the first version of this script put the summary line on top
of a circle.
Run with:  python figures/fig_06_two_trees_90.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
from pathlib import Path

GREEN = "#1E8449"            # prime
BLUE = "#2E86DE"             # composite
GREY = "#78909C"
PURPLE = "#8E44AD"           # the exponent form, as in Chapter 10
INK = "#212121"

R = 0.34                                   # radius of a node
W, H = 12.40, 8.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")                     # circles must stay circles

PW, PH = 5.80, 5.15                        # panel width and height
PBOT = 2.80                                # bottom edge of both panels
PTOP = PBOT + PH
ROW = {1: 6.55, 2: 5.40, 3: 4.25, 4: 3.30}  # y of each level of a tree

# Each tree is a dict of node key -> (level, x offset from the panel centre,
# value, is it prime), plus the branches that join them.
TREES = [
    (3.15, "Path A", r"start by splitting $90$ into $9 \times 10$",
     {"t": (1, 0.00, 90, False),
      "a": (2, -1.30, 9, False), "b": (2, 1.30, 10, False),
      "c": (3, -2.00, 3, True), "d": (3, -0.60, 3, True),
      "e": (3, 0.60, 2, True), "f": (3, 2.00, 5, True)},
     [("t", "a"), ("t", "b"), ("a", "c"), ("a", "d"), ("b", "e"), ("b", "f")]),
    (9.25, "Path B", r"start by splitting $90$ into $30 \times 3$",
     {"t": (1, 0.00, 90, False),
      "a": (2, -1.10, 30, False), "b": (2, 1.30, 3, True),
      "c": (3, -1.90, 10, False), "d": (3, -0.30, 3, True),
      "e": (4, -2.50, 5, True), "f": (4, -1.20, 2, True)},
     [("t", "a"), ("t", "b"), ("a", "c"), ("a", "d"), ("c", "e"), ("c", "f")]),
]

for cx, name, subtitle, nodes, edges in TREES:
    ax.add_patch(FancyBboxPatch((cx - PW / 2, PBOT), PW, PH,
                                boxstyle="round,pad=0.04,rounding_size=0.16",
                                facecolor="#FFFFFF", edgecolor=GREY, linewidth=1.5))
    ax.text(cx, PTOP - 0.34, name, ha="center", va="center",
            fontsize=16, color=INK, fontweight="bold")
    ax.text(cx, PTOP - 0.71, subtitle, ha="center", va="center",
            fontsize=13, color=GREY)

    # branches first, so the circles sit on top of their ends
    for a, b in edges:
        la, xa, _, _ = nodes[a]
        lb, xb, _, _ = nodes[b]
        ax.plot([cx + xa, cx + xb], [ROW[la], ROW[lb]],
                linewidth=1.7, color=GREY, zorder=1)

    for level, dx, value, is_prime in nodes.values():
        colour = GREEN if is_prime else BLUE
        ax.add_patch(Circle((cx + dx, ROW[level]), R, zorder=2,
                            facecolor="#E8F5EC" if is_prime else "#E9F2FC",
                            edgecolor=colour, linewidth=2.0))
        ax.text(cx + dx, ROW[level], str(value), ha="center", va="center",
                fontsize=17, color=colour, fontweight="bold", zorder=3)

    # collect the green circles of this tree, smallest first, under the panel
    primes = sorted(v for _, _, v, p in nodes.values() if p)
    ax.text(cx, PBOT - 0.36, "the green circles, sorted", ha="center", va="center",
            fontsize=12.5, color=GREY)
    ax.text(cx, PBOT - 0.86, r"$" + r" \times ".join(str(v) for v in primes) + r"$",
            ha="center", va="center", fontsize=21, color=GREEN)

# ------------------------------------------------ the answer both paths give
ax.add_patch(FancyBboxPatch((W / 2 - 3.90, 0.30), 7.80, 1.30,
                            boxstyle="round,pad=0.04,rounding_size=0.16",
                            facecolor="#E8F5EC", edgecolor=GREEN, linewidth=2.0))
ax.text(W / 2, 1.24, "Different trees. The same four primes.",
        ha="center", va="center", fontsize=15, color=GREEN, fontweight="bold")
ax.text(W / 2, 0.66, r"$90 = 2 \times 3 \times 3 \times 5 = 2 \times 3^{2} \times 5$",
        ha="center", va="center", fontsize=22, color=PURPLE)

ax.text(W / 2, H - 0.34, "One number, one set of building blocks",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_two_trees_90.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
