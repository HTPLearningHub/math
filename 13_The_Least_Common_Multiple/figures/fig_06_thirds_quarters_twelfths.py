"""Figure 6 - why the LCM of the two bottom numbers is the right cut.

The source draws this with text characters, which the book never does, and
the ASCII version also gets the point backwards: it shows the answer without
showing that both bars are cut the *same* way. Here all four bars are exactly
the same length, so the only thing that changes between them is where the
cuts fall.

Rows 1 and 2 are the same amount, one third, cut coarsely and then finely.
Rows 3 and 4 are one quarter, the same way. Twelfths are the first cut that
works for both, because 12 is the least common multiple of 3 and 4 - and
once both bars are cut into twelfths, comparing them is just counting.
Run with:  python figures/fig_06_thirds_quarters_twelfths.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"             # the first fraction, one third
ORANGE = "#E67E22"           # the second fraction, one quarter
GREEN = "#1E8449"            # the conclusion
GREY = "#78909C"
INK = "#212121"

W, H = 11.00, 6.80
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

LEFT = 2.70                  # left edge of every bar
BAR_W = 7.20                 # every bar is the same length - this is the point
BAR_H = 0.62

FILL = {BLUE: "#D6E8FA", ORANGE: "#FBE3CC"}


def bar(y, parts, shaded, colour, label, note):
    """One bar cut into `parts` equal pieces, with the first `shaded` filled."""
    piece = BAR_W / parts
    for k in range(parts):
        x = LEFT + k * piece
        ax.add_patch(Rectangle((x, y), piece, BAR_H,
                               facecolor=FILL[colour] if k < shaded else "white",
                               edgecolor=colour if k < shaded else GREY,
                               linewidth=1.6 if k < shaded else 1.0,
                               zorder=2))
    # the outline of the whole bar, drawn last so the ends stay crisp
    ax.add_patch(Rectangle((LEFT, y), BAR_W, BAR_H, facecolor="none",
                           edgecolor=GREY, linewidth=1.6, zorder=3))
    ax.text(LEFT - 0.30, y + BAR_H / 2 + 0.11, label, ha="right", va="center",
            fontsize=21, color=colour)
    ax.text(LEFT - 0.30, y + BAR_H / 2 - 0.26, note, ha="right", va="center",
            fontsize=12, color=GREY)
    return LEFT + shaded * piece          # x where the shaded part ends


Y1, Y2, Y3, Y4 = 5.05, 4.10, 2.75, 1.80

e1 = bar(Y1, 3, 1, BLUE, r"$\frac{1}{3}$", "cut into 3")
e2 = bar(Y2, 12, 4, BLUE, r"$\frac{4}{12}$", "cut into 12")
e3 = bar(Y3, 4, 1, ORANGE, r"$\frac{1}{4}$", "cut into 4")
e4 = bar(Y4, 12, 3, ORANGE, r"$\frac{3}{12}$", "cut into 12")

# ------- dashed drops, to show that the finer cut does not move the edge
for x_top, y_top, x_bot, y_bot, colour in ((e1, Y1, e2, Y2 + BAR_H, BLUE),
                                           (e3, Y3, e4, Y4 + BAR_H, ORANGE)):
    ax.plot([x_top, x_bot], [y_top, y_bot], color=colour, linewidth=1.6,
            linestyle=(0, (4, 3)), zorder=4)

# the label sits between the two bars of a pair, because it is about the pair
ax.text(LEFT + BAR_W + 0.18, (Y1 + Y2 + BAR_H) / 2, "same amount", ha="left",
        va="center", fontsize=12, color=GREY)
ax.text(LEFT + BAR_W + 0.18, (Y3 + Y4 + BAR_H) / 2, "same amount", ha="left",
        va="center", fontsize=12, color=GREY)

# --------------------------------------------------------- the two comparisons
ax.annotate("", xy=(e2, Y2 - 0.16), xytext=(LEFT, Y2 - 0.16),
            arrowprops=dict(arrowstyle="|-|,widthA=0.3,widthB=0.3",
                            color=BLUE, linewidth=1.4))
ax.text((LEFT + e2) / 2, Y2 - 0.44, "4 pieces", ha="center", va="center",
        fontsize=13, color=BLUE, fontweight="bold")

ax.annotate("", xy=(e4, Y4 - 0.16), xytext=(LEFT, Y4 - 0.16),
            arrowprops=dict(arrowstyle="|-|,widthA=0.3,widthB=0.3",
                            color=ORANGE, linewidth=1.4))
ax.text((LEFT + e4) / 2, Y4 - 0.44, "3 pieces", ha="center", va="center",
        fontsize=13, color=ORANGE, fontweight="bold")

# ------------------------------------------------------------- the conclusion
ax.text(W / 2, 0.86, "the pieces are the same size, so 4 of them beat 3 of them",
        ha="center", va="center", fontsize=14, color=GREY)
# written as three pieces, so that the word "so" is not set in maths type
ax.text(W / 2 - 1.10, 0.36, r"$\frac{4}{12} > \frac{3}{12}$", ha="center",
        va="center", fontsize=22, color=GREEN)
ax.text(W / 2, 0.36, "so", ha="center", va="center", fontsize=16, color=GREEN)
ax.text(W / 2 + 1.10, 0.36, r"$\frac{1}{3} > \frac{1}{4}$", ha="center",
        va="center", fontsize=22, color=GREEN)

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.40, r"Cut both bars into $\mathrm{LCM}(3,\, 4) = 12$ pieces",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.86, "twelfths is the first cut that fits thirds and quarters at once",
        ha="center", va="center", fontsize=13, color=GREY)

out = (Path(__file__).resolve().parent.parent / "assets"
       / "fig_06_thirds_quarters_twelfths.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
