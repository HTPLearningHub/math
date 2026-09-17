# Chapter 14 - The greatest common factor

File: [14_The_Greatest_Common_Factor/14_The_Greatest_Common_Factor.md](./../14_The_Greatest_Common_Factor/14_The_Greatest_Common_Factor.md)

Folder name and title match. Both are fixed - do not rename either.

This is the **twin of Chapter 13**, and it was written to be read as one. Chapter 12 § 5.3 says
"one number divides another exactly when every prime of the smaller appears in the bigger, at
least as often". Chapter 13 § 3.1 read that forwards (a common multiple must *meet* demands, so
take the **larger** count). Chapter 14 § 3.1 reads it backwards (a common factor must *respect*
limits, so take the **smaller** count). Three chapters, one sentence. If Chapter 12 § 5.3 is
ever edited, both § 3.1's break.

It also **pays two debts Chapter 13 left open**, both of which were recorded there as waiting
for a source:

* § 4.3 proves $\mathrm{LCM} \times \mathrm{GCF} = a \times b$ from
  $\min(e,\, f) + \max(e,\, f) = e + f$. Chapter 13 § 4.2 could only state and check it.
* § 4.2 shows that "coprime" (Ch. 13 § 4.1, defined by shared primes) and
  $\mathrm{GCF}(a,\, b) = 1$ are the same statement, in both directions.

And it closes a debt from Chapter 3: § 4.2 there introduced the GCF as a one-step short cut for
simplifying and had no way to find one. § 5.2 here finds it, and adds the reason one step is
always enough - what is left is coprime.

The chapter's own framing, which the source does not have, is **bricks**: a common factor can
only be built from prime bricks that both piles have, and what is left over after taking them
shares nothing (§ 3.3, fig_04). That last sentence is reused three times - pouches (§ 5.1),
fractions (§ 5.2) and brackets (§ 5.3) - and § 8 says so.

## Sections

| Section | Contains |
| --- | --- |
| 1. Numbers that share | 1.1 the 30 blue / 45 red pens, fig_01 with three splits (5 works, 10 fails, 15 works), the sentence naming the shape of the question, and the Note that this is Ch. 13 turned on its head (up vs down); 1.2 **factor** re-linked to Ch. 12 § 2 and *not* redefined, plus the three facts the chapter leans on - the list stops, $1$ divides everything, the biggest factor is the number itself; 1.3 **common factor** defined, $5$ yes and $10$ no on $30, 45$, and the Note that there is always an answer because $1$ is always shared; 1.4 **greatest common factor** re-linked to Ch. 3 § 4.2, the $\mathrm{GCF}(a,\, b)$ notation, and the Note naming **GCD** and tying *divisor* to Ch. 1 § 1.2 |
| 2. The first method: write the lists out | 2.1 the four steps, pointing at Ch. 12 § 2.2 for the walk; 2.2 $\mathrm{GCF}(10,\, 15) = 5$ with factor pairs, the two-division check that is then used everywhere, and the Warning about missing $1$ and the number itself; 2.3 $\mathrm{GCF}(18,\, 24) = 6$, fig_02; 2.4 the bracket $1 \leq \mathrm{GCF} \leq$ the smaller number, both with reasons, and the Warning that a too-big answer is a *multiple*; 2.5 why listing fails on $24$ and $108$ - the full pair walk, twelve factors, eleven test divisions, stopped by Ch. 12 § 2.4's crossing rule |
| 3. The second method: read it off the primes | **3.1 is the centre of the chapter**: Ch. 12 § 5.3 quoted, then read backwards on $24$ and $108$ as two *limits* rather than two demands, the **Explanation** that each prime may appear at most as often as the number that uses it least, fig_03, and the Note that $108$ wins the prime $2$ while $24$ wins the prime $3$; 3.2 the five steps, the Warning about taking the maximum (it silently gives the LCM) and the Warning that a prime missing from one number is dropped; 3.3 $18$ and $24$ from the primes, the count table, fig_04, the Note that $3$ and $4$ share nothing, and the Note that reordering bricks is Ch. 6 § 1.3; 3.4 $24$ and $108$ with both ladders written out, the table, $12$, and the Note pointing forward to the zero case; 3.5 the $\min$ formula with its symbol list, $\min$ explained as a word, tested on $24, 108$, and the Note that $p^{0} = 1$ (Ch. 10 § 6) means the formula needs no special case for a missing prime; 3.6 $\mathrm{GCF}(48,\, 72,\, 120) = 24$ with $5$ dropped, and the Note that one missing number is enough |
| 4. The GCF and the LCM, side by side | 4.1 *meet a demand* vs *respect a limit*, fig_05, the five-row comparison table, the size chain $1 \leq 12 \leq 24 \leq 108 \leq 216 \leq 2592$, and the Warning about answering $30$ for $\mathrm{GCF}(10,\, 15)$; 4.2 coprime $\Leftrightarrow \mathrm{GCF} = 1$, proved **both ways**, $8$ and $15$, and the Note carried from Ch. 13 that coprime is not the same as prime; 4.3 the bridge with its proof from $\min + \max = e + f$, checked on $24, 108$, and the Note that the rule is now a *method* for the LCM, not only a check |
| 5. What the greatest common factor is for | 5.1 the pens finished - $15$ pouches, then $2$ blue and $3$ red in each, and the Note that $2$ and $3$ being coprime is the signal you took the greatest; 5.2 $\frac{18}{24} = \frac{3}{4}$ in one step, the **Explanation** of why one step is always enough, the sentence that closes Ch. 3 § 4.2's Warning (a fraction is finished exactly when top and bottom are coprime), and $\frac{30}{45} = \frac{2}{3}$; 5.3 $12x + 18 = 6(2x + 3)$ in three steps, checked by distributing back, fig_06 as the Ch. 6 § 3 rectangle read backwards, the Note that a letter stands for any number (Ch. 10 § 2.5), and the Warning that $2(6x + 9)$ is true but unfinished |
| 6. Glossary / 7. Check your understanding / 8. Important notes | 4 new terms; 10 questions with hidden answers; 6 mistakes, 3 ideas to keep, and a closing section naming Chs. 3, 6, 12 and 13 |

