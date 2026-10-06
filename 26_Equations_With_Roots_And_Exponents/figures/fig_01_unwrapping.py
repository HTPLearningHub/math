"""Figure 1 - the letter in sqrt(x + 9) = 5 is wrapped in two layers.

Upper row (blue, forward): what was done to x. Start at 16, add 9 to reach 25,
then take the square root to reach 5. The square root went on last, so it is
the outside layer.

Lower row (orange, backward): how to undo it. Start at 5, square to reach 25,
then subtract 9 to reach 16. The outside layer comes off first.

The two rows use the same three numbers in mirror order, so the reader can see
that undoing is the forward road walked backwards (Chapter 20, section 5).

Colour convention, carried on from Chapters 24 and 25:
    blue   - the forward direction (what was done to the letter)
    orange - the backward direction (undoing it)
    green  - the letter's value, the answer
    grey   - quiet labels

Horizontal plan (x): cards at 1.40, 6.20 and 11.00.
Vertical plan (y): heading 6.40; forward row 4.60; backward row 1.70.

Run with:  python figures/fig_01_unwrapping.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"                                   # forward steps
BLUE_T = "#E9F2FC"                                 # pale blue card fill
ORANGE = "#E67E22"                                 # backward steps
ORANGE_T = "#FDF0E3"                               # pale orange card fill
GREEN = "#1E8449"                                  # the answer
GREEN_T = "#E8F5EC"                                # pale green card fill
GREY = "#78909C"                                   # quiet labels
INK = "#212121"                                    # main text

W, H = 12.6, 7.0                                   # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")                                     # no axes on a diagram
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# the heading: the equation itself
ax.text(0.30, 6.45, r"$\sqrt{x + 9} = 5$:  two layers around the letter",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")


def card(xc, yc, text, edge, fill, w=1.50):
    """A rounded card of width w centred on (xc, yc) holding text."""
    h = 1.05                                       # every card has one height
    ax.add_patch(FancyBboxPatch(
        (xc - w / 2, yc - h / 2), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.15",
        facecolor=fill, edgecolor=edge, linewidth=2.0, zorder=1))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=24,
            color=INK, zorder=2)


def step(x0, x1, yc, colour, label, sub):
    """An arrow from x0 to x1 at height yc, a bold label above, a note below."""
    ax.annotate("", xy=(x1, yc), xytext=(x0, yc),
                arrowprops=dict(arrowstyle="-|>", color=colour, lw=2.4,
                                mutation_scale=24))
    ax.text((x0 + x1) / 2, yc + 0.45, label, ha="center", va="center",
            fontsize=15, color=colour, fontweight="bold")
    ax.text((x0 + x1) / 2, yc - 0.42, sub, ha="center", va="center",
            fontsize=12.5, color=GREY)


# ---------------------------------------------------------- the forward row
yf = 4.60
ax.text(0.30, yf + 1.10, "what was done to $x$  (inside first)",
        ha="left", va="center", fontsize=15, color=BLUE, fontweight="bold")
card(1.40, yf, r"$16$", GREEN, GREEN_T)                     # the letter's value
step(2.25, 5.35, yf, BLUE, r"add $9$", "layer 1: inside the root")
card(6.20, yf, r"$25$", BLUE, BLUE_T)
step(7.05, 10.15, yf, BLUE, "take the square root", "layer 2: the outside")
card(11.00, yf, r"$5$", BLUE, BLUE_T)

# ---------------------------------------------------------- the backward row
yb = 1.70
ax.text(0.30, yb + 1.10, "how to undo it  (outside first)",
        ha="left", va="center", fontsize=15, color=ORANGE, fontweight="bold")
card(11.00, yb, r"$5$", ORANGE, ORANGE_T)
step(10.15, 7.05, yb, ORANGE, "square it", r"$5 \times 5 = 25$")
card(6.20, yb, r"$25$", ORANGE, ORANGE_T)
step(5.35, 2.25, yb, ORANGE, r"subtract $9$", r"$25 - 9 = 16$")
card(1.40, yb, r"$16$", GREEN, GREEN_T)                     # the answer

# a quiet closing line under everything
ax.text(W / 2, 0.42,
        r"the $9$ is under the root, so it cannot be reached until the root is gone",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_unwrapping.png", dpi=170, bbox_inches="tight",
            facecolor="white")
print("wrote", out / "fig_01_unwrapping.png")
