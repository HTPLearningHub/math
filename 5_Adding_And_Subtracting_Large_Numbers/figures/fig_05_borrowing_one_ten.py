"""Figure 5 - what borrowing actually does: 473 packed two different ways.

Top row: 473 packed the usual way - 4 hundreds, 7 tens, 3 ones.
Bottom row: the same 473 with one ten broken open - 4 hundreds, 6 tens and
13 ones. The ten ones that came out of the broken ten are orange, the colour
this book uses for the piece that moves.

The point of the picture is the two sums written under the rows: 400 + 70 + 3
and 400 + 60 + 13 are both 473. Borrowing does not make the number smaller or
bigger. It only re-packs it so that the ones column has enough to take 6 away.

Run with:  python figures/fig_05_borrowing_one_ten.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"        # pieces that were already there
BLUE_FILL = "#EAF2FB"
ORANGE = "#E67E22"      # the pieces that came out of the broken ten
ORANGE_FILL = "#FDF0E3"
GREY = "#78909C"
INK = "#212121"

W, H = 12.0, 5.2        # figure size in inches
Y_BOTTOM = 1.30         # bottom of the drawing area

# the three groups get their own strip of the page, left to right
AREA = {"hundreds": (0.60, 3.30), "tens": (3.85, 7.45), "ones": (7.75, 11.55)}

fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(Y_BOTTOM, Y_BOTTOM + H)


def tokens(area, y, count, size, label, colour, fill, fontsize):
    """Draw `count` square tokens in a row, centred inside `area`."""
    x_lo, x_hi = AREA[area]
    gap = min(0.12, size * 0.30)
    width = count * size + (count - 1) * gap
    x0 = (x_lo + x_hi) / 2 - width / 2
    for i in range(count):
        x = x0 + i * (size + gap)
        ax.add_patch(FancyBboxPatch((x, y - size / 2), size, size,
                                    boxstyle="round,pad=0.01,rounding_size=0.04",
                                    facecolor=fill, edgecolor=colour, linewidth=1.4))
        ax.text(x + size / 2, y, label, ha="center", va="center",
                fontsize=fontsize, color=colour)


def group_name(area, y, text, colour=BLUE):
    """Write the name of a group under it."""
    x_lo, x_hi = AREA[area]
    ax.text((x_lo + x_hi) / 2, y, text, ha="center", va="top",
            fontsize=13, color=colour, fontweight="bold")


ax.text(W / 2, 6.30, r"The same $473$, packed two different ways",
        ha="center", va="center", fontsize=17, fontweight="bold", color=INK)

# ------------------------------------------------- the usual packing of 473 --
tokens("hundreds", 5.40, 4, 0.50, "100", BLUE, BLUE_FILL, 8.5)
tokens("tens", 5.40, 7, 0.38, "10", BLUE, BLUE_FILL, 8.5)
tokens("ones", 5.40, 3, 0.30, "1", BLUE, BLUE_FILL, 8.5)
group_name("hundreds", 5.05, r"$4$ hundreds")
group_name("tens", 5.05, r"$7$ tens")
group_name("ones", 5.05, r"$3$ ones")
ax.text(W / 2, 4.42, r"$400 + 70 + 3 = 473$", ha="center", va="center",
        fontsize=15, color=INK)

# ------------------------------------------------------- the trade, in words --
ax.annotate("", xy=(W / 2, 3.62), xytext=(W / 2, 4.12),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, linewidth=2.4,
                            mutation_scale=20))
ax.text(W / 2 + 0.25, 3.87, "break one ten open into ten ones",
        ha="left", va="center", fontsize=13, color=ORANGE, fontweight="bold")

# --------------------------------------------------- 473 after the borrowing --
tokens("hundreds", 3.05, 4, 0.50, "100", BLUE, BLUE_FILL, 8.5)
tokens("tens", 3.05, 6, 0.38, "10", BLUE, BLUE_FILL, 8.5)
# the 13 ones sit in two short rows: the ten new ones above, the old three below
tokens("ones", 3.24, 10, 0.28, "1", ORANGE, ORANGE_FILL, 8.0)
tokens("ones", 2.86, 3, 0.28, "1", BLUE, BLUE_FILL, 8.0)
group_name("hundreds", 2.62, r"$4$ hundreds")
group_name("tens", 2.62, r"$6$ tens")
group_name("ones", 2.62, r"$13$ ones", ORANGE)
ax.text(W / 2, 2.00, r"$400 + 60 + 13 = 473$", ha="center", va="center",
        fontsize=15, color=INK)

ax.text(W / 2, 1.55, "Nothing was added and nothing was thrown away. "
                     "The number is still $473$.",
        ha="center", va="center", fontsize=13, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_05_borrowing_one_ten.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
