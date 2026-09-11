# Divisibility, Prime Numbers, and Prime Factorization: A Beginner's Guide

---

## 1. Introduction

When we learn mathematics, division is one of the most basic and useful tools we use. But what happens when we divide one whole number by another? Sometimes the division is clean and leaves no leftover parts. Other times, there is something left over, which we call a **remainder**. 

Understanding how numbers divide into each other opens up a fascinating area of mathematics known as **number theory**. In this guide, you will learn:
* What it means for one number to be **divisible** by another.
* What **factors** are and how to find all factors of any number.
* What makes **prime numbers** special and why they are called the "building blocks" of all numbers.
* How to break any number down into its prime components using **prime factorization**.
* Why the **Fundamental Theorem of Arithmetic** guarantees that every number has a unique mathematical "fingerprint."

This manual is written in simple language and breaks down every idea step by step so you can build a strong mathematical foundation.

---

## 2. Prerequisite Knowledge

Before exploring prime numbers, let us review a few basic mathematical ideas that you should know.

### 2.1 Whole Numbers and Natural Numbers
* **Whole Numbers**: The set of numbers starting from $0$ and going upward without fractions or decimals:
  $$0, 1, 2, 3, 4, 5, 6, 7, 8, \dots$$
* **Positive Integers (Natural Numbers)**: Whole numbers that are strictly greater than zero:
  $$1, 2, 3, 4, 5, 6, 7, 8, \dots$$

### 2.2 Basic Division and Remainders
When you divide a number $a$ (the **dividend**) by another number $b$ (the **divisor**), you get a **quotient** $q$ and a **remainder** $r$:
$$a \div b = q \text{ with remainder } r$$

Or written as an equation:
$$a = (b \times q) + r$$

* If $r = 0$, the division is **exact** or **even**. We say that $b$ divides $a$ without a remainder.
* If $r > 0$, the division leaves a remainder, meaning $b$ does not divide $a$ evenly.

#### Example:
* Divide $10$ by $2$:
  $$10 \div 2 = 5 \text{ with remainder } 0$$
  Here, $r = 0$, so $10$ is evenly divisible by $2$.

* Divide $10$ by $3$:
  $$10 \div 3 = 3 \text{ with remainder } 1$$
  Here, $r = 1$, so $10$ is **not** evenly divisible by $3$.

---

## 3. Important Definitions

To talk about numbers clearly, mathematicians use specific terms. Here are the most important definitions explained in simple language:

| Term | Simple Definition | Mathematical Notation / Example |
| :--- | :--- | :--- |
| **Divisibility** | The property of one whole number being divided by another whole number with no remainder ($r = 0$). | $10$ is divisible by $2$ because $10 \div 2 = 5$. |
| **Factor** | A number that divides another number evenly. | $2$ and $5$ are factors of $10$ because $2 \times 5 = 10$. |
| **Multiple** | The result of multiplying a given number by any whole number. | Multiples of $3$ are $3, 6, 9, 12, 15, \dots$ |
| **Even Number** | Any whole number that is divisible by $2$. | $0, 2, 4, 6, 8, 10, 12, \dots$ |
| **Odd Number** | Any whole number that is **not** divisible by $2$. | $1, 3, 5, 7, 9, 11, 13, \dots$ |
| **Prime Number** | A whole number greater than $1$ that has **exactly two** positive factors: $1$ and itself. | $2, 3, 5, 7, 11, 13, 17, 19, 23, \dots$ |
| **Composite Number** | A whole number greater than $1$ that has **more than two** positive factors. | $4, 6, 8, 9, 10, 12, 14, 15, \dots$ |
| **Prime Factorization** | Writing a composite number as a product of only prime numbers. | $20 = 2 \times 2 \times 5 = 2^2 \times 5$. |

---

## 4. Main Concepts

### 4.1 Understanding Factors and Divisibility

A **factor** is a building block of a number through multiplication. If you can multiply two whole numbers $a$ and $b$ to get $c$:
$$a \times b = c$$
then both $a$ and $b$ are factors of $c$.

#### The Halfway Rule for Finding Factors
When searching for factors of a positive integer $N$:
1. $1$ is **always** a factor of $N$, because $N \div 1 = N$.
2. $N$ is **always** a factor of $N$, because $N \div N = 1$.
3. **Important Property**: No number larger than half of $N$ ($\frac{N}{2}$) can be a factor of $N$, except $N$ itself!

