# Math Learning — Progress Log

> This file is my long-term memory of what we've covered. I READ it at the start of every
> session and UPDATE it at the end. Newest entries at the top of the Session Log.

## Skill Ledger

*(A skill enters this list only after the exercises are done and checked.)*

**Pending confirmation — taught in session 1, waiting for the 20 exercises of
`notebooks/01-real-numbers.ipynb`:**

- Classify a number as natural / integer / rational / irrational / real
- Read and write set notation, set-builder notation, interval notation
- Absolute value and distance on the number line
- Convert a repeating decimal to a fraction, and a fraction to a decimal
- Name the axioms of $\mathbb{R}$ and use them to justify a step
- Follow a proof by contradiction and a proof by contrapositive

**Pending confirmation — taught in session 2, waiting for the 20 exercises of
`notebooks/02-algebra-essentials.ipynb`:**

- Read an algebraic expression: terms, factors, coefficients, like terms
- Evaluate an expression at a value (always substituting with brackets)
- Find the domain of a variable (zero denominators, negative inside a square root)
- Tell an identity from an equation
- Use the laws of integer exponents, and say *why* $a^0=1$ and $a^{-n}=1/a^n$
- Understand and write a **proof by induction** (new technique this session)
- Use the principal square root correctly, especially $\sqrt{a^2}=|a|$
- Simplify square roots with $\sqrt{ab}=\sqrt a\sqrt b$
- Read, write and calculate with scientific notation
- SymPy basics: `symbols`, `subs`, `expand`, `simplify`, `sqrt`, `solve`, `denom`,
  and why symbol assumptions (`positive=True`) change what SymPy is allowed to do

## Current Focus

**Review § 2 — Algebra Essentials.** Notebook `notebooks/02-algebra-essentials.ipynb` is
built and runs top to bottom. Waiting for its 20 exercises.

Notebook 01's 20 exercises are **also still unmarked** — mark those first next session.

Next topic once he says "continue": **Review § 3 — Geometry Essentials**
(→ `notebooks/03-geometry-essentials.ipynb`).

## Known Weak Spots

*(Still nothing confirmed — no exercise answers have come back yet.)*

Things to watch for when the answers arrive:

From notebook 01:
- Ex 1–2: does he think $\sqrt{9}$ is irrational? Is $0$ counted as natural?
- Ex 8: the two-powers-of-ten subtraction trick, when the block does not start right
  after the decimal point.
- Ex 17–20: writing a real proof (naming the rule for every step) instead of just
  describing the idea.

From notebook 02:
- Ex 6: the classic sign traps — $-4^2$ against $(-4)^2$, and $-4^0$ against $(-4)^0$.
- Ex 8: does he drop the absolute value bars in $\sqrt{(x-5)^2}$? (This is the single
  most common mistake in the whole topic.)
- Ex 15: does he still believe any of the "distributing a power over a $+$" myths?
- Ex 17: is his induction a *real* induction — base case, inductive hypothesis stated
  clearly, and the step actually using the hypothesis — or just a re-statement?
- Ex 20: does he see that he must ALSO prove $\sqrt6$ is irrational, not just assume it?

## Session Log

### Session 2 — 2026-08-19 — Algebra Essentials

- **Topic taught:** Review § 2, Algebra Essentials (second topic in `math-topic.md`).
- **Notebook created:** `notebooks/02-algebra-essentials.ipynb` — 67 cells, 18 code cells,
  9 matplotlib figures, no ASCII art. Verified: executes top to bottom with no errors
  (`uv run jupyter nbconvert --to notebook --execute`). No new dependency needed.
