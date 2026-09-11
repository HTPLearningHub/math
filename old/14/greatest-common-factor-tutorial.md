# Greatest Common Factor (GCF): Complete Beginner-Friendly Guide

### Greatest Common Factor (GCF)

#### 1. Introduction
The **Greatest Common Factor (GCF)** is one of the foundational concepts in arithmetic and elementary algebra. When comparing two or more whole numbers, the GCF is the **largest whole number that divides evenly into all of them without leaving a remainder**.

Understanding the GCF is essential for several key mathematical tasks:
*   **Simplifying Fractions**: Reducing fractions to their lowest terms (for example, simplifying $\frac{18}{24}$ to $\frac{3}{4}$ by dividing both the numerator and denominator by their GCF, $6$).
*   **Factoring Expressions**: Factoring out common terms in algebra (such as $12x + 18 = 6(2x + 3)$).
*   **Solving Real-World Problems**: Dividing objects, resources, or items into equal groups without any leftovers.

---

#### 2. Prerequisite Knowledge
Before learning about the Greatest Common Factor, it is helpful to review a few basic mathematical building blocks.

##### A. Whole Numbers and Divisibility
*   **Whole Number**: A number without fractions or decimals (for example, $0, 1, 2, 3, 10, 45$).
*   **Divisibility**: A number $a$ is divisible by a number $b$ if dividing $a \div b$ yields a whole number with **no remainder** (a remainder of $0$). For example, $15$ is divisible by $5$ because $15 \div 5 = 3$.

##### B. Factors vs. Multiples
It is very common for students to confuse **factors** and **multiples**. Here is the simple distinction:
*   **Factor**: A number that divides *into* another number. Factors are always **smaller than or equal to** the target number.
    *   *Example*: The factors of $12$ are $1, 2, 3, 4, 6,$ and $12$.
*   **Multiple**: The product of multiplying a number by a whole number. Multiples are always **equal to or larger than** the target number.
    *   *Example*: The multiples of $12$ are $12, 24, 36, 48, 60, \dots$

| Feature | Factors | Multiples |
| :--- | :--- | :--- |
| **Meaning** | Numbers that divide *into* the target | Results of multiplying the target by $1, 2, 3, \dots$ |
| **Size** | Smaller than or equal to the number | Equal to or larger than the number |
| **Count** | Finite (limited list) | Infinite (never ends) |
| **Example for $6$** | $1, 2, 3, 6$ | $6, 12, 18, 24, 30, \dots$ |

##### C. Prime Numbers and Prime Factorization
*   **Prime Number**: A whole number greater than $1$ that has **exactly two factors**: $1$ and itself.
    *   *First few prime numbers*: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29$.
    *   *Note*: The number $2$ is the only even prime number.
*   **Composite Number**: A whole number greater than $1$ that has more than two factors (for example, $4, 6, 8, 9, 10, 12$).
*   **Prime Factorization**: Breaking down a composite number into a product of prime numbers only.
    *   *Example*: The prime factorization of $18$ is $2 \times 3 \times 3 = 2 \times 3^2$.

---

#### 3. Important Definitions

*   **Factor (Divisor)**: A whole number $d$ is a factor of $n$ if there exists a whole number $k$ such that:
    $$n = d \times k$$
*   **Common Factor**: A whole number that is a factor of two or more given numbers.
*   **Greatest Common Factor (GCF)**: The largest whole number that is a factor of all numbers in a given set. The GCF is also known as the **Greatest Common Divisor (GCD)**.
*   **Relatively Prime (Co-Prime)**: Two or more whole numbers are said to be relatively prime if their only common factor is $1$. That is:
    $$\text{GCF}(a, b) = 1$$
    *   *Example*: The factors of $8$ are $\{1, 2, 4, 8\}$ and the factors of $15$ are $\{1, 3, 5, 15\}$. Their only shared factor is $1$, so $8$ and $15$ are relatively prime.

---