Why does this rule work?
If a factor $f$ were larger than $\frac{N}{2}$, its matching factor pair $\frac{N}{f}$ would have to be smaller than $2$. But the only positive whole number smaller than $2$ is $1$. Therefore, once you test numbers up to $\frac{N}{2}$, you can stop searching and jump directly to $N$ itself.

---

### 4.2 Prime Numbers vs. Composite Numbers

Every whole number greater than $1$ falls into one of two categories: **prime** or **composite**.

```
                   Whole Numbers Greater Than 1
                               |
               +---------------+---------------+
               |                               |
         Prime Numbers                 Composite Numbers
     (Only 2 factors: 1 & N)       (3 or more factors)
    Examples: 2, 3, 5, 7, 11...   Examples: 4, 6, 8, 9, 10...
```

#### Why is $1$ Not a Prime Number?
A common mistake is thinking $1$ is a prime number. However, by mathematical definition:
* A prime number must have **exactly two distinct positive factors**: $1$ and itself.
* For the number $1$, the factors are $1$ and itself ($1$), which are the exact same number! So $1$ has only **one** factor.
* Because $1$ has only one factor, $1$ is **neither prime nor composite**.

#### The Special Status of the Number $2$
* $2$ is the **smallest** prime number.
* $2$ is the **only even prime number**.
* Why are no other even numbers prime? Because every even number greater than $2$ ($4, 6, 8, 10, \dots$) can be divided by $2$. Thus, every larger even number has at least three factors: $1$, $2$, and the number itself.

#### Are All Odd Numbers Prime?
No! While all prime numbers greater than $2$ are odd, not all odd numbers are prime.
* $9$ is odd, but $9 = 3 \times 3$, so its factors are $\{1, 3, 9\}$ (Composite).
* $15$ is odd, but $15 = 3 \times 5$, so its factors are $\{1, 3, 5, 15\}$ (Composite).
* $21$ is odd, but $21 = 3 \times 7$, so its factors are $\{1, 3, 7, 21\}$ (Composite).

#### Are There Infinitely Many Prime Numbers?
Yes! Ancient Greek mathematician Euclid proved over $2,000$ years ago that there is no largest prime number. Prime numbers go on forever. Computers continue to search for massive prime numbers; the largest known prime numbers have tens of millions of digits!

---

### 4.3 Prime Factorization and the Fundamental Theorem of Arithmetic

#### What is Prime Factorization?
Prime factorization is the process of breaking down a composite number into a product of numbers that are **all prime**. Think of prime numbers as the chemical elements (atoms) of the number world. Composite numbers are like molecules made by combining these prime atoms together.

For example, take the number $20$:
* We can break $20$ into $4 \times 5$.
* Here, $5$ is prime, but $4$ is composite ($4 = 2 \times 2$).
* Replacing $4$ with $2 \times 2$, we get:
  $$20 = 2 \times 2 \times 5 = 2^2 \times 5$$
* Now, all factors ($2, 2, 5$) are prime! We are finished.

#### The Fundamental Theorem of Arithmetic
The **Fundamental Theorem of Arithmetic** is one of the most important theorems in mathematics. It states:

> **Every integer greater than $1$ is either a prime number itself or can be written as a product of prime numbers in exactly one unique way (ignoring the order of the factors).**

What does this mean in practice?
It means that no matter which factor pair you choose to start with when breaking down a number, you will **always** end up with the exact same set of prime factors!

Let us see this in action with the number $90$:

* **Path A**: Start with factor pair $9 \times 10$:
  $$90 = 9 \times 10$$
  Break down $9$: $9 = 3 \times 3$
  Break down $10$: $10 = 2 \times 5$
  Combine all prime factors:
  $$90 = 3 \times 3 \times 2 \times 5 = 2 \times 3^2 \times 5$$

* **Path B**: Start with factor pair $30 \times 3$:
  $$90 = 30 \times 3$$
  Break down $30$: $30 = 10 \times 3$
  Break down $10$: $10 = 2 \times 5$
  Combine all prime factors:
  $$90 = (2 \times 5) \times 3 \times 3 = 2 \times 3^2 \times 5$$

Both paths give the exact same prime factors: one $2$, two $3$'s, and one $5$ ($2 \times 3^2 \times 5$).

---

## 5. Formulas and Rules

### 5.1 Divisibility Test Rules (Quick Reference)

Checking whether a number is divisible by small prime numbers saves time during prime factorization.

