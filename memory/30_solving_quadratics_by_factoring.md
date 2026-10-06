# Chapter 30 - Solving quadratic equations by factoring

File: [30_Solving_Quadratics_By_Factoring/30_Solving_Quadratics_By_Factoring.md](./../30_Solving_Quadratics_By_Factoring/30_Solving_Quadratics_By_Factoring.md)

Two new ideas: the **zero product property** and **factoring a trinomial** (FOIL backwards).
Everything else is linked: FOIL (Ch. 29), quadratic / degree / standard form (Ch. 27), factor
pairs (Ch. 12), sign rules (Ch. 9), one- and two-step equations (Ch. 20), checking (Ch. 20 § 4.5),
$x^{2} = k$ with two answers (Ch. 24 § 8.1).

The spine: **zero is special** (a product of $12$ tells nothing, a product of $0$ tells that one
factor is $0$), and **one hard equation becomes two easy ones**.

Running example: $x^{2} + 7x + 10 = 0 \to (x + 5)(x + 2) = 0 \to x = -5$ or $-2$
(§§ 1.3, 2.4, 3.2, 4.1, 6.2, figs 01 and 03).

## Sections

| Section | Contains |
| --- | --- |
| 1. What a quadratic equation is | 1.1 polynomial equation of degree 2 (Ch. 27 §§ 1.5, 5.2), one line of real-life uses; 1.2 standard form $ax^{2} + bx + c = 0$ on $3x^{2} + 5x - 2$, symbol list, $a \neq 0$ with reason, signs belong, invisible $1$ (Ch. 19 § 6.2); 1.3 solving (Ch. 20 § 1.2), $x = 1$ gives $18$, $x = -5$ gives $0$, two answers like Ch. 24 § 8.1, **root** / **zero**, Note on the two meanings of *root*; 1.4 why old methods fail: letter twice, $x^{2}$ and $x$ unlike |
| 2. The zero product property | 2.1 products of $12$ vs $0$; 2.2 proof both ways (Ch. 9 § 5.2; divide by $A$, Ch. 20 § 2.2, $\frac{0}{A} = 0$ via Ch. 8 § 1.1); 2.3 the rule, "or" includes both; 2.4 $(x+5)(x+2) = 0$, value table $x = -6 \ldots -1$; 2.5 only zero: $x(x+7) = -10$, $x = -10$ gives $30$ |
| 3. Factoring: FOIL backwards | 3.1 factoring (Ch. 19 § 5.1), **factored form**; 3.2 $5 + 2 = 7$, $5 \times 2 = 10$, fig_01; 3.3 $(x+m)(x+n) = x^{2} + (m+n)x + mn$, symbol list, only for $a = 1$; 3.4 start from the product (Ch. 12 § 2.3), sign table of four rows (further from $0$ carries $b$'s sign, Ch. 9 § 4) |
| 4. The simple case ($a = 1$) | 4.1 $x^{2}+7x+10$, six steps, pair table with sums, check; 4.2 $x^{2}-8x-20 \to (x-10)(x+2)$, six-row pair table, $10$ and $-2$, check |
| 5. A number in front of the square | 5.1 why the rule breaks: $(3x-1)(x+2)$, the $2$ meets $3x$; 5.2 $3x^{2}+5x-2$: first terms (3 prime, Ch. 12 § 3.1), pairs of $-2$, all four tries tabled, fig_02, "right size wrong sign: swap signs", $x = \frac{1}{3}$ (Ch. 20 § 5) or $-2$, fraction check one step per line; 5.3 method + $p r = a$, $q s = c$, $ps + qr = b$, reduces to § 3.3 when $a = 1$ |
| 6. The whole method | 6.1 fig_03 five steps; 6.2 trap: right side not $0$, $x^{2} + 7x = -10$; 6.3 trap: sign of the answer ($x = 5$ gives $70$); 6.4 trap: stopping at brackets |
| 7-9 | 5 glossary entries; 10 questions; 7 mistakes, 3 ideas, connections |

## Terms defined here (do not define them again)

**quadratic equation**, **zero product property**, **factored form**, **root (of an equation)**,
**zero (of an expression)**.

Linked, not defined: polynomial equation, degree, quadratic, binomial, trinomial, standard form
(Ch. 27); FOIL (Ch. 29); factoring, like terms (Ch. 19); solution (Ch. 20); factor pair (Ch. 12);
coefficient (Ch. 18); constant term (Ch. 21).

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_grid_backwards.png | fig_01_grid_backwards.py | Left: 2 by 2 grid with $x^{2}$ and $10$ known, red question marks (sides and middle boxes), conditions below. Right: filled with $+5$, $+2$: $x^{2}$, $2x$, $5x$, $10$; $2x + 5x = 7x$, $5 \times 2 = 10$ |
| fig_02_placement.png | fig_02_placement.py | $(3x-1)(x+2)$ with outer $6x$ / inner $-x$ arcs, $+5x$ tick; $(3x+2)(x-1)$ with $-3x$ / $2x$, $-x$ cross |
| fig_03_method_flow.png | fig_03_method_flow.py | Five boxes (zero right side, factor, split, solve, check) with the $x^{2} + 7x = -10$ example beside each |

Colours as Ch. 29: blue First, orange Outer, teal Inner, purple Last; green right / answer, red
unknown or wrong, grey labels. fig_03: blue = new steps, slate = older steps, green = check.

## Sources used

* `old/10/solving-quadratics-by-factoring.md` - a written study guide "Solving Quadratic
  Equations by Factoring": introduction, prerequisites (FOIL, factor pairs and signs),
  definitions, principle of factoring, zero product property, rules for $a = 1$ and $a \neq 1$,
  three examples, sign table, ASCII flowchart, three mistakes, three practice problems with
  solutions, summary, key points.

## Skipped because the book already has it

* FOIL method and its worked example $(x+5)(x+2)$ - Ch. 29 § 3; only re-run in § 3.2 to read off
  $5 + 2$ and $5 \times 2$.
* Binomial definition - Ch. 27 § 5.1. Integer sign rules - Ch. 9 § 5 (used, not re-taught).
* Source "Summary" and "Key things to remember" - folded into section summaries and Important
  notes.
* ASCII flowchart - became fig_03.

## Additions (source uses but does not explain)

* Why the zero product property is true (both directions, with the divide-by-$A$ proof).
* The value table in § 2.4; the numeric test $x = -10$ in § 2.5.
* Why $a \neq 0$ (Q8); why "add to $b$" fails when $a \neq 1$ (§ 5.1, fig_02).
* All four placements tabled (source tried two); the $p, q, r, s$ conditions written out.
* Why the sign table's "larger factor" rule holds (Ch. 9 § 4).
* Q4 ($x^{2} - 7x + 10$, the table's second row), Q5 (standard form first), Q6 (sign trap),
  Q7 ($(x-1)(x+2) = 4$), Q8 ($a = 0$), Q9 ($2x^{2} - x - 3$), Q10 ($x(x-4) = 0$) are the book's;
  Q1-Q3 are the source's practice problems.

## Corrections to the source

* "$a$, $b$, $c$ are constant numbers (integers)": they may be any numbers; only this chapter's
  examples use integers (§ 1.2).
* Sign table used $x^{2} - bx - c$ with $b$, $c$ as positive sizes, clashing with its own standard
  form where $b$, $c$ carry their signs; rewritten by sign of $b$ and $c$, and "larger factor"
  made precise as "further from $0$".
* "The first terms must be $3x$ and $x$": stated as a choice ("we take"), since $-3x$ and $-x$
  would also work.
* "values that make the equation true ($0 = 0$)" - dropped as unclear; § 1.3 uses Ch. 20's
  definition of a solution.
* Rule for $a \neq 1$ was vague ("factors that, multiplied across, add up to $b$"); § 5.3 gives the
  exact conditions.
* "Root" clashes with Ch. 24's root; Note added in § 1.3.

## Not covered yet - waiting for a source

* Quadratics with $b = 0$ or $c = 0$ as their own cases (only Q10 touches $c = 0$); difference of
  two squares; perfect-square trinomials; taking out a common factor before factoring a trinomial;
  the AC (grouping) method.
* Quadratics that cannot be factored with whole numbers; completing the square; the quadratic
  formula; graphs of quadratics (the source's "path of a ball" is one sentence only).
