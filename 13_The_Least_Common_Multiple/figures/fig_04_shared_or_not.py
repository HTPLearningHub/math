"""Figure 4 - why the product is sometimes too big, and sometimes exactly right.

The source states two separate rules: LCM(a, b) <= a x b, and LCM(a, b) =
a x b when the numbers are coprime. They are really one picture. Building
the LCM means laying out the primes of the first number and then adding only
what the second number still needs. A prime that both numbers own is written
once instead of twice, and that is exactly the saving; when nothing is
shared there is nothing to save, so the LCM is the whole product.

Left panel: 6 and 9 share a 3, so one tile is saved and 18 < 54.
Right panel: 4 and 5 share nothing, so 20 = 4 x 5.
Run with:  python figures/fig_04_shared_or_not.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"             # a prime that came from the first number
ORANGE = "#E67E22"           # a prime that came from the second number
GREEN = "#1E8449"            # a prime both numbers own
PURPLE = "#8E44AD"           # the exponent form of the answer
GREY = "#78909C"
INK = "#212121"

FILL = {BLUE: "#E9F2FC", ORANGE: "#FDF0E3", GREEN: "#E8F5EC"}

W, H = 12.00, 7.70
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

TW, TH, TGAP = 0.80, 0.72, 0.12
PANEL_W, PANEL_H = 5.30, 5.60
PANEL_Y = 0.85


def tiles(x, y, items):
    """Draw a horizontal row of prime tiles. `items` is (text, colour) pairs."""
    for i, (text, colour) in enumerate(items):
        tx = x + i * (TW + TGAP)
        ax.add_patch(FancyBboxPatch((tx, y), TW, TH,
                                    boxstyle="round,pad=0.02,rounding_size=0.10",
                                    facecolor=FILL[colour], edgecolor=colour,
                                    linewidth=1.8))
        ax.text(tx + TW / 2, y + TH / 2, text, ha="center", va="center",
                fontsize=19, color=colour, fontweight="bold")


def panel(px, heading, a, b, a_tiles, b_tiles, lcm_tiles, captions,
          lcm_line, product_line, verdict, verdict_colour):
    """Draw one of the two panels."""
    ax.add_patch(FancyBboxPatch((px, PANEL_Y), PANEL_W, PANEL_H,
                                boxstyle="round,pad=0.02,rounding_size=0.16",
                                facecolor="white", edgecolor=GREY,
                                linewidth=1.6))
    ax.text(px + PANEL_W / 2, PANEL_Y + PANEL_H - 0.42, heading,
            ha="center", va="center", fontsize=16, color=INK, fontweight="bold")

    LX = px + 1.40                       # left edge of the first tile in a row
    r1, r2, r3 = 4.90, 3.98, 2.85        # the three rows of tiles

    ax.text(LX - 0.22, r1 + TH / 2, a, ha="right", va="center",
            fontsize=17, color=BLUE, fontweight="bold")
    tiles(LX, r1, a_tiles)

    ax.text(LX - 0.22, r2 + TH / 2, b, ha="right", va="center",
            fontsize=17, color=ORANGE, fontweight="bold")
    tiles(LX, r2, b_tiles)

    # the rule that separates "what we have" from "what we build"
    ax.plot([px + 0.32, px + PANEL_W - 0.32], [r2 - 0.30, r2 - 0.30],
            color=GREY, linewidth=1.2, linestyle=(0, (4, 3)))

    ax.text(LX - 0.22, r3 + TH / 2, "LCM =", ha="right", va="center",
            fontsize=17, color=INK, fontweight="bold")
    tiles(LX, r3, lcm_tiles)

    # one small word under each tile of the LCM row, saying where it came from
    for i, (text, colour) in enumerate(captions):
        ax.text(LX + i * (TW + TGAP) + TW / 2, r3 - 0.26, text,
                ha="center", va="center", fontsize=11, color=colour)

    ax.text(px + PANEL_W / 2, 2.10, verdict, ha="center", va="center",
            fontsize=14, color=verdict_colour, fontweight="bold")
    ax.text(px + PANEL_W / 2, 1.55, lcm_line, ha="center",
            va="center", fontsize=18, color=PURPLE)
    ax.text(px + PANEL_W / 2, 1.12, product_line, ha="center",
            va="center", fontsize=14, color=GREY)


panel(0.40,
      "6 and 9 share a prime",
      "6 =", "9 =",
      [("2", BLUE), ("3", BLUE)],
      [("3", ORANGE), ("3", ORANGE)],
      [("2", BLUE), ("3", GREEN), ("3", ORANGE)],
      [("from 6", BLUE), ("shared", GREEN), ("one more", ORANGE)],
      r"$\mathrm{LCM}(6,\, 9) = 2 \times 3^{2} = 18$",
      r"while $6 \times 9 = 54$",
      "the shared 3 is written once, so 18 is enough", GREEN)

panel(6.30,
      "4 and 5 share nothing",
      "4 =", "5 =",
      [("2", BLUE), ("2", BLUE)],
      [("5", ORANGE)],
      [("2", BLUE), ("2", BLUE), ("5", ORANGE)],
      [("from 4", BLUE), ("from 4", BLUE), ("from 5", ORANGE)],
      r"$\mathrm{LCM}(4,\, 5) = 2^{2} \times 5 = 20$",
      r"and $4 \times 5 = 20$",
      "nothing is shared, so nothing is saved", ORANGE)

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.40, "Build the LCM: lay out one number, then add what the other still needs",
        ha="center", va="center", fontsize=19, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.84,
        "every prime they both own is written once - that is the whole saving",
        ha="center", va="center", fontsize=13, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_04_shared_or_not.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