| Divisor | Rule | Simple Example |
| :---: | :--- | :--- |
| **$2$** | The last digit is even ($0, 2, 4, 6, 8$). | $148$ ends in $8$ (even), so $148$ is divisible by $2$. |
| **$3$** | The sum of all digits is divisible by $3$. | For $372$: $3 + 7 + 2 = 12$. Since $12 \div 3 = 4$, $372$ is divisible by $3$. |
| **$5$** | The last digit is $0$ or $5$. | $845$ ends in $5$, so $845$ is divisible by $5$. |
| **$10$** | The last digit is $0$. | $90$ ends in $0$, so $90$ is divisible by $10$. |

---

### 5.2 Mathematical Rules and Formulas

1. **Definition of Divisibility**:
   $$a \mid b \iff \exists\, k \in \mathbb{Z} \text{ such that } b = k \cdot a$$
   *(Read: "$a$ divides $b$ if and only if there exists an integer $k$ such that $b = k \cdot a$")*

2. **Prime Factorization Standard Form (Canonical Representation)**:
   Any integer $N > 1$ can be expressed uniquely as:
   $$N = p_1^{e_1} \times p_2^{e_2} \times p_3^{e_3} \times \dots \times p_k^{e_k}$$
   where $p_1 < p_2 < \dots < p_k$ are distinct prime numbers and $e_1, e_2, \dots, e_k$ are positive integer exponents.

3. **Formula for Total Number of Factors**:
   If $N = p_1^{e_1} \times p_2^{e_2} \times \dots \times p_k^{e_k}$, the total number of positive factors $d(N)$ is calculated by adding $1$ to each exponent and multiplying them together:
   $$d(N) = (e_1 + 1)(e_2 + 1)\dots(e_k + 1)$$

   *Example for $N = 20 = 2^2 \times 5^1$:*
   $$d(20) = (2 + 1)(1 + 1) = 3 \times 2 = 6 \text{ factors}$$
   *(The factors are $\{1, 2, 4, 5, 10, 20\}$, which is exactly $6$ factors!)*

---

## 6. Step-by-Step Examples

### Example 1: Finding All Factors of $10$ (Easy)
**Task**: Find all factors of the number $10$.

**Step-by-step Solution**:
* **Step 1**: Start with $1$. Every number is divisible by $1$.
  $$10 \div 1 = 10 \implies (1, 10) \text{ are factors.}$$
* **Step 2**: Test $2$. Since $10$ ends in $0$, it is even and divisible by $2$.
  $$10 \div 2 = 5 \implies (2, 5) \text{ are factors.}$$
* **Step 3**: Test $3$.
  $$10 \div 3 = 3 \text{ remainder } 1 \implies 3 \text{ is not a factor.}$$
* **Step 4**: Test $4$.
  $$10 \div 4 = 2 \text{ remainder } 2 \implies 4 \text{ is not a factor.}$$
* **Step 5**: Check the halfway point. Half of $10$ is $\frac{10}{2} = 5$. We have reached $5$ in our pair $(2, 5)$. By our halfway rule, we can stop testing numbers between $5$ and $10$.
* **Conclusion**: The complete list of factors of $10$ is:
  $$\text{Factors of } 10 = \{1, 2, 5, 10\}$$

---

### Example 2: Finding All Factors of $20$ (Medium)
**Task**: Find all factors of the number $20$.

**Step-by-step Solution**:
* **Step 1**: Test $1$: $20 \div 1 = 20 \implies$ Pair: $(1, 20)$
* **Step 2**: Test $2$: $20 \div 2 = 10 \implies$ Pair: $(2, 10)$
* **Step 3**: Test $3$: $20 \div 3 = 6 \text{ remainder } 2 \implies 3$ is not a factor.
* **Step 4**: Test $4$: $20 \div 4 = 5 \implies$ Pair: $(4, 5)$
* **Step 5**: Test $5$: We already found $5$ paired with $4$. Since $5$ is right next to $4$, we have checked all possibilities up to half of $20$ ($\frac{20}{2} = 10$).
* **Conclusion**: Arranging the factors in ascending order gives:
  $$\text{Factors of } 20 = \{1, 2, 4, 5, 10, 20\}$$

---

### Example 3: Prime Factorization of $36$ (Medium)
**Task**: Find the prime factorization of $36$.

**Step-by-step Solution**:
* **Step 1**: Find any pair of factors for $36$. Let us pick $4 \times 9$:
  $$36 = 4 \times 9$$
* **Step 2**: Check if $4$ and $9$ are prime.
  * $4$ is composite because $4 = 2 \times 2$.
  * $9$ is composite because $9 = 3 \times 3$.
