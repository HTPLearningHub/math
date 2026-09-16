# Chapter 8 - Dividing large numbers

File: [8_Dividing_Large_Numbers/8_Dividing_Large_Numbers.md](./../8_Dividing_Large_Numbers/8_Dividing_Large_Numbers.md)

Folder name and title match. Both are fixed - do not rename either.

This is the chapter Chapter 5 and Chapter 7 both listed as still missing: **long division**.
It completes the four operations. The chapter is built on one claim, made in § 1.3 and § 1.4
and used everywhere after: a leftover in division is cut into ten smaller pieces and drops to
the place on the **right**, which is the mirror image of the carry in Chapters 2, 5 and 7, and
is the reason division alone runs left to right.

## Sections

| Section | Contains |
| --- | --- |
| 1. Sharing a large number | 1.1 $15 \div 5$ is a times-table fact read backwards, **inverse operations** defined with $a \times b = c \Rightarrow c \div b = a$, linked forward to the Ch. 1 § 1.1 check; 1.2 $625 \div 3$ has no times-table line, so we need an *algorithm* (Ch. 5 § 1.3); 1.3 $624$ as $6$ hundreds / $2$ tens / $4$ ones shared between $3$, fig_01, the two lessons (nothing is lost; the leftover moves right, which is Ch. 5 § 2.4 walked backwards); 1.4 fig_02, why multiplying runs right to left and dividing runs left to right, plus the warning that it is not a matter of taste |
| 2. The division bracket | 2.1 the four words recalled and linked, **long division** defined (*long* = written out in full); 2.2 **division bracket** (tableau) defined, fig_03, and the note that every quotient digit sits directly above the dividend digit it came from |
| 3. The four steps that repeat | fig_04, the ring; the four steps in words; **working number** defined; the Dad / Mum / Sister / Brother memory aid as a Note; when to stop |
| 4. A first division: $624 \div 3$ | 4.1 - 4.3 one subsection per turn of the loop (hundreds, tens, ones), with the $0$ written in turn two and the link back to fig_01's counters; fig_05 shows the finished tableau colour-coded by step; 4.4 the check $208 \times 3 = 624$ worked column by column, linked to Ch. 7 § 3 |
| 5. When something is left over: $625 \div 3$ | 5.1 the same three turns, last subtraction $25 - 24 = 1$; 5.2 $0 \leq \text{remainder} < \text{divisor}$ with the reason and the $25 \div 3 = 7$ r $4$ warning; 5.3 the division equation, its symbol list, and the note that it is Ch. 1 § 5.3's $N = (W \times D) + R$ renamed; 5.4 fig_06, the skipped zero, linked to Ch. 2 § 3.3 and Ch. 7 § 5.2 |
| 6. Dividing by a two-digit number: $397 \div 11$ | 6.1 take two digits when the divisor will not fit one; the quotient digit goes above the **last** digit taken; the note that a **leading** zero is not written, unlike the zero inside $208$; 6.2 count up in elevens and step back one; 6.3 the two turns, fig_07; 6.4 the check $(36 \times 11) + 1 = 397$ |
| 7. Going past the point: a decimal answer | 7.1 the idea is Ch. 4 § 2.3, linked, not re-derived; 7.2 the three additions to the layout and the warning about the point's column; 7.3 tenths and hundredths of $397 \div 11$, fig_08, $36.\overline{09}$; 7.4 the stopping rule - leftover $0$ stops, a repeated leftover repeats - and the note to write leftovers down |
| 8. Three ways to write one answer | the three-row table for $625 \div 3$; $\frac{\text{dividend}}{\text{divisor}} = \text{quotient} + \frac{\text{remainder}}{\text{divisor}}$ as Ch. 1 § 5.3 read backwards; which form suits which job, linked to Ch. 4 § 1.2; the warning that a written-out repeating decimal is always shortened |
| 9. Glossary / 10. Check your understanding / 11. Important notes | 8 questions with hidden answers (5 of them conceptual: Q4 why the zero, Q5 remainder too big **and the fact that the division equation does not catch it**, Q6 why the direction differs, Q7 checking someone else's answer, Q8 predicting the repeat); 3 common mistakes, 3 ideas to keep, and the note that this is the last of the four operations |

## Terms defined here (do not define them again anywhere else)

inverse operations, long division, division bracket (tableau), working number, bring down.

**Dividend, divisor, quotient and remainder are NOT defined here** - they are Ch. 1 § 1.2 and
§ 5.3, and § 2.1 links back. **Algorithm** is Ch. 5 § 1.3. **Place holder** is Ch. 2 § 3.3.
**Terminating decimal**, **repeating decimal** and the **bar notation** are Ch. 4 § 2.3 and
§ 2.4. **Place value** and the **rule of ten** are Ch. 2 § 2.1 and § 2.2. **Carrying** is
Ch. 2 § 6.5; the **trade** is Ch. 5 § 2.4; **borrowing** is Ch. 5 § 6.3.

## Formulas and facts that live here

* $a \times b = c \Rightarrow c \div b = a$ (§ 1.1) - the first statement of inverse operations
  in the book
* $0 \leq \text{remainder} < \text{divisor}$ (§ 5.2), with the reason: a leftover as big as the
  divisor means the divisor still fits once more
* $\text{dividend} = (\text{divisor} \times \text{quotient}) + \text{remainder}$ (§ 5.3) - the
  same equation as Ch. 1 § 5.3's $N = (W \times D) + R$
* $\frac{\text{dividend}}{\text{divisor}} = \text{quotient} + \frac{\text{remainder}}{\text{divisor}}$
  (§ 8)
* The stopping rule (§ 7.4): a leftover of $0$ terminates; a leftover seen before repeats
* Worked numbers, all checked with Python before they were written down:
  $624 \div 3 = 208$ (check $208 \times 3 = 624$);
  $625 \div 3 = 208$ r $1 = 208\frac{1}{3} = 208.\overline{3}$ (wrong version $28$, whose check
  gives $28 \times 3 = 84$);
  $397 \div 11 = 36$ r $1 = 36\frac{1}{11} = 36.\overline{09}$ (check $36 \times 11 = 396$,
  $396 + 1 = 397$; leftovers $1$, $10$, $1$);
  $25 \div 3 = 8$ r $1$, not $7$ r $4$
* Questions (§ 10): $486 \div 2 = 243$; $745 \div 4 = 186$ r $1 = 186\frac{1}{4} = 186.25$
  (leftovers $3$, $2$, $1$, $2$, $0$); $529 \div 12 = 44$ r $1 = 44\frac{1}{12} =
  44.08\overline{3}$ (leftovers $4$, $1$, $10$, $4$, $4$); $936 \div 7 = 133$ r $5$, which is
  correct ($133 \times 7 = 931$, $931 + 5 = 936$)

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_share_by_place.png | fig_01_share_by_place.py | Three bands - hundreds, tens, ones - of square counters for $624$ shared between $3$, with columns for "each gets" and "left on the table". The two leftover tens travel down an orange arrow and reappear as $20$ of the $24$ orange ones in the bottom band |
| fig_02_two_directions.png | fig_02_two_directions.py | Two panels. Blue: $425$ with a right-to-left arrow, "start at the right". Orange: $624$ with a left-to-right arrow, "start at the left". Each with the one-sentence reason underneath |
| fig_03_tableau_parts.png | fig_03_tableau_parts.py | The bracket for $624 \div 3$ with the quotient $208$ on top, place names as column headings, and three labelled arrows naming divisor, dividend and quotient |
| fig_04_four_steps.png | fig_04_four_steps.py | Divide / Multiply / Subtract / Bring down as four boxes in a ring, each in its step colour, with grey arrows round the ring |
| fig_05_624_divided_by_3.png | fig_05_624_divided_by_3.py | The full tableau for $624 \div 3$, every digit in its step colour, with the three turns of the loop written out beside it |
| fig_06_zero_in_the_quotient.png | fig_06_zero_in_the_quotient.py | $625 \div 3$ twice. Red: the zero skipped, answer $28$, check $28 \times 3 = 84$. Green: the zero written, answer $208$ r $1$, check $(208 \times 3) + 1 = 625$. Place names above both |
| fig_07_397_divided_by_11.png | fig_07_397_divided_by_11.py | The tableau for $397 \div 11$ with a dashed blue box round the first working number $39$, the commentary beside it, and the eleven times table as nine boxes along the bottom with $33$ and $66$ in orange |
| fig_08_repeating_remainder.png | fig_08_repeating_remainder.py | $397 \div 11$ carried to two decimal places. The two leftovers of $1$ are circled in red and joined by a red path routed down the empty left-hand side of the tableau; a red panel on the right explains why it repeats |

Colour convention: chapters 1 to 7 carry over, plus **one new convention that is specific to
this chapter and should be kept if it grows**: the four steps each own a colour, and every
written thing in a tableau is coloured by the step that produced it.

* blue `#2E86DE` - Divide, so every quotient digit
* orange `#E67E22` - Multiply, so every product written underneath (and, in fig_01 only,
  orange keeps its Chapter 5 meaning: the piece that moves)
* purple `#8E44AD` - Subtract, so every difference and every remainder
* green `#1E8449` - Bring down, so every digit just fetched from the dividend
* red `#C0392B` - the wrong method (fig_06) and the thing that repeats (fig_08)

Figures 3, 5, 6, 7 and 8 use the Chapter 2 fig_07 trick: `ax.set_position([0, 0, 1, 1])` so one
axis unit is one inch, which lets digits be placed by hand, column by column. Do not change
those figure sizes without changing the coordinates.

Five layout lessons worth keeping:

* **Do not set the digits in a mono-spaced font.** DejaVu Sans Mono draws its zero with a dot
  inside it, and this chapter turns on the reader seeing a plain zero. Every tableau uses
  `DejaVu Sans` and places each digit by hand instead. This is a deliberate break from
  Chapters 5 and 7, which used mono.
* **Keep the bracket clear of the first subtraction sign.** In fig_05 the vertical line was
  first drawn at `C[0] - 0.38`, which put it straight under the `-` of the first subtraction.
  It is now at `C[0] - 0.74`.
* **An arrow must approach through empty page.** fig_01's orange arrow runs through a corridor
  left open between the tens band and the ones band, and fig_08's red path runs down the
  left-hand columns of the tableau, which are empty in every row it passes. The first version
  of each crossed a digit.
* **Commentary blocks need a clear line of empty space between them.** fig_05's three "Turn"
  headings first overlapped the last line of the block above; the block spacing is now $2.10$
  units for four lines.
* **A label beside a tableau row will run into the commentary column.** fig_06's "with $1$ left
  over" was moved under the tableau for this reason, and fig_05's "nothing left over" with it.

## Sources used

* `old/8/long-division-tutorial.md` (a written tutorial: introduction, prerequisite knowledge,
  six definitions, the four-step cycle with a memory aid, handling zeros, extending to
  decimals, three formulas, four worked examples, an ASCII flowchart and an alignment table,
  three common mistakes, three practice problems with solutions, a summary and a key-points
  list).

## Material in the source that was deliberately skipped, because the book already has it

* **Dividend, divisor, quotient, remainder** - Ch. 1 § 1.2 and § 5.3. The source's definitions
  section repeats all four; § 2.1 links instead.
* **Place value, and a digit's value coming from its position** - Ch. 2 § 2.1 and Ch. 5 § 2.2.
  The source lists it as prerequisite knowledge.
* **Algorithm** - Ch. 5 § 1.3.
* **Repeating decimal and the bar notation** - Ch. 4 § 2.4. § 7.3 uses the bar and links; it
  does not redefine it. **Terminating decimal** - Ch. 4 § 2.3.
* **Why a leftover is cut into ten** - Ch. 2 § 2.2 and Ch. 4 § 2.3. § 7.1 states the rule in one
  sentence and links; the *reason* is not re-derived.
* **The fraction form of a remainder** - Ch. 1 § 5.3. § 8 links and only points out that the
  chapter reads it in the opposite direction.
* **Column subtraction and borrowing** - Ch. 5 § 6. Every "subtract" step relies on it silently.
* **Column multiplication** - Ch. 7 § 3. § 4.4 works the check column by column but links for
  the method.
* **The source's alignment table** (place value / quotient digit / dividend digit / working
  calculation for $625 \div 3$) was **not** reproduced. It is fig_05 in a worse form, and
  fig_03 already carries the place names as column headings.

