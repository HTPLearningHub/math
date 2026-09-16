# Chapter 12 - Divisibility and prime numbers

File: [12_Divisibility_And_Prime_Numbers/12_Divisibility_And_Prime_Numbers.md](./../12_Divisibility_And_Prime_Numbers/12_Divisibility_And_Prime_Numbers.md)

Folder name and title match. Both are fixed - do not rename either.

This is the first chapter about **numbers themselves** rather than about how to calculate with
them. Chapters 5 to 11 were methods; this one asks what a number is made of. It turns
Chapter 8's remainder round: Chapter 8 was about what to do with the leftover, this chapter is
about the divisions where there is none.

It is also the first chapter where Chapter 10's exponents do real work. $2^{3} \times 3 \times 5^{2}$
is not an exercise here, it is the *name* of $600$.

The chapter is held together by one framing the source does not have: **a prime factorization
is a fingerprint** (§ 5.2). Once the reader has it, § 5.3 (divisibility read off the primes)
and § 6 (counting the factors) are two uses of the same object rather than two new topics.

## Sections

| Section | Contains |
| --- | --- |
| 1. Division that leaves nothing behind | 1.1 $10 \div 2$ against $10 \div 3$, both put through Ch. 8 § 5.3's equation; **divisible** defined; the Note that Chs. 1, 2 and 4 were about using the leftover; 1.2 **whole numbers**, **positive integers** / **natural numbers**, and the Note that Ch. 9's negatives are set aside for this chapter; 1.3 fig_01, the three sentences around $2 \times 5 = 10$, **multiple** defined, the small table, and the Warning about swapping *factor* and *multiple*; 1.4 **even** and **odd** |
| 2. Finding every factor of a number | 2.1 $1$ and $N$ come free; 2.2 the walk up from $1$, all five tests for $10$, and the Note that $\{\;\}$ is not a grouping bracket; 2.3 the walk for $20$, fig_02, **factor pair** defined; 2.4 the halfway rule **with its proof** ($f > \frac{N}{2} \Rightarrow \frac{N}{f} < 2$, and $1$ is the only whole number below $2$), then the better stop - the pairs cross - and the Note that this is why the walk misses nothing; 2.5 the four digit tests, **and why each one works**: $148 = 140 + 8$ for $2$, $5$, $10$; $372 = (297+63) + (3+7+2)$ for $3$ |
| 3. Prime and composite | 3.1 factors of $7$ worked to the crossing point, **prime** and **composite** defined, fig_03; 3.2 why $1$ is neither - its two candidate factors are the same number - with the forward Note to § 5.2; 3.3 $2$ is the smallest prime and the only even one, and the Warning that "no even number is prime" is false; 3.4 the four-row table $9, 15, 21, 25$; 3.5 the full check that $29$ is prime, stopped by the crossing rule and **not** by a square root; 3.6 Euclid, and that the primes never run out |
| 4. Breaking a number into primes | 4.1 $20 = 4 \times 5 \to 2 \times 2 \times 5$, and the atoms-and-molecules analogy; 4.2 **prime factorization** defined, written with Ch. 10's exponents, the two habits (smallest prime first, no $^{1}$), and the Warning that $4 \times 5$ is not an answer; 4.3 **factor tree**, $36$ in five steps, fig_04, checked by multiplying back; 4.4 **ladder method**, $90$ in five steps using the § 2.5 digit tests, fig_05, checked; 4.5 $180$ on the ladder; 4.6 the four-row comparison table |
| 5. One number, one fingerprint | 5.1 Path A ($9 \times 10$) against Path B ($30 \times 3$), fig_06, plus the reminder that § 4.4's ladder gave the same line; 5.2 the **Fundamental Theorem of Arithmetic**, the word **fingerprint**, and the Note that proves why $1$ must be excluded ($20 = 1 \times 1 \times 2^{2} \times 5 \dots$ for ever); 5.3 $N = 2^{3} \times 3 \times 5^{2} = 600$; is it divisible by $15$? - answered from the primes, then the general **Explanation**, then the failing case $9$ |
| 6. Counting the factors without listing them | 6.1 the counting argument: three choices of $2$'s times two choices of $5$'s, fig_07, and where the $+1$ comes from; 6.2 **standard form** with its symbol list, then $d(N) = (e_{1}+1)\dots(e_{k}+1)$ with its symbol list, and the Warning that the formula is nonsense on a partial split; 6.3 $d(36) = 9$ checked against a list, $d(600) = 24$, and the Note about the invisible exponent $1$ |
| 7. Glossary / 8. Check your understanding / 9. Important notes | 16 new terms; 10 questions with hidden answers; 6 mistakes, 3 ideas to keep, and a closing section naming Chs. 1, 3, 6, 8, 10 and 11 |

