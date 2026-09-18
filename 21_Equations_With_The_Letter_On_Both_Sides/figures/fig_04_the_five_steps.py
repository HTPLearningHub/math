"""Figure 4 - the five steps, and which of them are new.

Steps 1 and 2 only clear the way: they are done when, and only when, the
equation actually has a bracket or a fraction in it. Steps 3, 4 and 5 are
Chapter 20's loop wearing a new coat. Two vertical bars on the right say
which is which, so the reader can see how little is really new.

The check hangs below, detached, because it is not one of the five - it
is done every time whatever the equation looked like.

Horizontal plan (x):
    0.85  the step number, in a small circle
    1.30  the left edge of every box (width 6.80)
    8.30  the vertical bar that groups the steps
    8.45  the label for that group, left aligned

Vertical plan (y, top to bottom):
    5.70  heading
    5.15  step 1        }  bar from 5.46 to 4.07
    4.38  step 2        }
    3.61  step 3        }
    2.84  step 4        }  bar from 3.92 to 1.76
    2.07  step 5        }
    1.10  the check, detached and green
    0.30  closing note

Run with:  python figures/fig_04_the_five_steps.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
from pathlib import Path

BLUE = "#2E86DE"          # the letter, and the steps that chase it
ORANGE = "#E67E22"        # the steps that clear the way
GREEN = "#1E8449"         # the finished line
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"

W, H = 10.80, 6.10
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BOX_X, BOX_W, BOX_H = 1.30, 6.80, 0.54

ax.text(0.60, 5.70, "five steps, and only the first two are new",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

STEPS = (
    (5.15, "1", "open every bracket", ORANGE, TINT_ORANGE),
    (4.38, "2", "clear every fraction", ORANGE, TINT_ORANGE),
    (3.61, "3", "gather the letters on one side", BLUE, TINT_BLUE),
    (2.84, "4", "gather the plain numbers on the other side", BLUE, TINT_BLUE),
    (2.07, "5", "divide by the number in front of the letter", BLUE,
     TINT_BLUE),
)
for ypos, number, words, colour, tint in STEPS:
    ax.add_patch(FancyBboxPatch((BOX_X, ypos - BOX_H / 2), BOX_W, BOX_H,
                                boxstyle="round,pad=0.04,rounding_size=0.14",
                                facecolor=tint, edgecolor=colour,
                                linewidth=2.2, zorder=3))
    ax.text(BOX_X + 0.28, ypos, words, ha="left", va="center",
            fontsize=16, color=INK, zorder=4)
    ax.add_patch(Circle((0.85, ypos), 0.22, facecolor="white",
                        edgecolor=colour, linewidth=2.0, zorder=4))
    ax.text(0.85, ypos, number, ha="center", va="center", fontsize=13,
            color=colour, zorder=5)

# the two grouping bars, each with its label to the right of it
GROUPS = (
    (5.46, 4.07, ORANGE, "do these only when\nthe equation really\nhas one"),
    (3.92, 1.76, BLUE, "this part is\nChapter 20,\nunchanged"),
)
for top, bottom, colour, label in GROUPS:
    ax.plot([8.30, 8.30], [bottom, top], linewidth=3.0, color=colour,
            solid_capstyle="round")
    ax.text(8.45, (top + bottom) / 2, label, ha="left", va="center",
            fontsize=12, color=colour)

# the check is not a sixth step; it is what you always do at the end
ax.add_patch(FancyBboxPatch((BOX_X, 1.10 - BOX_H / 2), BOX_W, BOX_H,
                            boxstyle="round,pad=0.04,rounding_size=0.14",
                            facecolor=TINT_GREEN, edgecolor=GREEN,
                            linewidth=2.4, zorder=3))
ax.text(BOX_X + 0.28, 1.10, "put the answer into the original equation",
        ha="left", va="center", fontsize=16, color=INK, zorder=4)
ax.text(8.45, 1.10, "every time", ha="left", va="center", fontsize=12,
        color=GREEN)

ax.text(0.60, 0.30, "steps 1 and 2 remove what is in the way. after them, "
        "the equation is one you can already solve", ha="left", va="center",
        fontsize=14, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_the_five_steps.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_04_the_five_steps.png")