## Terms defined here (do not define them again anywhere else)

common factor, the notation $\mathrm{GCF}(a,\, b)$, greatest common divisor (GCD), $\min$.

**Greatest common factor** itself is **Ch. 3 § 4.2** and is linked, not redefined - § 1.4
restates it in one sentence, because the reader needs it in his hands on that page, and adds
only the notation. **Factor**, **divisible**, **prime number**, **prime factorization**,
**factor pair** and the **ladder method** are Ch. 12. **Coprime**, **least common multiple**
and **$\max$** are Ch. 13. **Exponent** and **power** are Ch. 10 § 2.1, and $x^{0} = 1$ is
Ch. 10 § 6. **Term** and the **distributive property** are Ch. 6 § 2. **Numerator** and
**denominator** are Ch. 1. The glossary ends with a Note listing all of these with links.

## Formulas and facts that live here

* $1 \leq \mathrm{GCF}(a,\, b) \leq$ the smaller of $a$ and $b$, both halves with reasons (§ 2.4)
* Every common factor holds each prime at most as often as the number that holds it least; the
  greatest one holds it exactly that many times (§ 3.1) - the chapter's own statement, and the
  thing Q5 and Q10 test
* $\mathrm{GCF}(a,\, b) = p_{1}^{\min(e_{1},\, f_{1})} \times p_{2}^{\min(e_{2},\, f_{2})} \times \dots$ (§ 3.5)
* A prime missing from **any** one of the numbers contributes $p^{0} = 1$, so it drops out by
  itself (§ 3.5 Note, § 3.6)
* $a$ and $b$ are coprime $\Leftrightarrow \mathrm{GCF}(a,\, b) = 1$, proved in both
  directions (§ 4.2)
* $\min(e,\, f) + \max(e,\, f) = e + f$, hence
  $\mathrm{LCM}(a,\, b) \times \mathrm{GCF}(a,\, b) = a \times b$ (§ 4.3) - **the proof Ch. 13
  could not give**