## Terms defined here (do not define them again anywhere else)

divisible, divisibility, whole numbers, positive integers (natural numbers), multiple, even,
odd, factor pair, prime number, composite number, prime factorization, factor tree, ladder
method, Fundamental Theorem of Arithmetic, standard form, $d(N)$.

**Factor** and **product** are Ch. 6 § 1.1 and are linked, not redefined - this chapter only
widens the word from "one of two numbers in a multiplication" to "every number that divides
this one". **Dividend**, **divisor** and **quotient** are Ch. 1 § 1.2. **Remainder** is
Ch. 8 § 5.2. **Greatest common factor** is Ch. 3 § 4.2. **Base**, **exponent** and **power**
are Ch. 10 § 2.1. The glossary ends with a Note listing all of these with links.

## Formulas and facts that live here

* $a$ is a factor of $b$ $\Leftrightarrow$ $b$ is divisible by $a$ $\Leftrightarrow$ $b$ is a
  multiple of $a$ (§ 1.3, fig_01) - one fact, three sentences
* The halfway rule, with its proof (§ 2.4)
* The crossing rule: stop when the test number and its partner meet (§ 2.4, used again in
  § 3.1, § 3.5, Q1, Q2)
* Digit tests for $2$, $3$, $5$, $10$, each with a reason (§ 2.5)
* Fundamental Theorem of Arithmetic (§ 5.2)
* One number divides another exactly when every prime of the smaller appears in the bigger, at
  least as many times (§ 5.3) - the chapter's own statement, and the thing Q7 and Q10 test
* Standard form $N = p_{1}^{e_{1}} \times \dots \times p_{k}^{e_{k}}$ (§ 6.2)
* $d(N) = (e_{1}+1)(e_{2}+1)\dots(e_{k}+1)$, derived from counting, not asserted (§ 6.1, § 6.2)
* Worked numbers, all checked with Python before they were written down:
  factors of $10 = \{1,2,5,10\}$; of $20 = \{1,2,4,5,10,20\}$; of $7 = \{1,7\}$;
  of $1 = \{1\}$; of $29 = \{1,29\}$; of $9$, $15$, $21$, $25$ in the § 3.4 table;
  $36 = 2^{2} \times 3^{2}$; $90 = 2 \times 3^{2} \times 5$; $180 = 2^{2} \times 3^{2} \times 5$;
  $20 = 2^{2} \times 5$; $600 = 2^{3} \times 3 \times 5^{2}$ and $600 = 15 \times 40$;
  $600 \div 9 = 66$ remainder $6$; $d(20) = 6$, $d(36) = 9$, $d(600) = 24$;
  $148 = 140 + 8$; $372 = 360 + 12$ and $372 \div 3 = 124$ via $120 + 4$;
  three primes between $80$ and $100$ ($83$, $89$, $97$), eight below $20$
