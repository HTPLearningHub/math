"""Figure 2 - the trading rule that both carrying and borrowing are built on.

Three rows, one per trade: ten ones make one ten, ten tens make one hundred,
ten hundreds make one thousand. The ten pieces on the left are blue; the single
new piece they are traded for is orange, the colour this book uses for the piece
that moves.

The tokens are symbols, not drawn to scale - a real thousand block would be a
thousand times the area of a one block and would not fit on the page. The token
grows a little from row to row so that the reader feels the step up, while the
group of ten is squeezed into a band of fixed width so the rows stay aligned.

Run with:  python figures/fig_02_ten_make_one.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # the ten pieces we already have
BLUE_FILL = "#EAF2FB"
ORANGE = "#E67E22"      # the single new piece we trade them for
ORANGE_FILL = "#FDF0E3"
INK = "#212121"

# one entry per row: value of a small piece, value of the new piece, token size,
# the name of the ten, the name of the one
ROWS = [(1, 10, 0.44, "ten ones", "one ten"),
        (10, 100, 0.54, "ten tens", "one hundred"),
        (100, 1000, 0.64, "ten hundreds", "one thousand")]

W, H = 12.0, 7.6
BAND = 6.0              # every group of ten is squeezed into this width
X_START = 0.55          # left edge of the group of ten
X_ARROW = 7.15          # tail of the trade arrow
ARROW_LEN = 1.10
X_MID = 9.55            # centre of the single new token

fig, ax = plt.subplots(figsize=(W, H))
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")              # the tokens must stay square

ax.text(W / 2, H - 0.28, "Ten pieces of one size trade for one piece of the next size",
        ha="center", va="center", fontsize=17, fontweight="bold", color=INK)

for r, (small, big, size, left_name, right_name) in enumerate(ROWS):
    y = 6.15 - r * 2.00             # centre line of this row
    gap = (BAND - 10 * size) / 9    # whatever space is left over between tokens

    # --- the ten pieces we start with -------------------------------------
    for i in range(10):
        x = X_START + i * (size + gap)
        ax.add_patch(FancyBboxPatch((x, y - size / 2), size, size,
                                    boxstyle="round,pad=0.01,rounding_size=0.05",
                                    facecolor=BLUE_FILL, edgecolor=BLUE, linewidth=1.6))
        ax.text(x + size / 2, y, str(small), ha="center", va="center",
                fontsize=8 if small == 100 else 10, color=BLUE)
    ax.text(X_START + BAND / 2, y - size / 2 - 0.26, left_name,
            ha="center", va="top", fontsize=14, color=BLUE, fontweight="bold")

    # --- the trade arrow ---------------------------------------------------
    ax.annotate("", xy=(X_ARROW + ARROW_LEN, y), xytext=(X_ARROW, y),
                arrowprops=dict(arrowstyle="-|>", color=INK, linewidth=2.2,
                                mutation_scale=20))
    ax.text(X_ARROW + ARROW_LEN / 2, y + 0.20, "trade for", ha="center", va="bottom",
            fontsize=11, color=INK)

    # --- the single new piece ---------------------------------------------
    new = size * 1.8                # drawn bigger so it reads as one larger piece
    ax.add_patch(FancyBboxPatch((X_MID - new / 2, y - new / 2), new, new,
                                boxstyle="round,pad=0.01,rounding_size=0.06",
                                facecolor=ORANGE_FILL, edgecolor=ORANGE, linewidth=2.2))
    ax.text(X_MID, y, str(big), ha="center", va="center",
            fontsize=13, color=ORANGE, fontweight="bold")
    ax.text(X_MID, y - new / 2 - 0.26, right_name,
            ha="center", va="top", fontsize=14, color=ORANGE, fontweight="bold")

ax.text(W / 2, 0.30, "The amount never changes. Only the way it is packed changes.",
        ha="center", va="center", fontsize=13, color=INK, style="italic")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_02_ten_make_one.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