## Additions made because the source uses them without explaining them

* **Why division runs left to right.** The source states it as a fact and compares it with
  multiplication, but gives no reason. § 1.3 and § 1.4 give it: leftovers in division travel
  right, so the left end must be settled first. fig_01 and fig_02 exist for this.
* **What the working number is.** The source says "the current working number" throughout and
  never defines it. § 3 defines it.
* **How to find a quotient digit when you do not know the times table.** The source simply
  asserts "11 fits into 39 three times". § 6.2 adds the count-up-and-step-back method, and
  fig_07 draws the eleven times table.
* **The difference between a leading zero and an interior zero.** The source says to put a $0$
  above the $3$ of $397$ "(or leave it blank)" and then prints a quotient of $036$ while calling
  the answer $36$. § 6.1 makes the distinction explicit: a zero at the front is never written, a
  zero inside always is.
* **How to know a decimal repeats.** The source observes the pattern in one example
  ("the remainder is 1 again!"). § 7.4 turns it into a rule for every division, and § 10 Q8
  asks the reader to justify it.
* **Inverse operations.** The source lists it as prerequisite knowledge with the formula. The
  book had the *idea* (check by multiplying back, Ch. 1 § 1.1) but had never named it, so
  § 1.1 defines it.
* **A worked terminating decimal inside the bracket.** All of the source's decimal examples
  repeat. § 10 Q2 carries $745 \div 4$ past the point to $186.25$, so the reader sees a leftover
  of $0$ actually arrive.

