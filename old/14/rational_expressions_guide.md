# Manipulating Rational Expressions: Simplification and Operations
*A Complete, Beginner-Friendly Mathematical Manual*

---

## 1. Introduction

In algebra, a **rational expression** is simply a fraction where the top part (numerator) and the bottom part (denominator) are algebraic expressions called **polynomials**. 

Just as regular arithmetic requires working with numeric fractions like $\frac{1}{2}$ or $\frac{3}{4}$, algebra requires manipulating rational expressions such as:

$$\frac{x^2 - 1}{x^2 + 2x + 1} \quad \text{or} \quad \frac{x + 3}{x - 4}$$

### Why Are Rational Expressions Important?
Understanding how to simplify, multiply, divide, add, subtract, and rationalize these expressions is an essential algebraic skill. You will use these techniques to:
1. **Analyze Functions**: Graph complex functions and find where graphs have holes or vertical boundary lines (called *asymptotes*).
2. **Solve Equations**: Solve real-world formulas in physics, engineering, economics, and chemistry (such as work-rate problems and distance-time problems).
3. **Prepare for Advanced Math**: Succeed in higher-level topics, including Calculus, where manipulating fractions is required before applying calculus operations.

This manual provides a step-by-step guide to mastering rational expressions. Every concept is broken down assuming beginner-level background knowledge, using simple language and clear mathematical steps.

---

## 2. Prerequisite Knowledge

Before working with rational expressions, let us review four foundational topics: numeric fractions, polynomial factoring, the distributive property (FOIL), and basic square root rules.

### 2.1 Basic Fraction Rules
A fraction represents a division of two quantities: $\frac{\text{Numerator}}{\text{Denominator}}$.

* **Multiplication**: Multiply straight across (numerator by numerator, denominator by denominator).
  $$\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$$
* **Division**: Keep the first fraction, change division to multiplication, and flip the second fraction (this flipped fraction is called the **reciprocal**).
  $$\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c} = \frac{a \cdot d}{b \cdot c}$$
* **Addition and Subtraction**: You **cannot** add or subtract fractions unless they have the same denominator.
  $$\frac{1}{3} + \frac{1}{4}$$
  To add these, find the **Least Common Denominator (LCD)**, which is $12$:
  $$\frac{1 \cdot 4}{3 \cdot 4} + \frac{1 \cdot 3}{4 \cdot 3} = \frac{4}{12} + \frac{3}{12} = \frac{4 + 3}{12} = \frac{7}{12}$$

### 2.2 Polynomial Factoring Techniques
Factoring means rewriting an expression as a product of simpler expressions multiplied together.

1. **Greatest Common Factor (GCF)**: Look for terms shared by all parts of the expression.
   * *Example*: In $x^3 + x^2$, both terms share $x^2$. Factoring out $x^2$ gives:
     $$x^3 + x^2 = x^2(x + 1)$$
2. **Difference of Squares**: An expression in the form $a^2 - b^2$ always factors into $(a - b)(a + b)$.
   * *Example*: Factor $x^2 - 1$. Notice $1 = 1^2$, so:
     $$x^2 - 1 = (x - 1)(x + 1)$$
   * *Intuition*: Think of $x^2 - 1$ as $x^2 + 0x - 1$. You look for two numbers that multiply to give $-1$ and add up to $0$. Those numbers are $+1$ and $-1$.
3. **Factoring Trinomials ($x^2 + bx + c$)**: To factor a three-term polynomial into $(x + p)(x + q)$, find two numbers $p$ and $q$ that:
   * Multiply to equal the last number ($c$).
   * Add up to equal the middle coefficient ($b$).
   * *Example 1*: Factor $x^2 + 2x + 1$.
     * Find two numbers that multiply to $+1$ and add to $+2$. The numbers are $+1$ and $+1$.
     * $$x^2 + 2x + 1 = (x + 1)(x + 1) = (x + 1)^2$$
   * *Example 2*: Factor $x^2 + 4x - 5$.
     * Find two numbers that multiply to $-5$ and add to $+4$. The numbers are $+5$ and $-1$.
     * $$x^2 + 4x - 5 = (x + 5)(x - 1)$$

### 2.3 Distributive Property and FOIL
When multiplying two binomials $(a + b)(c + d)$, multiply every term in the first parentheses by every term in the second:

$$\text{FOIL}: \quad (a + b)(c + d) = \underbrace{ac}_{\text{First}} + \underbrace{ad}_{\text{Outer}} + \underbrace{bc}_{\text{Inner}} + \underbrace{bd}_{\text{Last}}$$

