"""Figure 4 - the four steps of long division, drawn as a ring.

Divide, Multiply, Subtract, Bring down. The ring shape is the point: the four
steps are not a list you walk down once, they are a loop you walk round again
for every digit of the dividend.

Each step keeps its own colour for the whole chapter: blue for the quotient
digit the Divide step produces, orange for the product the Multiply step
writes, purple for the difference the Subtract step leaves, green for the digit
the Bring-down step fetches. Figures 5, 7 and 8 colour the written tableau with
exactly these four colours, so the reader can read a finished tableau as four
repeating steps.
Run with:  python figures/fig_04_four_steps.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # step 1, Divide
ORANGE = "#E67E22"      # step 2, Multiply
PURPLE = "#8E44AD"      # step 3, Subtract
GREEN = "#1E8449"       # step 4, Bring down
GREY = "#78909C"
INK = "#212121"

W, H = 11.0, 6.20
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BW, BH = 4.30, 1.90                 # box width and height

# (x, y of the lower-left corner, colour, number, name, two lines of text)
STEPS = [
    (0.55, 3.85, BLUE, "1", "Divide",
     "How many times does the divisor fit\n"
     "into the number you are working on?\nWrite that digit on top."),
    (6.15, 3.85, ORANGE, "2", "Multiply",
     "Multiply the digit you just wrote\n"
     "by the divisor. Write the answer\nunderneath."),
    (6.15, 1.05, PURPLE, "3", "Subtract",
     "Take that answer away. What is\n"
     "left is smaller than the divisor,\nand it is the leftover so far."),
    (0.55, 1.05, GREEN, "4", "Bring down",
     "Fetch the next digit of the dividend\n"
     "and write it beside the leftover.\nThat is the new working number."),
]

for x, y, colour, num, name, body in STEPS:
    ax.add_patch(FancyBboxPatch((x, y), BW, BH,
                                boxstyle="round,pad=0.04,rounding_size=0.16",
                                facecolor="#FAFAFA", edgecolor=colour,
                                linewidth=2.2))
    # the step number in a small filled circle at the top-left of the box
    ax.add_patch(plt.Circle((x + 0.42, y + BH - 0.42), 0.24,
                            facecolor=colour, edgecolor="none"))
    ax.text(x + 0.42, y + BH - 0.42, num, ha="center", va="center",
            fontsize=15, color="white", fontweight="bold")
    ax.text(x + 0.82, y + BH - 0.42, name, ha="left", va="center",
            fontsize=21, color=colour, fontweight="bold")
    ax.text(x + BW / 2, y + 0.62, body, ha="center", va="center",
            fontsize=12.5, color=INK, linespacing=1.55)


def arrow(x1, y1, x2, y2):
    """One thick grey arrow along an edge of the ring."""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=GREY, linewidth=3.0,
                                mutation_scale=24))


arrow(4.99, 4.80, 6.11, 4.80)       # Divide  -> Multiply   (across the top)
arrow(8.30, 3.75, 8.30, 3.05)       # Multiply -> Subtract  (down the right)
arrow(6.11, 2.00, 4.99, 2.00)       # Subtract -> Bring down (back along the bottom)
arrow(2.70, 3.05, 2.70, 3.75)       # Bring down -> Divide  (up the left)

ax.text(W / 2, 3.40, "and\nround\nagain", ha="center", va="center",
        fontsize=12, color=GREY, fontweight="bold", linespacing=1.35)

ax.text(W / 2, 0.40, "Go round the loop once for every digit of the dividend. "
                     "Stop when there are no digits left to bring down.",
        ha="center", va="center", fontsize=14.5, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_four_steps.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
