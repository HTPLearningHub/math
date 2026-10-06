"""Figure 1 - cancel factors, never terms.

Two panels side by side.
Left (green): x^2 (x + 1) over (x + 1). The bracket (x + 1) is a factor of
the whole top and of the whole bottom, so both copies are struck through and
the answer is x^2.
Right (red): (x + 5) over (x + 2). The x is only a term (it is added), so
striking it out is wrong. A test with x = 3 shows the two values differ:
8/5 against 5/2.

Colours: green for the allowed move, red for the forbidden one, slate for
the parts that stay.

Run with:  python figures/fig_01_factors_vs_terms.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

INK = "#212121"
SLATE = "#5D6D7E"                                  # parts that stay
GREEN = "#1E8449"                                  # allowed cancelling
RED = "#C0392B"                                    # forbidden cancelling

fig, ax = plt.subplots(figsize=(15, 7.6))
ax.set_xlim(0, 15)
ax.set_ylim(0, 7.6)
ax.axis("off")


def piece(x, y, s, col, size=34):
    """Write one piece of a fraction and return its text object."""
    return ax.text(x, y, s, ha="center", va="center", fontsize=size, color=col)


def strike(t, col):
    """Draw a slanted line through a text object, like a pencil cross-out."""
    fig.canvas.draw()                              # positions exist only after a draw
    bb = t.get_window_extent().transformed(ax.transData.inverted())
    ax.plot([bb.x0 - 0.05, bb.x1 + 0.05], [bb.y0 - 0.02, bb.y1 + 0.02],
            color=col, lw=4, solid_capstyle="round")


# ---------- the two panel frames ----------
for x0, col in [(0.2, GREEN), (7.8, RED)]:
    ax.add_patch(FancyBboxPatch((x0, 0.3), 7.0, 6.9, boxstyle="round,pad=0.05",
                                facecolor=col, alpha=0.06, edgecolor=col, lw=2.5))

# ---------- left panel: a factor ----------
ax.text(3.7, 6.6, "Allowed: $(x + 1)$ is a factor", ha="center", fontsize=20,
        color=GREEN, fontweight="bold")
piece(2.55, 4.95, r"$x^{2}$", SLATE)               # stays on top
top_br = piece(3.95, 4.95, r"$(x + 1)$", GREEN)    # multiplied factor on top
ax.plot([1.9, 4.9], [4.3, 4.3], color=INK, lw=3)   # the fraction bar
bot_br = piece(3.4, 3.6, r"$(x + 1)$", GREEN)      # the whole bottom
strike(top_br, GREEN)
strike(bot_br, GREEN)
piece(5.75, 4.3, r"$= x^{2}$", SLATE)              # result
ax.text(3.7, 2.35, "The top is  $x^{2}$  times  $(x + 1)$.\n"
        "Dividing top and bottom by $(x + 1)$\nchanges nothing.",
        ha="center", va="center", fontsize=16, color=INK, linespacing=1.6)
ax.text(3.7, 0.85, r"(only for $x \neq -1$)", ha="center", fontsize=15,
        color=SLATE)

# ---------- right panel: a term ----------
ax.text(11.3, 6.6, "Not allowed: $x$ is a term", ha="center", fontsize=20,
        color=RED, fontweight="bold")
tx = piece(9.75, 4.95, r"$x$", RED)                # added, not multiplied
piece(10.75, 4.95, r"$+\ 5$", SLATE)
ax.plot([9.3, 11.3], [4.3, 4.3], color=INK, lw=3)  # the fraction bar
bx = piece(9.75, 3.6, r"$x$", RED)
piece(10.75, 3.6, r"$+\ 2$", SLATE)
strike(tx, RED)
strike(bx, RED)
piece(12.55, 4.3, r"$\neq \dfrac{5}{2}$", RED)     # the wrong answer
ax.text(11.3, 2.35, r"Test with $x = 3$:" "\n"
        r"$\dfrac{3 + 5}{3 + 2} = \dfrac{8}{5}$,   but   $\dfrac{5}{2}$ is a different number.",
        ha="center", va="center", fontsize=16, color=INK, linespacing=1.9)
ax.text(11.3, 0.85, "$x$ is added, so it is not a factor of the whole top",
        ha="center", fontsize=15, color=RED)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_factors_vs_terms.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_01_factors_vs_terms.png")
