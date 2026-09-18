# Solving Quadratic Equations by Factoring

### 1. Introduction

A **quadratic equation** is a special kind of algebra equation where the highest exponent of the variable $x$ is $2$ (written as $x^2$). In real life, quadratic equations help describe many natural events, such as the path of a thrown ball, the shape of a satellite dish, or profit calculations in business.

Solving a quadratic equation means finding the specific value or values of $x$ that make the equation true ($0 = 0$). One of the fastest and most elegant ways to solve these equations is by **factoring**. Factoring transforms a complex quadratic expression into a simple product of two smaller expressions called **binomials**. Once an equation is in factored form, finding the solutions becomes very easy.

---

### 2. Prerequisite Knowledge

Before learning how to factor quadratic equations, it is important to review two basic mathematical ideas: the **FOIL method** and **integer factor pairs**.

#### A. The FOIL Method (Multiplying Binomials)
A **binomial** is a mathematical expression with two terms added or subtracted together, such as $(x + 3)$ or $(x - 5)$. 

When we multiply two binomials together, we use the **FOIL** acronym to remember the order of multiplication:
*   **F**irst: Multiply the first terms in each bracket.
*   **O**utside: Multiply the outer terms.
*   **I**nside: Multiply the inner terms.
*   **L**ast: Multiply the last terms in each bracket.

##### FOIL Example:
Multiply $(x + 5)(x + 2)$:
1.  **First**: $x \cdot x = x^2$
2.  **Outside**: $x \cdot 2 = 2x$
3.  **Inside**: $5 \cdot x = 5x$
4.  **Last**: $5 \cdot 2 = 10$

Now combine all the terms:
$$x^2 + 2x + 5x + 10$$

Combine the like terms ($2x + 5x = 7x$):
$$x^2 + 7x + 10$$

> **Key Insight:** Factoring is simply running the FOIL method in **reverse**. We start with $x^2 + 7x + 10$ and work backward to find $(x + 5)(x + 2)$.

#### B. Integer Factor Pairs and Signs
Factors are numbers that multiply together to produce a target product.
*   If the product is **positive** ($+10$), both factors must have the **same sign**:
    *   Both positive: $(+5) \cdot (+2) = +10$
    *   Both negative: $(-5) \cdot (-2) = +10$
*   If the product is **negative** ($-20$), the factors must have **opposite signs**:
    *   One positive and one negative: $(+10) \cdot (-2) = -20$ or $(-10) \cdot (+2) = -20$

---

### 3. Important Definitions

*   **Quadratic Equation**: An equation of degree $2$, which means the highest power of the variable is $x^2$.
*   **Standard Form**: A quadratic equation written as $ax^2 + bx + c = 0$, where $a$, $b$, and $c$ are constant numbers (integers), and $a \neq 0$.
    *   $a$ is the **coefficient** of $x^2$.
    *   $b$ is the **coefficient** of $x$.
    *   $c$ is the **constant term** (a number without a variable).
*   **Binomial**: An algebraic expression containing exactly two terms, such as $(x + 2)$ or $(3x - 1)$.
*   **Factoring**: Breaking down an expression into smaller multiplicative parts (factors) so that when multiplied together, they equal the original expression.
*   **Zero Product Property**: A fundamental property of arithmetic stating that if the product of two numbers or expressions is zero ($A \cdot B = 0$), then at least one of the expressions must equal zero ($A = 0$ or $B = 0$).
*   **Roots / Solutions / Zeros**: The specific numerical values of $x$ that make the quadratic equation equal to $0$.

---

### 4. Main Concepts

#### Concept 1: The Principle of Factoring
When a quadratic equation is written in standard form $ax^2 + bx + c = 0$, our goal is to rewrite the left side as a product of two binomials:
$$(px + q)(rx + s) = 0$$

When we expand $(x + m)(x + n)$ using FOIL, we get:
$$(x + m)(x + n) = x^2 + (m + n)x + (m \cdot n)$$

Comparing this to $x^2 + bx + c$:
1.  The constant term $c$ is equal to the **product** of the two numbers: $m \cdot n = c$.
2.  The middle coefficient $b$ is equal to the **sum** of the two numbers: $m + n = b$.

Therefore, factoring a simple quadratic ($a = 1$) requires finding two numbers ($m$ and $n$) that:
*   **Multiply** to give $c$
*   **Add** to give $b$

#### Concept 2: The Zero Product Property
Why do we factor? Factoring turns addition and subtraction into multiplication. 

If $A \cdot B = 0$, there are only two possibilities:
1.  $A = 0$
2.  $B = 0$

If $(x + 5)(x + 2) = 0$, then either:
*   $x + 5 = 0 \implies x = -5$
*   $x + 2 = 0 \implies x = -2$