#### 4. Main Concepts

There are two primary methods to find the Greatest Common Factor of two or more numbers:

##### Method 1: The Listing Factors Method
1. Write down all the factors of the first number.
2. Write down all the factors of the second number.
3. Compare the two lists and identify all numbers present in both lists (**common factors**).
4. Select the largest number from the common factors.

*When to use*: This method works well for **small numbers** that have very few factors (such as $10$ and $15$). However, for larger numbers, listing every factor becomes slow, tedious, and prone to missing factors.

##### Method 2: The Prime Factorization Method (The "Shortcut")
Instead of listing every single factor, we break each number down into its prime building blocks.
1. Find the prime factorization of each number.
2. Identify all prime factors that appear in **both** factorizations.
3. Take each shared prime factor the minimum number of times it appears in any of the factorizations.
4. Multiply these common prime factors together to obtain the GCF.

*Why it works (The Intuition)*:
Every whole number greater than $1$ is uniquely constructed from prime factors (like building a house out of prime lego bricks). Any shared factor of two numbers must be built strictly from prime factors that *both* numbers possess. To form the *largest* possible shared factor, we take all the shared prime bricks available in both numbers and multiply them together.

---

#### 5. Formulas and Rules

##### Mathematical Definition of GCF via Listing
For sets of factors $\text{Factors}(a)$ and $\text{Factors}(b)$:
$$\text{Common Factors} = \text{Factors}(a) \cap \text{Factors}(b)$$
$$\text{GCF}(a, b) = \max\left(\text{Common Factors}\right)$$

##### Mathematical Definition of GCF via Prime Factorization
Given prime factorizations in prime-power form:
$$a = p_1^{e_1} \cdot p_2^{e_2} \cdots p_k^{e_k}$$
$$b = p_1^{f_1} \cdot p_2^{f_2} \cdots p_k^{f_k}$$
The formula for the GCF takes the **minimum exponent** for each prime factor:
$$\text{GCF}(a, b) = p_1^{\min(e_1, f_1)} \cdot p_2^{\min(e_2, f_2)} \cdots p_k^{\min(e_k, f_k)}$$

##### Summary Comparison of Methods

| Feature | Method 1: Listing Factors | Method 2: Prime Factorization |
| :--- | :--- | :--- |
| **Best suited for** | Small numbers (e.g., $10, 12, 15$) | Large numbers (e.g., $24, 108, 360$) |
| **Process** | List all factors $\rightarrow$ Find overlap $\rightarrow$ Pick largest | Prime factorize $\rightarrow$ Multiply common prime factors |
| **Speed** | Fast for small numbers | Fast for any size |
| **Reliability** | Medium (easy to miss factors) | High (systematic and reliable) |

---

#### 6. Step-by-Step Examples

##### Example 1 (Easy): Find the GCF of $10$ and $15$

**Method: Listing Factors**

*   **Step 1: List all factors of $10$.**
    Think of number pairs that multiply to $10$:
    $$1 \times 10 = 10$$
    $$2 \times 5 = 10$$
    Factors of $10$: $\{1, 2, 5, 10\}$

*   **Step 2: List all factors of $15$.**
    Think of number pairs that multiply to $15$:
    $$1 \times 15 = 15$$
    $$3 \times 5 = 15$$
    Factors of $15$: $\{1, 3, 5, 15\}$

*   **Step 3: Find the common factors.**
    Look for numbers in both lists: $\{1, 5\}$.

*   **Step 4: Select the greatest common factor.**
    The largest number in $\{1, 5\}$ is $5$.

$$\text{GCF}(10, 15) = 5$$

---

##### Example 2 (Medium): Find the GCF of $18$ and $24$

Let's solve this problem using both methods to see how they compare.

**Approach A: Listing Factors**
*   Factors of $18$: $\{1, 2, 3, 6, 9, 18\}$
*   Factors of $24$: $\{1, 2, 3, 4, 6, 8, 12, 24\}$
*   Common factors: $\{1, 2, 3, 6\}$
*   Greatest Common Factor: $6$

