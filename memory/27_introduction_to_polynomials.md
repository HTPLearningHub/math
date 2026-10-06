# Chapter 27 - Introduction to polynomials

File: [27_Introduction_To_Polynomials/27_Introduction_To_Polynomials.md](./../27_Introduction_To_Polynomials/27_Introduction_To_Polynomials.md)

A vocabulary chapter: no new calculation. Term, constant term, coefficient, $x^{1} = x$,
$x^{0} = 1$, negative and fractional exponents, expression vs equation are all older and linked.
New: the polynomial itself, the test for one, degree, the two naming systems, standard form,
leading term / coefficient.

The spine: **only the exponents decide** (polynomial or not, degree, standard form), and
**a plain number is a term with exponent $0$** (§ 1.3), which gives degree $0$ and the constant
last.

## Sections

| Section | Contains |
| --- | --- |
| 1. What a polynomial is | 1.1 $3x + 5$, $2x^{2} - 7x + 4$ already met (Ch. 19 § 4); 1.2 $6x^{4} = 6 \times x \times x \times x \times x$, **monomial**, **polynomial** defined, mono/poly word parts, whole numbers = **non-negative integers** (Ch. 12 § 1.2); 1.3 $x = x^{1}$, $7 = 7x^{0}$, Note: $x^{0}$ read as $1$ even at $x = 0$ (Ch. 10 says $x \neq 0$); 1.4 general formula $a_{n}x^{n} + \cdots + a_{0}$, subscript is a label, matched to $2x^{2} - 7x + 4$; 1.5 **polynomial equation**, links Ch. 18 § 4 |
| 2. What is not a polynomial | fig_02; 2.1 $x^{-2} = \frac{1}{x^{2}}$ (Ch. 10 § 7); 2.2 $\frac{3}{x} = 3x^{-1}$, $\frac{4}{2^{2}} = 4 \times 2^{-2} = 1$, Warning: $\frac{x}{4}$ IS one (coefficient may be any number), $\frac{1}{x+1}$ not; 2.3 $x^{\frac{1}{2}} = \sqrt{x}$ (Ch. 24 § 7); 2.4 three-step test + five-row table (A-E of the source) |
| 3. The parts | fig_01 on $6x^{4} - 3x^{2} + 8x - 5$; 3.1 terms, sign belongs (Ch. 21 § 1.2); 3.2 coefficients table, $x^{3} = 1x^{3}$, $-x^{3} = -1x^{3}$ (Ch. 19 § 6.2); 3.3 constant term $= -5x^{0}$ |
| 4. The degree | 4.1 definition, $7x^{5} - 2x^{3} + 4x - 9 \to 5$, $3x^{7} + \ldots \to 7$, why it matters (Ch. 10 § 3 growth); 4.2 not the biggest number ($6x^{2} + 3x + 100 \to 2$), not the first term ($8x^{2} + 100x^{5} - 3 \to 5$); 4.3 $8 = 8x^{0}$, degree $0$; Note: $0$ has no degree; 4.4 collect like terms first: $x^{3} + 2x - x^{3} = 2x$, checked at $x = 2$ ($4$ both) |
| 5. Two ways to name | 5.1 monomial/binomial/trinomial table, bi/tri word parts, four+ terms no name, count after collecting; 5.2 constant/linear/quadratic/cubic/quartic/quintic table, quadratic/cubic linked to "squared/cubed" Ch. 10 § 2.2, constant to Ch. 18 § 2.2; 5.3 quadratic trinomial, quartic trinomial, fig_03 grid with 3 impossible cells explained, Warning degree $\neq$ number of terms ($x^{5} + 2x + 1$) |
| 6. Standard form, leading term | 6.1 **standard form**, commutative (Ch. 19 § 2.1), $4 + 3x^{2} - 7x \to 3x^{2} - 7x + 4$, fig_04, sign travels (Ch. 19 § 2.4), Warning lost sign gives $30$ not $2$ at $x = 2$; $5 - 2x^{3} + 7x - x^{5} \to -x^{5} - 2x^{3} + 7x + 5$; Note missing powers; 6.2 **leading term** (largest exponent, not "first written"), **leading coefficient**, $8x^{5} - 3x^{3} + 2x - 9$, Warning $4 + 3x^{2} - 7x$; 6.3 why useful |
| 7. Reading a whole polynomial | 7.1 seven steps on $4x^{5} - 7x^{3} + 2x^{2} + 9x - 6$ (quintic, 5 terms); 7.2 $2 + 5x^{4} - 3x^{2} + x^{7} - 8x \to x^{7} + 5x^{4} - 3x^{2} - 8x + 2$, checked at $x = 1$ ($-3$ both), leading coefficient invisible $1$ |
| 8-10 | 11 glossary entries; 10 questions; 7 mistakes, 3 ideas, connections ($4x + 3$ linear binomial; $(x+3)^{2} = x^{2} + 6x + 9$ quadratic trinomial via Ch. 25 § 3) |

## Terms defined here (do not define them again)

