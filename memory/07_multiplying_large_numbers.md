# Chapter 7 - Multiplying large numbers

File: [7_Multiplying_Large_Numbers/7_Multiplying_Large_Numbers.md](./../7_Multiplying_Large_Numbers/7_Multiplying_Large_Numbers.md)

Folder name and title match. Both are fixed - do not rename either.

This is the chapter Chapter 5 and Chapter 6 both said was still missing: **long
multiplication in columns**. Chapter 5 gave the columns, Chapter 6 gave the split, and
Chapter 7 puts them together. The whole chapter is built on one claim, made in § 5: the two
rows of the written method **are** the two terms of the distributive property, so the
algorithm is not a new rule.

## Sections

| Section | Contains |
| --- | --- |
| 1. Two large numbers at once | 1.1 what Ch. 6 § 5 could already do (one factor a single digit), $6 \times 345$ recalled in one line; 1.2 $425 \times 12$ - splitting still works but you must invent the split every time, and $789 \times 47$ is where that hurts; 1.3 *algorithm* recalled from Ch. 5 § 1.3, and the promise of two tools (written and head) that always agree |
| 2. Multiplying by 10, 100, 1000 | 2.1 **why** $\times 10$ moves every digit one place left, derived from Ch. 2 § 2.2 and checked with $14 = 10 + 4$, fig_01; the zero named as the place holder of Ch. 2 § 3.3; 2.2 $100$ and $1000$, the count-the-zeros table, the note on *powers of ten*, and the **warning that the short cut is whole numbers only** ($2.5 \times 10 = 25$); 2.3 $20 = 2 \times 10$, justified by the associative property (Ch. 6 § 1.4), $425 \times 20 = 8500$ and $316 \times 20 = 6320$ |
| 3. Multiplying by one digit, in columns | 3.1 set-up and why right to left, both linked to Ch. 5 § 3; 3.2 $321 \times 3 = 963$ with no carrying, checked against the Ch. 6 split; 3.3 $425 \times 2 = 850$ with the carry, fig_02, the trade linked to Ch. 5 § 2.4; 3.4 the warning **multiply first, then add the carry**, with the wrong version $(2+1) \times 2 = 6$ giving $860$, and the reason (the carry belongs to the answer, not to $425$); 3.5 $316 \times 5 = 1580$, and why $15$ may be written in the leftmost column (Ch. 5 § 5) |
| 4. The standard method, two-digit multiplier | 4.1 $12 = 10 + 2$ and the distributive property (Ch. 6 § 2.4), then *partial product* defined; 4.2 the five steps, *place holder* defined, and the warning that the rows are added and never multiplied; 4.3 $14 \times 11 = 154$, where both rows come from the same $14 \times 1$ and only the place holder separates them; 4.4 $425 \times 12 = 5100$, fig_03, with the final addition worked column by column; 4.5 $316 \times 25 = 7900$, where both digits carry |
| 5. Why the method works | 5.1 the rectangle, fig_04, linked to Ch. 6 § 3 rather than re-derived; 5.2 fig_05, and the point that matters: without the place holder $425 \times 12$ silently becomes $425 \times 3 = 1275$; 5.3 the zeros rule as a four-row table (ones / tens / hundreds / thousands), then $213 \times 124 = 26412$ with three rows, fig_06 |
| 6. The same multiplication in your head | 6.1 the method is Ch. 6 § 5 with the split taken from the places; 6.2 $14 \times 11$; 6.3 $425 \times 12$, plus the friendly addition $4250 + 850 = 4250 + 750 + 100$ and **why $750$**; 6.4 $316 \times 25$ added as $6320 + 1000 + 580$; 6.5 the warning that the split uses $+$ and not $\times$, with $425 \times (10 \times 2) = 8500$ |
| 7. Choosing a method, and checking | 7.1 the five-row comparison table; 7.2 check by taking the other road, linked to Ch. 6 § 2.3, plus the warning that repeating the same route repeats the same mistake |
| 8. Glossary / 9. Check your understanding / 10. Important notes | 8 questions with hidden answers (3 of them conceptual: Q6 how many rows and zeros without multiplying, Q7 the times-instead-of-plus split, Q8 the carry added too early); 3 common mistakes, 3 ideas to keep, and how Ch. 2, 5, 6 and 7 fit together |

