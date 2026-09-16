# Chapter 5 - Adding and subtracting large numbers

File: [5_Adding_And_Subtracting_Large_Numbers/5_Adding_And_Subtracting_Large_Numbers.md](./../5_Adding_And_Subtracting_Large_Numbers/5_Adding_And_Subtracting_Large_Numbers.md)

Folder name and title match. Both are fixed - do not rename either.

This is the first chapter about **whole-number** arithmetic. Chapters 1 to 4 were about parts
of a whole (fractions, decimals, percents). Chapter 5 sits after them because that is the
order the reader's video course goes in, not because it is harder.

## Sections

| Section | Contains |
| --- | --- |
| 1. Why counting is not enough | 1.1 $2 + 3$ can be checked by pointing at apples; 1.2 $1\,293$ and $2\,614$ apples cannot, plus the note on the thousands separator (comma / thin space is not a decimal point); 1.3 *algorithm* defined, and why columns turn one hard sum into several single-digit sums |
| 2. The places to the left of the ones | 2.1 *digit* defined, ten symbols only; 2.2 walking left past the hundreds to *thousands*, fig_01, table of what one of each place is worth; 2.3 $1\,293$ written out as $(1 \times 1000) + \dots$ and added back in three steps; 2.4 the trading rule, fig_02, table of the three trades, and the naming of carrying (up) versus borrowing (down) |
| 3. Setting the numbers out in columns | 3.1 one column = one size of piece; a whole number's point sits at its right-hand end, so "line up the points" becomes "line up the last digits", fig_03; 3.2 draw the line, and why you must work right to left (leftovers always travel left) |
| 4. Adding large numbers | 4.1 *addition* and *sum*; 4.2 $524 + 315$ with no carrying; 4.3 the carrying rule in words, $1\,293 + 2\,614$ worked in four steps, fig_04, and the warning about the lost $100$; 4.4 $1\,584 + 2\,739$ where every column carries, plus the note that with two numbers the carry is always $0$ or $1$ |
| 5. Adding a long list of numbers at once | $17 + 22 + 11 + 34 + 46$; every single-digit step written out; why $13$ may be written in the leftmost column, and the alternative of carrying once more into a new hundreds column; the carry can be bigger than $1$ |
| 6. Subtracting large numbers | 6.1 *subtraction* and *difference*, the warning that order cannot be swapped, larger number on top; 6.2 $98 - 45$; 6.3 *borrowing* defined, $473 - 286$ worked in three steps, fig_05, the two packings of $473$, the check by adding back, the warning about not reducing the left digit; 6.4 covered inside 6.3 via the two sums under fig_05 |
| 7. When the column next door is a zero | $5\,042 - 2\,678$ worked in four steps, fig_06, the two-step trade through the empty hundreds, the $4000 + 900 + 130 + 12$ check and the add-back check |
| 8. Glossary / 9. Check your understanding / 10. Important notes | 8 questions with hidden answers (2 of them conceptual); 4 common mistakes, 3 ideas to keep |

## Terms defined here (do not define them again anywhere else)

algorithm, digit, thousands (the place), addition, sum, subtraction, difference,
borrowing (regrouping).

**Carrying is NOT defined here** - it belongs to Ch. 2 § 6.5, and § 4.3 links back to it.
Place value and the rule of ten are Ch. 2 § 2.1 and § 2.2.

## Formulas and facts that live here

* $1\,293 = (1 \times 1000) + (2 \times 100) + (9 \times 10) + (3 \times 1)$ (§ 2.3)
* The trade: $10$ ones $= 1$ ten, $10$ tens $= 1$ hundred, $10$ hundreds $= 1$ thousand (§ 2.4)
* Carrying rule in words: if a column reaches $10$ or more, write its right-hand digit and
  carry everything to the left of it (§ 4.3). This covers a carry of $2$ or $3$ as well (§ 5).
* Borrowing rule in words: take $1$ from the column on the left, it arrives as $10$ here (§ 6.3)
* $524 + 315 = 839$ (§ 4.2); $1\,293 + 2\,614 = 3\,907$ (§ 4.3);
  $1\,584 + 2\,739 = 4\,323$ (§ 4.4); $473 + 28 = 501$ (fig_03)
