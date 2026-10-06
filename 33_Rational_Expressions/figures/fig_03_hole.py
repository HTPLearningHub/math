"""Figure 3 - (x^3 + x^2) / (x + 1) is x^2 with one point missing.

The values of (x^3 + x^2) / (x + 1) for x from -3 to 2.5 lie on the curve of
x^2, except at x = -1, where the bottom is 0 and there is no value. That
point (-1, 1) is drawn as a hollow circle. A few whole-number points are
marked with dots and both expressions give the same value there.

Colours: blue curve and dots, red hollow circle for the missing point.

Run with:  python figures/fig_03_hole.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

INK = "#212121"
GREY = "#78909C"
BLUE = "#2E86DE"
RED = "#C0392B"

f = lambda x: (x**3 + x**2) / (x + 1)              # the rational expression

fig, ax = plt.subplots(figsize=(10, 8))

xs = np.linspace(-3.0, 2.5, 600)
xs = xs[np.abs(xs + 1) > 1e-9]                     # never divide by 0
ax.plot(xs, f(xs), color=BLUE, lw=3)

xi = np.array([-3, -2, 0, 1, 2])                   # whole numbers, -1 left out
ax.plot(xi, f(xi), "o", color=BLUE, ms=9)
for x0 in xi:                                      # label each dot with its value
    ax.text(x0 + 0.12, f(x0) + 0.25, f"${int(f(x0))}$", fontsize=14, color=BLUE)

ax.plot([-1], [1], "o", ms=15, mfc="white", mec=RED, mew=3)   # the hole
ax.annotate("no value at $x = -1$:\n" r"the bottom $x + 1$ is $0$ there",
            xy=(-1, 1), xytext=(-0.75, 5.6), fontsize=16, color=RED,
            arrowprops=dict(arrowstyle="->", color=RED, lw=1.8))

ax.axhline(0, color=INK, lw=1.2)                   # the zero line
ax.axvline(0, color=GREY, lw=1)

ax.set_xlim(-3.3, 2.8)
ax.set_ylim(-0.8, 9.8)
ax.set_xticks(range(-3, 3))
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"value of $\dfrac{x^{3} + x^{2}}{x + 1}$", fontsize=16)
ax.set_title(r"$\dfrac{x^{3} + x^{2}}{x + 1}$ is the curve of $x^{2}$ with one point missing",
             fontsize=17, pad=16)
ax.tick_params(labelsize=13)
ax.grid(alpha=0.25)

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_hole.png", dpi=160, bbox_inches="tight",
            facecolor="white")
print("wrote", out / "fig_03_hole.png")
