"""Figure 4 - a subtraction of fractions walked out on the number line.

Chapter 9, section 4.1 taught subtraction as a walk to the left along the
number line. Nothing about that changes when the steps are fractions - only
the size of one step does. Here one step is one thirty-fifth, and the walk
starts at 10 steps to the right of zero and goes 21 steps to the left. It
therefore passes zero and stops 11 steps on the other side.

Every tick on the line is one thirty-fifth, which is the point: once both
fractions are written in thirty-fifths, they are whole numbers of identical
steps and the picture is the Chapter 9 picture exactly.

Colours: blue is where the walk starts, orange is the step being taken away,
green is the answer, and the negative half of the line is tinted grey.

Run with:  python figures/fig_04_negative_on_the_line.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"             # where the walk starts, 10/35
ORANGE = "#E67E22"           # the amount taken away, 21/35
GREEN = "#1E8449"            # the answer, -11/35
GREY = "#78909C"
INK = "#212121"

LO, HI = -16, 16             # the line runs from -16/35 to +16/35
W, H = 12.60, 5.90
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

X0, X1 = 0.95, W - 0.95      # the two ends of the drawn line, in inches
BASE = 2.45                  # the height of the number line


def px(n):
    """Turn a count of thirty-fifths into a position on the page."""
    return X0 + (n - LO) * (X1 - X0) / (HI - LO)


# ----------------------------------------------- the negative half, tinted grey
ax.add_patch(Rectangle((px(LO), BASE - 0.30), px(0) - px(LO), 0.60,
                       facecolor="#ECEFF1", edgecolor="none", zorder=1))
ax.text(px(-14.2), BASE + 0.58, "below zero", ha="center", va="center",
        fontsize=12.5, color=GREY)

# ------------------------------------------------------------------- the line
ax.annotate("", xy=(px(HI) + 0.25, BASE), xytext=(px(LO) - 0.25, BASE),
            arrowprops=dict(arrowstyle="<->", color=INK, linewidth=1.8),
            zorder=3)

for n in range(LO, HI + 1):
    tall = (n % 5 == 0)
    ax.plot([px(n), px(n)], [BASE - (0.20 if tall else 0.10),
                             BASE + (0.20 if tall else 0.10)],
            color=INK if tall else GREY, linewidth=1.6 if tall else 1.0,
            zorder=4)

# only the multiples of five are labelled, or the line becomes unreadable
for n in range(LO + 1, HI, 1):
    if n % 5 == 0 and n != 0:
        sign = "-" if n < 0 else ""
        ax.text(px(n), BASE - 0.52, rf"${sign}\frac{{{abs(n)}}}{{35}}$",
                ha="center", va="center", fontsize=13, color=GREY)

ax.text(px(0), BASE - 0.55, "$0$", ha="center", va="center",
        fontsize=17, color=INK)

# ------------------------------------------------- the walk: start, step, land
ax.plot([px(10)], [BASE], marker="o", markersize=12, color=BLUE, zorder=6)
ax.plot([px(-11)], [BASE], marker="o", markersize=12, color=GREEN, zorder=6)

# the jump itself, drawn as an arc above the line so it does not hide the ticks
ax.add_patch(FancyArrowPatch((px(10), BASE + 0.26), (px(-11), BASE + 0.26),
                             connectionstyle="arc3,rad=0.30",
                             arrowstyle="-|>,head_length=12,head_width=6",
                             color=ORANGE, linewidth=2.4, zorder=5))

ax.text(px(0), BASE + 2.10, "21 steps to the left", ha="center", va="center",
        fontsize=16, color=ORANGE, fontweight="bold")
ax.text(px(0), BASE + 1.72, r"each step is $\frac{1}{35}$",
        ha="center", va="center", fontsize=14, color=ORANGE)

# the two end labels, placed below the line so the arc stays clear
ax.text(px(10), BASE - 1.18, r"start at $\frac{10}{35}$", ha="center",
        va="center", fontsize=15, color=BLUE)
ax.text(px(10), BASE - 1.62, r"which is $\frac{2}{7}$", ha="center",
        va="center", fontsize=13, color=GREY)

ax.text(px(-11), BASE - 1.18, r"land on $-\frac{11}{35}$", ha="center",
        va="center", fontsize=15, color=GREEN, fontweight="bold")
ax.text(px(-11), BASE - 1.62, "past zero, so negative", ha="center",
        va="center", fontsize=13, color=GREY)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.40,
        "Taking away more than you have, in thirty-fifths",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")

# ------------------------------------------------------------- the bottom line
ax.text(W / 2, 0.36,
        r"$\frac{2}{7} - \frac{3}{5} = \frac{10}{35} - \frac{21}{35} "
        r"= -\frac{11}{35}$",
        ha="center", va="center", fontsize=19, color=INK)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_04_negative_on_the_line.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
