"""Figure 2 - multiplying runs right to left, dividing runs left to right.

Both panels show a three-digit number with its place names underneath. The
thick arrow gives the direction of travel, and the sentence under it gives the
reason. The reason is the same fact seen twice: a leftover always moves to a
place where the pieces are a different size, and which way it moves decides
which end of the number you have to finish first.

Blue is used for the multiplication panel and orange for the division panel,
and those two colours are not reused for anything else in this figure, so the
two halves stay visually separate.
Run with:  python figures/fig_02_two_directions.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # multiplication, and the direction it runs
ORANGE = "#E67E22"      # division, and the direction it runs
GREY = "#78909C"
PALE = "#FAFAFA"
INK = "#212121"

W, H = 12.4, 4.8
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

PLACES = ["hundreds", "tens", "ones"]


def panel(x0, colour, title, digits, arrow_to_left, headline, reason):
    """Draw one half of the figure: a title, three digits, an arrow, a reason."""
    ax.add_patch(FancyBboxPatch((x0, 0.30), 5.65, 4.20,
                                boxstyle="round,pad=0.04,rounding_size=0.16",
                                facecolor=PALE, edgecolor=colour, linewidth=2.0))
    cx = x0 + 5.65 / 2                      # centre line of this panel
    ax.text(cx, 4.10, title, ha="center", va="center",
            fontsize=18, color=colour, fontweight="bold")

    # the three digits, evenly spaced, with the name of their place below
    xs = [cx - 1.30, cx, cx + 1.30]
    for x, d, place in zip(xs, digits, PLACES):
        ax.text(x, 3.28, d, ha="center", va="center",
                fontsize=42, color=INK, family="DejaVu Sans Mono")
        ax.text(x, 2.66, place, ha="center", va="center",
                fontsize=12, color=GREY, fontweight="bold")

    # the arrow of travel, drawn well below the place names
    tail, head = (xs[2] + 0.55, xs[0] - 0.55) if arrow_to_left else \
                 (xs[0] - 0.55, xs[2] + 0.55)
    ax.annotate("", xy=(head, 2.06), xytext=(tail, 2.06),
                arrowprops=dict(arrowstyle="-|>", color=colour, linewidth=3.4,
                                mutation_scale=26))
    ax.text(cx, 1.58, headline, ha="center", va="center",
            fontsize=16, color=colour, fontweight="bold")
    ax.text(cx, 0.88, reason, ha="center", va="center",
            fontsize=13.5, color=INK, linespacing=1.55)


panel(0.30, BLUE, "Multiplying", "425", True,
      "start at the right",
      "A leftover here is ten of these pieces,\n"
      "so it is carried to the place on the left.\n"
      "Finish the right end first.")

panel(6.45, ORANGE, "Dividing", "624", False,
      "start at the left",
      "A leftover here is cut into ten smaller\n"
      "pieces, so it drops to the place on the right.\n"
      "Finish the left end first.")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_two_directions.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