* $17 + 22 + 11 + 34 + 46 = 130$, ones column $20$, tens column $13$ (§ 5)
* $98 - 45 = 53$ (§ 6.2); $473 - 286 = 187$ (§ 6.3); $5\,042 - 2\,678 = 2\,364$ (§ 7)
* $400 + 70 + 3 = 400 + 60 + 13 = 473$ (§ 6.3, fig_05)
* $4000 + 900 + 130 + 12 = 5\,042$ (§ 7, fig_06)
* Questions: $624 - 358 = 266$, $600 - 247 = 353$, $48 + 15 + 83 + 29 + 67 = 242$ (§ 9)

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_place_value_thousands.png | fig_01_place_value_thousands.py | Four boxes - thousands, hundreds, tens, ones - holding $1$, $2$, $9$, $3$, with the "one step left $= \times 10$" arrow above and the value of each digit below |
| fig_02_ten_make_one.png | fig_02_ten_make_one.py | Three rows of ten blue tokens, each trading for one larger orange token: ones to a ten, tens to a hundred, hundreds to a thousand |
| fig_03_align_on_the_right.png | fig_03_align_on_the_right.py | $473 + 28$ in two panels: lined up on the left gives $753$ (red), lined up on the right gives $501$ (green); both panels carry the same rotated column names |
| fig_04_carrying_the_ten.png | fig_04_carrying_the_ten.py | Left: ten ten-tokens become one hundred-token plus a $0$. Right: the $1\,293 + 2\,614$ column sum with the carried $1$ and the $0$ in orange |
| fig_05_borrowing_one_ten.png | fig_05_borrowing_one_ten.py | $473$ as blocks, twice: $4$ / $7$ / $3$ above, and $4$ / $6$ / $13$ below with the ten new ones in orange; the two sums under the rows both give $473$ |
| fig_06_borrowing_across_a_zero.png | fig_06_borrowing_across_a_zero.py | A four-column table with three rows - $5,0,3,12$ then $4,10,3,12$ then $4,9,13,12$ - changed cells orange, empty cell grey, one sentence per row on the right |

Colour convention: the same as chapters 1 to 4. Blue `#2E86DE` for pieces that were already
there, **orange `#E67E22` for the piece that moves** (the traded hundred, the carried digit,
the borrowed ones, the changed cells), grey `#ECEFF1` / `#78909C` for an empty or used-up
column, red `#C0392B` for the wrong method and green `#1E8449` for the right one - red and
green only in the wrong-versus-right panels of fig_03, exactly as in Ch. 2 fig_07.

Figures 3 and 4 use Chapter 2 fig_07's trick: `ax.set_position([0, 0, 1, 1])` so that one axis
unit is one inch, which lets single mono-spaced digits be placed by hand
(`CH = FS / 72 * 0.602`). Do not change those figure sizes without changing the coordinates.
Figure 4 also sets `ylim` to start at `Y_BOTTOM` so the units stay inches after the height was
trimmed.

Two layout lessons that cost a re-render and are worth keeping:

* An arrow must never be routed across a digit. In fig_03 the "wrong" arrow runs horizontally
  through empty space on the left, and the right-hand panel has no arrow at all - the rotated
  column names do that job.
* Never overprint one glyph on another to recolour it. Fig_04 writes the answer `3907` one
  character at a time, each centred on its own column, so the `0` can be orange cleanly.
  A pale highlight band down a column was also tried and removed: any band wide enough to see
  also touched the digits beside it.

## Sources used

* `old/5/addition-and-subtraction-of-large-numbers.md` (a written tutorial: introduction,
  prerequisite place value, seven definitions, five main concepts, formulas and regrouping
  rules, three worked examples, visual explanations, four common mistakes, six practice
  problems with solutions, a summary and a key-points list).

## Material in the source that was deliberately skipped, because the book already has it

* Place value, and the idea that a digit's value comes from its position - Ch. 2 § 2.1.
  Chapter 5 links back and only adds the **thousands** place, which Ch. 2 never reached.
* The rule of ten (each place is ten times the one on its right) - Ch. 2 § 2.2.
* Carrying as an idea, and the "ten small pieces make one bigger piece" reasoning behind it -
  Ch. 2 § 6.5. § 4.3 restates the rule in one sentence and links; it does not re-explain why.