* Questions (§ 8): factors of $15$; factors of $12$; is $51$ prime (no, $3 \times 17$);
  $24 = 2^{3} \times 3$; $48 = 2^{4} \times 3$; $d(48) = 10$;
  $M = 2^{2} \times 7 = 28$, $d(M) = 6$, divisible by $14$;
  $200 = 2^{3} \times 5^{2}$; the student who stops at $40 = 4 \times 10$;
  is $2^{4} \times 3^{2}$ divisible by $24$ (yes, $= 144 = 24 \times 6$) and by $5$ (no)

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_one_fact_three_names.png | fig_01_one_fact_three_names.py | $2 \times 5 = 10$ in a green box, three grey arrows dropping into three panels: factor / divisible / multiple, each with its reason and its arithmetic |
| fig_02_factor_pairs.png | fig_02_factor_pairs.py | The numbers $1$ to $20$ as cells, factors filled green; three green arcs for the pairs $(1,20)$, $(2,10)$, $(4,5)$; a grey dashed mark at half of $20$ and an orange one between $4$ and $5$ |
| fig_03_primes_to_20.png | fig_03_primes_to_20.py | Four rows of five cells, $1$ to $20$, each with its factor list and count. Grey for $1$, green for prime, blue for composite. Legend above |
| fig_04_factor_tree_36.png | fig_04_factor_tree_36.py | The tree for $36$, blue circles for composite and green for prime, three grey level labels down the left, and the two answer lines below |
| fig_05_ladder_90.png | fig_05_ladder_90.py | The ladder for $90$: primes down the left of a vertical rule, what is left down the right, a row line after each division, the division written out in grey on the right, and a green arrow saying which column to read |
| fig_06_two_trees_90.png | fig_06_two_trees_90.py | Two panels, Path A ($9 \times 10$, two levels) and Path B ($30 \times 3$, three levels), the collected primes under each panel, and a green band with the shared answer |
| fig_07_factor_grid_20.png | fig_07_factor_grid_20.py | A $3 \times 2$ grid, rows $2^{0}, 2^{1}, 2^{2}$ and columns $5^{0}, 5^{1}$, each cell holding one factor of $20$; then the counting sentence and $d(20) = 3 \times 2 = 6$ |

Colour convention. New meanings for this chapter, and they should be kept if a later chapter
draws primes again:

* green `#1E8449` - **prime, and any exact division.** This is the chapter's main colour. It
  keeps Ch. 9's and Ch. 11's "this one is right" feeling, which is why a prime circle reads as
  *finished*
* blue `#2E86DE` - **composite, and any number still being broken up.** In Ch. 11 blue was
  Level 3; here it means "not done yet", so a blue circle is an instruction to keep splitting
* grey `#78909C` - $1$, quiet labels, arrows, branch lines
* purple `#8E44AD` - **the exponent form of an answer.** Exactly Ch. 10's and Ch. 11's meaning,
  carried over. Every figure that prints a prime factorization prints the short form in purple
* orange `#E67E22` - used once, for the crossing point in fig_02
* tints: `#E8F5EC` green, `#E9F2FC` blue, `#ECEFF1` grey

Layout lessons worth keeping, on top of the Chapter 9, 10 and 11 lists:

* **A legend spaced by guessing a character width will always collide.** fig_03's first version
  used `len(text) * 0.083` and put each swatch on top of the previous label. It now measures
  every label with `t.get_window_extent(renderer) / fig.dpi` - the same `width_of()` helper
  Ch. 11's fig_04 introduced - and advances by the measured width. Use it for any horizontal
  row of labelled items.
* **A tree with labels down the side must not be centred.** fig_04's first version centred the
  tree on the canvas and the level labels landed on the leftmost circle. The fix is a separate
  `CX` for the tree, set to the right of the label column, rather than `W / 2`.
* **A summary line under a tree collides with the deepest branch.** fig_06 originally printed
  the collected primes inside each panel; Path B is three levels deep and reached that line.
  The summary now sits *below* the panel. When two panels have different depths, put anything
  shared outside both of them.
* **Node circles need `ax.set_aspect("equal")` and data coordinates in inches.** All three tree
  and ladder figures set `ax.set_position([0, 0, 1, 1])` and use inches as data units, so a
  radius in the script is a radius on the page.
* **Draw branches before nodes.** Every tree figure plots the lines first with `zorder=1` and
  the circles at `zorder=2`, so no line shows through a circle.

