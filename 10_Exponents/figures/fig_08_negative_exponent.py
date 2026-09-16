"""Figure 8 - a negative exponent moves the term across the fraction bar.

Top half: the rule with letters. The term crosses the bar and the minus sign
on the exponent is spent doing it, so what arrives underneath has a positive
exponent.

Bottom half: the same move with numbers, next to the two answers a reader is
most likely to write instead. Each wrong answer carries a red cross beside
it rather than a line through it: a stroke drawn across a stacked fraction
lands in the middle of it and makes it unreadable.
Run with:  python figures/fig_08_negative_exponent.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"        # the term once it has a positive exponent
ORANGE = "#E67E22"      # the negative exponent
GREY = "#78909C"
RED = "#C0392B"         # the wrong answers
INK = "#212121"

W, H = 11.6, 5.80
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# ---- the top half: the rule, written with letters -------------------------
Y_TOP = 4.00
ax.text(1.95, Y_TOP, r"$x^{-3}$", ha="center", va="center",
        fontsize=40, color=ORANGE, fontweight="bold")
ax.text(1.95, Y_TOP + 0.92, "a minus sign\nup in the corner",
        ha="center", va="center", fontsize=13, color=GREY, linespacing=1.5)

# the move itself, drawn as one curved arrow from above the bar to below it
ax.add_patch(FancyArrowPatch((2.90, Y_TOP + 0.18), (5.70, Y_TOP - 0.52),
                             connectionstyle="arc3,rad=-0.38",
                             arrowstyle="-|>", mutation_scale=20,
                             color=GREY, linewidth=2.0))
ax.text(4.30, Y_TOP + 0.92, "move it under the bar",
        ha="center", va="center", fontsize=14.5, color=INK, fontweight="bold")

ax.text(6.55, Y_TOP + 0.02, r"$=$", ha="center", va="center", fontsize=26, color=INK)
ax.text(7.45, Y_TOP + 0.44, r"$1$", ha="center", va="center", fontsize=28, color=INK)
ax.plot([6.95, 7.95], [Y_TOP + 0.04] * 2, color=INK, linewidth=2.4)
ax.text(7.45, Y_TOP - 0.44, r"$x^{3}$", ha="center", va="center",
        fontsize=30, color=BLUE, fontweight="bold")
ax.text(9.65, Y_TOP + 0.02, "and the minus sign\nhas gone",
        ha="center", va="center", fontsize=13, color=BLUE, linespacing=1.5)

ax.plot([0.60, W - 0.60], [2.62] * 2, color=GREY, linewidth=1.1,
        linestyle=(0, (5, 4)))

# ---- the bottom half: the same move with real numbers ---------------------
Y_BOT = 1.62
ax.text(2.05, Y_BOT, r"$2^{-2} \;=\; \frac{1}{2^{2}} \;=\; \frac{1}{4}$",
        ha="center", va="center", fontsize=30, color=INK)
ax.text(2.05, Y_BOT - 0.88, "one quarter, and one quarter\nis bigger than zero",
        ha="center", va="center", fontsize=13, color=GREY, linespacing=1.5)

ax.add_patch(FancyBboxPatch((5.05, Y_BOT - 0.80), 6.05, 1.60,
                            boxstyle="round,pad=0.04,rounding_size=0.14",
                            facecolor="#FBECEA", edgecolor=RED, linewidth=1.6))
ax.text(5.42, Y_BOT + 0.48, "The two answers to never write:",
        ha="left", va="center", fontsize=13.5, color=RED, fontweight="bold")
for k, wrong in enumerate([r"$2^{-2} = -4$", r"$2^{-2} = \frac{1}{-4}$"]):
    cx = 6.90 + k * 2.85
    ax.text(cx, Y_BOT - 0.24, wrong, ha="center", va="center",
            fontsize=22, color=RED)
    # a cross beside the answer, not a line through it
    mx, my, r = cx - 1.20, Y_BOT - 0.24, 0.14
    ax.plot([mx - r, mx + r], [my - r, my + r], color=RED, linewidth=2.6)
    ax.plot([mx - r, mx + r], [my + r, my - r], color=RED, linewidth=2.6)

ax.text(W / 2, H - 0.30,
        "A minus sign on the exponent is an instruction, not a sign on the answer",
        ha="center", va="center", fontsize=16.5, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_08_negative_exponent.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
