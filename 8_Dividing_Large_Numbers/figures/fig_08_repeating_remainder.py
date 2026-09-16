"""Figure 8 - carrying 397 divided by 11 past the decimal point.

The work does not change when the point is reached. The same four steps keep
turning; the only new thing is that the digits being brought down are zeros
that the writer put there.

What the picture is really for is the red path. The leftover after the ones is
1. Two turns later the leftover is 1 again. Nothing else in the working has
changed, so the two quotient digits that came out in between - 0 and 9 - must
come out again, and again, for ever. Both 1s are circled and the red path joins
them.

The red path is routed down the empty left-hand side of the tableau, where no
row has a digit, so it crosses nothing.
Run with:  python figures/fig_08_repeating_remainder.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
from pathlib import Path

BLUE = "#2E86DE"        # Divide   - a digit of the quotient
ORANGE = "#E67E22"      # Multiply - a product written underneath
PURPLE = "#8E44AD"      # Subtract - what is left after taking the product away
GREEN = "#1E8449"       # Bring down - a digit fetched from the dividend
RED = "#C0392B"         # the thing that repeats
GREY = "#78909C"
INK = "#212121"
FONT = "DejaVu Sans"    # a plain, unmarked zero

W, H = 11.9, 7.60
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

FS = 29
# five digit columns: hundreds, tens, ones, tenths, hundredths.
# the columns after the point are pushed right by 0.26 to leave room for it.
C = [2.30 + i * 0.60 + (0.26 if i >= 3 else 0) for i in range(5)]
X_POINT = (C[2] + C[3]) / 2
X_BAR, X_END = 1.46, C[4] + 0.34
HALF = 0.28


def digit(col, y, ch, colour):
    ax.text(C[col], y, ch, ha="center", va="center",
            fontsize=FS, family=FONT, color=colour)


def minus(col, y):
    ax.text(C[col] - 0.44, y, r"$-$", ha="center", va="center",
            fontsize=FS - 4, color=INK)


def rule(col_from, col_to, y):
    ax.plot([C[col_from] - HALF, C[col_to] + HALF], [y, y],
            color=INK, linewidth=1.8)


# ---- the bracket, the divisor, the dividend, the quotient -------------------
ax.plot([X_BAR, X_END], [6.68, 6.68], color=INK, linewidth=2.4)
ax.plot([X_BAR, X_BAR], [6.68, 1.15], color=INK, linewidth=2.4)
ax.text(0.96, 6.22, "11", ha="center", va="center",
        fontsize=FS, family=FONT, color=INK)
for col, ch in enumerate("397"):
    digit(col, 6.22, ch, INK)
for col in (3, 4):
    digit(col, 6.22, "0", INK)              # the zeros the writer adds
ax.text(X_POINT, 6.10, ".", ha="center", va="center",
        fontsize=FS, family=FONT, color=INK)

for col, ch in [(1, "3"), (2, "6"), (3, "0"), (4, "9")]:
    ax.text(C[col], 7.10, ch, ha="center", va="center",
            fontsize=FS, family=FONT, color=BLUE, fontweight="bold")
ax.text(X_POINT, 6.98, ".", ha="center", va="center",
        fontsize=FS, family=FONT, color=BLUE, fontweight="bold")

# ---- the whole-number part, exactly as in figure 7 --------------------------
minus(0, 5.64); digit(0, 5.64, "3", ORANGE); digit(1, 5.64, "3", ORANGE)
rule(0, 1, 5.36)
digit(1, 5.02, "6", PURPLE); digit(2, 5.02, "7", GREEN)

minus(1, 4.44); digit(1, 4.44, "6", ORANGE); digit(2, 4.44, "6", ORANGE)
rule(1, 2, 4.16)
digit(2, 3.82, "1", PURPLE); digit(3, 3.82, "0", GREEN)

# ---- the tenths: 11 does not fit into 10, so the quotient digit is 0 --------
minus(3, 3.24); digit(3, 3.24, "0", ORANGE)
rule(2, 3, 2.96)
digit(2, 2.62, "1", PURPLE); digit(3, 2.62, "0", PURPLE)
digit(4, 2.62, "0", GREEN)

# ---- the hundredths: 11 fits into 100 nine times ---------------------------
minus(3, 2.04); digit(3, 2.04, "9", ORANGE); digit(4, 2.04, "9", ORANGE)
rule(2, 4, 1.76)
digit(4, 1.42, "1", PURPLE)

# ---- the two leftovers that are the same, and the path between them --------
for cx, cy in [(C[2], 3.82), (C[4], 1.42)]:
    ax.add_patch(Circle((cx, cy), 0.30, facecolor="none",
                        edgecolor=RED, linewidth=2.2))

ax.plot([C[2] - 0.34, 2.15], [3.82, 3.82], color=RED, linewidth=2.2)
ax.plot([2.15, 2.15], [3.82, 1.42], color=RED, linewidth=2.2)
ax.annotate("", xy=(C[4] - 0.36, 1.42), xytext=(2.15, 1.42),
            arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=2.2,
                            mutation_scale=18))
ax.text(1.92, 2.62, "the same leftover, again", ha="center", va="center",
        rotation=90, fontsize=11.5, color=RED, fontweight="bold")

# ---- the explanation panel --------------------------------------------------
ax.add_patch(FancyBboxPatch((6.15, 1.20), 5.50, 5.90,
                            boxstyle="round,pad=0.04,rounding_size=0.16",
                            facecolor="#FAFAFA", edgecolor=RED, linewidth=2.0))
ax.text(6.50, 6.70, "Why it never stops", ha="left", va="center",
        fontsize=17, color=RED, fontweight="bold")

LINES = [
    ("After the ones, $1$ was left over.", INK),
    ("", INK),
    (r"Bring down a $0$: the working number is $10$.", GREEN),
    (r"$11$ does not fit into $10$, so the quotient", BLUE),
    (r"digit is $0$, and $10$ is still left.", PURPLE),
    ("", INK),
    (r"Bring down a $0$: the working number is $100$.", GREEN),
    (r"$11$ fits into $100$ nine times, and", BLUE),
    (r"$9 \times 11 = 99$, so $100 - 99 = 1$ is left.", PURPLE),
    ("", INK),
    (r"That $1$ is exactly where we were two", RED),
    (r"steps ago. Nothing else has changed, so", RED),
    (r"the next two digits are $0$ and $9$ again -", RED),
    ("and again, and again, for ever.", RED),
]
for i, (text, colour) in enumerate(LINES):
    ax.text(6.50, 6.20 - i * 0.345, text, ha="left", va="center",
            fontsize=13, color=colour)

# ---- the answer -------------------------------------------------------------
ax.text(W / 2, 0.52, r"$397 \div 11 = 36.0909\ldots = 36.\overline{09}$",
        ha="center", va="center", fontsize=22, color=INK, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_08_repeating_remainder.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
