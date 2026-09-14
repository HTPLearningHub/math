"""Figure 4 - the conversion map between percent, fraction and decimal.

The three boxes hold the same amount, written in three ways.
Every arrow says exactly what you do to move from one box to the next,
so the reader can start in any box and reach the other two.
Run with:  python figures/fig_04_conversion_map.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"   # percent
BLUE = "#2E86DE"     # fraction
SLATE = "#546E7A"    # decimal
TEXT = "#37474F"     # the example inside a box

fig, ax = plt.subplots(figsize=(11.6, 8.0))
ax.axis("off")
ax.set_xlim(-0.5, 12.5)
ax.set_ylim(0.0, 9.7)

def box(cx, cy, title, example, colour, w=3.2, h=1.4):
    """One rounded box: the name of the form, then the example written in it."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.10,rounding_size=0.22",
                                facecolor="#FFFFFF", edgecolor=colour, linewidth=3.0))
    ax.text(cx, cy + 0.30, title, ha="center", va="center",
            fontsize=15, color=colour, fontweight="bold")
    ax.text(cx, cy - 0.38, example, ha="center", va="center",
            fontsize=16, color=TEXT)

# percent on top, fraction bottom left, decimal bottom right
box(6.0, 8.6, "PERCENT", r"$80\%$", ORANGE)
box(1.8, 1.5, "FRACTION", r"$\frac{80}{100} = \frac{4}{5}$", BLUE)
box(10.2, 1.5, "DECIMAL", r"$0.80$", SLATE)

def arrow(start, end, colour):
    """One straight arrow from start to end."""
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=24,
                                 linewidth=2.2, color=colour, shrinkA=2, shrinkB=2))

def label(x, y, text, colour):
    """A label that sits on its own arrow, on a white patch so it stays readable."""
    ax.text(x, y, text, ha="center", va="center", fontsize=12.5, color=colour,
            bbox=dict(facecolor="#FFFFFF", edgecolor="none", pad=2.5))

# percent -> fraction (outer, on the left) and fraction -> percent (inner)
arrow((4.7, 7.85), (1.6, 2.30), BLUE)
label(3.95, 6.5, "write the number\nover $100$, then simplify", BLUE)
arrow((2.6, 2.35), (5.3, 7.85), ORANGE)
label(3.41, 4.0, "make the\nbottom $100$", ORANGE)

# percent -> decimal (outer, on the right) and decimal -> percent (inner)
arrow((7.3, 7.85), (10.4, 2.30), SLATE)
label(8.05, 6.5, "divide by $100$:\nmove the point $2$ places left", SLATE)
arrow((9.4, 2.35), (6.7, 7.85), ORANGE)
label(8.59, 4.0, "multiply by $100$:\nmove the point\n$2$ places right", ORANGE)

# fraction <-> decimal, straight across the bottom
arrow((3.5, 1.85), (8.5, 1.85), SLATE)
ax.text(6.0, 2.45, "a bottom of $100$\nis two decimal places",
        ha="center", va="center", fontsize=12.5, color=SLATE)
arrow((8.5, 1.15), (3.5, 1.15), BLUE)
ax.text(6.0, 0.55, "two decimal places\nis a bottom of $100$",
        ha="center", va="center", fontsize=12.5, color=BLUE)

ax.set_title("Three ways to write the same amount", fontsize=18, fontweight="bold", pad=10)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_conversion_map.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
