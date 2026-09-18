# Solving Quadratic Equations using the Quadratic Formula

A complete, beginner-friendly mathematical tutorial based on the video tutorial by Professor Dave Explains.

---

## 1. Introduction

In algebra, a **quadratic equation** is a polynomial equation where the highest exponent of the variable $x$ is $2$. A general quadratic equation looks like this:

$$ax^2 + bx + c = 0$$

In earlier lessons, you may have learned to solve simple quadratic equations like $4x^2 = 64$ by performing inverse operations (dividing by $4$ and taking the square root):

$$x^2 = 16 \implies x = \pm 4$$

However, when an equation contains both an $x^2$ term and an $x$ term (such as $ax^2 + bx + c = 0$), finding $x$ becomes more difficult. While methods like **factoring** or **completing the square** work well for specific examples, they can be slow, complicated, or impossible when the numbers are messy.

To solve any quadratic equation quickly and directly, we use a general formula called the **Quadratic Formula**. By simply identifying the coefficients $a$, $b$, and $c$, we can plug them directly into the formula to find the exact solutions for $x$.

---

## 2. Prerequisite Knowledge

Before studying the Quadratic Formula, make sure you understand these basic mathematical ideas:

1. **Variables, Coefficients, and Constants**:
   - **Variable**: A letter representing an unknown number (for example, $x$).
   - **Coefficient**: A number multiplied by a variable (in $3x^2$, $3$ is the coefficient of $x^2$).
   - **Constant**: A fixed number with no variable attached (for example, $+5$ or $-7$).

2. **The $\pm$ (Plus-or-Minus) Symbol**:
   - The symbol $\pm$ means "plus or minus". It shows that there are two separate calculations: one using addition and one using subtraction.
   - For example, $x = 3 \pm 2$ means:
     $$x_1 = 3 + 2 = 5 \quad \text{and} \quad x_2 = 3 - 2 = 1$$

3. **Square Roots ($\sqrt{\quad}$)**:
   - A square root asks: "What number multiplied by itself gives this value?"
   - For example, $\sqrt{16} = 4$ because $4 \times 4 = 16$.
   - **Important Rule**: In real numbers, you cannot take the square root of a negative number (such as $\sqrt{-9}$) because multiplying two real numbers with the same sign always produces a positive result.

4. **Perfect Square Trinomials**:
   - An expression of the form $(x + d)^2$ expands to $x^2 + 2dx + d^2$.
   - For example, $(x + 3)^2 = x^2 + 6x + 9$.

5. **Completing the Square**:
   - To make an expression like $x^2 + px$ into a perfect square trinomial, take half of the middle coefficient $p$ (which is $\frac{p}{2}$) and square it to get $\left(\frac{p}{2}\right)^2$. Adding this term creates a square:
     $$x^2 + px + \left(\frac{p}{2}\right)^2 = \left(x + \frac{p}{2}\right)^2$$

---

## 3. Important Definitions

- **Standard Form of a Quadratic Equation**:
  The arrangement where all terms are moved to the left side and set equal to zero:
  $$ax^2 + bx + c = 0 \quad \text{where } a \neq 0$$
  - $a$ is the **quadratic coefficient** (must not be zero).
  - $b$ is the **linear coefficient**.
  - $c$ is the **constant term**.

- **Roots (or Solutions / x-intercepts)**:
  The values of $x$ that satisfy the equation $ax^2 + bx + c = 0$. Geometrically, these correspond to the points where the graph of $y = ax^2 + bx + c$ intersects the horizontal x-axis.

- **Discriminant**:
  The value under the square root in the quadratic formula, written as:
  $$D = b^2 - 4ac$$
  The discriminant tells us how many real solutions the equation has before we even solve it completely.

---

## 4. Main Concepts

### A. The General Quadratic Equation
Every quadratic equation can be written in the standard form $ax^2 + bx + c = 0$. 

Why must $a \neq 0$? If $a = 0$, the $x^2$ term disappears ($0 \cdot x^2 = 0$), leaving $bx + c = 0$, which is a simple linear equation, not a quadratic equation.

### B. Full Step-by-Step Derivation of the Quadratic Formula
Instead of just memorizing the formula, let us derive it from scratch using **completing the square** on the general equation $ax^2 + bx + c = 0$.

1. **Start with the standard form**:
   $$ax^2 + bx + c = 0 \quad (a \neq 0)$$

2. **Divide every term by $a$** so that the coefficient of $x^2$ becomes $1$:
   $$x^2 + \frac{b}{a}x + \frac{c}{a} = 0$$