* $\mathrm{LCM}(a,\, b) = \dfrac{a \times b}{\mathrm{GCF}(a,\, b)}$ (§ 4.3 Note, used in Q7)
* A fraction is fully simplified exactly when its top and bottom are coprime (§ 5.2)
* Worked numbers, all checked with Python before they were written down:
  factors of $10 = \{1,2,5,10\}$, of $15 = \{1,3,5,15\}$, of $18 = \{1,2,3,6,9,18\}$,
  of $24 = \{1,2,3,4,6,8,12,24\}$, of $30$, of $45 = \{1,3,5,9,15,45\}$,
  of $108 = \{1,2,3,4,6,9,12,18,27,36,54,108\}$;
  $\mathrm{GCF}(10,15) = 5$; $\mathrm{GCF}(18,24) = 6$ with $18 \div 6 = 3$, $24 \div 6 = 4$;
  $\mathrm{GCF}(24,108) = 12$ with $24 \div 12 = 2$, $108 \div 12 = 9$;
  $\mathrm{GCF}(48,72,120) = 24$ with quotients $2$, $3$, $5$;
  $\mathrm{GCF}(30,45) = 15$ with $2$ and $3$ per pouch;
  $\mathrm{GCF}(8,15) = 1$; $\mathrm{GCF}(12,18) = 6$;
  $24 = 2^{3} \times 3$, $108 = 2^{2} \times 3^{3}$, $18 = 2 \times 3^{2}$,
  $48 = 2^{4} \times 3$, $72 = 2^{3} \times 3^{2}$, $120 = 2^{3} \times 3 \times 5$,
  $30 = 2 \times 3 \times 5$, $45 = 3^{2} \times 5$;
  $\mathrm{LCM}(24,108) = 216$, $12 \times 216 = 2592 = 24 \times 108$, $2592 \div 12 = 216$
* Questions (§ 7): $\mathrm{GCF}(12,20) = 4$ by listing; $\mathrm{GCF}(36,60) = 12$ by primes
  with $5$ dropped; $\mathrm{GCF}(45,75) = 15$; the student who answers $30$ for
  $\mathrm{GCF}(10,15)$; the student who takes the maximum powers on $24$ and $108$ and gets
  $216$; $\mathrm{GCF}(8,15) = 1$ and the word for it; $\mathrm{LCM}(12,20) = 240 \div 4 = 60$
  from the bridge; $\frac{45}{75} = \frac{3}{5}$; $20x + 30 = 10(2x + 3)$;
  $N = 2^{4} \times 3^{2} \times 7$ and $M = 2^{2} \times 3^{3} \times 5$ give
  $\mathrm{GCF} = 36$, with $N = 1008$, $M = 540$, $1008 \div 36 = 28$, $540 \div 36 = 15$

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_pens_into_pouches.png | fig_01_pens_into_pouches.py | Three panels. In each, a row of $30$ blue pens and a row of $45$ red pens are cut into equal parts with a wide gap between parts. $5$ works, $10$ leaves five dashed ghost pens over, $15$ works and is the greatest |
| fig_02_two_factor_lists_18_24.png | fig_02_two_factor_lists_18_24.py | Two rows of number tiles in shared columns, blue for the factors of $18$ and orange for $24$; the four shared tiles green, an empty dashed slot where only one number has a factor, $6$ labelled *the greatest common factor* and $1$ labelled *always shared* |
| fig_03_min_powers_24_108.png | fig_03_min_powers_24_108.py | Two prime groups ($2$, $3$); in each a blue stack for $24$ and an orange stack for $108$, one tile per appearance. Tiles both stacks reach are green, tiles above are hollow and dashed, a dashed green line marks the shared height, and a green *take $p^{k}$* box sits under each group |
| fig_04_shared_bricks.png | fig_04_shared_bricks.py | Two panels of prime bricks, shared ones drawn first. Left: $18$ and $24$ share a $2$ and a $3$, so the GCF row is $2 \times 3 = 6$ and what is left is $3$ and $4$. Right: $8$ and $15$ share nothing, so the GCF row holds a single $1$ |
| fig_05_gcf_and_lcm_two_ends.png | fig_05_gcf_and_lcm_two_ends.py | The stacks of fig_03 again, with grey *take $p^{\max}$* boxes **above** them reaching $\mathrm{LCM} = 216$ and green *take $p^{\min}$* boxes **below** them reaching $\mathrm{GCF} = 12$, arrows in both directions |
| fig_06_common_factor_outside.png | fig_06_common_factor_outside.py | One rectangle of height $6$ cut into a $12x$ piece and an $18$ piece, widths $2x$ and $3$ braced underneath and $2x + 3$ braced under the whole; the height is boxed in green and labelled $\mathrm{GCF}(12,\, 18)$ |

