# Chapter 17 - Averages and range

File: [17_Averages_And_Range/17_Averages_And_Range.md](./../17_Averages_And_Range/17_Averages_And_Range.md)

Folder name and title match. Both are fixed - do not rename either.

This is **the book's first chapter about data** rather than about numbers on their own. Nothing
before it touches statistics, so nothing here repeats an earlier explanation; what it reuses is
*arithmetic*, and all of it is linked, never re-taught.

The chapter is built on two sentences of its own:

> **The mean is what each one would get if the total were shared out equally.**

> **The median is a position and the mode is a count - neither of them ever asks how big a value
> is.**

The first turns "add, then divide" from a rule into a consequence: adding collects the pile,
dividing hands it out. It is also what makes the mean Chapter 1 § 1.1's equal sharing, not a new
idea. The second is the whole of § 7: an outlier is enormous, and *being enormous* is exactly the
property the median and the mode cannot see. § 7.4 and fig_08 turn the source's bare assertion
("the median and mode are often less affected") into a reason.

A third framing runs through § 1.3, § 2.4, § 6.2 and § 8.4: **the four measures are four
questions, not four competitors.** The range is separated out as a measure of **spread**, not of
centre - the source's own title says "central tendency *and* range" but its body never makes the
distinction.

## Sections

| Section | Contains |
| --- | --- |
| 1. Describing many numbers with a few | 1.1 the ten baseball games and the question "how well do you hit?", and why a long list cannot be read; 1.2 **data set** and **value**, with the Note that the same number can appear as several separate values and that write-down order does not matter; 1.3 the four-row question table, the **two meanings of *average*** (everyday = mean, mathematical = any of the three middles), **measure of central tendency** defined, and the statement that the range is **not** one |
| 2. The range, or how wide the data is | 2.1 **maximum** and **minimum**; 2.2 fig_01 and the numbers first - the range is a *distance*, so it is a subtraction; 2.3 the formula, symbol list and three steps, plus the **Warning that rewrites the source's weak example**: $7+0=7$ hides the mistake, so the test scores $95-72=23$ against $95+72=167$ are used instead; 2.4 **what the range cannot see** - two data sets with the same range and nothing alike in the middle, and the Note naming **spread** |
| 3. The mean, or sharing the total equally | 3.1 **the chapter's own framing** - equal sharing, Ch. 1 § 1.1, fig_02; 3.2 the two-value example $1, 2 \to 1.5$; 3.3 the baseball mean with a **running total, one line per step**, and the check $2.8 \times 10 = 28$ justified by Ch. 6 § 1.1; 3.4 $\bar{x}$, subscripts, the $\cdots$, full symbol list; 3.5 why the mean need not be a value in the set, and the Warning against rounding it to one; 3.6 the source's Mistakes 1 and 2, plus the **Note giving the free check**: the mean always lies between the minimum and the maximum |
| 4. The median, or the value in the middle | 4.1 odd counts, $1,4,8$ then $2,3,5,7,10$, fig_03; 4.2 even counts, the baseball pair and the different-values case $\frac{2+3}{2}=2.5$, with the Note that the median need not be in the set either; 4.3 **the position formulas** $\frac{n+1}{2}$ and $\frac{n}{2}, \frac{n}{2}+1$, each checked on a worked set, and the **Warning that a position is not a value**; 4.4 sort first, fig_04, and the Warning built on the source's own broken Solution 7 |
| 5. The mode, or the value that happens most | 5.1 **frequency** defined, the frequency table, the check that frequencies sum to $n$, fig_05; 5.2 the mode is not the largest value ($1,2,2,3,10$); 5.3 **no mode** when every value appears once, and the Note that "no mode" is not "mode $= 0$"; 5.4 the mode works on words - the six favourite colours - and is the only average that does |
| 6. The four measures on one data set | 6.1 all four worked again on the baseball data, fig_06; 6.2 the four-row summary table and the point that **all four are true at once**, plus the observation that the three middles agree here *because* nothing unusual is present - which sets up § 7 |
| 7. When one value is far from the rest | 7.1 the fireworks data, given **unsorted** as the source gives it; 7.2 the mean $\frac{501}{9} \approx 55.67$, the repeating decimal (Ch. 4 § 2.4), **the $\approx$ symbol defined here**, and the honest question "does this describe a typical day?"; 7.3 median $0$ (sorted first, position $5$) and mode $0$; fig_07; 7.4 **the centre of the chapter** - fig_08 and the three bullets: the mean looks at sizes, the median at order, the mode at frequencies, so *a measure can only be moved by the part it looks at*; 7.5 **outlier** defined, with the Warning never to delete one |
| 8. Choosing a measure | 8.1 the mean when values are close ($10..14$, mean $=$ median $= 12$) or when the **total** matters; 8.2 the median for outliers, with income; 8.3 the mode for most-common and for non-numbers, with shoe sizes; 8.4 the four-row table with a **"weak when"** column, and the Note that reporting two measures often says more than one |
| 9. Glossary / 10. Check your understanding / 11. Important notes | 12 new terms; 10 questions with hidden answers; 8 mistakes, 3 ideas to keep, and a closing section naming Chs. 1, 4, 5, 8, 9 and 12 |

