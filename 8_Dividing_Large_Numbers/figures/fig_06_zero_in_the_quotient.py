"""Figure 6 - what happens when the zero is left out of the quotient.

Both panels divide 625 by 3. On the left the writer noticed that 3 does not go
into 2, skipped it, and wrote nothing. Their two digits then slide one place to
the right: the 2 that should mean two hundreds now means two tens, and the
answer reads 28. On the right the 0 is written, every digit keeps its place,
and the answer reads 208 with 1 left over.

The check underneath each panel is the same check both times, and it is the
reason the mistake is catchable without being told: multiply the answer by the
divisor, add the leftover, and see whether you come back to 625.

Red is the wrong method and green is the right one - the same pairing as
Chapter 2 fig_07, Chapter 5 fig_03 and Chapter 7 fig_05.
Run with:  python figures/fig_06_zero_in_the_quotient.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

RED = "#C0392B"         # the wrong way
GREEN = "#1E8449"       # the right way
GREY = "#78909C"
INK = "#212121"
FONT = "DejaVu Sans"    # a plain, unmarked zero

W, H = 12.2, 5.80
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])       # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

FS = 34
PW = 5.70                           # panel width


def panel(x0, colour, title, quotient, tail, check, verdict):
    """Draw one 625-divided-by-3 panel: heading, tableau, check, verdict.

    quotient is a list of (column index, character) pairs, so the wrong panel
    can put its two digits in the tens and ones columns.
    """
    ax.add_patch(FancyBboxPatch((x0, 0.30), PW, 5.20,
                                boxstyle="round,pad=0.04,rounding_size=0.16",
                                facecolor="#FAFAFA", edgecolor=colour,
                                linewidth=2.2))
    cx = x0 + PW / 2
    cols = [cx - 0.72, cx, cx + 0.72]
    ax.text(cx, 5.08, title, ha="center", va="center",
            fontsize=16, color=colour, fontweight="bold")

    # place names, so the reader can see which place each digit is standing in
    for x, place in zip(cols, ["hundreds", "tens", "ones"]):
        ax.text(x, 4.52, place, ha="center", va="center",
                fontsize=11.5, color=GREY, fontweight="bold")
    ax.plot([cols[0] - 0.40, cols[2] + 0.40], [4.30, 4.30],
            color=GREY, linewidth=1.0)

    # the quotient, then the bracket, the divisor and the dividend
    for col, ch in quotient:
        ax.text(cols[col], 3.86, ch, ha="center", va="center",
                fontsize=FS, family=FONT, color=colour, fontweight="bold")
    ax.plot([cols[0] - 0.52, cols[2] + 0.34], [3.46, 3.46],
            color=INK, linewidth=2.4)
    ax.plot([cols[0] - 0.52, cols[0] - 0.52], [3.46, 2.72],
            color=INK, linewidth=2.4)
    ax.text(cols[0] - 0.88, 3.06, "3", ha="center", va="center",
            fontsize=FS, family=FONT, color=INK)
    for x, ch in zip(cols, "625"):
        ax.text(x, 3.06, ch, ha="center", va="center",
                fontsize=FS, family=FONT, color=INK)
    if tail:
        # under the tableau, not beside it: beside it would run off the panel
        ax.text(cx, 2.56, tail, ha="center", va="center",
                fontsize=14, color=colour, fontweight="bold")

    # the check, and what it tells you
    ax.text(cx, 2.10, "Check it:", ha="center", va="center",
            fontsize=13.5, color=GREY, fontweight="bold")
    ax.text(cx, 1.58, check, ha="center", va="center",
            fontsize=17, color=INK)
    ax.text(cx, 0.82, verdict, ha="center", va="center",
            fontsize=14.5, color=colour, fontweight="bold", linespacing=1.5)


panel(0.30, RED, "The zero was skipped",
      [(1, "2"), (2, "8")], None,
      r"$28 \times 3 = 84$",
      "$84$ is nowhere near $625$.\n"
      "The $2$ slid out of the hundreds into the tens.")

panel(6.20, GREEN, "The zero holds the place",
      [(0, "2"), (1, "0"), (2, "8")], "with $1$ left over",
      r"$(208 \times 3) + 1 = 624 + 1 = 625$",
      "Back to the number we started with.\n"
      "Every digit stayed in its own place.")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_06_zero_in_the_quotient.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
