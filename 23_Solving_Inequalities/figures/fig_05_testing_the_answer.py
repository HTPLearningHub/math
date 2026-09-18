"""Figure 5 - checking an inequality needs two numbers, not one.

An equation is checked by putting the one solution back in. An inequality
has no single solution to put back, so the check is a different act: pick
a number from inside the answer and a number from outside it, and show
that the first makes the original inequality true and the second makes it
false. Two tests, because one test can only ever half-succeed.

The example is the chapter's hardest one, -x > 6, whose answer is x < -6.
The number from outside is 0, and 0 is exactly the number that catches the
commonest mistake: if the symbol had not been turned round the answer
would have been x > -6, which contains 0.

Horizontal plan (x): the axis runs -12 to 2 across 1.60 to 11.05, so one
unit is 0.675 of an inch. The axis overhangs its last tick by 0.78 and
the green ray stops 0.42 past it, leaving the green arrowhead clear of
the black one.

Vertical plan (y, top to bottom):
    5.32  heading
    4.70  the inequality and the answer
    4.00  the tick and the cross, above the line
    3.42  the number line
    3.08  the numbers under it
    2.50  the two test cards
    1.12  bottom of the cards
    0.36  closing note

Run with:  python figures/fig_05_testing_the_answer.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"
GREEN = "#1E8449"         # inside the answer, and the answer itself
RED = "#C0392B"           # outside the answer
GREY = "#78909C"
INK = "#212121"
BLUE_T = "#E9F2FC"
GREEN_T = "#E8F5EC"
RED_T = "#FCEAE8"

W, H = 12.60, 5.55
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

X0, X1 = 1.60, 11.05
V0, V1 = -12.0, 2.0
Y_LINE = 3.42
OVERHANG = 0.78           # how far the axis runs past its last tick
RAY_END = 0.42            # how far the green ray runs past its last tick


def px(value):
    """Turn a number on the line into a position on the page."""
    return X0 + (X1 - X0) * (value - V0) / (V1 - V0)


def cross(cx, cy, size, colour):
    """A cross built from two strokes, not from a font glyph."""
    ax.plot([cx - size, cx + size], [cy - size, cy + size],
            linewidth=4.0, color=colour, solid_capstyle="round", zorder=7)
    ax.plot([cx - size, cx + size], [cy + size, cy - size],
            linewidth=4.0, color=colour, solid_capstyle="round", zorder=7)


def tick(cx, cy, size, colour):
    """A tick built from two strokes, for the same reason."""
    ax.plot([cx - size, cx - size * 0.15], [cy + size * 0.05, cy - size],
            linewidth=4.0, color=colour, solid_capstyle="round", zorder=7)
    ax.plot([cx - size * 0.15, cx + size * 1.05],
            [cy - size, cy + size * 0.95],
            linewidth=4.0, color=colour, solid_capstyle="round", zorder=7)


ax.text(0.45, 5.32, "one number from inside, one from outside",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# what we solved, and what we got
ax.text(2.55, 4.70, r"$-x > 6$", ha="center", va="center", fontsize=20,
        color=INK, zorder=3,
        bbox=dict(boxstyle="round,pad=0.34", facecolor=BLUE_T,
                  edgecolor=BLUE, linewidth=1.7))
ax.annotate("", xy=(4.35, 4.70), xytext=(3.55, 4.70),
            arrowprops=dict(arrowstyle="-|>", linewidth=2.0, color=INK))
ax.text(5.55, 4.70, r"answer:  $x < -6$", ha="center", va="center",
        fontsize=20, color=INK, zorder=3,
        bbox=dict(boxstyle="round,pad=0.34", facecolor=GREEN_T,
                  edgecolor=GREEN, linewidth=1.7))

# ------------------------------------------------------------- the line
ax.annotate("", xy=(X1 + OVERHANG, Y_LINE), xytext=(X0 - OVERHANG, Y_LINE),
            arrowprops=dict(arrowstyle="<|-|>", linewidth=1.7, color=INK))
for value in range(int(V0), int(V1) + 1):
    ax.plot([px(value), px(value)], [Y_LINE - 0.10, Y_LINE + 0.10],
            linewidth=1.4, color=INK)
    ax.text(px(value), Y_LINE - 0.34, str(value), ha="center", va="center",
            fontsize=10.5, color=GREY)

# the solution set, running off the left-hand end
# the ray stops short of the black arrowhead, so that its own arrowhead
# stays visible - that arrowhead is what says the answer never ends
ax.annotate("", xy=(X0 - RAY_END, Y_LINE), xytext=(px(-6), Y_LINE),
            arrowprops=dict(arrowstyle="-|>", linewidth=5.0, color=GREEN,
                            mutation_scale=17), zorder=4)
ax.plot([px(-6)], [Y_LINE], marker="o", markersize=14,
        markerfacecolor="white", markeredgecolor=GREEN,
        markeredgewidth=2.8, zorder=6)

# the two numbers we are going to test
ax.plot([px(-10)], [Y_LINE], marker="o", markersize=11, color=GREEN,
        zorder=6)
tick(px(-10), 4.00, 0.19, GREEN)
ax.plot([px(0)], [Y_LINE], marker="o", markersize=11, color=RED, zorder=6)
cross(px(0), 4.00, 0.19, RED)

# ------------------------------------------------------- the two tests
def test_card(x_left, x_right, colour, tint, lines):
    """One card holding the arithmetic of a single test."""
    ax.add_patch(FancyBboxPatch(
        (x_left, 1.12), x_right - x_left, 1.52,
        boxstyle="round,pad=0.0,rounding_size=0.16",
        facecolor=tint, edgecolor=colour, linewidth=1.8, zorder=1))
    cx = (x_left + x_right) / 2
    for y, text, size, bold in lines:
        ax.text(cx, y, text, ha="center", va="center", fontsize=size,
                color=colour if bold else INK,
                fontweight="bold" if bold else "normal", zorder=3)


test_card(0.85, 6.05, GREEN, GREEN_T, (
    (2.42, r"from inside:  $x = -10$", 15, False),
    (1.92, r"$-(-10) = 10$,  and  $10 > 6$", 18, False),
    (1.42, "true, as it must be", 14, True),
))
test_card(6.55, 11.75, RED, RED_T, (
    (2.42, r"from outside:  $x = 0$", 15, False),
    (1.92, r"$-(0) = 0$,  and  $0 > 6$", 18, False),
    (1.42, "false, as it must be", 14, True),
))

ax.text(0.45, 0.36,
        "had the symbol not been turned round the answer would have been "
        "$x > -6$, which holds $0$ - so the number from outside is the one "
        "that catches the mistake",
        ha="left", va="center", fontsize=12.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_05_testing_the_answer.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_05_testing_the_answer.png")