* **Step 3**: Substitute the prime factors back into the product:
  $$36 = (2 \times 2) \times (3 \times 3)$$
* **Step 4**: Check that all remaining factors are prime numbers:
  * $2$ is prime.
  * $3$ is prime.
* **Step 5**: Write the final result using exponents:
  $$36 = 2^2 \times 3^2$$

---

### Example 4: Prime Factorization of $90$ (Challenging)
**Task**: Find the prime factorization of $90$ using the Division Method (Ladder Method).

**Step-by-step Solution**:
We repeatedly divide $90$ by the smallest possible prime numbers ($2, 3, 5, \dots$):

1. Divide $90$ by prime number $2$:
   $$90 \div 2 = 45$$
2. $45$ is odd, so it cannot be divided by $2$. Test prime number $3$:
   Sum of digits of $45$: $4 + 5 = 9$ (divisible by $3$).
   $$45 \div 3 = 15$$
3. Divide $15$ by prime number $3$:
   $$15 \div 3 = 5$$
4. $5$ is a prime number. Divide $5$ by $5$:
   $$5 \div 5 = 1$$
5. We reached $1$, so the division is complete.

Collect all the prime divisors used: $2, 3, 3, 5$.
$$\text{Prime Factorization of } 90 = 2 \times 3 \times 3 \times 5 = 2 \times 3^2 \times 5$$

---

## 7. Visual Explanations

### 7.1 Factor Tree Diagram for $36$

A factor tree is a helpful visual diagram used to break down a composite number into its prime factors.

```
                   36
                  /  \
                 4    9
                / \  / \
               2   2 3  3   <-- All bottom numbers are Prime!
```

$$\text{Final Prime Factorization: } 36 = 2 \times 2 \times 3 \times 3 = 2^2 \times 3^2$$

---

### 7.2 Factor Tree Diagram for $90$ (Two Different Paths)

This diagram shows visually how two different initial choices lead to the exact same prime building blocks (Fundamental Theorem of Arithmetic):

```
        Path 1: Starting with 9 x 10                 Path 2: Starting with 30 x 3

                     90                                           90
                    /  \                                         /  \
                   9    10                                     30    3 (Prime)
                  / \   / \                                   /  \
                 3   3 2   5                                 10   3 (Prime)
                (All Primes!)                               /  \
                                                           5    2
                                                         (All Primes!)

   Result: 2 * 3 * 3 * 5 = 2 * 3^2 * 5          Result: 5 * 2 * 3 * 3 = 2 * 3^2 * 5
```

---

### 7.3 Number Line of First 25 Whole Numbers

The chart below shows prime numbers (circled/bold) versus composite numbers and $1$:

```
 Number | Category     | Factors
--------------------------------------------
   1    | Neither      | {1}
   2    | Prime (Even) | {1, 2}
   3    | Prime        | {1, 3}
   4    | Composite    | {1, 2, 4}
   5    | Prime        | {1, 5}
   6    | Composite    | {1, 2, 3, 6}
   7    | Prime        | {1, 7}
   8    | Composite    | {1, 8}
   9    | Composite    | {1, 3, 9}
  10    | Composite    | {1, 2, 5, 10}
  11    | Prime        | {1, 11}
  12    | Composite    | {1, 2, 3, 4, 6, 12}
  13    | Prime        | {1, 13}
  14    | Composite    | {1, 2, 7, 14}
  15    | Composite    | {1, 3, 5, 15}
  16    | Composite    | {1, 2, 4, 8, 16}
  17    | Prime        | {1, 17}
  18    | Composite    | {1, 2, 3, 6, 9, 18}
  19    | Prime        | {1, 19}
  20    | Composite    | {1, 2, 4, 5, 10, 20}
```

---

## 8. Common Mistakes

Here are frequent errors students make when learning about divisibility and prime numbers, along with explanations of how to avoid them:

### Mistake 1: Classifying $1$ as a Prime Number
* ❌ **Wrong thinking**: "$1$ is only divisible by $1$ and itself, so it must be prime."
* ✅ **Correct understanding**: A prime number **must have exactly two distinct positive factors**. $1$ has only one factor ($1$). Therefore, $1$ is neither prime nor composite.

---

### Mistake 2: Thinking All Odd Numbers Are Prime
* ❌ **Wrong thinking**: "Since even numbers are divisible by $2$, all odd numbers must be prime."
* ✅ **Correct understanding**: Odd numbers cannot be divided by $2$, but they might be divisible by other numbers like $3, 5, 7, \dots$ For example, $9, 15, 21, 25, 27$ are all odd, but they are composite numbers.

