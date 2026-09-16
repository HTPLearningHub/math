"""Figure 1 - why long division starts on the left: 624 shared between 3 people.

The picture answers the question the chapter opens with. A large number is a
pile of pieces of three different sizes: hundreds, tens and ones. You hand out
the biggest pieces first, because whatever is left over from a place can still
be cut into ten smaller pieces and handed out in the next place down.

Row 2 is the row that matters. Two tens cannot be shared between three people,
so nobody gets a ten and both tens stay on the table. They are not lost: the
orange arrow carries them into row 3, where they have become twenty ones and
join the four ones that were already there.

Colour: blue is a piece that was already in that place, orange is a piece that
moved down from the place above - the same convention as Chapter 5.

Layout note: the arrow and its label live in an empty corridor between the tens
band and the ones band, so the arrow crosses no text and no counter. The dotted
column separators are drawn band by band for the same reason. Do not close that
corridor up.
Run with:  python figures/fig_01_share_by_place.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

BLUE = "#2E86DE"        # a piece that already belonged to this place
ORANGE = "#E67E22"      # a piece that moved down from the place above
GREY = "#78909C"
PALE = "#FAFAFA"
INK = "#212121"

W, H = 12.0, 7.0
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# ---- the three column headings ----------------------------------------------
for x, label in [(3.05, "What is on the table"),
                 (7.75, "Each of the 3 people gets"),
                 (10.45, "Left on the table")]:
    ax.text(x, 6.60, label, ha="center", va="center",
            fontsize=15, color=INK, fontweight="bold")
ax.plot([0.35, 11.65], [6.32, 6.32], color=GREY, linewidth=1.4)

# ---- one band per place value -----------------------------------------------
# (centre height, place name, "each gets" text, "left over" text)
HALF = 0.78
BANDS = [(5.38, "hundreds", "2 hundreds", "nothing"),
         (3.62, "tens", "0 tens", "2 tens"),
         (1.15, "ones", "8 ones", "nothing")]

for y, name, got, left in BANDS:
    ax.add_patch(FancyBboxPatch((0.35, y - HALF), 11.30, 2 * HALF,
                                boxstyle="round,pad=0.02,rounding_size=0.12",
                                facecolor=PALE, edgecolor=GREY, linewidth=1.2))
    # the place name, standing on its own at the far left of the band
    ax.text(0.62, y, name, ha="left", va="center", rotation=90,
            fontsize=12, color=GREY, fontweight="bold")
    ax.text(7.75, y, got, ha="center", va="center",
            fontsize=17, color=INK, fontweight="bold")
    ax.text(10.45, y, left, ha="center", va="center",
            fontsize=17, color=ORANGE if left != "nothing" else GREY,
            fontweight="bold")
    # the two column separators, drawn inside this band only
    for x in (6.35, 9.15):
        ax.plot([x, x], [y - HALF + 0.10, y + HALF - 0.10],
                color=GREY, linewidth=1.0, linestyle=":")


def token(x, y, size, colour, label=None, fontsize=11):
    """Draw one square counter of the given size with its value inside."""
    ax.add_patch(Rectangle((x, y - size / 2), size, size,
                           facecolor=colour, edgecolor="white", linewidth=1.4))
    if label:
        ax.text(x + size / 2, y, label, ha="center", va="center",
                fontsize=fontsize, color="white", fontweight="bold")


# ---- row 1: six hundreds ----------------------------------------------------
S1, G1 = 0.72, 0.16
x = 1.15
for _ in range(6):
    token(x, 5.38, S1, BLUE, "100", 12)
    x += S1 + G1

# ---- row 2: two tens --------------------------------------------------------
S2, G2 = 0.60, 0.16
x = 1.15
for _ in range(2):
    token(x, 3.62, S2, BLUE, "10", 12)
    x += S2 + G2

# ---- row 3: twenty traded ones (orange) plus the four original ones (blue) --
S3, G3 = 0.26, 0.07
for row in range(2):
    y = 1.15 + (0.20 if row == 0 else -0.20)
    x = 1.15
    for col in range(12):
        n = row * 12 + col          # counter number, 0 to 23
        token(x, y, S3, ORANGE if n < 20 else BLUE)
        x += S3 + G3
ax.text(1.15 + 12 * (S3 + G3) + 0.22, 1.15, "24 ones", ha="left", va="center",
        fontsize=13, color=INK, fontweight="bold")

# ---- the arrow that carries the two leftover tens down into the ones --------
# It runs through the empty corridor between the tens band (bottom 2.92) and
# the ones band (top 1.93). Nothing else is drawn there.
ax.annotate("", xy=(2.55, 2.10), xytext=(10.20, 2.34),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, linewidth=2.4,
                            mutation_scale=20,
                            connectionstyle="arc3,rad=0.05"))
ax.text(6.30, 2.70, "cut each leftover ten into ten ones: "
                    r"$2$ tens become $20$ ones",
        ha="center", va="center", fontsize=14, color=ORANGE, fontweight="bold")

# ---- the answer, read down the middle column --------------------------------
ax.text(6.0, 0.14, r"Read the middle column downwards: $2$, $0$, $8$."
                   r"    That is the answer:  $624 \div 3 = 208$",
        ha="center", va="center", fontsize=15, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_share_by_place.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
