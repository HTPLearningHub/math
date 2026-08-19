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

**Pending confirmation — taught in session 3, waiting for the 20 exercises of
`notebooks/03-geometry-essentials.ipynb`:**

- Name and use the basic objects: point, segment, ray, angle, and the degree
- Classify angles (acute / right / obtuse / straight, complementary, supplementary) and
  triangles (by sides and by angles)
- State the small axiom list of Euclidean geometry (G1–G5 + the area assumption) and say
  which axiom or theorem a step uses
- Prove and use the angle sum of a triangle, and the area $\tfrac12 bh$
- State, prove and apply the **Pythagorean theorem** (two area-rearrangement proofs)
- State, prove and apply its **converse**, including the acute / obtuse refinement
- Recognise Pythagorean triples
- Prove and use **Thales' basic proportionality theorem** and the **AA similarity test**
- Use the scaling rule: lengths $\times k$, areas $\times k^2$, volumes $\times k^3$
- Explain what $\pi$ *is* — a ratio that similarity proves is the same for every circle —
  and why the area of a disk is $\pi r^2$
- The $45$-$45$-$90$ and $30$-$60$-$90$ triangles, derived and not memorised
- The **distance formula**, and that it is Pythagoras in disguise
- Volume and surface formulas for box, cylinder, sphere, cone — and which of them we have
  actually proved
- New habit: telling a proved statement from an assumed one, and spotting where a **limit**
  is hiding (the first calculus-shaped reasoning in the course)
- Numerical lesson: two algebraically identical formulas can behave very differently in
  floating point (catastrophic cancellation)

## Current Focus

**Review § 3 — Geometry Essentials.** Notebook `notebooks/03-geometry-essentials.ipynb` is
built and verified: it runs top to bottom with no errors. Waiting for its 20 exercises.

**The exercises of notebooks 01 and 02 are still unmarked too** — three sets of homework are
now outstanding. Next session, mark them oldest first. Do not teach a fourth topic before at
least notebooks 01 and 02 are marked, otherwise the weak-spot list stays empty and the
teaching is blind.

Next topic once he says "continue": **Review § 4 — Polynomials**
(→ `notebooks/04-polynomials.ipynb`).

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

From notebook 03:
- Ex 4: does he test the **longest** side as the hypotenuse, or just the last number given?
- Ex 8: the classic $k$ vs $k^2$ vs $k^3$ confusion (pizza, map area, model weight).
- Ex 10(b): does he compare with the *longest* side squared, and does he keep values exact
  instead of rounding first?
- Ex 16 (rope round the Earth): does he trust the algebra when the answer feels impossible?
- Ex 17–20: real proofs — naming the axiom or theorem for every step — or just descriptions?
  Ex 19 is the first proof where he must *choose* which similar triangles to compare, and
  Ex 20 asks him to compare two proofs of one theorem, which is new.
- Watch for the congruent (same size) vs similar (same shape) mix-up.
- Watch whether he treats "assumed" and "proved" as the same thing.

## Session Log

### Session 3 — 2026-08-19 — Geometry Essentials

- **Topic taught:** Review § 3, Geometry Essentials (third topic in `math-topic.md`).
- **Notebook created:** `notebooks/03-geometry-essentials.ipynb` — 105 cells, 30 code cells,
  21 matplotlib figures, no ASCII art. Verified: executes top to bottom with no errors
  (`uv run jupyter nbconvert --to notebook --execute`). No new dependency needed — numpy,
  sympy and matplotlib only.
