"""Figure 4 - the whole method for a higher-degree equation.

Six boxes from top to bottom, joined by arrows, with a red loop from
"remainder not 0" back to "try a candidate", and a dashed blue loop from
"degree still 3 or more" back to the test. Beside each box, the same step
done on the example 2x^3 + 3x^2 - 3x - 2 = 0.

Colours (as Chapters 30 and 31, fig_03): blue for steps new in this chapter,
slate for steps the book already had, green for the final check, red for the
"try again" loop.

Run with:  python figures/fig_04_method_flow.py
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
RED = "#C0392B"

# (text in the box, colour, the example written beside it)
steps = [
    ("1. Standard form, $0$ on the right;\n    write $0$ for missing powers", OLD,
     r"coefficients  $2,\ 3,\ -3,\ -2$"),
    ("2. Rational roots test:\n    list the candidates", NEW,
     r"$\pm 1,\ \pm 2,\ \pm \frac{1}{2}$"),
    ("3. Synthetic division\n    with one candidate", NEW,
     r"try $1$:  bottom row  $2,\ 5,\ 2,\ 0$"),
    ("4. Remainder $0$? Then it is a\n    solution; keep the bottom row", NEW,
     r"$x = 1$;   new polynomial  $2x^{2} + 5x + 2$"),
    ("5. Degree $2$: factor, or\n    complete the square", OLD,
     r"$(2x + 1)(x + 2) = 0$,  so  $x = -\frac{1}{2}$  or  $x = -2$"),
    ("6. Check every answer in the\n    original equation", GREEN,
     r"$1,\ -\frac{1}{2},\ -2$  each give $0$ $\checkmark$"),
]

fig, ax = plt.subplots(figsize=(16, 12.6))
ax.set_xlim(0, 16)
ax.set_ylim(0, 13.4)
ax.axis("off")

ax.text(0.3, 13.0, r"Example:  $2x^{3} + 3x^{2} - 3x - 2 = 0$", fontsize=20,
        color=INK, va="center")

H, W, X0 = 1.45, 6.0, 2.6                          # box height, width, left
ys = []
for i, (txt, col, ex) in enumerate(steps):
    y = 11.2 - i * 2.0                             # bottom edge of this box
    ys.append(y)
    ax.add_patch(FancyBboxPatch((X0, y), W, H,
                                boxstyle="round,pad=0.08",
                                facecolor=col, alpha=0.13,
                                edgecolor=col, lw=2.5))
    ax.text(X0 + 0.25, y + H / 2, txt, ha="left", va="center",
            fontsize=16, color=col, fontweight="bold")
    ax.text(X0 + W + 0.6, y + H / 2, ex, ha="left", va="center",
            fontsize=18, color=INK)                # the example, beside it
    if i < len(steps) - 1:                         # arrow down to next box
        ax.add_patch(FancyArrowPatch((X0 + W / 2, y - 0.04),
                                     (X0 + W / 2, y - 0.5),
                                     arrowstyle="-|>", mutation_scale=22,
                                     color=GREY, lw=2))

# loop on the right, in the gap: remainder not 0 -> back to step 3
y2, y3, y4 = ys[1], ys[2], ys[3]
ax.add_patch(FancyArrowPatch((X0 + W + 0.1, y4 + H - 0.25),
                             (X0 + W + 0.1, y3 + 0.25),
                             connectionstyle="arc3,rad=1.2",
                             arrowstyle="-|>", mutation_scale=18,
                             color=RED, lw=2))
ax.text(X0 + W + 0.75, y3 - 0.27, "not $0$: try the next candidate",
        ha="left", va="center", fontsize=13, color=RED)   # in the gap

# loop on the left: degree still 3 or more -> back to step 2
ax.add_patch(FancyArrowPatch((X0 - 0.1, y4 + H / 2), (X0 - 0.1, y2 + H / 2),
                             connectionstyle="arc3,rad=-0.45",
                             arrowstyle="-|>", mutation_scale=20,
                             color=NEW, lw=2, ls="--"))
ax.text(0.0, y3 + H / 2, "degree still\n$3$ or more:\nrepeat on\nthe bottom\nrow",
        ha="left", va="center", fontsize=12, color=NEW)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_method_flow.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_04_method_flow.png")
