"""Figure 1 - two brackets multiplied give four pieces.

Left: the rectangle 13 by 12 = (10 + 3) by (10 + 2), drawn to scale and
cut at 10 in both directions. It falls into four pieces 100, 20, 30, 6,
and 100 + 20 + 30 + 6 = 156 = 13 x 12 (Chapter 6, section 3, cut both ways).
Right: the same layout as a grid for (x + 3)(x - 2). The cells hold
x^2, -2x, 3x, -6. With a negative length it is no longer a real picture
of area, only a way to keep track of the four products.

Colour convention for this chapter (one colour per FOIL product):
    blue   - First
    orange - Outer
    teal   - Inner
    purple - Last
    green  - the final answer
    grey   - labels

Run with:  python figures/fig_01_four_pieces.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
GREEN = "#1E8449"
# FOIL product -> (edge colour, light fill)
F = ("#2E86DE", "#E9F2FC")
O = ("#E67E22", "#FDF0E3")
I = ("#138D75", "#E6F5F1")
L = ("#8E44AD", "#F3EAF8")

fig, (axL, axR) = plt.subplots(1, 2, figsize=(16, 8))


def piece(ax, x0, y0, w, h, col, text, size=20):
    """One coloured rectangle with its product written in the middle."""
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=col[1],
                           edgecolor=col[0], linewidth=2.5))
    ax.text(x0 + w / 2, y0 + h / 2, text, ha="center", va="center",
            fontsize=size, color=col[0], fontweight="bold")


# --- left panel: the real rectangle 13 by 12, drawn to scale ----------------
# columns: 10 then 2 (the second bracket); rows: 10 on top, 3 below (first)
piece(axL, 0, 3, 10, 10, F, r"$10 \times 10 = 100$")       # First
piece(axL, 10, 3, 2, 10, O, r"$20$")                        # Outer, 10 x 2
piece(axL, 0, 0, 10, 3, I, r"$3 \times 10 = 30$")           # Inner
piece(axL, 10, 0, 2, 3, L, r"$6$", 17)                      # Last, 3 x 2
# the second bracket across the top, the first bracket down the left side
axL.text(5, 13.5, r"$10$", ha="center", fontsize=20, color=INK)
axL.text(11, 13.5, r"$+\,2$", ha="center", fontsize=20, color=INK)
axL.text(-0.5, 8, r"$10$", ha="right", va="center", fontsize=20, color=INK)
axL.text(-0.5, 1.5, r"$+\,3$", ha="right", va="center", fontsize=20,
         color=INK)
axL.text(6, 15.2, r"$(10 + 3) \times (10 + 2) = 13 \times 12$",
         ha="center", fontsize=20, color=INK)
axL.text(6, -1.6, r"$100 + 20 + 30 + 6 = 156$", ha="center", fontsize=20,
         color=GREEN, fontweight="bold")
axL.text(6, -3.0, r"and $13 \times 12 = 156$ too", ha="center", fontsize=15,
         color=GREY)
axL.set_xlim(-2.8, 13.5)
axL.set_ylim(-3.8, 16.4)
axL.set_aspect("equal")                            # squares stay square
axL.axis("off")

# --- right panel: the same grid for (x + 3)(x - 2) --------------------------
S = 5.0                                            # side of one grid cell
cells = [  # (column, row, colour, text, name); row 1 is the top row
    (0, 1, F, r"$x \cdot x = x^{2}$", "First"),
    (1, 1, O, r"$x \cdot (-2) = -2x$", "Outer"),
    (0, 0, I, r"$3 \cdot x = 3x$", "Inner"),
    (1, 0, L, r"$3 \cdot (-2) = -6$", "Last"),
]
for c, r, col, text, name in cells:
    piece(axR, c * S, r * S, S, S, col, text, 17)
    axR.text(c * S + S / 2, r * S + 0.7, name, ha="center", fontsize=14,
             color=col[0])                          # the FOIL name, small
axR.text(S / 2, 2 * S + 0.5, r"$x$", ha="center", fontsize=22, color=INK)
axR.text(1.5 * S, 2 * S + 0.5, r"$-\,2$", ha="center", fontsize=22,
         color=INK)
axR.text(-0.5, 1.5 * S, r"$x$", ha="right", va="center", fontsize=22,
         color=INK)
axR.text(-0.5, 0.5 * S, r"$+\,3$", ha="right", va="center", fontsize=22,
         color=INK)
axR.text(S, 2 * S + 2.2, r"$(x + 3)(x - 2)$", ha="center", fontsize=20,
         color=INK)
axR.text(S, -1.6, r"$x^{2} - 2x + 3x - 6 = x^{2} + x - 6$",
         ha="center", fontsize=20, color=GREEN, fontweight="bold")
axR.text(S, -3.0, "the orange and teal cells are like terms",
         ha="center", fontsize=15, color=GREY)
axR.set_xlim(-2.8, 2 * S + 1.5)
axR.set_ylim(-3.8, 2 * S + 3.2)
axR.set_aspect("equal")
axR.axis("off")

fig.tight_layout(w_pad=4)
out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_four_pieces.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_01_four_pieces.png")