## Corrections and simplifications made to the source

* **The source's own "Accuracy Note" was dropped.** It is a paragraph about the video saying
  $624$ and writing $625$, and it solves the problem by doing both divisions. The book does both
  divisions too, but silently and for a better reason: $624 \div 3$ teaches the loop with no
  remainder (§ 4), and $625 \div 3$ then adds the remainder and the skipped-zero mistake (§ 5).
  Per CLAUDE.md § 5.2, the chapter never discusses what the source said.
* **The "$0$ times, multiply, subtract" step for a leading zero was removed.** The source's
  Example 2 writes $-0$ under the $3$ of $397$ and subtracts it. That step does nothing. § 6.1
  simply takes two digits.
* **The two ASCII tableaus and the ASCII flowchart were not reproduced in any form.** No ASCII
  art in the book (CLAUDE.md § 7). They became fig_05, fig_06, fig_07, fig_08 and fig_04.
* **The remainder-size warning was given a second half.** The source's Mistake 2 says a
  remainder must be smaller than the divisor. § 10 Q5 adds the part that makes it worth
  knowing: the division equation $(7 \times 3) + 4 = 25$ **still comes out right** for
  $25 \div 3 = 7$ r $4$, so the size check is not optional.
* **"Tableau" was kept but demoted.** The source uses it as a main term. The book calls the
  thing a *division bracket* and mentions *tableau* once, in the definition and the glossary,
  because the reader may meet the word elsewhere.
