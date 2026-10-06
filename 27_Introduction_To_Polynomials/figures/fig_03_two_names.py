"""Figure 3 - a polynomial has two names, and they answer different questions.

A grid. The rows are the degree (0 to 3: constant, linear, quadratic, cubic).
The columns are the number of terms (1, 2, 3: monomial, binomial, trinomial).
Each cell holds one example and its two-part name. Three cells are grey and
say "not possible": a polynomial of degree 0 has only one kind of term (a
number), and one of degree 1 has only two kinds (x and a number), once like
terms are collected (Chapter 19, section 4).

Colour convention:
    blue   - the number-of-terms names (columns)
    purple - the degree names (rows)
    green  - a cell that exists
    grey   - a cell that cannot exist

Run with:  python figures/fig_03_two_names.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

BLUE = "#2E86DE"
PURPLE = "#8E44AD"
GREEN = "#1E8449"
GREEN_T = "#E8F5EC"
GREY = "#78909C"
GREY_T = "#F2F4F5"
INK = "#212121"

CW, CH = 3.3, 1.25                                 # cell width and height in inches
X0, Y0 = 2.6, 0.3                                  # bottom-left corner of the grid
W, H = X0 + 3 * CW + 0.3, Y0 + 4 * CH + 1.5        # figure size
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

cols = [("monomial", "1 term"), ("binomial", "2 terms"), ("trinomial", "3 terms")]
rows = [("constant", "degree 0"), ("linear", "degree 1"),
        ("quadratic", "degree 2"), ("cubic", "degree 3")]

# cells[row][col] = (example, full name) or None when impossible
cells = [
    [(r"$7$", "constant monomial"), None, None],
    [(r"$5x$", "linear monomial"), (r"$3x - 2$", "linear binomial"), None],
    [(r"$4x^{2}$", "quadratic monomial"), (r"$x^{2} - 9$", "quadratic binomial"),
     (r"$x^{2} + 4x + 3$", "quadratic trinomial")],
    [(r"$-2x^{3}$", "cubic monomial"), (r"$x^{3} + 2x$", "cubic binomial"),
     (r"$2x^{3} - x + 5$", "cubic trinomial")],
]

top = Y0 + 4 * CH                                  # y of the grid's top edge
for c, (name, count) in enumerate(cols):           # column headings
    xc = X0 + (c + 0.5) * CW
    ax.text(xc, top + 0.80, name, ha="center", va="center", fontsize=17,
            color=BLUE, fontweight="bold")
    ax.text(xc, top + 0.35, count, ha="center", va="center", fontsize=13,
            color=BLUE)
ax.text(X0 + 1.5 * CW, top + 1.28, "how many terms?", ha="center",
        va="center", fontsize=13, color=GREY)

for r, (name, deg) in enumerate(rows):             # row headings, degree 0 on top
    yc = top - (r + 0.5) * CH
    ax.text(X0 - 0.20, yc + 0.20, name, ha="right", va="center",
            fontsize=17, color=PURPLE, fontweight="bold")
    ax.text(X0 - 0.20, yc - 0.25, deg, ha="right", va="center",
            fontsize=13, color=PURPLE)
ax.text(0.15, top + 0.35, "what is the\ndegree?", ha="left", va="center",
        fontsize=13, color=GREY)

for r in range(4):                                 # the cells themselves
    for c in range(3):
        x = X0 + c * CW
        y = top - (r + 1) * CH
        item = cells[r][c]
        ok = item is not None
        ax.add_patch(Rectangle((x, y), CW, CH,
                               facecolor=GREEN_T if ok else GREY_T,
                               edgecolor="white", linewidth=4))
        if ok:
            ex, full = item
            ax.text(x + CW / 2, y + CH * 0.62, ex, ha="center", va="center",
                    fontsize=21, color=INK)
            ax.text(x + CW / 2, y + CH * 0.22, full, ha="center",
                    va="center", fontsize=12, color=GREEN)
        else:
            ax.text(x + CW / 2, y + CH / 2, "not possible", ha="center",
                    va="center", fontsize=13, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_two_names.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_03_two_names.png")