If $x = -5$, the first bracket becomes $0$, making the entire product $0 \cdot (-3) = 0$.
If $x = -2$, the second bracket becomes $0$, making the entire product $3 \cdot 0 = 0$.

Thus, $x = -5$ and $x = -2$ are the two valid solutions to the equation.

---

### 5. Formulas and Rules

#### Standard Form of a Quadratic Equation
$$ax^2 + bx + c = 0$$

#### The Zero Product Property Rule
$$\text{If } A \cdot B = 0, \text{ then } A = 0 \quad \text{or} \quad B = 0$$

#### Rule for Case 1: Simple Quadratic ($a = 1$)
For an equation $x^2 + bx + c = 0$:
1.  Find two numbers $m$ and $n$ such that:
    $$m \cdot n = c \quad \text{and} \quad m + n = b$$
2.  Write the factored form:
    $$(x + m)(x + n) = 0$$
3.  Set each factor to zero and solve for $x$:
    $$x + m = 0 \implies x = -m$$
    $$x + n = 0 \implies x = -n$$

#### Rule for Case 2: Non-Simple Quadratic ($a \neq 1$)
For an equation $ax^2 + bx + c = 0$:
1.  Set up binomial brackets where the first terms multiply to $ax^2$:
    $$(px + \underline{\quad})(rx + \underline{\quad}) = 0 \quad \text{where } p \cdot r = a$$
2.  Find factors of $c$ that, when multiplied across the outer and inner terms of FOIL, add up to $b$.
3.  Solve each linear equation for $x$.

---

### 6. Step-by-Step Examples

#### Example 1 (Easy): Positive Terms ($a = 1$)
**Problem:** Solve $x^2 + 7x + 10 = 0$ for $x$.

*   **Step 1: Identify $a$, $b$, and $c$.**
    Here $a = 1$, $b = 7$, and $c = 10$.

*   **Step 2: List factor pairs of $c = 10$.**
    We need two numbers that multiply to $+10$:
    *   $+1 \cdot +10 = 10$
    *   $-1 \cdot -10 = 10$
    *   $+2 \cdot +5 = 10$
    *   $-2 \cdot -5 = 10$

*   **Step 3: Choose the pair that adds to $b = 7$.**
    *   $1 + 10 = 11$ (Incorrect)
    *   $2 + 5 = 7$ (Correct!)

*   **Step 4: Write in factored form.**
    $$(x + 5)(x + 2) = 0$$

*   **Step 5: Apply the Zero Product Property.**
    Set each binomial equal to $0$:
    $$x + 5 = 0 \implies x = -5$$
    $$x + 2 = 0 \implies x = -2$$

*   **Step 6: Verify the solutions by substitution.**
    *   Test $x = -5$:
        $$(-5)^2 + 7(-5) + 10 = 25 - 35 + 10 = 0 \quad \checkmark$$
    *   Test $x = -2$:
        $$(-2)^2 + 7(-2) + 10 = 4 - 14 + 10 = 0 \quad \checkmark$$

---

#### Example 2 (Medium): Negative Terms ($a = 1$)
**Problem:** Solve $x^2 - 8x - 20 = 0$ for $x$.

*   **Step 1: Identify $a$, $b$, and $c$.**
    Here $a = 1$, $b = -8$, and $c = -20$.

*   **Step 2: List factor pairs of $c = -20$.**
    Since $c$ is negative, one factor must be positive and one negative:
    *   $+1 \cdot -20$ or $-1 \cdot +20$
    *   $+2 \cdot -10$ or $-2 \cdot +10$
    *   $+4 \cdot -5$ or $-4 \cdot +5$

*   **Step 3: Choose the pair that adds to $b = -8$.**
    *   $1 + (-20) = -19$
    *   $2 + (-10) = -8$ (Correct!)

*   **Step 4: Write in factored form.**
    $$(x - 10)(x + 2) = 0$$

*   **Step 5: Solve for $x$.**
    $$x - 10 = 0 \implies x = 10$$
    $$x + 2 = 0 \implies x = -2$$

*   **Step 6: Verify the solutions.**
    *   Test $x = 10$:
        $$(10)^2 - 8(10) - 20 = 100 - 80 - 20 = 0 \quad \checkmark$$
    *   Test $x = -2$:
        $$(-2)^2 - 8(-2) - 20 = 4 + 16 - 20 = 0 \quad \checkmark$$

---

#### Example 3 (Challenging): Leading Coefficient $a > 1$
**Problem:** Solve $3x^2 + 5x - 2 = 0$ for $x$.

*   **Step 1: Set up the template for binomials.**
    Because $a = 3$ (a prime number), the first terms must be $3x$ and $x$:
    $$(3x + \underline{\quad})(x + \underline{\quad}) = 0$$

