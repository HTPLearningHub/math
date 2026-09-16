"""Figure 1 - one expression, two roads, two different answers.

This is the problem the whole chapter exists to solve. The same four
operations are worked in two sensible-looking orders and the results are
nowhere near each other, so "just start somewhere" cannot be the rule.

Both roads are drawn in red, because both of them are wrong. The point of
the picture is not that one road beats the other. It is that a rule has to
come from outside the expression.
Run with:  python figures/fig_01_two_answers.py
"""

import matplotlib
matplotlib.use("Agg")                          # no window, just a file
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

RED = "#C0392B"
GREY = "#78909C"
INK = "#212121"

W, H = 11.4, 7.7
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                  # 1 unit on the axes = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

# ---- the expression both roads start from -------------------------------
ax.text(W / 2, H - 0.42, "One expression",
        ha="center", va="center", fontsize=19, color=INK, fontweight="bold")
ax.text(W / 2, H - 1.08, r"$5 \times 3 + 4 - 2 \times 6$",
        ha="center", va="center", fontsize=30, color=INK)

# ---- the two columns ----------------------------------------------------
COLS = (2.95, 8.45)                            # middle of the left / right column
TOP = H - 1.95                                 # where the first step line sits
STEP = 0.62                                    # gap between two step lines

ROADS = [
    ("Road A: work from the left",
     [r"$5 \times 3 = 15$",
      r"$15 + 4 = 19$",
      r"$19 - 2 = 17$",
      r"$17 \times 6 = 102$"],
     r"$102$"),
    ("Road B: work from the right",
     [r"$2 \times 6 = 12$",
      r"$4 - 12 = -8$",
      r"$3 + (-8) = -5$",
      r"$5 \times (-5) = -25$"],
     r"$-25$"),
]

for cx, (title, steps, answer) in zip(COLS, ROADS):
    # the pale panel that holds one road
    ax.add_patch(FancyBboxPatch((cx - 2.45, TOP - 3.92), 4.90, 4.40,
                                boxstyle="round,pad=0.06,rounding_size=0.16",
                                facecolor="#FBECEA", edgecolor=RED, linewidth=1.6))
    ax.text(cx, TOP, title, ha="center", va="center",
            fontsize=15.5, color=RED, fontweight="bold")
    for i, s in enumerate(steps):
        y = TOP - 0.70 - i * STEP
        # the small step number, kept quiet so the sum itself reads first
        ax.text(cx - 2.10, y, f"{i + 1}.", ha="left", va="center",
                fontsize=12.5, color=GREY)
        ax.text(cx - 1.60, y, s, ha="left", va="center",
                fontsize=19, color=INK)
    # the answer, on its own line below a dividing rule inside the panel.
    # the word and the number share the line, so neither sits on the rule
    ax.plot([cx - 2.10, cx + 2.10], [TOP - 2.98, TOP - 2.98],
            color=RED, linewidth=1.0, linestyle=(0, (4, 3)))
    ax.text(cx - 2.06, TOP - 3.46, "answer", ha="left", va="center",
            fontsize=13.5, color=GREY)
    ax.text(cx + 0.72, TOP - 3.46, answer, ha="center", va="center",
            fontsize=27, color=RED, fontweight="bold")

# ---- the closing sentence ----------------------------------------------
ax.text(W / 2, 0.98,
        "Same numbers. Same signs. Nothing was miscalculated.",
        ha="center", va="center", fontsize=15.5, color=INK)
ax.text(W / 2, 0.48,
        "Only the order changed, and the two answers are not even close.",
        ha="center", va="center", fontsize=16.5, color=RED, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_two_answers.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
