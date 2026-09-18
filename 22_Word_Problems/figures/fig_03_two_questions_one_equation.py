"""Figure 3 - one equation, two questions, two different jobs.

The story gives you s = 2g - 3 once. Which of the two letters the problem
hands you decides whether the job is Chapter 18's evaluating or Chapter
20's solving. The equation itself does not change at all, and that is the
point of the picture: the two lanes are the same three columns, run in
opposite directions.

Horizontal plan (x), three columns of cards, width 2.35:
    0.70 - 3.05   what you are given
    4.15 - 6.50   the line you write
    7.60 - 9.95   what you get
    10.25         the left edge of the lane label

Vertical plan (y, top to bottom):
    5.85  heading
    5.05  the equation from the story, centred, orange
    4.28  the three column headings
    3.25  lane 1, the forward lane
    1.55  lane 2, the backward lane
    0.30  closing note

Run with:  python figures/fig_03_two_questions_one_equation.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # the unknown, and the work of finding it
ORANGE = "#E67E22"        # the equation the story gave, and what is known
GREEN = "#1E8449"         # what comes out
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"

W, H = 12.90, 6.25
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CARD_W, CARD_H = 2.35, 0.86
COL_X = (0.70, 4.15, 7.60)          # left edge of each column

ax.text(0.70, 5.85, "the same equation, asked in two directions",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# the equation the story produced, written once, above both lanes
ax.add_patch(FancyBboxPatch((4.15, 5.05 - 0.40), 2.35, 0.80,
                            boxstyle="round,pad=0.05,rounding_size=0.14",
                            facecolor=TINT_ORANGE, edgecolor=ORANGE,
                            linewidth=2.4, zorder=3))
ax.text(5.325, 5.05, r"$s = 2g - 3$", ha="center", va="center",
        fontsize=19, color=INK, zorder=4)
ax.text(6.80, 5.05, "written once, from the story", ha="left",
        va="center", fontsize=12.5, color=ORANGE)

HEADINGS = ("what the problem gives you", "the line you write",
            "what you find")
for left, heading in zip(COL_X, HEADINGS):
    ax.text(left + CARD_W / 2, 4.28, heading, ha="center", va="center",
            fontsize=12.5, color=GREY)

# (y of the lane, name, colour of the name, the three cards)
LANES = (
    (3.25, "evaluate  -  Chapter 18", BLUE,
     (r"$g = 12$", r"$s = 2(12) - 3$", r"$s = 21$")),
    (1.55, "solve  -  Chapter 20", BLUE,
     (r"$s = 21$", r"$21 = 2g - 3$", r"$g = 12$")),
)
for ypos, lane_name, name_colour, cards in LANES:
    for index, (left, body) in enumerate(zip(COL_X, cards)):
        # given is orange, the working blue, the result green
        colour, tint = ((ORANGE, TINT_ORANGE), (BLUE, TINT_BLUE),
                        (GREEN, TINT_GREEN))[index]
        ax.add_patch(FancyBboxPatch((left, ypos - CARD_H / 2), CARD_W,
                                    CARD_H,
                                    boxstyle="round,pad=0.05,"
                                             "rounding_size=0.14",
                                    facecolor=tint, edgecolor=colour,
                                    linewidth=2.2, zorder=3))
        ax.text(left + CARD_W / 2, ypos, body, ha="center", va="center",
                fontsize=17, color=INK, zorder=4)
        # an arrow into the next card, except after the last one
        if index < 2:
            ax.add_patch(FancyArrowPatch((left + CARD_W + 0.16, ypos),
                                         (COL_X[index + 1] - 0.16, ypos),
                                         arrowstyle="-|>",
                                         mutation_scale=16, linewidth=2.2,
                                         color=GREY, zorder=5))
    ax.text(10.25, ypos, lane_name, ha="left", va="center", fontsize=14,
            color=name_colour)

# the two little words on the arrows, said once each, between the lanes
ax.text(3.60, 3.25 + 0.60, "put the known number in", ha="center",
        va="center", fontsize=11.5, color=GREY)
ax.text(3.60, 1.55 + 0.60, "put the known number in", ha="center",
        va="center", fontsize=11.5, color=GREY)
ax.text(7.05, 3.25 + 0.60, "work it out", ha="center", va="center",
        fontsize=11.5, color=GREY)
ax.text(7.05, 1.55 + 0.60, "undo, both sides", ha="center", va="center",
        fontsize=11.5, color=GREY)

ax.text(0.70, 0.30, "which letter the story hands you decides the job. "
        "the equation is the same equation either way",
        ha="left", va="center", fontsize=13.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_two_questions_one_equation.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_03_two_questions_one_equation.png")
