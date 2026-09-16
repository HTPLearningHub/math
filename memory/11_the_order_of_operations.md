# Chapter 11 - The order of operations

File: [11_The_Order_Of_Operations/11_The_Order_Of_Operations.md](./../11_The_Order_Of_Operations/11_The_Order_Of_Operations.md)

Folder name and title match. Both are fixed - do not rename either.

This chapter closes the hole that Chapters 6, 7, 8, 9 and 10 all left open. It adds no new
arithmetic at all; it arranges arithmetic the book already has. Every level is an earlier
chapter: Ch. 6 § 1.2 for Level 1, Ch. 10 for Level 2, Chs. 7 and 8 for Level 3, Ch. 5 for
Level 4.

The chapter is built on one idea used everywhere: **each operation is a package of the one
below it, and a package has to be opened before what is inside it can be used** (§ 3.1). That
single sentence generates the whole tower, and it is the "why" the source never gives.

## Sections

| Section | Contains |
| --- | --- |
| 1. One expression, two answers | 1.1 the five operations, as links to Ch. 10 § 1.1 and § 1.2, not re-explained; 1.2 fig_01, $5 \times 3 + 4 - 2 \times 6$ worked from the left ($102$) and from the right ($-25$), every step shown; 1.3 **convention** and **expression** defined, the driving-side analogy, and the note that an equation is not an expression |
| 2. The agreed order | 2.1 fig_02, the four levels read from the top; 2.2 **PEMDAS** defined, **parentheses** named, and the Warning that six letters cover four levels; 2.3 the five-column priority table; 2.4 **equal priority** and the **left-to-right rule** defined, with $12 \div 3 \times 2$ against $5 \times 12 \div 3$ to show position is the only thing that decides |
| 3. Why the order is this way round | 3.1 the package idea, built on Ch. 10 § 1.2; 3.2 $2 + 3 \times 4$ unpacked into $2 + 4 + 4 + 4 = 14$, with the $20$ shown to be *five* fours; 3.3 fig_03, a subtraction is an addition (Ch. 9 § 4.3) and a division is a multiplication by the reciprocal (Ch. 10 § 7.1), checked with $12 \times \frac{1}{3} = 4$; 3.4 the honest reason for left-to-right - **the answer does not depend on the order once the signs are attached**; three reorderings of $10 + (-4) + 2$ all give $8$, and the real mistake is regrouping, not reordering |
| 4. Level 1, brackets | 4.1 Ch. 6 § 1.2 linked, then $2 + 3 \times 4 = 14$ against $(2+3) \times 4 = 20$, with the Note that a bracket changes the question and not the rule; 4.2 **square brackets**, **curly brackets**, **grouping symbols**; 4.3 fig_04, innermost first; 4.4 the order restarts inside a bracket ($8 - 3^{2} = -1$), and the Note that the order is a loop, not a list |
| 5. Level 2, exponents | 5.1 $3 \times 2^{3} = 24$, fig_05, and the Warning against $216$; 5.2 $(3 \times 2)^{3} = 216$ and $(3+2)^{2} = 25$ as Level 1 then Level 2; 5.3 two powers in one line, $5^{2}$ and $2^{3}$, and the point that left-to-right here is a habit and not a rule |
| 6. Level 3, multiply and divide | 6.1 $12 \div 3 \times 2 = 8$ and the Warning about M-before-D; 6.2 fig_06, the wrong answer named as **an invented bracket**, $12 \div (3 \times 2)$; 6.3 when the order genuinely does not matter, $4 \times 5 \times 2$ grouped both ways, via Ch. 6 § 1.4 |
| 7. Level 4, add and subtract | 7.1 $10 - 4 + 2 = 8$, the same invented bracket, the Warning about A-before-S; 7.2 $15 + 25 - 54 + 8 = -6$ one step per line, linked to Ch. 9 § 4.1, and the Note that a negative running total is not a dead end |
| 8. Three expressions, worked in full | 8.1 fig_07, the loop, and the rewrite-the-line habit; 8.2 $5 \times 3 + 4 - 2 \times 6 = 7$ answering § 1.2; 8.3 $15 + (3+2)^{2} - 9 \times 6 + 2^{3} = -6$, with the Note that the bracket held a Level 4 operation and still went first; 8.4 $100 \div 5 \times 2 - [\,4 + (8 - 3^{2})\,] = 37$, fig_08, and the Warning that doing $5 \times 2$ first gives $7$ |
| 9. Glossary / 10. Check your understanding / 11. Important notes | 11 new terms; 10 questions with hidden answers (Q6, Q7 and Q8 are about the shape rather than the arithmetic); 4 mistakes, 3 ideas to keep, and the paragraph that names every earlier chapter that had to leave this rule out |

