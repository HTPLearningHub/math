### Addition and Subtraction of Large Numbers

#### 1. Introduction
When learning basic mathematics, we often begin with small numbers. For example, adding $2 \text{ apples}$ and $3 \text{ apples}$ gives $5 \text{ apples}$ ($2 + 3 = 5$). We can easily verify this answer by physically counting the objects one by one [12].

However, in real-life situations, we frequently work with much larger numbers [12]. Imagine a scenario where one store sells $1,293 \text{ apples}$ in a day and another store sells $2,614 \text{ apples}$ [12]. Counting several thousand apples individually is impractical and takes too much time [12]. 

Instead of counting, we use written mathematical procedures called **algorithms** [12]. An algorithm is a step-by-step method for solving a problem. By learning the standard algorithms for addition and subtraction, we can calculate answers quickly and accurately using only paper and pencil [12].

---

#### 2. Prerequisite Knowledge
To add and subtract large numbers successfully, you must understand how numbers are built.

##### Digits
In mathematics, we use ten basic symbols called **digits**:
$$0, 1, 2, 3, 4, 5, 6, 7, 8, 9$$
Every number, no matter how large, is created by combining these ten digits.

##### The Base-10 (Decimal) Place Value System
Our number system is based on groups of $10$ [12]. The position (place) of a digit in a number tells us its value [12]. This is called **place value** [12].

Moving from **right to left**, each place value position is $10 \text{ times}$ larger than the one before it [12]:
* **Units (Ones) Place:** Represents single items ($1$).
* **Tens Place:** Represents groups of $10$ ($10 \text{ units} = 1 \text{ ten}$).
* **Hundreds Place:** Represents groups of $100$ ($10 \text{ tens} = 1 \text{ hundred}$).
* **Thousands Place:** Represents groups of $1,000$ ($10 \text{ hundreds} = 1 \text{ thousand}$).

##### Place Value Chart for $1,293$:
| Thousands ($1,000$) | Hundreds ($100$) | Tens ($10$) | Units ($1$) |
| :---: | :---: | :---: | :---: |
| $1$ | $2$ | $9$ | $3$ |

Mathematically, $1,293$ means:
$$1,293 = (1 \times 1,000) + (2 \times 100) + (9 \times 10) + (3 \times 1)$$

##### Key Equivalence Rules:
* $10 \text{ Units} = 1 \text{ Ten}$ [12]
* $10 \text{ Tens} = 1 \text{ Hundred}$ [12]
* $10 \text{ Hundreds} = 1 \text{ Thousand}$

---

#### 3. Important Definitions
Here are the key terms used in this tutorial:

* **Addition:** The mathematical operation of combining two or more numbers to find their total value [12]. The symbol for addition is $+$.
* **Sum:** The total result obtained after adding numbers together [12]. In $a + b = c$, $c$ is the sum.
* **Subtraction:** The mathematical operation of taking one number away from another to find how much is left [12]. The symbol for subtraction is $-$.
* **Difference:** The result obtained after subtracting one number from another [12]. In $a - b = c$, $c$ is the difference.
* **Place Value:** The numerical value a digit holds based on its position in a number [12].
* **Carrying (Regrouping in Addition):** The process of moving a value of $10$ or more from a smaller place value column to the next larger column on the left [12].
* **Borrowing (Decomposing in Subtraction):** The process of taking $1$ unit from a larger place value column on the left and converting it into $10$ units in the smaller place value column on the right [12].

---

#### 4. Main Concepts

##### 1. Vertical Column Alignment
When adding or subtracting large numbers on paper, write one number directly above the other [12]. 
* You **must align place values in perfect vertical correspondence** [12].
* The units digit must sit above the units digit, the tens digit above the tens digit, the hundreds digit above the hundreds digit, and so forth [12].
* Draw a horizontal line below the numbers. The answer will be written under this line [12].

##### 2. Direction of Calculation
Always calculate from **right to left** [12]. Start with the smallest place value (the units column) and move left column by column (tens, hundreds, thousands) [12].

