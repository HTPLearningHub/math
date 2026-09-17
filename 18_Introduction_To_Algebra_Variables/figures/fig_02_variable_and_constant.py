"""Figure 2 - a variable holds a different number each time; a constant does not.

Top row: three days of the week. The same blue letter x is drawn three times,
and each time it holds a different number of TV hours. The letter is the same
letter; what it holds changes.

Bottom row: the same three days for the number of minutes in an hour. The
orange box holds 60 on all three days, because 60 is a constant.

The two rows are deliberately identical in layout, so the only difference the
reader sees is that the top row's numbers move and the bottom row's do not.

Run with:  python figures/fig_02_variable_and_constant.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

BLUE = "#2E86DE"          # the variable
ORANGE = "#E67E22"        # the constant
GREY = "#78909C"
INK = "#212121"
TINT_BLUE = "#E9F2FC"
TINT_ORANGE = "#FDF0E3"

DAYS = ["Monday", "Tuesday", "Friday"]
HOURS = [2, 5, 0]                      # what x held on each day
MINUTES = [60, 60, 60]                 # what the constant held on each day

W, H = 12.40, 6.10
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

X_CENTRES = [4.30, 7.30, 10.30]        # one column per day
BOX_W, BOX_H = 1.55, 1.15
Y_TOP = 4.35                           # centre line of the variable row
Y_BOT = 1.55                           # centre line of the constant row
LABEL_X = 0.30                         # left edge of the row headings


def cell(cx, cy, label, value, edge, face, lab_size=19):
    """One box: the name on the lid, the number it is holding inside."""
    ax.add_patch(FancyBboxPatch((cx - BOX_W / 2, cy - BOX_H / 2),
                                BOX_W, BOX_H,
                                boxstyle="round,pad=0.05,rounding_size=0.14",
                                facecolor=face, edgecolor=edge,
                                linewidth=2.2, zorder=3))
    # the lid: the name of the thing the box stands for
    ax.text(cx, cy + 0.30, label, ha="center", va="center", fontsize=lab_size,
            color=edge, fontweight="bold", zorder=4)
    ax.plot([cx - BOX_W / 2 + 0.16, cx + BOX_W / 2 - 0.16],
            [cy + 0.09, cy + 0.09], color=edge, linewidth=1.1, zorder=4)
    # what it is holding today
    ax.text(cx, cy - 0.27, value, ha="center", va="center", fontsize=24,
            color=INK, zorder=4)


# ------------------------------------------------------------- day headings
for cx, day in zip(X_CENTRES, DAYS):
    ax.text(cx, H - 0.45, day, ha="center", va="center", fontsize=17,
            color=GREY)

# --------------------------------------------------------- the variable row
ax.text(LABEL_X, Y_TOP + 0.34, "a variable", ha="left", va="center",
        fontsize=20, color=BLUE, fontweight="bold")
ax.text(LABEL_X, Y_TOP - 0.16, "hours of TV", ha="left", va="center",
        fontsize=14.5, color=GREY)
ax.text(LABEL_X, Y_TOP - 0.60, "you watched", ha="left", va="center",
        fontsize=14.5, color=GREY)
for cx, v in zip(X_CENTRES, HOURS):
    cell(cx, Y_TOP, r"$x$", f"${v}$", BLUE, TINT_BLUE)
ax.text((X_CENTRES[0] + X_CENTRES[-1]) / 2, Y_TOP - 1.08,
        "same letter, a different number each day", ha="center", va="top",
        fontsize=15, color=BLUE, style="italic")

# --------------------------------------------------------- the constant row
ax.text(LABEL_X, Y_BOT + 0.34, "a constant", ha="left", va="center",
        fontsize=20, color=ORANGE, fontweight="bold")
ax.text(LABEL_X, Y_BOT - 0.16, "minutes in", ha="left", va="center",
        fontsize=14.5, color=GREY)
ax.text(LABEL_X, Y_BOT - 0.60, "one hour", ha="left", va="center",
        fontsize=14.5, color=GREY)
for cx, v in zip(X_CENTRES, MINUTES):
    cell(cx, Y_BOT, "minutes", f"${v}$", ORANGE, TINT_ORANGE, lab_size=14)
ax.text((X_CENTRES[0] + X_CENTRES[-1]) / 2, Y_BOT - 1.08,
        "the same number on every day, for ever", ha="center", va="top",
        fontsize=15, color=ORANGE, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_variable_and_constant.png", dpi=170,
            facecolor="white")
print("saved", out / "fig_02_variable_and_constant.png")
