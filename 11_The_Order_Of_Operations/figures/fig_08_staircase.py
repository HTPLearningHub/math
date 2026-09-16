"""Figure 8 - one long expression, one operation per line.

The habit this figure is selling is the one that stops nearly every error:
after each single operation, write the whole expression out again. The line
gets shorter every time, and the reader can see how much is left.

Each row carries a coloured tag naming the level the step came from, using
the same four colours as Figure 2. The tags do not arrive in order, and
that is the lesson: Level 2 and Level 4 steps happen first here because
they are inside a bracket, and a bracket outranks everything outside it.
Run with:  python figures/fig_08_staircase.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

ORANGE = "#E67E22"
PURPLE = "#8E44AD"
BLUE = "#2E86DE"
SLATE = "#546E7A"
GREEN = "#1E8449"
GREY = "#78909C"
INK = "#212121"

W, H = 12.4, 7.35
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

EXPR_X = 1.05                 # every expression starts here, left aligned
TAG_X = 8.35                  # left edge of the level tag
TAG_W = 1.62
NOTE_X = 10.15                # what was actually calculated
TOP = H - 1.42
STEP = 0.74                   # one row

# expression, tag colour, tag text, what was done on this line
LINES = [
    (r"$100 \div 5 \times 2 - [\,4 + (8 - 3^{2})\,]$", None, "start", ""),
    (r"$100 \div 5 \times 2 - [\,4 + (8 - 9)\,]$", PURPLE, "Level 2",
     r"$3^{2} = 9$"),
    (r"$100 \div 5 \times 2 - [\,4 + (-1)\,]$", SLATE, "Level 4",
     r"$8 - 9 = -1$"),
    (r"$100 \div 5 \times 2 - 3$", SLATE, "Level 4", r"$4 + (-1) = 3$"),
    (r"$20 \times 2 - 3$", BLUE, "Level 3", r"$100 \div 5 = 20$"),
    (r"$40 - 3$", BLUE, "Level 3", r"$20 \times 2 = 40$"),
    (r"$37$", SLATE, "Level 4", r"$40 - 3 = 37$"),
]

for i, (expr, colour, tag, note) in enumerate(LINES):
    y = TOP - i * STEP
    # the last line is the answer, so it gets the green treatment
    last = (i == len(LINES) - 1)
    ax.text(EXPR_X, y, expr, ha="left", va="center",
            fontsize=22, color=GREEN if last else INK,
            fontweight="bold" if last else "normal")
    if colour is None:
        # the first line has no step behind it, only a label
        ax.text(TAG_X + TAG_W / 2, y, tag, ha="center", va="center",
                fontsize=13, color=GREY)
        continue
    ax.add_patch(FancyBboxPatch((TAG_X, y - 0.20), TAG_W, 0.40,
                                boxstyle="round,pad=0.03,rounding_size=0.10",
                                facecolor=colour, edgecolor="none"))
    ax.text(TAG_X + TAG_W / 2, y, tag, ha="center", va="center",
            fontsize=13, color="white", fontweight="bold")
    ax.text(NOTE_X, y, note, ha="left", va="center",
            fontsize=16, color=colour)

# the two rows that come from inside the bracket are marked once, on the left
BRACKET_TOP = TOP - 0.74 + 0.30
BRACKET_BOT = TOP - 3 * 0.74 - 0.30
ax.plot([0.62, 0.62], [BRACKET_BOT, BRACKET_TOP], color=ORANGE, linewidth=2.6)
ax.text(0.40, (BRACKET_TOP + BRACKET_BOT) / 2, "inside the bracket",
        ha="center", va="center", fontsize=12.5, color=ORANGE,
        fontweight="bold", rotation=90)

ax.text(W / 2, H - 0.45, "Rewrite the whole line after every single step",
        ha="center", va="center", fontsize=19.5, color=INK, fontweight="bold")
ax.plot([0.55, W - 0.55], [0.98, 0.98], color=GREY,
        linewidth=1.0, linestyle=(0, (4, 3)))
ax.text(W / 2, 0.55,
        "Six steps, and the levels do not arrive in order - "
        "because a bracket outranks everything that is not inside it.",
        ha="center", va="center", fontsize=15, color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_08_staircase.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