**Approach B: Prime Factorization**

*   **Step 1: Perform prime factorization of $18$.**
    $$18 = 2 \times 9 = 2 \times 3 \times 3$$

*   **Step 2: Perform prime factorization of $24$.**
    $$24 = 2 \times 12 = 2 \times 4 \times 3 = 2 \times 2 \times 2 \times 3$$

*   **Step 3: Extract prime factors present in BOTH lists.**
    *   Is there a $2$ in both lists? Yes, one $2$ appears in both lists.
    *   Is there a second $2$ in both lists? No, $18$ only has one $2$.
    *   Is there a $3$ in both lists? Yes, one $3$ appears in both lists.
    *   Is there a second $3$ in both lists? No, $24$ only has one $3$.

*   **Step 4: Multiply the common prime factors.**
    $$\text{GCF}(18, 24) = 2 \times 3 = 6$$

Both methods yield the same result: $\text{GCF}(18, 24) = 6$.

---

##### Example 3 (Challenging): Find the GCF of $24$ and $108$

For larger numbers like $108$, listing all factors is inefficient. We use **Prime Factorization**.

*   **Step 1: Prime factorize $24$.**
    Break $24$ into prime numbers using factor trees:
    $$24 = 2 \times 12 = 2 \times 2 \times 6 = 2 \times 2 \times 2 \times 3$$
    In exponent form:
    $$24 = 2^3 \times 3^1$$

*   **Step 2: Prime factorize $108$.**
    Break $108$ into prime numbers:
    $$108 = 2 \times 54 = 2 \times 2 \times 27 = 2 \times 2 \times 3 \times 9 = 2 \times 2 \times 3 \times 3 \times 3$$
    In exponent form:
    $$108 = 2^2 \times 3^3$$

*   **Step 3: Compare and select shared prime factors.**
    *   **Prime factor $2$**: $24$ has three $2$'s ($2^3$), while $108$ has two $2$'s ($2^2$). The shared amount is **two $2$'s** ($2^2$).
    *   **Prime factor $3$**: $24$ has one $3$ ($3^1$), while $108$ has three $3$'s ($3^3$). The shared amount is **one $3$** ($3^1$).

*   **Step 4: Multiply the shared prime factors.**
    $$\text{GCF}(24, 108) = 2 \times 2 \times 3 = 12$$

Alternatively, using the exponent formula:
$$\text{GCF}(24, 108) = 2^{\min(3, 2)} \times 3^{\min(1, 3)} = 2^2 \times 3^1 = 4 \times 3 = 12$$

---

#### 7. Visual Explanations

Visualizing factor overlaps makes the concept of GCF clear and intuitive.

##### A. Factor Tree Breakdown Diagram
Below is the step-by-step prime decomposition for $24$ and $108$:

```
       24                      108
      /  \                    /   \
     2   12                  2    54
        /  \                     /  \
       2    6                   2   27
           / \                     /  \
          2   3                   3    9
                                      / \
                                     3   3

Prime Factors of 24  :  [2] × [2] ×  2  × [3]
Prime Factors of 108 :  [2] × [2] × [3] ×  3  × 3
                        ---   ---   ---
Shared Prime Factors :   2  ×  2  ×  3  = 12
```

##### B. Shared Factors Breakdown Table
| Number | Prime Factorization | Shared Primes | Unshared Primes | GCF Product |
| :--- | :--- | :--- | :--- | :--- |
| **24** | $2 \times 2 \times 2 \times 3$ | $2, 2, 3$ | $2$ | $2 \times 2 \times 3 = 12$ |
| **108** | $2 \times 2 \times 3 \times 3 \times 3$ | $2, 2, 3$ | $3, 3$ | $2 \times 2 \times 3 = 12$ |

---

#### 8. Common Mistakes