3. **Move the constant term $\frac{c}{a}$ to the right side**:
   $$x^2 + \frac{b}{a}x = -\frac{c}{a}$$

4. **Complete the square on the left side**:
   - Take half of the coefficient of $x$: $\frac{1}{2} \cdot \frac{b}{a} = \frac{b}{2a}$.
   - Square this term: $\left(\frac{b}{2a}\right)^2 = \frac{b^2}{4a^2}$.
   - Add $\frac{b^2}{4a^2}$ to **both sides** of the equation:
     $$x^2 + \frac{b}{a}x + \frac{b^2}{4a^2} = -\frac{c}{a} + \frac{b^2}{4a^2}$$

5. **Simplify both sides**:
   - The left side is now a perfect square: $\left(x + \frac{b}{2a}\right)^2$.
   - On the right side, find a common denominator ($4a^2$):
     $$-\frac{c}{a} + \frac{b^2}{4a^2} = -\frac{4ac}{4a^2} + \frac{b^2}{4a^2} = \frac{b^2 - 4ac}{4a^2}$$
   - So the equation becomes:
     $$\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}$$

6. **Take the square root of both sides**:
   $$x + \frac{b}{2a} = \pm \sqrt{\frac{b^2 - 4ac}{4a^2}}$$
   Since $\sqrt{4a^2} = 2a$, we can simplify the denominator:
   $$x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}$$

7. **Isolate $x$** by subtracting $\frac{b}{2a}$ from both sides:
   $$x = -\frac{b}{2a} \pm \frac{\sqrt{b^2 - 4ac}}{2a}$$

8. **Combine into a single fraction**:
   $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

This is the **Quadratic Formula**!

---

### C. Understanding the Discriminant ($b^2 - 4ac$)
The part of the formula inside the square root, $b^2 - 4ac$, is called the **Discriminant** ($D$). Because we cannot take the real square root of a negative number, the sign of $D$ determines the number and type of solutions:

1. **If $b^2 - 4ac > 0$ (Positive)**:
   - There are **two distinct real solutions**.
   - The square root gives a positive real number, leading to two different answers ($x_1$ and $x_2$).
   - The parabola crosses the x-axis at two points.

2. **If $b^2 - 4ac = 0$ (Zero)**:
   - There is **one real solution** (also called a repeated root).
   - $\sqrt{0} = 0$, so $x = \frac{-b \pm 0}{2a} = \frac{-b}{2a}$.
   - The vertex of the parabola touches the x-axis at exactly one point.

3. **If $b^2 - 4ac < 0$ (Negative)**:
   - There are **no real solutions**.
   - You cannot take the square root of a negative number using real numbers. (In advanced math, this produces complex/imaginary solutions).
   - The parabola lies completely above or below the x-axis and never crosses it.

---

## 5. Formulas and Rules

### The Quadratic Formula
For any quadratic equation in standard form $ax^2 + bx + c = 0$ (with $a \neq 0$):

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### The Discriminant Formula
$$D = b^2 - 4ac$$

| Value of $D = b^2 - 4ac$ | Number of Real Solutions | Graph Behavior |
| :--- | :--- | :--- |
| $D > 0$ | $2$ Real Solutions | Curve crosses x-axis twice |
| $D = 0$ | $1$ Real Solution | Curve touches x-axis once |
| $D < 0$ | $0$ Real Solutions | Curve does not touch x-axis |

### Workflow to Solve Any Quadratic Equation
1. **Rewrite** the equation into standard form: $ax^2 + bx + c = 0$.
2. **Identify** the values of $a$, $b$, and $c$ (including negative signs!).
3. **Calculate** the discriminant $D = b^2 - 4ac$ first to determine the number of solutions.
4. **Substitute** $a$, $b$, and $c$ into $x = \frac{-b \pm \sqrt{D}}{2a}$.
5. **Simplify** the results to find $x_1$ and $x_2$.

---

## 6. Step-by-Step Examples

### Example 1 (Easy): Standard Form with Integer Solutions
**Problem**: Solve the equation $x^2 - 5x + 6 = 0$.

**Step 1: Identify coefficients**:
- $a = 1$
- $b = -5$
- $c = 6$

**Step 2: Calculate the discriminant**:
$$D = b^2 - 4ac = (-5)^2 - 4(1)(6) = 25 - 24 = 1$$
Since $D = 1 > 0$, there are **two real solutions**.

