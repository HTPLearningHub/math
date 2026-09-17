"""Figure 4 - the GCF is the part the two numbers are both built from.

Chapter 13 drew the LCM as "lay out one number's primes, then add whatever
the other still needs". This is the same picture read the other way: keep
only the bricks that appear in *both* piles, and throw the rest away.

The bricks that both numbers own are drawn first in each row, so the two
rows start with the same green block and the reader can see the overlap
without counting. Reordering is allowed - the order of factors in a product
never changes it (Chapter 6, section 1.3).

The right panel is the case where the overlap is empty. There is still an
answer, because 1 divides everything, and it is exactly the case Chapter 13
called coprime.

Run with:  python figures/fig_04_shared_bricks.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"             # a brick only the first number has
ORANGE = "#E67E22"           # a brick only the second number has
GREEN = "#1E8449"            # a brick both numbers have
PURPLE = "#8E44AD"           # the exponent form of the answer
GREY = "#78909C"
INK = "#212121"

FILL = {BLUE: "#E9F2FC", ORANGE: "#FDF0E3", GREEN: "#E8F5EC"}

W, H = 12.40, 6.90
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

TW, TH, TGAP = 0.80, 0.72, 0.12
PANEL_W, PANEL_H = 5.50, 5.45
PANEL_Y = 0.25
PGAP = 0.55
PLEFT = (W - 2 * PANEL_W - PGAP) / 2


def tiles(x, y, items):
    """Draw a row of prime bricks. `items` is (text, colour, shared) triples."""
    for i, (text, colour, shared) in enumerate(items):
        tx = x + i * (TW + TGAP)
        ax.add_patch(FancyBboxPatch((tx, y), TW, TH,
                                    boxstyle="round,pad=0.02,rounding_size=0.10",
                                    facecolor=FILL[colour] if shared else "white",
                                    edgecolor=colour,
                                    linewidth=2.0 if shared else 1.4,
                                    linestyle="solid" if shared else (0, (3, 3))))
        ax.text(tx + TW / 2, y + TH / 2, text, ha="center", va="center",
                fontsize=19, color=colour,
                fontweight="bold" if shared else "normal")


def panel(px, heading, a_label, b_label, a_tiles, b_tiles, gcf_tiles,
          captions, gcf_line, left_line, verdict, verdict_colour):
    """Draw one of the two panels."""
    ax.add_patch(FancyBboxPatch((px, PANEL_Y), PANEL_W, PANEL_H,
                                boxstyle="round,pad=0.02,rounding_size=0.16",
                                facecolor="white", edgecolor=GREY,
                                linewidth=1.6))
    ax.text(px + PANEL_W / 2, PANEL_Y + PANEL_H - 0.42, heading,
            ha="center", va="center", fontsize=16, color=INK, fontweight="bold")

    LX = px + 1.30                       # left edge of the first brick in a row
    r1, r2, r3 = 4.15, 3.23, 2.08        # the three rows of bricks

    ax.text(LX - 0.22, r1 + TH / 2, a_label, ha="right", va="center",
            fontsize=17, color=BLUE, fontweight="bold")
    tiles(LX, r1, a_tiles)

    ax.text(LX - 0.22, r2 + TH / 2, b_label, ha="right", va="center",
            fontsize=17, color=ORANGE, fontweight="bold")
    tiles(LX, r2, b_tiles)

    # the rule that separates "what the two numbers are" from "what we keep"
    ax.plot([px + 0.32, px + PANEL_W - 0.32], [r2 - 0.30, r2 - 0.30],
            color=GREY, linewidth=1.2, linestyle=(0, (4, 3)))

    ax.text(LX - 0.22, r3 + TH / 2, "GCF =", ha="right", va="center",
            fontsize=17, color=INK, fontweight="bold")
    tiles(LX, r3, gcf_tiles)

    # one small word under each brick of the answer row
    for i, (text, colour) in enumerate(captions):
        ax.text(LX + i * (TW + TGAP) + TW / 2, r3 - 0.26, text,
                ha="center", va="center", fontsize=11, color=colour)

    ax.text(px + PANEL_W / 2, 1.35, verdict, ha="center", va="center",
            fontsize=14, color=verdict_colour, fontweight="bold")
    ax.text(px + PANEL_W / 2, 0.83, gcf_line, ha="center", va="center",
            fontsize=18, color=PURPLE)
    ax.text(px + PANEL_W / 2, 0.43, left_line, ha="center", va="center",
            fontsize=13, color=GREY)


panel(PLEFT,
      "18 and 24 share two bricks",
      "18 =", "24 =",
      [("2", GREEN, True), ("3", GREEN, True), ("3", BLUE, False)],
      [("2", GREEN, True), ("3", GREEN, True), ("2", ORANGE, False),
       ("2", ORANGE, False)],
      [("2", GREEN, True), ("3", GREEN, True)],
      [("in both", GREEN), ("in both", GREEN)],
      r"$\mathrm{GCF}(18,\, 24) = 2 \times 3 = 6$",
      r"what is left: $18 \div 6 = 3$ and $24 \div 6 = 4$",
      "keep only the bricks that are in both rows", GREEN)

panel(PLEFT + PANEL_W + PGAP,
      "8 and 15 share no brick at all",
      "8 =", "15 =",
      [("2", BLUE, False), ("2", BLUE, False), ("2", BLUE, False)],
      [("3", ORANGE, False), ("5", ORANGE, False)],
      [("1", GREEN, True)],
      [("nothing shared", GREEN)],
      r"$\mathrm{GCF}(8,\, 15) = 1$",
      r"nothing can be taken out of both",
      "an empty overlap still has an answer: 1", ORANGE)

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.40,
        "The greatest common factor is the overlap of the two prime piles",
        ha="center", va="center", fontsize=19, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.82,
        "a solid green brick is in both numbers; a hollow brick belongs to one of "
        "them only and has to be dropped",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_shared_bricks.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