* *Example*: Multiply $(x + 2)(x + 5)$:
  $$(x + 2)(x + 5) = x \cdot x + x \cdot 5 + 2 \cdot x + 2 \cdot 5 = x^2 + 5x + 2x + 10 = x^2 + 7x + 10$$

### 2.4 Square Roots (Radicals) and Exponents
A square root $\sqrt{a}$ represents a number that, when multiplied by itself, equals $a$.
* In exponent notation: $\sqrt{a} = a^{1/2}$.
* Multiplying a square root by itself removes the root symbol:
  $$\sqrt{a} \cdot \sqrt{a} = a^{1/2} \cdot a^{1/2} = a^{1/2 + 1/2} = a^1 = a$$
* *Example*: $\sqrt{2} \cdot \sqrt{2} = 2$.

---

## 3. Important Definitions

* **Rational Expression**: An algebraic expression written as a fraction $\frac{P(x)}{Q(x)}$, where $P(x)$ and $Q(x)$ are polynomials and $Q(x) \neq 0$.
* **Polynomial**: An expression composed of variables and coefficients using addition, subtraction, and non-negative integer exponents (e.g., $3x^2 - 4x + 7$).
* **Numerator**: The top expression in a fraction.
* **Denominator**: The bottom expression in a fraction. (Note: A denominator can **never** equal zero, because division by zero is undefined).
* **Domain Restriction**: Excluded values of the variable $x$ that would make the denominator equal to zero.
* **Reciprocal**: The inverted form of a fraction. The reciprocal of $\frac{A}{B}$ is $\frac{B}{A}$.
* **Least Common Denominator (LCD)**: The simplest polynomial expression that is evenly divisible by all denominators in an addition or subtraction problem.
* **Complex Rational Expression**: A fraction that contains smaller fractions inside its numerator, denominator, or both.
* **Radical**: An expression containing a root symbol ($\sqrt{\phantom{x}}$).
* **Conjugate**: A two-term expression formed by changing the sign between the terms. The conjugate of $a + \sqrt{b}$ is $a - \sqrt{b}$.

---

## 4. Main Concepts

### 4.1 Simplifying Rational Expressions

#### What It Means
Simplifying a rational expression means reducing it to its simplest form so that the numerator and denominator share no common polynomial factors other than $1$.

#### Why It Works
According to the fundamental property of fractions:

$$\frac{A \cdot C}{B \cdot C} = \frac{A}{B} \quad (\text{where } B \neq 0 \text{ and } C \neq 0)$$

Because $\frac{C}{C} = 1$, multiplying or dividing the top and bottom by the same non-zero factor $C$ does not change the value of the expression.

#### Step-by-Step Procedure
1. **Factor** the numerator completely.
2. **Factor** the denominator completely.
3. **Cancel out** any identical factors present in both the top and bottom.
4. **Write** the simplified remaining expression.

> ⚠️ **Crucial Rule**: You can **only cancel factors** (expressions that are *multiplied*), **NEVER terms** (expressions that are *added or subtracted*).

---

### 4.2 Multiplying Rational Expressions

#### What It Means
Multiplying two rational expressions means combining two fractions into a single product.

#### Step-by-Step Procedure
1. **Factor** all numerators and denominators completely.
2. **Cancel** common factors that appear in *any* numerator and *any* denominator.
3. **Multiply** the remaining factors in the numerators together, and the remaining factors in the denominators together.

---

### 4.3 Dividing Rational Expressions

#### What It Means
Dividing by a fraction is equivalent to multiplying by its reciprocal.

#### Why It Works
Division asks: "How many times does the divisor fit into the dividend?" In fraction arithmetic:

$$\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \cdot \frac{D}{C}$$

#### Step-by-Step Procedure
1. **Change** the division symbol ($\div$) to a multiplication symbol ($\cdot$).
2. **Flip** the second fraction upside down to get its reciprocal ($\frac{C}{D} \rightarrow \frac{D}{C}$).
3. **Factor** all numerators and denominators completely.
4. **Cancel** common factors between top and bottom.
5. **Multiply** the remaining expressions.

---

### 4.4 Adding and Subtracting Rational Expressions

#### What It Means
Combining two or more rational expressions into a single fraction using addition or subtraction.

#### Why It Works
You can only combine quantities that represent parts of the same whole size. This requires a **Least Common Denominator (LCD)**.