## Terms defined here (do not define them again anywhere else)

partial product, place holder **in multiplication** (the term itself is Ch. 2 § 3.3 and § 2.1
links back to it), standard method / standard algorithm, powers of ten.

**Algorithm is NOT defined here** - it is Ch. 5 § 1.3. **Multiplication, factor, product,
brackets, the associative property, the distributive property and area** are all Chapter 6.
**Carrying** is Ch. 2 § 6.5, the **trade** is Ch. 5 § 2.4, **place value** and the **rule of
ten** are Ch. 2 § 2.1 and § 2.2.

## Formulas and facts that live here

* $\times 10$ moves every digit one place to the left; the $0$ that appears is a place holder
  (§ 2.1). $\times 100$ moves two places, $\times 1000$ three (§ 2.2)
* $425 \times 20 = (425 \times 2) \times 10 = 8500$ (§ 2.3); $316 \times 20 = 6320$
* A column with a carry is $(\text{digit} \times \text{digit}) + \text{carry}$, never
  $(\text{digit} + \text{carry}) \times \text{digit}$ (§ 3.4)
* $425 \times 12 = (425 \times 10) + (425 \times 2)$ (§ 4.1)
* Zeros rule (§ 5.3): a row ends with as many zeros as there are places between its digit and
  the ones place - ones $0$, tens $1$, hundreds $2$, thousands $3$
* Worked numbers, all checked with Python before they were written down:
  $14 \times 10 = 140$; $23 \times 10 = 230$, $23 \times 100 = 2300$, $23 \times 1000 = 23000$;
  $321 \times 3 = 963$; $425 \times 2 = 850$ (wrong version $860$); $316 \times 5 = 1580$;
  $14 \times 11 = 154$; $425 \times 12 = 5100$ (rows $850$ and $4250$; wrong version $1275$,
  which is $425 \times 3$; gap $3825$); $316 \times 25 = 7900$ (rows $1580$ and $6320$);
  $213 \times 124 = 26412$ (rows $852$, $4260$, $21300$; $852 + 4260 = 5112$);
  $425 \times (10 \times 2) = 8500$
* Questions (§ 9): $18 \times 11 = 198$; $34 \times 12 = 408$ (rows $68$, $340$);
  $215 \times 14 = 3010$ (rows $860$, $2150$); $412 \times 21 = 8652$ (rows $8240$, $412$);
  $524 \times 35 = 18340$ (rows $2620$, $15720$); $3471 \times 268$ - three rows, $0$ / $1$ /
  $2$ zeros, no multiplying needed

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_times_ten_shift.png | fig_01_times_ten_shift.py | A hundreds / tens / ones chart. Top row $14$, bottom row $140$, with two curved arrows showing each digit stepping one place left and an orange $0$ filling the ones place |
| fig_02_one_digit_column.png | fig_02_one_digit_column.py | Left: $425 \times 2$ in columns with the small orange carried $1$. Right: the three steps in order, in four aligned text columns (number, place name, sum, action) |
| fig_03_two_partial_products.png | fig_03_two_partial_products.py | $425 \times 12$ in full. The $2$ of $12$ and the row $850$ are blue, the $1$ and the row $4250$ are orange, the place-holding $0$ is larger and named by an arrow coming in from the lower right |
| fig_04_rectangle_425_by_12.png | fig_04_rectangle_425_by_12.py | A $425 \times 12$ rectangle cut at height $10$: blue $4250$ above, orange $850$ below, three height marks ($10$, $2$, and $12$ for the pair), and the sum $5100$ in a side box |
| fig_05_missing_zero.png | fig_05_missing_zero.py | Two panels. Red: second row written $425$, answer $1275$, captioned "this is really $425 \times 3$". Green: second row $4250$ with the orange place holder, answer $5100$ |
| fig_06_three_rows.png | fig_06_three_rows.py | $213 \times 124$ with three rows - $852$ blue, $4260$ orange, $21300$ purple - the place-holding zeros in bold, and "no zeros / one zero / two zeros" beside them |