**Step 3: Apply the Quadratic Formula**:
$$x = \frac{-b \pm \sqrt{D}}{2a} = \frac{-(-5) \pm \sqrt{1}}{2(1)} = \frac{5 \pm 1}{2}$$

**Step 4: Calculate the two values**:
- First solution ($+$):
  $$x_1 = \frac{5 + 1}{2} = \frac{6}{2} = 3$$
- Second solution ($-$):
  $$x_2 = \frac{5 - 1}{2} = \frac{4}{2} = 2$$

**Final Answer**: $x = 3$ or $x = 2$.

---

### Example 2 (Medium): Rearranging Required & Radical Solutions
**Problem**: Solve the equation $2x^2 + 4x = 3$.

**Step 1: Rewrite in standard form**:
Subtract $3$ from both sides to get $2x^2 + 4x - 3 = 0$.

**Step 2: Identify coefficients**:
- $a = 2$
- $b = 4$
- $c = -3$

**Step 3: Calculate the discriminant**:
$$D = b^2 - 4ac = (4)^2 - 4(2)(-3) = 16 - (-24) = 16 + 24 = 40$$
Since $D = 40 > 0$, there are **two real solutions**.

**Step 4: Apply the Quadratic Formula**:
$$x = \frac{-4 \pm \sqrt{40}}{2(2)} = \frac{-4 \pm \sqrt{40}}{4}$$

**Step 5: Simplify the radical $\sqrt{40}$**:
$$\sqrt{40} = \sqrt{4 \times 10} = 2\sqrt{10}$$
Substitute back:
$$x = \frac{-4 \pm 2\sqrt{10}}{4}$$

Factor out $2$ in the numerator and simplify with the denominator:
$$x = \frac{2(-2 \pm \sqrt{10})}{4} = \frac{-2 \pm \sqrt{10}}{2}$$

**Final Answer**:
$$x_1 = \frac{-2 + \sqrt{10}}{2}, \quad x_2 = \frac{-2 - \sqrt{10}}{2}$$

---

### Example 3 (Challenging): Negative Discriminant (No Real Solutions)
**Problem**: Solve the equation $x^2 - 2x + 5 = 0$.

**Step 1: Identify coefficients**:
- $a = 1$
- $b = -2$
- $c = 5$

**Step 2: Calculate the discriminant**:
$$D = b^2 - 4ac = (-2)^2 - 4(1)(5) = 4 - 20 = -16$$

**Step 3: Interpret the result**:
Since $D = -16 < 0$, we cannot take the square root of $-16$ within real numbers ($\sqrt{-16}$ is not a real number).

**Final Answer**: There are **no real solutions** to this equation.

---

## 7. Visual Explanations

### Graphical Meaning of Quadratic Solutions
The solutions to $ax^2 + bx + c = 0$ correspond to the x-intercepts of the curve $y = ax^2 + bx + c$ (a curve called a **parabola**).

Below is a visual concept of how the curve relates to the solutions:

```
        Case 1: D > 0               Case 2: D = 0               Case 3: D < 0
       (2 Real Roots)              (1 Real Root)              (0 Real Roots)

             y                           y                           y
             |   *                       |   *                       |     *
             |  * *                      |  * *                      |    * *
   ----------+--*---*--> x     ----------+---*---> x       ----------+---------*-> x
             | *     *                   |  *   *                    |   *     *
             |                           |                           |
```

- **Case 1 ($D > 0$)**: The curve dips below the x-axis and crosses it at **two distinct points**.
- **Case 2 ($D = 0$)**: The lowest point (vertex) of the curve sits directly **on the x-axis**.
- **Case 3 ($D < 0$)**: The curve sits entirely **above the x-axis** and never touches it.

---

## 8. Common Mistakes

Here are the most frequent mistakes students make when using the Quadratic Formula and how to avoid them:

| Common Mistake | Incorrect Work | Correct Approach | Why it is Wrong |
| :--- | :--- | :--- | :--- |
| **1. Not setting equation to zero** | For $x^2 + 3x = 10$, using $c = 10$. | First rewrite as $x^2 + 3x - 10 = 0$, so $c = -10$. | $c$ must be on the same side as $ax^2 + bx$ so the right side equals $0$. |
| **2. Squaring negative numbers incorrectly** | For $b = -5$, writing $b^2 = -5^2 = -25$. | Write $(-5)^2 = +25$. Use parentheses! | Any real number squared is always positive. |
| **3. Dividing only part of the formula by $2a$** | Writing $x = -b \pm \frac{\sqrt{b^2-4ac}}{2a}$. | Write $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$. | The fraction bar extends under BOTH $-b$ and the square root. |
| **4. Forgetting the minus sign in $-b$** | If $b = -6$, writing $-b = -6$. | Write $-b = -(-6) = +6$. | $-b$ means "the opposite of $b$". If $b$ is negative, $-b$ becomes positive. |
| **5. Forgetting the $\pm$ symbol** | Calculating only $x = \frac{-b + \sqrt{D}}{2a}$. | Keep $\pm$ to calculate both $x_1$ and $x_2$. | Quadratic equations usually have two solutions. |

