"""Figure 5 - how far an exponent reaches.

The mistake this figure is built against is reading 3 x 2^3 as if the 3 and
the 2 were multiplied first. The exponent sits on one number only, and the
only thing that can widen its reach is a bracket.

Left panel: the expression as written, with a brace under the 2 alone.
Right panel: the expression the mistake actually computes, with the brace
under both numbers. The two answers are printed at the bottom of each panel
so the size of the mistake is visible: 24 against 216.
Run with:  python figures/fig_05_reach.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

PURPLE = "#8E44AD"           # the exponent, as in Chapter 10
GREEN = "#1E8449"            # the right answer
RED = "#C0392B"              # the wrong answer
GREY = "#78909C"
INK = "#212121"

W, H = 11.6, 6.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

PW, PH = 5.05, 4.18                       # panel width and height
COLS = (3.03, 8.57)                       # centre of the left / right panel
TOP = H - 1.42                            # top edge of both panels

PANELS = [
    (GREEN, "#E8F5EC", "What is written",
     r"$3 \times 2^{3}$",
     r"$2^{3}$", "the exponent sits on the 2 only",
     [r"$2^{3} = 8$", r"$3 \times 8 = 24$"], r"$24$", "right"),
    (RED, "#FBECEA", "What the mistake computes",
     r"$(3 \times 2)^{3}$",
     r"$(3 \times 2)$", "a bracket would be needed to reach the 3",
     [r"$3 \times 2 = 6$", r"$6^{3} = 216$"], r"$216$", "wrong"),
]

for cx, (edge, tint, title, expr, reach, note, steps, answer, verdict) in zip(COLS, PANELS):
    ax.add_patch(FancyBboxPatch((cx - PW / 2, TOP - PH), PW, PH,
                                boxstyle="round,pad=0.05,rounding_size=0.16",
                                facecolor=tint, edgecolor=edge, linewidth=1.9))
    ax.text(cx, TOP - 0.42, title, ha="center", va="center",
            fontsize=15.5, color=edge, fontweight="bold")
    # the expression itself, large
    ax.text(cx, TOP - 1.22, expr, ha="center", va="center",
            fontsize=34, color=INK)
    # what the exponent reaches, said in words rather than drawn with a brace,
    # because a brace under mathtext never lines up with the glyph above it
    ax.text(cx, TOP - 1.96, "the exponent reaches", ha="center", va="center",
            fontsize=12.5, color=GREY)
    ax.text(cx, TOP - 2.40, reach, ha="center", va="center",
            fontsize=23, color=PURPLE)
    ax.text(cx, TOP - 2.86, note, ha="center", va="center",
            fontsize=12.5, color=GREY)
    # the two steps, side by side, then the answer
    ax.text(cx, TOP - 3.32, steps[0] + "          " + steps[1],
            ha="center", va="center", fontsize=17, color=INK)
    ax.text(cx - 0.55, TOP - 3.72, answer, ha="center", va="center",
            fontsize=25, color=edge, fontweight="bold")
    ax.text(cx + 0.72, TOP - 3.72, verdict, ha="center", va="center",
            fontsize=15, color=edge, fontweight="bold")

ax.text(W / 2, H - 0.45, "An exponent holds on to one number",
        ha="center", va="center", fontsize=19.5, color=INK, fontweight="bold")
ax.text(W / 2, 0.45,
        "Level 2 comes before Level 3, so the power is worked out first "
        "and only then multiplied by the 3.",
        ha="center", va="center", fontsize=15, color=INK)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_reach.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