Colour convention: the same as chapters 1 to 6. Blue `#2E86DE` for the first part of a split,
orange `#E67E22` for the second part **and for the place-holding zero** (it is the piece that
appears, exactly as in Ch. 5), purple `#8E44AD` for the third part (the hundreds row of
fig_06, matching Ch. 6 fig_06), red `#C0392B` for the wrong method and green `#1E8449` for the
right one (fig_05 only).

Figures 2, 3, 5 and 6 use the Chapter 2 fig_07 trick: `ax.set_position([0, 0, 1, 1])` so one
axis unit is one inch, which lets single mono-spaced digits be placed by hand
(`CH = FS / 72 * 0.602`). Do not change those figure sizes without changing the coordinates.

Four layout lessons worth keeping:

* **Never pad a text column with spaces to line it up.** The maths is set in mathtext, not in
  a mono-spaced font, so spaces do not align. fig_02 fixes four x positions by hand
  (`NUM_X`, `NAME_X`, `SUM_X`, `ACT_X`) instead.
* **A row whose last digit must be a different colour is written one character at a time.**
  fig_03, fig_05 and fig_06 all do this. Printing an orange `0` on top of a green `0` leaves a
  visible coloured ring around it - it was tried in fig_05 and removed.
* **An arrow must approach through empty page.** fig_03's place-holder arrow comes in from the
  lower right, so it crosses neither a digit nor the line under the rows. The first version
  came from the left and cut straight through the addition line.
* **fig_04 is deliberately not to scale in both directions.** The two heights ($10$ and $2$)
  keep their true proportion, but $425$ beside $12$ would be a hair-thin ribbon, so the width
  is squashed. The picture and the caption both say so. A third height mark, $12$ for the two
  pieces together, is what makes it read as one rectangle cut in two rather than two boxes.

## Sources used

* `old/7/multiplication-of-large-numbers-manual.md` (a written manual: introduction,
  prerequisite knowledge, six definitions, two main concepts with the connection between them,
  the distributive formula and the zero-placeholder rule, three worked examples each done both
  ways, a method-comparison table and an ASCII flowchart, three common mistakes, five practice
  problems with solutions, a summary and a key-points list).

## Material in the source that was deliberately skipped, because the book already has it

* **Multiplication, factors, products** - Ch. 6 § 1.1. The source's definitions section
  repeats them; § 1.1 links instead.
* **The distributive property itself**, its formula and its three-term form - Ch. 6 § 2.4 and
  § 4.2. § 4.1 uses the rule and links; it does not re-derive it.
* **Algorithm** - Ch. 5 § 1.3.
* **The area model as an idea, and why a cut cannot create or destroy squares** - Ch. 6 § 3.
  § 5.1 applies it to $425 \times 12$ in four lines and links back for the proof.
* **Place value, and a number written as a sum of its places** - Ch. 2 § 2.1, Ch. 5 § 2.3.
* **Column addition with carrying** - Ch. 5 § 4. Every "add the partial products" step links
  there; the addition itself is still worked column by column, because those are new numbers.
* **The source's flowchart for $425 \times 12$** (split into $10 + 2$, two branches, add) was
  **not** drawn. Chapter 6 fig_06 is already exactly that shape for $6 \times 345$, and
  redrawing it would be the repetition this book exists to avoid.
* **The "two roads must agree" check** - Ch. 6 § 2.3. § 7.2 links and adds only the part that
  is new: a check is worthless if the second road is the same as the first.

## Additions made because the source uses them without explaining them

* **Why multiplying by ten adds a zero.** The source lists it as prerequisite knowledge in one
  line: "adding a zero to the right of any whole number". Nothing in the book had explained
  it - Ch. 6 § 5.3 only said "with zeros stuck on the end". § 2.1 derives it from the rule of
  ten, checks it with $14 = 10 + 4$, and names the zero as a place holder.
* **Multiplying by 20.** The source's own examples need $425 \times 20$ and $316 \times 20$,
  but it never says how to do one. § 2.3 gives it, and justifies the regrouping with the
  associative property.
* **Multiplying by one digit in columns.** The source jumps straight to the two-digit
  algorithm and does the single-digit row inside it. Section 3 does that row on its own first,
  with a no-carry example before the carry example, so that section 4 has nothing new in it
  except the place holder.