**polynomial**, **monomial**, **binomial**, **trinomial**, **non-negative integers** (as a name
for the whole numbers), **polynomial equation**, **degree**, **constant / linear / quadratic /
cubic / quartic / quintic** (as polynomial names), **standard form**, **leading term**,
**leading coefficient**.

Linked, not defined: term, variable term, constant term (Ch. 21); coefficient, constant,
expression, equation (Ch. 18); like terms, commutative property (Ch. 19); exponent, $x^{1}$,
$x^{0}$, negative exponent (Ch. 10); fractional exponent (Ch. 24); whole numbers (Ch. 12).

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_anatomy.png | fig_01_anatomy.py | $6x^{4} - 3x^{2} + 8x - 5$ cut into 4 cards (blue variable terms, orange constant); coefficient and exponent under each, invisible exponents light purple; green line "largest is 4, degree 4" |
| fig_02_allowed_exponents.png | fig_02_allowed_exponents.py | Exponent number line $-3 \ldots 4$: whole numbers green dots, negatives and $\frac{1}{2}, \frac{3}{2}$ red crosses; $x^{-2} = \frac{1}{x^{2}}$, $x^{-1} = \frac{1}{x}$, $x^{\frac{1}{2}} = \sqrt{x}$ below |
| fig_03_two_names.png | fig_03_two_names.py | Grid: rows degree 0-3 (purple names), columns 1-3 terms (blue names), example + two-part name in each green cell; 3 grey "not possible" cells |
| fig_04_standard_form.png | fig_04_standard_form.py | Cards $4, +3x^{2}, -7x$ (exp 0, 2, 1) arrowed to $3x^{2}, -7x, +4$ (exp 2, 1, 0); right panel: both $= 2$ at $x = 2$ |

Colours as Chs. 24-26: blue variable term, orange constant term, purple exponent / degree,
green allowed or agreeing, red not allowed, grey labels.

## Sources used

* `old/7/introduction_to_polynomials_tutorial.md` - a written study guide based on Professor Dave
  Explains, "Introduction to Polynomials" (YouTube, about 5 min): prerequisites, definition,
  non-examples, parts, degree, mono/bi/trinomial, degree names, standard form, leading term,
  full example, three graded examples, test checklist, examples A-E, expression vs equation,
  "why polynomials matter", six mistakes, ten practice problems with solutions, table, summary.

## Skipped because the book already has it

* Variables, $3x$ meaning $3 \cdot x$, evaluating at $x = 4$ - Ch. 18 §§ 2, 3, 6.
* Exponent as repeated multiplication - Ch. 10 § 2. Coefficient - Ch. 18 § 3.3; invisible $1$ -
  Ch. 19 § 6.2. Term and "the sign belongs to the term" - Ch. 21 § 1.2.
* Expression vs equation - Ch. 18 § 4; § 1.5 only adds the name "polynomial equation".
* Source § 17 "Why polynomials matter" and § 25 "Connection to the next lessons" (adding,
  multiplying, FOIL, factoring, solving, graphing polynomials): previews of untaught topics, left
  out by CLAUDE.md § 5.1.
* Source § 22 "mental model" (building blocks) - became fig_01. § 21 classification table -
  became fig_03 and the § 5.2 table.

## Additions (source uses but does not explain)

* Word parts mono/bi/tri/poly; quadratic/cubic linked to "squared/cubed".
* $\frac{x}{4}$ is a polynomial (coefficient may be a fraction) - Warning in § 2.2 and Q10; the
  source's "variable in denominator" rule invites the wrong conclusion.
* Why degree 0 binomials and degree 1 trinomials cannot exist (fig_03).
* Number checks of every reordering ($x = 2$, $x = 1$).
* Q9 (degree of $7$) and Q10 (the fraction-bar contrast) are the book's; Q1-Q8 are the source's
  practice problems (its Problem 8 is Q4, its Problems 6 and 9 merged into Q6 with Problem 9's
  numbers).

## Corrections to the source

* "Leading term = the first term in standard form" made precise: the term with the largest
  exponent, which standard form puts first (§ 6.2 Warning).
* Degree must be read **after collecting like terms** - the source never says so (§ 4.4,
  $x^{3} + 2x - x^{3}$).
* $-5 = -5x^{0}$ quietly uses $x^{0} = 1$ at $x = 0$, which Ch. 10 excludes; § 1.3 Note states the
  convention.
* Zero polynomial: the source says "undefined or $-\infty$"; the book says only "no degree",
  with the reason ($0 = 0x^{n}$ for every $n$).
* $P(x)$ and $\deg(P)$ notation dropped: function notation has never been taught.
* Dot for multiplication -> $\times$; boxed answers -> bold.

## Not covered yet - waiting for a source

* (Adding and subtracting: now Ch. 28.) Multiplying, dividing polynomials; FOIL for binomials; factoring
  polynomials; solving quadratic and higher equations; graphing polynomial functions - all
  named by the source as "next lessons".
* Polynomials in more than one letter (degree of $x^{2}y^{3}$) - not in the source.
* Function notation $P(x)$ - still open.