## Sources used

* `old/12/divisibility-and-prime-factorization-manual.md` (a written manual: an introduction, a
  prerequisite section on whole numbers and remainders, a table of eight definitions, three
  main concept sections, a divisibility-test table, three "formulas and rules", four worked
  examples, three ASCII diagrams, five common mistakes, eight practice problems with full
  solutions, a summary and a key-points list).

## Material in the source that was deliberately skipped, because the book already has it

* **What a dividend, a divisor, a quotient and a remainder are.** The source re-defines all
  four in its prerequisite section. Ch. 1 § 1.2 and Ch. 8 § 5.2 have them; § 1.1 links.
* **The equation $a = (b \times q) + r$.** Ch. 8 § 5.3 derives it. § 1.1 states it once and
  links, then uses it on $10 \div 2$ and $10 \div 3$.
* **What a factor is.** Ch. 6 § 1.1. § 1.3 links and then adds only what is new - that *factor*,
  *divisible* and *multiple* are one fact.
* **What an exponent is, and that $2^{2} = 4$.** Ch. 10 § 2.1 and § 2.3. § 4.2 links.
* **That $x^{1} = x$.** Ch. 10 § 2.4. § 4.2 links, and it matters again in § 6.3.
* **Place value.** Ch. 5 § 2.3, used in § 2.5's explanation of the digit tests, and linked.
* **The distributive property.** Ch. 6 § 2.4, used to open the brackets in the digit-test-for-3
  proof, and linked.
* **The order of operations.** Ch. 11. Used silently whenever a standard form is turned into a
  number; § 9 points that out at the end instead of re-teaching it.

## Additions made because the source states a rule without giving a reason

* **Why the digit tests work** (§ 2.5). The source gives the four tests as a lookup table with
  no explanation at all. $148 = 140 + 8$ covers $2$, $5$ and $10$ in one move, because the part
  in front of the last digit is always a multiple of $10$. The test for $3$ gets the full
  $300 = 3 \times (99+1)$ argument. This is the largest single addition in the chapter and it
  is the reason § 2.5 is not just a table.
* **Why the walk up from $1$ never misses a factor** (§ 2.4 Note). The source asserts the
  method works.
* **The crossing rule, stated properly** (§ 2.4). See the corrections section below.
* **Why $1$ has to be excluded from the primes** (§ 5.2 Note). The source says $1$ is not prime
  because it has one factor, which is true but circular-sounding. The real reason is that
  uniqueness would fail: $20 = 1 \times 2^{2} \times 5 = 1 \times 1 \times 2^{2} \times 5$ and
  so on for ever. § 3.2 promises this and § 5.2 delivers it.
* **Divisibility read straight off the fingerprint** (§ 5.3). The source uses this idea once,
  buried in the solution to its problem 7c, and never states it. The chapter pulls it out as an
  **Explanation**, gives it a failing case ($600$ and $9$), and builds Q7 and Q10 on it.
* **Where $d(N)$ comes from** (§ 6.1, fig_07). The source presents the formula as a thing to
  memorise. It is a counting argument: $e + 1$ choices per prime, because *taking none* is a
  choice. The grid makes the six cells and the six factors the same picture.
* **The word "fingerprint"** (§ 5.2). The source says "unique mathematical fingerprint" once in
  its introduction and then never uses it again. The chapter makes it the name of the object and
  uses it in § 5.3, § 6.1 and § 9.

## Corrections and simplifications made to the source

* **The source's factor list for $8$ is wrong.** Its § 7.3 table gives $\{1, 8\}$, which would
  make $8$ prime. fig_03 gives $\{1, 2, 4, 8\}$, and the whole table was regenerated from
  Python rather than copied.
* **Square roots were removed.** The source's solution to its problem 2 says "test prime
  divisors up to $\sqrt{29} \approx 5.38$", which contradicts its own halfway rule and uses a
  symbol the book has never introduced. § 3.5 reaches the same stopping point with the crossing
  rule instead: at $5$ the quotient is also $5$, so the two ends have met. **Do not put a square
  root back into this chapter until a source covers roots.**