- **What is inside:**
  - Intuition: a letter is a box; an expression is a *recipe*, an equation is a *question*.
  - Definitions: expression, term, factor, coefficient, like terms, evaluating,
    domain of a variable, identity vs equation, natural power (recursive), $a^0$,
    $a^{-n}$, principal square root, scientific notation.
  - **New proof technique: mathematical induction**, introduced with the line-of-dominoes
    picture and the formal principle (base case + inductive step).
  - Theorems, all fully proved: Thm 1–3 (the three exponent laws for naturals, by
    induction), Lemma 1 ($a^{-k}=1/a^k$ for every integer $k$), Thm 4 (product law for
    **all integers**, all four sign cases checked), Cor 5 (quotient law), Thm 6 (the
    remaining laws for integers), Lemma 2 (a non-negative square root is unique),
    Thm 7 (existence of square roots, from the **completeness axiom** via $\sup$ —
    marked "optional on a first read"), Thm 8 ($\sqrt{a^2}=|a|$), Thm 9
    ($\sqrt{ab}=\sqrt a\sqrt b$).
  - Motivated $a^0=1$ and $a^{-n}=1/a^n$ as *forced* by the product law, not invented;
    explained why $0^0$ stays undefined.
  - Traps given their own section: $-3^2$ vs $(-3)^2$, $(a+b)^2\ne a^2+b^2$ (with the
    area-square picture), $\sqrt{a+b}\ne\sqrt a+\sqrt b$ (with a graph).
  - Worked examples 1–7: evaluate, collect like terms, domain, exponent simplification,
    root simplification, root with a letter, scientific-notation arithmetic.
  - Python: SymPy `subs`/`expand`/`simplify`, exponent laws checked on random NumPy
    numbers *and* proved symbolically, the `sqrt(x**2)` assumption demo, exact root
    simplification, domain finding with `denom` + `solve` + `try/except`, scientific
    notation both directions with `log10`/`floor`.
  - 9 figures: expression-as-machine, the undefined point of $1/(x-2)$, factor boxes
    ($a^2\cdot a^3=a^5$), dominoes for induction, powers of 2 on a log axis, the
    $(a+b)^2$ area square, the sideways parabola + $y=\sqrt a$, $\sqrt{x^2}$ vs $x$,
    and 36 orders of magnitude on a log axis.
- **What went well:** nothing to judge yet — he has not sent answers for notebook 01 or 02.
- **Mistakes to revisit:** none recorded yet (still no answers).
- **Homework given:** the 20 exercises in notebook 02. Exercises 11–13 are Python;
  17–20 are proofs (induction for $a^n<b^n$; $a<b\Rightarrow\sqrt a<\sqrt b$;
  $\sqrt{a+b}<\sqrt a+\sqrt b$; and $\sqrt2+\sqrt3$ is irrational).
- **Next session plan:** (1) mark notebook 01's exercises, then notebook 02's;
  (2) quiz him out loud on: why $a^0$ *must* be 1, why $\sqrt{x^2}=|x|$, and what the two
  halves of an induction proof are; (3) only then teach **Geometry Essentials**.

### Session 1 — 2026-08-19 — Real Numbers

- **Topic taught:** Review § 1, Real Numbers (the first topic in `math-topic.md`).
- **Notebook created:** `notebooks/01-real-numbers.ipynb` — 68 cells, 22 code cells,
  8 matplotlib figures, no ASCII art. Verified: executes top to bottom with no errors
  (`uv run jupyter nbconvert --to notebook --execute`).
- **What is inside:**
  - Intuition: numbers as points on a line; why each new kind of number was invented.
  - Definitions: sets and set-builder notation; $\mathbb{N}, \mathbb{Z}, \mathbb{Q},
    \mathbb{I}, \mathbb{R}$; decimal forms; order; absolute value and distance; intervals;
    the field axioms, the order axioms, and the completeness axiom.
  - Theorems, all fully proved: Lemma 1 (inverses are unique), A ($a\cdot0=0$),
    B (zero-product), C (sign rules, incl. why minus times minus is plus),
    D (rational $\iff$ terminating/repeating decimal, via pigeonhole),
    E ($\sqrt2$ is irrational), F (triangle inequality),
    G (density of $\mathbb{Q}$ in $\mathbb{R}$, via the Archimedean property).
  - Worked examples: classification, repeating decimal → fraction, order of operations,
    absolute-value equations and inequalities, where an expression is undefined.
  - Python: a pure-Python `long_division` function, SymPy exact arithmetic
    (`Rational`, `sqrt`, `is_rational`, `nsimplify`, `factorint`), the terminating-decimal
    experiment, and 8 figures (number line, nested sets, intervals, remainder cycle,
    $\sqrt2$ approximation error, triangle inequality, $|x|$ graph, density zoom).
  - **What went well:** first session — nothing to judge yet.
  - **Mistakes to revisit:** none recorded yet.
  - **Homework given:** all 20 exercises in the notebook (the last four are proofs:
    rational + irrational is irrational; $\sqrt3$ is irrational; $(-1)a=-a$ and the
    cancellation law from the axioms only; an irrational number sits between any two reals).
  - **Next session plan:** quiz him on Theorem D and Theorem E in his own words, mark the
    20 exercises, record real weak spots, then teach **Algebra Essentials**.