#### Step-by-Step Procedure
1. **Factor** all denominators to identify all unique factors.
2. **Determine the LCD**, which is the product of every unique factor present across the denominators.
3. **Rewrite** each fraction by multiplying its top and bottom by whatever factor is missing to match the LCD.
4. **FOIL/Expand** the numerators.
5. **Combine like terms** in the numerator.
   * *Warning for Subtraction*: Be sure to distribute the minus sign to **every term** in the second numerator!
6. **Keep** the common denominator unchanged.
7. **Simplify** the final result if the new numerator can be factored.

---

### 4.5 Complex Rational Expressions

#### What It Means
A complex rational expression is a "fraction inside a fraction", such as:

$$\frac{1 + \frac{1}{x}}{1 - \frac{1}{x}}$$

#### How to Solve
* **Method 1 (Single Fraction Method)**:
  1. Simplify the top numerator into one single fraction.
  2. Simplify the bottom denominator into one single fraction.
  3. Divide the top fraction by the bottom fraction (flip and multiply).

---

### 4.6 Rationalizing Denominators

#### What It Means
Rationalizing means removing square roots or radicals from the denominator of a fraction. Mathematically, having radicals in the denominator is considered unsimplified.

#### Technique 1: Single Radical Denominator ($\frac{1}{\sqrt{a}}$)
Multiply both the top and bottom by $\sqrt{a}$:

$$\frac{1}{\sqrt{a}} \cdot \frac{\sqrt{a}}{\sqrt{a}} = \frac{\sqrt{a}}{a}$$

#### Technique 2: Binomial Radical Denominator ($\frac{1}{a - \sqrt{b}}$)
Multiply top and bottom by the **conjugate** $(a + \sqrt{b})$:

$$\frac{1}{a - \sqrt{b}} \cdot \frac{a + \sqrt{b}}{a + \sqrt{b}} = \frac{a + \sqrt{b}}{(a)^2 - (\sqrt{b})^2} = \frac{a + \sqrt{b}}{a^2 - b}$$

#### Why the Conjugate Works
The difference of squares formula $(x - y)(x + y) = x^2 - y^2$ squares both terms individually. Squaring a square root removes the root symbol completely!

---

## 5. Formulas and Rules

Here is a quick-reference table of the key algebraic rules used when working with rational expressions:

| Rule / Operation | Formula / Property | Condition / Notes |
| :--- | :--- | :--- |
| **Fundamental Cancellation Property** | $\frac{A \cdot C}{B \cdot C} = \frac{A}{B}$ | $B \neq 0, C \neq 0$ (Only cancel factors) |
| **Multiplication Rule** | $\frac{A}{B} \cdot \frac{C}{D} = \frac{A \cdot C}{B \cdot D}$ | $B \neq 0, D \neq 0$ |
| **Division Rule** | $\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \cdot \frac{D}{C} = \frac{A \cdot D}{B \cdot C}$ | $B, C, D \neq 0$ (Multiply by reciprocal) |
| **Addition (Same Denominator)** | $\frac{A}{C} + \frac{B}{C} = \frac{A + B}{C}$ | $C \neq 0$ |
| **Subtraction (Same Denominator)** | $\frac{A}{C} - \frac{B}{C} = \frac{A - B}{C}$ | $C \neq 0$ (Distribute negative sign!) |
| **Difference of Squares Factoring** | $a^2 - b^2 = (a - b)(a + b)$ | Essential for quadratic expressions |
| **Square Root Product** | $\sqrt{a} \cdot \sqrt{a} = a$ | $a \ge 0$ |
| **Conjugate Identity** | $(a - \sqrt{b})(a + \sqrt{b}) = a^2 - b$ | Eliminates radical from denominator |

---

## 6. Step-by-Step Examples

### Example 1: Simplifying a GCF Rational Expression (Easy)
**Problem**: Simplify $\frac{x^3 + x^2}{x + 1}$.

* **Step 1: Factor the numerator**.
  In $x^3 + x^2$, both terms contain $x^2$. Factor out $x^2$:
  $$x^3 + x^2 = x^2(x + 1)$$
* **Step 2: Rewrite the expression**.
  $$\frac{x^2(x + 1)}{x + 1}$$
* **Step 3: Cancel common factors**.
  The factor $(x + 1)$ appears in both numerator and denominator. Cancel it out:
  $$\frac{x^2 \mathbf{\cancel{(x + 1)}}}{\mathbf{\cancel{x + 1}}} = x^2$$
* **Final Answer**: $x^2$ (where $x \neq -1$).

---