## Terms defined here (do not define them again anywhere else)

**data set**, **value**, **average** (the two meanings), **measure of central tendency**,
**spread**, **maximum**, **minimum**, **range**, **mean**, **median**, **mode**, **frequency**,
**outlier**. The symbol **$\approx$** is also explained here, in § 7.2 - it had been used in
Chs. 15 and 16 without ever being named.

Everything else is linked: **division as sharing** is Ch. 1 § 1.1; **dividend, divisor, quotient**
are Ch. 1 § 1.2; **the fraction bar as a division sign** is Ch. 1 § 2.2; **difference** is
Ch. 5 § 6.1; **repeating decimals** are Ch. 4 § 2.4 and **rounding** is Ch. 4 § 6.3; **odd and
even** are Ch. 12 § 1.4. The glossary ends with a Note listing all of these with links.

## Formulas and facts that live here

* $\text{range} = \text{maximum} - \text{minimum}$ (§ 2.3), always a subtraction
* $\bar{x} = \frac{x_{1} + x_{2} + \cdots + x_{n}}{n}$ (§ 3.4), derived from equal sharing in
  § 3.1 rather than stated
* The mean always satisfies $\text{minimum} \leq \bar{x} \leq \text{maximum}$ (§ 3.6, Note) -
  **the chapter's own addition**, used as the standing check and again in Q1 and § 11
* Median, odd $n$: the value at position $\frac{n+1}{2}$ (§ 4.3)
* Median, even $n$: the mean of the values at positions $\frac{n}{2}$ and $\frac{n}{2}+1$
  (§ 4.2, § 4.3)
* The mode is the value of highest **frequency**; frequencies must sum to $n$ (§ 5.1)
* No mode when every value has the same frequency (§ 5.3)
* Worked numbers, all checked with Python before they were written down.
  Baseball $0,1,1,2,2,2,3,5,5,7$: $n=10$, total $28$, mean $2.8$, median $2$, mode $2$,
  range $7$; running total $1, 2, 4, 6, 8, 11, 16, 21, 28$; check $2.8 \times 10 = 28$.
  $1, 2$: mean $1.5$. $\frac{2+3}{2} = 2.5$.
  $2,4,6$: total $12$, mean $4$. $2,4,6,8$: total $20$, mean $5$ (and the wrong $\frac{20}{8}=2.5$).
  $1,2,2,3,10$: mode $2$. $7,2,10,3,5 \to 2,3,5,7,10$: median $5$.
  $8,2,5,1,4 \to 1,2,4,5,8$: median $4$ (unsorted third value $5$ is the trap).
  $1,4,8$: median $4$. $2,3,5,7,10$: median $5$.
  $10,11,12,13,14$: total $60$, mean $12$, median $12$.
  $0,0,0,0,0,7,7,7,7,7$: range $7$, same as the baseball data (§ 2.4).
  Test scores $72,75,76,78,79,80,81,95$: range $23$, running total
  $147, 223, 301, 380, 460, 541, 636$, mean $79.5$, median $\frac{157}{2} = 78.5$, no mode.
  Fireworks $0,0,0,0,1,0,0,0,500$: $n=9$, total $501$, mean $\frac{501}{9} = 55.666\ldots
  \approx 55.67$, median $0$ (position $5$), mode $0$, range $500$.
  Colours blue/red/blue/green/blue/red: blue $3$, red $2$, green $1$, mode blue.