*   **Step 2: Find factor pairs for $c = -2$.**
    The pairs for $-2$ are:
    *   $+1$ and $-2$
    *   $-1$ and $+2$

*   **Step 3: Test placement of factors.**
    Remember that the factor placed in the second bracket will be multiplied by $3x$ during the **Outside** step of FOIL!
    *   *Trial 1:* Try $(3x + 1)(x - 2)$.
        Outside + Inside: $3x(-2) + 1(x) = -6x + x = -5x$ (Close, but wrong sign).
    *   *Trial 2:* Try $(3x - 1)(x + 2)$.
        Outside + Inside: $3x(+2) + (-1)(x) = +6x - x = +5x$ (Correct!)

*   **Step 4: Write the correct factored form.**
    $$(3x - 1)(x + 2) = 0$$

*   **Step 5: Solve each equation for $x$.**
    *   First factor:
        $$3x - 1 = 0 \implies 3x = 1 \implies x = \frac{1}{3}$$
    *   Second factor:
        $$x + 2 = 0 \implies x = -2$$

*   **Step 6: Verify the solutions.**
    *   Test $x = \frac{1}{3}$:
        $$3\left(\frac{1}{3}\right)^2 + 5\left(\frac{1}{3}\right) - 2 = 3\left(\frac{1}{9}\right) + \frac{5}{3} - 2 = \frac{1}{3} + \frac{5}{3} - 2 = \frac{6}{3} - 2 = 0 \quad \checkmark$$
    *   Test $x = -2$:
        $$3(-2)^2 + 5(-2) - 2 = 3(4) - 10 - 2 = 12 - 10 - 2 = 0 \quad \checkmark$$

---

### 7. Visual Explanations

#### Summary Table: How Signs in $ax^2 + bx + c = 0$ Determine Factor Signs

| Quadratic Sign Pattern | Sign of $c$ | Sign of $b$ | Factor Signs | Example Factored Form |
| :--- | :--- | :--- | :--- | :--- |
| $x^2 + bx + c = 0$ | Positive ($+$) | Positive ($+$) | Both Positive $(+)(+)$ | $(x + 5)(x + 2)$ |
| $x^2 - bx + c = 0$ | Positive ($+$) | Negative ($-$) | Both Negative $(-)(-)$ | $(x - 5)(x - 2)$ |
| $x^2 + bx - c = 0$ | Negative ($-$) | Positive ($+$) | Mixed $(+)$ and $(-)$, larger factor is $(+)$ | $(x + 10)(x - 2)$ |
| $x^2 - bx - c = 0$ | Negative ($-$) | Negative ($-$) | Mixed $(+)$ and $(-)$, larger factor is $(-)$ | $(x - 10)(x + 2)$ |

#### Process Flowchart for Factoring $x^2 + bx + c = 0$

```
                     +---------------------------------------+
                     |  Write equation in Standard Form:    |
                     |          ax^2 + bx + c = 0            |
                     +---------------------------------------+
                                         |
                                         v
                     +---------------------------------------+
                     |    List all factor pairs of 'c'       |
                     |       (Consider positive & negative)  |
                     +---------------------------------------+
                                         |
                                         v
                     +---------------------------------------+
                     | Find the factor pair (m, n) that adds |
                     |          to give coefficient 'b'      |
                     +---------------------------------------+
                                         |
                                         v
                     +---------------------------------------+
                     |      Write factored expression:       |
                     |           (x + m)(x + n) = 0          |
                     +---------------------------------------+
                                         |
                                         v
                     +---------------------------------------+
                     | Apply Zero Product Property:          |
                     |    x + m = 0   -->   x = -m           |
                     |    x + n = 0   -->   x = -n           |
                     +---------------------------------------+
```

---

### 8. Common Mistakes

#### Mistake 1: Forgetting to put the equation into Standard Form first
*   **Incorrect Approach:** Trying to factor $x^2 + 7x = -10$ directly by writing $x(x + 7) = -10$, then setting $x = -10$ or $x + 7 = -10$.
*   **Why it is wrong:** The Zero Product Property ONLY works when the equation equals **zero** ($0$). $A \cdot B = -10$ has infinitely many solutions (e.g., $2 \cdot (-5)$, $1 \cdot (-10)$, $0.5 \cdot (-20)$), so you cannot conclude $A = -10$ or $B = -10$.
*   **How to avoid:** Always move all terms to one side so the right side is $0$ before factoring:
    $$x^2 + 7x + 10 = 0$$