### Example 2: Simplifying a Quadratic Rational Expression (Medium)
**Problem**: Simplify $\frac{x^2 - 1}{x^2 + 2x + 1}$.

* **Step 1: Factor the numerator**.
  $x^2 - 1$ is a difference of squares ($x^2 - 1^2$):
  $$x^2 - 1 = (x + 1)(x - 1)$$
* **Step 2: Factor the denominator**.
  $x^2 + 2x + 1$ is a perfect square trinomial (find numbers multiplying to $+1$ and adding to $+2$):
  $$x^2 + 2x + 1 = (x + 1)(x + 1)$$
* **Step 3: Substitute the factored forms**.
  $$\frac{(x + 1)(x - 1)}{(x + 1)(x + 1)}$$
* **Step 4: Cancel one common $(x + 1)$ factor from top and bottom**.
  $$\frac{\mathbf{\cancel{(x + 1)}}(x - 1)}{\mathbf{\cancel{(x + 1)}}(x + 1)} = \frac{x - 1}{x + 1}$$
* **Final Answer**: $\frac{x - 1}{x + 1}$ (where $x \neq -1$).

---

### Example 3: Multiplying Rational Expressions (Medium)
**Problem**: Multiply $\frac{x + 2}{x - 1} \cdot \frac{x^2 + 4x - 5}{x + 3}$.

* **Step 1: Factor all polynomials**.
  * $\frac{x + 2}{x - 1}$ is already fully factored.
  * In the numerator $x^2 + 4x - 5$, find numbers multiplying to $-5$ and adding to $+4$: $+5$ and $-1$.
    $$x^2 + 4x - 5 = (x - 1)(x + 5)$$
* **Step 2: Rewrite the multiplication problem**.
  $$\frac{x + 2}{x - 1} \cdot \frac{(x - 1)(x + 5)}{x + 3}$$
* **Step 3: Combine into a single fraction and cancel common factors**.
  Cancel $(x - 1)$ from numerator and denominator:
  $$\frac{(x + 2)\mathbf{\cancel{(x - 1)}}(x + 5)}{\mathbf{\cancel{(x - 1)}}(x + 3)} = \frac{(x + 2)(x + 5)}{x + 3}$$
* **Step 4: Expand the numerator (optional/standard)**.
  Use FOIL: $(x + 2)(x + 5) = x^2 + 5x + 2x + 10 = x^2 + 7x + 10$.
* **Final Answer**: $\frac{x^2 + 7x + 10}{x + 3}$ or $\frac{(x + 2)(x + 5)}{x + 3}$.

---

### Example 4: Dividing Rational Expressions (Challenging)
**Problem**: Divide $\frac{x + 3}{x - 4} \div \frac{x^2 + x - 6}{x^2 - 3x - 4}$.

* **Step 1: Convert division to multiplication by flipping the second fraction**.
  $$\frac{x + 3}{x - 4} \cdot \frac{x^2 - 3x - 4}{x^2 + x - 6}$$
* **Step 2: Factor all quadratic expressions**.
  * Top right: $x^2 - 3x - 4 \rightarrow$ numbers multiplying to $-4$ and adding to $-3$ are $-4$ and $+1$:
    $$x^2 - 3x - 4 = (x - 4)(x + 1)$$
  * Bottom right: $x^2 + x - 6 \rightarrow$ numbers multiplying to $-6$ and adding to $+1$ are $+3$ and $-2$:
    $$x^2 + x - 6 = (x + 3)(x - 2)$$
* **Step 3: Substitute factored forms**.
  $$\frac{x + 3}{x - 4} \cdot \frac{(x - 4)(x + 1)}{(x + 3)(x - 2)}$$
* **Step 4: Cancel common factors**.
  Cancel $(x + 3)$ and $(x - 4)$:
  $$\frac{\mathbf{\cancel{(x + 3)}}}{\mathbf{\cancel{(x - 4)}}} \cdot \frac{\mathbf{\cancel{(x - 4)}}(x + 1)}{\mathbf{\cancel{(x + 3)}}(x - 2)} = \frac{x + 1}{x - 2}$$
* **Final Answer**: $\frac{x + 1}{x - 2}$.

---

### Example 5: Adding Rational Expressions with Different Denominators (Challenging)
**Problem**: Add $\frac{x + 1}{x - 1} + \frac{x + 2}{x + 3}$.

* **Step 1: Find the Least Common Denominator (LCD)**.
  The denominators $(x - 1)$ and $(x + 3)$ have no common factors. The LCD is their product:
  $$\text{LCD} = (x - 1)(x + 3)$$