##### 3. The Carrying Mechanism (Addition)
Each place value column can only hold a single digit ($0$ to $9$) [12].
* If the sum of digits in a column is $9$ or less, write the result directly below that column [12].
* If the sum of digits in a column is $10$ or greater (for example, $9 + 1 = 10$), you cannot place two digits in one column slot [12].
* Instead, keep the single units digit in the current column and **carry the tens digit** to the top of the next column to the left [12].

**Why carrying works (Intuition):**
Since $10 \text{ tens} = 1 \text{ hundred}$, having $10$ in the tens column is worth exactly $1$ in the hundreds column [12]. Carrying moves that value to its correct place value position [12].

##### 4. The Borrowing Mechanism (Subtraction)
When subtracting column by column, the top digit must be equal to or larger than the bottom digit [12].
* If the top digit is smaller than the bottom digit (for example, $3 - 6$), you cannot perform the subtraction directly [12].
* To fix this, **borrow $1$** from the column directly to the left [12].
* Reduce the top digit in the left column by $1$, and add $10$ to the top digit of your current column [12]. Now you can subtract [12].

**Why borrowing works (Intuition):**
Taking $1$ from the tens column gives you $10$ units because $1 \text{ ten} = 10 \text{ units}$ [12]. Taking $1$ from the hundreds column gives you $10$ tens because $1 \text{ hundred} = 10 \text{ tens}$ [12]. You are not changing the total value of the number; you are simply regrouping it [12].

##### 5. Adding Multiple Numbers at Once
When adding a long list of numbers (such as $17, 22, 11, 34, 46$), adding them two at a time is slow [12]. 
* Stack all numbers vertically with matching place values [12].
* Add all digits in the units column together [12].
* If the total is $20$, place a $0$ in the units column and carry $2$ to the top of the tens column (because $20 \text{ units} = 2 \text{ tens}$) [12].
* Add the carried number to all the digits in the tens column [12].

---

#### 5. Formulas and Rules

##### Standard Vertical Addition Layout
$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c@{\quad}c}
& \text{Thousands} & \text{Hundreds} & \text{Tens} & \text{Units} \\
& & \scriptscriptstyle{\text{Carried}} & & \\
& a_3 & a_2 & a_1 & a_0 \\
+ & b_3 & b_2 & b_1 & b_0 \\
\hline
& s_3 & s_2 & s_1 & s_0
\end{array}$$

##### Standard Vertical Subtraction Layout
When subtracting, **always place the larger number on top** [12]:
$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c}
& \text{Hundreds} & \text{Tens} & \text{Units} \\
& a_2 & a_1 & a_0 \quad (\text{Larger Number}) \\
- & b_2 & b_1 & b_0 \quad (\text{Smaller Number}) \\
\hline
& d_2 & d_1 & d_0 \quad (\text{Difference})
\end{array}$$

##### Mathematical Rules for Regrouping:
1. **Carrying Rule (Addition):**
   $$\text{If Column Sum } S \ge 10:$$
   $$\text{Write in column} = S \bmod 10$$
   $$\text{Carry to next left column} = \lfloor S / 10 \rfloor$$

2. **Borrowing Rule (Subtraction):**
   $$\text{If Top Digit } T < \text{Bottom Digit } B:$$
   $$\text{New Left Top Digit} = \text{Old Left Top Digit} - 1$$
   $$\text{New Current Top Digit} = T + 10$$
   $$\text{Column Result} = (T + 10) - B$$

---

#### 6. Step-by-Step Examples

##### Example 1: Addition with Carrying
**Problem:** One market sold $1,293 \text{ apples}$ today, while another market sold $2,614 \text{ apples}$ [12]. How many apples were sold in total [12]?

**Solution:**

**Step 1: Set up the vertical alignment.**
Place $1,293$ above $2,614$. Align units, tens, hundreds, and thousands [12].

$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c@{\quad}c}
& 1 & 2 & 9 & 3 \\
+ & 2 & 6 & 1 & 4 \\
\hline
\end{array}$$

