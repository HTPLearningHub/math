"""Figure 2 - the picture of x^4 + x^3 - 11x^2 - 5x + 30.

The curve crosses the zero line four times: at -3, -sqrt(5), 2 and sqrt(5).
The last two are very close, so a small zoomed window shows that the curve
really dips below zero between 2 and sqrt(5) = 2.236...

Colours: blue curve, green solutions (as in Chapter 31, fig_02).

Run with:  python figures/fig_02_quartic_graph.py
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


def f(x):                                          # the quartic
    return x**4 + x**3 - 11 * x**2 - 5 * x + 30


r5 = np.sqrt(5)                                    # 2.236...

fig, ax = plt.subplots(figsize=(11, 8))

xs = np.linspace(-3.85, 3.2, 600)                  # smooth curve
ax.plot(xs, f(xs), color=BLUE, lw=3)
ax.axhline(0, color=INK, lw=1.4)                   # the "value 0" line
ax.axvline(0, color=GREY, lw=1)                    # x = 0, for reference

# the four solutions, with labels placed so they do not overlap
sols = [(-3, r"$-3$", (-3.75, 9)),
        (-r5, r"$-\sqrt{5} \approx -2.24$", (-2.2, 12)),
        (2, r"$2$", (1.2, -8)),
        (r5, r"$\sqrt{5} \approx 2.24$", (2.3, -9))]
for x0, lab, (tx, ty) in sols:
    ax.plot([x0], [0], "o", color=GREEN, ms=12)    # crossing point = solution
    ax.annotate(lab, xy=(x0, 0), xytext=(tx, ty), fontsize=16, color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.5))

ax.set_xlim(-4, 3.4)
ax.set_ylim(-12, 60)                               # room above for the window
ax.set_xticks(range(-4, 4))
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"value of $x^{4} + x^{3} - 11x^{2} - 5x + 30$", fontsize=15)
ax.set_title(r"$x^{4} + x^{3} - 11x^{2} - 5x + 30$: four crossings",
             fontsize=18)
ax.tick_params(labelsize=13)
ax.grid(alpha=0.25)

# zoomed window around 2 and sqrt(5)
ins = ax.inset_axes([0.33, 0.62, 0.3, 0.3])         # [left, bottom, w, h]
zx = np.linspace(1.9, 2.33, 300)
ins.plot(zx, f(zx), color=BLUE, lw=2.5)
ins.axhline(0, color=INK, lw=1.2)
ins.plot([2, r5], [0, 0], "o", color=GREEN, ms=9)
ins.set_xlim(1.9, 2.33)
ins.set_ylim(-0.6, 1.0)
ins.set_xticks([2, r5])
ins.set_xticklabels([r"$2$", r"$\sqrt{5}$"], fontsize=13)
ins.set_yticks([0])
ins.set_title("close up", fontsize=13, color=GREY)
ins.grid(alpha=0.25)
ax.indicate_inset_zoom(ins, edgecolor=GREY)        # box + lines to the window

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_02_quartic_graph.png", dpi=160, bbox_inches="tight",
            facecolor="white")
print("wrote", out / "fig_02_quartic_graph.png")