* **The crossing rule was stated instead of hinted at.** The source's Example 2 stops at $5$ and
  justifies it with "since $5$ is right next to $4$, we have checked all possibilities up to
  half of $20$", which is not true - $6$ to $10$ were never checked. § 2.4 separates the two
  facts properly: the halfway rule (true, proved) and the crossing rule (also true, and much
  stronger).
* **The set-theory notation was dropped.** The source's rule 1 is
  $a \mid b \iff \exists\, k \in \mathbb{Z} \text{ such that } b = k \cdot a$. The book has never
  used $\exists$, $\in$ or $\mathbb{Z}$, and the vertical bar would collide with Ch. 9 § 2.3's
  absolute-value bars. § 1.3 says the same thing in three plain sentences and a figure.
* **The claim "there are infinitely many primes" was kept, the arithmetic around it was not.**
  The source gives no counts. The chapter's two counts (eight primes below $20$, three between
  $80$ and $100$) were computed, not guessed, and the first is readable straight off fig_03.
* **All three ASCII diagrams were dropped**, as always (CLAUDE.md § 7). The prime/composite
  branch diagram became fig_03, the two factor trees became fig_04 and fig_06, and the number
  table became fig_03 as well.
* **The source's separate "worked examples", "practice problems" and "solutions" sections were
  dissolved**, as in Chapters 7 to 11. Examples 1 to 4 became § 2.2, § 2.3, § 4.3 and § 4.4;
  problems 4, 5, 6 and 8 became Q4, Q5, Q6 and § 4.5; problem 7 was rebuilt as § 5.3 and a
  *different* number became Q7, so the question is not a copy of a worked example.
* **Problems that the chapter body already answers were replaced.** The source's problem 2
  ($29$) is § 3.5, its problem 6 ($36$) is § 6.3, and its problem 8 ($180$) is § 4.5. Q3
  ($51$), Q6 ($48$), Q8 ($200$), Q9 ($40$) and Q10 are new, and Q3 and Q9 test the two mistakes
  the chapter warns about rather than the arithmetic.
* **The five "common mistakes" were used twice**, as in Chapters 10 and 11: each appears as a
  Warning at the point where the reader could make it (§ 1.3, § 3.3, § 3.4, § 4.2, § 6.2), and
  all of them are collected again in § 9.

## Not covered yet - waiting for a source

* **Finding the GCF from prime factorizations**, and the LCM. § 9 links back to Ch. 3 § 4.2 and
  says § 2 is the proper version of the listing it did, but stops there. The source never
  mentions either, so CLAUDE.md § 5.1 keeps them out. This is the most obvious next step from
  this chapter and the first thing to add when a source arrives.
* **The Sieve of Eratosthenes.** The standard way of finding all primes up to a limit, and
  fig_03 is one grid away from it. The source does not mention it.
* **Testing only up to the square root**, which is the real stopping rule and is much faster
  than the crossing rule for large numbers. Blocked by roots being unknown - see the
  corrections above, and the open square-root item carried from Chapters 10 and 11.
* **Euclid's proof** that the primes never run out. § 3.6 states the result because the source
  does; the source gives no proof and neither does the chapter.
* **The divisibility tests for $4$, $6$, $8$, $9$ and $11$.** The source's table has four rows
  and the chapter has four rows. The test for $9$ would be easy now that the test for $3$ is
  explained.
* **The notation $a \mid b$.** See the corrections above.
* **Coprime numbers**, and why a fraction is fully simplified exactly when its top and bottom
  share no prime. Ch. 1 § 3.3 and Ch. 3 § 4.2 both circle this without a name for it.
* **Negative numbers and divisibility.** § 1.2 sets Ch. 9 aside in one Note. Whether $-3$ counts
  as a factor of $12$ is never asked.
* **Division by zero**, still untouched, as in Chapters 8, 9, 10 and 11.
* **Estimation**, still open from Chapters 5, 7, 8, 9, 10 and 11.
