# Chapter 32 - Solving higher-degree equations: synthetic division and the rational roots test

File: [32_Solving_Higher_Degree_Equations/32_Solving_Higher_Degree_Equations.md](./../32_Solving_Higher_Degree_Equations/32_Solving_Higher_Degree_Equations.md)

One idea: **a root gives a bracket, a bracket lowers the degree by 1**; repeat until a quadratic
is left, then Ch. 30 / Ch. 31 / Ch. 24 § 8.1. Two tools: synthetic division (test + divide) and the
rational roots test (which numbers to test). Everything else is linked: division equation (Ch. 8
§ 5.3), factor (Ch. 12 § 1.3), prime fingerprint (Ch. 12 § 5.3), coprime / simplified fraction
(Ch. 13 § 4.1, Ch. 14 § 5.2), common factor outside bracket (Ch. 14 § 5.3), evaluating (Ch. 18
§ 6.1), irrational / exact symbol (Ch. 24 §§ 3.2-3.3), $\pm$ root (Ch. 24 § 8.1), degree names,
standard form, missing powers, leading coefficient, constant term (Ch. 27), every term times
every term (Ch. 29 § 5), zero product property, root/zero, trial of places (Ch. 30), graph and
"no solution" (Ch. 31 §§ 6, 7.4).

Running examples: quartic $x^{4} + x^{3} - 11x^{2} - 5x + 30 = (x-2)(x+3)(x^{2}-5)$, roots
$2, -3, \pm\sqrt{5}$ (§§ 1, 3.3, 4.2, 5, 6.5, fig_01, fig_02); cubic
$2x^{3} + 3x^{2} - 3x - 2 = (x-1)(2x+1)(x+2)$, roots $1, -\frac{1}{2}, -2$ (§§ 6.3, 7, fig_03,
fig_04).

## Sections

| Section | Contains |
| --- | --- |
| 1. Degree three and more | 1.1 cubic/quartic named (Ch. 27 § 5.2), "higher-degree", $P(2) = 0$ by evaluation; 1.2 why Ch. 30/31 do not reach it, the plan; 1.3 **$P(x)$ notation** minimally (name + value at a number), $P(c) = 0$ |
| 2. A solution gives a bracket | 2.1 bracket to root via zero product, sign table $(x-2) \to 2$, $(x+3) \to -3$; 2.2 **factor theorem** with $\Longleftrightarrow$, factor of a polynomial; reason for root-to-bracket deferred to § 4.3; 2.3 degree drops by 1, **depressed polynomial** |
| 3. Synthetic division | 3.1 $P(x) = (x-c)Q(x) + r$ from Ch. 8's $625 = 3 \times 208 + 1$; 3.2 WHY: $(x-2)(Ax^{2}+Bx+C)+r$ for $x^{3}+3x^{2}-5x-15$, coefficient-matching table, $A=1, B=5, C=5, r=-5$ - "multiply by $c$, add next"; 3.3 fig_01 board, four moves, step table, board-as-Markdown-table format; 3.4 reading bottom row, one power lower; 3.5 missing power $0$: $x^{3}-7x+6$ by $(x-2) \to x^{2}+2x-3$, Warning without $0$ gives remainder $-4$; 3.6 corner holds $c$, $(x+3) \to -3$ |
| 4. Remainder = value | 4.1 **remainder theorem** proof $P(c) = 0 \cdot Q(c) + r$; 4.2 $c = 1$ on quartic: board $16$, $P(1) = 16$; 4.3 remainder $0$ / root / factor one fact; finishes § 2.2 |
| 5. Quartic all the way | 5.1 root 2; 5.2 $-3$ on the cubic $\to x^{2} - 5$; 5.3 $\pm\sqrt{5}$, exact check ($5\sqrt{5}$ cancels); 5.4 fig_02 |
| 6. Rational roots test | 6.1 **integer**, **rational number** defined; 6.2 integer root divides constant: $r(r^{2}+3r-5) = 15$, candidates $\pm 1, 3, 5, 15$; 6.3 Explanation block: $\frac{p}{q}$ coprime, multiply by $q^{3}$, $p \mid 2q^{3} \Rightarrow p \mid 2$ via fingerprint, same for $q$; 6.4 **the test** $\pm\frac{p}{q}$, **candidate**, Note: possible only; 6.5 quartic's 16 candidates, $2$ and $-3$ on it, $\pm\sqrt{5}$ not (irrational) - bring degree to 2 then quadratic methods |
| 7. Cubic from nothing | 7.1 $p/q$ table, $\pm 1, \pm 2, \pm\frac{1}{2}$; 7.2 board $c=1 \to 2x^{2}+5x+2$, leading coefficient brought down; 7.3 Ch. 30 trial of places (2 tries) $(2x+1)(x+2)$; 7.4 check $-\frac{1}{2}$ line by line, fig_03 |
| 8. Whole method | 8.1 fig_04 flow; 8.2 **at most $n$ solutions** with reason (product $k(x-c_1)\cdots(x-c_n)$, no other number gives 0); "at most" - $x^{2}+4x+10$ has none (Ch. 31 § 7.4) |
| 9-11 | 13 glossary entries; 9 questions; 7 mistakes, 3 ideas, connections |

