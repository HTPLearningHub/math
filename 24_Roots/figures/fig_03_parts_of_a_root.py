"""Figure 3 - the three parts of a root symbol, and their names.

Chapter 10's fig_02 did this job for a power (base, exponent, power).
This is the matching picture for a root, and it uses the same colours on
purpose: purple for the small number in the corner, blue for the number
being worked on.

The radical sign is drawn stroke by stroke rather than typeset, because
mathtext cannot colour one part of a string - the lesson recorded in the
Chapter 10 notes. Drawing it also lets the arrows point at exactly the
right piece.

A first version drew the sign far too tall, so the overbar floated a long
way above the radicand and the whole symbol stopped looking like one
thing. The bar now sits just over the top of the digits.

Colour convention:
    orange - the radical sign itself, the operation
    purple - the index, the small number that says which root
    blue   - the radicand, the number under the sign

Horizontal plan (x): the sign's strokes run 4.80 -> 5.10 -> 5.45, and the
    bar from 5.45 to 7.30. The index sits at 5.00, the radicand is centred
    at 6.40, and "= 4" starts at 7.60. The left labels are right-aligned
    at 4.10; the right label is left-aligned at 7.95.

Vertical plan (y, top to bottom):
    6.55  figure heading
    5.75  the "index" label
    5.35  the top bar of the radical sign
    4.55  the radicand
    4.05  the bottom point of the sign
    3.20  the "radical sign" label (left) and "radicand" label (right)
    2.40  the dashed rule
    1.55  the missing-index statement
    0.45  the closing note

Run with:  python figures/fig_03_parts_of_a_root.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

BLUE = "#2E86DE"        # the radicand
PURPLE = "#8E44AD"      # the index, as in Chapter 10
ORANGE = "#E67E22"      # the radical sign
GREY = "#78909C"
INK = "#212121"

W, H = 13.00, 6.95
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.40, 6.55, "the three parts of a root, and what each one is called",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# ------------------------------------------------- the radical sign, by hand
# A radical sign is three strokes: a short dip, a long rise, then a bar
# that runs over everything being rooted.
ax.plot([4.80, 5.10, 5.45, 7.30],
        [5.00, 4.05, 5.35, 5.35],
        linewidth=4.0, color=ORANGE, solid_capstyle="round",
        solid_joinstyle="round", zorder=2)

# the index, tucked into the notch above the short stroke
ax.text(4.98, 5.30, "$3$", ha="center", va="center", fontsize=21,
        color=PURPLE, fontweight="bold", zorder=3)

# the radicand, under the bar
ax.text(6.40, 4.55, "$64$", ha="center", va="center", fontsize=40,
        color=BLUE, zorder=3)

# the answer, to the right of the whole thing
ax.text(7.60, 4.55, "$= 4$", ha="left", va="center", fontsize=32, color=INK)

# ------------------------------------------------------------- the labels
ax.annotate("", xy=(4.92, 5.52), xytext=(4.20, 5.95),
            arrowprops=dict(arrowstyle="-|>", linewidth=1.8, color=PURPLE))
ax.text(4.12, 6.05, "the index", ha="right", va="center", fontsize=17,
        color=PURPLE, fontweight="bold")
ax.text(4.12, 5.62, "which root this is:\n$3$ means the cube root",
        ha="right", va="center", fontsize=13.5, color=GREY,
        linespacing=1.45)

ax.annotate("", xy=(5.02, 4.35), xytext=(4.25, 3.60),
            arrowprops=dict(arrowstyle="-|>", linewidth=1.8, color=ORANGE))
ax.text(4.15, 3.50, "the radical sign", ha="right", va="center",
        fontsize=17, color=ORANGE, fontweight="bold")
ax.text(4.15, 3.10, "it says: take a root",
        ha="right", va="center", fontsize=13.5, color=GREY)

ax.annotate("", xy=(6.75, 4.18), xytext=(7.55, 3.45),
            arrowprops=dict(arrowstyle="-|>", linewidth=1.8, color=BLUE))
ax.text(7.65, 3.35, "the radicand", ha="left", va="center", fontsize=17,
        color=BLUE, fontweight="bold")
ax.text(7.65, 2.95, "the number you take\nthe root of",
        ha="left", va="center", fontsize=13.5, color=GREY, linespacing=1.45)

# ------------------------------------------- the index that is not written
ax.plot([0.60, 12.40], [2.40, 2.40], linewidth=1.4, color=GREY,
        linestyle=(0, (6, 5)))

ax.text(6.50, 1.55,
        r"$\sqrt{9}$   means   $\sqrt[2]{9}$   and both are   $3$",
        ha="center", va="center", fontsize=25, color=INK)

ax.text(6.50, 0.48,
        "when no small number is written, the index is $2$ - a square root "
        "is the one root that hides its index",
        ha="center", va="center", fontsize=13.5, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_parts_of_a_root.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_03_parts_of_a_root.png")