Here are four frequent errors students make when calculating the GCF, along with how to avoid them:

##### 1. Confusing GCF (Factor) with LCM (Multiple)
*   **The Error**: Students often calculate the Least Common Multiple (LCM) when asked for the GCF. For example, claiming the GCF of $10$ and $15$ is $30$.
*   **Why it's wrong**: $30$ is a *multiple* of $10$ and $15$, not a factor. A factor must be **equal to or smaller** than the numbers given.
*   **How to avoid**: Remember: **Factor = Few/Smaller**, **Multiple = Many/Larger**. The GCF can never be larger than the smallest number in the problem!

##### 2. Missing Factors when Using the Listing Method
*   **The Error**: Listing factors of $24$ as $\{2, 3, 4, 6, 8, 12\}$ and missing $1$ and $24$.
*   **How to avoid**: Always list factors in **rainbow pairs**:
    $$1 \times 24 = 24$$
    $$2 \times 12 = 24$$
    $$3 \times 8 = 24$$
    $$4 \times 6 = 24$$

##### 3. Taking the Highest Exponent Instead of the Lowest
*   **The Error**: When prime factorizing $24 = 2^3 \times 3^1$ and $108 = 2^2 \times 3^3$, taking $2^3 \times 3^3 = 216$.
*   **Why it's wrong**: Taking the highest powers calculates the **LCM** ($216$), not the GCF.
*   **How to avoid**: For GCF, always pick the **minimum** exponent for shared prime factors: $2^{\min(3,2)} \times 3^{\min(1,3)} = 2^2 \times 3^1 = 12$.

##### 4. Including Unshared Prime Factors
*   **The Error**: Including prime factors that only appear in one number's factorization.
*   **How to avoid**: A prime factor MUST appear in **all** numbers to be included in the GCF calculation.

---

#### 9. Practice Problems

Try these practice problems to test your understanding. Complete solutions are provided in Section 10.

1.  **Problem 1 (Easy)**: Find the GCF of $12$ and $20$ using the listing factors method.
2.  **Problem 2 (Medium)**: Find the GCF of $36$ and $60$ using prime factorization.
3.  **Problem 3 (Medium)**: Find the GCF of $45$ and $75$.
4.  **Problem 4 (Challenging)**: Find the GCF of three numbers: $48$, $72$, and $120$.
5.  **Problem 5 (Word Problem)**: A teacher has $30$ blue pens and $45$ red pens. She wants to divide all the pens into identical pencil pouches with no pens left over.
    *   (a) What is the maximum number of identical pouches she can make?
    *   (b) How many blue pens and how many red pens will be in each pouch?

---

#### 10. Solutions

##### Solution to Problem 1
*   **Step 1: List factors of $12$.**
    $$1 \times 12 = 12, \quad 2 \times 6 = 12, \quad 3 \times 4 = 12$$
    Factors of $12$: $\{1, 2, 3, 4, 6, 12\}$
*   **Step 2: List factors of $20$.**
    $$1 \times 20 = 20, \quad 2 \times 10 = 20, \quad 4 \times 5 = 20$$
    Factors of $20$: $\{1, 2, 4, 5, 10, 20\}$
*   **Step 3: Common factors.**
    $$\text{Common Factors} = \{1, 2, 4\}$$
*   **Step 4: Select greatest factor.**
    $$\text{GCF}(12, 20) = 4$$

---

##### Solution to Problem 2
*   **Step 1: Prime factorize $36$.**
    $$36 = 6 \times 6 = (2 \times 3) \times (2 \times 3) = 2^2 \times 3^2$$
*   **Step 2: Prime factorize $60$.**
    $$60 = 6 \times 10 = (2 \times 3) \times (2 \times 5) = 2^2 \times 3^1 \times 5^1$$