## Terms defined here (do not define them again anywhere else)

convention, expression, level, order of operations, PEMDAS, parentheses, square brackets,
curly brackets, grouping symbols, equal priority, left-to-right rule.

**Brackets** are Ch. 6 § 1.2 and are linked, not redefined - this chapter only adds the other
two shapes. The **commutative** and **associative** properties are Ch. 6 § 1.3 and § 1.4.
**Base**, **exponent** and **power** are Ch. 10 § 2.1. **Reciprocal** is Ch. 10 § 7.1.
**Negative number** and **opposite** are Ch. 9 § 1.3 and § 2.2. The glossary ends with a Note
listing all of these with links.

## Formulas and facts that live here

* The four levels: brackets, exponents, multiply-and-divide, add-and-subtract (§ 2.1, § 2.3)
* Inside one level, work left to right (§ 2.4)
* Inside a bracket the whole order restarts (§ 4.4) - this is why nested brackets need no extra
  rule
* An exponent reaches one number only; a bracket is the only way to widen it (§ 5.1, § 5.2)
* A wrong answer on a shared level is always an **invented bracket** (§ 6.2, § 7.1, Q7, Q8) -
  this is the chapter's own framing and it is used five times
* Worked numbers, all checked with Python before they were written down:
  $5 \times 3 + 4 - 2 \times 6 = 7$ (with the wrong roads $102$ and $-25$);
  $2 + 3 \times 4 = 14$ against $(2+3) \times 4 = 20$;
  $12 \div 3 \times 2 = 8$ against $12 \div (3 \times 2) = 2$;
  $10 - 4 + 2 = 8$ against $10 - (4+2) = 4$;
  $3 \times 2^{3} = 24$ against $(3 \times 2)^{3} = 216$;
  $(3+2)^{2} = 25$; $15 + (3+2)^{2} - 9 \times 6 + 2^{3} = -6$ (via $40$, $-14$);
  $100 \div 5 \times 2 - [\,4 + (8 - 3^{2})\,] = 37$ (via $9$, $-1$, $3$, $20$, $40$), and the
  wrong $7$ from doing $5 \times 2$ first;
  $4 \times 5 \times 2 = 40$ both ways; $12 \times \frac{1}{3} = 4$
* Questions (§ 10): $18 - 3 \times 4 + 2 = 8$; $24 \div 6 \times 2 = 8$;
  $5 + 2 \times (8-3)^{2} = 55$; $40 - 2^{4} \div 4 + 7 = 43$;
  $3 \times [\,15 - (2+3)^{2} \div 5\,] + 6 = 36$; $2 \times 3^{2} = 18$ against
  $(2 \times 3)^{2} = 36$; $36 \div 6 \div 3 = 2$ against the invented $18$;
  Q8 asks *where to put* a bracket to make $10 - 4 + 2$ equal $4$;
  $7 \times 2 - 4^{2} \div 8 = 12$; $1 + 2 \times 3^{2} - (10-4) = 13$

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_two_answers.png | fig_01_two_answers.py | Two red panels, Road A and Road B, four numbered steps each, ending $102$ and $-25$. Both panels are red because both roads are wrong |
| fig_02_levels.png | fig_02_levels.py | Four stacked bars, one per level, each with a solid letter tab (P / E / M D / A S), the level name, how to work inside it, and its signs. A grey arrow down the right says which end is done first |
| fig_03_one_operation.png | fig_03_one_operation.py | Two panels. Level 4: $10 - 4$ becomes $10 + (-4)$. Level 3: $12 \div 3$ becomes $12 \times \frac{1}{3}$. Each half is labelled "how it is written" and "what it really is" |
| fig_04_nested.png | fig_04_nested.py | Three rows of the same expression, one bracket layer gone per row, the layer about to go ringed - purple for the innermost, orange for the outer |
| fig_05_reach.png | fig_05_reach.py | Green panel $3 \times 2^{3} = 24$ against red panel $(3 \times 2)^{3} = 216$, each naming what the exponent reaches |
| fig_06_left_to_right.png | fig_06_left_to_right.py | Two rows ($12 \div 3 \times 2$ and $10 - 4 + 2$), each with a green "left to right" box and a red "right one first" box. The red boxes print the invented bracket |
| fig_07_routine.png | fig_07_routine.py | A flow chart: four questions down the left, a dashed action box on each "yes" branch, and a long grey arrow on the right returning to the top. It leaves at the bottom into a green "one number left" box |
| fig_08_staircase.png | fig_08_staircase.py | Seven lines of $100 \div 5 \times 2 - [\,4 + (8-3^{2})\,]$ getting shorter, each tagged with its level, and an orange bar down the left marking the three steps that happened inside the bracket |

