# Chapter 25 - Simplifying expressions with exponents and roots

File: [25_Simplifying_Expressions/25_Simplifying_Expressions.md](./../25_Simplifying_Expressions/25_Simplifying_Expressions.md)

The folder is `25_Simplifying_Expressions` and the title is the full one ("... with exponents and
roots"). They differ on purpose, as in Chapters 4, 18, 22 and 24. Both are fixed - do not rename.

This is a **synthesis chapter**. Most of its source repeats Chapters 10 and 24, so most of the
chapter is links. What is genuinely new is four things: the power of a quotient (§ 2, open since
Ch. 10), the square of a sum and the ban on handing an exponent across $+$ / $-$ (§ 3), a negative
exponent on a fraction (§ 4), and the root-first road for $x^{\frac{m}{n}}$ (§ 5). § 6 then works
the source's three examples with an explicit six-step order of attack.

The spine is one question, asked in § 3.4 and fig_03: **what joins the pieces inside the
bracket?** Times or divide - hand the exponent out. Plus or minus - never.

## Sections

| Section | Contains |
| --- | --- |
| 1. What "simplified" means here | 1.1 the seven-row table of rules already owned, with their usual names (product rule, quotient rule, ...) and links, plus the **Note: every letter in the chapter is positive**; 1.2 the five-point **finished form** (no bracket, each base once, numbers worked out, no negative/zero exponent, fraction in lowest terms), and the Note that $9x^{-1}y^{5}$ and $\frac{9y^{5}}{x}$ are equal but only the second is finished; 1.3 $6x^{3}y^{2}$ against $(6x^{3}y)^{2}$, **quantity** defined, linked to Ch. 11 § 5.1 |
| 2. A power of a fraction | 2.1 $\left(\frac{2}{3}\right)^{2} = \frac{4}{9}$ via Ch. 16 § 3.3; 2.2 fig_01 and the tops-with-tops explanation; 2.3 $\left(\frac{a}{b}\right)^{n} = \frac{a^{n}}{b^{n}}$, **power of a quotient** named; 2.4 $\left(\frac{3xy^{2}}{2x^{3}}\right)^{2} = \frac{9x^{2}y^{4}}{4x^{6}}$ and the Warning that plain numbers are powered too |
| 3. An exponent cannot pass a plus sign | 3.1 $(3+2)^{2} = 25$ vs $13$, and $(5-2)^{2} = 9$ vs $21$; 3.2 fig_02, the four pieces, and the explanation (regrouping a product vs distributing a sum); 3.3 $(a+b)^{2} = a^{2} + 2ab + b^{2}$ derived in four steps via Ch. 6 § 4.3, Ch. 19 § 3 and § 4, checked at $3, 2$; **expand** defined; the Note naming FOIL as not yet covered; 3.4 fig_03 and the three-row test table |
| 4. A negative exponent on a fraction | 4.1 $\left(\frac{2}{3}\right)^{-2} = \frac{9}{4}$ by Rule 4 and keep-change-flip; 4.2 the four-line proof with letters, fig_04; 4.3 $\left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^{n}$ and two Warnings (not negative; flip **and** drop the minus) |
| 5. A fractional exponent: take the root first | 5.1 $x^{\frac{m}{n}} = \left(\sqrt[n]{x}\right)^{m}$ derived from Rule 5 read backwards; 5.2 $64^{\frac{2}{3}} = 16$ by both roads, fig_05; 5.3 why root first, and $27^{\frac{4}{3}} = 81$ |
| 6. Putting the rules together | 6.1 the six-step order of attack; 6.2 $(6x^{3}y)^{2} = 36x^{6}y^{2}$; 6.3 $4x^{3}y \times \left(\frac{3xy^{2}}{2x^{3}}\right)^{2} = \frac{9y^{5}}{x}$, by the source's road and then tidying first; 6.4 $\left(\frac{x^{6}}{64}\right)^{-\frac{2}{3}} = \frac{16}{x^{4}}$ |
| 7. Glossary / 8. Check your understanding / 9. Important notes | 4 new terms; 10 questions (Q7 substitution test on $(x+3)^{2}$, Q9 conceptual without "rule", Q10 finished form); 6 mistakes, 3 ideas, connections, and what is still open |

## Terms defined here (do not define them again anywhere else)

**quantity**, **simplified** (for an expression with exponents - the five-point finished form),
**power of a quotient**, **expand**.

The usual names **product rule**, **quotient rule**, **power of a power**, **power of a product**
are attached to Ch. 10's Rules 1, 2, 5 and § 8.4 in the § 1.1 table only. They are not new ideas.

## Formulas and facts that live here

* $\left(\frac{a}{b}\right)^{n} = \frac{a^{n}}{b^{n}}$, $b \neq 0$ (§ 2.3)
* $(a + b)^{n} \neq a^{n} + b^{n}$; also for $-$ (§ 3.1, § 3.4)
* $(a + b)^{2} = a^{2} + 2ab + b^{2}$ (§ 3.3)
* $\left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^{n}$, $a, b \neq 0$ (§ 4.3)
* $x^{\frac{m}{n}} = \sqrt[n]{x^{m}} = \left(\sqrt[n]{x}\right)^{m}$; root first is the habit (§ 5)
* Worked numbers, all checked with Python (sympy) before they were written down:
  $\left(\frac{2}{3}\right)^{2} = \frac{4}{9}$; $(3+2)^{2} = 25$, $9+4 = 13$, $6+6 = 12$;
  $(5-2)^{2} = 9$, $25-4 = 21$; $\left(\frac{2}{3}\right)^{-2} = \frac{9}{4}$;
  $64^{2} = 4\,096$, $16^{3} = 4\,096$, $64^{\frac{2}{3}} = 16$; $27^{\frac{4}{3}} = 81$,
  $27^{4} = 531\,441$; $(6x^{3}y)^{2} = 36x^{6}y^{2}$;
  $\left(\frac{3xy^{2}}{2x^{3}}\right)^{2} = \frac{9x^{2}y^{4}}{4x^{6}}$, and the bracket tidies
  to $\frac{3y^{2}}{2x^{2}}$; $4x^{3}y \times (\ldots)^{2} = \frac{9y^{5}}{x}$;
  $\left(\frac{x^{6}}{64}\right)^{-\frac{2}{3}} = \frac{16}{x^{4}}$
* Questions (§ 8): $(3a^{2}b^{4})^{3} = 27a^{6}b^{12}$; $\left(\frac{2}{5}\right)^{3} = \frac{8}{125}$;
  $\left(\frac{3}{4}\right)^{-2} = \frac{16}{9}$; $16^{\frac{3}{4}} = 8$ (and $16^{3} = 4\,096$);
  $5m^{2}n\left(\frac{2m^{3}n}{m^{4}}\right)^{3} = \frac{40n^{4}}{m}$;
  $\left(\frac{27}{a^{9}}\right)^{-\frac{4}{3}} = \frac{a^{12}}{81}$; $(x+3)^{2} = x^{2}+6x+9$,
  $16 \neq 10$ at $x = 1$; $(6x^{3})^{2} = 36x^{6}$; Q9 uses $7^{2} = 49$ vs $29$, missing $20$;
  Q10 is the finished-form question

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_power_of_a_fraction.png | fig_01_power_of_a_fraction.py | A whole square cut $3 \times 3$, the bottom-left $2 \times 2$ shaded blue and measured $\frac{2}{3}$ on two sides; right column: tops $2 \times 2 = 4$ (blue), bottoms $3 \times 3 = 9$ (orange), $\left(\frac{2}{3}\right)^{2} = \frac{2^{2}}{3^{2}} = \frac{4}{9}$ |
| fig_02_square_of_a_sum.png | fig_02_square_of_a_sum.py | A $5 \times 5$ grid cut at $3$: blue $3^{2}$ and $2^{2}$ squares, orange $3 \times 2$ strips; right column 25 / 13 / 12 / total, then $(a+b)^{2} = a^{2} + 2ab + b^{2}$ in green under a dashed rule |
| fig_03_reach_test.png | fig_03_reach_test.py | Green panel "joined by $\times$ or $\div$" with $(2 \times 5)^{2}$ and $\left(\frac{6}{3}\right)^{2}$ checked; red panel "joined by $+$ or $-$" with $(3+2)^{2}$ and $(5-2)^{2}$ failing. Replaces the source's ASCII decision tree |
| fig_04_flip.png | fig_04_flip.py | $\left(\frac{2}{3}\right)^{-2}$ (orange) to $\left(\frac{3}{2}\right)^{2}$ (blue) to $\frac{9}{4}$ (green); below a dashed rule, $-\frac{4}{9}$ and $\left(\frac{3}{2}\right)^{-2}$ in red with drawn crosses |
| fig_05_two_roads.png | fig_05_two_roads.py | Two rows of cards for $64^{\frac{2}{3}}$: green root-first road $64 \to 4 \to 16$; grey power-first road $64 \to 4\,096 \to 16$ with "cube root: ?". Replaces the source's LaTeX `array` "visual" |

Colour convention, carried on from Chapters 10 and 24, no new meanings:

* blue `#2E86DE` - the top of a fraction, a power step, a positive exponent after the flip
* orange `#E67E22` - the bottom of a fraction, a root step, a negative exponent, the forgotten strips
* green `#1E8449` - a correct or finished answer, the recommended road
* red `#C0392B` - a wrong answer
* grey `#78909C` - quiet labels, checks, rules

Layout notes: the Chapter 10 lesson held - crosses drawn **beside** stacked fractions, never
through them (fig_04). Labels inside fig_02's pieces sit on a white box so the grid does not cut
through them.

## Sources used

* `old/5/simplifying-expressions-tutorial.md` (a written tutorial: introduction, prerequisites,
  definitions including "quantity", three main concepts, a seven-row rule table, three worked
  examples, two "visuals" (an ASCII decision tree and a LaTeX array of two paths), four common
  mistakes, three practice problems with solutions, a summary and key points).

## Material in the source that was deliberately skipped, because the book already has it

* **Base and exponent, what an exponent means** - Ch. 10 § 2.1.
* **Order of operations** - Ch. 11. Linked in § 1.3 and § 6.1.
* **Reciprocal** - Ch. 10 § 7.1, Ch. 16 § 4.1. § 4.2 links.
* **Radical, radicand, index** - Ch. 24 § 2.2. Glossary Note links.
* **Product, quotient, zero... rules; power of a power; power of a product** - Ch. 10 §§ 4-8.
  § 1.1 is a table of links. The "multiplication is associative and commutative" reason for
  $(ab)^{2} = a^{2}b^{2}$ is Ch. 10 § 8.4 and is only recalled in § 3.2.
* **$x^{-n} = \frac{1}{x^{n}}$** and **$x^{-2} \neq -x^{2}$** - Ch. 10 § 7.4, § 7.5.
* **$(x^{3})^{2} \neq x^{5}$** - Ch. 10 § 8.3. Recalled as a Warning in § 6.2 only.
* **$x^{\frac{m}{n}} = \sqrt[n]{x^{m}}$** - Ch. 24 § 7.3. § 5 adds only the second form.

## Additions made because the source uses them without explaining them

* **What "simplified" means** (§ 1.2). The source writes "final simplified expression" and gives
  two forms as equally final. The book fixes the five-point finished form.
* **Why $\left(\frac{a}{b}\right)^{n} = \frac{a^{n}}{b^{n}}$** (§ 2.1-2.2, fig_01). The source only
  states it.
* **Why $(a+b)^{2} = a^{2} + 2ab + b^{2}$** (§ 3.2-3.3, fig_02). The source states it in its
  mistakes table and says "use expansion methods like FOIL". The book derives the square only,
  from the distributive property; FOIL is named in a Note and left open.
* **Why $\left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^{n}$** (§ 4.2). Stated only in
  the source.
* **Why $x^{\frac{m}{n}} = \left(\sqrt[n]{x}\right)^{m}$** (§ 5.1), from Rule 5 backwards.
* **The quotient property for a cube root** (§ 6.4). The source takes the cube root of top and
  bottom silently; the book links Ch. 24 § 4.5 and says it works for index $3$ too.
* **The positive-letter assumption** (§ 1.1 Note). The source never states it.
* **Q2, Q3, Q4, Q7-Q10** are the book's; Q1, Q5, Q6 are the source's practice problems.

## Corrections and simplifications made to the source

* **The dot for multiplication was replaced by $\times$**, as everywhere since Ch. 6.
* **"Quantity" was narrowed.** The source calls it "a math term used to group multiple items in
  parentheses". The book defines it as the bracketed group and gives the spoken form
  ("the quantity ..., squared"), which is how the word is actually used.
* **Example 2's "or $9x^{-1}y^{5}$" as an equally final answer** was kept as true but not
  finished (§ 1.2 Note, Q10).
* **The source's examples and its solution 2 use different roads** (power first vs tidy inside
  first) without comment. § 6.3 does both on the same expression and says step 2 is a choice.
* **Both "visuals" were replaced** - ASCII tree became fig_03, the LaTeX `array` became fig_05.
* **Worked examples, mistakes and practice problems were dissolved** into the sections that need
  them, as in every chapter since Ch. 7.
* $\mathbf{bold}$ final answers in maths were written as plain "**Answer: ...**" lines.

## Not covered yet - waiting for a source

* **Multiplying two different brackets**, $(a+b)(c+d)$, and FOIL - open since Ch. 6 and Ch. 19,
  named again in § 3.3's Note and § 9.
* **$(a - b)^{2}$ expanded**, and **$(a + b)^{3}$** - the source only says they cannot be handed
  out.
* **Adding and subtracting roots**, rationalising a denominator - still open from Ch. 24.
* **A negative base with a fractional exponent**, e.g. $(-8)^{\frac{2}{3}}$ - deliberately excluded
  by the positive-letter assumption.