* "You can only add pieces of the same size", the reason columns must match - Ch. 2 § 6.1.
  § 3.1 links, then adds the part that is new: a whole number's point is at its right-hand end,
  so the rule becomes "line up the last digits".

## Additions made because the source uses them without explaining them

* **The thousands separator.** The source writes $1,293$ throughout and never says what the
  comma is. § 1.2 has a note: it only groups digits for reading, and it is not a decimal
  point. The book itself uses the thin space $1\,293$, to match `$100\,000$` in Ch. 2 § 2.4
  and to avoid any collision with the decimal point the reader already learned.
* **Why right to left.** The source states the rule ("always calculate from right to left")
  without a reason. § 3.2 gives it: leftovers always travel left, so a column finished from the
  right never has to be changed again.
* **Why the carried digit is a $1$ and not a $10$.** The source never addresses this, and it
  is the thing a beginner finds strangest. § 9 Question 4 answers it: the digit is written in a
  place worth ten times more.
* **Checking by adding the answer back on.** The source only mentions "verify by counting" for
  $2 + 3$. § 6.3 and § 7 check each subtraction by addition, linking to the check-by-multiplying
  idea in Ch. 1 § 1.1. Every check is worked out digit by digit in the text.

## Corrections and simplifications made to the source

* **The `mod` and floor notation was dropped.** The source states the carrying rule as
  $S \bmod 10$ and $\lfloor S / 10 \rfloor$, and the borrowing rule as a three-line algebraic
  recipe. Neither modular arithmetic nor the floor function is in the book, and neither is
  needed: "write the right-hand digit, carry everything to its left" is the same rule, gives
  the same answers for a carry of $2$ or $3$, and can be read by someone who does not know
  mathematics. The rule itself is taught in full; only the symbols were dropped. **If a later
  transcript teaches `mod` or floor properly, this is the place that should link to it.**
* **The source's own "Mistake 1" layout is broken.** Its LaTeX array declares three columns and
  then puts four entries in the row, so it does not render, and its "wrong" example shows no
  answer. The book replaces it with fig_03, which shows what the wrong alignment actually
  produces ($473 + 28$ coming out as $753$) beside the right answer $501$.
* **"Always place the larger number on top" was given its real reason.** The source states it
  as a rule with no explanation, which invites the reader to think the two numbers may simply
  be swapped whenever that is easier. § 6.1 says instead that the number you start with goes
  first, that swapping changes the sum, and that the larger number is on top throughout this
  chapter because numbers below zero are not in the book yet.
* **"Units" was renamed "ones".** The source says "Units (Ones) Place". Chapter 2 already calls
  it the ones place, so the book uses *ones* only, for consistency.
* **The ASCII regrouping pictures were replaced.** The source draws bundling with
  `10 + 10 + ... = 100` under a brace and decomposing with `1 + 1 + ... = 10`. Those became
  fig_02 (the three trades) and fig_05 (473 packed two ways).
* The source's Example 3 and Solution 6 write $13$ and $24$ in the leftmost column without
  saying whether that is allowed. § 5 says it is, explains why ($13$ tens is $130$), and shows
  the alternative of carrying once more.

## Not covered yet - waiting for a source

* ~~Multiplication of large numbers~~ **is now Chapter 7** (long multiplication in columns).
  **Division of large numbers is still open**: Ch. 4 § 2.3 teaches division into decimal
  places as a share-and-trade table, but there is no whole-number long-division algorithm in
  the book.
* Estimation and rounding whole numbers, so that an answer can be checked for size
  ("about $1300 + 2600$, so about $3900$"). Rounding a *decimal* is Ch. 4 § 6.3.
* Place values above thousands: ten thousands, hundred thousands, millions. § 2.2 says the list
  goes on for ever but stops there.
* Negative numbers, and therefore subtracting a larger number from a smaller one. § 6.1 names
  this as out of scope.
* Subtracting decimals - still open from Ch. 2. Chapter 5's borrowing would transfer to it
  directly, so whichever transcript covers it should link back to § 6.3 rather than re-teach.
* Adding and subtracting with more than four digits, and sums where the answer needs a new
  leftmost column ($900 + 300$).
* Why addition can be done in any order but subtraction cannot, as a named property
  (commutativity). § 6.1 states the fact but does not name it.
