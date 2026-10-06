"""Figure 3 - the candidates and the solutions of 2x^3 + 3x^2 - 3x - 2 = 0.

The rational roots test gives six candidates: -2, -1, -1/2, 1/2, 1, 2.
They are drawn as hollow grey circles on the zero line. The curve crosses the
line at three of them (-2, -1/2, 1), drawn as filled green dots. At the other
three the curve misses the line; a dotted grey stick shows the value there.

Colours: blue curve, green solutions, grey candidates that fail.

Run with:  python figures/fig_03_cubic_graph.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
BLUE = "#2E86DE"
GREEN = "#1E8449"


def f(x):                                          # the cubic
    return 2 * x**3 + 3 * x**2 - 3 * x - 2


fig, ax = plt.subplots(figsize=(11, 8))

xs = np.linspace(-2.6, 1.75, 500)                  # smooth curve
ax.plot(xs, f(xs), color=BLUE, lw=3)
ax.axhline(0, color=INK, lw=1.4)                   # the "value 0" line
ax.axvline(0, color=GREY, lw=1)                    # x = 0, for reference

cands = [-2, -1, -0.5, 0.5, 1, 2]                  # from the test
names = {-2: r"$-2$", -1: r"$-1$", -0.5: r"$-\frac{1}{2}$",
         0.5: r"$\frac{1}{2}$", 1: r"$1$", 2: r"$2$"}
for c in cands:
    v = f(c)
    if abs(v) < 1e-12:                             # a real solution
        ax.plot([c], [0], "o", color=GREEN, ms=14, zorder=5)
        left = c == -0.5                           # free corner: below-left
        ax.text(c - 0.06 if left else c + 0.06, -0.5, names[c],
                ha="right" if left else "left", va="top", fontsize=18,
                color=GREEN, fontweight="bold")
    else:                                          # a candidate that fails
        ax.plot([c], [0], "o", mfc="white", mec=GREY, mew=2.2, ms=13,
                zorder=5)
        below = v > 0                              # label on the free side
        ax.text(c, -0.7 if below else 0.7, names[c], ha="center",
                va="top" if below else "bottom", fontsize=17, color=GREY)
        if abs(v) < 12:                            # stick up to the curve
            ax.plot([c, c], [0, v], ls=":", color=GREY, lw=2)

ax.text(2.0, 1.0, r"value $20$," + "\n" + "off the top",
        ha="center", va="bottom", fontsize=13, color=GREY)

ax.set_xlim(-2.8, 2.3)
ax.set_ylim(-8, 11)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"value of $2x^{3} + 3x^{2} - 3x - 2$", fontsize=15)
ax.set_title("six candidates (circles), three solutions (green)",
             fontsize=18)
ax.tick_params(labelsize=13)
ax.grid(alpha=0.25)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_cubic_graph.png", dpi=160, bbox_inches="tight",
            facecolor="white")
print("wrote", out / "fig_03_cubic_graph.png")