* **The source's separate "worked examples" section was dissolved**, as in Chapter 7. Each
  example was placed where it teaches something new: $624 \div 3$ in § 4, $625 \div 3$ in § 5,
  $397 \div 11$ in § 6, and the same division continued in § 7. The source's three practice
  problems became § 10 Q1 - Q3.
* **"$\text{R}$" was written out as "remainder"** in the running text, because the reader has
  not met the abbreviation. The short form appears only in the § 8 table.

## Not covered yet - waiting for a source

* **Estimation**, so that an answer can be checked for size ("about $600 \div 3$, so about
  $200$"). Still open from Chapters 5 and 7. Every check in this chapter is an exact
  recomputation.
* **Divisors of three digits or more.** § 6 reaches two digits, which is where the source stops.
* **Dividing a decimal**, and dividing **by** a decimal ($6.4 \div 0.8$). § 7 divides a whole
  number and lets the *answer* be a decimal; the dividend is never a decimal to start with.
  Still open from Ch. 2 and Ch. 4.
* **Turning a repeating decimal back into a fraction.** Still open from Ch. 4.
* **Rounding a division to a given number of decimal places**, and deciding when to round up to
  a whole item. Ch. 1 § 6 rounds up to whole pizzas as a one-off; Ch. 4 § 6.3 rounds to the
  nearest cent. Neither is connected to long division yet.
* **Why some divisions repeat and others stop**, in terms of the prime factors of the divisor.
  § 7.4 gives the rule you can see (watch the leftovers) but not the reason. Still open from
  Ch. 4 § 4.2.
* **Divisibility rules** (a number divides by $3$ when its digits add to a multiple of $3$, and
  so on). Nothing in the book mentions them.
* **Division by zero.** The source never raises it and neither does the chapter.
* **Negative numbers**, so a negative dividend or divisor is out of scope, as in every chapter
  so far.
* **The order of operations** (PEMDAS / BODMAS). Still open from Chapters 6 and 7. This chapter
  keeps its brackets, as they did: $(\text{divisor} \times \text{quotient}) + \text{remainder}$.