- **What is inside:**
  - Intuition: geometry = measuring shapes (how long / how much flat space / how much room
    inside); an angle is *turning*, not a corner; the length of the rays does not change it.
  - Definitions 1–14: segment / ray / length with the $\overline{AB}$ vs $AB$ vs $m\angle$
    notation, angle names, perpendicular and parallel, the triangle families, the parts of a
    right triangle, polygon and perimeter, **area given as three rules** (unit / adding /
    moving) instead of hand-waving, volume, circle vocabulary, similar triangles,
    parallelogram.
  - The axiom list is stated **explicitly** (G1–G5 + Assumption A) so he can always answer
    "what am I allowed to use here?".
  - Theorems, all fully proved: warm-up (vertical angles); Thm 1 (angle sum, via the parallel
    line through the apex); Thm 2 ($\tfrac12 bh$, all three cases including the obtuse one)
    with Corollaries 2a and 2b; Thm 3 (**Pythagoras**, by rearranging areas, plus a second
    rearrangement in the same figure); Thm 4 (**converse**, by building a right triangle and
    using SSS together with the uniqueness of the non-negative square root from notebook 02);
    Lemma 5 (parallelogram); Thm 5 (**Thales**, proved with areas); Thm 6 (**AA similarity**,
    with the full construction); Thm 7 (scaling: $k$, $k^2$, $k^3$); Lemma 6 (isosceles base
    angles); Thm 8 ($\pi$ is the same number for every circle — proved with similar
    polygons); Thm 9 (disk area, by rearranging sectors); Thm 10 (the $45$-$45$-$90$ and
    $30$-$60$-$90$ triangles); Thm 11 (**distance formula**).
  - Honesty notes wherever a **limit** is used (Thm 8, Thm 9, cylinder volume), plus an
    explicit list of what is still owed: sphere and cone volume, and that $\pi$ is
    irrational. The notebook ends with a table of every result and what it depends on.
  - Worked examples 1–7: the ladder; converse tests including the acute / obtuse refinement;
    a 16:9 television; the height of a tree from its shadow; a composite window area with the
    "the cut line is not part of the frame" trap; coordinates — where **Example 6 contains a
    deliberately false claim** ("show that these three points form a right triangle") so he
    sees that the honest answer is sometimes "no, and here is why"; and a drink can, ending
    with an optimisation teaser for calculus.
  - Python: exact roots with SymPy; a triangle classifier built on the converse; a
    Pythagorean-triple hunt; SymPy re-deriving Pythagoras from the area equation;
    **Archimedes' method for $\pi$ using only square roots**, with the doubling formula
    derived from Pythagoras; the unstable vs stable version of that formula (catastrophic
    cancellation, shown on a log-scale error plot — his first numerical-analysis lesson);
    Monte Carlo $\pi$; the shoelace formula confirming the $k^2$ scaling rule; and the
    distance formula.
  - 21 figures: the four basic objects; kinds of angle; kinds of triangle; the parts of a
    circle; alternate angles; the angle-sum proof; the three cases of the area proof; the
    Pythagoras rearrangement (both packings side by side); the classic 3–4–5 squares picture;
    the converse construction; similar triangles; the Thales areas; the AA construction with
    its parallelogram; the pizza-slice limit at $n=6,12,24,60$; the two special triangles;
    the distance formula on a grid; the three solids in 3D; the ladder and the window; and
    the three Python plots.
- **What went well:** nothing to judge yet — still no answers from him for notebooks 01, 02
  or 03.
- **Mistakes to revisit:** none recorded yet (still no answers).
- **Homework given:** the 20 exercises in notebook 03. Exercises 11–13 are Python (an exact
  triangle classifier that also handles $\sqrt2$, primitive triples up to 100, and a Monte
  Carlo estimate of the window's area). Exercises 17–20 are proofs: the hypotenuse is the
  longest side; the diagonals of a rhombus are perpendicular; the altitude to the hypotenuse
  creates three similar triangles, giving $h^2=pq$, $b^2=cp$, $a^2=cq$; and finally
  **proving Pythagoras a second time from similarity**, then comparing what the two proofs
  each depend on.
- **Next session plan:** (1) mark notebook 01, then 02, then 03 — three sets are outstanding;
  (2) quiz him out loud on: why the angles of a triangle add to $180^\circ$, what a *converse*
  is and why it needs its own proof, the difference between congruent and similar, and what
  $\pi$ actually *is*; (3) only then teach **Polynomials**.

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
