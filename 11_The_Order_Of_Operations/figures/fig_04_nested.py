"""Figure 4 - brackets inside brackets are peeled from the inside out.

Three rows. Each row is the same expression after one more layer has been
removed, and the layer that is about to go is ringed. The rings are drawn
as rounded boxes behind the text rather than as printed characters, so the
reader sees a wrapper being taken off and not more punctuation.

A ring drawn at a guessed position never lands on the right characters, so
every row here is built from pieces: each piece is drawn, measured with the
renderer, and the next piece starts where the last one ended. The rings are
then drawn around measured pieces, not around estimates. The doubled thin
spaces inside the pieces are there to give the rings something to sit on -
without them a ring edge lands on the neighbouring sign.
Run with:  python figures/fig_04_nested.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

ORANGE = "#E67E22"
PURPLE = "#8E44AD"
GREY = "#78909C"
INK = "#212121"

W, H = 12.6, 6.55
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])            # 1 data unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)
fig.canvas.draw()                        # a renderer must exist before measuring
REND = fig.canvas.get_renderer()

FS = 25                                  # one size for every expression piece


def width_of(s):
    """Return the width of one piece of mathtext, in data units (inches)."""
    t = ax.text(0, -50, s, fontsize=FS)                 # drawn off the picture
    w = t.get_window_extent(renderer=REND).width / fig.dpi
    t.remove()
    return w


def row(y, pieces, centre):
    """Draw pieces left to right, centred on `centre`.

    Returns a list of (left, right) x-pairs, one per piece, so that a ring
    can be drawn around any run of them afterwards.
    """
    widths = [width_of(p) for p in pieces]
    x = centre - sum(widths) / 2
    spans = []
    for p, w in zip(pieces, widths):
        ax.text(x, y, p, ha="left", va="center", fontsize=FS, color=INK,
                zorder=3)
        spans.append((x, x + w))
        x += w
    return spans


def ring(spans, first, last, edge, tint, pad_x, pad_y, y, lw=2.0):
    """Draw a rounded ring behind the pieces `first`..`last` of a row."""
    x0 = spans[first][0] - pad_x
    x1 = spans[last][1] + pad_x
    ax.add_patch(FancyBboxPatch((x0, y - pad_y), x1 - x0, 2 * pad_y,
                                boxstyle="round,pad=0.03,rounding_size=0.13",
                                facecolor=tint, edgecolor=edge,
                                linewidth=lw, zorder=1))


ax.text(W / 2, H - 0.42, "Take the innermost wrapper off first",
        ha="center", va="center", fontsize=19.5, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.92,
        "one layer per step, and nothing outside a bracket is touched until it is gone",
        ha="center", va="center", fontsize=13.5, color=GREY)

CX = 5.35                                # expressions are centred here
ROWS = (H - 2.05, H - 3.50, H - 4.70)    # the three expression lines
LABEL_X = 0.45

LEAD = r"$100 \div 5 \times 2 \; - \;\;$"        # the part outside every bracket

# ---- row 1: the whole thing, both pairs ringed --------------------------
ax.text(LABEL_X, ROWS[0], "Step 1", ha="left", va="center",
        fontsize=14, color=GREY)
s1 = row(ROWS[0],
         [LEAD, r"$[\,4 +\;\;$", r"$(8 - 3^{2})$", r"$\;\;]$"],
         CX)
ring(s1, 1, 3, ORANGE, "#FBEEE0", 0.10, 0.40, ROWS[0], lw=1.6)   # outer, pale
ring(s1, 2, 2, PURPLE, "#F3EAF8", 0.04, 0.31, ROWS[0])           # inner, strong
ax.text(s1[3][1] + 0.55, ROWS[0], "innermost pair", ha="left", va="center",
        fontsize=13.5, color=PURPLE, fontweight="bold")

# ---- row 2: the innermost pair is gone ---------------------------------
ax.text(LABEL_X, ROWS[1], "Step 2", ha="left", va="center",
        fontsize=14, color=GREY)
s2 = row(ROWS[1], [LEAD, r"$[\,4 + (-1)\,]$"], CX)
ring(s2, 1, 1, ORANGE, "#FBEEE0", 0.11, 0.35, ROWS[1])
ax.text(s2[1][1] + 0.55, ROWS[1], "now this one is the innermost",
        ha="left", va="center", fontsize=13.5, color=ORANGE, fontweight="bold")

# ---- row 3: no brackets left -------------------------------------------
ax.text(LABEL_X, ROWS[2], "Step 3", ha="left", va="center",
        fontsize=14, color=GREY)
s3 = row(ROWS[2], [r"$100 \div 5 \times 2 \; - \; 3$"], CX)
ax.text(s3[0][1] + 0.55, ROWS[2], "no brackets left, move down to Level 3",
        ha="left", va="center", fontsize=13.5, color=GREY)

# ---- the closing sentence ----------------------------------------------
ax.plot([0.45, W - 0.45], [1.02, 1.02], color=GREY,
        linewidth=1.0, linestyle=(0, (4, 3)))
ax.text(W / 2, 0.55,
        r"$8 - 3^{2}$ is worked out first, then $4 + (-1)$,"
        " and only then anything outside the square bracket.",
        ha="center", va="center", fontsize=15.5, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_nested.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
