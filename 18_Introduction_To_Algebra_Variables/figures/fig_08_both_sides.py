"""Figure 8 - whatever you do to one side, do to the other, and it stays level.

Three balances, left to right, are the three lines of the solution of
9 = 2x + 1.

  1. As it arrives: 9 in the left pan, 2x + 1 in the right pan, level.
  2. One unit taken off both pans: 8 and 2x. Still level.
  3. Both pans halved: 4 and x. Still level, and the answer is now readable.

The pans are in the same order as the equation in section 7.3 - the known
number on the left, the expression holding the unknown on the right - so the
reader can read the picture and the lines of working as one thing.

Every balance is drawn with the same beam, stand and pans, so the only thing
that changes across the picture is the load. Under each one the operation that
produced it is written in orange, with "both sides" spelt out, because doing
it to one side only is the mistake this figure exists to prevent.

Vertical layout, from the top down:
  4.85  the heading
  4.15  "still level", over the second and third balance only
  3.47  the two loads and the equals sign
  3.01  the pans
  2.71  the beam, and the orange arrows between the balances
  1.85  the ground
  1.30  "step n"
  0.75  the operation that produced this balance

Run with:  python figures/fig_08_both_sides.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from pathlib import Path

BLUE = "#2E86DE"          # the side that still holds the unknown
GREEN = "#1E8449"         # the level beam, and the answer
ORANGE = "#E67E22"        # the operation done to both sides
GREY = "#78909C"
INK = "#212121"
TINT_GREY = "#ECEFF1"

W, H = 13.00, 5.20
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

BASE = 1.85                            # the ground every balance stands on
HALF = 1.10                            # half the length of the beam
PAN = 0.50                             # half the width of one pan
CENTRES = [2.35, 6.50, 10.65]
# left pan = the number we know, right pan = the side holding the unknown
LOADS = [(r"$9$", r"$2x + 1$"),
         (r"$8$", r"$2x$"),
         (r"$4$", r"$x$")]
STEPS = ["as it arrives",
         r"take $1$ off both sides",
         "halve both sides"]
STEP_COLOURS = [GREY, ORANGE, ORANGE]


def balance(cx, left_text, right_text, answer=False):
    """One level balance, loaded with left_text and right_text."""
    # the stand and the ground
    ax.add_patch(Polygon([[cx - 0.48, BASE], [cx + 0.48, BASE],
                          [cx, BASE + 0.82]],
                         closed=True, facecolor=TINT_GREY, edgecolor=GREY,
                         linewidth=1.7, zorder=2))
    ax.plot([cx - 0.82, cx + 0.82], [BASE, BASE], color=GREY, linewidth=2.3,
            zorder=2)
    beam_y = BASE + 0.86
    # the beam, level because both sides weigh the same
    ax.plot([cx - HALF, cx + HALF], [beam_y, beam_y], color=GREEN,
            linewidth=3.2, zorder=3)
    ax.plot([cx], [beam_y], marker="o", markersize=8, color=GREEN, zorder=4)
    for side in (-1, 1):
        x = cx + side * HALF
        ax.plot([x, x], [beam_y, beam_y + 0.30], color=GREY, linewidth=1.7,
                zorder=3)
        ax.plot([x - PAN, x + PAN], [beam_y + 0.30, beam_y + 0.30],
                color=GREY, linewidth=2.8, zorder=3)
    # on the last balance the known number is the answer, so it turns green
    lc = GREEN if answer else INK
    lw = "bold" if answer else "normal"
    ax.text(cx - HALF, beam_y + 0.76, left_text, ha="center", va="center",
            fontsize=22, color=lc, fontweight=lw, zorder=4)
    ax.text(cx + HALF, beam_y + 0.76, right_text, ha="center", va="center",
            fontsize=22, color=BLUE, fontweight=lw, zorder=4)
    # the equals sign is the pivot, seen from above
    ax.text(cx, beam_y + 0.76, r"$=$", ha="center", va="center", fontsize=20,
            color=GREEN, fontweight="bold", zorder=4)


ax.text(0.30, H - 0.35, r"solving   $9 = 2x + 1$", ha="left", va="center",
        fontsize=20, color=INK, fontweight="bold")

for i, (cx, (lt, rt), step, colour) in enumerate(
        zip(CENTRES, LOADS, STEPS, STEP_COLOURS)):
    balance(cx, lt, rt, answer=(i == 2))
    ax.text(cx, 1.30, f"step {i + 1}", ha="center", va="center",
            fontsize=15, color=GREY)
    ax.text(cx, 0.75, step, ha="center", va="center", fontsize=16.5,
            color=colour, fontweight="bold")
    # the beam did not tip, and that is the point of the whole figure
    if i > 0:
        ax.text(cx, 4.15, "still level", ha="center", va="center",
                fontsize=14.5, color=GREEN, style="italic")

# the arrows between the three balances, drawn at beam height in the gap
for cx_from, cx_to in zip(CENTRES[:-1], CENTRES[1:]):
    ax.annotate("", xy=(cx_to - HALF - PAN - 0.18, BASE + 0.86),
                xytext=(cx_from + HALF + PAN + 0.18, BASE + 0.86),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, linewidth=2.1,
                                shrinkA=0, shrinkB=0))

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_08_both_sides.png", dpi=170, facecolor="white")
print("saved", out / "fig_08_both_sides.png")
