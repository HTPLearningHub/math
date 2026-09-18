# Square Roots, Cube Roots, and Other Roots

#### 1. Introduction
In mathematics, we often need to undo operations. For example, subtraction undoes addition, and division undoes multiplication. When we work with exponents (powers), such as squaring or cubing a number, we also need an operation to undo them. This inverse operation is called taking a **root**.

Understanding roots is essential for:
* Solving algebraic equations like $x^2 = 9$ or $x^3 = 27$.
* Working with geometric measurements, such as finding the side length of a square when you know its area.
* Understanding number systems, including whole numbers, fractions, and **irrational numbers** (numbers with non-repeating infinite decimals).
* Simplifying complex mathematical formulas in science and engineering.

In this tutorial, you will learn what square roots, cube roots, and higher-order roots are, how they work, how to simplify them, and how to represent them using fractional exponents.

---

#### 2. Prerequisite Knowledge
Before learning about roots, let us review a few basic mathematical ideas.

##### Inverse Operations
An **inverse operation** is an operation that reverses or "undoes" the effect of another operation.
* **Addition and Subtraction**: If you start with $x$ and add $2$, you get $x + 2$. To get back to $x$, you subtract $2$:
  $$(x + 2) - 2 = x$$
* **Multiplication and Division**: If you multiply $x$ by $3$, you get $3x$. To get back to $x$, you divide by $3$:
  $$\frac{3x}{3} = x$$

##### Exponents (Powers)
An **exponent** tells us how many times to multiply a number by itself.
* **Squaring a number** ($x^2$): Multiplying $x$ by itself once.
  $$5^2 = 5 \times 5 = 25$$
* **Cubing a number** ($x^3$): Multiplying $x$ by itself twice.
  $$2^3 = 2 \times 2 \times 2 = 8$$

##### Multiplication Sign Rules
When multiplying positive and negative numbers:
1. **Positive $\times$ Positive = Positive**:
   $$(+3) \times (+3) = +9$$
2. **Negative $\times$ Negative = Positive**:
   $$(-3) \times (-3) = +9$$
3. **Negative $\times$ Negative $\times$ Negative = Negative**:
   $$(-3) \times (-3) \times (-3) = (+9) \times (-3) = -27$$

Keep these sign rules in mind because they explain why square roots and cube roots behave differently!

---

#### 3. Important Definitions

* **Radical Symbol ($\sqrt{\phantom{x}}$)**: The mathematical symbol used to denote a root.
* **Radicand**: The number or expression placed inside (under) the radical symbol. In $\sqrt{9}$, the radicand is $9$.
* **Index ($n$)**: The small number written on the top-left of the radical symbol $\sqrt[n]{x}$ that indicates which root is being taken. 
  * If no index is written (e.g., $\sqrt{x}$), the index is understood to be $2$ (a square root).
  * If the index is $3$ (e.g., $\sqrt[3]{x}$), it is a **cube root**.
* **Square Root**: A value that, when multiplied by itself, gives the original number.
* **Principal Square Root**: The non-negative (positive or zero) square root of a number. Symbolized as $\sqrt{x}$.
* **Perfect Square**: An integer whose square root is a whole number (e.g., $1, 4, 9, 16, 25, 36, 49, 64, 81, 100$).
* **Irrational Number**: A number that cannot be written as a simple fraction $\frac{a}{b}$ (where $a$ and $b$ are integers). Its decimal form goes on forever without repeating.
* **Cube Root**: A value that, when multiplied by itself three times, gives the original number.
* **Even Root**: A root where the index $n$ is an even integer ($n = 2, 4, 6, \dots$).
* **Odd Root**: A root where the index $n$ is an odd integer ($n = 3, 5, 7, \dots$).

---

#### 4. Main Concepts

##### Concept 1: The Square Root as the Inverse of Squaring
When we have an equation such as $x^2 = 9$, we want to find the value of $x$. To isolate $x$, we take the square root of both sides.
Taking the square root asks: *"What number multiplied by itself equals the radicand?"*

Because:
$$(+3) \times (+3) = 9$$
and
$$(-3) \times (-3) = 9$$

Both $+3$ and $-3$ are valid solutions! Therefore:
$$\sqrt{9} = \pm 3 \quad \text{(read as "plus or minus 3")}$$

