"""Figure 5 - why -b = 3 means b = -3.

Chapter 9 section 2.2 said that a number and its opposite sit the same
distance from zero, on opposite sides. So if the opposite of b has landed
on 3, then b itself is at -3. The dashed line at zero is the mirror.

The first version joined the two dots with one curved arrow, which cut
across the number line at both ends. Two straight measuring arrows, drawn
in the empty band BELOW the tick labels, say the same thing and touch
nothing.

Vertical plan (y, top to bottom):
    4.60  heading
    3.90  "mirror at 0"
    3.15  the two dot labels, -b and b
    2.60  the number line (the mirror line runs 1.35 to 3.70)
    2.22  the tick labels
    1.85  the two measuring arrows, out from zero
    1.50  "3 steps", under each arrow
    0.55  closing note

Run with:  python figures/fig_05_the_letter_left_negative.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

ORANGE = "#E67E22"        # the thing the equation actually tells you about
GREEN = "#1E8449"         # the answer
GREY = "#78909C"
INK = "#212121"

W, H = 10.00, 5.00
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.60, 4.60, r"$-b = 3$  tells you where the opposite of $b$ is, "
        r"not where $b$ is", ha="left", va="center", fontsize=18,
        color=INK, fontweight="bold")


def px(value):
    """Turn a number-line value into an x position. -5 -> 1.0, 5 -> 9.0."""
    return 5.00 + 0.80 * value


LINE_Y = 2.60

# the number line itself, with a tick and a label at every whole number
ax.annotate("", xy=(px(5.5), LINE_Y), xytext=(px(-5.5), LINE_Y),
            arrowprops=dict(arrowstyle="<|-|>", linewidth=2.0, color=INK))
for v in range(-5, 6):
    ax.plot([px(v), px(v)], [LINE_Y - 0.13, LINE_Y + 0.13],
            color=INK, linewidth=1.8, zorder=3)
    ax.text(px(v), 2.22, str(v), ha="center", va="center", fontsize=14,
            color=GREY)

# the mirror: everything on one side has a partner the same distance away.
# Drawn in two pieces so that it does not run through the "0" tick label.
for y0, y1 in ((1.35, 2.06), (2.38, 3.70)):
    ax.plot([px(0), px(0)], [y0, y1], color=GREY, linewidth=1.8,
            linestyle=(0, (5, 4)), zorder=2)
ax.text(px(0), 3.90, "mirror at $0$", ha="center", va="center", fontsize=14,
        color=GREY)

# the two dots
ax.plot([px(3)], [LINE_Y], marker="o", markersize=13, color=ORANGE, zorder=5)
ax.text(px(3), 3.15, r"$-b$", ha="center", va="center", fontsize=25,
        color=ORANGE, fontweight="bold")

ax.plot([px(-3)], [LINE_Y], marker="o", markersize=13, color=GREEN, zorder=5)
ax.text(px(-3), 3.15, r"$b$", ha="center", va="center", fontsize=25,
        color=GREEN, fontweight="bold")

# the two distances, measured out from the mirror in the clear band below
for target, colour in ((3, ORANGE), (-3, GREEN)):
    ax.annotate("", xy=(px(target), 1.85), xytext=(px(0), 1.85),
                arrowprops=dict(arrowstyle="-|>", linewidth=2.2,
                                color=colour))
    ax.text(px(target / 2), 1.50, r"$3$ steps", ha="center", va="center",
            fontsize=15, color=colour)

ax.text(0.60, 0.55, r"same distance, other side - so $-b = 3$ gives "
        r"$b = -3$", ha="left", va="center", fontsize=17, color=INK)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_05_the_letter_left_negative.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_05_the_letter_left_negative.png")