**Step 2: Add the units column (rightmost).**
$$3 + 4 = 7$$
Write $7$ in the units place below the line [12].

$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c@{\quad}c}
& 1 & 2 & 9 & 3 \\
+ & 2 & 6 & 1 & 4 \\
\hline
& & & & 7
\end{array}$$

**Step 3: Add the tens column.**
$$9 + 1 = 10$$
We cannot write $10$ in a single digit spot [12]. 
* Write $0$ in the tens place below the line [12].
* Carry $1$ to the top of the hundreds column [12].

$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c@{\quad}c}
& & \scriptscriptstyle{1} & & \\
& 1 & 2 & 9 & 3 \\
+ & 2 & 6 & 1 & 4 \\
\hline
& & & 0 & 7
\end{array}$$

**Step 4: Add the hundreds column.**
Include the carried $1$ [12]:
$$1 \text{ (carried)} + 2 + 6 = 9$$
Write $9$ in the hundreds place [12].

$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c@{\quad}c}
& & \scriptscriptstyle{1} & & \\
& 1 & 2 & 9 & 3 \\
+ & 2 & 6 & 1 & 4 \\
\hline
& & 9 & 0 & 7
\end{array}$$

**Step 5: Add the thousands column.**
$$1 + 2 = 3$$
Write $3$ in the thousands place [12].

$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c@{\quad}c}
& & \scriptscriptstyle{1} & & \\
& 1 & 2 & 9 & 3 \\
+ & 2 & 6 & 1 & 4 \\
\hline
& 3 & 9 & 0 & 7
\end{array}$$

**Final Answer:** A total of $3,907 \text{ apples}$ were sold [12].

---

##### Example 2: Subtraction with Borrowing
**Problem:** A market vendor started with $473 \text{ apples}$ and sold $286$ [12]. How many apples does the vendor have left [12]?

**Solution:**

**Step 1: Set up vertical alignment.**
Place the larger number ($473$) on top and the smaller number ($286$) below [12].

$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c}
& 4 & 7 & 3 \\
- & 2 & 8 & 6 \\
\hline
\end{array}$$

**Step 2: Subtract the units column.**
We have $3 - 6$. Since $3$ is smaller than $6$, we cannot subtract [12].
* Borrow $1$ ten from the tens digit ($7$) [12].
* The tens digit $7$ becomes $6$ [12].
* Add $10$ to the units digit $3$, making it $13$ ($3 + 10 = 13$) [12].
* Now calculate $13 - 6 = 7$ [12]. Write $7$ in the units place [12].

$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c}
& 4 & \cancel{7}^6 & \scriptscriptstyle{1}3 \\
- & 2 & 8 & 6 \\
\hline
& & & 7
\end{array}$$

**Step 3: Subtract the tens column.**
Now we have $6 - 8$ in the tens column [12]. Since $6$ is smaller than $8$, we cannot subtract [12].
* Borrow $1$ hundred from the hundreds digit ($4$) [12].
* The hundreds digit $4$ becomes $3$ [12].
* Add $10$ tens to the tens digit $6$, making it $16$ ($6 + 10 = 16$) [12].
* Now calculate $16 - 8 = 8$ [12]. Write $8$ in the tens place [12].

$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c}
& \cancel{4}^3 & \cancel{7}^{16} & \scriptscriptstyle{1}3 \\
- & 2 & 8 & 6 \\
\hline
& & 8 & 7
\end{array}$$

**Step 4: Subtract the hundreds column.**
Now calculate $3 - 2 = 1$ [12]. Write $1$ in the hundreds place [12].

$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c}
& \cancel{4}^3 & \cancel{7}^{16} & \scriptscriptstyle{1}3 \\
- & 2 & 8 & 6 \\
\hline
& 1 & 8 & 7
\end{array}$$

**Final Answer:** The vendor has $187 \text{ apples}$ left [12].

---

##### Example 3: Adding Multiple Numbers Simultaneously
**Problem:** Calculate the sum of $17, 22, 11, 34,$ and $46$ [12].

