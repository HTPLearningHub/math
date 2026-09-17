"""Figure 6 - taking the greatest common factor outside a bracket.

The source lists "factoring expressions" as a use of the GCF and gives one
line: 12x + 18 = 6(2x + 3). It gives no reason, and a reader who has only
ever multiplied a bracket out will read it as a trick.

It is not a trick. It is the rectangle from Chapter 6, section 3, read from
right to left. One rectangle of height 6 is cut into two pieces; counting
the two pieces gives 12x + 18, and measuring the whole thing gives
6 x (2x + 3). Nothing was added or removed by the cut, so the two readings
must agree.

The height of the rectangle is the greatest common factor, and that is the
whole reason the GCF is the number you take outside: it is the tallest
rectangle both areas will sit on.

Run with:  python figures/fig_06_common_factor_outside.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrow
from pathlib import Path

BLUE = "#2E86DE"             # the 12x piece
ORANGE = "#E67E22"           # the 18 piece
GREEN = "#1E8449"            # the common factor, the height of the rectangle
PURPLE = "#8E44AD"           # the finished answer
GREY = "#78909C"
INK = "#212121"

W, H = 10.20, 5.85
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

WA, WB = 3.90, 1.95          # the two widths: 2x on the left, 3 on the right
RH = 1.60                    # the height of the rectangle - it stands for 6
RY = 2.30                    # the floor of the rectangle
LEFT = (W - WA - WB) / 2

# ---------------------------------------------------------------- the two pieces
ax.add_patch(Rectangle((LEFT, RY), WA, RH, facecolor="#E9F2FC",
                       edgecolor=BLUE, linewidth=2.0))
ax.text(LEFT + WA / 2, RY + RH / 2, r"$12x$", ha="center", va="center",
        fontsize=26, color=BLUE, fontweight="bold")

ax.add_patch(Rectangle((LEFT + WA, RY), WB, RH, facecolor="#FDF0E3",
                       edgecolor=ORANGE, linewidth=2.0))
ax.text(LEFT + WA + WB / 2, RY + RH / 2, r"$18$", ha="center", va="center",
        fontsize=26, color=ORANGE, fontweight="bold")

# --------------------------------------------- the height, which is the GCF of 12 and 18
ax.add_patch(FancyBboxPatch((LEFT - 0.78, RY), 0.52, RH,
                            boxstyle="round,pad=0.01,rounding_size=0.08",
                            facecolor="#E8F5EC", edgecolor=GREEN, linewidth=2.0))
ax.text(LEFT - 0.52, RY + RH / 2, "6", ha="center", va="center",
        fontsize=24, color=GREEN, fontweight="bold")
ax.text(LEFT - 0.92, RY + RH / 2, "height", ha="right", va="center",
        fontsize=13, color=GREEN, fontweight="bold")
ax.text(LEFT - 0.92, RY + RH / 2 - 0.34, r"$= \mathrm{GCF}(12,\, 18)$",
        ha="right", va="center", fontsize=13, color=GREEN)

# ------------------------------------------------------- the two widths, underneath
for x0, wid, label, colour in ((LEFT, WA, r"$2x$", BLUE),
                               (LEFT + WA, WB, r"$3$", ORANGE)):
    ax.plot([x0 + 0.06, x0 + wid - 0.06], [RY - 0.22, RY - 0.22],
            color=colour, linewidth=1.6)
    ax.plot([x0 + 0.06, x0 + 0.06], [RY - 0.30, RY - 0.14], color=colour,
            linewidth=1.6)
    ax.plot([x0 + wid - 0.06, x0 + wid - 0.06], [RY - 0.30, RY - 0.14],
            color=colour, linewidth=1.6)
    ax.text(x0 + wid / 2, RY - 0.52, label, ha="center", va="center",
            fontsize=20, color=colour)

# -------------------------------------------------- the whole width, further down
ax.plot([LEFT, LEFT + WA + WB], [RY - 0.94, RY - 0.94], color=INK, linewidth=1.6)
ax.plot([LEFT, LEFT], [RY - 1.02, RY - 0.86], color=INK, linewidth=1.6)
ax.plot([LEFT + WA + WB, LEFT + WA + WB], [RY - 1.02, RY - 0.86],
        color=INK, linewidth=1.6)
ax.text(LEFT + (WA + WB) / 2, RY - 1.24, r"$2x + 3$", ha="center", va="center",
        fontsize=20, color=INK)

# ---------------------------------------- the two ways of reading the same picture
ax.text(LEFT + (WA + WB) / 2, RY + RH + 0.46,
        r"count the two pieces:   $12x + 18$",
        ha="center", va="center", fontsize=20, color=INK)

ax.add_patch(FancyArrow(W / 2, 0.96, 0, -0.26, width=0.04, head_width=0.20,
                        head_length=0.14, length_includes_head=True, color=GREY))
ax.text(W / 2, 0.42, r"measure the whole:   $6 \times (2x + 3) = 6(2x + 3)$",
        ha="center", va="center", fontsize=21, color=PURPLE)

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.38, "Taking the common factor outside the bracket",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.78,
        "one rectangle, two readings - the cut cannot change how much is there",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_common_factor_outside.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
