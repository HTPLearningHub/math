# Least Common Multiple (LCM): A Beginner's Guide

---

## 1. Introduction

When working with numbers in mathematics, we often need to compare two or more numbers or find where their patterns overlap [12]. One of the most fundamental concepts for comparing numbers is the **Least Common Multiple (LCM)** [12].

Understanding the LCM helps us solve many mathematical problems [12]. For example, it allows us to:
* Compare fractions with different denominators to see which one is larger [12].
* Add or subtract fractions with different denominators [12].
* Solve real-world scheduling problems (for instance, finding when two buses arriving at different intervals will meet at the same time).

This tutorial explains what the Least Common Multiple is, why it works, how to find it using step-by-step methods, and how to apply it [1, 3, 12].

---

## 2. Prerequisite Knowledge

Before learning about the Least Common Multiple, let us review a few basic mathematical concepts [2].

### Positive Integers
**Positive integers** are the whole counting numbers starting from $1$ [12]:
$$\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \dots\}$$
They do not include zero, negative numbers, or fractions [12].

### Factors
A **factor** is a whole number that divides into another number evenly, leaving a remainder of zero [12].
* For example, the factors of $12$ are $1, 2, 3, 4, 6,$ and $12$, because $12$ can be divided by any of these numbers without a remainder.

### Prime Numbers
A **prime number** is a positive integer greater than $1$ that has exactly two factors: $1$ and itself [12].
* The first few prime numbers are: $2, 3, 5, 7, 11, 13, 17, 19, 23, \dots$
* Note: The number $2$ is the only even prime number.

### Prime Factorization
**Prime factorization** is the process of breaking down a composite number into a product of prime numbers [12]. Every number greater than $1$ can be written as a unique product of prime numbers [12].
* For example, the prime factorization of $12$ is:
  $$12 = 2 \times 2 \times 3 = 2^2 \times 3$$
* The prime factorization of $80$ is:
  $$80 = 2 \times 2 \times 2 \times 2 \times 5 = 2^4 \times 5$$

---

## 3. Important Definitions

Let us define the core terms clearly [3, 8].

### Multiple
A **multiple** of a number is the product obtained when that number is multiplied by any positive integer ($1, 2, 3, 4, \dots$) [12].
* Multiples of $3$: $3 \times 1 = 3$, $3 \times 2 = 6$, $3 \times 3 = 9$, $3 \times 4 = 12, \dots$ [12]
* The list of multiples goes on forever (to infinity) [12].

### Common Multiple
A **common multiple** is a number that is a multiple of two or more numbers at the same time [12].
* For example, $12$ is a multiple of $3$ ($3 \times 4 = 12$) and also a multiple of $4$ ($4 \times 3 = 12$) [12]. Therefore, $12$ is a common multiple of $3$ and $4$ [12].

### Least Common Multiple (LCM)
The **Least Common Multiple (LCM)** of two or more numbers is the **smallest positive integer** that is a multiple of all those numbers [12].
* For $3$ and $4$, the smallest number that appears in both lists of multiples is $12$ [12]. So, $\text{LCM}(3, 4) = 12$ [12].

---

## 4. Main Concepts

There are two primary methods to find the Least Common Multiple: listing multiples and prime factorization [12].

### Method 1: Listing Multiples (Best for Small Numbers)

For small numbers, you can simply write out the first few multiples of each number until you find the smallest number they share [12].

**Steps:**
1. List the multiples of the first number.
2. List the multiples of the second number.
3. Identify the common multiples.
4. Choose the smallest common multiple.

**Example: Finding $\text{LCM}(6, 9)$** [12]
* Multiples of $6$: $6, 12, \mathbf{18}, 24, 30, \mathbf{36}, 42, 48, \mathbf{54}, \dots$ [12]
* Multiples of $9$: $9, \mathbf{18}, 27, \mathbf{36}, 45, \mathbf{54}, \dots$ [12]
* Common multiples: $18, 36, 54, \dots$ [12]
* Smallest common multiple: $18$ [12]

