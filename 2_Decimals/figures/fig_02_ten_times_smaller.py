"""Figure 2 - one whole, one tenth, one hundredth, one thousandth.

Four bars of exactly the same length. Every bar is one whole.
Bar 1 is completely shaded. Bar 2 is cut into 10 parts and one part is shaded.
Bar 3 is cut into 100 parts, bar 4 into 1000 parts, one part shaded each time.
The shaded piece becomes ten times smaller on every line, until it is almost
impossible to see - which is exactly the point.
Run with:  python figures/fig_02_ten_times_smaller.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

PART = "#E67E22"      # orange - the shaded piece
EMPTY = "#ECEFF1"     # pale grey - the rest of the whole
EDGE = "#B0BEC5"      # light grey - the thin lines between the parts
FRAME = "#546E7A"     # darker grey - the outline of the whole bar

# one tuple per bar: (how many parts, label on the left, label on the right)
rows = [
    (1, r"$1$ whole", r"$1$"),
    (10, r"$1$ part out of $10$", r"$0.1 = \frac{1}{10}$"),
    (100, r"$1$ part out of $100$", r"$0.01 = \frac{1}{100}$"),
    (1000, r"$1$ part out of $1000$", r"$0.001 = \frac{1}{1000}$"),
]

BAR_W, BAR_H, STEP = 10.0, 0.95, 1.65      # bar width, bar height, distance between bars
TOP = (len(rows) - 1) * STEP               # y of the first bar

fig, ax = plt.subplots(figsize=(12.0, 5.6))
ax.axis("off")
ax.set_xlim(-6.6, BAR_W + 4.4)
ax.set_ylim(-0.9, TOP + BAR_H + 0.4)

for i, (parts, left_label, right_label) in enumerate(rows):
    y = TOP - i * STEP                     # first row on top, last row at the bottom
    piece = BAR_W / parts                  # width of one single part

    ax.add_patch(Rectangle((0, y), BAR_W, BAR_H,                  # the whole bar, empty
                           facecolor=EMPTY, edgecolor="none"))
    ax.add_patch(Rectangle((0, y), piece, BAR_H,                  # the one shaded part
                           facecolor=PART, edgecolor="none"))

    if parts == 10:                        # only the tenths bar gets dividing lines;
        for k in range(1, parts):          # 100 or 1000 lines would be a grey smudge
            ax.plot([k * piece, k * piece], [y, y + BAR_H], color=EDGE, linewidth=1.2)

    ax.add_patch(Rectangle((0, y), BAR_W, BAR_H,                  # the outline on top
                           facecolor="none", edgecolor=FRAME, linewidth=2.0))

    ax.text(-0.45, y + BAR_H / 2, left_label, ha="right", va="center",
            fontsize=13, color="#37474F")
    ax.text(BAR_W + 0.45, y + BAR_H / 2, right_label, ha="left", va="center",
            fontsize=15, fontweight="bold", color=PART if parts > 1 else "#37474F")

    if parts >= 100:                       # point at a piece that is nearly invisible
        ax.annotate("the piece is here, almost too thin to see",
                    xy=(piece, y + BAR_H / 2), xytext=(1.5, y + BAR_H / 2),
                    ha="left", va="center", fontsize=11, color=PART,
                    arrowprops=dict(arrowstyle="->", color=PART, linewidth=1.6))

# the arrow on the left that says what happens from one line to the next
ax.annotate("", xy=(-5.9, 0.15), xytext=(-5.9, TOP + BAR_H - 0.15),
            arrowprops=dict(arrowstyle="-|>", color=PART, linewidth=2.4))
ax.text(-6.25, (TOP + BAR_H) / 2, r"each step: $\div\, 10$",
        ha="center", va="center", rotation=90,
        fontsize=13, fontweight="bold", color=PART)

ax.set_title("Every step to the right cuts the whole into ten times more pieces",
             fontsize=16, fontweight="bold", pad=12)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_ten_times_smaller.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