**Solution:**

**Step 1: Stack all numbers vertically by place value.**

$$\begin{array}{r@{\quad}c@{\quad}c}
& 1 & 7 \\
& 2 & 2 \\
& 1 & 1 \\
& 3 & 4 \\
+ & 4 & 6 \\
\hline
\end{array}$$

**Step 2: Add the units column.**
$$7 + 2 + 1 + 4 + 6 = 20$$
* Write $0$ in the units place below the line [12].
* Carry $2$ to the top of the tens column (since $20 \text{ units} = 2 \text{ tens}$) [12].

$$\begin{array}{r@{\quad}c@{\quad}c}
& \scriptscriptstyle{2} & \\
& 1 & 7 \\
& 2 & 2 \\
& 1 & 1 \\
& 3 & 4 \\
+ & 4 & 6 \\
\hline
& & 0
\end{array}$$

**Step 3: Add the tens column.**
Include the carried $2$ [12]:
$$2 \text{ (carried)} + 1 + 2 + 1 + 3 + 4 = 13$$
Since there is no hundreds column to carry to, write $13$ directly [12].

$$\begin{array}{r@{\quad}c@{\quad}c}
& \scriptscriptstyle{2} & \\
& 1 & 7 \\
& 2 & 2 \\
& 1 & 1 \\
& 3 & 4 \\
+ & 4 & 6 \\
\hline
& 13 & 0
\end{array}$$

**Final Answer:** The total sum is $130$ [12].

---

#### 7. Visual Explanations

##### Regrouping Visualized (Carrying)
When adding $9 \text{ tens}$ and $1 \text{ ten}$, we get $10 \text{ tens}$ [12]. Because of our Base-10 place value structure, $10 \text{ tens}$ are bundled together into $1 \text{ hundred}$ [12]:

$$\text{10 Tens } (\underbrace{10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10}_{100}) \longrightarrow \text{1 Hundred } (100)$$

##### Decomposing Visualized (Borrowing)
When borrowing $1 \text{ ten}$ for the units column, we break down $1 \text{ block of 10}$ into $10 \text{ single unit blocks}$ [12]:

$$\text{1 Ten } (10) \longrightarrow \text{10 Single Units } (\underbrace{1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1}_{10})$$

##### Column Alignment Matrix
| Operation | Thousands | Hundreds | Tens | Units |
| :--- | :---: | :---: | :---: | :---: |
| **Addition Example** | $1$ | $2$ | $9$ | $3$ |
| | $+ 2$ | $6$ | $1$ | $4$ |
| **Carried Digits** | | $\scriptscriptstyle{+1}$ | | |
| **Result** | **$3$** | **$9$** | **$0$** | **$7$** |

---

#### 8. Common Mistakes

##### Mistake 1: Misaligning Columns by Place Value
* **Wrong Approach:** Aligning numbers on the left instead of aligning units on the right.
  $$\begin{array}{r@{\quad}c@{\quad}c}
  & 4 & 7 & 3 \\
  + & 2 & 8 & \text{(Wrong alignment!)}
  \end{array}$$
* **Why it is wrong:** Adding $4 \text{ hundreds}$ to $2 \text{ tens}$ creates an incorrect calculation because place values are mixed up.
* **Correct Approach:** Always align digits starting from the **rightmost units place**.

##### Mistake 2: Forgetting to Add the Carried Digit
* **Wrong Approach:** In $1,293 + 2,614$, adding the tens column ($9 + 1 = 10$), writing $0$, carrying $1$, but then calculating the hundreds column as $2 + 6 = 8$ (forgetting the carried $1$).
* **Why it is wrong:** You lose $100$ from your total sum, giving an incorrect answer ($3,807$ instead of $3,907$).
* **Correct Approach:** Always write the carried number small at the top of the next column so you remember to add it.