* Questions (§ 10): $2,3,3,4,5$ (range $3$, mean $3.4$, median $3$, mode $3$);
  $6,8,10$ (mean $8$); $1,4,7,9,12$ (median $7$);
  $1,2,2,4,5,6,6,6$ (range $5$, mean $4$, median $4.5$, mode $6$, running total
  $3,5,9,14,20,26,32$); $3,8,1,9,4,7 \to$ median $5.5$ (and the unsorted trap gives $5$);
  the eight test scores with the "which is more representative" discussion;
  $0,0,1,0,2,0,100$ (mean $\approx 14.71$, median $0$, mode $0$) - **the question that carries
  the source's broken solution, corrected**; a range of $0$ forces all values equal and all three
  middles to agree; Ana and Ben on sorting before using the position rule;
  nine salaries of $20\,000$ with an owner on $920\,000$ (total $1\,100\,000$, mean $110\,000$,
  median $20\,000$)

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_range.png | fig_01_range.py | The ten baseball values as a dot plot over a number line $0$ to $7$, dots stacked where a value repeats, minimum and maximum in orange, and a double-headed orange arrow between them labelled $7-0=7$ |
| fig_02_mean_is_equal_sharing.png | fig_02_mean_is_equal_sharing.py | Two rows of ten bars - the real heights, then ten equal bars of $2.8$ - with an orange dashed line at $2.8$ crossing **both** rows and the total $28$ printed under each |
| fig_03_median_odd_and_even.png | fig_03_median_odd_and_even.py | Two strips of numbered cards: five cards with the third green and grey arrows counting "two below, two above"; ten cards with the fifth and sixth orange and an elbow arrow down to a green $\frac{2+2}{2}=2$ box |
| fig_04_order_first.png | fig_04_order_first.py | $7,2,10,3,5$ with the third card red and crossed through, an arrow "put them in order", then $2,3,5,7,10$ with the third card green. Position numbers under every card in both rows |
| fig_05_mode.png | fig_05_mode.py | A column of squares above each value $0$ to $7$; the stack above $2$ is three tall and green, the rest blue, and $4$ and $6$ get a grey dash instead of a stack. A curved green arrow names the tallest stack |
| fig_06_four_measures.png | fig_06_four_measures.py | The baseball dot plot with a green dashed line at $2$ (median **and** mode share it), an orange dashed line at $2.8$, and the range arrow below the axis. The two vertical lines sit at `zorder=1`, behind the dots |
| fig_07_one_big_value.png | fig_07_one_big_value.py | The fireworks data on a **to-scale** line $0$ to $520$: eight small dots stacked at $0$, one purple dot at $500$, green median/mode marker at $0$, orange mean marker near $56$, and a horizontal orange arrow showing the drag |
| fig_08_what_each_one_looks_at.png | fig_08_what_each_one_looks_at.py | Three panels of the same nine days - true sizes (one purple bar fills the panel), nine identical ordered cards (fifth green), three frequency stacks - each with a one-line conclusion underneath |

Colour convention. As Chapters 13 to 16, with one addition:

* blue `#2E86DE` - the data values themselves
* orange `#E67E22` - **the mean**, and the range arrow (both are things that move or measure)
* green `#1E8449` - **the median and the mode**, and any answer
* red `#C0392B` - the wrong answer; used in fig_04 only
* purple `#8E44AD` - **new in this chapter: the outlier.** Deliberately *not* red, because $500$
  is real data, not a mistake. Used in fig_07 and fig_08 only
* grey `#78909C` - axes, position numbers, quiet labels, and in fig_08 the parts a measure ignores
* tints: `#E9F2FC` blue, `#FDF0E3` orange, `#E8F5EC` green, `#FCEAE8` red, `#F2E7F7` purple,
  `#ECEFF1` grey

Layout lessons worth keeping, on top of the Chapter 9 to 16 lists:

