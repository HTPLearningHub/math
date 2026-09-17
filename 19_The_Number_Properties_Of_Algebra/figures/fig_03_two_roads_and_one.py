"""Figure 3 - in arithmetic there are two roads; in algebra there is one.

Left panel: 4(2 + 3). The upper road adds inside the bracket first, the lower
road hands the 4 out. Both arrive at 20, so a reader may pick either.

Right panel: 4(2x + 3). The upper road is barred, because 2x and 3 cannot be
added into one term. Only the lower road is open, and that is the reason the
distributive property stops being a convenience and becomes the method.

Every x position inside a panel is measured from that panel's left edge x0,
and the widest thing in a panel reaches x0 + 5.95, so the panel needs 6.35 of
width. Two panels plus the gap fix the figure width at 13.60.

Vertical plan (y, from the top):
    5.85  the two panel headings
    4.55  the upper road's destination
    3.05  the starting card
    1.55  the lower road's destination
    0.40  the note under each panel

Run with:  python figures/fig_03_two_roads_and_one.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"
GREEN = "#1E8449"
RED = "#C0392B"
GREY = "#78909C"
INK = "#212121"
TINT_GREY = "#ECEFF1"
TINT_GREEN = "#E8F5EC"
TINT_RED = "#FCEAE8"

W, H = 13.60, 6.25
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

Y_UP = 4.55               # the "add inside first" road
Y_MID = 3.05              # the starting expression
Y_LOW = 1.55              # the "hand the multiplier out" road
CARD_H = 1.00


def card(cx, cy, w, text, face, edge, fontsize=24):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - CARD_H / 2), w, CARD_H,
                                boxstyle="round,pad=0.05,rounding_size=0.15",
                                facecolor=face, edgecolor=edge,
                                linewidth=2.3, zorder=3))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize,
            color=INK, zorder=4)


def road(x0, y0, x1, y1, colour, open_road=True):
    """One curved road out of the starting card."""
    rad = 0.22 if y1 > y0 else -0.22
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1),
                                 connectionstyle=f"arc3,rad={rad}",
                                 arrowstyle="-|>" if open_road else "-",
                                 mutation_scale=20, linewidth=2.2,
                                 color=colour, zorder=2,
                                 linestyle="solid" if open_road
                                 else (0, (5, 4))))


def panel(x0, heading, heading_colour, start_text, up_text, up_open,
          low_text, note, note_colour):
    """One half of the figure. x0 is the left edge of the panel."""
    ax.text(x0 + 3.05, 5.85, heading, ha="center", va="center", fontsize=20,
            color=heading_colour, fontweight="bold")

    card(x0 + 1.20, Y_MID, 2.20, start_text, TINT_GREY, GREY)

    up_colour = GREEN if up_open else RED
    road(x0 + 2.35, Y_MID + 0.22, x0 + (3.80 if up_open else 3.45),
         Y_UP - 0.18, up_colour, up_open)
    card(x0 + 4.90, Y_UP, 2.10, up_text,
         TINT_GREEN if up_open else TINT_RED, up_colour)
    ax.text(x0 + 3.05, 5.20, "add inside first", ha="center", va="center",
            fontsize=15, color=up_colour)

    road(x0 + 2.35, Y_MID - 0.22, x0 + 3.65, Y_LOW + 0.18, GREEN)
    card(x0 + 4.90, Y_LOW, 2.40, low_text, TINT_GREEN, GREEN)
    ax.text(x0 + 3.00, 0.95, "hand the 4 out", ha="center", va="center",
            fontsize=15, color=GREEN)

    if not up_open:
        # a thick red bar right across the end of the barred road
        bx, by = x0 + 3.45, Y_UP - 0.18
        ax.plot([bx - 0.34, bx + 0.34], [by - 0.30, by + 0.30], color=RED,
                linewidth=4.5, zorder=5)
        ax.plot([bx - 0.34, bx + 0.34], [by + 0.30, by - 0.30], color=RED,
                linewidth=4.5, zorder=5)
        # the wrong answer crossed out inside its card
        ax.plot([x0 + 4.25, x0 + 5.55], [Y_UP, Y_UP], color=RED,
                linewidth=2.6, zorder=5)
        ax.text(x0 + 4.90, Y_UP - 0.82, r"$2x$ and $3$ are unlike terms",
                ha="center", va="center", fontsize=14.5, color=RED)

    ax.text(x0 + 3.05, 0.35, note, ha="center", va="center", fontsize=15,
            color=note_colour, style="italic")


panel(0.20, "in arithmetic", GREY, r"$4(2 + 3)$", r"$4(5) = 20$", True,
      r"$8 + 12 = 20$", "both roads are open, so take whichever is easier",
      GREY)

ax.plot([6.80, 6.80], [0.70, 5.60], color=GREY, linewidth=1.3,
        linestyle=(0, (4, 4)), zorder=1)

panel(7.05, "in algebra", BLUE, r"$4(2x + 3)$", r"$2x + 3$", False,
      r"$8x + 12$", "one road is barred, so there is nothing to choose", RED)

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_03_two_roads_and_one.png", dpi=170,
            facecolor="white", bbox_inches="tight")
print("saved", out / "fig_03_two_roads_and_one.png")