##### Mistake 3: Subtracting the Top Digit from the Bottom Digit when Top is Smaller
* **Wrong Approach:** In $473 - 286$, looking at the units place ($3$ and $6$) and doing $6 - 3 = 3$.
* **Why it is wrong:** Subtraction is not commutative ($a - b \neq b - a$). You are taking away $286$ from $473$, not the other way around.
* **Correct Approach:** If the top digit is smaller, you **must borrow** from the column to the left.

##### Mistake 4: Forgetting to Reduce the Left Digit After Borrowing
* **Wrong Approach:** Borrowing $10$ for the units place ($3 \rightarrow 13$), but leaving the tens digit as $7$ instead of changing it to $6$.
* **Why it is wrong:** You effectively created $10$ extra units out of nowhere, making your answer too large by $10$.
* **Correct Approach:** Immediately cross out the left digit and write its new reduced value above it when borrowing.

---

#### 9. Practice Problems

##### Easy Problems
1. Calculate the sum:
   $$524 + 315$$
2. Calculate the difference:
   $$98 - 45$$

##### Medium Problems
3. Calculate the sum:
   $$1,584 + 2,739$$
4. Calculate the difference:
   $$624 - 358$$

##### Challenging Problems
5. Calculate the difference (Borrowing across zero):
   $$5,042 - 2,678$$
6. Calculate the total sum of five numbers simultaneously:
   $$48 + 15 + 83 + 29 + 67$$

---

#### 10. Solutions

##### Solution to Problem 1: $524 + 315$
**Step 1:** Align numbers vertically.
$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c}
& 5 & 2 & 4 \\
+ & 3 & 1 & 5 \\
\hline
\end{array}$$
**Step 2:** Units column: $4 + 5 = 9$.
**Step 3:** Tens column: $2 + 1 = 3$.
**Step 4:** Hundreds column: $5 + 3 = 8$.
**Final Result:** $839$.

---

##### Solution to Problem 2: $98 - 45$
**Step 1:** Align numbers vertically.
$$\begin{array}{r@{\quad}c@{\quad}c}
& 9 & 8 \\
- & 4 & 5 \\
\hline
\end{array}$$
**Step 2:** Units column: $8 - 5 = 3$.
**Step 3:** Tens column: $9 - 4 = 5$.
**Final Result:** $53$.

---

##### Solution to Problem 3: $1,584 + 2,739$
**Step 1:** Align numbers vertically.
$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c@{\quad}c}
& 1 & 5 & 8 & 4 \\
+ & 2 & 7 & 3 & 9 \\
\hline
\end{array}$$
**Step 2:** Units column: $4 + 9 = 13$. Write $3$, carry $1$ to tens.
**Step 3:** Tens column: $1 \text{ (carried)} + 8 + 3 = 12$. Write $2$, carry $1$ to hundreds.
**Step 4:** Hundreds column: $1 \text{ (carried)} + 5 + 7 = 13$. Write $3$, carry $1$ to thousands.
**Step 5:** Thousands column: $1 \text{ (carried)} + 1 + 2 = 4$. Write $4$.
$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c@{\quad}c}
& \scriptscriptstyle{1} & \scriptscriptstyle{1} & \scriptscriptstyle{1} & \\
& 1 & 5 & 8 & 4 \\
+ & 2 & 7 & 3 & 9 \\
\hline
& 4 & 3 & 2 & 3
\end{array}$$
**Final Result:** $4,323$.

---

##### Solution to Problem 4: $624 - 358$
**Step 1:** Align numbers vertically.
$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c}
& 6 & 2 & 4 \\
- & 3 & 5 & 8 \\
\hline
\end{array}$$
**Step 2:** Units column: $4 - 8$ requires borrowing. Borrow $1$ from tens digit $2$ (making it $1$). Units digit becomes $14$. Calculate $14 - 8 = 6$.
**Step 3:** Tens column: $1 - 5$ requires borrowing. Borrow $1$ from hundreds digit $6$ (making it $5$). Tens digit becomes $11$. Calculate $11 - 5 = 6$.
**Step 4:** Hundreds column: $5 - 3 = 2$.
$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c}
& \cancel{6}^5 & \cancel{2}^{11} & \scriptscriptstyle{1}4 \\
- & 3 & 5 & 8 \\
\hline
& 2 & 6 & 6
\end{array}$$
**Final Result:** $266$.

