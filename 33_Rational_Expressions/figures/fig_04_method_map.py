"""Figure 4 - which steps for which task.

A box at the top asks "What must you do?". Five arrows lead to five columns:
simplify, multiply, divide, add or subtract, rationalize. Under each heading,
its numbered steps. Below the first four columns, one long bar: write the
excluded values next to the answer.

Colours: slate for steps the book already had, blue for steps new in this
chapter, green for the closing bar.

Run with:  python figures/fig_04_method_map.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
SLATE = "#5D6D7E"
BLUE = "#2E86DE"
GREEN = "#1E8449"

# (heading, list of steps) for each column
cols = [
    ("Simplify", ["1. Factor the top", "2. Factor the bottom",
                  "3. Cancel common\n    factors"]),
    ("Multiply", ["1. Factor every top\n    and bottom", "2. Cancel any top\n    against any bottom",
                  "3. Multiply what\n    is left"]),
    ("Divide", ["1. Keep, change, flip", "2. Factor everything", "3. Cancel, then\n    multiply",
                "4. Also exclude the\n    zeros of the top\n    you flipped"]),
    ("Add or subtract", ["1. Factor the bottoms;\n    find the LCD", "2. Give every fraction\n    the LCD",
                         "3. Combine the tops\n    (brackets for minus)", "4. Simplify if you can"]),
    ("Rationalize", ["One root $\\sqrt{a}$:\n  multiply by $\\dfrac{\\sqrt{a}}{\\sqrt{a}}$",
                     "Two terms $a - \\sqrt{b}$:\n  multiply by the\n  conjugate $a + \\sqrt{b}$"]),
]

fig, ax = plt.subplots(figsize=(18, 10.5))
ax.set_xlim(0, 18)
ax.set_ylim(0, 10.5)
ax.axis("off")

# the question box at the top
ax.add_patch(FancyBboxPatch((6.5, 9.3), 5.0, 0.9, boxstyle="round,pad=0.08",
                            facecolor=SLATE, alpha=0.12, edgecolor=SLATE, lw=2.5))
ax.text(9.0, 9.75, "What must you do?", ha="center", va="center",
        fontsize=20, color=SLATE, fontweight="bold")

W, GAP = 3.25, 0.35                                # column width and gap
for i, (head, steps) in enumerate(cols):
    x0 = 0.2 + i * (W + GAP)                       # left edge of this column
    xc = x0 + W / 2
    col = BLUE if head == "Rationalize" else SLATE
    ax.add_patch(FancyArrowPatch((9.0, 9.2), (xc, 8.35), arrowstyle="-|>",
                                 mutation_scale=20, color=GREY, lw=2))
    ax.add_patch(FancyBboxPatch((x0, 7.5), W, 0.8, boxstyle="round,pad=0.06",
                                facecolor=BLUE, alpha=0.15, edgecolor=BLUE, lw=2.5))
    ax.text(xc, 7.9, head, ha="center", va="center", fontsize=18,
            color=BLUE, fontweight="bold")
    y = 6.9                                        # top of the first step
    for s in steps:
        n = s.count("\n") + 1                      # lines in this step
        h = 0.42 * n + 0.35 + (0.35 if "dfrac" in s else 0)
        ax.add_patch(FancyBboxPatch((x0 + 0.05, y - h), W - 0.1, h,
                                    boxstyle="round,pad=0.05", facecolor="white",
                                    edgecolor=col, lw=1.6))
        ax.text(x0 + 0.2, y - h / 2, s, ha="left", va="center", fontsize=14,
                color=INK, linespacing=1.35)
        y -= h + 0.25

# closing bar under the four fraction columns
bar_w = 4 * W + 3 * GAP
ax.add_patch(FancyBboxPatch((0.2, 0.3), bar_w, 0.85, boxstyle="round,pad=0.06",
                            facecolor=GREEN, alpha=0.12, edgecolor=GREEN, lw=2.5))
ax.text(0.2 + bar_w / 2, 0.72,
        "Always: no bottom may be $0$. Write the excluded values next to the answer.",
        ha="center", va="center", fontsize=16, color=GREEN, fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_04_method_map.png", dpi=160, bbox_inches="tight",
            facecolor="white")
print("wrote", out / "fig_04_method_map.png")