##### Concept 2: Square Roots of Negative Numbers (Real Numbers Only)
What is $\sqrt{-9}$?
Let us check potential answers:
* Could it be $+3$? No, because $(+3) \times (+3) = +9$.
* Could it be $-3$? No, because $(-3) \times (-3) = +9$.

There is **no real number** that equals $-9$ when multiplied by itself. 
* **Rule**: You cannot take the square root of a negative number in the real number system. (In advanced math, this leads to *imaginary numbers*, but for basic algebra, there is no real solution).

##### Concept 3: Perfect Squares vs. Non-Perfect Squares
* **Perfect Squares**: Numbers like $4, 9, 16, 25$ yield clean integer roots:
  $$\sqrt{4} = \pm 2, \quad \sqrt{16} = \pm 4, \quad \sqrt{25} = \pm 5$$
* **Non-Perfect Squares**: Numbers like $2, 3, 5, 8, 27$ do not yield integers when taking square roots.
  * Their values are decimal numbers that never terminate and never repeat (irrational numbers).
  * For example, $\sqrt{2} \approx 1.41421356\dots$

##### Concept 4: Simplifying Radical Expressions
When a number is not a perfect square, we can simplify the radical by breaking it into factors, looking for factors that **are** perfect squares.

Using the **Product Property of Radicals**:
$$\sqrt{A \times B} = \sqrt{A} \times \sqrt{B}$$

**Example**: Simplify $\sqrt{8}$
1. Break $8$ into factors: $8 = 4 \times 2$. Notice that $4$ is a perfect square!
2. Apply the product rule: $\sqrt{8} = \sqrt{4 \times 2} = \sqrt{4} \times \sqrt{2}$.
3. Evaluate $\sqrt{4}$: $\sqrt{4} = 2$.
4. Combine: $\sqrt{8} = \pm 2\sqrt{2}$.

##### Concept 5: Cube Roots ($\sqrt[3]{x}$)
A **cube root** undoes cubing a number. It asks: *"What number multiplied by itself 3 times gives the radicand?"*

For $x^3 = 27$:
$$3 \times 3 \times 3 = 27 \implies \sqrt[3]{27} = 3$$

Cube roots differ from square roots in two important ways:
1. **Odd roots have only ONE real solution**: 
   * $(-3) \times (-3) \times (-3) = -27$.
   * Therefore, $(-3)$ does **not** yield $+27$. So $\sqrt[3]{27}$ is **only** $+3$, not $-3$.
2. **You CAN take the cube root of a negative number**:
   * What is $\sqrt[3]{-27}$?
   * Since $(-3) \times (-3) \times (-3) = -27$, we get:
     $$\sqrt[3]{-27} = -3$$

##### Concept 6: Generalizing Higher Roots (Even vs. Odd Index)
* **Even Roots** ($n = 2, 4, 6, \dots$):
  * Positive radicand $\implies$ Two real solutions ($\pm$).
  * Negative radicand $\implies$ No real solution.
* **Odd Roots** ($n = 3, 5, 7, \dots$):
  * Positive radicand $\implies$ One positive real solution.
  * Negative radicand $\implies$ One negative real solution.

##### Concept 7: Roots as Fractional Exponents
One of the most powerful concepts in algebra is expressing roots as powers with fractional exponents.

Why is $\sqrt{x} = x^{1/2}$?
Recall the exponent rule for multiplication: $x^a \cdot x^b = x^{a+b}$.
We know that:
$$\sqrt{x} \cdot \sqrt{x} = x^1$$
If we replace $\sqrt{x}$ with $x^{1/2}$:
$$x^{1/2} \cdot x^{1/2} = x^{\frac{1}{2} + \frac{1}{2}} = x^1 = x$$

Thus, taking a root is identical to raising a base to a fractional power:
$$\sqrt[n]{x} = x^{\frac{1}{n}}$$
$$\sqrt[n]{x^m} = x^{\frac{m}{n}}$$

---

#### 5. Formulas and Rules