---

##### Solution to Problem 5: $5,042 - 2,678$ (Borrowing across zero)
**Step 1:** Align numbers vertically.
$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c@{\quad}c}
& 5 & 0 & 4 & 2 \\
- & 2 & 6 & 7 & 8 \\
\hline
\end{array}$$
**Step 2:** Units column: $2 - 8$ requires borrowing. Borrow $1$ from tens digit $4$ (making it $3$). Units digit becomes $12$. Calculate $12 - 8 = 4$.
**Step 3:** Tens column: $3 - 7$ requires borrowing from hundreds. But hundreds digit is $0$!
* First, borrow $1$ thousand from $5$ (making it $4$), turning the $0$ hundreds into $10$ hundreds.
* Now borrow $1$ hundred from $10$ (making it $9$), turning the $3$ tens into $13$ tens.
* Calculate $13 - 7 = 6$.
**Step 4:** Hundreds column: Calculate $9 - 6 = 3$.
**Step 5:** Thousands column: Calculate $4 - 2 = 2$.
$$\begin{array}{r@{\quad}c@{\quad}c@{\quad}c@{\quad}c}
& \cancel{5}^4 & \cancel{0}^9 & \cancel{4}^{13} & \scriptscriptstyle{1}2 \\
- & 2 & 6 & 7 & 8 \\
\hline
& 2 & 3 & 6 & 4
\end{array}$$
**Final Result:** $2,364$.

---

##### Solution to Problem 6: $48 + 15 + 83 + 29 + 67$
**Step 1:** Align all five numbers vertically.
$$\begin{array}{r@{\quad}c@{\quad}c}
& 4 & 8 \\
& 1 & 5 \\
& 8 & 3 \\
& 2 & 9 \\
+ & 6 & 7 \\
\hline
\end{array}$$
**Step 2:** Add units column: $8 + 5 + 3 + 9 + 7 = 32$.
* Write $2$ in units place.
* Carry $3$ to tens column ($32 \text{ units} = 3 \text{ tens} + 2 \text{ units}$).
**Step 3:** Add tens column: $3 \text{ (carried)} + 4 + 1 + 8 + 2 + 6 = 24$.
* Write $24$.
$$\begin{array}{r@{\quad}c@{\quad}c}
& \scriptscriptstyle{3} & \\
& 4 & 8 \\
& 1 & 5 \\
& 8 & 3 \\
& 2 & 9 \\
+ & 6 & 7 \\
\hline
& 24 & 2
\end{array}$$
**Final Result:** $242$.

---

#### 11. Summary
* Vertical addition and subtraction allow us to perform arithmetic on large numbers without physical counting [12].
* Numbers must always be stacked vertically with matching place values (units aligned with units, tens with tens) [12].
* Calculations always proceed from **right to left**, starting at the units place [12].
* In addition, when a column total is $10$ or greater, write the single units digit and **carry** the tens value to the next column on the left [12].
* In subtraction, when the top digit is smaller than the bottom digit, **borrow** $1$ from the next left column ($1 \text{ unit left} = 10 \text{ units current}$) [12].
* Long lists of numbers can be added simultaneously by summing entire columns at once [12].

---

#### 12. Key Things to Remember
1. **Always align by place value:** Line up units, tens, hundreds, and thousands vertically on the right edge [12].
2. **Work right to left:** Start at the units place and move left [12].
3. **Carrying rule:** $10 \text{ units} = 1 \text{ ten}$ and $10 \text{ tens} = 1 \text{ hundred}$ [12].
4. **Borrowing rule:** Borrowing $1$ from the left column adds $10$ to your current right column [12].
5. **Always write larger number on top** when performing subtraction [12].
6. **Don't forget carried numbers:** Write them small at the top of the column so you add them into your column total [12].
7. **Reduce when borrowing:** Immediately reduce the left top digit by $1$ when you borrow from it [12].
