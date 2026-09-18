"""Figure 6 - the method, with the one step Chapter 20 did not have.

This is deliberately the same shape as Chapter 20 figure 6: a row of
boxes with a loop arrow running back from the "is the letter alone?"
question to the start. The reader is meant to recognise it.

Only one box is new, and it is the only orange one. Everything blue is
work the reader already owns from Chapter 20. Drawing it this way says
the chapter's main claim - "you already know how to do this, except for
one question you now have to ask after every multiply or divide" -
without a sentence of text.

Horizontal plan (x): five boxes 2.25 wide with 0.35 gaps, starting at
0.38, so the box centres are at 1.505, 4.105, 6.705, 9.305 and 11.905.

Vertical plan (y, top to bottom):
    4.38  heading
    3.90  the step numbers
    3.66  top of the boxes
    2.85  the middle of the boxes
    2.04  bottom of the boxes
    0.95  the label on the loop, on a white pad so the arc does not
          run through the letters
    0.22  closing note

Run with:  python figures/fig_06_the_method.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # steps that are already Chapter 20's
ORANGE = "#E67E22"        # the one step this chapter adds, and the loop
GREEN = "#1E8449"         # the check at the end
GREY = "#78909C"
INK = "#212121"
BLUE_T = "#E9F2FC"
ORANGE_T = "#FDF0E3"
GREEN_T = "#E8F5EC"

W, H = 13.40, 4.72
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BW, BH = 2.25, 1.62          # box width and height
Y_MID = 2.85
Y_TOP = Y_MID + BH / 2
Y_BOT = Y_MID - BH / 2

# (text, edge colour, fill colour)
STEPS = (
    ("look at the letter\nand ask what has\nbeen done to it", BLUE, BLUE_T),
    ("undo the last one,\non both sides", BLUE, BLUE_T),
    ("was that a multiply\nor divide by a\nnegative number?\nthen turn the\nsymbol round",
     ORANGE, ORANGE_T),
    ("is the letter\nalone now?", BLUE, BLUE_T),
    ("test one number\nfrom inside your\nanswer and one\nfrom outside", GREEN,
     GREEN_T),
)

centres = []
x = 0.38
for index, (text, edge, fill) in enumerate(STEPS, start=1):
    cx = x + BW / 2
    centres.append(cx)
    ax.add_patch(FancyBboxPatch(
        (x, Y_BOT), BW, BH,
        boxstyle="round,pad=0.0,rounding_size=0.16",
        facecolor=fill, edgecolor=edge, linewidth=2.0, zorder=2))
    # the step number sits above its box, in the box's own colour
    ax.text(cx, 3.90, str(index), ha="center", va="center", fontsize=15,
            color=edge, fontweight="bold")
    ax.text(cx, Y_MID, text, ha="center", va="center", fontsize=12.5,
            color=INK, linespacing=1.45, zorder=3)
    x += BW + 0.35

# the arrows between the boxes
for left, right in zip(centres, centres[1:]):
    ax.add_patch(FancyArrowPatch(
        (left + BW / 2 + 0.03, Y_MID), (right - BW / 2 - 0.03, Y_MID),
        arrowstyle="-|>", mutation_scale=20, linewidth=2.2, color=INK,
        shrinkA=0, shrinkB=0, zorder=1))

# the loop: from the question in box 4 back to box 1, under the row
ax.add_patch(FancyArrowPatch(
    (centres[3], Y_BOT - 0.05), (centres[0], Y_BOT - 0.05),
    connectionstyle="arc3,rad=-0.28",
    arrowstyle="-|>", mutation_scale=22, linewidth=2.6, color=ORANGE,
    shrinkA=0, shrinkB=0, zorder=1))
ax.text((centres[0] + centres[3]) / 2, 0.95,
        "if not, go back and ask again", ha="center", va="center",
        fontsize=13.5, color=ORANGE, fontweight="bold", zorder=5,
        bbox=dict(boxstyle="round,pad=0.28", facecolor="white",
                  edgecolor="none"))

ax.text(0.38, 4.38,
        "the same four steps as an equation, with one extra question in the middle",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

ax.text(0.38, 0.22,
        "blue is Chapter 20 exactly as it stands; only the orange box is new, "
        "and only the green one is done differently",
        ha="left", va="center", fontsize=12.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_06_the_method.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_06_the_method.png")