*   **Step 3: Extract shared prime factors.**
    *   Prime $2$: Minimum power is $2^{\min(2,2)} = 2^2 = 4$.
    *   Prime $3$: Minimum power is $3^{\min(2,1)} = 3^1 = 3$.
    *   Prime $5$: Only in $60$, so minimum power is $5^0 = 1$ (do not include).
*   **Step 4: Multiply shared prime factors.**
    $$\text{GCF}(36, 60) = 2^2 \times 3^1 = 4 \times 3 = 12$$

---

##### Solution to Problem 3
*   **Step 1: Prime factorize $45$.**
    $$45 = 5 \times 9 = 5 \times 3 \times 3 = 3^2 \times 5^1$$
*   **Step 2: Prime factorize $75$.**
    $$75 = 3 \times 25 = 3 \times 5 \times 5 = 3^1 \times 5^2$$
*   **Step 3: Extract shared prime factors.**
    *   Prime $3$: Minimum power is $3^{\min(2,1)} = 3^1$.
    *   Prime $5$: Minimum power is $5^{\min(1,2)} = 5^1$.
*   **Step 4: Multiply.**
    $$\text{GCF}(45, 75) = 3^1 \times 5^1 = 15$$

---

##### Solution to Problem 4
*   **Step 1: Prime factorize all three numbers.**
    *   $48 = 16 \times 3 = 2^4 \times 3^1$
    *   $72 = 8 \times 9 = 2^3 \times 3^2$
    *   $120 = 10 \times 12 = (2 \times 5) \times (4 \times 3) = 2^3 \times 3^1 \times 5^1$
*   **Step 2: Identify prime factors common to ALL THREE numbers.**
    *   Prime $2$: Exponents are $4, 3, 3$. Minimum exponent is $3 \rightarrow 2^3$.
    *   Prime $3$: Exponents are $1, 2, 1$. Minimum exponent is $1 \rightarrow 3^1$.
    *   Prime $5$: Only present in $120$, so exclude.
*   **Step 3: Multiply common prime powers.**
    $$\text{GCF}(48, 72, 120) = 2^3 \times 3^1 = 8 \times 3 = 24$$

---

##### Solution to Problem 5
*   **(a) Find the maximum number of identical pouches:**
    The maximum number of pouches that divides both $30$ blue pens and $45$ red pens evenly is the GCF of $30$ and $45$.
    *   $30 = 2 \times 3 \times 5 = 2^1 \times 3^1 \times 5^1$
    *   $45 = 3 \times 3 \times 5 = 3^2 \times 5^1$
    *   Shared prime factors: $3^1 \times 5^1 = 15$.
    *   $$\text{GCF}(30, 45) = 15$$
    *   **Answer (a)**: The maximum number of identical pouches is **$15$ pouches**.

*   **(b) Find the contents of each pouch:**
    *   Blue pens per pouch: $30 \div 15 = 2$ blue pens.
    *   Red pens per pouch: $45 \div 15 = 3$ red pens.
    *   **Answer (b)**: Each pouch will contain **$2$ blue pens** and **$3$ red pens**.

---

#### 11. Summary

1.  The **Greatest Common Factor (GCF)** is the largest whole number that divides evenly into two or more numbers.
2.  For **small numbers**, list all factors for each number and choose the largest common factor.
3.  For **larger numbers**, perform **prime factorization**, pick the shared prime factors with the smallest exponents, and multiply them together.
4.  If two numbers share no prime factors, their GCF is $1$, and they are called **relatively prime**.

---

#### 12. Key Things to Remember

*   $\text{GCF} \le \text{smallest number in the set}$.
*   **Listing Method**: Good for small numbers; list factor pairs in order.
*   **Prime Factorization Method**: Express numbers as products of primes, then take $p_i^{\min(e_i, f_i)}$.
*   **GCF vs LCM**: GCF uses the **lowest** exponents of common primes (finding factors), while LCM uses the **highest** exponents of all primes (finding multiples).
*   If $\text{GCF}(a, b) = 1$, $a$ and $b$ are **co-prime** (relatively prime).