* **Step 2: Convert fractions to have the LCD**.
  Multiply top and bottom of each fraction by the missing factor:
  $$\frac{(x + 1)(x + 3)}{(x - 1)(x + 3)} + \frac{(x + 2)(x - 1)}{(x + 3)(x - 1)}$$
* **Step 3: FOIL the numerators**.
  * First numerator: $(x + 1)(x + 3) = x^2 + 3x + x + 3 = x^2 + 4x + 3$
  * Second numerator: $(x + 2)(x - 1) = x^2 - x + 2x - 2 = x^2 + x - 2$
* **Step 4: Combine numerators over the LCD**.
  $$\frac{(x^2 + 4x + 3) + (x^2 + x - 2)}{(x - 1)(x + 3)}$$
* **Step 5: Combine like terms**.
  $$(x^2 + x^2) + (4x + x) + (3 - 2) = 2x^2 + 5x + 1$$
* **Final Answer**: $\frac{2x^2 + 5x + 1}{(x - 1)(x + 3)}$ or $\frac{2x^2 + 5x + 1}{x^2 + 2x - 3}$.

---

### Example 6: Complex Rational Expression (Challenging)
**Problem**: Simplify $\frac{1 + \frac{1}{x}}{1 - \frac{1}{x}}$.

* **Step 1: Simplify the top numerator**.
  Express $1$ as $\frac{x}{x}$:
  $$1 + \frac{1}{x} = \frac{x}{x} + \frac{1}{x} = \frac{x + 1}{x}$$
* **Step 2: Simplify the bottom denominator**.
  Express $1$ as $\frac{x}{x}$:
  $$1 - \frac{1}{x} = \frac{x}{x} - \frac{1}{x} = \frac{x - 1}{x}$$
* **Step 3: Rewrite as a division problem**.
  $$\frac{\frac{x + 1}{x}}{\frac{x - 1}{x}} = \frac{x + 1}{x} \div \frac{x - 1}{x}$$
* **Step 4: Flip the bottom fraction and multiply**.
  $$\frac{x + 1}{x} \cdot \frac{x}{x - 1}$$
* **Step 5: Cancel the common factor $x$**.
  $$\frac{x + 1}{\mathbf{\cancel{x}}} \cdot \frac{\mathbf{\cancel{x}}}{x - 1} = \frac{x + 1}{x - 1}$$
* **Final Answer**: $\frac{x + 1}{x - 1}$.

---

### Example 7: Rationalizing a Single Radical Denominator (Easy)
**Problem**: Simplify $\frac{1}{\sqrt{2}}$.

* **Step 1: Identify the radical in the denominator**.
  The denominator contains $\sqrt{2}$.
* **Step 2: Multiply top and bottom by $\frac{\sqrt{2}}{\sqrt{2}}$**.
  $$\frac{1}{\sqrt{2}} \cdot \frac{\sqrt{2}}{\sqrt{2}}$$
* **Step 3: Multiply across**.
  * Numerator: $1 \cdot \sqrt{2} = \sqrt{2}$
  * Denominator: $\sqrt{2} \cdot \sqrt{2} = \sqrt{4} = 2$
* **Final Answer**: $\frac{\sqrt{2}}{2}$.

---

### Example 8: Rationalizing a Binomial Denominator with a Conjugate (Challenging)
**Problem**: Simplify $\frac{1}{1 - \sqrt{2}}$.

* **Step 1: Identify the conjugate of the denominator**.
  The denominator is $1 - \sqrt{2}$. Its conjugate is $1 + \sqrt{2}$.
* **Step 2: Multiply top and bottom by the conjugate**.
  $$\frac{1}{1 - \sqrt{2}} \cdot \frac{1 + \sqrt{2}}{1 + \sqrt{2}}$$
* **Step 3: Expand numerator and denominator**.
  * Numerator: $1 \cdot (1 + \sqrt{2}) = 1 + \sqrt{2}$
  * Denominator (FOIL):
    $$(1 - \sqrt{2})(1 + \sqrt{2}) = 1^2 - (\sqrt{2})^2 = 1 - 2 = -1$$
* **Step 4: Simplify the fraction**.
  $$\frac{1 + \sqrt{2}}{-1} = -(1 + \sqrt{2}) = -1 - \sqrt{2}$$
* **Final Answer**: $-1 - \sqrt{2}$.

---

## 7. Visual Explanations

Visual representations help clarify how operations work and prevent common algebraic mistakes.

### 7.1 Decision Flowchart for Operations
When faced with any rational expression problem, follow this structured decision path:

```
                      +------------------------------------------+
                      | START: What operation do you need to do? |
                      +------------------------------------------+
                                           |
     +-------------------+-----------------+-------------------+-------------------+
     |                   |                                     |                   |
     v                   v                                     v                   v
+----------+   +-------------------+                   +---------------+   +---------------+
| SIMPLIFY |   | MULTIPLY / DIVIDE |                   | ADD / SUBTRACT|   |  RATIONALIZE  |
+----------+   +-------------------+                   +---------------+   +---------------+
     |                   |                                     |                   |
     v                   v                                     v                   v
1. Factor top  1. If ÷, FLIP 2nd fraction.            1. Find LCD.        1. Single √a:
   & bottom.   2. Factor all numerators               2. Rewrite top/        Multiply top/
2. Cancel         & denominators.                        bottom to match    bottom by √a.
   identical   3. Cancel top vs bottom.                  LCD.             2. Binomial a±√b:
   FACTORS.    4. Multiply remaining terms.           3. FOIL & combine      Multiply by
                                                         numerators.         conjugate a∓√b.
```

---

### 7.2 Terms vs. Factors: Visual Comparison

Understanding the difference between **factors** (multiplied) and **terms** (added/subtracted) is the single most important rule in algebraic fraction simplification:

```
CORRECT (Canceling Factors)                   INCORRECT (Canceling Terms)
===========================                   ===========================

      x³ + x²                                        x + 5
     ---------                                      -------
       x + 1                                         x + 2

Factor numerator first:                       CANNOT cancel 'x' terms!
     x² · (x + 1)                                   (x) + 5
    --------------                                  ---------   <-- WRONG!
       (x + 1)                                      (x) + 2

Cancel (x + 1) factor:                        Why? x is ADDED, not multiplied.
    = x²  (VALID!)                            Cannot simplify further!
```

---

## 8. Common Mistakes

Students frequently make predictable errors when solving rational expression problems. Review these five common mistakes to avoid them:

### Mistake 1: Canceling Terms Instead of Factors
* **Incorrect**: $\frac{x + 5}{x + 2} = \frac{5}{2}$  ❌
* **Why it is wrong**: The variable $x$ is being *added* in both top and bottom. You cannot cancel terms separated by addition or subtraction symbols.
* **Correct Rule**: Only cancel entire factors that are multiplied together. $\frac{x + 5}{x + 2}$ cannot be simplified.

---

### Mistake 2: Forgetting to Distribute the Negative Sign in Subtraction
* **Incorrect**: $\frac{5x + 2}{x + 1} - \frac{2x - 3}{x + 1} = \frac{5x + 2 - 2x - 3}{x + 1} = \frac{3x - 1}{x + 1}$  ❌
* **Why it is wrong**: The subtraction applies to the **entire** second numerator $(2x - 3)$, not just $2x$.
* **Correct Method**: Put parentheses around the second numerator and distribute the minus sign:
  $$\frac{(5x + 2) - (2x - 3)}{x + 1} = \frac{5x + 2 - 2x + 3}{x + 1} = \frac{3x + 5}{x + 1} \quad \checkmark$$

---

### Mistake 3: Adding Numerators Without Finding a Common Denominator
* **Incorrect**: $\frac{a}{b} + \frac{c}{d} = \frac{a + c}{b + d}$  ❌
* **Why it is wrong**: Fractions of different whole sizes cannot be added directly.
* **Correct Method**: Convert both fractions to a common denominator ($b \cdot d$) before adding:
  $$\frac{a \cdot d}{b \cdot d} + \frac{c \cdot b}{d \cdot b} = \frac{ad + bc}{bd} \quad \checkmark$$

---

### Mistake 4: Forgetting to Flip the Second Fraction in Division
* **Incorrect**: $\frac{A}{B} \div \frac{C}{D} = \frac{A \cdot C}{B \cdot D}$  ❌
* **Why it is wrong**: Division requires multiplying by the *reciprocal*.
* **Correct Method**: Always invert the divisor (second fraction):
  $$\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \cdot \frac{D}{C} = \frac{A \cdot D}{B \cdot C} \quad \checkmark$$

---