## Terms defined here (do not define them again)

**higher-degree equation**, **$P(x)$ notation** (minimal: name and value; not functions in
general), **factor of a polynomial**, **factor theorem**, **quotient (of polynomials)**,
**remainder theorem**, **depressed polynomial**, **synthetic division**, **integer** (the full set
with negatives - first time in the book), **rational number**, **rational roots test**,
**candidate root**.

Linked, not defined: cubic, quartic, degree, standard form, leading coefficient, constant term
(Ch. 27); root, zero, zero product property (Ch. 30); graph (Ch. 31); irrational (Ch. 24);
remainder, quotient of numbers (Ch. 8); coprime (Ch. 13); factor (Ch. 12).

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_synthetic_board.png | fig_01_synthetic_board.py | Board for quartic $\div (x-2)$: orange $2$ in corner, slate top row under power headings, orange middle row, blue bottom row, green boxed remainder $0$; blue dashed "bring down", orange "$\times 2$" diagonal arrows, slate "add" arrow; caption of new polynomial |
| fig_02_quartic_graph.png | fig_02_quartic_graph.py | W-shaped curve, green crossings $-3, -\sqrt{5}, 2, \sqrt{5}$; inset close-up of the dip between $2$ and $\sqrt{5}$ (min about $-0.31$) |
| fig_03_cubic_graph.png | fig_03_cubic_graph.py | Cubic curve, six candidates on the zero line: green filled at $-2, -\frac{1}{2}, 1$; grey hollow at $-1, \frac{1}{2}, 2$ with dotted sticks to the value ($2$ is off the top, value $20$) |
| fig_04_method_flow.png | fig_04_method_flow.py | Six boxes (style of Ch. 30/31 fig_03), example on the cubic beside each; red loop 4 to 3 "next candidate", blue dashed loop 4 to 2 "degree still 3 or more" |

Colours: blue curve / bottom row / new steps, green roots and remainder, orange multiply row and
$c$, slate given coefficients and old steps, grey failed candidates, red retry loop.

Format decision: worked boards are **Markdown tables** (header row of powers; rows
"coefficients", "$c \times$ bottom number on the left", "bottom row (sums)"); only fig_01 is a
drawn board. Reuse this format in later chapters.

## Sources used

* `old/13/solving_higher_degree_polynomials.md` (with `cubic_graph.png`, `quartic_graph.png`) - a
  study guide based on a video lesson: standard form, zeros/roots/factors, factor theorem,
  synthetic division algorithm, rational roots test, quartic example (given candidate $2$, then
  $-3$), cubic example from the test, two graphs, four mistakes, three practice problems with
  solutions, summary. Removed from `old/` after conversion (in git history).

## Skipped because the book already has it

* Polynomial, standard form, degree, leading coefficient, constant term, degree names - Ch. 27.
* Solving $x^{2} = 5$ with $\pm$ - Ch. 24 § 8.1. Factoring $2x^{2} + 5x + 2$ - Ch. 30 § 5 (the
  book uses its trial of places, **not** the source's split-the-middle / grouping, which the book
  has never taught).
* Source images - redrawn as fig_02 and fig_03 (source quartic image had overlapping labels at
  $2$ and $2.24$; fixed with an inset). Source ASCII flowchart and board diagrams - became fig_04
  and fig_01.
* Source summary / key points / formula table - folded into section summaries, glossary and
  Important notes.

## Additions (source uses but does not explain)

* WHY synthetic division works (§ 3.2, coefficient matching via Ch. 29); WHY remainder $0$ means
  root (§ 4.1, remainder theorem, named); proof of factor theorem both ways (§§ 2.1, 4.3).
* WHY the rational roots test holds: integer case (§ 6.2) and fraction case (§ 6.3).
* WHY degree $n$ gives at most $n$ solutions (§ 8.2).
* $P(x)$ notation, integer, rational number (source uses them).
* Failing candidate $c = 1$ on the quartic (§ 4.2); missing-zero Warning with numbers (§ 3.5).
* Q4-Q9 are the book's; Q1-Q3 are the source's practice problems.

## Corrections to the source

* Source gives the quadratic formula as a tool; the book has not taught it, so the last quadratic
  is solved by factoring / completing the square / Ch. 24 § 8.1 only.
* Source's "Fundamental Theorem of Algebra: exactly $n$ complex roots" - complex numbers not in
  the book; replaced by "at most $n$ solutions" with proof.
* Source's missing-zero example ($x^{3} - 7x + 6$, coefficients $1, -7, 6$) did not say what goes
  wrong; with $c = 2$ the wrong board gives remainder $-4$ (with $c = 1$ it accidentally gives $0$,
  which is why $c = 2$ was chosen).
* "$p$ factor of $a_{0}$, $q$ factor of $a_{n}$" stated with its condition: root in lowest terms,
  integer coefficients.

## Not covered yet - waiting for a source

* The quadratic formula (still open, also listed in Ch. 31).
* Polynomial long division (source mentions it only as the slow alternative); dividing by
  anything other than $(x - c)$.
* Complex roots, the Fundamental Theorem of Algebra; repeated roots / multiplicity.
* Functions and function notation in general (§ 1.3 gives only the name-and-value use of $P(x)$).
