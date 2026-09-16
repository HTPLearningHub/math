# Chapter 9 - Negative numbers

File: [9_Negative_Numbers/9_Negative_Numbers.md](./../9_Negative_Numbers/9_Negative_Numbers.md)

Folder name and title match. Both are fixed - do not rename either.

This is the chapter every previous chapter has been waiting for. Chapter 5 § 6.1 ended with an
explicit promise ("numbers below zero are not in this book yet") and Chapters 6, 7 and 8 all
listed negative numbers as out of scope. § 1.1 quotes that promise and § 10 retires it.

The chapter is built on one sentence, given in § 2.2 and used in § 4.4, § 5.1 and § 5.2:
**a minus sign in front of a number means "the opposite of".** Everything else - why two minus
signs cancel, why multiplying by a negative turns the jumps round - is that sentence applied.

## Sections

| Section | Contains |
| --- | --- |
| 1. Where the numbers we have run out | 1.1 $10 - 3 = 7$ works only because the start is bigger; quotes the Ch. 5 § 6.1 warning; 1.2 the customer who wants $15$ apples, $10 - 15 = -5$, "less than nothing"; 1.3 fig_01, **positive number**, **negative number** and **sign** defined, the two notes (zero is neither; $+5$ means $5$) |
| 2. The line goes both ways | 2.1 fig_02, the line continued left, linked back to Ch. 1 § 5.2 and Ch. 2 § 4.2, plus the note that the steps are the same size on both sides; 2.2 fig_03, **opposite** defined, the "opposite of" sentence, zero is its own opposite; 2.3 **absolute value** defined, with the two-bar notation, tied to Ch. 2 § 2.4's *magnitude*, the warning that it is never negative, and why it matters (§ 5.3 needs it) |
| 3. Which of two numbers is bigger | 3.1 the one rule (further right is greater) and its three consequences; 3.2 fig_04, $-2 > -5$ read off the line and read as debt; 3.3 the digit trap as a Warning, then the four-case comparison table |
| 4. Adding and subtracting | 4.1 fig_05, plus = right, minus = left, the number = how far, $-4 + 9 = 5$; 4.2 the two jobs of the minus sign and why brackets are written (explicitly *not* the Ch. 6 § 1.2 brackets); 4.3 $a + (-b) = a - b$ with symbol list, the bill example, $-3 + (-4) = -7$, and the warning pointing at § 7; 4.4 $a - (-b) = a + b$ with **three** reasons - forgiven debt, fig_06 distance, and a five-row pattern table; 4.5 $-8 - (-5) + (-3) = -6$ with "clear the signs" as its own step |
| 5. Multiplying | 5.1 fig_07, repeated addition from Ch. 6 § 1.1, $5 \times (-2) = -10$, then the commutative property (Ch. 6 § 1.3) to cover $(-a) \times b$; 5.2 fig_08 pattern as the main reason, the "turn round twice" memory aid as a Note, then the distributive-property proof as an Explanation; 5.3 the two-question method (absolute values, then count the minus signs) with two examples and a note that Ch. 7's columns are unchanged |
| 6. Dividing | 6.1 the four multiplications of § 5 read backwards as a table, justified by inverse operations (Ch. 8 § 1.1); the three fraction forms with a symbol list; three worked examples; the check-by-multiplying note; 6.2 the fraction bar as a grouping symbol, $\frac{(-4) \times (-6)}{-3} = -8$, and the warning not to count minus signs across a whole expression |
| 7. All the signs in one place | fig_09, then two Markdown tables (one for $+$ and $-$, one for $\times$ and $\div$), the note that after clearing signs the answer's side depends on which number is further from zero, and the big warning about misusing "two negatives make a positive" |
| 8. Glossary / 9. Check your understanding / 10. Important notes | 10 questions with hidden answers (Q9 and Q10 are conceptual); 3 common mistakes, 3 ideas to keep, and the paragraph that formally retires the Ch. 5 § 6.1 restriction |

## Terms defined here (do not define them again anywhere else)

positive number, negative number, sign, opposite, absolute value.

**Number line** is Ch. 1 § 5.2 (and Ch. 2 § 4.2); § 2.1 links. **Magnitude** is Ch. 2 § 2.4;
§ 2.3 links to it and gives *absolute value* as the version with direction removed - it does
**not** redefine magnitude. **Subtraction** and **difference** are Ch. 5 § 6.1.
**Multiplication**, **factor**, **product** and the **commutative property** are Ch. 6 § 1.
**Brackets** are Ch. 6 § 1.2. The **distributive property** is Ch. 6 § 2.4. **Inverse
operations** are Ch. 8 § 1.1. The glossary ends with a Note listing all of these with links.

