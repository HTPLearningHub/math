# Chapter 2 - Decimals

File: [2_Decimals/2_Decimals.md](./../2_Decimals/2_Decimals.md)

## Sections

| Section | Contains |
| --- | --- |
| 1. Why we need decimals | 1.1 real amounts are not whole numbers; 1.2 fractions are correct but slow, so we write the same amount with digits and a point |
| 2. Place value: a system you already use | 2.1 place value in 325; 2.2 the rule of ten (left = times 10, right = divide by 10); 2.3 the decimal point, decimal place, tenths / hundredths / thousandths, fig_01; 2.4 magnitude, each step ten times smaller, the digit 1 in five places, fig_02 |
| 3. Reading and writing decimals | 3.1 mixed number to decimal, fig_03, the two ways of reading 2.3; 3.2 fraction with 10 / 100 / 1000 to decimal; 3.3 zero as a place holder (0.03 not 0.3); 3.4 trailing zeros, proved from Ch. 1 § 3.2 |
| 4. Two pictures of a decimal | 4.1 hundredths grid, fig_04, shows 0.1 = 0.10; 4.2 number line in tenths, fig_05 |
| 5. Which decimal is bigger | compare from the left, or pad with trailing zeros and compare as whole numbers; 0.5 against 0.125, fig_06; 0.7 against 0.68 |
| 6. Adding decimals | 6.1 golden rule with fig_07 (wrong vs right alignment); 6.2 the five steps; 6.3 2.3 + 1.4; 6.4 5.2 + 3.14 (padding); 6.5 4.85 + 2.67 (carrying) |
| 7. A full example: the fruit shop | 1.75 kg + 2.6 kg = 4.35 kg, with a sanity check |
| 8. Glossary / 9. Check your understanding / 10. Important notes | 6 questions with hidden answers; 3 common mistakes |

## Terms defined here (do not define them again anywhere else)

decimal, decimal point, decimal place, place value, tenths, hundredths, thousandths,
magnitude, trailing zero, carrying (regrouping).

## Formulas and facts that live here

* $\frac{1}{10} = 0.1$, $\frac{1}{100} = 0.01$, $\frac{1}{1000} = 0.001$ (§ 2.3)
* One step left is $\times 10$, one step right is $\div 10$ (§ 2.2)
* $0.5 = 0.50 = 0.500 = \frac{5}{10} = \frac{50}{100}$ (§ 3.4)
* $2\frac{3}{10} = 2.3$ (§ 3.1); $\frac{9}{100} = 0.09$ (§ 3.3)
* $0.5 > 0.125$ (§ 5)
* $2.3 + 1.4 = 3.7$; $5.2 + 3.14 = 8.34$; $4.85 + 2.67 = 7.52$; $1.75 + 2.60 = 4.35$ (§ 6, § 7)

## Figures

| Image (in `assets/`) | Script (in `figures/`) | Shows |
| --- | --- | --- |
| fig_01_place_value_chart.png | fig_01_place_value_chart.py | Boxes from hundreds to thousandths with the times-ten and divide-by-ten arrows |
| fig_02_ten_times_smaller.png | fig_02_ten_times_smaller.py | Four equal bars cut into 1, 10, 100 and 1000 parts, one part shaded each time |
| fig_03_pizza_two_point_three.png | fig_03_pizza_two_point_three.py | Two whole pizzas plus 3 slices out of 10, giving 2.3 |
| fig_04_hundredths_grid.png | fig_04_hundredths_grid.py | 10 by 10 grid: one square = 0.01, one column = 0.1, whole = 1 |
| fig_05_number_line_tenths.png | fig_05_number_line_tenths.py | Number line 0 to 2 in tenths, with 0.1 and 1.1 marked |
| fig_06_compare_decimals.png | fig_06_compare_decimals.py | 0.5 against 0.125 on two equal bars |
| fig_07_align_decimal_points.png | fig_07_align_decimal_points.py | Two panels: ends lined up (wrong) against points lined up (right), 2.30 + 1.45 = 3.75 |

Colour convention: the same as chapter 1 — blue `#2E86DE` for the whole / bigger amount,
orange `#E67E22` for the part / smaller amount, grey `#ECEFF1` for what nobody took.
Chapter 2 adds red `#C0392B` for the wrong method and green `#1E8449` for the right one;
use those two only for "wrong versus right" panels.

Figure 7 sets `ax.set_position([0, 0, 1, 1])` so that one axis unit is one inch. That is what
makes the hand-placed mono-spaced digits line up. Do not change the figure size without
changing the coordinates.

## Sources used

* `old/2/decimals-notation-and-operations.md`, together with the three PNG files in `old/2/`
  (place value chart, tenths number line, hundredths grid). The three source pictures were
  redrawn as fig_01, fig_05 and fig_04 so that the whole book uses one style.

## Corrections made to the source

* The source's "Mistake 1" showed the wrong method and the right method producing the **same**
  answer, $3.75$, which teaches nothing. The book instead shows what actually goes wrong: with
  the ends lined up, $3$ tenths lands in the same column as $5$ hundredths, so that column
  cannot be added at all. The correct answer $2.30 + 1.45 = 3.75$ is then worked separately.
* The source explained the same mistake with the sentence "the digit 3 is in the tenths place,
  but 4 in 1.45 is in the tenths place! Adding 3 to 5 mixes different place values", which
  contradicts itself. It was rewritten.

## Not covered yet - waiting for a source

* Subtraction, multiplication and division of decimals (the source is called "Notation and
  Operations" but only teaches addition).
* Turning a decimal back into a fraction, and simplifying the result.
* Decimals that do not stop, and repeating decimals.
* Rounding a decimal to a given number of places.
* Negative decimals.
* Place values above hundreds (thousands and further).