Therefore, $\text{LCM}(6, 9) = 18$ [12].

> **Important Insight:** Multiplying the two numbers gives $6 \times 9 = 54$ [12]. While $54$ is a common multiple, it is **not** the *least* common multiple [12]. The smaller common multiple $18$ exists because $6$ and $9$ share a common factor ($3$) [12].

---

### Method 2: Prime Factorization Method (Shortcut for Larger Numbers)

Listing multiples for large numbers like $12$ and $80$ can take a long time and become tedious [12]. Prime factorization gives us a fast, systematic way to find the LCM [12].

**Steps:**
1. Find the prime factorization of each number [12].
2. Identify every unique prime factor that appears in any of the numbers [12].
3. Count how many times each prime factor appears in each number [12].
4. Take each prime factor repeated the **maximum number of times** it appears in any single number [12].
5. Multiply these prime factors together to get the LCM [12].

**Example: Finding $\text{LCM}(12, 80)$** [12]
1. Write prime factorizations:
   $$12 = 2 \times 2 \times 3 = 2^2 \times 3$$
   $$80 = 2 \times 2 \times 2 \times 2 \times 5 = 2^4 \times 5$$ [12]
2. List unique prime factors: $2, 3,$ and $5$ [12].
3. Determine the maximum frequency for each factor:
   * Factor $2$: appears twice in $12$ ($2^2$), but **four times** in $80$ ($2^4$). Maximum = $4$ times [12].
   * Factor $3$: appears **once** in $12$ ($3^1$), and zero times in $80$. Maximum = $1$ time [12].
   * Factor $5$: appears zero times in $12$, and **once** in $80$ ($5^1$). Maximum = $1$ time [12].
4. Multiply these maximum occurrences:
   $$\text{LCM}(12, 80) = 2 \times 2 \times 2 \times 2 \times 3 \times 5 = 2^4 \times 3^1 \times 5^1$$ [12]
   $$\text{LCM}(12, 80) = 16 \times 3 \times 5 = 240$$ [12]

---

### Practical Application: Comparing Fractions

Suppose you want to know which fraction is larger: $\frac{1}{3}$ or $\frac{1}{4}$ [12].

Because their denominators ($3$ and $4$) are different, direct comparison can be tricky [12]. To make comparison easy, we convert both fractions to **equivalent fractions** with a **least common denominator (LCD)**, which is simply the LCM of the denominators [12].

1. Find $\text{LCM}(3, 4) = 12$ [12].
2. Convert $\frac{1}{3}$ to a fraction with denominator $12$:
   Multiply top and bottom by $4$ (since $\frac{4}{4} = 1$, the value does not change):
   $$\frac{1}{3} \times \frac{4}{4} = \frac{4}{12}$$ [12]
3. Convert $\frac{1}{4}$ to a fraction with denominator $12$:
   Multiply top and bottom by $3$:
   $$\frac{1}{4} \times \frac{3}{3} = \frac{3}{12}$$ [12]
4. Compare numerators:
   Since $4 > 3$, we have:
   $$\frac{4}{12} > \frac{3}{12} \implies \frac{1}{3} > \frac{1}{4}$$ [12]

---

## 5. Formulas and Rules

### 1. General Product Rule
For any two positive integers $a$ and $b$, their product $a \times b$ is always a common multiple, but not necessarily the *least* common multiple [12].
$$\text{LCM}(a, b) \le a \times b$$ [12]

### 2. Coprime Numbers Rule
If two numbers $a$ and $b$ share no common prime factors (they are **coprime** or **relatively prime**), then their LCM is simply their product [12]:
$$\text{LCM}(a, b) = a \times b$$ [12]
* Example: $\text{LCM}(3, 5) = 3 \times 5 = 15$ [12].
* Example: $\text{LCM}(4, 5) = 4 \times 5 = 20$ [12].

