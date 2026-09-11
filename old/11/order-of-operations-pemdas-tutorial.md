# Order of Arithmetic Operations: PEMDAS

#### 1. Introduction

When we solve mathematical problems, we often use several basic arithmetic operations: addition ($+$), subtraction ($-$), multiplication ($\times$), division ($\div$), and exponentiation ($a^n$). 

However, what happens when a single mathematical expression contains multiple operations at the same time? Consider the expression:

$$5 \times 3 + 4 - 2 \times 6$$

If we calculate from left to right:
1. $5 \times 3 = 15$
2. $15 + 4 = 19$
3. $19 - 2 = 17$
4. $17 \times 6 = 102$

If we calculate from right to left:
1. $2 \times 6 = 12$
2. $4 - 12 = -8$
3. $3 + (-8) = -5$
4. $5 \times (-5) = -25$

We get two completely different answers ($102$ and $-25$) for the exact same expression! Depending on which operation we perform first, we could get many different results.

To make sure that everyone around the world solves math problems in the exact same way and gets the same correct answer, mathematicians created an agreed rule called the **Order of Operations**. The standard rule for this order is remembered using the acronym **PEMDAS**.

---

#### 2. Prerequisite Knowledge

Before learning PEMDAS, make sure you are familiar with the five basic arithmetic operations:

* **Addition ($+$):** Combining numbers together (e.g., $3 + 4 = 7$).
* **Subtraction ($-$):** Taking one number away from another (e.g., $19 - 12 = 7$).
* **Multiplication ($\times$ or $\cdot$):** Repeated addition (e.g., $5 \times 3 = 15$).
* **Division ($\div$ or $/ Hawkes$):** Splitting a number into equal parts (e.g., $12 \div 3 = 4$).
* **Exponents ($a^b$):** Repeated multiplication of a base number by itself $b$ times. 
  * In the expression $2^3$, $2$ is the **base** and $3$ is the **exponent**.
  * $2^3 = 2 \times 2 \times 2 = 8$.
  * In the expression $5^2$, $5^2 = 5 \times 5 = 25$.

---

#### 3. Important Definitions

* **Expression:** A mathematical phrase containing numbers, operation symbols ($+$, $-$, $\times$, $\div$), and grouping symbols without an equal sign (for example, $15 + 3^2 - 4$).
* **Convention:** An agreed-upon rule or standard accepted by everyone in a field (such as mathematics).
* **PEMDAS:** An acronym that helps us remember the priority order of arithmetic operations:
  * **P** = Parentheses $( \ )$
  * **E** = Exponents $a^b$
  * **M** = Multiplication $\times$
  * **D** = Division $\div$
  * **A** = Addition $+$
  * **S** = Subtraction $-$
* **Equal Priority / Left-to-Right Rule:** Operations that share the same level of importance are evaluated in the order they appear from left to right.

---

#### 4. Main Concepts

The key idea of PEMDAS is that mathematical operations have a natural **hierarchy** (levels of priority). Higher-priority operations must be evaluated before lower-priority operations.

Here is the exact step-by-step order:

1. **Step 1: Parentheses $( \ )$**
   Calculate everything inside parentheses or grouping symbols first. If there are multiple or nested parentheses, start from the innermost pair and work outward.

2. **Step 2: Exponents $a^b$**
   Evaluate all powers and roots next.

3. **Step 3: Multiplication ($\times$) and Division ($\div$)**
   Perform all multiplication and division operations. 
   > **Crucial Rule:** Multiplication does **not** take precedence over division. They have **equal priority**. Evaluate them from **left to right** as they appear in the expression.

4. **Step 4: Addition ($+$) and Subtraction ($-$ )**
   Perform all addition and subtraction operations last.
   > **Crucial Rule:** Addition does **not** take precedence over subtraction. They have **equal priority**. Evaluate them from **left to right** as they appear in the expression.

---

#### 5. Formulas and Rules

##### Priority Summary Table

| Priority Level | Acronym Letter | Operation Name | Symbol / Form | Direction / Rule |
| :--- | :---: | :--- | :---: | :--- |
| **1st (Highest)** | **P** | Parentheses | $( \ ), [ \ ], \{ \ \}$ | Innermost to outermost |
| **2nd** | **E** | Exponents | $a^b, \sqrt{x}$ | Left to right |
| **3rd** | **M & D** | Multiplication & Division | $\times, \cdot, \div, /$ | **Equal priority** (Left to right) |
| **4th (Lowest)** | **A & S** | Addition & Subtraction | $+ , -$ | **Equal priority** (Left to right) |

---

#### 6. Step-by-Step Examples

##### Example 1: Basic Operations without Parentheses (Easy)

**Problem:**
Evaluate the expression:
$$5 \times 3 + 4 - 2 \times 6$$

**Step-by-Step Solution:**

1. **Check Parentheses (P):** None present.
2. **Check Exponents (E):** None present.
3. **Multiplication and Division (M & D) from left to right:**
   * First multiplication: $5 \times 3 = 15$
   * Second multiplication: $2 \times 6 = 12$
   * Rewrite the expression:
     $$15 + 4 - 12$$

