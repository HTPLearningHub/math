"""Figure 3 - the minus sign in front of a bracket reaches every term.

Top: -( x^4 - 3x^2 + 6x - 4 ), the four terms as cards coloured by exponent
(same colours as fig_01), with a big minus sign and brackets around them.
A magenta rail from the minus sign drops onto each of the four cards.
Bottom: the four cards after the minus has been handed out:
-x^4, +3x^2, -6x, +4. The sign of every card has changed, and under each
arrow the small calculation is written, e.g. -(-3x^2) = +3x^2.
The coefficient and the exponent never change - only the sign.

Run with:  python figures/fig_03_sign_flip.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
MAGENTA = "#C2185B"                                # the minus sign being handed out
# exponent -> (edge colour, light fill), as in fig_01
COL = {
    4: ("#8E44AD", "#F3EAF8"),
    2: ("#138D75", "#E6F5F1"),
    1: ("#B7950B", "#FBF5DE"),
    0: ("#E67E22", "#FDF0E3"),
}

W, H = 13.0, 7.2                                   # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def card(xc, yc, text, exp, w=1.75, h=0.95, size=24):
    """A rounded card centred on (xc, yc), coloured by its exponent."""
    e, f = COL[exp]
    ax.add_patch(FancyBboxPatch(
        (xc - w / 2, yc - h / 2), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.15",
        facecolor=f, edgecolor=e, linewidth=2.2, zorder=2))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=size,
            color=INK, zorder=3)


xs = [4.0, 6.3, 8.6, 10.9]                         # card centres
exps = [4, 2, 1, 0]
YT, YB = 5.0, 1.45                                 # top and bottom rows

# --- top row: the minus sign outside the bracket ---------------------------
ax.text(2.05, YT, r"$-$", ha="center", va="center", fontsize=46,
        color=MAGENTA, fontweight="bold")
ax.text(2.75, YT, r"$($", ha="center", va="center", fontsize=52, color=INK)
ax.text(12.1, YT, r"$)$", ha="center", va="center", fontsize=52, color=INK)
before = [r"$x^{4}$", r"$-3x^{2}$", r"$+6x$", r"$-4$"]
for xc, t, e in zip(xs, before, exps):
    card(xc, YT, t, e)

# --- the minus sign reaches every card: a magenta rail above the bracket ----
RAIL = YT + 0.95
ax.plot([2.05, 2.05], [YT + 0.45, RAIL], color=MAGENTA, lw=2.2)
ax.plot([2.05, xs[-1]], [RAIL, RAIL], color=MAGENTA, lw=2.2)
for xc in xs:                                      # one drop onto each card
    ax.annotate("", xy=(xc, YT + 0.5), xytext=(xc, RAIL),
                arrowprops=dict(arrowstyle="-|>", color=MAGENTA, lw=2.0,
                                mutation_scale=16))

# --- straight arrows down, each with its small calculation ------------------
calc = [r"$-(x^{4}) = -x^{4}$", r"$-(-3x^{2}) = +3x^{2}$",
        r"$-(+6x) = -6x$", r"$-(-4) = +4$"]
for xc, c in zip(xs, calc):
    ax.annotate("", xy=(xc, YB + 0.55), xytext=(xc, YT - 0.55),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.6,
                                mutation_scale=16))
    ax.text(xc, (YT + YB) / 2, c, ha="center", va="center", fontsize=13,
            color=MAGENTA, bbox=dict(facecolor="white", edgecolor="none",
                                     pad=3.0), zorder=5)

# --- bottom row: every sign has changed ------------------------------------
ax.text(0.3, YB, "after", ha="left", va="center", fontsize=15,
        color=GREY, fontweight="bold")
ax.text(0.3, YT, "before", ha="left", va="center", fontsize=15,
        color=GREY, fontweight="bold")
after = [r"$-x^{4}$", r"$+3x^{2}$", r"$-6x$", r"$+4$"]
for xc, t, e in zip(xs, after, exps):
    card(xc, YB, t, e)

ax.text(W / 2 + 0.8, 0.35,
        "every sign changes; the numbers and the exponents do not",
        ha="center", va="center", fontsize=14, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_sign_flip.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_03_sign_flip.png")
