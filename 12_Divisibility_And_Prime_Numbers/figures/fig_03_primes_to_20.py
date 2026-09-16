"""Figure 3 - every number from 1 to 20, sorted into the three groups.

The definitions of *prime* and *composite* are about a count: exactly two
factors, or more than two. So the picture prints the count next to every
number, and lets the colour follow from it. The number 1 gets its own
colour, because it is the one number that lands in neither group, and the
reader has to see that it is not being hidden.

Layout: four rows of five cells. Each cell holds the number, its complete
list of factors, and how many there are. A legend sits above the grid; its
three entries are spaced by measuring each label with the renderer, because
guessing a character width put the swatches on top of the words.
Run with:  python figures/fig_03_primes_to_20.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

GREEN = "#1E8449"            # prime
BLUE = "#2E86DE"             # composite
GREY = "#78909C"             # neither, and quiet labels
INK = "#212121"

TINT = {GREEN: "#E8F5EC", BLUE: "#E9F2FC", GREY: "#ECEFF1"}


def factors(n):
    """Every whole number from 1 to n that divides n exactly."""
    return [d for d in range(1, n + 1) if n % d == 0]


W, H = 12.4, 7.55
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)
renderer = fig.canvas.get_renderer()


def width_of(text, **kw):
    """Width of a piece of text in inches. Drawn, measured, then removed."""
    t = ax.text(0, -50, text, **kw)                       # off-canvas
    w = t.get_window_extent(renderer).width / fig.dpi
    t.remove()
    return w


COLS, ROWS = 5, 4
CW, CH = 2.34, 1.34                        # width and height of one cell
GAP_X, GAP_Y = 0.10, 0.13                  # space between cells
GRID_W = COLS * CW + (COLS - 1) * GAP_X
LEFT = (W - GRID_W) / 2
TOP = H - 1.62                             # top edge of the first row

for n in range(1, 21):
    i = n - 1
    r, c = divmod(i, COLS)
    x = LEFT + c * (CW + GAP_X)
    y = TOP - (r + 1) * CH - r * GAP_Y

    f = factors(n)
    if n == 1:
        colour, label = GREY, "neither"
    elif len(f) == 2:
        colour, label = GREEN, "prime"
    else:
        colour, label = BLUE, "composite"

    ax.add_patch(FancyBboxPatch((x, y), CW, CH,
                                boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor=TINT[colour], edgecolor=colour,
                                linewidth=1.7))
    # the number itself, on the left of the cell
    ax.text(x + 0.42, y + CH / 2 + 0.04, str(n), ha="center", va="center",
            fontsize=24, color=colour, fontweight="bold")
    # the word, then the list of factors, then how many there are
    ax.text(x + 0.78, y + CH - 0.32, label, ha="left", va="center",
            fontsize=12.5, color=colour, fontweight="bold")
    ax.text(x + 0.78, y + CH - 0.71, "{" + ", ".join(str(d) for d in f) + "}",
            ha="left", va="center", fontsize=10.5, color=INK)
    word = "factor" if len(f) == 1 else "factors"
    ax.text(x + 0.78, y + CH - 1.06, f"{len(f)} {word}", ha="left", va="center",
            fontsize=11.5, color=GREY)

# ------------------------------------------------------------------ the title
ax.text(W / 2, H - 0.40, "Every number from 1 to 20, and how many factors it has",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")

# ----------------------------------------------------------------- the legend
KEYS = [(GREY, "1 factor - neither prime nor composite"),
        (GREEN, "exactly 2 factors - prime"),
        (BLUE, "3 or more factors - composite")]
SW = 0.30                                  # side of a legend swatch
GAP_KEY = 0.55                             # space between two legend entries
key_y = H - 1.16
key_x = LEFT + 0.06
for colour, text in KEYS:
    ax.add_patch(FancyBboxPatch((key_x, key_y), SW, SW,
                                boxstyle="round,pad=0.01,rounding_size=0.06",
                                facecolor=TINT[colour], edgecolor=colour,
                                linewidth=1.7))
    ax.text(key_x + SW + 0.14, key_y + SW / 2, text, ha="left", va="center",
            fontsize=12.5, color=colour)
    key_x += SW + 0.14 + width_of(text, fontsize=12.5) + GAP_KEY

out = Path(__file__).resolve().parent.parent / "assets" / "fig_03_primes_to_20.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