### 3. Prime Factorization Formula
If $a = p_1^{e_1} \times p_2^{e_2} \times \dots$ and $b = p_1^{f_1} \times p_2^{f_2} \times \dots$, then:
$$\text{LCM}(a, b) = p_1^{\max(e_1, f_1)} \times p_2^{\max(e_2, f_2)} \times \dots$$ [12]

### 4. Relationship Between LCM and GCF
For any two positive integers $a$ and $b$:
$$\text{LCM}(a, b) \times \text{GCF}(a, b) = a \times b$$
*(where GCF is the Greatest Common Factor).*

---

## 6. Step-by-Step Examples

### Example 1 (Easy): Find $\text{LCM}(3, 5)$ [12]

* **Goal:** Find the smallest common multiple of $3$ and $5$ [12].
* **Step 1:** List multiples of $3$:
  $$3, 6, 9, 12, \mathbf{15}, 18, 21, 24, 27, 30, \dots$$ [12]
* **Step 2:** List multiples of $5$:
  $$5, 10, \mathbf{15}, 20, 25, 30, \dots$$ [12]
* **Step 3:** Identify the first common multiple:
  The smallest number in both lists is $15$ [12].
* **Conclusion:** $\text{LCM}(3, 5) = 15$ [12].

---

### Example 2 (Medium): Find $\text{LCM}(6, 9)$ [12]

* **Goal:** Find the smallest common multiple of $6$ and $9$ using prime factorization [12].
* **Step 1:** Find prime factorization of $6$:
  $$6 = 2 \times 3 = 2^1 \times 3^1$$
* **Step 2:** Find prime factorization of $9$:
  $$9 = 3 \times 3 = 3^2$$
* **Step 3:** Select maximum powers of each prime factor ($2$ and $3$):
  * For $2$: maximum power is $2^1$ (from $6$).
  * For $3$: maximum power is $3^2$ (from $9$).
* **Step 4:** Multiply the maximum powers:
  $$\text{LCM}(6, 9) = 2^1 \times 3^2 = 2 \times 9 = 18$$ [12]
* **Conclusion:** $\text{LCM}(6, 9) = 18$ [12].

---

### Example 3 (Challenging): Find $\text{LCM}(12, 80)$ [12]

* **Goal:** Find the LCM of $12$ and $80$ using prime factorization [12].
* **Step 1:** Break $12$ into prime factors:
  $$12 = 4 \times 3 = 2 \times 2 \times 3 = 2^2 \times 3^1$$ [12]
* **Step 2:** Break $80$ into prime factors:
  $$80 = 8 \times 10 = (2 \times 2 \times 2) \times (2 \times 5) = 2^4 \times 5^1$$ [12]
* **Step 3:** Collect all unique prime factors and their highest exponent:
  * Prime factor $2$: maximum power is $2^4 = 16$ (from $80$) [12].
  * Prime factor $3$: maximum power is $3^1 = 3$ (from $12$) [12].
  * Prime factor $5$: maximum power is $5^1 = 5$ (from $80$) [12].
* **Step 4:** Calculate the product:
  $$\text{LCM}(12, 80) = 2^4 \times 3^1 \times 5^1 = 16 \times 3 \times 5 = 240$$ [12]
* **Conclusion:** $\text{LCM}(12, 80) = 240$ [12].

---

## 7. Visual Explanations

### Visual 1: Multiples Grid Table
The table below shows how multiples of $3, 4,$ and $5$ progress. Notice where common multiples first appear [12].

| Multiplier ($n$) | $3 \times n$ | $4 \times n$ | $5 \times n$ |
| :---: | :---: | :---: | :---: |
| $1$ | $3$ | $4$ | $5$ |
| $2$ | $6$ | $8$ | $10$ |
| $3$ | $9$ | **$12$** | $15$ |
| $4$ | **$12$** | $16$ | **$20$** |
| $5$ | $15$ | **$20$** | $25$ |
| $6$ | $18$ | $24$ | $30$ |

* $\text{LCM}(3, 4) = 12$ (first match between row $4$ of $3$ and row $3$ of $4$) [12].
* $\text{LCM}(4, 5) = 20$ (first match between row $5$ of $4$ and row $4$ of $5$) [12].