Colour convention. Unchanged from Chapter 13, with one addition:

* blue `#2E86DE` - the first number and everything belonging to it
* orange `#E67E22` - the second number and everything belonging to it
* green `#1E8449` - **shared, and this chapter's answer.** A green tile is one both numbers own,
  and every *take* box is green
* purple `#8E44AD` - the exponent form of an answer, as in Chs. 10 to 13
* grey `#78909C` - quiet labels, arrows, leftovers, and **in fig_05 only, the LCM**, because
  green had to stay with the GCF and adding a seventh colour was worse than borrowing grey.
  Both answer *lines* in fig_05 are still purple
* red `#C0392B` - used once, in fig_01, for the split that fails. New in this chapter
* tints: `#E8F5EC` green, `#E9F2FC` blue, `#FDF0E3` orange, `#ECEFF1` grey

Layout lessons worth keeping, on top of the Chapter 9 to 13 lists:

* **Do not draw a crowd of objects inside a container that has to hold them all.** fig_01's
  first version drew $15$ pens inside each of $15$ pouch boxes; the pens overflowed the boxes
  and the boxes overflowed the panel. The fix was to drop the containers and draw each pile as
  one row cut by gaps, which also made the failing case (five pens with nowhere to go) drawable.
* **A gap that means "a new group" must be several times the gap that means "the next item".**
  fig_01's second version used $0.055$ against $0.014$ and the groups were invisible; the ratio
  now is about $4.5$ to $1$. Measure the worst case first - here $45$ items in $15$ groups - and
  size the item from that, not from the prettiest panel.
* **`FancyBboxPatch(pad=...)` grows the box outwards on all four sides.** At tile widths under
  about $0.1$ inch the padding swallows the gap between tiles and they merge into a bar. Use a
  plain `Rectangle` for anything that small.
* **Bottom whitespace is not cropped away by `bbox_inches="tight"` when the artists stop well
  above `ylim[0]`.** Three figures here were re-rendered after the whole block was shifted down
  and `H` reduced. Place the lowest artist first, then set `H`.
* **A short `FancyArrow` disappears under its own head.** fig_05's green arrows were $0.28$ long
  with a $0.16$ head and read as nubs; ending them exactly on the edge of the target box, rather
  than overlapping it, is what made them legible.

## Sources used

* `old/14/greatest-common-factor-tutorial.md` (a written tutorial: an introduction, a
  prerequisite section, four definitions, two methods, two "formulas and rules" plus a
  comparison table, three worked examples, two "visual explanations" - one ASCII factor-tree
  diagram and one markdown table - four common mistakes, five practice problems with full
  solutions, a summary and a key-points list).

## Material in the source that was deliberately skipped, because the book already has it

* **The whole prerequisite section (§ 2).** The source re-teaches whole numbers, divisibility,
  factors against multiples (with a four-row table), prime numbers, composite numbers and prime
  factorization. Every one of those is Chapter 12 - the factor/multiple table is Ch. 12 § 1.3's
  Warning - and § 1.2 and § 3.2 link rather than repeat. This is the largest single cut.
* **The definition of *factor*** (source § 3, with $n = d \times k$). Ch. 6 § 1.1 and
  Ch. 12 § 1.3. § 1.2 restates it in one sentence and links.
* **How to build a factor tree**, and the ASCII trees for $24$ and $108$. Ch. 12 § 4.3 and
  § 4.4. § 3.4 writes the two ladders out as arithmetic instead, because the reader needs the
  numbers on that page, and links.
* **The definition of *relatively prime* / *co-prime*** (source § 3). Ch. 13 § 4.1. § 4.2 here
  adds only what is new - that it is the same as $\mathrm{GCF} = 1$ - and links.
* **What an exponent is.** Ch. 10 § 2.1. § 3.5 links, and $x^{0} = 1$ links to Ch. 10 § 6.
* **Equivalent fractions and the rule for simplifying.** Ch. 1 § 3.2 and § 3.3. § 5.2 uses the
  rule and links to both.
