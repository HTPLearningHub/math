# Chapter 3 - Percentages

File: [3_Percentages/3_Percentages.md](./../3_Percentages/3_Percentages.md)

## Sections

| Section | Contains |
| --- | --- |
| 1. Why we need percentages | 1.1 where you meet them (discount, tip, rain, grade); 1.2 the real problem - three quizzes with totals 10, 20, 500 cannot be compared, so rewrite everything out of one shared total |
| 2. What a percentage is | 2.1 *per centum*, the definition, fig_01; 2.2 why the total is 100 (easy to picture, fine enough steps); 2.3 ratio, equivalent ratios, and $P\% = \frac{P}{100}$; 2.4 $100\%$ is the whole, $0\%$ is none |
| 3. Turning any score into a percentage | 3.1 reuses the rule of equivalence from Ch. 1 § 3.2; 3.2 the three quizzes worked (9/10 up, 18/20 up, 450/500 **down**), fig_02, the "same ruler" explanation; 3.3 table of bottoms that reach 100 (2, 4, 5, 10, 20, 25, 50, 100, 500), plus 3/5 and 1/2 |
| 4. Percent, fraction and decimal | 4.1 percent to fraction (over 100, then simplify): 50%, 80%, 3%; 4.2 GCF as the one-step short cut, 80/100 by 20; 4.3 percent to decimal, two places left, built on Ch. 2 § 3.2 and § 2.2; 4.4 decimal to percent, two places right; 4.5 fraction to percent (points back to § 3); 4.6 the three-form table, then fig_03, then the whole map as fig_04 |
| 5. The percentage formula | 5.1 part and whole defined; 5.2 18/20 worked first; 5.3 the formula, symbol list, and the proof that it *is* the scaling method of § 3 |
| 6. Finding a percentage of an amount | 6.1 the question turned around, $\text{part} = \frac{P}{100} \times \text{whole}$; 6.2 Method 1 (simplify the percent first) with the 20% tip on 45; 6.3 Method 2 (find 1% first) with 15% off 500; 6.4 a table saying which method to pick |
| 7. A full example: the shoes in the sale | 120 with 30% off, discount 36, pay 84, fig_05, two checks, and the "30% off = pay 70%" short cut |
| 8. Glossary / 9. Check your understanding / 10. Important notes | 7 questions with hidden answers; 3 common mistakes, fig_06 sits inside the first one |

## Terms defined here (do not define them again anywhere else)

percent, percentage, ratio, equivalent ratios, greatest common factor (GCF), part, whole.

## Formulas and facts that live here

* $P\% = \frac{P}{100}$ (§ 2.3) - the sentence the whole chapter is built on
* $100\% = 1$ and $0\% = 0$ (§ 2.4)
* $\text{percentage} = \left( \frac{\text{part}}{\text{whole}} \right) \times 100$ (§ 5.3)
* $\text{part} = \left( \frac{P}{100} \right) \times \text{whole}$ (§ 6.1)
* $\frac{9}{10} = \frac{18}{20} = \frac{450}{500} = \frac{90}{100} = 90\%$ (§ 3.2, § 9 Q7)
* $50\% = \frac{1}{2} = 0.50$; $80\% = \frac{4}{5} = 0.80$; $3\% = \frac{3}{100} = 0.03$ (§ 4)
* $25\% = \frac{1}{4} = 0.25$; $7\% = \frac{7}{100} = 0.07$ (§ 9 Q1, Q2)
* $20\% = \frac{1}{5}$, so $20\%$ of $45$ is $9$, and the bill becomes $54$ (§ 6.2)
* $15\%$ of $500$ is $75$, sale price $425$ (§ 6.3, § 9 Q6)
* $30\% = \frac{3}{10}$, so $30\%$ of $120$ is $36$ and you pay $84$; $30\%$ of $80$ is $24$ (§ 7, § 9 Q4)
* $\frac{3}{5} = 60\%$; $\frac{16}{20} = 80\%$ (§ 3.3, § 9 Q3, Q5)
* $100\% - 30\% = 70\%$, so "30% off" and "pay 70%" are one instruction (§ 7)

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_percent_means_out_of_100.png | fig_01_percent_means_out_of_100.py | A 10 by 10 grid with 25 squares shaded, and 25/100, 0.25, 25% written beside it |
| fig_02_same_score_three_ways.png | fig_02_same_score_three_ways.py | Four equal bars cut into 10, 20, 500 and 100 pieces, all shaded to the same point, dashed line at 90% |
| fig_03_three_percentages_on_grids.png | fig_03_three_percentages_on_grids.py | Three identical grids of 100 with 50, 80 and 3 squares shaded |
| fig_04_conversion_map.png | fig_04_conversion_map.py | Percent / fraction / decimal boxes joined by six labelled arrows |
| fig_05_discount_bar.png | fig_05_discount_bar.py | The 120 price bar split into 70% paid (84, blue) and 30% off (36, orange), with a percent scale |
| fig_06_three_percent_is_not_zero_point_three.png | fig_06_three_percent_is_not_zero_point_three.py | Wrong (red, 30 squares) against right (green, 3 squares), for the 3% vs 0.3 mistake |