---

### Visual 2: Prime Factor Comparison Matrix for $12$ and $80$

| Number | Prime Factor $2$ | Prime Factor $3$ | Prime Factor $5$ |
| :--- | :---: | :---: | :---: |
| $12 = 2^2 \times 3^1$ | $2^2$ ($2$ times) | $3^1$ ($1$ time) | $5^0$ ($0$ times) |
| $80 = 2^4 \times 5^1$ | $2^4$ ($4$ times) | $3^0$ ($0$ times) | $5^1$ ($1$ time) |
| **Highest Power** | **$2^4$** | **$3^1$** | **$5^1$** |

**Calculation:** $2^4 \times 3^1 \times 5^1 = 16 \times 3 \times 5 = 240$ [12].

---

### Visual 3: Fraction Area Model ($\frac{1}{3}$ vs $\frac{1}{4}$)

Imagine dividing a whole circle or bar into equal parts [12]:

```text
Whole Unit divided into 12 equal slices: [ | | | | | | | | | | | ]

1/3 of the whole  =  4 out of 12 slices: [ * | * | * | * |   |   |   |   |   |   |   |   ]  (4/12)
1/4 of the whole  =  3 out of 12 slices: [ * | * | * |   |   |   |   |   |   |   |   |   ]  (3/12)
```

By converting both fractions to 12ths using the LCM of $3$ and $4$, it is clear that $\frac{4}{12}$ is larger than $\frac{3}{12}$ by $1$ slice [12].

---

## 8. Common Mistakes

### Mistake 1: Assuming LCM is always $a \times b$
* **Wrong thought:** "The LCM of $6$ and $9$ is $6 \times 9 = 54$." [12]
* **Why it is wrong:** $54$ is a common multiple, but it is not the *least* common multiple [12].
* **Correct approach:** List multiples or use prime factorization. The LCM of $6$ and $9$ is $18$ [12].

### Mistake 2: Confusing LCM with GCF
* **Wrong thought:** "The LCM of $12$ and $80$ is $4$."
* **Why it is wrong:** $4$ is the **Greatest Common Factor** (the largest number that divides both $12$ and $80$). Multiples are larger than or equal to the original numbers, whereas factors are smaller than or equal.
* **Correct approach:** Multiples grow larger: $\text{LCM}(12, 80) = 240$ [12].

### Mistake 3: Taking the minimum power instead of the maximum power
* **Wrong thought:** "For $12 = 2^2 \times 3$ and $80 = 2^4 \times 5$, take $2^2$ because it is smaller."
* **Why it is wrong:** If you only take $2^2$, the result will not be divisible by $80$ (which requires $2^4$).
* **Correct approach:** Always select the **maximum** exponent for each prime factor [12].

### Mistake 4: Multiplying only the denominator when finding equivalent fractions
* **Wrong thought:** To convert $\frac{1}{3}$ to 12ths, change it to $\frac{1}{12}$."
* **Why it is wrong:** Changing $\frac{1}{3}$ to $\frac{1}{12}$ alters the value of the fraction!
* **Correct approach:** You must multiply both top and bottom by $4$: $\frac{1 \times 4}{3 \times 4} = \frac{4}{12}$ [12].

---

## 9. Practice Problems

Try to solve these practice problems on your own before reading the solutions [8, 9].

1. **Problem 1 (Easy):** Find the Least Common Multiple of $4$ and $6$.
2. **Problem 2 (Medium):** Find the Least Common Multiple of $15$ and $20$ using prime factorization.
3. **Problem 3 (Challenging):** Find the Least Common Multiple of three numbers: $12$, $18$, and $30$.
4. **Problem 4 (Application):** Which fraction is larger: $\frac{5}{6}$ or $\frac{7}{9}$? Use the LCM of their denominators to show your reasoning step by step.

---

## 10. Solutions

