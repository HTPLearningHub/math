"""Figure 1 - adding two polynomials by grouping like terms.

Top: the first polynomial 4x^3 + 2x^2 - 6x + 9, as four cards.
Second row: the second polynomial x^4 - 3x^2 + 6x - 4, as four cards.
Every card is coloured by its exponent, and an arrow carries it down to the
box that collects that exponent. Third row: the five boxes, largest exponent
on the left (standard form, Chapter 27, section 6). Bottom row: what each box
becomes. The x box gives 0x, which disappears (drawn in grey).

Colour convention for this chapter (one colour per exponent):
    purple - x^4
    blue   - x^3
    teal   - x^2
    gold   - x  (exponent 1)
    orange - constant term (exponent 0)
    green  - the final answer
    grey   - labels, and a term that has disappeared

Run with:  python figures/fig_01_grouping.py
"""

import matplotlib
matplotlib.use("Agg")                              # draw to a file, no window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

INK = "#212121"
GREY = "#90A4AE"
GREEN = "#1E8449"
# exponent -> (edge colour, light fill)
COL = {
    4: ("#8E44AD", "#F3EAF8"),
    3: ("#2E86DE", "#E9F2FC"),
    2: ("#138D75", "#E6F5F1"),
    1: ("#B7950B", "#FBF5DE"),
    0: ("#E67E22", "#FDF0E3"),
}

W, H = 15.3, 8.6                                   # figure size in inches
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])                      # one data unit = one inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)


def card(xc, yc, text, exp, w=1.6, h=0.85, size=22, edge=None, fill=None,
         color=INK):
    """A rounded card centred on (xc, yc), coloured by its exponent."""
    e, f = COL[exp] if exp is not None else (edge, fill)
    ax.add_patch(FancyBboxPatch(
        (xc - w / 2, yc - h / 2), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.14",
        facecolor=f, edgecolor=e, linewidth=2.2, zorder=2))
    ax.text(xc, yc, text, ha="center", va="center", fontsize=size,
            color=color, zorder=3)


# --- rows 1 and 2: the two polynomials as written -------------------------
Y1, Y2 = 7.65, 6.25                                # heights of the two rows
xs_in = [5.3, 7.4, 9.5, 11.6]                      # card positions, reading order
first = [(r"$4x^{3}$", 3), (r"$+2x^{2}$", 2), (r"$-6x$", 1), (r"$+9$", 0)]
second = [(r"$x^{4}$", 4), (r"$-3x^{2}$", 2), (r"$+6x$", 1), (r"$-4$", 0)]

ax.text(0.25, Y1, "first", ha="left", va="center", fontsize=15,
        color=GREY, fontweight="bold")
ax.text(0.25, Y2, "plus second", ha="left", va="center", fontsize=15,
        color=GREY, fontweight="bold")
for xc, (t, e) in zip(xs_in, first):
    card(xc, Y1, t, e)
for xc, (t, e) in zip(xs_in, second):
    card(xc, Y2, t, e)

# --- row 3: one box per exponent, largest exponent on the left --------------
Y3 = 3.55                                          # height of the group boxes
xs_g = {4: 3.05, 3: 5.55, 2: 8.15, 1: 10.85, 0: 13.55}   # box centres
widths = {4: 1.7, 3: 1.7, 2: 2.6, 1: 2.6, 0: 2.3}         # box widths
inside = {4: r"$x^{4}$", 3: r"$4x^{3}$", 2: r"$2x^{2} - 3x^{2}$",
          1: r"$-6x + 6x$", 0: r"$9 - 4$"}
labels = {4: r"$x^{4}$ terms", 3: r"$x^{3}$ terms", 2: r"$x^{2}$ terms",
          1: r"$x$ terms", 0: "plain numbers"}
ax.text(0.25, Y3, "grouped by\nexponent", ha="left", va="center",
        fontsize=15, color=GREY, fontweight="bold")
for e, xc in xs_g.items():
    card(xc, Y3, inside[e], e, w=widths[e], h=0.95, size=20)
    ax.text(xc, Y3 - 0.75, labels[e], ha="center", va="center",
            fontsize=12, color=COL[e][0])

# arrows: each written card goes down to the box of its exponent
for row, y in ((first, Y1), (second, Y2)):
    for xc, (t, e) in zip(xs_in, row):
        ax.annotate("", xy=(xs_g[e], Y3 + 0.52), xytext=(xc, y - 0.45),
                    arrowprops=dict(arrowstyle="-|>", color=COL[e][0],
                                    lw=1.6, mutation_scale=16, alpha=0.55,
                                    shrinkA=0, shrinkB=0))

# --- row 4: what each box becomes -----------------------------------------
Y4 = 1.75
ax.text(0.25, Y4, "add the\ncoefficients", ha="left", va="center",
        fontsize=15, color=GREY, fontweight="bold")
results = {4: r"$x^{4}$", 3: r"$+4x^{3}$", 2: r"$-x^{2}$", 1: r"$0x$",
           0: r"$+5$"}
for e, xc in xs_g.items():
    if e == 1:                                     # the x terms cancel out
        card(xc, Y4, results[e], None, edge=GREY, fill="#F4F6F7",
             color=GREY, w=1.6)
        ax.plot([xc - 0.55, xc + 0.55], [Y4 - 0.28, Y4 + 0.28],
                color=GREY, lw=2.2, zorder=4)     # struck out: it is zero
    else:
        card(xc, Y4, results[e], e, w=1.6)
    ax.annotate("", xy=(xc, Y4 + 0.47), xytext=(xc, Y3 - 0.95),
                arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.4,
                                mutation_scale=14))

# --- the answer -----------------------------------------------------------
ax.text(W / 2 + 0.6, 0.45, r"answer:  $x^{4} + 4x^{3} - x^{2} + 5$",
        ha="center", va="center", fontsize=22, color=GREEN,
        fontweight="bold")

out = Path(__file__).resolve().parent.parent / "assets"    # ../assets
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_01_grouping.png", dpi=160,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_01_grouping.png")
