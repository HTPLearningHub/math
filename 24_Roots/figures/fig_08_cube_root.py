"""Figure 8 - a cube root is the side of a cube.

Figure 1 showed a square root as the side of a square. This is the same
sentence one dimension up, and it is the reason the words "squared" and
"cubed" exist at all: 3 cubed is the number of small cubes in a box that
is 3 along, 3 across and 3 high.

The box is drawn in a simple corner view. A point (x, y, z) of the box is
put on the page at
    px = ox + (x - y) * A
    py = oy + (x + y) * B + z * C
which sends the near bottom corner to (ox, oy), the x direction up and to
the right, the y direction up and to the left, and z straight up. Only the
three faces the viewer can see are drawn, each divided into nine squares
so the 3 x 3 x 3 is countable.

Colour convention, matching figure 1:
    blue   - the box and the forward direction (cubing)
    orange - the backward direction (the cube root)

Horizontal plan (x): the box is centred on 3.20 and reaches 1.64 to 4.76.
    In the right panel the "3" card sits at 7.55, the "27" card at 11.25,
    and both arrows run between 8.25 and 10.55.

Vertical plan (y, top to bottom):
    5.85  figure heading
    4.92  the highest corner of the box
    1.50  the near bottom corner of the box
    0.75  the line under the box
    In the right panel: 4.40 the forward label, 3.90 the forward arrow,
    2.95 the two cards, 2.00 the backward arrow, 1.50 the backward label,
    0.75 the closing sentence.

Run with:  python figures/fig_08_cube_root.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch, FancyArrowPatch
from pathlib import Path

BLUE = "#2E86DE"        # the box, and cubing
ORANGE = "#E67E22"      # the cube root
GREY = "#78909C"
INK = "#212121"
BLUE_T = "#E9F2FC"      # the lit faces
BLUE_D = "#CFE3F8"      # the shaded face
ORANGE_T = "#FDF0E3"

W, H = 13.00, 6.25
fig, ax = plt.subplots(figsize=(W, H))
ax.set_position([0, 0, 1, 1])
ax.axis("off")
ax.set_xlim(0, W)
ax.set_ylim(0, H)

A, B, C = 0.52, 0.28, 0.58      # how far one unit moves the page position
OX, OY = 3.20, 1.50             # where the near bottom corner is drawn
N = 3                           # the box is N by N by N


def pt(x, y, z):
    """Put one corner of the box on the page."""
    return (OX + (x - y) * A, OY + (x + y) * B + z * C)


def face(corners, fill):
    """Fill one whole face of the box."""
    ax.add_patch(Polygon([pt(*c) for c in corners], closed=True,
                         facecolor=fill, edgecolor=BLUE, linewidth=2.0,
                         zorder=1))


def grid(fixed, kind):
    """Draw the nine squares on one face, as N-1 lines each way."""
    for i in range(1, N):
        if kind == "right":            # the face at y = 0, spanned by x, z
            ax.plot(*zip(pt(i, fixed, 0), pt(i, fixed, N)), color=BLUE,
                    linewidth=1.0, zorder=2)
            ax.plot(*zip(pt(0, fixed, i), pt(N, fixed, i)), color=BLUE,
                    linewidth=1.0, zorder=2)
        elif kind == "left":           # the face at x = 0, spanned by y, z
            ax.plot(*zip(pt(fixed, i, 0), pt(fixed, i, N)), color=BLUE,
                    linewidth=1.0, zorder=2)
            ax.plot(*zip(pt(fixed, 0, i), pt(fixed, N, i)), color=BLUE,
                    linewidth=1.0, zorder=2)
        else:                          # the top face, at z = N
            ax.plot(*zip(pt(i, 0, fixed), pt(i, N, fixed)), color=BLUE,
                    linewidth=1.0, zorder=2)
            ax.plot(*zip(pt(0, i, fixed), pt(N, i, fixed)), color=BLUE,
                    linewidth=1.0, zorder=2)


ax.text(0.40, 5.85,
        "cubing turns a side into a box of small cubes; a cube root turns "
        "the box back into the side",
        ha="left", va="center", fontsize=19, color=INK, fontweight="bold")

# ------------------------------------------------------------ the three faces
face([(0, 0, 0), (N, 0, 0), (N, 0, N), (0, 0, N)], BLUE_T)      # right face
face([(0, 0, 0), (0, N, 0), (0, N, N), (0, 0, N)], BLUE_D)      # left face
face([(0, 0, N), (N, 0, N), (N, N, N), (0, N, N)], "white")     # top face
grid(0, "right")
grid(0, "left")
grid(N, "top")

# The three measurements, one per direction. The two along the ground are
# nudged outwards; the upright one sits on the front edge itself, so it is
# given a white patch to stay readable where it crosses the edge.
ax.text(pt(1.6, 0, 0)[0] + 0.30, pt(1.6, 0, 0)[1] - 0.30, "$3$",
        ha="center", va="center", fontsize=15, color=BLUE,
        fontweight="bold")
ax.text(pt(0, 1.6, 0)[0] - 0.30, pt(0, 1.6, 0)[1] - 0.30, "$3$",
        ha="center", va="center", fontsize=15, color=BLUE,
        fontweight="bold")
ax.text(pt(0, 0, 1.5)[0], pt(0, 0, 1.5)[1], "$3$", ha="center",
        va="center", fontsize=15, color=BLUE, fontweight="bold", zorder=4,
        bbox=dict(boxstyle="round,pad=0.14", facecolor="white",
                  edgecolor="none"))

ax.text(3.20, 0.75, "$3$ along, $3$ across, $3$ high: $27$ small cubes",
        ha="center", va="center", fontsize=15, color=INK)

# ================================================================ right panel
ax.add_patch(FancyBboxPatch(
    (6.20, 0.45), 6.40, 5.10,
    boxstyle="round,pad=0.0,rounding_size=0.18",
    facecolor="white", edgecolor=ORANGE, linewidth=1.8, zorder=0))

for x, text, edge, fill in ((7.55, "$3$", BLUE, BLUE_T),
                            (11.25, "$27$", ORANGE, ORANGE_T)):
    ax.text(x, 2.95, text, ha="center", va="center", fontsize=26, color=INK,
            zorder=3,
            bbox=dict(boxstyle="round,pad=0.42", facecolor=fill,
                      edgecolor=edge, linewidth=2.0))

ax.add_patch(FancyArrowPatch((8.25, 3.90), (10.55, 3.90), arrowstyle="-|>",
                             mutation_scale=24, linewidth=3.0, color=BLUE,
                             zorder=2))
ax.text(9.40, 4.42, "cube it", ha="center", va="center", fontsize=16,
        color=BLUE, fontweight="bold")
ax.text(9.40, 3.57, r"$3^{3} = 3 \times 3 \times 3 = 27$", ha="center",
        va="center", fontsize=15, color=BLUE)

ax.add_patch(FancyArrowPatch((10.55, 2.00), (8.25, 2.00), arrowstyle="-|>",
                             mutation_scale=24, linewidth=3.0, color=ORANGE,
                             zorder=2))
ax.text(9.40, 2.37, r"$\sqrt[3]{27} = 3$", ha="center", va="center",
        fontsize=15, color=ORANGE)
ax.text(9.40, 1.52, "take the cube root", ha="center", va="center",
        fontsize=16, color=ORANGE, fontweight="bold")

ax.text(9.40, 0.78, "the little $3$ says: three of them multiplied together",
        ha="center", va="center", fontsize=13, color=GREY, style="italic")

out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
fig.savefig(out / "fig_08_cube_root.png", dpi=170,
            bbox_inches="tight", facecolor="white")
print("wrote", out / "fig_08_cube_root.png")
