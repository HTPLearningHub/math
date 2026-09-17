"""Figure 5 - the same product, split two ways.

The source states LCM(a, b) x GCF(a, b) = a x b as its fourth rule and never
draws it. The picture worth having is that a x b is one number, and that the
pair (GCF, LCM) is a second way of cutting that same number in two. Drawing
the product once, in the middle, with the two factor pairs above and below,
makes the rule look like what it is: a rearrangement, not a new fact.

Two examples, so that the reader sees it hold when the numbers share a prime
(6 and 9) and when they are much further apart (12 and 80).
Run with:  python figures/fig_05_lcm_gcf_bridge.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"             # the two numbers you started with
GREEN = "#1E8449"            # the product they both make
PURPLE = "#8E44AD"           # the GCF and LCM pair
GREY = "#78909C"
INK = "#212121"

W, H = 12.00, 7.00
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

PANEL_W, PANEL_H, PANEL_Y = 5.30, 5.00, 0.80
BH = 0.80                                  # every box is this tall


def box(cx, y, w, text, colour, fill, size=19):
    """One rounded box, centred on cx."""
    ax.add_patch(FancyBboxPatch((cx - w / 2, y), w, BH,
                                boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor=fill, edgecolor=colour, linewidth=2.0))
    ax.text(cx, y + BH / 2, text, ha="center", va="center",
            fontsize=size, color=colour, fontweight="bold")


def panel(px, a, b, gcf, lcm):
    """Draw one worked case: a x b on top, GCF x LCM underneath."""
    product = a * b
    cx = px + PANEL_W / 2

    ax.add_patch(FancyBboxPatch((px, PANEL_Y), PANEL_W, PANEL_H,
                                boxstyle="round,pad=0.02,rounding_size=0.16",
                                facecolor="white", edgecolor=GREY, linewidth=1.6))
    ax.text(cx, 5.42, f"the numbers {a} and {b}", ha="center", va="center",
            fontsize=16, color=INK, fontweight="bold")

    # ------------------------------------------- the pair you started with
    box(cx - 1.00, 4.35, 1.50, str(a), BLUE, "#E9F2FC")
    box(cx + 1.00, 4.35, 1.50, str(b), BLUE, "#E9F2FC")
    ax.text(cx, 4.35 + BH / 2, r"$\times$", ha="center", va="center",
            fontsize=20, color=GREY)
    ax.annotate("", xy=(cx, 3.99), xytext=(cx, 4.31),
                arrowprops=dict(arrowstyle="-|>", color=GREY, linewidth=1.8))

    # --------------------------------------------------- the shared product
    box(cx, 3.10, 3.90, str(product), GREEN, "#E8F5EC", size=26)

    ax.annotate("", xy=(cx, 2.71), xytext=(cx, 3.06),
                arrowprops=dict(arrowstyle="<|-", color=GREY, linewidth=1.8))

    # ------------------------------------------------- the other pair, below
    box(cx - 1.15, 1.85, 1.90, f"GCF = {gcf}", PURPLE, "#F4ECF7", size=15)
    box(cx + 1.15, 1.85, 1.90, f"LCM = {lcm}", PURPLE, "#F4ECF7", size=15)
    ax.text(cx, 1.85 + BH / 2, r"$\times$", ha="center", va="center",
            fontsize=20, color=GREY)

    ax.text(cx, 1.28, f"{gcf} " + r"$\times$" + f" {lcm} = {product}",
            ha="center", va="center", fontsize=16, color=PURPLE)


panel(0.40, 6, 9, 3, 18)
panel(6.30, 12, 80, 4, 240)

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.40, "One product, two ways to split it",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")
ax.text(W / 2, H - 0.84,
        r"$a \times b$ and $\mathrm{GCF} \times \mathrm{LCM}$ always land on the same number",
        ha="center", va="center", fontsize=14, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_lcm_gcf_bridge.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
