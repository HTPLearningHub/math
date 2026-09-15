"""Figure 4 - the finished map between the three forms.

Chapter 3 drew the same three boxes, but the two arrows between
FRACTION and DECIMAL only worked when the bottom number was 100.
Here all six arrows work for any fraction, so the map is complete.
The example carried round the map is 3/5 = 0.6 = 60%.
Run with:  python figures/fig_04_full_conversion_map.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

ORANGE = "#E67E22"   # percent - the same colour as in chapter 3
BLUE = "#2E86DE"     # fraction
SLATE = "#546E7A"    # decimal
TEXT = "#37474F"

fig, ax = plt.subplots(figsize=(12.0, 8.4))
ax.axis("off")
ax.set_xlim(-0.5, 12.5)
ax.set_ylim(-0.3, 9.9)


def box(cx, cy, title, example, colour, w=3.4, h=1.4):
    """One rounded box: the name of the form, then the example written in it."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.10,rounding_size=0.22",
                                facecolor="#FFFFFF", edgecolor=colour, linewidth=3.0))
    ax.text(cx, cy + 0.30, title, ha="center", va="center",
            fontsize=15, color=colour, fontweight="bold")
    ax.text(cx, cy - 0.40, example, ha="center", va="center",
            fontsize=16, color=TEXT)


def arrow(start, end, colour):
    """One straight arrow from one box to another."""
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=24,
                                 linewidth=2.4, color=colour,
                                 shrinkA=2, shrinkB=2))


def label(x, y, text, colour):
    """A label sitting on its own arrow, on a white patch so it stays readable."""
    ax.text(x, y, text, ha="center", va="center", fontsize=12.5, color=colour,
            bbox=dict(boxstyle="round,pad=0.30", facecolor="#FFFFFF",
                      edgecolor="none"))


# the same layout as chapter 3: percent on top, fraction left, decimal right
box(6.0, 8.6, "PERCENT", r"$60\%$", ORANGE)
box(1.9, 1.6, "FRACTION", r"$\frac{3}{5}$", BLUE)
box(10.1, 1.6, "DECIMAL", r"$0.6$", SLATE)

# percent <-> fraction (chapter 3, section 4)
arrow((4.8, 7.85), (1.7, 2.40), BLUE)
label(4.05, 6.45, "write it over $100$,\nthen simplify", BLUE)
arrow((2.7, 2.45), (5.4, 7.85), ORANGE)
label(3.50, 4.10, "make the\nbottom $100$", ORANGE)

# percent <-> decimal (chapter 3, section 4)
arrow((7.2, 7.85), (10.3, 2.40), SLATE)
label(7.95, 6.45, "move the point\n$2$ places left", SLATE)
arrow((9.3, 2.45), (6.6, 7.85), ORANGE)
label(8.50, 4.10, "move the point\n$2$ places right", ORANGE)

# fraction <-> decimal: the two arrows this chapter adds
arrow((3.7, 1.95), (8.3, 1.95), SLATE)
ax.text(6.0, 2.62, "divide the top\nby the bottom", ha="center", va="center",
        fontsize=12.5, color=SLATE, fontweight="bold")
arrow((8.3, 1.15), (3.7, 1.15), BLUE)
ax.text(6.0, 0.48, "put the digits over $10$, $100$ or $1000$,\nthen simplify",
        ha="center", va="center", fontsize=12.5, color=BLUE, fontweight="bold")

# say out loud which two arrows are new
ax.text(6.0, 3.35, "both arrows below are new in this chapter", ha="center", va="center",
        fontsize=11.5, color="#C0392B", style="italic")

ax.set_title("Every route between the three forms",
             fontsize=18, fontweight="bold", pad=10)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_full_conversion_map.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
