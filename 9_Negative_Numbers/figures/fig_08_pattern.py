"""Figure 8 - the pattern that decides what negative times negative must be.

Seven multiplications, all by -2, with the first number dropping by one each
row. The answers climb by two each row: -6, -4, -2, 0, 2, 4, 6. The top four
rows are ones the reader can already work out. The bottom three are the ones
in question, and the pattern leaves them no choice: they have to be positive.

The dashed line separates what is already known from what the pattern decides.
Run with:  python figures/fig_08_pattern.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # positive answers
ORANGE = "#E67E22"      # negative answers
GREY = "#78909C"        # zero, and the quiet labels
INK = "#212121"

W, H = 11.6, 6.35
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ROWS = [3, 2, 1, 0, -1, -2, -3]            # the first factor, one less each row
TOP, STEP = 5.05, 0.62                     # the first row, and the gap between rows
X_MULT, X_EQ, X_ANS = 4.60, 5.55, 6.40     # the three columns of the table


def y_of(k):
    """The height of row number k, counting from zero at the top."""
    return TOP - k * STEP


# a pale panel behind the three rows the pattern has to decide
ax.add_patch(FancyBboxPatch((1.15, y_of(6) - 0.32), 6.35, 3 * STEP + 0.04,
                            boxstyle="round,pad=0.04,rounding_size=0.12",
                            facecolor="#EAF2FC", edgecolor="none"))

for k, a in enumerate(ROWS):
    y = y_of(k)
    answer = a * -2
    colour = GREY if answer == 0 else (BLUE if answer > 0 else ORANGE)
    first = rf"$({a})$" if a < 0 else rf"${a}$"       # brackets only when negative
    ax.text(X_MULT, y, rf"{first} $\times$ $(-2)$", ha="right", va="center",
            fontsize=18, color=INK)
    ax.text(X_EQ, y, r"$=$", ha="center", va="center", fontsize=18, color=INK)
    ax.text(X_ANS, y, rf"${answer}$", ha="left", va="center",
            fontsize=18, color=colour, fontweight="bold")

    # the step from this answer to the next one, drawn between the two rows
    if k < len(ROWS) - 1:
        ax.annotate("", xy=(7.75, y - STEP + 0.20), xytext=(7.75, y - 0.20),
                    arrowprops=dict(arrowstyle="-|>", color=GREY, linewidth=1.6,
                                    mutation_scale=14))
        ax.text(7.95, y - STEP / 2, r"$+2$", ha="left", va="center",
                fontsize=13, color=GREY)

# the line between what is known and what the pattern decides
y_split = (y_of(3) + y_of(4)) / 2
ax.plot([1.05, 7.45], [y_split] * 2, color=INK, linewidth=1.4,
        linestyle=(0, (6, 4)))
ax.text(8.95, y_of(1), "you already\nknow these rows", ha="left", va="center",
        fontsize=13, color=INK, linespacing=1.5)
ax.text(8.95, y_of(5), "so these rows\nmust follow", ha="left", va="center",
        fontsize=13, color=BLUE, fontweight="bold", linespacing=1.5)

# the two headings and the two messages
ax.text(3.30, 5.62, "one less every row", ha="center", va="center",
        fontsize=13.5, color=GREY, fontweight="bold")
ax.text(6.70, 5.62, "two more every row", ha="center", va="center",
        fontsize=13.5, color=GREY, fontweight="bold")
ax.text(W / 2, H - 0.28,
        "Keep the pattern going and the answer has to turn positive",
        ha="center", va="center", fontsize=16.5, color=INK, fontweight="bold")
ax.text(W / 2, 0.34,
        r"This is why $(-1) \times (-2) = 2$: nothing else keeps the steps equal.",
        ha="center", va="center", fontsize=15, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_08_pattern.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