4. **Addition and Subtraction (A & S) from left to right:**
   * Perform addition first (since it appears first from the left): $15 + 4 = 19$
   * Rewrite the expression:
     $$19 - 12$$
   * Perform subtraction: $19 - 12 = 7$

**Final Answer:**
$$\mathbf{7}$$

---

##### Example 2: Expression with Parentheses and Exponents (Medium)

**Problem:**
Evaluate the expression:
$$15 + (3 + 2)^2 - 9 \times 6 + 2^3$$

**Step-by-Step Solution:**

1. **Parentheses (P):**
   * Simplify the term inside parentheses: $(3 + 2) = 5$
   * Substitute back into expression:
     $$15 + 5^2 - 9 \times 6 + 2^3$$

2. **Exponents (E):**
   * Evaluate $5^2 = 5 \times 5 = 25$
   * Evaluate $2^3 = 2 \times 2 \times 2 = 8$
   * Substitute back into expression:
     $$15 + 25 - 9 \times 6 + 8$$

3. **Multiplication and Division (M & D):**
   * Perform multiplication: $9 \times 6 = 54$
   * Substitute back into expression:
     $$15 + 25 - 54 + 8$$

4. **Addition and Subtraction (A & S) from left to right:**
   * First operation from left ($15 + 25$): $15 + 25 = 40$
     $$40 - 54 + 8$$
   * Next operation from left ($40 - 54$): $40 - 54 = -14$
     $$-14 + 8$$
   * Final operation ($-14 + 8$): $-14 + 8 = -6$

**Final Answer:**
$$\mathbf{-6}$$

---

##### Example 3: Nested Grouping and Left-to-Right Chain (Challenging)

**Problem:**
Evaluate the expression:
$$100 \div 5 \times 2 - [4 + (8 - 3^2)]$$

**Step-by-Step Solution:**

1. **Innermost Parentheses (P):**
   * Look inside $[4 + (8 - 3^2)]$. The innermost part is $(8 - 3^2)$.
   * Inside $(8 - 3^2)$, apply exponent rules first: $3^2 = 9$.
   * Evaluate innermost subtraction: $8 - 9 = -1$.
   * Expression becomes:
     $$100 \div 5 \times 2 - [4 + (-1)]$$

2. **Outer Bracket / Grouping:**
   * Evaluate $[4 + (-1)] = 4 - 1 = 3$.
   * Expression becomes:
     $$100 \div 5 \times 2 - 3$$

3. **Multiplication and Division (M & D) from left to right:**
   * Notice that division ($100 \div 5$) comes **before** multiplication ($\times 2$) from left to right!
   * First, evaluate division: $100 \div 5 = 20$.
     $$20 \times 2 - 3$$
   * Next, evaluate multiplication: $20 \times 2 = 40$.
     $$40 - 3$$

4. **Addition and Subtraction (A & S):**
   * Subtract: $40 - 3 = 37$.

**Final Answer:**
$$\mathbf{37}$$

---

#### 7. Visual Explanations

##### Flowchart of PEMDAS Decision Process

```
                   +------------------------+
                   |  Start Expression      |
                   +-----------+------------+
                               |
                               v
                   /------------------------\
                  /  Any Parentheses (P)?    \--- YES ---> Simplify innermost terms
                  \--------------------------/             first
                               | NO
                               v
                   /------------------------\
                  /    Any Exponents (E)?   \--- YES ---> Evaluate powers & roots
                  \--------------------------/
                               | NO
                               v
                   /------------------------\
                  / Any Multiplication (M)  \--- YES ---> Perform from LEFT to RIGHT
                  \  or Division (D)?       /             as they appear
                   \------------------------/
                               | NO
                               v
                   /------------------------\
                  /   Any Addition (A)      \--- YES ---> Perform from LEFT to RIGHT
                  \   or Subtraction (S)?   /             as they appear
                   \------------------------/
                               | NO
                               v
                   +------------------------+
                   | Final Answer Reached   |
                   +------------------------+
```

##### Level Diagram of Priority

```
Level 1 (Top Priority):    [  P  ]  Parentheses  ( )  [ ]  { }
                                |
Level 2:                   [  E  ]  Exponents    a^b
                                |
Level 3:                   [ M  D ] Multiplication & Division (Equal Priority: Left to Right)
                                |
Level 4 (Lowest Priority): [ A  S ] Addition & Subtraction       (Equal Priority: Left to Right)
```

---

#### 8. Common Mistakes

##### Mistake 1: Thinking Multiplication Always Comes Before Division

* **The Misconception:** Students often assume that because **M** comes before **D** in the letter sequence PEMDAS, multiplication must always be done first.
* **Incorrect Approach:**
  $$12 \div 3 \times 2$$
  * Incorrect: $3 \times 2 = 6 \implies 12 \div 6 = 2$  *(WRONG!)*
