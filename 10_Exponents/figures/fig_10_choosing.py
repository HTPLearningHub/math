"""Figure 10 - which rule belongs to which shape.

Four cells, one shape each. The reader looks at the expression in front of
them, finds the cell that matches its shape, and reads off what happens to
the exponents.

The fourth cell is the one that matters most. Every other chart of this kind
lists three rules and quietly leaves addition out, which is exactly why a
reader invents a fourth rule for it. Here it has a cell of its own, in red,
and the cell says that the right move is to do nothing.
Run with:  python figures/fig_10_choosing.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"
PURPLE = "#8E44AD"
RED = "#C0392B"
GREY = "#78909C"
INK = "#212121"

W, H = 11.6, 7.05
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CW, CH = 5.10, 2.42                        # the size of one cell
COLS = (3.05, 8.55)                        # the middle of the left and right columns
ROWS = (4.62, 1.92)                        # the middle of the top and bottom rows

CELLS = [
    # centre, tint, edge, the shape, what happens, the result
    ((COLS[0], ROWS[0]), "#EAF2FC", BLUE,
     r"$x^{a} \times x^{b}$", "ADD the exponents", r"$= \; x^{a + b}$"),
    ((COLS[1], ROWS[0]), "#EAF2FC", BLUE,
     r"$\dfrac{x^{a}}{x^{b}}$", "SUBTRACT the exponents", r"$= \; x^{a - b}$"),
    ((COLS[0], ROWS[1]), "#F3EAF8", PURPLE,
     r"$(x^{a})^{b}$", "MULTIPLY the exponents", r"$= \; x^{a \times b}$"),
    ((COLS[1], ROWS[1]), "#FBECEA", RED,
     r"$x^{a} + x^{b}$", "no rule at all", "leave it exactly as it is"),
]

for (cx, cy), tint, edge, shape, action, result in CELLS:
    ax.add_patch(FancyBboxPatch((cx - CW / 2, cy - CH / 2), CW, CH,
                                boxstyle="round,pad=0.05,rounding_size=0.16",
                                facecolor=tint, edgecolor=edge, linewidth=1.8))
    ax.text(cx, cy + 0.74, shape, ha="center", va="center",
            fontsize=27, color=INK)
    ax.text(cx, cy - 0.08, action, ha="center", va="center",
            fontsize=16, color=edge, fontweight="bold")
    # plain words need a smaller size than a formula to look the same weight
    ax.text(cx, cy - 0.82, result, ha="center", va="center",
            fontsize=22 if result.startswith("$") else 17,
            color=edge, fontweight="bold")

ax.text(W / 2, H - 0.32, "Look at the shape first, then pick the rule",
        ha="center", va="center", fontsize=19, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.78,
        r"in every cell $x$ is the base, and it is the same $x$ throughout",
        ha="center", va="center", fontsize=13.5, color=GREY)
ax.text(W / 2, 0.36,
        r"All four cells need the same base. $2^{3} \times 5^{4}$ has no short cut at all.",
        ha="center", va="center", fontsize=15.5, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_10_choosing.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
