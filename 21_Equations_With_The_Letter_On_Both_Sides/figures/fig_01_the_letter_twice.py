"""Figure 1 - why Chapter 20's first question stalls.

Chapter 20 starts every solution with one question: what has been done to
the letter? When the letter sits on both sides, that question has two
answers at the same time, and neither of them is "the last one".

The picture also does a second job: it names the four pieces of the
equation, which section 1.2 then defines.

Horizontal plan (x):
    2.30  4x        (variable term, blue highlight)
    4.00  + 3       (constant term)
    5.60  =
    7.05  x         (variable term, blue highlight)
    8.70  - 6       (constant term)

Vertical plan (y, top to bottom):
    4.45  heading
    3.45  the name of each piece
    2.75  the equation, with the two blue highlights behind it
    1.05  the question, in an orange pill, with two arrows going up
    0.30  closing note

Run with:  python figures/fig_01_the_letter_twice.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # the letter
ORANGE = "#E67E22"        # the move being attempted
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"

W, H = 10.80, 4.90
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.60, 4.45, "the same letter, on both sides of the equals sign",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# the five pieces of the equation, each placed by hand so that a highlight
# box can be put exactly behind the two that carry the letter
X_4X, X_P3, X_EQ, X_X, X_M6 = 2.30, 4.00, 5.60, 7.05, 8.70
EQ_Y = 2.75

# the two blue highlights go down first, so the text sits on top of them
ax.add_patch(FancyBboxPatch((X_4X - 0.50, EQ_Y - 0.42), 1.00, 0.84,
                            boxstyle="round,pad=0.04,rounding_size=0.14",
                            facecolor=TINT_BLUE, edgecolor=BLUE,
                            linewidth=2.2, zorder=2))
ax.add_patch(FancyBboxPatch((X_X - 0.35, EQ_Y - 0.42), 0.70, 0.84,
                            boxstyle="round,pad=0.04,rounding_size=0.14",
                            facecolor=TINT_BLUE, edgecolor=BLUE,
                            linewidth=2.2, zorder=2))

for xpos, piece in ((X_4X, r"$4x$"), (X_P3, r"$+\,3$"), (X_EQ, r"$=$"),
                    (X_X, r"$x$"), (X_M6, r"$-\,6$")):
    ax.text(xpos, EQ_Y, piece, ha="center", va="center",
            fontsize=30, color=INK, zorder=4)

# the name of each piece, above it
for xpos, name, colour in ((X_4X, "variable term", BLUE),
                           (X_P3, "constant term", GREY),
                           (X_X, "variable term", BLUE),
                           (X_M6, "constant term", GREY)):
    ax.text(xpos, 3.45, name, ha="center", va="center",
            fontsize=12, color=colour)

# the question that no longer has one answer
ax.add_patch(FancyBboxPatch((3.30, 0.75), 4.60, 0.60,
                            boxstyle="round,pad=0.04,rounding_size=0.28",
                            facecolor=TINT_ORANGE, edgecolor=ORANGE,
                            linewidth=2.0, zorder=3))
ax.text(5.60, 1.05, "what has been done to the letter?", ha="center",
        va="center", fontsize=15, color=ORANGE, zorder=4)

# one arrow to each variable term - the point of the figure is that there
# are two of them
for start_x, end_x in ((4.20, X_4X), (6.90, X_X)):
    ax.add_patch(FancyArrowPatch((start_x, 1.40), (end_x, 2.26),
                                 arrowstyle="-|>", mutation_scale=18,
                                 linewidth=2.2, color=ORANGE, zorder=5))

ax.text(0.60, 0.30, "two answers at once - so there is no single last step "
        "to undo, and nothing to start from", ha="left", va="center",
        fontsize=15, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_the_letter_twice.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_01_the_letter_twice.png")