---

## 9. Practice Problems

Try solving these practice problems on your own before looking at the solutions below!

### Problem 1 (Easy)
Solve for $x$:
$$x^2 - 7x + 10 = 0$$

### Problem 2 (Medium)
Solve for $x$:
$$3x^2 - 6x - 2 = 0$$

### Problem 3 (Challenging)
Solve for $x$:
$$2x^2 + 3x + 5 = 0$$

---

## 10. Solutions

### Solution to Problem 1
**Equation**: $x^2 - 7x + 10 = 0$
- **Coefficients**: $a = 1$, $b = -7$, $c = 10$
- **Discriminant**:
  $$D = (-7)^2 - 4(1)(10) = 49 - 40 = 9$$
- **Apply Formula**:
  $$x = \frac{-(-7) \pm \sqrt{9}}{2(1)} = \frac{7 \pm 3}{2}$$
- **Calculate Solutions**:
  $$x_1 = \frac{7 + 3}{2} = \frac{10}{2} = 5$$
  $$x_2 = \frac{7 - 3}{2} = \frac{4}{2} = 2$$
- **Final Answer**: $x = 5$ or $x = 2$.

---

### Solution to Problem 2
**Equation**: $3x^2 - 6x - 2 = 0$
- **Coefficients**: $a = 3$, $b = -6$, $c = -2$
- **Discriminant**:
  $$D = (-6)^2 - 4(3)(-2) = 36 - (-24) = 36 + 24 = 60$$
- **Apply Formula**:
  $$x = \frac{-(-6) \pm \sqrt{60}}{2(3)} = \frac{6 \pm \sqrt{60}}{6}$$
- **Simplify $\sqrt{60}$**:
  $$\sqrt{60} = \sqrt{4 \times 15} = 2\sqrt{15}$$
  $$x = \frac{6 \pm 2\sqrt{15}}{6} = \frac{2(3 \pm \sqrt{15})}{6} = \frac{3 \pm \sqrt{15}}{3}$$
- **Final Answer**:
  $$x = \frac{3 \pm \sqrt{15}}{3}$$

---

### Solution to Problem 3
**Equation**: $2x^2 + 3x + 5 = 0$
- **Coefficients**: $a = 2$, $b = 3$, $c = 5$
- **Discriminant**:
  $$D = (3)^2 - 4(2)(5) = 9 - 40 = -31$$
- **Interpretation**:
  Since $D = -31 < 0$, the discriminant is negative.
- **Final Answer**: **No real solutions**.

---

## 11. Summary

In this tutorial, we learned how to solve quadratic equations of the form $ax^2 + bx + c = 0$ using the **Quadratic Formula**:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

We derived this formula step by step by taking the general equation $ax^2 + bx + c = 0$ and applying the method of **completing the square**. 

We also learned about the **Discriminant** ($D = b^2 - 4ac$), which acts as a quick shortcut to discover how many real solutions an equation has before solving it completely:
- If $D > 0$, there are **2 real solutions**.
- If $D = 0$, there is **1 real solution**.
- If $D < 0$, there are **no real solutions**.

---

## 12. Key Things to Remember

1. **Standard Form First**: Always move all terms to one side so the equation equals zero ($ax^2 + bx + c = 0$) before identifying $a$, $b$, and $c$.
2. **Watch the Signs**: Keep negative signs attached to their numbers. When calculating $b^2$, always put negative values in parentheses: $(-b)^2$.
3. **Check the Discriminant ($b^2 - 4ac$)**:
   - Positive $D \implies 2$ real answers
   - Zero $D \implies 1$ real answer
   - Negative $D \implies 0$ real answers
4. **Divide Everything by $2a$**: Make sure the fraction bar goes under both $-b$ and $\sqrt{b^2 - 4ac}$.
5. **The $\pm$ Sign**: Remember to calculate both solutions ($+$ and $-$).
