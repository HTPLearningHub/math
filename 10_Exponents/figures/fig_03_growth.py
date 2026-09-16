"""Figure 3 - adding, multiplying and raising to a power, drawn on one pair of axes.

The chapter claims that a power grows in a way the other two operations
never approach. A table of numbers says it; this says it far louder, because
the reader can see that the orange and blue lines are still crawling along
the bottom when the purple one has left the picture.

Every point is computed, not typed, so the curve cannot disagree with the
table in the text.
Run with:  python figures/fig_03_growth.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"
PURPLE = "#8E44AD"      # the power - the line that runs away
GREY = "#78909C"
ORANGE = "#E67E22"
INK = "#212121"

STEPS = list(range(0, 11))                      # n from 0 to 10
add = [2 + n for n in STEPS]                    # 2 + n
mul = [2 * n for n in STEPS]                    # 2 x n
pow_ = [2 ** n for n in STEPS]                  # 2 to the power n

fig, ax = plt.subplots(figsize=(10.2, 6.0))

ax.plot(STEPS, add, "-o", color=ORANGE, linewidth=2.4, markersize=6, label=r"$2 + n$")
ax.plot(STEPS, mul, "-s", color=BLUE, linewidth=2.4, markersize=6, label=r"$2 \times n$")
ax.plot(STEPS, pow_, "-^", color=PURPLE, linewidth=3.0, markersize=8, label=r"$2^{n}$")

# name the end of the runaway line, where there is room for it
ax.annotate(r"$2^{10} = 1\,024$", xy=(10, 1024), xytext=(7.55, 930),
            fontsize=14.5, color=PURPLE, ha="right", fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=PURPLE, linewidth=1.2))

# the sentence the picture is making
ax.text(0.35, 800, "Both of the lines\nalong the bottom are\nstill there. They have\n"
                   "simply been left\nbehind.",
        fontsize=13.5, color=GREY, va="top", linespacing=1.6)

# the three tenth-step values, listed instead of labelled on the lines themselves:
# an arrow reaching across to n = 10 would have to cut through the purple curve
ax.text(0.35, 355, "After ten steps", fontsize=14, color=INK,
        fontweight="bold", va="top")
ENDINGS = [(r"$2 + n$  reaches  $12$", ORANGE),
           (r"$2 \times n$  reaches  $20$", BLUE),
           (r"$2^{n}$  reaches  $1\,024$", PURPLE)]
for k, (text, colour) in enumerate(ENDINGS):
    ax.text(0.35, 285 - k * 74, text, fontsize=13.5, color=colour, va="top")

ax.set_xlabel(r"the step $n$", fontsize=14)
ax.set_ylabel("the value", fontsize=14)
ax.set_title("Three ways to use the number 2, ten steps each",
             fontsize=17, color=INK, fontweight="bold", pad=14)
ax.set_xticks(STEPS)
ax.set_xlim(-0.35, 10.6)
ax.set_ylim(-45, 1120)
ax.grid(True, color="#E4E9EE", linewidth=1)
ax.set_axisbelow(True)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
ax.legend(fontsize=15, frameon=False, loc="upper left", bbox_to_anchor=(0.02, 0.98))

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_growth.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