| Rule Name | Mathematical Formula | Conditions / Notes |
| :--- | :--- | :--- |
| **Square Root Definition** | $y = \sqrt{x} \iff y^2 = x$ | $x \ge 0$ for real solutions |
| **Square Root of Equation** | $x^2 = k \implies x = \pm \sqrt{k}$ | Produces both positive & negative solutions |
| **Product Property of Radicals** | $\sqrt[n]{a \cdot b} = \sqrt[n]{a} \cdot \sqrt[n]{b}$ | $a, b \ge 0$ for even $n$ |
| **Quotient Property of Radicals** | $\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$ | $b \neq 0$ |
| **Odd Root of Negative Number** | $\sqrt[n]{-a} = -\sqrt[n]{a}$ | Only valid when $n$ is odd |
| **Fractional Exponents** | $\sqrt[n]{x} = x^{1/n}$ | Converts radical to exponential form |
| **General Power-Root Formula** | $\sqrt[n]{x^m} = (x^{1/n})^m = x^{\frac{m}{n}}$ | $n$ is the root (denominator), $m$ is power (numerator) |

---

#### 6. Step-by-Step Examples

##### Example 1 (Easy): Solving a Square Root Equation
**Problem**: Solve for $x$ in the equation $x^2 = 25$.

**Step-by-Step Reasoning**:
1. Identify the operation applied to $x$: $x$ is raised to the 2nd power (squared).
2. Perform the inverse operation: Take the square root of both sides of the equation.
   $$\sqrt{x^2} = \sqrt{25}$$
3. Find all numbers that equal $25$ when squared:
   * $(+5) \times (+5) = 25$
   * $(-5) \times (-5) = 25$
4. Write the complete solution:
   $$x = \pm 5$$

---

##### Example 2 (Easy): Evaluating a Simple Cube Root
**Problem**: Find the value of $\sqrt[3]{64}$.

**Step-by-Step Reasoning**:
1. Identify the index: The index is $3$ (cube root).
2. Ask the key question: *"What number multiplied by itself 3 times equals $64$?"*
3. Test small integer values:
   * $2 \times 2 \times 2 = 8$
   * $3 \times 3 \times 3 = 27$
   * $4 \times 4 \times 4 = 64$
4. Conclude the answer:
   $$\sqrt[3]{64} = 4$$

---

##### Example 3 (Medium): Simplifying a Non-Perfect Square Radical
**Problem**: Simplify $\sqrt{27}$.

**Step-by-Step Reasoning**:
1. Check if $27$ is a perfect square: $5^2 = 25$ and $6^2 = 36$, so $27$ is not a perfect square.
2. Find factors of $27$: The factors of $27$ are $1, 3, 9, 27$.
3. Identify the largest factor that is a perfect square: $9$ is a perfect square ($3^2 = 9$).
4. Rewrite $27$ as a product of $9$ and $3$:
   $$\sqrt{27} = \sqrt{9 \times 3}$$
5. Apply the Product Property of Radicals:
   $$\sqrt{27} = \sqrt{9} \times \sqrt{3}$$
6. Simplify $\sqrt{9}$ to $\pm 3$:
   $$\sqrt{27} = \pm 3\sqrt{3}$$

---

##### Example 4 (Medium): Evaluating a Negative Cube Root
**Problem**: Evaluate $\sqrt[3]{-125}$.

**Step-by-Step Reasoning**:
1. Identify the index and radicand: Index is $3$ (odd root), radicand is $-125$ (negative).
2. Recall the rule for odd roots: An odd root of a negative number has a negative real solution.
3. Find the cube root of the positive number $125$:
   $$5 \times 5 \times 5 = 125 \implies \sqrt[3]{125} = 5$$
4. Apply the negative sign:
   $$(-5) \times (-5) \times (-5) = -125$$
5. Final answer:
   $$\sqrt[3]{-125} = -5$$

---

##### Example 5 (Challenging): Simplifying Higher Order Radicals with Variables
**Problem**: Simplify $\sqrt[4]{16 x^8}$.

**Step-by-Step Reasoning**:
1. Split the radical using the product property:
   $$\sqrt[4]{16 x^8} = \sqrt[4]{16} \times \sqrt[4]{x^8}$$
2. Evaluate $\sqrt[4]{16}$:
   * Ask: What number raised to the 4th power gives $16$?
   * $2 \times 2 \times 2 \times 2 = 16 \implies \sqrt[4]{16} = \pm 2$.
3. Convert $\sqrt[4]{x^8}$ into fractional exponent form:
   $$\sqrt[4]{x^8} = x^{\frac{8}{4}} = x^2$$
