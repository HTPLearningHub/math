# Chapter 31 - Solving quadratic equations by completing the square

File: [31_Solving_Quadratics_By_Completing_The_Square/31_Solving_Quadratics_By_Completing_The_Square.md](./../31_Solving_Quadratics_By_Completing_The_Square/31_Solving_Quadratics_By_Completing_The_Square.md)

One new idea: **add $\left(\frac{b}{2}\right)^{2}$ to make the left side a bracket squared**, then
finish with Ch. 24 § 8.1's $\pm$ root. Everything else is linked: $(a+b)^{2}$ (Ch. 25 § 3.3),
power of a fraction (Ch. 25 § 2.3), quotient property of roots (Ch. 24 § 4.5), irrational /
exact symbol (Ch. 24 §§ 3.2-3.3), no solution for a negative square (Ch. 24 § 8.3), properties of
equality (Ch. 20 § 2.2), common denominators (Ch. 15 § 3), area (Ch. 6 § 3.1), factoring and
standard form (Ch. 30).

Running example: $x^{2} + 2x - 6 = 0 \to (x + 1)^{2} = 7 \to x = -1 \pm \sqrt{7}$
(§§ 1.1, 4.2, 6, fig_02).

## Sections

| Section | Contains |
| --- | --- |
| 1. When factoring does not work | 1.1 pair table for $x^{2}+2x-6$, no sum $2$; 1.2 $(x+3)^{2} = 16 \to 1, -7$, bracket as one number; 1.3 the plan |
| 2. Perfect square trinomials | 2.1 $(x+d)^{2} = x^{2}+2dx+d^{2}$ from Ch. 25; 2.2 definition, test "half of middle, squared = last", 3-row table; 2.3 $(x-2)^{2} = x^{2}-4x+4$, last number never negative; 2.4 $x^{2}+bx+\left(\frac{b}{2}\right)^{2} = \left(x+\frac{b}{2}\right)^{2}$, symbol list, Note: needs exactly $x^{2}$ |
| 3. Why the name | fig_01, $x^{2}+6x$, two $3x$ strips, missing $3 \times 3$ corner |
| 4. $a = 1$ | 4.1 $x^{2}+6x-7 \to 1, -7$, seven steps, cross-check with $(x+7)(x-1)$; 4.2 $x^{2}+2x-6 \to -1 \pm \sqrt{7} \approx 1.65, -3.65$, exact check (roots cancel); 4.3 $x^{2}+5x+3 \to \frac{-5 \pm \sqrt{13}}{2}$, $-3 = -\frac{12}{4}$, Note: keep fractions |
| 5. $a \neq 1$ | 5.1 why divide: $2x^{2}+8x+16$ vs $(x+4)^{2}$ at $x=1$: $26 \neq 25$; then $1, -5$; 5.2 $2x^{2}-8x-10 \to 5, -1$ |
| 6. Picture | 6.1 value table $x = -5 \ldots 3$, graph defined, fig_02; 6.2 solutions = crossings, lowest point from $(x+1)^{2} - 7$, mirror pair; names parabola, vertex, axis of symmetry |
| 7. Method + traps | 7.1 fig_03 seven steps; 7.2 one side only; 7.3 forgetting $\pm$; 7.4 $x^{2}+2x+5 \to (x+1)^{2} = -4$, no solution |
| 8-10 | 6 glossary entries; 9 questions; 7 mistakes, 3 ideas, connections |

## Terms defined here (do not define them again)

**perfect square trinomial**, **completing the square**, **graph (of an expression)**,
**parabola**, **vertex**, **axis of symmetry** (the last four minimally, § 6 only).

Linked, not defined: quadratic equation, root/zero (Ch. 30); expand (Ch. 25); irrational number,
perfect square (Ch. 24); trinomial (Ch. 27); coefficient (Ch. 18).

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_completing_the_square.png | fig_01_completing_the_square.py | Three panels: $x^{2}$ + $6x$ strip; strip halved around the square, red dashed missing corner; green $9$ added, big square side $x + 3$ |
| fig_02_graph.png | fig_02_graph.py | $y = x^{2}+2x-6$, table dots, lowest point $(-1,-7)$, dashed $x = -1$, green crossings $-1 \pm \sqrt{7}$ with $\sqrt{7}$ distance arrows |
| fig_03_method_flow.png | fig_03_method_flow.py | Seven boxes with $2x^{2}-8x-10 = 0$ beside each; style of Ch. 30 fig_03 |

Colours: blue $x^{2}$ / curve / new steps, orange strips, green added corner / solutions / check,
red missing, purple lowest point, slate older steps.

## Sources used

* `old/11/solving-quadratics-by-completing-the-square.md` (with two images) - a study guide
  based on a Professor Dave video: why factoring fails, the $\left(\frac{b}{2}\right)^{2}$ rule,
  seven-step algorithm, four examples, geometric picture, graph of $x^{2}+2x-6$, five mistakes,
  six practice problems with solutions. Removed from `old/` after conversion (in git history).

## Skipped because the book already has it

* "Golden rule of equations" - Ch. 20 § 2.2 (linked). Square root property $y^{2} = k \to \pm\sqrt{k}$
  - Ch. 24 § 8.1. Expanding $(x+d)^{2}$ - Ch. 25 § 3.3 (re-used with $a = x$, $b = d$).
* Definitions of quadratic equation, binomial, trinomial, coefficient, irrational - earlier
  chapters.
* Source summary / key points - folded into section summaries and Important notes.
* Source images - redrawn as fig_01 and fig_02.

## Additions (source uses but does not explain)

* Why the corner must be squared (fig_01); why divide by $a$, tested at $x = 1$ (§ 5.1).
* Exact check of $-1 + \sqrt{7}$ (§ 4.2); value table and lowest-point reasoning (§ 6).
* Minimal definitions of graph, parabola, vertex, axis of symmetry (source uses the words).
* Q7 (what to add to $x^{2}-12x$, $x^{2}+7x$), Q8 (not dividing by $a$), Q9 (no solution) are
  the book's; Q1-Q6 are the source's practice problems.

## Corrections to the source

* "Completing the square can solve **any** quadratic equation": it always reaches
  $(x + d)^{2} = k$, but when $k < 0$ there is no solution (§ 7.4, Q9).
* "Irrational: cannot be written as a simple fraction" - book uses Ch. 24's definition (no
  fraction with whole numbers at all).
* "Sign inside the bracket always matches the sign of $b$" - true only after dividing by $a$;
  stated in that order.
* "Magic constant" wording dropped.

## Not covered yet - waiting for a source

* The quadratic formula and its derivation (source mentions it only as motivation).
* Vertex form $y = a(x - h)^{2} + k$ as a named form; graphing parabolas in general; the
  coordinate plane properly (§ 6 gives only what the source's graph needs).
* $(x + d)^{2} = 0$ with one repeated answer; the discriminant.
