"""Figure 1 - the question the whole chapter answers.

The source keeps its pen problem for the very last practice question and
gives only the answer. It is a much better opening than an ending, because
it shows in one picture what a *common factor* is and why *greatest* matters.

Three attempts stand side by side: 5 pouches (works, but small), 10 pouches
(fails - 45 does not cut into 10), and 15 pouches (works, and nothing bigger
can). Each pile is drawn as a row of pens cut into equal parts, with a wide
gap between parts and a narrow one between pens, so a part is something the
eye counts rather than reads. Both rows start at the same left edge, so the
blue pile is visibly the shorter one. The middle panel is the important one:
it is the only place in the chapter where a split is shown failing, and the
five pens that cannot be placed are drawn as dashed ghosts, so the failure
is visible rather than asserted.

Run with:  python figures/fig_01_pens_into_pouches.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

BLUE = "#2E86DE"             # the 30 blue pens
ORANGE = "#E67E22"           # the 45 red pens (orange reads better on screen)
GREEN = "#1E8449"            # a split that works
GREY = "#78909C"             # leftovers, quiet labels
RED = "#C0392B"              # a split that fails
INK = "#212121"

W, H = 14.00, 5.70
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

PANEL_W, PANEL_H = 4.40, 3.45
PANEL_Y = 1.10
GAP = 0.34
LEFT = (W - 3 * PANEL_W - 2 * GAP) / 2

CW, CH = 0.048, 0.40         # one pen
CGAP = 0.014                 # space between two pens inside the same part
PGAP = 0.065                 # space between two parts - deliberately much wider

# the four text lines inside a panel, measured down from the top of the panel
Y_TITLE = 0.38
Y_BLUE_LABEL = 0.85
Y_BLUE_ROW = 1.42
Y_BLUE_NOTE = 1.67
Y_RED_LABEL = 2.11
Y_RED_ROW = 2.68
Y_RED_NOTE = 2.93


def row(x, y, total, parts, colour, leftover=0):
    """Draw `total` pens cut into `parts` equal groups, plus `leftover` ghosts."""
    per = (total - leftover) // parts
    cx = x
    for _ in range(parts):
        for _ in range(per):
            ax.add_patch(Rectangle((cx, y), CW, CH, facecolor=colour,
                                   edgecolor=colour, linewidth=0.6))
            cx += CW + CGAP
        cx += PGAP - CGAP
    # the pens that could not be placed in any group
    if leftover:
        cx += 0.14
        for _ in range(leftover):
            ax.add_patch(Rectangle((cx, y), CW, CH, facecolor="white",
                                   edgecolor=GREY, linewidth=0.9,
                                   linestyle=(0, (2, 2))))
            cx += CW + CGAP


def panel(px, parts, blue_left, red_left, ok, verdict, note):
    """Draw one attempt at splitting 30 blue and 45 red pens into `parts` parts."""
    top = PANEL_Y + PANEL_H
    ax.add_patch(FancyBboxPatch((px, PANEL_Y), PANEL_W, PANEL_H,
                                boxstyle="round,pad=0.02,rounding_size=0.16",
                                facecolor="white",
                                edgecolor=GREEN if ok else RED,
                                linewidth=2.2 if ok else 1.8))

    ax.text(px + PANEL_W / 2, top - Y_TITLE, f"{parts} pouches",
            ha="center", va="center", fontsize=17, color=INK, fontweight="bold")

    x0 = px + 0.28

    # ------------------------------------------------------------- the blue pile
    ax.text(x0, top - Y_BLUE_LABEL, "30 blue pens", ha="left", va="center",
            fontsize=13, color=BLUE, fontweight="bold")
    row(x0, top - Y_BLUE_ROW, 30, parts, BLUE, blue_left)
    ax.text(x0, top - Y_BLUE_NOTE,
            f"{(30 - blue_left) // parts} in each pouch"
            + (f", {blue_left} left over" if blue_left else ""),
            ha="left", va="center", fontsize=12,
            color=RED if blue_left else GREY)

    # -------------------------------------------------------------- the red pile
    ax.text(x0, top - Y_RED_LABEL, "45 red pens", ha="left", va="center",
            fontsize=13, color=ORANGE, fontweight="bold")
    row(x0, top - Y_RED_ROW, 45, parts, ORANGE, red_left)
    ax.text(x0, top - Y_RED_NOTE,
            f"{(45 - red_left) // parts} in each pouch"
            + (f", {red_left} left over" if red_left else ""),
            ha="left", va="center", fontsize=12,
            color=RED if red_left else GREY)

    # ------------------------------------------------ verdict and note, outside
    ax.text(px + PANEL_W / 2, PANEL_Y - 0.32, verdict, ha="center", va="center",
            fontsize=16, color=GREEN if ok else RED, fontweight="bold")
    ax.text(px + PANEL_W / 2, PANEL_Y - 0.66, note, ha="center", va="center",
            fontsize=12, color=GREY)


panel(LEFT, 5, 0, 0, True,
      "it works", "but 5 is not the largest that works")

panel(LEFT + PANEL_W + GAP, 10, 0, 5, False,
      "it fails", "45 does not cut into 10 equal parts")

panel(LEFT + 2 * (PANEL_W + GAP), 15, 0, 0, True,
      "it works, and nothing bigger does",
      "this is the greatest common factor")

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.38,
        "30 blue pens and 45 red pens, shared out into identical pouches",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.78,
        "a number of pouches works only if it divides both 30 and 45 with nothing left over",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_pens_into_pouches.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