Colour convention. Chapter 10's five colours are kept, and **the four level colours are new and
must be kept if any later chapter draws the tower again**:

* orange `#E67E22` - **Level 1, brackets and grouping.** New meaning. It was "the far side of
  zero" in Ch. 9 and "below the bar" in Ch. 10
* purple `#8E44AD` - **Level 2, exponents.** This is exactly Ch. 10's meaning, carried over
* blue `#2E86DE` - **Level 3, multiply and divide**
* slate `#546E7A` - **Level 4, add and subtract.** A new colour in the book. The four run warm
  to cool as priority falls, so the tower reads as a fall before it is read as words
* green `#1E8449` - the right answer (Ch. 9's meaning)
* red `#C0392B` - the wrong answer, and both roads in fig_01
* grey `#78909C` - quiet labels, arrows and dividers

Layout lessons worth keeping, on top of the Chapter 9 and 10 lists:

* **A ring drawn around part of a mathtext string never lands on the right characters.**
  fig_04's first version ringed "× 2 − [4 + (8" instead of the bracket. It now draws each row
  as separate pieces, measures every piece with `t.get_window_extent(renderer)` and divides by
  `fig.dpi` to get inches, and places the rings around measured spans. Any future figure that
  highlights part of a formula should copy `width_of()` and `row()` from that script.
* **A ring still needs padding *inside* the string.** Even with measured spans, the ring edge
  landed on the neighbouring `+` and `]`. Doubled thin spaces (`\;\;`) were added to the
  pieces to give the ring something to sit on.
* **Do not leave a placeholder `ax.text(..., fontsize=0.1)` in a script.** Two of these were
  written while drafting and both had to be removed; a zero-size text is invisible in the
  output but is dead code in a file that is meant to be read.
* **Check whether a bottom caption is inside the last panel before shipping.** fig_02, fig_03
  and fig_07 all had the closing sentence land on top of the last box, because the panel
  heights are computed from `H` and the caption is not.
* **A text label that is long enough to pass `W` makes `bbox_inches="tight"` widen the canvas.**
  fig_06's first version did this, and the right-hand note then ran outside its own box. The
  note was shortened rather than the figure widened.

## Sources used

* `old/11/order-of-operations-pemdas-tutorial.md` (a written tutorial: an introduction with the
  two-roads problem, a prerequisite list of five operations, four definitions, the four steps,
  a priority table, three worked examples in three difficulty levels, two ASCII diagrams
  (a decision flowchart and a level diagram), three common mistakes, five practice problems
  with full solutions, a summary and a key-points list).

## Material in the source that was deliberately skipped, because the book already has it

* **The five basic operations.** The source spends a whole prerequisite section defining
  addition, subtraction, multiplication, division and exponents. § 1.1 is two sentences of
  links to Ch. 10 § 1.1 and § 1.2.
* **What a base and an exponent are, and that $2^{3} = 8$.** Ch. 10 § 2.1 and § 2.3. The source
  repeats it inside its prerequisites; the chapter uses it and links.
* **What a bracket means.** Ch. 6 § 1.2. § 4.1 links and then goes straight to the thing that
  is new - that a bracket outranks the order.
* **That order and grouping may be changed for multiplication.** Ch. 6 § 1.3 and § 1.4. § 3.4
  and § 6.3 link.
* **That subtraction and division do not allow it.** Ch. 6 § 1.5.
* **Negative results.** Ch. 9. The source's Example 2 passes through $-14$ without comment;
  § 7.2 links to Ch. 9 § 4.1 instead of re-teaching it.
* **Adding a negative.** Ch. 9 § 4.3, used twice in § 3.3 and § 8.4 and linked both times.
* **Reciprocal.** Ch. 10 § 7.1, used in § 3.3 and linked.

## Additions made because the source states a rule without giving a reason

* **Why the levels are in that order at all** (§ 3.1, § 3.2). The source says the operations
  "have a natural hierarchy" and stops. The chapter derives the hierarchy from Ch. 10 § 1.2:
  a power packs multiplications, a multiplication packs additions, and the tighter package is
  opened first. $2 + 3 \times 4$ is then unpacked into $2 + 4 + 4 + 4$ to show it.
* **Why M and D share a level, and A and S share a level** (§ 3.3, fig_03). The source asserts
  "equal priority" four times and never explains it. The reason is that each pair is one
  operation: $10 - 4 = 10 + (-4)$ and $12 \div 3 = 12 \times \frac{1}{3}$. Both halves were
  already in the book and had never been put together.
* **What the left-to-right rule is really for** (§ 3.4). This is the chapter's most important
  correction of emphasis - see the next section.
* **The "invented bracket" framing** (§ 6.2, § 7.1, Q7, Q8). The source presents its first two
  mistakes as two separate facts to memorise. They are one mistake, and naming it that way
  turns Q8 (*where would you put a bracket to get the wrong answer on purpose?*) into a
  question that tests the idea rather than the arithmetic.
* **That the order is a loop, not a list** (§ 4.4 Note, § 8.1, fig_07). The source's own
  flowchart runs top to bottom once and never returns, which cannot handle a bracket inside a
  bracket. fig_07 has the return arrow.
* **The rewrite-the-line habit** (§ 8.1). The source mentions it in one line of its closing
  list ("Don't Rush"). It is the single most effective thing in the chapter, so it opens § 8
  and it has fig_08 to itself.

## Corrections and simplifications made to the source

* **The left-to-right rule was corrected, not just repeated.** The source implies that the
  answer depends on the order, which is false. § 3.4 shows $10 + (-4) + 2$, $10 + 2 + (-4)$ and
  $2 + (-4) + 10$ all giving $8$, and then says plainly that the real mistake is *regrouping* -
  dragging the minus sign onto the $2$ - and not reordering. Left to right is described as a
  safe recipe that keeps every sign attached to the number after it. **This is the chapter's
  main departure from the source and it must not be undone.**
* **Square roots were dropped.** The source's priority table lists $\sqrt{x}$ on Level 2 and
  its step 2 says "powers and roots". The book has never mentioned a root, and CLAUDE.md § 5.1
  forbids previewing a topic the reader has not reached. The table in § 2.3 lists $a^{b}$ only.
  See the open list below.
* **A transcription error was fixed.** The source writes the division symbols as
  "$\div$ or $/ Hawkes$". The stray word is an artefact; the chapter writes $\div$ and $/$.
* **The third "common mistake" was renamed.** The source calls it "Forgetting to Apply Exponent
  to Parentheses Terms Correctly" and then gives $3 \times 2^{3}$, which has no parentheses in
  it. The mistake is about how far an exponent *reaches*, so § 5.1 is titled that way and
  fig_05 shows the reach.
* **Both ASCII diagrams were dropped.** No ASCII art in the book (CLAUDE.md § 7). The level
  diagram became fig_02 and the flowchart became fig_07, rebuilt with a return arrow.
* **The source's separate "worked examples" and "practice problems" sections were dissolved**,
  as in Chapters 7, 8, 9 and 10. The three examples became § 8.2, § 8.3 and § 8.4, and the five
  practice problems became Q1 to Q5 in § 10.
* **The "common mistakes" section was used twice**, as in Ch. 10: each is a Warning at the
  point where the reader could make it (§ 2.2, § 5.1, § 6.1, § 7.1, § 8.4) and all four are
  collected again in § 11.
* **"Parentheses" was kept as a term but not as the book's word.** The source uses it
  throughout. § 2.2 names it once, because PEMDAS needs the P, and then the book carries on
  saying *brackets*.

## Not covered yet - waiting for a source

* **BODMAS / BIDMAS**, the other acronym for the same convention, with B for brackets, O for
  *of* or *order*, and I for *indices*. The source never mentions it, so § 5.1 of CLAUDE.md
  keeps it out. It is the most likely thing a reader will meet elsewhere and be confused by.
* **Square roots and fractional exponents.** Still open from Ch. 10, and now doubly open: they
  belong on Level 2 and the chapter had to leave them off the table.
* **Implied multiplication next to a bracket**, as in $2(3+4)$ or the viral $8 \div 2(2+2)$.
  Ch. 10 § 8.4 explained implied multiplication between letters; this chapter never writes a
  number directly against a bracket, and the source does not either.
* **The unary minus**, as in $-3^{2}$ against $(-3)^{2}$. Ch. 9 § 4.2 gave the minus sign two
  jobs and Ch. 10 § 7.5 gave it a third, but no chapter has yet said where a leading minus sits
  in the order. Every base in this chapter is positive.
* **The fraction bar as a grouping symbol.** Ch. 9 § 6.2 says a bar groups the work above and
  below it, and § 11 of this chapter points at that, but the bar is not in the Level 1 table
  because the source's table does not have it.
* **Nested brackets more than two deep**, and the convention of alternating $(\;)$, $[\;]$,
  $\{\;\}$ from the inside out. § 4.2 says why the shapes exist; no example goes past two.
* **Whether a calculator or a spreadsheet follows this order.** The source claims the rule
  makes "everyone around the world" agree, and it is worth knowing that some cheap calculators
  do not. Nothing in the source supports saying more.
* **Division by zero**, still untouched, as in Chapters 8, 9 and 10.
* **Estimation**, still open from Chapters 5, 7, 8, 9 and 10.
