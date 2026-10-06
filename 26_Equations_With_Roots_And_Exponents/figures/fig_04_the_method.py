"""Figure 4 - the whole method for an equation with a root or a power.

Four boxes in one column, joined by arrows:
    1  isolate the root or the power      (grey  - Chapter 20's moves)
    2  undo it                            (orange - the new move)
    3  solve what is left                 (grey  - Chapters 20 and 21)
    4  check every answer                 (green - never optional)
To the right of box 2, a small table says which move undoes which shape.
To the right of box 4, a red note says why the check is compulsory after
squaring. This figure replaces the source's ASCII flowchart.

Run with:  python figures/fig_04_the_method.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

ORANGE = "#E67E22"                                 # the new move
GREEN = "#1E8449"                                  # the check
RED = "#C0392B"                                    # the warning
GREY = "#78909C"                                   # old moves, labels
INK = "#212121"

TINT = {ORANGE: "#FDF0E3", GREEN: "#E8F5EC", GREY: "#ECEFF1",
        RED: "#FBEAEA"}

W, H = 14.4, 9.6                                   # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CX = 3.60                                          # the main column
BW, BH = 6.40, 1.25                                # every step box, same size
YS = [8.35, 6.15, 3.95, 1.75]                      # the four box centres


def box(cx, cy, colour, title, body, w=BW, h=BH):
    """One rounded step box: a bold title and a quiet line underneath."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.14",
                                facecolor=TINT[colour], edgecolor=colour,
                                linewidth=2.0, zorder=3))
    ax.text(cx, cy + 0.22, title, ha="center", va="center",
            fontsize=15, color=INK, fontweight="bold", zorder=4)
    ax.text(cx, cy - 0.25, body, ha="center", va="center",
            fontsize=12.5, color=GREY, zorder=4)


def arrow(x1, y1, x2, y2, colour=GREY):
    """A plain straight arrow between two points."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=colour, linewidth=2.0,
                                shrinkA=0, shrinkB=0), zorder=2)


box(CX, YS[0], GREY, "1   get the root or power alone",
    r"undo every $+$, $-$, $\times$, $\div$ standing outside it")
box(CX, YS[1], ORANGE, "2   undo the root or the power",
    "do the same to both sides  (the table on the right)")
box(CX, YS[2], GREY, "3   solve what is left",
    "open brackets, gather the letters, divide  (Chapters 20, 21)")
box(CX, YS[3], GREEN, "4   check every answer",
    "in the ORIGINAL equation, each side on its own")

for a, b in zip(YS[:-1], YS[1:]):                  # arrows down the column
    arrow(CX, a - BH / 2, CX, b + BH / 2)

# ------------------------------------------------- the table beside box 2
tx = 7.50                                          # left edge of the table
rows = [
    (r"$\sqrt{\ \ }$  on one side", "square both sides"),
    (r"$\sqrt[3]{\ \ }$  on one side", "cube both sides"),
    (r"power $\frac{m}{n}$", r"raise to the power $\frac{n}{m}$"),
    (r"$x^{2} = k$", r"take the root, and write $\pm$"),
    (r"a number in front: $3\sqrt{\ \ }$", r"square the $3$ as well"),
]
ax.text(tx, 7.55, "if you see ...", ha="left", va="center", fontsize=13.5,
        color=GREY, fontweight="bold")
ax.text(tx + 3.65, 7.55, "... do this", ha="left", va="center",
        fontsize=13.5, color=ORANGE, fontweight="bold")
y = 6.95
for shape, move in rows:                           # one row per shape
    ax.text(tx, y, shape, ha="left", va="center", fontsize=14, color=INK)
    ax.text(tx + 3.65, y, move, ha="left", va="center", fontsize=14,
            color=ORANGE)
    y -= 0.58
# a thin bracket line joining box 2 to its table
ax.plot([CX + BW / 2, tx - 0.20], [YS[1], YS[1]], color=ORANGE, lw=1.4,
        ls=(0, (3, 3)), zorder=1)

# ------------------------------------------------- the warning beside box 4
wx, wy, ww, wh = 7.50, YS[3] - 0.95, 6.50, 1.90
ax.add_patch(FancyBboxPatch((wx, wy), ww, wh,
                            boxstyle="round,pad=0.02,rounding_size=0.14",
                            facecolor=TINT[RED], edgecolor=RED, linewidth=1.6,
                            zorder=3))
ax.text(wx + 0.25, wy + wh - 0.42, "after squaring, the check is not optional",
        ha="left", va="center", fontsize=14, color=RED, fontweight="bold",
        zorder=4)
ax.text(wx + 0.25, wy + wh - 0.95,
        "squaring can let in a number that does not work",
        ha="left", va="center", fontsize=12.5, color=INK, zorder=4)
ax.text(wx + 0.25, wy + wh - 1.40,
        "throw away any answer that fails  (section 6)",
        ha="left", va="center", fontsize=12.5, color=INK, zorder=4)
ax.plot([CX + BW / 2, wx], [YS[3], YS[3]], color=RED, lw=1.4,
        ls=(0, (3, 3)), zorder=1)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_the_method.png", dpi=170, bbox_inches="tight",
            facecolor="white")
print("wrote", out / "fig_04_the_method.png")
