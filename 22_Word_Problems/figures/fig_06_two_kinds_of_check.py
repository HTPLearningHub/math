"""Figure 6 - the arithmetic check and the sense check are two checks.

Chapter 20 taught one check: put the number back into the equation. A word
problem needs a second one, because the equation can be obeyed perfectly by
a number the story cannot hold - a negative age, half a child. The left
panel is the old check; the right panel is the one this chapter adds.

The ticks and crosses are drawn as line segments rather than typed as
characters, so the figure does not depend on the font having those glyphs.

Horizontal plan (x):
    0.55 - 5.15   the left panel
    5.65 - 10.25  the right panel

Vertical plan (y, top to bottom):
    6.10  heading
    5.40  the name of each panel
    5.05  the question each panel asks
    4.35  panel frames, from 1.05 up to 4.62
    4.10  first line inside a panel, then every 0.72 downwards
    0.55  closing note

Run with:  python figures/fig_06_two_kinds_of_check.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"
GREEN = "#1E8449"         # a thing that passes
RED = "#C0392B"           # a thing that fails
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_GREEN = "#E8F5EC"

W, H = 10.80, 6.55
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def tick(x, y):
    """A green tick, drawn from two short strokes."""
    ax.plot([x - 0.13, x - 0.03], [y + 0.01, y - 0.11], linewidth=2.8,
            color=GREEN, solid_capstyle="round", zorder=5)
    ax.plot([x - 0.03, x + 0.16], [y - 0.11, y + 0.15], linewidth=2.8,
            color=GREEN, solid_capstyle="round", zorder=5)


def cross(x, y):
    """A red cross, drawn from two crossing strokes."""
    ax.plot([x - 0.12, x + 0.12], [y - 0.12, y + 0.12], linewidth=2.8,
            color=RED, solid_capstyle="round", zorder=5)
    ax.plot([x - 0.12, x + 0.12], [y + 0.12, y - 0.12], linewidth=2.8,
            color=RED, solid_capstyle="round", zorder=5)


ax.text(0.55, 6.10, "a number can pass one check and fail the other",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# (left edge, border colour, fill, panel name, the question it asks,
#  the lines inside it as (passes?, text))
PANELS = (
    (0.55, BLUE, TINT_BLUE, "the arithmetic check",
     "does the equation agree?",
     ((True, r"$2(10) + 3(16) = 68$"),
      (True, r"$20 + 48 = 68$"),
      (True, "the two sides match"),
      (None, "this is Chapter 20's check,"),
      (None, "and it never changes"))),
    (5.65, GREEN, TINT_GREEN, "the sense check",
     "can the story hold this number?",
     ((True, "$10$ spots on a dog"),
      (False, "an age of $-4$ years"),
      (False, "$3.5$ children in a family"),
      (None, "this check is new, and only"),
      (None, "the story can answer it"))),
)
for left, colour, tint, name, question, lines in PANELS:
    ax.text(left + 2.30, 5.40, name, ha="center", va="center",
            fontsize=15, color=colour, fontweight="bold")
    ax.text(left + 2.30, 5.05, question, ha="center", va="center",
            fontsize=12.5, color=GREY)
    ax.add_patch(FancyBboxPatch((left, 1.05), 4.60, 3.57,
                                boxstyle="round,pad=0.05,rounding_size=0.16",
                                facecolor=tint, edgecolor=colour,
                                linewidth=2.2, zorder=2))
    ypos = 4.10
    for passes, text in lines:
        if passes is True:
            tick(left + 0.50, ypos)
            ax.text(left + 0.85, ypos, text, ha="left", va="center",
                    fontsize=14, color=INK, zorder=4)
        elif passes is False:
            cross(left + 0.50, ypos)
            ax.text(left + 0.85, ypos, text, ha="left", va="center",
                    fontsize=14, color=INK, zorder=4)
        else:
            # the two closing lines carry no mark: they are commentary
            ax.text(left + 0.50, ypos, text, ha="left", va="center",
                    fontsize=12.5, color=GREY, style="italic", zorder=4)
            ypos += 0.28      # the commentary lines sit closer together
        ypos -= 0.72

ax.text(0.55, 0.55, "do both. an answer that obeys the equation but not "
        "the story means the equation was written wrongly",
        ha="left", va="center", fontsize=13.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_06_two_kinds_of_check.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_06_two_kinds_of_check.png")