---

### Mistake 3: Believing $2$ Is Not Prime Because It Is Even
* ❌ **Wrong thinking**: "Even numbers can be divided by $2$, so no even number can be prime."
* ✅ **Correct understanding**: $2 \div 2 = 1$ and $2 \div 1 = 2$. Its only factors are $1$ and $2$. That satisfies the definition of a prime number perfectly! $2$ is the **only** even prime number.

---

### Mistake 4: Stopping Prime Factorization Too Early
* ❌ **Wrong thinking**: "The prime factorization of $20$ is $4 \times 5$."
* ✅ **Correct understanding**: $4$ is not a prime number ($4 = 2 \times 2$). You must continue factoring until **every single number** in the multiplication is prime:
  $$20 = 2 \times 2 \times 5 = 2^2 \times 5$$

---

### Mistake 5: Thinking Different Factor Trees Give Different Prime Factors
* ❌ **Wrong thinking**: "If I start factoring $36$ as $6 \times 6$, I will get a different answer than starting with $4 \times 9$."
* ✅ **Correct understanding**: According to the **Fundamental Theorem of Arithmetic**, every composite number has only **one unique set** of prime factors. No matter how you start, $36$ will always factor into $2^2 \times 3^2$.

---

## 9. Practice Problems

Test your understanding with these practice problems arranged from easy to challenging. Try solving them on your own before looking at the solutions!

### Easy Level
1. Is the number $15$ prime or composite? List all of its factors to prove your answer.
2. Is the number $29$ prime or composite? Explain why.
3. List all factors of the number $12$.

### Medium Level
4. Find the prime factorization of $24$ using a factor tree or repeated division. Write your final answer using exponents.
5. Find the prime factorization of $48$.
6. Using the total factors formula $d(N) = (e_1 + 1)(e_2 + 1)\dots$, calculate how many total factors the number $36$ has.

### Challenging Level
7. A number $N$ has the prime factorization $N = 2^3 \times 3^1 \times 5^2$.
   a) What is the value of the number $N$?
   b) How many total positive factors does $N$ have?
   c) Is $N$ divisible by $15$? Explain why using its prime factors.
8. Find the prime factorization of $180$. Show step-by-step reasoning.

---

## 10. Solutions

### Solution to Problem 1
* **Question**: Is $15$ prime or composite? List all of its factors.
* **Step-by-step Reasoning**:
  * $15 \div 1 = 15 \implies (1, 15)$
  * $15 \div 2 = 7 \text{ remainder } 1 \implies 2$ is not a factor.
  * $15 \div 3 = 5 \implies (3, 5)$
  * Factors of $15 = \{1, 3, 5, 15\}$.
* **Answer**: Since $15$ has $4$ factors (more than $2$), $15$ is a **composite number**.

---

### Solution to Problem 2
* **Question**: Is $29$ prime or composite? Explain why.
* **Step-by-step Reasoning**:
  * Test prime divisors up to $\sqrt{29} \approx 5.38$:
    * $29 \div 2 = 14 \text{ remainder } 1$
    * $29 \div 3 = 9 \text{ remainder } 2$
    * $29 \div 5 = 5 \text{ remainder } 4$
  * No prime numbers divide $29$ evenly.
* **Answer**: $29$ has only two positive factors: $1$ and $29$. Therefore, $29$ is a **prime number**.

---

### Solution to Problem 3
* **Question**: List all factors of $12$.
* **Step-by-step Reasoning**:
  * $12 \div 1 = 12 \implies (1, 12)$
  * $12 \div 2 = 6 \implies (2, 6)$
  * $12 \div 3 = 4 \implies (3, 4)$
* **Answer**: The factors of $12$ are $\{1, 2, 3, 4, 6, 12\}$.

---

### Solution to Problem 4
* **Question**: Find the prime factorization of $24$.
* **Step-by-step Reasoning**:
  * Split $24$ into $4 \times 6$.
  * Factor $4$: $4 = 2 \times 2$.
  * Factor $6$: $6 = 2 \times 3$.
  * Combine factors: $24 = 2 \times 2 \times 2 \times 3$.
* **Answer**: In exponential form:
  $$24 = 2^3 \times 3^1$$

---