## Formulas and facts that live here

* $10 - 15 = -5$ (§ 1.2) - the first calculation in the book with an answer below zero
* $|-5| = 5$ and $|5| = 5$ (§ 2.3)
* further right on the line $\Rightarrow$ greater (§ 3.1) - the only comparison rule
* $a + (-b) = a - b$ (§ 4.3)
* $a - (-b) = a + b$ (§ 4.4)
* $a \times (-b) = -(a \times b)$ and $(-a) \times b = -(a \times b)$ (§ 5.1)
* $(-a) \times (-b) = a \times b$ (§ 5.2)
* $\frac{-a}{b} = -\frac{a}{b}$, $\frac{a}{-b} = -\frac{a}{b}$, $\frac{-a}{-b} = \frac{a}{b}$
  (§ 6.1)
* The § 5.2 proof, which is the chapter's best piece of reasoning:
  $(-2) \times 0 = 0$, and $0 = 3 + (-3)$, so $(-2) \times 3 + (-2) \times (-3) = 0$, so
  $-6 + (-2) \times (-3) = 0$, so $(-2) \times (-3) = 6$
* Worked numbers, all checked with Python before they were written down:
  $5 + (-2) = 3$; $50 + (-10) = 40$; $-3 + (-4) = -7$; $5 - (-2) = 7$; $12 - (-8) = 20$;
  $-8 - (-5) + (-3) = -6$ (via $-8 + 5 = -3$, then $-3 - 3 = -6$);
  $5 \times (-2) = -10$; $6 \times (-3) = -18$; $(-4) \times (-6) = 24$;
  $\frac{15}{-3} = -5$; $\frac{-15}{-3} = 5$; $\frac{-36}{-4} = 9$;
  $\frac{(-4) \times (-6)}{-3} = -8$
* The § 4.4 pattern table: $5 - 2 = 3$, $5 - 1 = 4$, $5 - 0 = 5$, $5 - (-1) = 6$, $5 - (-2) = 7$
* The § 5.2 pattern (fig_08): first factor $3, 2, 1, 0, -1, -2, -3$ against $-2$ gives
  $-6, -4, -2, 0, 2, 4, 6$
* Questions (§ 9): $-4 + 9 = 5$; $-7 < -3$; $6 \times (-3) = -18$; $12 - (-8) = 20$;
  $\frac{-36}{-4} = 9$; $-15 + (-7) - (-10) = -12$;
  $\frac{(-6) \times (-4)}{-2 + (-6)} = \frac{24}{-8} = -3$;
  temperature $-5 + 12 = 7$, then $7 - 9 = -2$; Q9 asks *why* $(-1) \times (-3) = 3$;
  Q10 is the $-2 + (-5) = 7$ mistake, answer $-7$

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_below_zero.png | fig_01_below_zero.py | Three panels with the same skeleton - a vertical scale, a grey dashed zero line, an orange marker below it: a thermometer at $-5\,^\circ$C, a bank balance bar at $-10$, and a blue-filled sea with a depth of $-3$ m |
| fig_02_number_line.png | fig_02_number_line.py | The number line from $-6$ to $6$, orange band left of zero and blue band right of it, both halves named, zero labelled "neither one nor the other", and a smaller-to-larger arrow along the bottom |
| fig_03_opposites.png | fig_03_opposites.py | $5$ and $-5$ as filled dots, with two measuring arrows of identical length running out from zero, each labelled "5 steps from zero" |
| fig_04_comparing.png | fig_04_comparing.py | $-5$ and $-2$ on a line from $-7$ to $2$, a black arrow between them labelled "further right, so greater", debt labels underneath, and two verdict boxes - red $-5 > -2$, green $-2 > -5$ |
| fig_05_walking.png | fig_05_walking.py | Two number lines. Top: $5 + (-2) = 3$, two purple hops left. Bottom: $-4 + 9 = 5$, nine purple hops right across zero. Hollow circle = start, filled circle = finish |
| fig_06_subtracting_a_negative.png | fig_06_subtracting_a_negative.py | $5 - (-2)$ as a gap: a purple bracket over all seven steps from $-2$ to $5$, and below it the same gap split into an orange $2$ and a blue $5$ |
| fig_07_five_times_minus_two.png | fig_07_five_times_minus_two.py | Five orange arrows, each two steps long, walking from $0$ to $-10$, numbered "jump 1" to "jump 5", with the repeated addition written underneath |
| fig_08_pattern.png | fig_08_pattern.py | Seven multiplications by $-2$ in a column, first factor falling from $3$ to $-3$, answers climbing by $2$ (grey $+2$ arrows between rows), a dashed line under the $0$ row, and a pale blue panel behind the three rows the pattern decides |
| fig_09_sign_grid.png | fig_09_sign_grid.py | A $2 \times 2$ grid of the sign of the answer, each cell carrying a $+$ or $-$, the word, one multiplication and one division; a red bar underneath says the grid is not for $+$ and $-$ |