* **Why the carry must be added after the multiplying.** The source says "order of operations
  requires multiplication before addition" - but the book has not taught the order of
  operations, only brackets. § 3.4 gives the real reason instead: the carried digit came out
  of the previous column, so it belongs to the answer, not to the number being multiplied.
  Multiplying it too would count it twice.
* **What the missing zero actually costs.** The source says the answer is wrong. § 5.2 shows
  that the wrong answer $1275$ is exactly $425 \times 3$: without the place holder the bottom
  number stops being $12$ and becomes $1 + 2 = 3$.
* **A worked three-digit multiplier.** The source states the $k-1$ zeros rule for the hundreds
  place but never works an example with three rows. § 5.3 adds $213 \times 124$ and fig_06.
* **Why $750$.** The source's mental short cut $4250 + 850 = 4250 + (750 + 100)$ appears with
  no explanation. § 6.3 says why: $4250$ needs exactly $750$ to reach the round $5000$.
* **Powers of ten.** The source uses the phrase in a heading and never explains it. § 2.2 has
  a one-line note, because the reader will meet the words elsewhere.

## Corrections and simplifications made to the source

* **The $k-1$ zeros rule was rewritten without $k$.** The source states it as "insert $k-1$
  zero placeholders where $k$ is the place position". Index notation is not in the book and
  buys nothing here. § 5.3 gives the same rule in words plus a four-row table.
* **The "$25 = \frac{100}{4}$" remark was dropped.** The source opens its third example's
  mental method with it and then never uses it - it splits $25$ as $20 + 5$ like everything
  else. Dividing by four as a short cut is not taught anywhere in the book, so the sentence
  would have raised a question it did not answer.
* **The ASCII flowchart was not reproduced in any form.** No ASCII art in the book (§ 7 of
  CLAUDE.md), and the figure it would have become already exists as Ch. 6 fig_06.
* **"Units" was written as "ones" throughout**, as in Chapter 5.
* **Brackets were kept on the right-hand side of every rule**, as Ch. 6 decided:
  $(425 \times 10) + (425 \times 2)$, never $425 \times 10 + 425 \times 2$. The order of
  operations is still not taught. **If a later transcript teaches it, that is the place to
  relax this.**
* **The dot was replaced by $\times$** in the distributive formula, matching Ch. 6 § 1.1.
* **A whole-numbers-only warning was added to the $\times 10$ short cut.** The source says
  "adding a zero to the right of any whole number" and stops. Because this book taught
  decimals in Chapter 2, a reader could reasonably try $2.5 \times 10 = 2.50$. § 2.2 warns in
  three sentences that only the digit shift is always true.
* **The source's separate "worked examples" section was dissolved.** Each example was placed
  where it teaches something: $425 \times 2$ in § 3.3, $316 \times 5$ in § 3.5,
  $14 \times 11$ in § 4.3, $425 \times 12$ in § 4.4, $316 \times 25$ in § 4.5, and the mental
  versions of all three in § 6. Doing every example twice, once per method, is exactly the
  repetition rule § 5.3 forbids.

## Not covered yet - waiting for a source

* **The full order of operations** (PEMDAS / BODMAS). Still open from Chapter 6. Every rule in
  this chapter keeps its brackets.
* **Multiplying decimals**, including $2.5 \times 10$. § 2.2 warns that the zero short cut
  fails for decimals but does not teach the decimal case. Ch. 4 § 6.1 multiplies a decimal by
  a whole number; two decimals are still missing.
* **Estimation**, so that an answer can be checked for size ("about $400 \times 12$, so about
  $4800$"). § 7.2 checks by redoing the work a second way, which is the only check the source
  offers. Still open from Chapter 5.
* **Long division**, and division by a two-digit number. Still open from Chapter 5.
* **Two brackets multiplied together**, $(a + b) \times (c + d)$, and the four partial
  products that come with it. This chapter multiplies a multi-digit number by a multi-digit
  number, which is the arithmetic version of exactly that, but the algebraic form is not
  taught and FOIL is not mentioned.
* **The lattice method, doubling and halving, and other multiplication short cuts.** The
  source teaches two methods only.
* **Negative numbers**, so a negative factor is out of scope, as in every chapter so far.
* **Place values above ten thousands.** § 4.5 and § 9 Q5 reach ten thousands; nothing names a
  place beyond that. Ch. 5 § 2.2 is still the last word on the place names.