### Solution to Problem 1
* **Goal:** Find $\text{LCM}(4, 6)$.
* **Method 1 (Listing multiples):**
  * Multiples of $4$: $4, 8, \mathbf{12}, 16, 20, \mathbf{24}, \dots$
  * Multiples of $6$: $6, \mathbf{12}, 18, \mathbf{24}, 30, \dots$
  * The smallest common multiple is $12$.
* **Answer:** $\text{LCM}(4, 6) = 12$.

---

### Solution to Problem 2
* **Goal:** Find $\text{LCM}(15, 20)$ using prime factorization.
* **Step 1:** Prime factorization of $15$:
  $$15 = 3^1 \times 5^1$$
* **Step 2:** Prime factorization of $20$:
  $$20 = 4 \times 5 = 2^2 \times 5^1$$
* **Step 3:** Select maximum powers of each prime factor ($2, 3, 5$):
  * Prime $2$: $2^2 = 4$
  * Prime $3$: $3^1 = 3$
  * Prime $5$: $5^1 = 5$
* **Step 4:** Multiply the maximum powers:
  $$\text{LCM}(15, 20) = 2^2 \times 3^1 \times 5^1 = 4 \times 3 \times 5 = 60$$
* **Answer:** $\text{LCM}(15, 20) = 60$.

---

### Solution to Problem 3
* **Goal:** Find $\text{LCM}(12, 18, 30)$.
* **Step 1:** Write prime factorizations for all three numbers:
  $$12 = 2^2 \times 3^1$$
  $$18 = 2^1 \times 3^2$$
  $$30 = 2^1 \times 3^1 \times 5^1$$
* **Step 2:** Identify highest power for each prime factor ($2, 3, 5$):
  * Highest power of $2$: $2^2 = 4$ (from $12$)
  * Highest power of $3$: $3^2 = 9$ (from $18$)
  * Highest power of $5$: $5^1 = 5$ (from $30$)
* **Step 3:** Multiply maximum powers together:
  $$\text{LCM}(12, 18, 30) = 2^2 \times 3^2 \times 5^1 = 4 \times 9 \times 5 = 180$$
* **Answer:** $\text{LCM}(12, 18, 30) = 180$.

---

### Solution to Problem 4
* **Goal:** Compare $\frac{5}{6}$ and $\frac{7}{9}$.
* **Step 1:** Find LCM of denominators $6$ and $9$.
  From earlier, $\text{LCM}(6, 9) = 18$.
* **Step 2:** Convert $\frac{5}{6}$ to 18ths:
  $$\frac{5}{6} = \frac{5 \times 3}{6 \times 3} = \frac{15}{18}$$
* **Step 3:** Convert $\frac{7}{9}$ to 18ths:
  $$\frac{7}{9} = \frac{7 \times 2}{9 \times 2} = \frac{14}{18}$$
* **Step 4:** Compare the numerators:
  Since $15 > 14$, we have $\frac{15}{18} > \frac{14}{18}$.
* **Answer:** $\frac{5}{6}$ is larger than $\frac{7}{9}$.

---

## 11. Summary

* A **multiple** is the result of multiplying a number by a positive integer ($1, 2, 3, \dots$) [12].
* The **Least Common Multiple (LCM)** is the smallest number that is a multiple of two or more numbers [12].
* For small numbers, find the LCM by listing multiples [12].
* For larger numbers, use **prime factorization**: take the highest power of every prime factor present and multiply them together [12].
* Common applications of LCM include finding common denominators to compare, add, or subtract fractions [12].

---

## 12. Key Things to Remember

* $\text{LCM}(a, b)$ is never smaller than the larger of the two numbers [12].
* Multiplying $a \times b$ always gives a common multiple, but it is only the *least* common multiple if $a$ and $b$ share no prime factors [12].
* In prime factorization, **always take the maximum power** of each prime factor [12].
* When creating equivalent fractions, multiply both numerator and denominator by the same factor so the fraction's magnitude remains unchanged ($\frac{n}{n} = 1$) [12].