Colour convention, carried on from earlier chapters with **one new meaning that is specific to
this chapter and must be kept if it grows**: blue and orange are now the two sides of zero.

* blue `#2E86DE` - positive numbers, the right-hand side of the line, a positive answer
* orange `#E67E22` - negative numbers, the left-hand side of the line, a negative answer, and
  the jumps in fig_07
* grey `#78909C` - zero, the line itself, and quiet labels
* purple `#8E44AD` - movement: the walk in fig_05 and the whole gap in fig_06
* green `#1E8449` - the right answer (fig_04 only)
* red `#C0392B` - the wrong answer (fig_04) and the warning bar (fig_09)

Layout lessons worth keeping:

* **`bbox_inches="tight"` does not crop these figures**, because the axes is pinned with
  `ax.set_position([0, 0, 1, 1])`. Empty space at the top of a figure has to be removed by
  reducing `H` by hand. Figures 3, 4, 6 and 7 were all shortened this way after a first look.
* **A dashed rule drawn across a figure will cut through whatever is beside the table.**
  fig_08's split line was first drawn to $x = 8.80$ and crossed the middle $+2$ arrow; it stops
  at $7.45$ now.
* **An arrow pointing at a filled bar must stop short of it.** In fig_01 the bank panel needed
  its own arrow head position (`cx + 0.34`), because the shared one landed inside the orange
  bar.
* **Do not write a caption line at a fixed low height without checking the labels above it.**
  fig_05's closing sentence first sat on top of the second line's "start" and "finish" labels.
* Every number label is drawn with mathtext (`rf"${n}$"`) so the minus sign is a real minus
  sign and not a hyphen. Do not replace these with plain strings.

## Sources used

* `old/9/negative_numbers_tutorial.md` (a written tutorial: introduction, prerequisite
  subtraction, five definitions, two main concepts - below-zero intuition and the number line -
  four rules with intuitions, six worked examples, two "visuals" (an ASCII number line and a
  sign matrix table), three common mistakes, eight practice problems with full solutions, a
  summary and a key-points list).

## Material in the source that was deliberately skipped, because the book already has it

* **The number line itself** - Ch. 1 § 5.2 and Ch. 2 § 4.2. The source defines it in its
  definitions list; § 2.1 links and only draws the new half.
* **Basic subtraction with positive numbers** ($10 - 3 = 7$) - Ch. 5 § 6. The source spends a
  whole "prerequisite knowledge" section on it; § 1.1 uses it in three lines as the set-up for
  the question the chapter answers.
* **Multiplication as repeated addition** - Ch. 6 § 1.1. § 5.1 links and applies it.
* **That the order of two factors does not matter** - Ch. 6 § 1.3. The source states
  $a \times (-b)$ and $(-a) \times b$ as two separate rules; § 5.1 gives one rule and a swap.
* **What brackets mean** - Ch. 6 § 1.2. § 4.2 makes the opposite point instead: the brackets in
  $5 + (-2)$ are *not* those brackets.
* **That a fraction bar is a division** - Ch. 1 § 2.2. § 6.1 links.
* **Inverse operations** - Ch. 8 § 1.1. § 6.1 links, and uses it to justify the division signs.
* **Magnitude** - Ch. 2 § 2.4. § 2.3 links rather than redefining it.

## Additions made because the source uses them without explaining them

* **The two jobs of the minus sign** (§ 4.2). The source writes $5 + (-2)$ from its first
  example and never says why the brackets are there, or that the same symbol is doing two
  different things. Nothing else in the chapter reads properly until this is said.
* **"A minus sign means the opposite of"** (§ 2.2). The source defines a negative number only
  as "less than zero, written with a minus sign". The opposite-of reading is what makes § 4.4
  and § 5.2 explainable, so it is introduced early and used three times.
* **The walk along the line** (§ 4.1, fig_05). The source's solutions say "starting at $-8$ and
  moving $5$ units right", but the idea is never set up. § 4.1 sets it up once and the rest of
  the chapter uses it.
