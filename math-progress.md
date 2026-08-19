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

## Current Focus

**Review § 1 — Real Numbers.** Notebook `notebooks/01-real-numbers.ipynb` is built and
runs top to bottom. Waiting for the 20 exercises to be attempted.

Next topic once he says "continue": **Review § 2 — Algebra Essentials**
(→ `notebooks/02-algebra-essentials.ipynb`).

## Known Weak Spots

*(Nothing recorded yet — no exercise answers have come back. Fill in from Exercises 1–20.)*

Things to watch for when the answers arrive:
- Ex 1–2: does he think $\sqrt{9}$ is irrational? Is $0$ counted as natural?
- Ex 8: the two-powers-of-ten subtraction trick, when the block does not start right
  after the decimal point.
- Ex 17–20: writing a real proof (naming the rule for every step) instead of just
  describing the idea.

## Session Log

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