#### Mistake 2: Mixing up the signs of the final solutions
*   **Incorrect Approach:** Factoring $x^2 + 7x + 10 = 0$ into $(x + 5)(x + 2) = 0$ and concluding that the solutions are $x = 5$ and $x = 2$.
*   **Why it is wrong:** The factors are $(x + 5)$ and $(x + 2)$, but solving $x + 5 = 0$ yields $x = -5$, not $+5$.
*   **How to avoid:** Always write out the intermediate step $x + m = 0$ explicitly before stating the final answer.

#### Mistake 3: Stopping at the factored form
*   **Incorrect Approach:** Writing $(x + 5)(x + 2)$ as the final answer when asked to **solve** the equation.
*   **Why it is wrong:** Factoring is a step in the process, not the final solution. The prompt asks to solve for $x$, so you must give the actual values of $x$.
*   **How to avoid:** Make sure your final answer is written as $x = \text{number}$.

---

### 9. Practice Problems

Try solving these problems on your own before looking at the solutions below!

1.  **Problem 1 (Easy):** Solve $x^2 + 6x + 8 = 0$ for $x$.
2.  **Problem 2 (Medium):** Solve $x^2 - 3x - 18 = 0$ for $x$.
3.  **Problem 3 (Challenging):** Solve $2x^2 + 7x + 3 = 0$ for $x$.

---

### 10. Solutions

#### Solution to Problem 1: $x^2 + 6x + 8 = 0$
1.  **Identify $b$ and $c$:** $b = 6$ and $c = 8$.
2.  **Find factors of $8$ that add to $6$:**
    *   $1 \cdot 8 = 8 \implies 1 + 8 = 9$
    *   $2 \cdot 4 = 8 \implies 2 + 4 = 6$ (Correct pair: $2$ and $4$)
3.  **Factored Form:**
    $$(x + 4)(x + 2) = 0$$
4.  **Solve for $x$:**
    *   $x + 4 = 0 \implies x = -4$
    *   $x + 2 = 0 \implies x = -2$
5.  **Final Answer:** $x = -4$ and $x = -2$.

---

#### Solution to Problem 2: $x^2 - 3x - 18 = 0$
1.  **Identify $b$ and $c$:** $b = -3$ and $c = -18$.
2.  **Find factors of $-18$ that add to $-3$:**
    *   $+1 \cdot -18 \implies 1 - 18 = -17$
    *   $+2 \cdot -9 \implies 2 - 9 = -7$
    *   $+3 \cdot -6 \implies 3 - 6 = -3$ (Correct pair: $+3$ and $-6$)
3.  **Factored Form:**
    $$(x - 6)(x + 3) = 0$$
4.  **Solve for $x$:**
    *   $x - 6 = 0 \implies x = 6$
    *   $x + 3 = 0 \implies x = -3$
5.  **Final Answer:** $x = 6$ and $x = -3$.

---

#### Solution to Problem 3: $2x^2 + 7x + 3 = 0$
1.  **Set up binomial structure:**
    Since $a = 2$, the first terms must be $2x$ and $x$:
    $$(2x + \underline{\quad})(x + \underline{\quad}) = 0$$
2.  **Factors of $c = 3$:** $1$ and $3$.
3.  **Test placement:**
    We need an inner + outer sum of $+7x$.
    If we place $+3$ in the second bracket, it multiplies by $2x$ to give $6x$:
    $$(2x + 1)(x + 3) = 2x^2 + 6x + 1x + 3 = 2x^2 + 7x + 3 \quad \checkmark$$
4.  **Solve for $x$:**
    *   $2x + 1 = 0 \implies 2x = -1 \implies x = -\frac{1}{2}$
    *   $x + 3 = 0 \implies x = -3$
5.  **Final Answer:** $x = -\frac{1}{2}$ and $x = -3$.

---

### 11. Summary

Factoring is a powerful algebraic method for solving quadratic equations of the form $ax^2 + bx + c = 0$. By transforming a quadratic expression into a product of two linear binomials $(px + q)(rx + s) = 0$, we can leverage the **Zero Product Property** to break one complex degree-2 equation into two simple degree-1 equations. Always ensure the equation equals zero before factoring, list integer factor pairs systematically, check your signs carefully, and verify your solutions by substituting them back into the original equation.

---

### 12. Key Things to Remember

*   **Standard Form First:** Always rewrite the quadratic equation as $ax^2 + bx + c = 0$ before trying to factor.
*   **Reverse FOIL:** Factoring is undoing FOIL multiplication.
*   **The Two Numbers Rule (when $a=1$):** Find two numbers that **multiply** to $c$ and **add** to $b$.
*   **Zero Product Property:** If $(x - m)(x - n) = 0$, then $x - m = 0$ or $x - n = 0$.
*   **Watch the Signs:** If factor is $(x + m)$, the solution for $x$ is $-m$.
*   **Always Check:** Plug your calculated solutions back into the original equation to ensure they result in $0$.