### Solution to Problem 5
* **Question**: Find the prime factorization of $48$.
* **Step-by-step Reasoning**:
  * $48 = 6 \times 8$
  * $6 = 2 \times 3$
  * $8 = 2 \times 2 \times 2$
  * Combine: $48 = 2 \times 3 \times 2 \times 2 \times 2 = 2 \times 2 \times 2 \times 2 \times 3$.
* **Answer**: In exponential form:
  $$48 = 2^4 \times 3^1$$

---

### Solution to Problem 6
* **Question**: How many total factors does $36$ have?
* **Step-by-step Reasoning**:
  * First, write the prime factorization of $36$:
    $$36 = 2^2 \times 3^2$$
  * Identify exponents: $e_1 = 2$, $e_2 = 2$.
  * Apply the formula $d(N) = (e_1 + 1)(e_2 + 1)$:
    $$d(36) = (2 + 1)(2 + 1) = 3 \times 3 = 9$$
* **Answer**: $36$ has **$9$ total factors**.
  *(Verification: Factors of $36$ are $\{1, 2, 3, 4, 6, 9, 12, 18, 36\}$, which is exactly $9$ numbers!)*

---

### Solution to Problem 7
* **Question**: $N = 2^3 \times 3^1 \times 5^2$.
  a) Find $N$.
  b) Total factors of $N$.
  c) Is $N$ divisible by $15$?
* **Step-by-step Reasoning**:
  * **a)** $N = 8 \times 3 \times 25 = 24 \times 25 = 600$.
  * **b)** Exponents are $e_1 = 3, e_2 = 1, e_3 = 2$.
    $$d(N) = (3 + 1)(1 + 1)(2 + 1) = 4 \times 2 \times 3 = 24 \text{ factors.}$$
  * **c)** The prime factorization of $15$ is $3 \times 5$. Since $N$ contains at least one $3$ ($3^1$) and at least one $5$ ($5^2$), we can factor out $15$:
    $$N = (3 \times 5) \times (2^3 \times 5^1) = 15 \times 40$$
* **Answer**:
  a) $N = 600$
  b) $N$ has $24$ positive factors.
  c) Yes, $N$ is divisible by $15$ because its prime factors contain $3 \times 5$.

---

### Solution to Problem 8
* **Question**: Prime factorization of $180$.
* **Step-by-step Reasoning**:
  * Divide by $2$: $180 \div 2 = 90$
  * Divide by $2$: $90 \div 2 = 45$
  * Divide by $3$: $45 \div 3 = 15$
  * Divide by $3$: $15 \div 3 = 5$
  * Divide by $5$: $5 \div 5 = 1$
* **Answer**:
  $$180 = 2 \times 2 \times 3 \times 3 \times 5 = 2^2 \times 3^2 \times 5^1$$

---

## 11. Summary

* **Divisibility**: One number is divisible by another if dividing them results in a whole number with zero remainder ($r = 0$).
* **Factors**: Numbers you multiply together to get another number. To find all factors of $N$, test divisors up to $\frac{N}{2}$.
* **Prime Numbers**: Whole numbers greater than $1$ with exactly two factors: $1$ and itself ($2, 3, 5, 7, 11, \dots$).
* **Composite Numbers**: Whole numbers greater than $1$ with three or more factors ($4, 6, 8, 9, 10, \dots$).
* **The Special Cases**:
  * $1$ is **neither** prime nor composite.
  * $2$ is the **only** even prime number.
* **Prime Factorization**: Breaking a composite number down until it is expressed purely as a product of prime numbers.
* **Fundamental Theorem of Arithmetic**: Every composite number has a single, unique prime factorization, regardless of the order or method used to find it.

---

## 12. Key Things to Remember

1. **Prime Check Rule**: A prime number has **exactly 2 factors** ($1$ and itself).
2. **Even Primes**: $2$ is the smallest prime number and the only even prime.
3. **Number 1 Exception**: $1$ is NOT prime because it only has $1$ factor.
4. **Odd Primes Caution**: Not all odd numbers are prime (e.g., $9, 15, 21, 25$ are composite).
5. **Prime Factorization Format**: Express final prime factorizations using exponents in increasing prime order:
   $$N = 2^a \times 3^b \times 5^c \times \dots$$
6. **Total Factor Formula**: If $N = p_1^{e_1} \times p_2^{e_2} \times \dots$, total factor count is:
   $$d(N) = (e_1 + 1)(e_2 + 1)\dots(e_k + 1)$$
7. **Unique Fingerprint**: The Fundamental Theorem of Arithmetic guarantees that every number has only **one unique prime factorization**.