Colour convention: the same as chapters 1 and 2 - blue `#2E86DE` for the whole or the amount
you keep, orange `#E67E22` for the part that is counted or taken away, grey `#ECEFF1` for the
squares nobody took, red `#C0392B` for the wrong method and green `#1E8449` for the right one
(fig_06 only). Slate `#546E7A` is used for frames, scales and, in fig_04 only, for the decimal
box, so the three forms each have their own colour.

Note for figures 1, 3 and 6: the grids are filled from the **top-left**, row by row, so the
shaded part reads like text. Chapter 2's fig_04 fills by column instead, because it had to show
that one column is one tenth. That difference is deliberate.

## Sources used

* `old/3/working-with-percentages-tutorial.md` (a written tutorial: definitions, the
  three-quiz comparison, the three conversions, two formulas, six worked examples, three
  common mistakes and seven practice problems).

## Corrections made to the source

* The source listed "divide the numerator by the denominator to get a decimal" as a way to turn
  a fraction into a percent. That needs long division into decimals, which the book has not
  taught, and every single example in the source actually used scaling instead. The chapter
  therefore teaches scaling to a bottom of 100, and § 3.3 lists the bottoms that reach 100.
* The source computed percentages of an amount by multiplying a decimal by a whole number
  ($45 \times 0.20$, $120 \times 0.30$). Multiplying decimals is not in the book yet. The
  chapter gets the same answers with whole-number arithmetic only: simplify the percent to a
  small fraction and divide (Method 1), or divide the whole by 100 to find 1% and multiply
  (Method 2). Both were checked against the source's answers - they agree.
* The source's practice problem 7 asked "which test score was higher?" when both are 90%. The
  chapter keeps the question but makes the answer explicit: neither, and the reason the second
  *looks* bigger is that it had more points in it.
* The source's "Tri-Way Conversion Map" was ASCII art and was missing the two arrows between
  fraction and decimal. It was redrawn as fig_04, with all six arrows.
* The source's grid column was only a written description ("50 squares filled out of 100"). It
  was drawn for real as fig_03.

## Not covered yet - waiting for a source

* Percentages of a fraction whose bottom does not reach 100 by a whole-number step
  (for example $\frac{1}{3}$ or $\frac{2}{7}$) - this needs division into decimals.
* Percentage increase and percentage decrease as a *change* ("the price rose by 20%"), and
  finding the original amount back from a percentage.
* Percentages above 100%.
* Percentage points, and the difference between "rose by 5%" and "rose by 5 percentage points".
* Interest, tax and repeated percentage changes.
* Turning a percentage into a ratio written with a colon, beyond the one-line definition.
