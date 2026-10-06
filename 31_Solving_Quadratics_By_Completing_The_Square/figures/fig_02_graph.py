"""Figure 2 - the picture of x^2 + 2x - 6.

The curve y = x^2 + 2x - 6 for x from -5 to 3, with the whole-number points of
the value table as dots, the lowest point (-1, -7), the dashed line x = -1
down the middle, and the two crossing points -1 - sqrt(7) and -1 + sqrt(7).

Colours: blue curve and table dots, purple lowest point and middle line,
green crossing points (the solutions).

Run with:  python figures/fig_02_graph.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
BLUE = "#2E86DE"
PURPLE = "#8E44AD"
GREEN = "#1E8449"

f = lambda x: x**2 + 2 * x - 6                     # the expression we solve
r = np.sqrt(7)                                     # distance of each answer from -1

fig, ax = plt.subplots(figsize=(10, 9))

xs = np.linspace(-5.2, 3.2, 400)                   # smooth curve
ax.plot(xs, f(xs), color=BLUE, lw=3)
xi = np.arange(-5, 4)                              # the table's whole numbers
ax.plot(xi, f(xi), "o", color=BLUE, ms=8)

ax.axhline(0, color=INK, lw=1.4)                   # the "value 0" line
ax.axvline(0, color=GREY, lw=1)                    # x = 0, for reference

ax.axvline(-1, color=PURPLE, lw=2, ls="--")        # middle line x = -1
ax.plot([-1], [-7], "o", color=PURPLE, ms=13)      # lowest point
ax.annotate(r"lowest point $(-1,\ -7)$", xy=(-1, -7), xytext=(0.0, -7.6),
            fontsize=16, color=PURPLE,
            arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.6))

for x0, lab, dx in [(-1 - r, r"$-1 - \sqrt{7} \approx -3.65$", -3.9),
                    (-1 + r, r"$-1 + \sqrt{7} \approx 1.65$", -0.3)]:
    ax.plot([x0], [0], "o", color=GREEN, ms=14)    # crossing point = solution
    ty = 3.0 if dx < -2 else 5.6                   # right label higher, off the curve
    ax.annotate(lab, xy=(x0, 0), xytext=(dx, ty), fontsize=16, color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.6))

# the two equal distances from the middle line
ax.annotate("", xy=(-1 - r, -1.2), xytext=(-1, -1.2),
            arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.6))
ax.annotate("", xy=(-1 + r, -1.2), xytext=(-1, -1.2),
            arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.6))
ax.text(-1 - r / 2, -2.0, r"$\sqrt{7}$", ha="center", fontsize=16, color=GREEN)
ax.text(-1 + r / 2, -2.0, r"$\sqrt{7}$", ha="center", fontsize=16, color=GREEN)

ax.set_xlim(-5.5, 3.5)
ax.set_ylim(-8.5, 10)
ax.set_xticks(range(-5, 4))
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"value of $x^{2} + 2x - 6$", fontsize=16)
ax.set_title(r"$x^{2} + 2x - 6$ for $x$ from $-5$ to $3$", fontsize=18)
ax.tick_params(labelsize=13)
ax.grid(alpha=0.25)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_graph.png", dpi=160, bbox_inches="tight",
            facecolor="white")
print("wrote", out / "fig_02_graph.png")
