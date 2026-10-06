# Chapter 28 - Adding and subtracting polynomials

File: [28_Adding_And_Subtracting_Polynomials/28_Adding_And_Subtracting_Polynomials.md](./../28_Adding_And_Subtracting_Polynomials/28_Adding_And_Subtracting_Polynomials.md)

No new rule: like terms (Ch. 19 § 4), sign rules (Ch. 9 § 4), negative multiplier (Ch. 19 § 3.5),
columns (Ch. 5 § 3), standard form (Ch. 27 § 6) are all linked. New: organising the work for whole
polynomials, the minus in front of a bracket, the opposite of a polynomial, place holders
$0x^{k}$, no carrying between columns.

The spine: **only like terms join, and only their coefficients change**, and **subtracting is
adding the opposite** ($A - B = A + (-B)$).

One running example all chapter: $P_{1} = 4x^{3} + 2x^{2} - 6x + 9$ (value $37$ at $x = 2$, $9$ at
$x = 1$), $P_{2} = x^{4} - 3x^{2} + 6x - 4$ (value $12$ at $x = 2$, $0$ at $x = 1$).
$P_{1} + P_{2} = x^{4} + 4x^{3} - x^{2} + 5$ ($49$); $P_{1} - P_{2} = -x^{4} + 4x^{3} + 5x^{2} - 12x + 13$ ($25$).

## Sections

| Section | Contains |
| --- | --- |
| 1. What adding polynomials really is | 1.1 it is collecting like terms; 1.2 like = same exponent (one letter), table, plain numbers all like ($x^{0}$), apples/oranges analogy; 1.3 $Ax^{k} \pm Bx^{k} = (A \pm B)x^{k}$, check $x = 2$: $72$ vs wrong $9x^{6} = 576$; Warning: exponents add only in multiplication (Ch. 10 § 4) |
| 2. Horizontal method | 2.1 plus before bracket = $\times 1$, $10 + (4 - 3) = 11$; 2.2 four steps; 2.3 $P_{1} + P_{2}$ with fig_01, check $37 + 12 = 49$; 2.4 $0x$ disappears (Ch. 19 § 6.1) |
| 3. Vertical method | 3.1 one column per exponent (Ch. 5 § 3.1); 3.2 place holder $0x^{k}$ (word from Ch. 2 § 3.3); 3.3 fig_02, column by column; 3.4 **no carrying**: $10x^{2} \neq x^{3}$ because $x \neq 10$ ($40$ vs $8$ at $x = 2$); 3.5 which method |
| 4. Subtracting | 4.1 "subtract $B$ from $A$" is $A - B$ (Ch. 19 § 2.3, Ch. 22 § 3.3); 4.2 $-(a + b - c) = -a - b + c$, numbers $10 - (6 - 2) = 6$ vs wrong $2$; minus = $\times(-1)$ (Ch. 20 § 6.3) then Ch. 19 § 3.5; fig_03; finger habit (source's tip); 4.3 **opposite of a polynomial**, $A - B = A + (-B)$ (Ch. 9 §§ 2.2, 4.3); 4.4 $P_{1} - P_{2}$, check $25$; 4.5 columns: write the opposite in row 2, then add (Markdown table) |
| 5. Three polynomials | $(4x^{3} - x^{2} + 6) + (2x^{3} + 5x - 3) - (3x^{3} - 4x^{2} + 2x - 8) = 3x^{3} + 3x^{2} + 3x + 11$, check $x = 1$: $9 + 4 + 7 = 20$; Warning: only the minus bracket flips |
| 6. Method and check | 6.1 six steps; 6.2 substitution test (Ch. 19 § 1.3): $x = 0$ sees only constants, $x = 1$ cannot catch a wrong exponent, use $x = 2$ |
| 7-9 | 3 glossary entries; 9 questions; 7 mistakes, 3 ideas, connections |

## Terms defined here (do not define them again)

**horizontal method**, **vertical method** (column method), **opposite of a polynomial**.

Linked, not defined: like terms, collecting like terms, equivalent expressions (Ch. 19);
opposite of a number (Ch. 9); place holder (Ch. 2 § 3.3); polynomial, degree, standard form
(Ch. 27).

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_grouping.png | fig_01_grouping.py | $P_{1}$, $P_{2}$ as cards coloured by exponent, arrows into five exponent boxes, results below, $0x$ grey struck out, green answer |
| fig_02_columns.png | fig_02_columns.py | Five tinted columns ($x^{4}$ to number), dashed grey place holders $0x^{4}$, $0x^{3}$, sum row with $0x$ struck out |
| fig_03_sign_flip.png | fig_03_sign_flip.py | Magenta minus with a rail dropping onto each card of $(x^{4} - 3x^{2} + 6x - 4)$; arrows down to $-x^{4}, +3x^{2}, -6x, +4$ with the small calculations |

Colours (new for this chapter, one per exponent): purple $x^{4}$, blue $x^{3}$, teal $x^{2}$,
gold $x$, orange constant; green answer; grey labels / vanished term; magenta the minus sign.

## Sources used

* `old/8/adding-and-subtracting-polynomials.md` - a written study guide "Adding and Subtracting
  Polynomials: A Beginner-Friendly Guide": prerequisites, definitions table, like terms (apples
  and oranges), horizontal and vertical methods, formulas, two worked examples (the $P_{1}$,
  $P_{2}$ pair), fruit table, ASCII column diagram, three mistakes, four practice problems with
  solutions, summary, key points.

## Skipped because the book already has it

* Variable, coefficient, exponent, constant, $x^{0} = 1$ - Chs. 18, 10, 27.
* Distributive property and $5x + 4x = 9x$ - Ch. 6, Ch. 19 § 4.2.
* Definitions table (polynomial, term, degree, standard form, like terms) - Ch. 27, Ch. 19 § 4.1.
* General form $a_{n}x^{n} + \cdots + a_{0}$ - Ch. 27 § 1.4. $P(x)$ notation still not used.
* $-(-3) = +3$ - Ch. 9 § 4.4.
* Fruit table ("Visual 1") - covered by § 1.2-1.3 and Ch. 19 fig_05. ASCII column diagram
  ("Visual 2") - became fig_02.

## Additions (source uses but does not explain)

* Why a plus in front of a bracket changes nothing; why a minus flips every sign ($\times(-1)$).
* Opposite of a polynomial, $A - B = A + (-B)$ (source says it in one line).
* Why placeholders are safe ($0x^{k} = 0$); why columns never carry.
* "Subtract $B$ from $A$" order (source's Example 2 uses it without comment).
* Choosing the check value ($x = 2$, not $0$ or $1$).
* Q4 is the source's Mistake 2; Q5, Q6 its Mistakes 1, 3; Q7, Q8, Q9 are the book's. Source
  Problem 4 became § 5.

## Corrections to the source

* "Exponents must be positive whole numbers ($0, 1, 2, \dots$)": $0$ is not positive; the book
  says whole numbers (already Ch. 27).
* "Exactly like $123 + 456$": true for the columns, false for carrying - § 3.4.
* Vertical subtraction: source says "subtract each column"; the book writes the opposite and
  adds, to keep signs safe (§ 4.5).
* Source's prerequisites list "four concepts" but gives two; ignored.

## Not covered yet - waiting for a source

* (Multiplying and FOIL: now Ch. 29.) Dividing polynomials; factoring polynomials; solving polynomial
  equations; graphing.
* Polynomials in more than one letter (adding $3xy + 2xy$).
* Function notation $P(x)$.