### Mistake 5: Using the Wrong Sign When Rationalizing Binomials
* **Incorrect**: To rationalize $\frac{1}{3 - \sqrt{2}}$, multiplying by $\frac{3 - \sqrt{2}}{3 - \sqrt{2}}$  ❌
* **Why it is wrong**: Multiplying $(3 - \sqrt{2})(3 - \sqrt{2})$ yields $9 - 6\sqrt{2} + 2 = 11 - 6\sqrt{2}$, which still contains a radical!
* **Correct Method**: Multiply by the **conjugate** $(3 + \sqrt{2})$:
  $$(3 - \sqrt{2})(3 + \sqrt{2}) = 3^2 - (\sqrt{2})^2 = 9 - 2 = 7 \quad \checkmark$$

---

## 9. Practice Problems

Test your understanding with these practice problems, arranged from easy to hard. Complete solutions are provided in Section 10.

### Problem 1 (Easy - Simplification)
Simplify the expression:
$$\frac{2x^2 + 6x}{2x}$$

### Problem 2 (Medium - Simplification)
Simplify the expression:
$$\frac{x^2 - 9}{x^2 - 5x + 6}$$

### Problem 3 (Medium - Multiplication)
Multiply and simplify:
$$\frac{x - 3}{x + 4} \cdot \frac{x^2 + 5x + 4}{x^2 - 9}$$

### Problem 4 (Challenging - Division)
Divide and simplify:
$$\frac{x^2 - 4}{x + 1} \div \frac{x + 2}{x^2 + 3x + 2}$$

### Problem 5 (Challenging - Addition / Subtraction)
Subtract and simplify:
$$\frac{x}{x - 2} - \frac{2}{x + 3}$$

### Problem 6 (Challenging - Rationalize Binomial Denominator)
Rationalize the denominator:
$$\frac{3}{2 - \sqrt{5}}$$

---

## 10. Solutions

### Solution to Problem 1
**Problem**: Simplify $\frac{2x^2 + 6x}{2x}$.

1. **Factor out the GCF** ($2x$) in the numerator:
   $$2x^2 + 6x = 2x(x + 3)$$
2. **Rewrite the fraction**:
   $$\frac{2x(x + 3)}{2x}$$
3. **Cancel the common factor $2x$**:
   $$\frac{\mathbf{\cancel{2x}}(x + 3)}{\mathbf{\cancel{2x}}} = x + 3$$
* **Final Answer**: $x + 3$ (where $x \neq 0$).

---

### Solution to Problem 2
**Problem**: Simplify $\frac{x^2 - 9}{x^2 - 5x + 6}$.

1. **Factor the numerator** (Difference of Squares):
   $$x^2 - 9 = (x - 3)(x + 3)$$
2. **Factor the denominator** (Trinomial factoring: numbers multiplying to $+6$ and adding to $-5$ are $-3$ and $-2$):
   $$x^2 - 5x + 6 = (x - 3)(x - 2)$$
3. **Rewrite and cancel $(x - 3)$**:
   $$\frac{\mathbf{\cancel{(x - 3)}}(x + 3)}{\mathbf{\cancel{(x - 3)}}(x - 2)} = \frac{x + 3}{x - 2}$$
* **Final Answer**: $\frac{x + 3}{x - 2}$ (where $x \neq 3, 2$).

---

### Solution to Problem 3
**Problem**: Multiply $\frac{x - 3}{x + 4} \cdot \frac{x^2 + 5x + 4}{x^2 - 9}$.

1. **Factor all components**:
   * $x^2 + 5x + 4 = (x + 4)(x + 1)$
   * $x^2 - 9 = (x - 3)(x + 3)$
2. **Rewrite the product**:
   $$\frac{x - 3}{x + 4} \cdot \frac{(x + 4)(x + 1)}{(x - 3)(x + 3)}$$
3. **Cancel common factors $(x - 3)$ and $(x + 4)$**:
   $$\frac{\mathbf{\cancel{(x - 3)}}}{\mathbf{\cancel{(x + 4)}}} \cdot \frac{\mathbf{\cancel{(x + 4)}}(x + 1)}{\mathbf{\cancel{(x - 3)}}(x + 3)} = \frac{x + 1}{x + 3}$$
* **Final Answer**: $\frac{x + 1}{x + 3}$.

---

### Solution to Problem 4
**Problem**: Divide $\frac{x^2 - 4}{x + 1} \div \frac{x + 2}{x^2 + 3x + 2}$.

1. **Change division to multiplication by flipping the second fraction**:
   $$\frac{x^2 - 4}{x + 1} \cdot \frac{x^2 + 3x + 2}{x + 2}$$
2. **Factor all components**:
   * $x^2 - 4 = (x - 2)(x + 2)$
   * $x^2 + 3x + 2 = (x + 1)(x + 2)$
