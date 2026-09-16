"""Figure 1 - three everyday scales that carry on below zero.

The point of the picture is that zero is not the bottom of the world. In all
three panels the same two things are drawn: a grey dashed line at zero, and an
orange marker sitting underneath it. Only the story changes - temperature,
money, depth.

Colours follow the chapter convention:
    blue   - the positive side, above zero
    orange - the negative side, below zero
    grey   - zero itself, and the scale
Run with:  python figures/fig_01_below_zero.py
"""

import matplotlib
matplotlib.use("Agg")                      # draw to a file, never to a window
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from pathlib import Path

BLUE = "#2E86DE"        # above zero
ORANGE = "#E67E22"      # below zero
GREY = "#78909C"        # the scale and zero
PALE = "#FAFAFA"        # panel background
WATER = "#D6EAF8"       # the sea in panel three
INK = "#212121"

W, H = 13.2, 5.6
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])              # axes fills the figure: 1 unit = 1 inch
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

PANEL_W = 4.0                              # width of one panel
PANEL_Y0, PANEL_Y1 = 0.30, 5.10            # bottom and top of every panel
SCALE_Y0, SCALE_Y1 = 1.05, 4.05            # bottom and top of the vertical scale


def panel(x0, title, lo, hi, ticks, value, value_label, story, water=False,
          bar=False, bulb=False):
    """Draw one panel: a frame, a vertical scale, zero, and one orange marker.

    x0          left edge of the panel, in inches
    lo, hi      the smallest and largest number on the scale
    ticks       the numbers that get a tick and a label
    value       the number the orange marker points at
    """
    ax.add_patch(FancyBboxPatch((x0, PANEL_Y0), PANEL_W, PANEL_Y1 - PANEL_Y0,
                                boxstyle="round,pad=0.04,rounding_size=0.16",
                                facecolor=PALE, edgecolor=GREY, linewidth=1.6))
    cx = x0 + 1.55                          # the scale sits left of centre
    ax.text(x0 + PANEL_W / 2, 4.70, title, ha="center", va="center",
            fontsize=16, color=INK, fontweight="bold")

    def y_of(v):
        """Turn a number on the scale into a height in inches."""
        return SCALE_Y0 + (v - lo) / (hi - lo) * (SCALE_Y1 - SCALE_Y0)

    y0 = y_of(0)

    if water:                               # panel three: fill the sea in blue
        ax.add_patch(Rectangle((x0 + 0.22, SCALE_Y0), PANEL_W - 0.44, y0 - SCALE_Y0,
                               facecolor=WATER, edgecolor="none", zorder=1))
    if bulb:                                # panel one: the thermometer tube
        ax.add_patch(Rectangle((cx - 0.13, SCALE_Y0), 0.26, SCALE_Y1 - SCALE_Y0,
                               facecolor="white", edgecolor=GREY,
                               linewidth=1.4, zorder=2))
        ax.add_patch(Rectangle((cx - 0.13, y_of(value)), 0.26, y0 - y_of(value),
                               facecolor=ORANGE, edgecolor="none", zorder=3))
    if bar:                                 # panel two: the money bar
        ax.add_patch(Rectangle((cx - 0.26, y_of(value)), 0.52, y0 - y_of(value),
                               facecolor=ORANGE, edgecolor="none", zorder=3))

    # the scale itself, drawn as a thin grey line with short ticks
    ax.plot([cx, cx], [SCALE_Y0, SCALE_Y1], color=GREY, linewidth=1.6, zorder=4)
    for t in ticks:
        colour = GREY if t == 0 else (BLUE if t > 0 else ORANGE)
        weight = "bold" if t == 0 else "normal"
        ax.plot([cx - 0.10, cx + 0.10], [y_of(t)] * 2,
                color=colour, linewidth=1.6, zorder=5)
        ax.text(cx - 0.26, y_of(t), rf"${t}$", ha="right", va="center",
                fontsize=12.5, color=colour, fontweight=weight, zorder=5)

    # zero, as a dashed line straight across the panel
    ax.plot([x0 + 0.22, x0 + PANEL_W - 0.22], [y0, y0],
            color=GREY, linewidth=1.6, linestyle=(0, (5, 4)), zorder=6)
    ax.text(x0 + PANEL_W - 0.30, y0 + 0.20, "zero", ha="right", va="bottom",
            fontsize=12, color=GREY, fontweight="bold", zorder=6)

    # the orange marker and its label; it must stop short of the orange bar
    head = cx + (0.34 if bar else 0.16)
    ax.annotate("", xy=(head, y_of(value)), xytext=(cx + 1.05, y_of(value)),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, linewidth=2.4,
                                mutation_scale=18), zorder=7)
    ax.text(cx + 1.15, y_of(value), value_label, ha="left", va="center",
            fontsize=15, color=ORANGE, fontweight="bold", zorder=7)

    ax.text(x0 + PANEL_W / 2, 0.62, story, ha="center", va="center",
            fontsize=12.5, color=INK, linespacing=1.5)


panel(0.20, "Temperature", -10, 10, [-10, -5, 0, 5, 10],
      -5, r"$-5\,^{\circ}\mathrm{C}$",
      "Five degrees colder\nthan freezing point.", bulb=True)

panel(4.60, "Bank balance", -20, 20, [-20, -10, 0, 10, 20],
      -10, r"$-10$",
      "You owe the bank ten.\nYou must pay ten to reach zero.", bar=True)

panel(9.00, "Depth", -6, 6, [-6, -3, 0, 3, 6],
      -3, r"$-3\ \mathrm{m}$",
      "Three metres under\nthe surface of the sea.", water=True)

out = Path(__file__).resolve().parent.parent / "assets" / "fig_01_below_zero.png"
fig.savefig(out, dpi=200, bbox_inches="tight")
print("saved:", out)