4. Multiply the simplified terms together:
   $$\sqrt[4]{16 x^8} = \pm 2 x^2$$

---

#### 7. Visual Explanations

##### 1. Perfect Squares vs. Irrational Roots on a Number Line
On a number line, perfect squares land exactly on whole integer values. Non-perfect squares fall in between them as irrational decimals:

```
 Integer Points:   0       1       2       3       4       5       6
                   |-------|-------|-------|-------|-------|-------|
 Perfect Squares:       √(1)=1  √(4)=2  √(9)=3  √(16)=4 √(25)=5 √(36)=6
                                  ^       ^               ^
 Irrationals:             √(2)≈1.414    √(8)≈2.828     √(27)≈5.196
```

##### 2. Comparing Even Roots vs. Odd Roots

| Feature | Even Root (e.g., Square Root $\sqrt{x}$) | Odd Root (e.g., Cube Root $\sqrt[3]{x}$) |
| :--- | :--- | :--- |
| **Default Index** | $n = 2$ | $n = 3$ |
| **Solutions for Positive Radicand ($+x$)** | 2 solutions ($\pm \sqrt{x}$) | 1 positive solution |
| **Solutions for Negative Radicand ($-x$)** | No real solution | 1 negative solution |
| **Example Positive** | $\sqrt{9} = \pm 3$ | $\sqrt[3]{27} = 3$ |
| **Example Negative** | $\sqrt{-9} \implies \text{Not real}$ | $\sqrt[3]{-27} = -3$ |
| **Graph Behavior** | Defined only for $x \ge 0$ | Defined for all real $x$ ($-\infty < x < \infty$) |

---

#### 8. Common Mistakes

##### Mistake 1: Forgetting the negative solution when taking square roots of equations
* **Incorrect**: $x^2 = 16 \implies x = 4$.
* **Why it is wrong**: $(-4) \times (-4)$ also equals $16$.
* **Correct Approach**: Always write $x = \pm 4$.

##### Mistake 2: Claiming that square roots of negative numbers equal negative numbers
* **Incorrect**: $\sqrt{-16} = -4$.
* **Why it is wrong**: Test the answer: $(-4) \times (-4) = +16$, not $-16$.
* **Correct Approach**: Recognize that $\sqrt{-16}$ has no real solution.

##### Mistake 3: Believing cube roots cannot be negative
* **Incorrect**: $\sqrt[3]{-8}$ has no solution.
* **Why it is wrong**: Cube roots have an odd index ($3$). $(-2) \times (-2) \times (-2) = -8$.
* **Correct Approach**: $\sqrt[3]{-8} = -2$.

##### Mistake 4: Incorrectly simplifying non-perfect square radicals
* **Incorrect**: $\sqrt{8} = 4$.
* **Why it is wrong**: $4 \times 4 = 16$, not $8$. $8$ is not a perfect square, but it contains a perfect square factor ($4$).
* **Correct Approach**: $\sqrt{8} = \sqrt{4 \times 2} = \sqrt{4}\sqrt{2} = \pm 2\sqrt{2}$.

##### Mistake 5: Misinterpreting fractional exponent positions
* **Incorrect**: $\sqrt[3]{x^2} = x^{3/2}$.
* **Why it is wrong**: The root index goes in the **denominator**, and the exponent power goes in the **numerator**.
* **Correct Approach**: $\sqrt[3]{x^2} = x^{\frac{2}{3}}$.

---

#### 9. Practice Problems

Try solving these problems to test your understanding! Solutions are provided in the next section.

##### Easy Level
1. Solve for $x$: $x^2 = 49$.
2. Find the value of $\sqrt[3]{125}$.
3. Convert $\sqrt{x^6}$ into exponential form and simplify.

##### Medium Level
4. Simplify the radical expression $\sqrt{50}$.
5. Evaluate $\sqrt[3]{-64}$.
6. Solve for $y$: $y^3 = -216$.

##### Challenging Level
7. Simplify the radical expression $\sqrt{72}$.
8. Rewrite $x^{\frac{5}{3}}$ in radical form and simplify $\sqrt[3]{x^5}$.

---

#### 10. Solutions

##### Solution 1
* **Problem**: $x^2 = 49$.
* **Step 1**: Take the square root of both sides: $x = \pm \sqrt{49}$.
* **Step 2**: Since $7 \times 7 = 49$, $\sqrt{49} = 7$.
* **Answer**: $x = \pm 7$.