3. **Substitute factored forms**:
   $$\frac{(x - 2)(x + 2)}{x + 1} \cdot \frac{(x + 1)(x + 2)}{x + 2}$$
4. **Cancel common factors $(x + 1)$ and $(x + 2)$**:
   $$\frac{(x - 2)\mathbf{\cancel{(x + 2)}}}{\mathbf{\cancel{x + 1}}} \cdot \frac{\mathbf{\cancel{(x + 1)}}(x + 2)}{\mathbf{\cancel{x + 2}}} = (x - 2)(x + 2) = x^2 - 4$$
* **Final Answer**: $x^2 - 4$ or $(x - 2)(x + 2)$.

---

### Solution to Problem 5
**Problem**: Subtract $\frac{x}{x - 2} - \frac{2}{x + 3}$.

1. **Identify the LCD**:
   $$\text{LCD} = (x - 2)(x + 3)$$
2. **Rewrite each fraction over the LCD**:
   $$\frac{x(x + 3)}{(x - 2)(x + 3)} - \frac{2(x - 2)}{(x - 2)(x + 3)}$$
3. **Expand the numerators**:
   * First numerator: $x(x + 3) = x^2 + 3x$
   * Second numerator: $2(x - 2) = 2x - 4$
4. **Combine numerators over LCD (Distribute the minus sign!)**:
   $$\frac{(x^2 + 3x) - (2x - 4)}{(x - 2)(x + 3)} = \frac{x^2 + 3x - 2x + 4}{(x - 2)(x + 3)}$$
5. **Combine like terms**:
   $$\frac{x^2 + x + 4}{(x - 2)(x + 3)}$$
* **Final Answer**: $\frac{x^2 + x + 4}{(x - 2)(x + 3)}$ or $\frac{x^2 + x + 4}{x^2 + x - 6}$.

---

### Solution to Problem 6
**Problem**: Rationalize $\frac{3}{2 - \sqrt{5}}$.

1. **Identify conjugate of denominator**:
   The conjugate of $(2 - \sqrt{5})$ is $(2 + \sqrt{5})$.
2. **Multiply top and bottom by conjugate**:
   $$\frac{3}{2 - \sqrt{5}} \cdot \frac{2 + \sqrt{5}}{2 + \sqrt{5}}$$
3. **Expand numerator and denominator**:
   * Numerator: $3(2 + \sqrt{5}) = 6 + 3\sqrt{5}$
   * Denominator: $(2 - \sqrt{5})(2 + \sqrt{5}) = 2^2 - (\sqrt{5})^2 = 4 - 5 = -1$
4. **Simplify fraction**:
   $$\frac{6 + 3\sqrt{5}}{-1} = -(6 + 3\sqrt{5}) = -6 - 3\sqrt{5}$$
* **Final Answer**: $-6 - 3\sqrt{5}$ or $-3(2 + \sqrt{5})$.

---

## 11. Summary

Working with rational expressions requires combining fraction rules with algebraic factoring skills:

1. **Simplification**: Factor polynomials completely and cancel identical top-and-bottom factors.
2. **Multiplication & Division**: Factor all parts, cancel common factors across fractions, and multiply straight across. For division, multiply by the reciprocal of the second fraction.
3. **Addition & Subtraction**: Find the Least Common Denominator (LCD), convert each fraction, combine numerators carefully (always distributing negative signs), and keep the denominator.
4. **Complex Rational Expressions**: Simplify top and bottom into single fractions first, then divide.
5. **Rationalizing Denominators**: Remove square roots by multiplying single radicals by $\frac{\sqrt{a}}{\sqrt{a}}$ and binomial radicals by their conjugate $\frac{a \mp \sqrt{b}}{a \mp \sqrt{b}}$.

---

## 12. Key Things to Remember

* 💡 **Golden Rule**: **Only cancel factors**, NEVER terms! You can cancel $(x+1)$ in $\frac{x(x+1)}{x+1}$, but you CANNOT cancel $x$ in $\frac{x+5}{x+2}$.
* 💡 **Division Flip**: Always change $\div$ to $\cdot$ and flip **only** the second fraction.
* 💡 **Distribute Minuses**: When subtracting fractions, put parentheses around the second numerator so the minus sign applies to every term.
* 💡 **Conjugate Power**: The conjugate of $a - \sqrt{b}$ is $a + \sqrt{b}$. Multiplying them creates $a^2 - b$, eliminating radicals completely.
* 💡 **Factoring First**: Always factor polynomials completely *before* trying to cancel or find LCDs.
