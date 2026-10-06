# Chapter 29 - Multiplying polynomials: the FOIL method

File: [29_Multiplying_Polynomials/29_Multiplying_Polynomials.md](./../29_Multiplying_Polynomials/29_Multiplying_Polynomials.md)

No new rule: distributive property (Ch. 6, Ch. 19 § 3), product rule (Ch. 10 § 4), sign rules
(Ch. 9 § 5), like terms (Ch. 19 § 4, Ch. 28) are all linked. New: distributing twice, FOIL as a
fixed order, counting products (terms times terms), the grid, two-letter products ($yx = xy$),
and the check-value rule "no bracket may become $0$".

The spine: **every term meets every term**. FOIL is that idea for two binomials.

Running example: $(x + 3)(x - 2) = x^{2} + x - 6$ (§§ 2, 3, figs 01, 02), checked at $x = 3$
($6$). Numbers version: $(10 + 3)(10 + 2) = 100 + 20 + 30 + 6 = 156$.

## Sections

| Section | Contains |
| --- | --- |
| 1. Multiplying single terms | 1.1 $2x \times 3 = 6x$ via Ch. 6 §§ 1.3-1.4; 1.2 $2x \times 3x = 6x^{2}$, $x^{2} \cdot (-2x) = -2x^{3}$ (Ch. 10 §§ 2.4, 4); Warning $x \cdot x \neq 2x$; 1.3 one term times bracket, reminder only, links Ch. 19 § 3.4 |
| 2. Two brackets: distributing twice | 2.1 $13 \times 12$ rectangle cut both ways, fig_01; 2.2 $(x+3)(x-2)$ in four steps (Ch. 6 § 4.3), check $x = 3$, Note: not $x = 2$ (bracket $0$, $x^{2} - 4$ would pass); 2.3 $2 \times 2 = 4$ products; grid with $-2$ is a table, not area |
| 3. The FOIL method | 3.1 the four letters, fig_02, FOIL = § 2 in fixed order; 3.2 numbers then $(a+b)(c+d) = ac + ad + bc + bd$ with underbrace, symbol list; 3.3 table for $(x+3)(x-2)$; 3.4 order does not matter, only for two binomials |
| 4. Every term carries its own sign | 4.1 bracket = list of terms (Ch. 19 § 2.4), sign table (Ch. 9 § 5), Ch. 9 § 5.3 method; 4.2 $(x^{2}+4)(-2x-1) = -2x^{3} - x^{2} - 8x - 4$, nothing to collect, check $x = 2$: $-40$ |
| 5. More than two terms | 5.1 counting $4, 6, 9$; partial product (Ch. 7 § 4.1); 5.2 $(x+2y)(3x-y-4) = 3x^{2} + 5xy - 2y^{2} - 4x - 8y$, fig_03, $yx = xy$ alphabetical, like terms with two letters (Ch. 19 § 4.1), order habit, check $x=1, y=2$: $-15$; 5.3 grid table $(x^{2}+2x-1)(x^{2}-x+3) = x^{4} + x^{3} + 7x - 3$, $0x^{2}$ drops (Ch. 28 § 2.4), check $35$ |
| 6. Method and check | 6.1 six steps; 6.2 Ch. 28 § 6.2 advice + no bracket may be $0$ |
| 7-9 | 2 glossary entries; 10 questions; 7 mistakes, 3 ideas, connections |

## Terms defined here (do not define them again)

**FOIL method**, **grid method**. (*acronym* explained in passing in § 3.1.)

Linked, not defined: monomial, binomial, trinomial, standard form (Ch. 27); like terms,
equivalent expressions (Ch. 19); distributive property (Ch. 6); partial product (Ch. 7);
expand (Ch. 25 § 3.3).

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_four_pieces.png | fig_01_four_pieces.py | Left: $13 \times 12$ rectangle to scale, pieces 100, 20, 30, 6. Right: 2 by 2 grid for $(x+3)(x-2)$ labelled First/Outer/Inner/Last, answer |
| fig_02_foil_arcs.png | fig_02_foil_arcs.py | $(x + 3)(x - 2)$ with F, O arcs above and I, L arcs below, products, answer |
| fig_03_every_term.png | fig_03_every_term.py | $(x + 2y)$ cards, $(3x - y - 4)$ cards, 6 arrows, two coloured product rows, answer |

Colours: blue First, orange Outer, teal Inner, purple Last (figs 01, 02); in fig_03 blue = "from
$x$", orange = "from $2y$"; green answer; grey labels.

## Sources used

* `old/9/multiplying-binomials-foil-method.md` - a written study guide "Multiplying Binomials by
  the FOIL Method": prerequisites (monomial products, monomial times binomial, like terms),
  definitions, why FOIL works, ASCII arc diagram, extension to trinomials, formula, sign rules,
  three examples, area grid, summary table, three mistakes, five practice problems, summary.

## Skipped because the book already has it

* Definitions of polynomial, monomial, binomial, trinomial - Ch. 27 § 5.1.
* Distributive property definition - Ch. 6. Like terms definition - Ch. 19 § 4.1.
* Monomial times binomial $2x(x - 4)$ - Ch. 19 § 3.4; § 1.3 is a 2-line reminder.
* Sign rules - Ch. 9 § 5; shown as a 3-row table with a link only.
* ASCII arc diagram - became fig_02. "FOIL breakdown table" - became the § 3.3 table.

## Additions (source uses but does not explain)

* Numbers first: $13 \times 12$ rectangle (the source's "area model" without numbers).
* Why a grid with a negative side is only a table, not an area.
* Counting products before collecting; link to Ch. 7 rows.
* $yx = xy$ (source writes $6xy$ without comment).
* Trinomial times trinomial worked example (source only states "9 terms").
* Check value must not make a bracket $0$.
* Q7 ($(x+5)^{2}$, link to Ch. 25), Q8 ($2x \cdot 3x$), Q9 (counting), Q10 (check value) are the
  book's; Q1-Q5 are the source's practice problems; Q6 is its Mistake 2.

## Corrections to the source

* "Arrange by standard convention: squared terms first..." and the answer
  $3x^{2} - 2y^{2} + 5xy - 4x - 8y$: there is no standard form with two letters in this book;
  the book writes $3x^{2} + 5xy - 2y^{2} - 4x - 8y$ and calls the order a habit.
* "Final step: combine like terms ($O + I$)": the Outer and Inner products are often, not always,
  like terms (Example 2 has none) - § 3.3, § 4.2.
* Polynomial "made up of terms added or subtracted": the book's definition is Ch. 27's.
* The source's Problem 5 answer order ($2x^{2} - 3y^{2} - 5xy + \dots$) reordered the same way.
* Learning FOIL "provides a foundation for quadratic equations": a preview, left out.

## Not covered yet - waiting for a source

* Special products $(a - b)^{2}$, $(a + b)(a - b)$; vertical (column) multiplication of
  polynomials; dividing polynomials. (Factoring trinomials and solving quadratics by factoring:
  now Ch. 30.)
* Degree / standard form for polynomials in two letters.
