"""Figure 1 - where the equation was coming from, and where it comes from now.

Chapters 20 and 21 always started at the second card: the equation was
already written down. A real problem starts one card earlier, at a story,
and it does not finish at the third card either - a number is not an
answer until it is said back in the words of the story.

So the blue middle is everything the reader already knows, and the two
orange arrows on the outside are the whole of this chapter.

Horizontal plan (x), four cards of width 2.25 with 0.45 of arrow between:
    0.42 - 2.67   card 1, the story          (grey)
    3.12 - 5.37   card 2, the equation       (blue)
    5.82 - 8.07   card 3, the number         (blue)
    8.52 - 10.77  card 4, the answer         (green)

Vertical plan (y, top to bottom):
    3.85  heading
    2.62  the four cards, height 1.34, so 1.95 to 3.29
    1.52  the name of each arrow, above the bracket
    1.08  the bracket line that says whose work it is
    0.78  whose work it is
    0.22  closing note

Run with:  python figures/fig_01_the_missing_half.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # the algebra the reader already owns
ORANGE = "#E67E22"        # the new work: translating, and answering
GREEN = "#1E8449"         # the finished answer
GREY = "#78909C"          # the story, before any mathematics happens
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"
TINT_GREY = "#ECEFF1"

W, H = 11.20, 4.25
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

CARD_W, CARD_H = 2.25, 1.34
CARD_Y = 2.62                       # centre line of the row of cards

ax.text(0.42, 3.85, "the equation is only the middle of the job",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# (left edge, border colour, fill colour, small label, the thing itself)
CARDS = (
    (0.42, GREY, TINT_GREY, "a story",
     "Sally is $3$ less\nthan twice Gabby.\nSally is $21$."),
    (3.12, BLUE, TINT_BLUE, "an equation", r"$21 = 2g - 3$"),
    (5.82, BLUE, TINT_BLUE, "a number", r"$g = 12$"),
    (8.52, GREEN, TINT_GREEN, "an answer",
     "Gabby is $12$\nyears old."),
)
for left, colour, tint, label, body in CARDS:
    ax.add_patch(FancyBboxPatch((left, CARD_Y - CARD_H / 2), CARD_W, CARD_H,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=tint, edgecolor=colour,
                                linewidth=2.2, zorder=3))
    # the small name of the card sits above it, clear of the border
    ax.text(left + CARD_W / 2, CARD_Y + CARD_H / 2 + 0.24, label,
            ha="center", va="center", fontsize=12.5, color=colour)
    ax.text(left + CARD_W / 2, CARD_Y, body, ha="center", va="center",
            fontsize=14.5, color=INK, linespacing=1.55, zorder=4)

# the three arrows between the cards, each in the colour of the work it is
ARROWS = (
    (2.72, 3.07, ORANGE),
    (5.42, 5.77, BLUE),
    (8.12, 8.47, ORANGE),
)
for x0, x1, colour in ARROWS:
    ax.add_patch(FancyArrowPatch((x0, CARD_Y), (x1, CARD_Y),
                                 arrowstyle="-|>", mutation_scale=17,
                                 linewidth=2.4, color=colour, zorder=5))

# under each gap: what that step is called, and who does it
# (centre of the gap, colour, name of the step, whose work it is)
STEPS = (
    (2.895, ORANGE, "translate", "this chapter"),
    (5.595, BLUE, "solve", "Chapters 20 and 21"),
    (8.295, ORANGE, "answer the question", "this chapter"),
)
for xc, colour, name, owner in STEPS:
    ax.text(xc, 1.52, name, ha="center", va="center", fontsize=13.5,
            color=colour)
    ax.plot([xc - 1.05, xc + 1.05], [1.08, 1.08], linewidth=2.6,
            color=colour, solid_capstyle="round")
    ax.text(xc, 0.78, owner, ha="center", va="center", fontsize=12,
            color=colour)

ax.text(0.42, 0.22, "the middle step is the one you already know how to "
        "do. the two on the outside are what this chapter adds",
        ha="left", va="center", fontsize=13.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_the_missing_half.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_01_the_missing_half.png")
