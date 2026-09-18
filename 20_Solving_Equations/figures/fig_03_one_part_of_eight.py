"""Figure 3 - why dividing by 8 is undone by multiplying by 8.

y/8 = 3 says: cut the unknown amount into eight equal parts, and one part
is 3. The bar shows all eight parts. Counting them back up is the
multiplication, so y = 8 x 3 = 24.

The first part is drawn in solid blue because it is the one the equation
tells you about. The other seven are the same size, which is the whole
point - they are equal parts.

The pointer arrow needs room to be seen as an arrow and not just a head,
so the bar sits low enough to leave 0.45 of clear space under the label.

Vertical plan (y, top to bottom):
    5.05  heading
    4.45  "this part is 3"
    4.25  the pointer arrow starts, reaching the bar top at 3.78
    2.70  the bar (height 1.00, so it reaches 3.70)
    2.30  the measuring line under the whole bar
    1.92  "eight parts: 8 x 3 = 24"
    1.00  the green answer card (height 0.80)
    0.22  closing note

Run with:  python figures/fig_03_one_part_of_eight.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from pathlib import Path

BLUE = "#2E86DE"          # the unknown amount y
GREEN = "#1E8449"         # the answer
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_GREEN = "#E8F5EC"

W, H = 11.00, 5.50
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.70, 5.05, r"$\frac{y}{8} = 3$  -  the unknown amount, cut into "
        r"eight equal parts", ha="left", va="center", fontsize=19,
        color=INK, fontweight="bold")

BAR_X0, BAR_X1 = 0.70, 10.30
BAR_Y0, BAR_H = 2.70, 1.00
N = 8
SEG_W = (BAR_X1 - BAR_X0) / N

for i in range(N):
    x0 = BAR_X0 + i * SEG_W
    first = (i == 0)
    ax.add_patch(Rectangle((x0, BAR_Y0), SEG_W, BAR_H,
                           facecolor=BLUE if first else TINT_BLUE,
                           edgecolor=BLUE, linewidth=2.0, zorder=3))
    ax.text(x0 + SEG_W / 2, BAR_Y0 + BAR_H / 2, r"$3$", ha="center",
            va="center", fontsize=21,
            color="white" if first else INK, zorder=4)

# what the equation actually told us, pointing at the part it told us about
ax.text(BAR_X0 + SEG_W / 2, 4.45, "this part is $3$", ha="center",
        va="center", fontsize=15, color=BLUE)
ax.add_patch(FancyArrowPatch((BAR_X0 + SEG_W / 2, 4.25),
                             (BAR_X0 + SEG_W / 2, BAR_Y0 + BAR_H + 0.08),
                             arrowstyle="-|>", mutation_scale=14,
                             linewidth=2.0, color=BLUE, zorder=5))

# a plain measuring line under the whole bar, with a tick at each end
ax.plot([BAR_X0, BAR_X1], [2.30, 2.30], color=GREY, linewidth=2.0, zorder=3)
for x in (BAR_X0, BAR_X1):
    ax.plot([x, x], [2.18, 2.42], color=GREY, linewidth=2.0, zorder=3)
ax.text((BAR_X0 + BAR_X1) / 2, 1.92,
        r"eight parts:  $8 \times 3 = 24$", ha="center", va="center",
        fontsize=17, color=GREY)

ax.add_patch(FancyBboxPatch((4.20, 0.60), 2.60, 0.80,
                            boxstyle="round,pad=0.05,rounding_size=0.16",
                            facecolor=TINT_GREEN, edgecolor=GREEN,
                            linewidth=2.6, zorder=3))
ax.text(5.50, 1.00, r"$y = 24$", ha="center", va="center", fontsize=26,
        color=INK, zorder=4)

ax.text(0.70, 0.22, "dividing cut the amount up; multiplying puts it back "
        "together", ha="left", va="center", fontsize=15, color=GREY,
        style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_one_part_of_eight.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_03_one_part_of_eight.png")
