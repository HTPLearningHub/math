"""Figure 3 - the one question to ask before handing out an exponent.

The source draws this as an ASCII decision tree. Here it is two panels:
what joins the pieces inside the bracket? If it is times or divide, the
exponent may be given to every piece (green). If it is plus or minus, it
may not (red). Each panel carries two worked number checks so the reader
sees the rule hold, and fail, with real numbers.

Colour convention:
    green - the exponent may be handed out
    red   - the exponent may not be handed out
    grey  - the small "check" lines under each example

Horizontal plan (x): left panel 0.40 - 6.40 (centre 3.40), right panel
    6.70 - 12.70 (centre 9.70).
Vertical plan (y): heading 6.55; panels run 0.40 - 6.00.

Run with:  python figures/fig_03_reach_test.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

GREEN = "#1E8449"
GREEN_T = "#F1F9F4"
RED = "#C0392B"
RED_T = "#FCF0EE"
GREY = "#78909C"
INK = "#212121"

W, H = 13.1, 6.95
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

ax.text(0.40, 6.55, "first ask: what joins the pieces inside the bracket?",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

panels = [
    # x_left, colour, fill, heading, verdict, rows of (example, check)
    (0.40, GREEN, GREEN_T, r"joined by $\times$ or $\div$",
     "give the exponent to every piece",
     [(r"$(2 \times 5)^{2} = 2^{2} \times 5^{2}$",
       r"check:  $10^{2} = 100$  and  $4 \times 25 = 100$"),
      (r"$\left(\frac{6}{3}\right)^{2} = \frac{6^{2}}{3^{2}}$",
       r"check:  $2^{2} = 4$  and  $\frac{36}{9} = 4$")]),
    (6.70, RED, RED_T, r"joined by $+$ or $-$",
     "do not hand it out",
     [(r"$(3 + 2)^{2} \neq 3^{2} + 2^{2}$",
       r"check:  $5^{2} = 25$  but  $9 + 4 = 13$"),
      (r"$(5 - 2)^{2} \neq 5^{2} - 2^{2}$",
       r"check:  $3^{2} = 9$  but  $25 - 4 = 21$")]),
]

for x_left, colour, fill, heading, verdict, rows in panels:
    ax.add_patch(FancyBboxPatch(
        (x_left, 0.40), 6.00, 5.60,
        boxstyle="round,pad=0.0,rounding_size=0.18",
        facecolor=fill, edgecolor=colour, linewidth=2.0, zorder=0))
    cx = x_left + 3.00                     # centre of the panel
    ax.text(cx, 5.45, heading, ha="center", va="center", fontsize=20,
            color=INK, fontweight="bold")
    ax.text(cx, 4.85, verdict, ha="center", va="center", fontsize=17,
            color=colour, fontweight="bold")
    # two worked examples, each with its check line below it
    for k, (example, check) in enumerate(rows):
        y = 3.75 - k * 1.85
        ax.text(cx, y, example, ha="center", va="center", fontsize=23,
                color=INK)
        ax.text(cx, y - 0.75, check, ha="center", va="center",
                fontsize=14, color=GREY)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_reach_test.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_03_reach_test.png")