* **The word *sign*** (§ 1.3). The source uses it constantly ("Input Signs", "the negative
  signs cancel") without defining it.
* **The absolute-value bars** $|-5|$ (§ 2.3). The source names *absolute value* in its
  definitions but never writes the notation. One line was added, because the reader will meet
  it elsewhere.
* **"Size first, sign last" as a stated method** (§ 5.3, § 6.1). The source does this in its
  examples but never names it as the method.

## Corrections and simplifications made to the source

* **The circular proof of negative times negative was replaced.** The source argues
  $(-5) \times (-2) = (-1 \times 5) \times (-1 \times 2) = (-1 \times -1) \times (5 \times 2)$,
  which assumes $(-1) \times (-1) = 1$ - the very thing being shown. § 5.2 uses the countdown
  pattern (fig_08) as the reason, keeps the turn-round-twice idea only as a labelled memory
  aid, and adds a real proof from the distributive property.
* **The source's own summary contradicts its rule.** Its section 11 says "Subtracting a
  negative is the same as subtracting a positive: $a - (-b) = a + b$". The words say
  *subtracting*; the formula says *adding*. The book says *adding* everywhere.
* **A mismatched example was fixed.** The source compares $-2$ and $-5$, then explains it with
  "owing $2$ means you have more money than owing $20$ ($-20$)". § 3.2 uses $-5$ throughout.
* **Both ASCII number lines were dropped.** No ASCII art in the book (CLAUDE.md § 7). They
  became fig_02 and fig_06.
* **The source's separate "worked examples" section was dissolved**, as in Chapters 7 and 8.
  Each example now sits in the section that needs it: $5 + (-2)$ in § 4.3, $5 - (-2)$ in § 4.4,
  $-8 - (-5) + (-3)$ in § 4.5, $5 \times (-2)$ in § 5.1, $6 \times (-3)$ and
  $(-4) \times (-6)$ in § 5.3, the divisions in § 6.1, and the mixed one in § 6.2.
* **The sign matrix was split in two.** The source's single table mixes $+$, $-$, $\times$ and
  $\div$ in one grid, which is exactly what its own Mistake 3 warns against. § 7 has one table
  for adding and subtracting and a separate one for multiplying and dividing, with fig_09
  covering only the second.
* **The source's "Result Sign: Depends on magnitudes" row was turned into a sentence.** § 7
  says plainly that after the signs are cleared the answer sits on the side of whichever number
  is further from zero, with $5 - 2$ and $2 - 5$ as the two cases.
* **The three "common mistakes" were used twice.** Each one is placed as a Warning at the point
  where the reader could make it (§ 3.3, § 4.3, § 6.2), and then collected again in § 10.
  Mistake 3 also became question Q10.
* **Currency symbols were removed from the running text.** The source writes $\$50$ and
  $\$10$; a dollar sign fights with the maths delimiters on GitHub, so the book writes "You
  have $50$ in the bank" and lets the context carry the money.

## Not covered yet - waiting for a source

* **The order of operations** (PEMDAS / BODMAS). Still open from Chapters 6, 7 and 8. § 4.5
  works left to right and § 6.2 leans on the fraction bar's grouping, but the general rule has
  never been stated. This is now the most obvious hole in the book.
* **Negative fractions and negative decimals.** § 1.3 mentions $-2.5$ once in the definition
  and the chapter never returns to it. Every calculation here uses whole numbers.
* **Negative numbers inside the written methods** - a column subtraction that goes below zero,
  or a long division with a negative dividend. § 5.3 and § 6.1 say the digits are worked out as
  in Chapters 7 and 8 and the sign is written in front, but no full worked example exists.
* **Multiplying or dividing three or more negative numbers**, and the odd/even rule for counting
  minus signs. The chapter always has exactly two numbers at a time.
* **Adding two negative numbers where a column carry is involved**, e.g. $-48 + (-76)$.
* **The absolute value as an operation** ($|3 - 8| = 5$). § 2.3 only applies the bars to a
  single number.
* **Why $|x|$ matters later** - distance between two points, $|a - b|$. Not raised.
* **Subtracting a bigger positive from a smaller one inside a real problem**, such as a
  temperature drop crossing zero, appears only in Q8. There is no worked example in the body.
* **Division by zero.** Still untouched, as in Chapter 8.
* **Square roots of negative numbers**, and why they are a different kind of problem. Nothing
  in the book mentions them.
* **Estimation**, still open from Chapters 5, 7 and 8.