* **Budget the vertical space before writing any `ax.text`.** Four of the eight figures had to be
  redone because a row heading landed on the row above's value labels. Write the y positions out
  as a list first - title, subtitle, heading, drawing, labels, caption - and derive each one from
  the drawing height instead of typing a guess.
* **`ax.set_position([0, 0, 1, 1])` defeats `bbox_inches="tight"`.** The axes fill the figure, so
  nothing is ever trimmed and empty space at the bottom stays in the PNG. The figure height has to
  be tuned by hand to the lowest piece of ink.
* **A marker line through a dot plot belongs at `zorder=1`.** fig_06's first version drew the
  median line on top and it appeared as dashes inside the circles. Behind the dots, the part that
  sticks out above the stack still names the position, and the data stays readable.
* **Move the axis label aside rather than the marker.** In fig_07 the median sits at $x = 0$, right
  where the "$0$" tick label is. Shifting that one tick label left by a fraction is cleaner than
  bending the marker.
* **Draw an outlier to scale, or do not draw it.** fig_07 only works because $500$ really is that
  far from the cluster. A broken axis would have destroyed the one thing the picture exists to say.
* **Three panels beat three sentences for "why they differ".** fig_08 redraws one data set three
  ways, greying out what each measure ignores. It is the only figure that explains § 7 rather than
  illustrating it.
* **Heredocs are not safe for figure scripts with LaTeX in them.** A `\a` in `\approx` was eaten in
  transit and produced a mathtext parse error. Write each script with a single quoted heredoc in
  one go, or with the Write tool - never by string-patching a file that contains backslashes.

## Sources used

* `old/17/measures_of_central_tendency_and_range.md` (a written tutorial: an introduction, a
  prerequisite section, sections on range, mean, median with odd and even counts, why ordering is
  needed, mode, all four together, why there are different averages, the fireworks example, the
  effect of extreme values, when to use each, a differences table, five common mistakes, seven
  practice problems with full step-by-step solutions, a summary and a ten-point key-points list).

## Material in the source that was deliberately skipped, because the book already has it

* **The whole prerequisite section (§ 2).** The source lists "how to add, subtract, divide, order
  numbers and count". Those are Ch. 5, Ch. 8, Ch. 9 § 3 and Ch. 12 § 1.4. They are named in
  **Before you start** as links and nowhere else.
* **Re-explaining that a fraction bar means division.** Ch. 1 § 2.2, linked once from § 3.2.
* **Re-explaining decimal answers to a division.** Ch. 8 § 7 and Ch. 4 § 2.3, linked from § 3.3.
* **Re-explaining repeating decimals and rounding.** Ch. 4 § 2.4 and Ch. 4 § 6.3, linked from
  § 7.2 and § 3.5.
* **The source's summary (§ 20) and key-points list (§ 21).** Two flat restatements of the same
  four rules, one after the other. Their content is the per-section summaries plus § 6.2, § 8.4
  and § 11. A third copy would be the repetition the book exists to avoid.
* **The "Important differences" table (source § 16).** It is § 8.4, with a **"weak when"** column
  added so the table answers *which one do I use* instead of only *what is it*.

## Additions made because the source states a rule without giving a reason

* **The mean as an equal share** (§ 3.1, fig_02). The source says only "add all the values and
  divide by the number of values". That is a procedure with no idea behind it. Equal sharing is
  Ch. 1 § 1.1, it explains why there are exactly two steps, and it is what makes § 3.5 and the
  § 3.6 check obvious rather than arbitrary.
* **The check $\text{minimum} \leq \bar{x} \leq \text{maximum}$** (§ 3.6). Not in the source at all.
  It catches both of the source's own Mistakes 1 and 2 immediately, so it is worth more than the
  two warnings it replaces.
* **The check that frequencies sum to $n$** (§ 5.1). Also not in the source. It is the mode's
  equivalent of the above.
* **The median position formulas** (§ 4.3). The source identifies the middle *positions* twice -
  "the third value" for five values, "the fifth and sixth" for ten - but never generalises. Stating
  $\frac{n+1}{2}$ and $\frac{n}{2}, \frac{n}{2}+1$ is the general form of what the source already
  does twice, and it comes with the Warning that a position is not a value.