* **Correct Explanation:** 
  Multiplication and division have equal priority. Work strictly from **left to right**.
  * Correct: $12 \div 3 = 4 \implies 4 \times 2 = 8$  *(CORRECT!)*

##### Mistake 2: Thinking Addition Always Comes Before Subtraction

* **The Misconception:** Assuming that because **A** comes before **S**, addition must always be completed before subtraction.
* **Incorrect Approach:**
  $$10 - 4 + 2$$
  * Incorrect: $4 + 2 = 6 \implies 10 - 6 = 4$  *(WRONG!)*
* **Correct Explanation:**
  Addition and subtraction have equal priority. Work strictly from **left to right**.
  * Correct: $10 - 4 = 6 \implies 6 + 2 = 8$  *(CORRECT!)*

##### Mistake 3: Forgetting to Apply Exponent to Parentheses Terms Correctly

* **The Misconception:** Multiplying before calculating the exponent inside or outside parentheses.
* **Example:** $3 \times 2^3$
  * Incorrect: $(3 \times 2)^3 = 6^3 = 216$  *(WRONG!)*
  * Correct: Evaluate exponent first: $2^3 = 8 \implies 3 \times 8 = 24$  *(CORRECT!)*

---

#### 9. Practice Problems

Try solving these practice problems on your own before checking the solutions.

1. **Problem 1 (Easy):** 
   Evaluate $$18 - 3 \times 4 + 2$$

2. **Problem 2 (Easy):** 
   Evaluate $$24 \div 6 \times 2$$

3. **Problem 3 (Medium):** 
   Evaluate $$5 + 2 \times (8 - 3)^2$$

4. **Problem 4 (Medium):** 
   Evaluate $$40 - 2^4 \div 4 + 7$$

5. **Problem 5 (Challenging):** 
   Evaluate $$3 \times [15 - (2 + 3)^2 \div 5] + 6$$

---

#### 10. Solutions

##### Solution to Problem 1
$$18 - 3 \times 4 + 2$$
1. Multiplication first: $3 \times 4 = 12$
   $$18 - 12 + 2$$
2. Subtraction and Addition left to right: $18 - 12 = 6$
   $$6 + 2 = 8$$
**Answer:** $\mathbf{8}$

##### Solution to Problem 2
$$24 \div 6 \times 2$$
1. Division and Multiplication have equal priority. Go left to right.
2. First operation from left ($24 \div 6$): $24 \div 6 = 4$
   $$4 \times 2 = 8$$
**Answer:** $\mathbf{8}$

##### Solution to Problem 3
$$5 + 2 \times (8 - 3)^2$$
1. Parentheses first: $(8 - 3) = 5$
   $$5 + 2 \times 5^2$$
2. Exponent next: $5^2 = 25$
   $$5 + 2 \times 25$$
3. Multiplication next: $2 \times 25 = 50$
   $$5 + 50 = 55$$
**Answer:** $\mathbf{55}$

##### Solution to Problem 4
$$40 - 2^4 \div 4 + 7$$
1. Exponent first: $2^4 = 16$
   $$40 - 16 \div 4 + 7$$
2. Division next: $16 \div 4 = 4$
   $$40 - 4 + 7$$
3. Subtraction and Addition left to right: $40 - 4 = 36$
   $$36 + 7 = 43$$
**Answer:** $\mathbf{43}$

##### Solution to Problem 5
$$3 \times [15 - (2 + 3)^2 \div 5] + 6$$
1. Innermost parentheses: $(2 + 3) = 5$
   $$3 \times [15 - 5^2 \div 5] + 6$$
2. Exponents inside bracket: $5^2 = 25$
   $$3 \times [15 - 25 \div 5] + 6$$
3. Division inside bracket: $25 \div 5 = 5$
   $$3 \times [15 - 5] + 6$$
4. Subtraction inside bracket: $15 - 5 = 10$
   $$3 \times 10 + 6$$
5. Multiplication next: $3 \times 10 = 30$
   $$30 + 6 = 36$$
**Answer:** $\mathbf{36}$

---

#### 11. Summary

The order of operations is a standard mathematical convention that ensures everyone calculates mathematical expressions consistently and gets the exact same result. The acronym **PEMDAS** stands for **P**arentheses, **E**xponents, **M**ultiplication, **D**ivision, **A**ddition, and **S**ubtraction. 

Always remember that Multiplication and Division share equal priority, as do Addition and Subtraction. When two operations share equal priority, evaluate them from left to right as they appear in the expression.

---

#### 12. Key Things to Remember

* **Parentheses First:** Always resolve grouping symbols $( \ ), [ \ ], \{ \ \}$ from the inside out.
* **Exponents Second:** Evaluate powers and roots before basic operations.
* **Equal Priority Pairs:**
  * $\mathbf{M \ \& \ D}$ are equal: Evaluate from **Left to Right**.
  * $\mathbf{A \ \& \ S}$ are equal: Evaluate from **Left to Right**.
* **Don't Rush:** Work step-by-step, rewriting the expression after each completed step to avoid simple mistakes.