##### Solution 2
* **Problem**: $\sqrt[3]{125}$.
* **Step 1**: Find a number that multiplied by itself 3 times equals $125$.
* **Step 2**: Check $5 \times 5 \times 5 = 125$.
* **Answer**: $5$.

##### Solution 3
* **Problem**: Convert $\sqrt{x^6}$ to exponential form and simplify.
* **Step 1**: Write radical as power: $\sqrt{x^6} = (x^6)^{\frac{1}{2}}$.
* **Step 2**: Multiply exponents: $6 \times \frac{1}{2} = 3$.
* **Answer**: $x^3$.

##### Solution 4
* **Problem**: Simplify $\sqrt{50}$.
* **Step 1**: Find factors of $50$: $25 \times 2 = 50$, where $25$ is a perfect square.
* **Step 2**: Apply product rule: $\sqrt{50} = \sqrt{25 \times 2} = \sqrt{25} \times \sqrt{2}$.
* **Step 3**: Evaluate $\sqrt{25} = 5$.
* **Answer**: $\pm 5\sqrt{2}$.

##### Solution 5
* **Problem**: Evaluate $\sqrt[3]{-64}$.
* **Step 1**: Odd root of negative number yields a negative result.
* **Step 2**: Since $4 \times 4 \times 4 = 64$, $(-4) \times (-4) \times (-4) = -64$.
* **Answer**: $-4$.

##### Solution 6
* **Problem**: Solve $y^3 = -216$.
* **Step 1**: Take cube root of both sides: $y = \sqrt[3]{-216}$.
* **Step 2**: Find number: $6 \times 6 \times 6 = 216 \implies (-6)^3 = -216$.
* **Answer**: $y = -6$.

##### Solution 7
* **Problem**: Simplify $\sqrt{72}$.
* **Step 1**: Find largest perfect square factor of $72$: $36 \times 2 = 72$.
* **Step 2**: Apply product property: $\sqrt{72} = \sqrt{36 \times 2} = \sqrt{36} \times \sqrt{2}$.
* **Step 3**: Simplify $\sqrt{36} = 6$.
* **Answer**: $\pm 6\sqrt{2}$.

##### Solution 8
* **Problem**: Rewrite $x^{\frac{5}{3}}$ in radical form and simplify $\sqrt[3]{x^5}$.
* **Step 1**: Denominator $3$ is index, numerator $5$ is power: $x^{5/3} = \sqrt[3]{x^5}$.
* **Step 2**: Factor $x^5$ into $x^3 \cdot x^2$: $\sqrt[3]{x^3 \cdot x^2} = \sqrt[3]{x^3} \cdot \sqrt[3]{x^2}$.
* **Step 3**: Simplify $\sqrt[3]{x^3} = x$.
* **Answer**: $x\sqrt[3]{x^2}$.

---

#### 11. Summary
* **Taking a root** is the inverse operation of raising a number to an exponent.
* **Square roots** ($\sqrt{x}$) undo squaring ($x^2$). Positive numbers have two real square roots ($\pm$). Negative numbers have no real square roots.
* **Cube roots** ($\sqrt[3]{x}$) undo cubing ($x^3$). Every real number has exactly one real cube root. Negative numbers have negative cube roots.
* **Radicals can be simplified** by factoring out perfect squares using $\sqrt{A \cdot B} = \sqrt{A}\sqrt{B}$.
* **Roots are fractional exponents**: $\sqrt[n]{x^m} = x^{\frac{m}{n}}$, where the root index is always in the denominator.

---

#### 12. Key Things to Remember
* $\sqrt{x^2} = \pm x$ when solving equations (don't forget the negative root!).
* Even roots ($n=2, 4, 6$) of negative numbers $\implies$ **No real solution**.
* Odd roots ($n=3, 5, 7$) of negative numbers $\implies$ **Negative real solution**.
* Radical conversion formula: $\mathbf{\sqrt[index]{base^{power}} = base^{\frac{power}{index}}}$.
* Memorize the first 10 perfect squares: $1, 4, 9, 16, 25, 36, 49, 64, 81, 100$.
* Memorize the first 5 perfect cubes: $1, 8, 27, 64, 125$.