* **Why the three middles react differently to an outlier** (§ 7.4, fig_08). **The largest
  addition.** The source asserts "the mean is sensitive to extreme values" and "the median is
  usually more resistant" and leaves it there. The chapter derives both from one sentence: a
  measure can only be moved by the part of the data it looks at - sizes, order or counts.
* **The range cannot see the middle** (§ 2.4). The source says a larger range means a wider
  interval and stops. The two data sets with range $7$ and nothing else in common are what justify
  calling the range a measure of **spread** and keeping it out of the central-tendency group.
* **The $\approx$ symbol** (§ 7.2, Note). Used in Chs. 15 and 16 and never explained. This chapter
  needs it constantly, so it is named here.
* **Questions 8, 9 and 10** (§ 10). A range of $0$; the two students and the sorting rule; and the
  ten-worker company. The last is the source's own income remark (§ 15.2) turned into numbers the
  reader can actually follow.

## Corrections and simplifications made to the source

* **Solution 7 is wrong, and the chapter says so by doing it properly.** The source writes
  "The data is already ordered" about $0, 0, 1, 0, 2, 0, 100$ - it is not - and then reads the
  fourth value straight off the unsorted list. The answer $0$ comes out right **by luck**, and the
  method directly contradicts the source's own § 9 and its own Mistake 3. § 4.4's Warning uses this
  exact data set as the example of an accident that looks like a method, and Q7 sorts it first.
* **The range's "common mistake" example is useless as given.** The source warns against adding the
  minimum and maximum, then demonstrates with $7 + 0 = 7$ and admits "this example happens to give
  the same number". § 2.3's Warning keeps the warning and replaces the example with the test
  scores, where $95 - 72 = 23$ and $95 + 72 = 167$ are unmistakably different.
* **The source never separates spread from centre**, although its own title does ("central
  tendency *and* range"). § 1.3 names **measure of central tendency** and says plainly that the
  range is not one; § 2.4 gives the reason.
* **"The word average usually means a value that represents or describes a larger data set"**
  followed by "the mean is the usual mathematical average" is muddled. § 1.3 separates the two
  meanings cleanly: everyday English = the mean; mathematics = any of the three middles.
* **"An anomalous value"** (source § 12) is given its standard name, **outlier** (§ 7.5), together
  with the point the source never makes: an outlier is not an error, and deleting it is not an
  option.
* **"The mode depends on frequency, so an extreme value that occurs only once may have little
  effect on it"** is softened to the point of vagueness. § 7.4 states the precise version: a value
  that happens once cannot be the tallest stack, so it has **no** effect unless it becomes the most
  common value.
* **The source's practice problems were re-ordered and re-purposed, not copied.** Problems 1 to 7
  became Q1 to Q7 with every arithmetic step written out one per line (the source jumps from a
  list of eight numbers straight to their total). Q8 to Q10 are new and test understanding rather
  than calculation, as CLAUDE.md § 4 asks.
* **No ASCII was carried over**, as always. The source has none, but it does use `\boxed{}` on
  nearly every line, which the book does not: a result is made clear by where it sits and what the
  sentence around it says.

## Topics the transcripts have not covered yet

* **More than one mode** (bimodal data, and data where two values tie for the tallest stack). The
  source never raises it - its § 5.3 case is "every value appears once", which the chapter does
  cover. The tie case is the obvious next thing and is genuinely common.
* **The mean of a data set that contains negative numbers.** Ch. 9 has everything needed, but no
  source data set has gone below zero.
* **Weighted means** (some values counting more than others).
* **Quartiles, the interquartile range, and box plots.** The natural continuation of § 2.4's point
  that the range only looks at two values.
* **Standard deviation** - the measure of spread that does look at every value, and so is to the
  range what the mean is to the median.
* **Reading data off a chart** rather than from a written list. Every data set in this chapter
  arrives as a row of numbers.
* **How many values you need before an average means anything** (sample size).
* Still open from Chapter 16: **cancelling before you multiply**, **multiplying and dividing mixed
  numbers**, **multiplying or dividing negative fractions**, and **three or more fractions in one
  line**. Still open from Chapter 15: **an addition whose answer comes out bigger than $1$**, and
  **adding and subtracting mixed numbers**.
