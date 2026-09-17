"""Figure 1 - arithmetic answers one order; algebra answers every order.

Left panel: the cheeseburger bill worked out with arithmetic. Every new
number of burgers needs a whole new calculation, so the panel is a list that
never ends.

Right panel: the same shop with one algebraic rule, y = 3x. The rule is a
single box. Numbers go in on the left, prices come out on the right, and the
box itself never changes.

The point of the picture is the *shape* of the two panels: a growing list
against one fixed box. That is what "algebra says it once" means.

Run with:  python figures/fig_01_one_rule_instead_of_a_list.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"          # the variable, and any number going in
ORANGE = "#E67E22"        # fixed numbers - here the price 3
GREEN = "#1E8449"         # the answer coming out
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"
TINT_GREEN = "#E8F5EC"
TINT_GREY = "#ECEFF1"

W, H = 13.20, 6.30
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])          # the axes fill the whole figure
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def box(cx, cy, w, h, text, face, edge, fontsize=17, weight="normal",
        tcolour=INK):
    """One rounded box with its text centred inside it."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.055,rounding_size=0.13",
                                facecolor=face, edgecolor=edge,
                                linewidth=2.0, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize,
            color=tcolour, fontweight=weight, zorder=4)


def arrow(x1, y1, x2, y2, colour):
    """A thin arrow from one point to another."""
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2),
                                 arrowstyle="-|>", mutation_scale=17,
                                 color=colour, linewidth=1.9,
                                 shrinkA=2, shrinkB=2, zorder=2))


# ------------------------------------------------------------- panel headings
ax.text(3.30, H - 0.45, "arithmetic", ha="center", va="center", fontsize=21,
        color=GREY, fontweight="bold")
ax.text(3.30, H - 0.95, "one order, one answer", ha="center", va="center",
        fontsize=14, color=GREY)

ax.text(9.55, H - 0.45, "algebra", ha="center", va="center", fontsize=21,
        color=BLUE, fontweight="bold")
ax.text(9.55, H - 0.95, "one rule, every order", ha="center", va="center",
        fontsize=14, color=BLUE)

# the divider between the two panels
ax.plot([6.55, 6.55], [0.35, H - 1.35], color=GREY, linewidth=1.3,
        linestyle=(0, (4, 4)), zorder=1)

# ---------------------------------------------------------------- left panel
LINES = [r"$3 \times 1 = 3$",
         r"$3 \times 5 = 15$",
         r"$3 \times 10 = 30$",
         r"$3 \times 100 = 300$"]
TOP = H - 1.80
STEP = 0.82
for i, line in enumerate(LINES):
    box(3.30, TOP - i * STEP, 3.55, 0.60, line, TINT_GREY, GREY, fontsize=18)
ax.text(3.30, TOP - 4 * STEP + 0.02, r"$\vdots$", ha="center", va="center",
        fontsize=22, color=GREY)
ax.text(3.30, TOP - 4 * STEP - 0.62, "a new calculation for every order",
        ha="center", va="center", fontsize=14.5, color=GREY, style="italic")

# --------------------------------------------------------------- right panel
X_IN, X_RULE, X_OUT = 7.45, 9.55, 11.90
Y_RULE = TOP - 1.30
INPUTS = [1, 5, 10]
OUTPUTS = [3, 15, 30]
Y_ROWS = [Y_RULE + 1.30, Y_RULE, Y_RULE - 1.30]

# the rule itself, in the middle
box(X_RULE, Y_RULE, 2.00, 0.95, r"$y = 3x$", TINT_ORANGE, ORANGE,
    fontsize=27, weight="bold")
ax.text(X_RULE, Y_RULE + 0.80, "the rule", ha="center", va="center",
        fontsize=13.5, color=ORANGE)

for y, vin, vout in zip(Y_ROWS, INPUTS, OUTPUTS):
    box(X_IN, y, 0.90, 0.62, f"${vin}$", TINT_BLUE, BLUE, fontsize=18)
    box(X_OUT, y, 1.05, 0.62, f"${vout}$", TINT_GREEN, GREEN, fontsize=18)
    arrow(X_IN + 0.52, y, X_RULE - 1.08, Y_RULE + (y - Y_RULE) * 0.20, BLUE)
    arrow(X_RULE + 1.08, Y_RULE + (y - Y_RULE) * 0.20, X_OUT - 0.60, y, GREEN)

ax.text(X_IN, Y_ROWS[0] + 0.62, "burgers", ha="center", va="center",
        fontsize=13.5, color=BLUE)
ax.text(X_OUT, Y_ROWS[0] + 0.62, "dollars", ha="center", va="center",
        fontsize=13.5, color=GREEN)
ax.text(9.55, Y_ROWS[2] - 0.78, "the box never changes",
        ha="center", va="center", fontsize=14.5, color=BLUE, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_one_rule_instead_of_a_list.png", dpi=170,
            facecolor="white")
print("saved", out / "fig_01_one_rule_instead_of_a_list.png")