* **The distributive property.** Ch. 6 § 2 and § 3. § 5.3 uses it and links; fig_06 is Ch. 6's
  rectangle, not a new idea.
* **The order of operations**, used silently whenever $2^{2} \times 3$ becomes $12$. Ch. 11.

## Additions made because the source states a rule without giving a reason

* **Why the minimum exponent is the right choice** (§ 3.1). This is the largest addition in the
  chapter and the reason § 3 is not a recipe. The source's "why it works" paragraph is an
  analogy about lego bricks and one sentence - "any shared factor must be built strictly from
  prime factors that both numbers possess" - which is true but never turned into the counting
  rule. The chapter derives it from Ch. 12 § 5.3 as a pair of **limits**, and everything after
  it follows.
* **Why $\mathrm{GCF} \geq 1$ and $\mathrm{GCF} \leq$ the smaller number** (§ 2.4). The source
  gives the upper bound in its key-points list with no reason and never states the lower one.
  Together they are a bracket the reader can use to reject an answer at a glance, which is what
  the Warning in § 2.4 and the size chain in § 4.1 do.
* **Why coprime and $\mathrm{GCF} = 1$ are the same thing** (§ 4.2). The source *defines*
  relatively prime by $\mathrm{GCF}(a, b) = 1$ and separately says the numbers share no factor
  but $1$. It never joins the two. Both directions are one sentence each once § 3.5 exists.
* **The proof of $\mathrm{LCM} \times \mathrm{GCF} = a \times b$** (§ 4.3). See the note below
  about scope.
* **Why one division by the GCF finishes a fraction** (§ 5.2). The source's introduction says
  $\frac{18}{24}$ becomes $\frac{3}{4}$ by dividing by $6$ and stops. The reason is that what
  is left is coprime, which the source has all the pieces for and never assembles. This also
  closes the Warning left open in Ch. 3 § 4.2.
* **Why the greatest common factor is what goes outside a bracket** (§ 5.3, fig_06). The source
  gives $12x + 18 = 6(2x + 3)$ as a single line in its introduction. The rectangle makes it the
  same picture as Ch. 6 § 3, and the Warning about $2(6x + 9)$ shows what *greatest* is for.
* **The "bricks, and what is left over" framing** (§ 3.3, fig_04). The source has the lego
  analogy in one sentence and no picture of the overlap. This is the chapter's own framing and
  it is reused in § 4.2, § 5.1, § 5.2, § 5.3 and § 8.
* **The check by division** (§ 2.2 onwards). The source never checks a GCF. Every worked example
  and every answer here divides the result into each starting number and shows the remainder $0$.

## Corrections and simplifications made to the source

* **The set-theory notation was dropped.** The source's § 5 writes
  $\text{Common Factors} = \text{Factors}(a) \cap \text{Factors}(b)$ and
  $\mathrm{GCF} = \max(\text{Common Factors})$. The book has never used $\cap$, and the
  $\max$-of-a-set form would collide with Ch. 13 § 3.5's $\max$ of two exponents. § 2.1 says the
  same thing in four plain steps. The $\{\;\}$ lists were kept, as in Ch. 12 § 2.2.
* **The ASCII factor-tree diagram was dropped**, as always (CLAUDE.md § 7). Its two trees are
  already Ch. 12 § 4.3, and the part of it that is really about the GCF - the row of shared
  bricks with boxes round them - became fig_04, where the leftovers are drawn too.
* **The "Shared Factors Breakdown Table" was replaced**, not kept. Its *Shared Primes* and
  *Unshared Primes* columns repeat the same two numbers on both rows, which reads as though the
  two numbers had different answers. fig_03 and fig_04 carry the reasoning instead, and § 3.3
  and § 3.4 use a count table shaped like Ch. 13 § 3.4's, so the two chapters look alike on the
  page.
* **Source solution 2 says "minimum power is $5^{0} = 1$ (do not include)".** That is two
  different statements glued together and it invites the reader to think $5^{0}$ is a special
  case. § 3.5's Note separates them: the formula gives $5^{0}$, Ch. 10 § 6 says $5^{0} = 1$, and
  multiplying by $1$ is what "do not include" means. No special case is needed.
