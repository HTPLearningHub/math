# Chapter 26 - Solving equations with roots and exponents

File: [26_Equations_With_Roots_And_Exponents/26_Equations_With_Roots_And_Exponents.md](./../26_Equations_With_Roots_And_Exponents/26_Equations_With_Roots_And_Exponents.md)

Folder and title differ on purpose ("Equations_With_Roots_And_Exponents" vs "Solving equations
with roots and exponents"). Both fixed - do not rename.

Closes Ch. 20 § 5.2's promise ("equations with a power on the letter ... are a later chapter")
and Ch. 24 § 8's other half: Ch. 24 undid a power with a root; this chapter undoes a root with a
power. Most of the source's background (fractional exponents, power of a power, reciprocal, $\pm$)
is already in Chs. 10, 16, 24, 25 and is linked, not re-taught.

The spine: **undo with the opposite power**, and **even powers forget the sign** - the one fact
behind both the $\pm$ (§ 4) and extraneous solutions (§ 6). fig_03 is that sentence drawn.

## Sections

| Section | Contains |
| --- | --- |
| 1. The letter is under a root | 1.1 two-row table of what the book can solve, then $\sqrt{x+9} = 5$ as what it cannot; 1.2 the root bar is an invisible bracket (like Ch. 21 § 4.1's fraction bar), $\sqrt{x+9} \neq \sqrt{x} + 9$ tested at $x = 16$ ($5$ vs $13$), linked to Ch. 25 § 3; 1.3 outside in = Ch. 20 § 5's order, fig_01 |
| 2. Undoing a root | 2.1 $(\sqrt{A})^{2} = A$ from the meaning of $\sqrt{\ }$, and again via $A^{\frac{1}{2} \times 2}$; legality by Ch. 20 § 2.2, "if $A = B$ then $A^{2} = B^{2}$", flagged as one-way for § 6; 2.2 $\sqrt{x+9} = 5 \to 16$; 2.3 $\sqrt{x+9} + 1 = 6$, get the root alone first, Warning; 2.4 $\sqrt[3]{x-2} = 3 \to 29$; 2.5 the index table, $(\sqrt[n]{A})^{n} = A$ |
| 3. Undoing a fractional exponent | 3.1 $4^{\frac{3}{2}} = 8$ (root then cube, Ch. 25 § 5); 3.2 backwards: cube root then square = $\frac{2}{3}$, fig_02, reciprocal linked to Ch. 16 § 4.1; 3.3 $(X^{\frac{m}{n}})^{\frac{n}{m}} = X$ via Ch. 10 § 8.2 + Ch. 16 § 4.2, **reciprocal power** defined; 3.4 $(x+2)^{\frac{3}{2}} = 8 \to x = 2$, checked; 3.5 Warning: exponent is not a multiplier ($8 \div \frac{3}{2} = \frac{16}{3}$, check gives about $12.3$); 3.6 Note: bracket assumed not negative; with even top, $(x-1)^{\frac{2}{3}} = 9$ also has $x = -26$ |
| 4. When the letter is squared | 4.1 $x^{2} + 5 = 41 \to \pm 6$, both checked, number line linked to Ch. 24 fig_02; 4.2 $\sqrt{x^{2}+5} \neq x + \sqrt{5}$ at $x = 6$ ($\approx 6.40$ vs $\approx 8.24$); 4.3 taking a root needs $\pm$, squaring does not |
| 5. A number in front, roots on both sides | 5.1 $(3\sqrt{x-1})^{2} = 9(x-1)$ via Ch. 10 § 8.4, checked at $x = 5$ ($36$ vs wrong $12$), $(c\sqrt{A})^{2} = c^{2}A$; 5.2 $3\sqrt{x-1} = \sqrt{x+1} \to \frac{5}{4}$ using Ch. 21 §§ 2-3, Ch. 14 § 5.2, checked with Ch. 24 § 4.5 ($\frac{3}{2}$ both sides) |
| 6. Squaring can let in a wrong answer | 6.1 $3 = -3$ false, squared $9 = 9$ true; the one-way sentence; 6.2 $\sqrt{2x+1} = -3 \to x = 4$, check fails, fig_03, **extraneous solution** defined, no solution (like Ch. 24 § 8.3), visible at once from Ch. 24 § 2.3; 6.3 the check catches the method's own output, not your slips; Note: cubing is safe (Ch. 24 § 6.2) |
| 7. The method in one place | fig_04 and four numbered steps; only step 2 is new |
| 8-10 | 2 glossary terms; 10 questions; 6 mistakes, 3 ideas, connections, what is still open |

## Terms defined here (do not define them again)

**reciprocal power**, **extraneous solution**.

Linked, not defined: solution, isolating, properties of equality (Ch. 20); term (Ch. 21); root,
radical sign, radicand, index, principal square root, fractional exponent (Ch. 24); reciprocal
(Ch. 10 / Ch. 16).

## Formulas and facts that live here

* $(\sqrt{A})^{2} = A$, $(\sqrt[n]{A})^{n} = A$ (§ 2.1, § 2.5)
* If $A = B$ then $A^{2} = B^{2}$; **not** the converse (§ 2.1, § 6.1)
* $(X^{\frac{m}{n}})^{\frac{n}{m}} = X$, $X \geq 0$ (§ 3.3)
* $(c\sqrt{A})^{2} = c^{2} \times A$ (§ 5.1)
* Worked numbers, all checked with Python before writing: $\sqrt{25} = 5$, $\sqrt{16} + 9 = 13$;
  $x = 16$; $\sqrt[3]{27} = 3$, $x = 29$; $41 - 5 = 36$, $\pm 6$; $4^{\frac{3}{2}} = 8$,
  $8^{\frac{2}{3}} = 4$, $x = 2$; $\frac{16}{3}$ and $(\frac{16}{3})^{\frac{3}{2}} \approx 12.32$;
  $\sqrt{41} \approx 6.40$, $6 + \sqrt{5} \approx 8.24$; $(3 \times 2)^{2} = 36$, $9 \times 4 = 36$,
  $3 \times 4 = 12$; $x = \frac{5}{4}$, both sides $\frac{3}{2}$; $\sqrt{2x+1} = -3 \to x = 4$,
  $\sqrt{9} = 3$
* Questions: Q1 $40$; Q2 $\pm 5$; Q3 $28$ (and $-26$ without the assumption, checked:
  $\sqrt[3]{-27}^{2} = 9$); Q4 $76$ ($27^{\frac{4}{3}} = 81$, $81^{\frac{3}{4}} = 27$); Q5 $8$
  ($2\sqrt{11} = \sqrt{44}$); Q6 $\sqrt[3]{2x+1} = -3 \to -14$; Q7 $\sqrt{x+5} = -2$, extraneous
  $-1$, no solution; Q8 subtract-9-first mistake; Q9 $(2\sqrt{x})^{2} = 4x$, at $x = 9$: $36$ vs
  $18$; Q10 why check, without "rule"

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_unwrapping.png | fig_01_unwrapping.py | Blue forward row $16 \to$ add 9 $\to 25 \to$ root $\to 5$; orange backward row $5 \to$ square $\to 25 \to$ subtract 9 $\to 16$; green end cards |
| fig_02_reciprocal_power.png | fig_02_reciprocal_power.py | Forward $4 \to 2 \to 8$ (power $\frac{3}{2}$), backward $8 \to 2 \to 4$ (power $\frac{2}{3}$), purple lines naming bottom/top jobs, green $\frac{3}{2} \times \frac{2}{3} = 1$ under a dashed rule |
| fig_03_squaring_forgets_the_sign.png | fig_03_squaring_forgets_the_sign.py | Left: blue $3$ and orange $-3$, $\neq$, arrows into green $9$; right: $\sqrt{2x+1} = -3$ solved to $x = 4$, red failing check with a drawn cross beside it |
| fig_04_the_method.png | fig_04_the_method.py | Four boxes (grey, orange, grey, green), a five-row "if you see / do this" table beside box 2, red "check not optional" panel beside box 4. Replaces the source's ASCII flowchart |

Colours as Chs. 24-25: blue forward / positive, orange backward / negative partner, green answer
or true, red false or rejected, purple exponent jobs, grey labels.

## Sources used

* `old/6/solving-algebraic-equations-roots-exponents.md` (written tutorial: intro, prerequisites,
  definitions table, four concepts, five rules, four examples, ASCII flowchart, three graphs,
  four mistakes, five practice problems with solutions, summary, key points) and its three PNGs.

## Skipped because the book already has it

* Inverse operations, order of operations - Ch. 8 § 1.1, Ch. 20 §§ 3, 5, Ch. 11.
* Power of a power - Ch. 10 § 8. Roots as fractional exponents - Ch. 24 § 7. Root-first
  evaluation - Ch. 25 § 5. Reciprocal - Ch. 10 § 7.1, Ch. 16 § 4.
* Equation, variable, exponent, radical sign, radicand, fractional exponent, principal square root
  definitions - Chs. 18, 10, 24.
* $x^{2} = k \Rightarrow x = \pm\sqrt{k}$ - Ch. 24 § 8.1. § 4 adds only "isolate first".

## Additions (source uses but does not explain)

* **Why** $(\sqrt{A})^{2} = A$ (§ 2.1) and **why** the reciprocal power works, via the forward /
  backward machine (fig_02) - the source only states both.
* **Extraneous solution**: the source defines it and says "verify", but never shows one. § 6 adds
  $\sqrt{2x+1} = -3$ as the minimal example, and the reason (squaring is one-way).
* Cube-root worked example $\sqrt[3]{x-2} = 3$ (§ 2.4) and the outside-the-root example
  $\sqrt{x+9} + 1 = 6$ (§ 2.3) - the source states both ideas without an example.
* Q6-Q10 are the book's; Q1-Q5 are the source's practice problems.

## Corrections to the source

* Its prerequisite list labels $\sqrt[n]{x} = x^{1/n}$ as "Cube root". Not carried over.
* Rule 3 $(x^{a/b})^{b/a} = x$ has no condition. The book states $X \geq 0$ and shows, in § 3.6,
  that practice problem 3 $(x-1)^{\frac{2}{3}} = 9$ also has $x = -26$ if the bracket may be
  negative. The source gives only $28$.
* Problem 4's check line was garbled ($(\sqrt[3]{81})^{3} \dots$); rewritten with $\sqrt[4]{81} = 3$.
* Mistake 4 ("multiplying 8 by 3/2") reframed as the real error: undoing an exponent by dividing.
* "Verify to rule out extraneous solutions" strengthened: after squaring, the check is part of
  the method (§ 6.3).
* The three graphs (curve meets line, parabola, number line) were dropped: the book has never
  drawn a graph of a function (open since Ch. 18). The number line is linked to Ch. 24 fig_02.
* ASCII flowchart -> fig_04. Dot for multiplication -> $\times$. $\implies$ -> words.

## Not covered yet - waiting for a source

* **Quadratic equations** ($x^{2} + 5x = 6$), and root equations that square into one
  ($\sqrt{x+3} = x - 3$) - named in § 10.
* **Drawing an equation as a graph** - still open from Ch. 18.
* Adding/subtracting roots, rationalising - still open from Chs. 24-25.
