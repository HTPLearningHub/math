"""Figure 5 - one pair of stacks, two different answers.

The source's third common mistake is taking the highest power instead of the
lowest, and it says in one line that the highest power gives the LCM. That
line deserves a picture, because it is the single fact that keeps the GCF
and the LCM apart in the reader's head.

The stacks here are exactly the stacks of Figure 3. Nothing about the two
numbers has changed. Only the reading has: take the shorter stack of each
prime and you go down to 12, take the taller one and you go up to 216. The
layout says it too - the LCM is drawn above the stacks and the GCF below
them, because one answer is always at least as big as both numbers and the
other is always at most as small.

Run with:  python figures/fig_05_gcf_and_lcm_two_ends.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrow
from pathlib import Path

BLUE = "#2E86DE"             # comes from 24
ORANGE = "#E67E22"           # comes from 108
GREEN = "#1E8449"            # the GCF, this chapter's answer
PURPLE = "#8E44AD"           # the exponent form of an answer, as in Chapters 10-13
GREY = "#78909C"             # the LCM here: Chapter 13's answer, shown for contrast
INK = "#212121"

W, H = 10.60, 7.95
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

TW, TH = 1.05, 0.62          # one tile
TGAP = 0.10
COLGAP = 0.16
GROUPGAP = 1.55
BASE = 2.95                  # the floor every stack stands on

# prime, how many times it is in 24, how many times it is in 108
GROUPS = [(2, 3, 2), (3, 1, 3)]

GW = 2 * TW + COLGAP
TOTAL = len(GROUPS) * GW + (len(GROUPS) - 1) * GROUPGAP
LEFT = (W - TOTAL) / 2


def stack(x, count, shared, colour, fill, prime):
    """One column of tiles. The bottom `shared` of them are green (both own them)."""
    for k in range(count):
        y = BASE + k * (TH + TGAP)
        solid = k < shared
        ax.add_patch(FancyBboxPatch((x, y), TW, TH,
                                    boxstyle="round,pad=0.02,rounding_size=0.10",
                                    facecolor="#E8F5EC" if solid else fill,
                                    edgecolor=GREEN if solid else colour,
                                    linewidth=2.0 if solid else 1.6))
        ax.text(x + TW / 2, y + TH / 2, str(prime), ha="center", va="center",
                fontsize=19, color=GREEN if solid else colour, fontweight="bold")


for g, (prime, c24, c108) in enumerate(GROUPS):
    gx = LEFT + g * (GW + GROUPGAP)
    lo, hi = min(c24, c108), max(c24, c108)

    stack(gx, c24, lo, BLUE, "#E9F2FC", prime)
    stack(gx + TW + COLGAP, c108, lo, ORANGE, "#FDF0E3", prime)

    # ------------------------------ what each column is, and how tall it stands
    for x, count, colour, who in ((gx, c24, BLUE, "24"),
                                  (gx + TW + COLGAP, c108, ORANGE, "108")):
        ax.text(x + TW / 2, BASE - 0.30, f"in {who}", ha="center", va="center",
                fontsize=13, color=colour, fontweight="bold")
        word = "time" if count == 1 else "times"
        ax.text(x + TW / 2, BASE - 0.60, f"{count} {word}", ha="center",
                va="center", fontsize=12, color=GREY)

    # ------------------------------------- downwards to the GCF: the shorter stack
    ax.add_patch(FancyArrow(gx + GW / 2, BASE - 0.75, 0, -0.23, width=0.05,
                            head_width=0.22, head_length=0.16,
                            length_includes_head=True, color=GREEN))
    ax.add_patch(FancyBboxPatch((gx, 1.25), GW, 0.72,
                                boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor="#E8F5EC", edgecolor=GREEN,
                                linewidth=2.0))
    ax.text(gx + GW / 2, 1.61, rf"take ${prime}^{{{lo}}}$", ha="center",
            va="center", fontsize=18, color=GREEN, fontweight="bold")

    # ---------------------------------------- upwards to the LCM: the taller stack
    top = BASE + hi * (TH + TGAP) - TGAP        # the top of the taller stack
    ax.add_patch(FancyArrow(gx + GW / 2, top + 0.06, 0, 0.28, width=0.05,
                            head_width=0.22, head_length=0.16,
                            length_includes_head=True, color=GREY))
    ax.add_patch(FancyBboxPatch((gx, 5.35), GW, 0.72,
                                boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor="#ECEFF1", edgecolor=GREY,
                                linewidth=2.0))
    ax.text(gx + GW / 2, 5.71, rf"take ${prime}^{{{hi}}}$", ha="center",
            va="center", fontsize=18, color=INK, fontweight="bold")

# ------------------------------------------------------------- the LCM, at the top
ax.text(W / 2, 6.92,
        r"$\mathrm{LCM}(24,\, 108) = 2^{3} \times 3^{3} = 216$",
        ha="center", va="center", fontsize=20, color=PURPLE)
ax.text(W / 2, 6.42,
        "the LCM keeps the taller stack of each prime - it is at least as big as "
        "both numbers",
        ha="center", va="center", fontsize=13, color=GREY)

# ---------------------------------------------------------- the GCF, at the bottom
ax.text(W / 2, 0.88,
        "the GCF keeps the shorter stack of each prime - it is at most as big as "
        "the smaller number",
        ha="center", va="center", fontsize=13, color=GREEN)
ax.text(W / 2, 0.38,
        r"$\mathrm{GCF}(24,\, 108) = 2^{2} \times 3 = 12$",
        ha="center", va="center", fontsize=20, color=PURPLE)

# ------------------------------------------------------------------- the title
ax.text(W / 2, H - 0.38,
        "The same two stacks, read in the two possible directions",
        ha="center", va="center", fontsize=20, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_gcf_and_lcm_two_ends.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