* **The source's *when to use* advice was turned into a demonstration.** It says listing is
  "slow, tedious, and prone to missing factors" for large numbers. § 2.5 actually does it on
  $108$ - eleven test divisions, twelve factors - so the reader feels the cost before being
  offered the second method, exactly as Ch. 13 § 2.6 does with twenty multiples of $12$.
* **The GCF-versus-LCM contrast was promoted from a bullet to a section** (§ 4.1, fig_05). The
  source mentions it twice, once inside mistake 1 and once in its key-points list. It is the
  single most useful thing a reader who has just finished Ch. 13 can be told, so it gets the
  figure, a table, and the size chain.
* **The source's separate "worked examples", "practice problems" and "solutions" sections were
  dissolved**, as in Chapters 7 to 13. Its examples 1, 2 and 3 became § 2.2, § 2.3 / § 3.3 and
  § 2.5 / § 3.4; its problem 4 became § 3.6 and its problem 5 became § 1.1 and § 5.1. Its
  problems 1, 2 and 3 became Q1, Q2 and Q3, and Q4 to Q10 are new.
* **Two of the four "common mistakes" were turned into questions** rather than only warnings:
  mistake 1 is Q4 and mistake 3 is Q5, so the reader has to find the error instead of reading
  about it. All four appear as Warnings at the point of danger (§ 2.2, § 2.4, § 3.2 twice) and
  are collected again in § 8, as in Chapters 10 to 13.
* **The source's problem 5 was moved to the front.** It is the only concrete situation in the
  whole tutorial and it was the last thing in it. As § 1.1 it gives the chapter a question to
  answer, and § 5.1 answers it properly - including part (b), which fig_01 also shows.

## A note on scope

Two things in this chapter are **not** in `old/14` and were added deliberately. Both finish
something the book already contains rather than opening a new topic, and both were listed in
Chapter 13's own "not covered yet" section as the thing to add when a GCF source arrived:

* **§ 4.3's proof** of $\mathrm{LCM} \times \mathrm{GCF} = a \times b$. Ch. 13 § 4.2 already
  states the rule; this chapter supplies the one line of reasoning
  ($\min + \max = e + f$) that the source's own "GCF uses the lowest exponents, LCM uses the
  highest" key point is one step away from.
* **§ 4.3's Note** that the rule is now a method for the LCM, not only a check. Ch. 13 § 4.2
  explicitly says it cannot be used to compute, "because the book has no method for finding a
  GCF from primes yet". § 3.5 removes that obstacle, so the limitation had to be lifted
  somewhere, and this is the only place it can be.

If a future source covers Euclid's algorithm, it belongs in a new section here rather than a new
chapter.

## Not covered yet - waiting for a source

* **Euclid's algorithm** for the GCF - repeated division with remainders. It is by far the
  fastest method and it needs no prime factorization at all. Nowhere in this source. Carried
  over from Chapter 13's list.
* **Adding and subtracting fractions with different bottom numbers.** Still the biggest genuine
  gap in the book: the reader now has the LCD (Ch. 13 § 5.2) and the GCF and still cannot add
  $\frac{1}{3} + \frac{1}{4}$. Neither source demonstrates it.
* **When one number is a factor of the other**, so that the GCF is simply the smaller one (and
  the LCM the bigger). A direct consequence of § 3.5 and a useful short cut; neither source
  states it. Worth adding the moment a source touches it. Carried over from Chapter 13.
* **Every common factor divides the GCF** - the exact mirror of Chapter 13's open item that
  every common multiple is a multiple of the LCM. § 2.3 and § 3.3 make it visible ($1$, $2$, $3$
  and $6$ all divide $6$) and the chapter does not claim it, because the source does not.
* **Factoring an expression where the letters are also shared**, such as $12x^{2} + 18x$. § 5.3
  handles a common *number* only, which is all the source's one-line example does. This is the
  natural next step and the book already has Ch. 10's rules for it.
* **The Sieve of Eratosthenes**, **square roots as a stopping rule**, **divisibility tests for
  $4$, $6$, $8$, $9$ and $11$**, **the notation $a \mid b$**, **negative numbers and
  divisibility**, **division by zero** and **estimation** - all still open, carried over from
  Chapters 12 and 13.
