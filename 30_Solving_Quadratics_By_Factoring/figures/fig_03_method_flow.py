"""Figure 3 - the method for solving a quadratic equation by factoring.

Five boxes from top to bottom, joined by arrows. Next to each box, the same
step done on the running example x^2 + 7x = -10.

Colours: blue for the two steps that are new in this chapter (factor, split
with the zero product property), slate for steps the book already had,
green for the final check.

Run with:  python figures/fig_03_method_flow.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
OLD = "#5D6D7E"                                    # steps from earlier chapters
NEW = "#2E86DE"                                    # steps new in this chapter
GREEN = "#1E8449"

# (text in the box, colour, the example written beside it)
steps = [
    ("1. Move everything to one side,\n    so the right side is $0$", OLD,
     r"$x^{2} + 7x + 10 = 0$"),
    ("2. Factor the left side\n    into two brackets", NEW,
     r"$(x + 5)(x + 2) = 0$"),
    ("3. Set each bracket equal to $0$\n    (zero product property)", NEW,
     r"$x + 5 = 0$   or   $x + 2 = 0$"),
    ("4. Solve each small equation", OLD,
     r"$x = -5$   or   $x = -2$"),
    ("5. Check each answer in the\n    original equation", GREEN,
     r"$25 - 35 = -10$ $\checkmark$     $4 - 14 = -10$ $\checkmark$"),
]

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10.6)
ax.axis("off")

ax.text(0.3, 10.2, r"Example:  $x^{2} + 7x = -10$", fontsize=20, color=INK,
        va="center")

H, W, X0 = 1.45, 5.6, 0.3                          # box height, width, left
for i, (txt, col, ex) in enumerate(steps):
    y = 8.4 - i * 2.0                              # bottom edge of this box
    ax.add_patch(FancyBboxPatch((X0, y), W, H,
                                boxstyle="round,pad=0.08",
                                facecolor=col, alpha=0.13,
                                edgecolor=col, lw=2.5))
    ax.text(X0 + 0.25, y + H / 2, txt, ha="left", va="center",
            fontsize=16, color=col, fontweight="bold")
    ax.text(X0 + W + 0.6, y + H / 2, ex, ha="left", va="center",
            fontsize=19, color=INK)                # the example, beside it
    if i < len(steps) - 1:                         # arrow down to next box
        ax.add_patch(FancyArrowPatch((X0 + W / 2, y - 0.04),
                                     (X0 + W / 2, y - 0.5),
                                     arrowstyle="-|>", mutation_scale=22,
                                     color=GREY, lw=2))

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_method_flow.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_03_method_flow.png")
