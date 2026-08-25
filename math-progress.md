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

**Pending confirmation — taught in session 4, waiting for the 20 exercises of
`notebooks/04-polynomials.ipynb`:**

- Say what a polynomial is (only $+,-,\times$) and give the exact reason why $1/x$,
  $\sqrt{x}$, $x^{-2}$ and $2^{x}$ are not polynomials
- Degree, leading coefficient, constant term, standard form; why the zero polynomial gets
  no degree
- Add, subtract and multiply polynomials; the coefficient formula
  $c_{k}=\sum_i a_i b_{k-i}$ (and that it is called a *convolution*)
- $\deg(pq)=\deg p+\deg q$ and $\deg(p+q)\le\max$ — and why the second is only $\le$
- The special products (i)–(vii), each proved, plus the general
  $a^{n}-b^{n}$ telescoping identity
- **Polynomial long division** by hand, and the division algorithm with its *uniqueness*
- **Remainder theorem** and **factor theorem**, and using them instead of dividing
- "Degree $n$ $\Rightarrow$ at most $n$ real roots", proved by induction
- **Identity theorem**: equal as functions $\iff$ equal as coefficient lists — so
  "comparing coefficients" is now a proved move, not a habit
- Factorials, binomial coefficients, Pascal's rule, and the **binomial theorem** proved by
  induction (second induction proof of the course)
- Horner's method for evaluation (and that it is next topic's "synthetic division")
- SymPy: `expand`, `factor`, `degree`, `Poly.all_coeffs`, `div`, `rem`, `solve`, `binomial`
- Second numerical-analysis lesson: catastrophic cancellation in $(x-1)^7$ expanded

**Pending confirmation — taught in session 5, waiting for the 20 exercises of
`notebooks/05-factoring-polynomials.ipynb`:**

- Say what factoring *is* (un-multiplying) and why the factored form is the useful form
- Use the five-step factoring checklist: GCF → count the terms → pattern → rational roots →
  check every bracket again → multiply back
- The vocabulary of factoring: unit, trivial factorisation, **irreducible**, completely
  factored, content/GCF, monic, **multiplicity**, quadratic in form
- Understand that irreducibility depends on the number system ($\mathbb{Q}$ vs $\mathbb{R}$
  vs $\mathbb{C}$), and name it out loud before answering
- Factor by GCF, by grouping, by the special products backwards, by the trinomial rule, and
  by the **$ac$ method** — each one proved, not memorised
- **Completing the square** and the **discriminant** $D=b^2-4ac$; prove that a real
  quadratic is irreducible exactly when $D<0$
- **Rational root theorem**, with a full proof — including **Bézout's identity** proved from
  the well-ordering principle, and the coprime-powers lemma proved with the binomial theorem
- Corollary: a rational root of a *monic* integer polynomial is an integer — an irrationality
  machine ($\sqrt[3]{2}$, $\sqrt7$)
- The general factoring algorithm: find a rational root, peel it off, repeat, stop at degree 2
- **Unique factorisation for polynomials** (the summit), via polynomial Bézout and Euclid's
  lemma — and the big analogy: degree plays the role of size, irreducibles play the role of
  primes
- Sign charts: solve a polynomial inequality by factoring and checking each bracket
- New habit: the "multiply back" check, and the "put $x=1$" fast check
- SymPy: `factor`, `factor_list`, `expand`, `extension=`, `gaussian=`, and comparing two
  expressions by **subtracting and simplifying to zero**
- Third numerical-analysis lesson: **ill-conditioning** — Wilkinson's polynomial, where a
  $10^{-9}$ change in one coefficient throws roots off the real line

**Pending confirmation — taught in session 6, waiting for the 20 exercises of
`notebooks/06-synthetic-division.ipynb`:**

- Run a synthetic division table by hand: bring down, multiply by $c$, add — and read the
  quotient and the remainder out of the bottom row
- Say *why* it works: it is long division with the letters deleted, and the recurrence
  $b_{k-1}=a_k+c\,b_k$ is **forced** by "compare coefficients", not chosen
- The two habits that stop most wrong answers: write a $0$ for every missing power, and read
  the divisor as "$x$ **minus** something" to get the sign of $c$
- Use the table as a fast evaluator (remainder theorem) and as a fast factor test (factor
  theorem)
- Know that synthetic division and **Horner's method are the same loop** — Horner throws the
  quotient away
- Cost: exactly $n$ multiplications against about $n^2/2$ for the naive method (linear vs
  quadratic)
- **Deflation**: peel a root off and repeat; count how many zero remainders in a row to get
  the **multiplicity**
- Divide by a non-monic linear $ax-b$: use $c=b/a$, then divide the *quotient* (never the
  remainder) by $a$
- Rewrite a polynomial in **powers of $(x-c)$** by repeated synthetic division — the
  remainders are the coefficients (the algebraic skeleton of a Taylor expansion)
- **Upper and lower bound theorems**: one table with all-non-negative row, or one with an
  alternating row, fences all real roots into a finite interval
- Python: writing the algorithm from the definition, testing it against SymPy on 200 random
  cases, exact `Fraction` arithmetic, and a full rational-root factoriser built from
  deflation
- Fourth numerical-analysis lesson: **deflation order matters** — peeling the largest root
  first amplifies rounding error by $|c|$ per step ($10^{12}$ worse in the demo); peel the
  smallest first, and polish roots against the original polynomial

**Pending confirmation — taught in session 7, waiting for the 20 exercises of
`notebooks/07-rational-expressions.ipynb`:**

- Say what a rational expression is, and see the big analogy: $\mathbb{Z}\to\mathbb{Q}$ is the
  same step as $\mathbb{R}[x]\to\mathbb{R}(x)$ (square brackets vs round brackets)
- **Domain**: find the forbidden values from the ORIGINAL expression, before cancelling, and
  carry the restrictions on every line of the answer
- Cancel a **factor**, never a **term** — and say exactly which hypothesis of the cancellation
  theorem fails in $\frac{x+3}{x}$
- The two meanings of "equal" (cross-multiplying vs agreeing as functions) and the theorem that
  they are the same
- Multiply, divide, add and subtract rational expressions; the reversed-bracket rule
  $a-b=-(b-a)$; the minus-sign-over-the-whole-numerator rule
- **LCD** by taking the highest power of each irreducible factor, and why that is the *least*
  common multiple
- Complex (compound) fractions, by both methods
- Split improper $\to$ polynomial part + proper part, using synthetic division from nb 06
- **Hole vs vertical asymptote (wall)**: reduce first, then look at the reduced bottom
- $\mathbb{R}(x)$ is a **field**; $\mathbb{R}[x]$ is not — the single axiom that differs is the
  reciprocal, and the price paid is the domain
- **Lowest terms exist and are unique up to a constant** (via Bezout + unique factorisation)
- **Lagrange interpolation**: exactly one polynomial of degree $\le n-1$ through $n$ points
- **Partial fractions** for distinct linear factors, with the **cover-up formula** proved (no
  system of equations needed)
- The **difference quotient** $\frac{f(x+h)-f(x)}{h}$, and why the $h$ cancelling is the trick
  that calculus is built on
- SymPy: `cancel`, `together`, `apart`, `factor_list`, `fraction`, `lcm`, `lambdify` — and the
  warning that `together` silently cancels and so silently changes the domain
- Plotting rational functions honestly with `np.nan` instead of letting matplotlib draw a fake
  vertical line
- Fifth numerical-analysis lesson: **simplifying the algebra makes the computation stable** —
  the raw difference quotient loses every digit as $h\to0$; the simplified form is exact

**Pending confirmation — taught in session 8, waiting for the 20 exercises of
`notebooks/08-nth-roots-rational-exponents.ipynb`:**

- Say what an $n$th root *is* (Def 1: any $t$ with $t^n=a$) and how the **principal** root
  (Def 2) picks one of them — and that the pick is a convention with a reason (keeps the root a
  function, keeps it increasing)
- The even/odd split: even index $\Rightarrow$ two roots or none; odd index $\Rightarrow$ exactly
  one, for every real number
- $\sqrt[n]{a^n}=|a|$ for even $n$, $=a$ for odd $n$ (nb 02 Thm 8, now general) — the bars trap,
  fifth appearance in the course
- Existence of $\sqrt[n]{a}$ proved from the **completeness axiom** by $\sup$, generalising nb 02
  Thm 7 from $n=2$ to every $n$; Lemma 1 (powers keep the order) and Lemma 2 (a power cannot
  jump) both proved from the nb 04 telescoping identity
- The **uniqueness pattern**: to prove two non-negative things are equal, raise both to the $n$th
  power and quote Corollary 1a — the same three lines prove Theorems 3–6 and 10–11
- Product, quotient, root-of-a-root and order laws for radicals, each with the hypothesis that
  makes it legal, and the exact place each one dies without it
- $\sqrt[n]{a+b}<\sqrt[n]a+\sqrt[n]b$ proved from the binomial theorem — not just "you cannot
  split over a plus", but *which way* the inequality goes
- AM–GM for two numbers, proved twice: by the semicircle picture (nb 03 similar triangles) and by
  $(\sqrt a-\sqrt b)^2\ge0$
- Simplest radical form; combining like radicals; rationalising a **denominator** (conjugate, and
  the cube-root version built from $u^3-v^3$) and a **numerator** (the difference quotient of
  $\sqrt x$ — second calculus teaser of the course)
- **Rational exponents**: the definition is *forced* by $(a^r)^s=a^{rs}$, not chosen;
  **Theorem 10 (well defined)** — why $a^{2/6}=a^{1/3}$ needs a proof, and why it is exactly the
  theorem that fails for $a<0$; Theorem 11 (all four exponent laws for rationals)
- Comparing roots with no calculator by raising to the lcm of the indices
- Un-nesting $\sqrt{7+4\sqrt3}=2+\sqrt3$, and why matching the rational and irrational parts is
  legal (irrationality of $\sqrt3$, nb 01)
- Domains of radical expressions: even root $\ge0$, and the extra strictness when the same
  expression is also a denominator
- The honest gap flagged out loud: $2^{\sqrt2}$ needs limits, so rational exponents are as far as
  we can go — the same kind of gap as the circle area (nb 03) and the asymptote (nb 07)
- Python: `**(1/n)` returning a **complex** number for a negative base, `np.cbrt` vs `np.sqrt`,
  `sp.root` vs **`sp.real_root`**, `sp.radsimp`, `sp.sqrtdenest`, `sp.refine(..., Q.real(x))` to
  get `Abs(x)` out of `sqrt(x**2)`, and the laws tested on 200 000 random cases before being
  proved symbolically
- Theorem 1's proof executed as **bisection**, then measured against **Newton's method**
  (41 steps vs 8 to reach $10^{-12}$) — the proof and the algorithm are the same idea
- Sixth numerical-analysis lesson: **catastrophic cancellation** in $\sqrt{x+1}-\sqrt x$ —
  100% relative error at $x=10^{16}$, cured completely by rationalising the numerator

**Pending confirmation — taught in session 9, waiting for the 20 exercises of
`notebooks/09-linear-equations.ipynb`:**

- The change of *kind*: notebooks 01–08 rewrote **objects**, this one answers a **question**.
  An expression is a recipe; an equation is a question; the answer is a **set**, never a number
- Definitions: equation in one variable, the **domain of the equation** ($D_L\cap D_R$),
  solution/root, solution set, identity vs contradiction vs conditional equation,
  **equivalent equations** (same solution set — not "looks alike"), linear equation $ax+b=0$
  with $a\neq0$ as a *definition*, and "an equation that leads to a linear equation"
- Solving as a **chain of equivalent equations**, each $\Longleftrightarrow$ a promise that the
  answer set did not change — not as "computing the answer"
- The two safe moves, proved by double inclusion from the nb 01 field axioms: **Theorem 1**
  (add any expression defined on all of $D$) and **Theorem 2** (multiply by a non-zero *number*),
  plus exactly where each hypothesis is used and what breaks without it
- **Theorem 3** (if $a\neq0$ then $ax+b=0$ has exactly one solution) proved as existence +
  uniqueness, uniqueness by the nb 08 three-line pattern and the zero-product property
- **Theorem 4** ($a=0$: nothing or everything) and **Theorem 5** (the trichotomy for
  $px+q=rx+s$) — so "one, none, or all" is a *theorem*, not an observation about pictures
- The two dangerous moves, both proved: **Theorem 6** ($S'=S\cup Z$ — multiplying by $E(x)$
  never loses a solution and adds exactly the zeros of $E$) and **Theorem 7** (dividing by
  $E(x)$ deletes them). **Corollary 6a**: "check your answer" is the second half of the proof
- **Corollary 6b**: squaring merges $L=R$ with $L=-R$ — the nb 08 Trap 7 debt, now paid
- Nine traps, including: cancelling a bracket containing $x$; deciding the domain *after* seeing
  the answer; checking in the wrong (already-cleared) equation; and reading $0=5$ as a mistake
  instead of as the answer $S=\varnothing$
- Worked technique: brackets, LCD with numeric denominators, decimals by $\times100$, rational
  equations with and without an extraneous root, an equation that only *looks* quadratic,
  **literal equations** (solve for a letter), a **parameter** equation whose three cases are
  exactly Theorem 5, and a first word problem with its hidden domain
- Python: `sp.Eq` vs `==`; **`sp.solveset` vs `sp.solve`** (a list cannot tell "no solution"
  from "every number"; a set can); `.subs` + `sp.simplify` as an exact checker; `sp.zoo` as
  "outside the domain"; `sp.cancel` to clear denominators by hand and watch the fake solution
  appear; Theorems 3–5 written out as his own `solve_linear`
- **Numerical-analysis lesson 7:** `(0.1+0.2)-0.3 = 5.55e-17`, fed in as the coefficient $a$,
  turns "no solution" into $x\approx1.8\times10^{16}$. Never test `a == 0` on floats; test
  against a tolerance. First meeting with **ill-conditioning** (nearly parallel lines), named
  as the thing that matters later for systems and for training networks

**Pending confirmation — taught in session 10, waiting for the 20 exercises of
`notebooks/10-quadratic-equations.ipynb`:**

- The step from $x^1$ to $x^2$: one side of the equation **bends**, so "exactly two solutions"
  — which nb 09 Theorem 5 forbade — becomes the normal case, and "every real number" disappears
- Definitions: quadratic equation $ax^2+bx+c=0$ with $a\neq0$ (again $a\neq0$ is *part of the
  definition*), the **discriminant** $D=b^2-4ac$, **double root / multiplicity 2**, parabola
- **Four methods, each proved, each a special case of the next:** factoring (Thm 1, straight from
  the nb 01 zero-product property), the **square-root property** (Thm 2, proved by difference of
  squares, with all three cases $p>0$, $p=0$, $p<0$), **completing the square** (Thm 3, proved as
  an identity and drawn as a literal square with a missing corner), and the **quadratic formula**
  (Thm 4, derived by the multiply-by-$4a$ route so no fractions appear until the last line)
- The formula understood as *what it is*: completing the square carried out once, with letters,
  so it never has to be done again
- **Theorem 5 (the discriminant theorem)** — two / one / none, fully proved, including *why* the
  two roots are distinct when $D>0$ and why $D=0$ gives a genuine double root
- **Theorem 6 (Vieta)** and **Theorem 7 (factorisation)** — so "factoring by inspection" is
  revealed as guessing the formula's answer quickly, and factoring is not a separate method
- **Theorem 8**: for integer coefficients, the roots are rational **iff** $D$ is a perfect square
  — proved via the nb 05 rational root theorem applied to $t^2-D$. Used as a *test*: do not hunt
  for a factorisation the theorem says cannot exist
- **Theorem 9** (the vertex identity, and $D<0\Rightarrow$ the quadratic keeps the sign of $a$)
  and **Theorem 10** (vertex / axis of symmetry, flagged as a preview but fully proved), plus the
  observation that the roots sit symmetrically about $x=-b/(2a)$
- Ten traps, including: zero-product used without a zero; dividing by $x$ (nb 09 Thm 7 again);
  the missing $\pm$; $-b$ when $b<0$; dividing only part of the numerator by $2a$; and reading
  $D<0$ or $D=0$ as "I made a mistake"
- 14 worked examples: the four methods; a double root; a $D<0$ case argued with Thm 9; building
  an equation from given roots two ways; a rational equation that becomes quadratic (two
  candidates, two checks, nb 09 Cor 6a); a **parameter** example whose trap is the forgotten
  $k=0$ case; and two word problems — one with a rejected negative width, one using the
  Pythagorean theorem from nb 03
- The difference, stated explicitly, between a **fake** solution (invented by a dangerous move,
  nb 09 Thm 6) and a **real** solution the *problem* rejects (a negative length)
- Python: `sp.discriminant`, `sp.factor` over $\mathbb{Q}$ versus `extension=sqrt(5)`, Vieta and
  Thm 7 re-proved symbolically with letters, his own `solve_quadratic` branching on $D$, and a
  one-line labelled preview of `domain=sp.S.Complexes`
- **Numerical-analysis lesson 8 (two halves):** (a) **catastrophic cancellation in the quadratic
  formula** — with $a=c=1$ the naive small root is 25% wrong at $b=10^8$ and exactly $0.0$ from
  $b=10^9$ on, cured completely by *rationalising the numerator* (nb 08 lesson 6) into
  $2c/(-b-\sqrt D)$; (b) **the $D$ test itself fails** — for roots $1$ and $1+\varepsilon$ the
  computer reports a double root once $\varepsilon\le10^{-8}$, although Theorem 5 proves there
  are two. A proof and a computation are not the same thing

**Pending confirmation — taught in session 11, waiting for the 20 exercises of
`notebooks/11-complex-numbers.ipynb`:**

- The pattern behind every number system: $\mathbb{N}\to\mathbb{Z}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}$,
  each step invented to solve one equation the old set could not solve — and the historical point
  that *negative*, *irrational* and *imaginary* were all originally insults
- **$\mathbb{C}$ built honestly**, as ordered pairs of reals with
  $(a,b)(c,d)=(ac-bd,\ ad+bc)$ — so $i^2=-1$ is a **computed theorem** (Thm 2), never an
  assumption, and nb 01 Thm C ($t^2\ge0$ for *real* $t$) is never contradicted
- Why the multiplication rule must be that one: $i$ = the quarter turn, and a quarter turn done
  twice is the half turn, which is multiplying by $-1$; also why the naive rule $(ac,bd)$ would
  kill the zero-product property
- Definitions: standard form $a+bi$ with $a,b$ **real**, $\operatorname{Re}$, $\operatorname{Im}$
  (a real number!), pure imaginary, conjugate, modulus, $\sqrt{-N}:=i\sqrt N$ as a *choice*
- **Theorem 1**: all field axioms in $\mathbb{C}$, including the full associativity-of-product
  computation — and the point that *every identity proved from the axioms (perfect squares,
  difference of squares, completing the square, the whole of nb 04) is therefore free in
  $\mathbb{C}$*
- Thm 3 (standard form is unique) used as a **working tool**: one complex equation = two real
  equations
- Thm 5 (conjugate rules, including $z\bar z=|z|^2$ and $z\in\mathbb{R}\iff z=\bar z$) and
  Thm 6 (division by the conjugate — the same trick as nb 08 rationalising), so $\mathbb{C}$ is
  a field and the zero-product property survives
- Thm 7: $|zw|=|z||w|$ and the **triangle inequality**, both proved by comparing squares
- Thm 8: powers of $i$ have period 4, proved with the division algorithm (nb 06)
- **Thm 9: $\mathbb{C}$ cannot be ordered** — proved by contradiction. So $z<w$ is meaningless,
  there is no "positive" square root of $-1$, and inequalities stay in $\mathbb{R}$ forever
- Thm 10 + 10b: the two square roots of a negative real, and the disproof of
  $\sqrt{ab}=\sqrt a\sqrt b$ for negatives by **one counterexample** — with the lesson that a
  theorem used outside its hypotheses is not a theorem at all
- **Thm 11**: the quadratic formula over $\mathbb{C}$; case $D<0$ gives a conjugate pair, and
  notebook 10 was not wrong, it was answering a question about $\mathbb{R}$
- **Thm 12: notebook 10 repaired** — Vieta and the factorisation theorem lose the "$D\ge0$"
  condition completely; every real quadratic has exactly two roots in $\mathbb{C}$
- **Thm 13 (conjugate root theorem)** for real polynomials of any degree, with the hypothesis
  located in exactly one line of the proof, and a counterexample when it is dropped
- **Thm 14**: every complex number has a square root, proved **constructively** ($r=|w|$,
  $x^2=(r+p)/2$, $y^2=(r-p)/2$, sign rule from $2xy=q$) — so quadratics with *complex*
  coefficients are solvable too (Thm 14b)
- **Thm 15 (Fundamental Theorem of Algebra): stated, NOT proved**, with an explicit reason
  (needs limits/continuity), an explicit list of what depends on it, and a promise to return.
  First deliberate unproved statement in the whole course
- Eleven traps, including the $\sqrt{-4}\sqrt{-9}$ family, "$i$ is not the positive root",
  $\operatorname{Im}$ is real, no comparing, $i$ never left in a denominator, and **"no solution"
  now depends on the set the question asks about**
- 16 worked examples: arithmetic, powers of $i$, division, $(1+i)^8$ by squaring, real quadratics
  with $D<0$, building a real quadratic from one complex root, factoring $x^2+4$, $x^4-1$ and
  $x^4+4$ over $\mathbb{C}$, the three cube roots of 1, $\sqrt{3+4i}$ by hand, and a full
  quadratic with complex coefficients
- Python: the **built-in `complex` type of core Python** (first topic needing no library),
  `math` vs `cmath`, a solver that branches exactly where Thm 11 branches, the Thm 14
  construction coded and checked against `cmath`, multiplying a whole shape by $i$ and $1+i$
  (rotation and stretch = similarity from nb 03), and `np.roots` showing conjugate symmetry
- **Numerical-analysis lesson 9:** near a double root the *type* of the answer (real or complex)
  depends on digits the computer does not have. Two opposite failures shown side by side —
  `1.0 + 1e-16 == 1.0` **hides** a real effect, while rounding noise **invents** an imaginary
  part of the same size. "Is this root real?" is not decidable in floating point
- 12 matplotlib figures, no ASCII art

## Current Focus

**Equations and Inequalities § 3 — Complex Numbers.** Notebook
`notebooks/11-complex-numbers.ipynb` is built and verified: it runs top to bottom with no
errors (88 cells, 38 code cells, 12 matplotlib figures, no ASCII art, every cell has an `id`,
`nbformat.validate` passes). No new dependency — and note that the *core* of this topic needs
no library at all, because Python has a built-in `complex` type.

**ELEVEN sets of homework are now outstanding (notebooks 01–11).** He wrote "please continue
next topic" with no answers attached, for the eleventh time. I said so in one line and taught.

The three doors notebook 10 left open are now all closed: Thm 5 case 3 ("no real solution")
became Thm 11 case $D<0$; Thm 6 and Thm 7 lost the "$D\ge0$" condition (Thm 12); and the
$\mathbb{C}$ preview of § 6.1 became the whole notebook. The number-tower framing was reused as
promised, but **counted correctly this time as the fourth extension** ($\mathbb{N}\to\mathbb{Z}\to
\mathbb{Q}\to\mathbb{R}\to\mathbb{C}$ is three past steps plus today) — the old note in this file
called it "the sixth", which was wrong.

One deliberate first: **the Fundamental Theorem of Algebra is stated without proof**, flagged
loudly, with the reason and the list of what depends on it. Until now every statement in the
course has been proved. If he ever asks "why should I believe that one?", the answer is
"you shouldn't yet — that is why it is marked".

Everything below "Known Weak Spots" is still **guesswork**. No exercise answer has ever
arrived. Notebook 11 leans on nb 01 (axioms, order axioms, $t^2\ge0$, absolute value), nb 02
(the $\sqrt{ab}$ hypothesis, $\sqrt{t^2}=|t|$, induction), nb 03 (Pythagoras, similarity),
nb 04 (difference of squares, at-most-$n$-roots, identity theorem), nb 05/06 (factor theorem,
division algorithm), nb 08 (principal roots, rationalising by the conjugate) and nb 10 (all of
it). Eight notebooks deep, all unverified.

**The cheapest tests, in order of cheapness:** notebook 11 Ex 14 (four written solutions, find
the mistakes — no calculation at all), then notebook 10 Ex 13, then notebook 11 Ex 2 (powers of
$i$ — six one-line answers that reveal instantly whether he divides by 4 or multiplies).

**Next session: ask for answers before opening anything new.** If he insists on continuing, run
the seven oral questions of notebook 11 § 8 first — especially Q1 (does $i$ contradict nb 01
Thm C?), Q4 (is $i$ bigger than 1? — the trap), and Q7, the sharpest: *the program printed
$1.0000000037 \pm 0.0000000041i$ — are the true roots real or complex?*

Next topic when we move on: **Equations and Inequalities § 4 — Radical Equations; Equations
Quadratic in Form; Factorable Equations** (→ `notebooks/12-radical-and-quadratic-form-equations.ipynb`,
the name he chose in `README.md`). It needs the nb 09 domain-first habit and the nb 09 Thm 6
fake-solution machinery, plus today's lesson that the **solution set depends on the set you
solve in**. Squaring both sides is the first *irreversible* move he will meet in force, so
checking stops being optional there.

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

From notebook 04:
- Ex 1: does he say $\frac{x^{2}-1}{4}$ is not a polynomial? (Dividing by a *number* is
  fine; dividing by the *letter* is not.) And does he handle $0$ and $\sqrt5\,x^{3}$?
- Ex 3(a) and Ex 8(c): does he accept that the degree of a sum can *drop*?
- Ex 7(c): the sign trap $-x^{2}$ against $(-x)^{2}$ — the same trap as notebook 02 Ex 6.
  If he misses it twice, it goes on the permanent review list.
- Ex 9: does he insert the missing $0x^{2}$ before dividing? This is the single most common
  cause of a wrong long division.
- Ex 10(c): does he test $c=+2$ for the factor $x-2$, and $c=-1$ for $x+1$ (Example 6b)?
  Sign of $c$ is the classic factor-theorem slip.
- Ex 14(c): does he see that the binomial theorem still applies to $(x+1/x)^6$ even though
  that is not a polynomial?
- Ex 16(b): can he turn "divisible by" into equations using the factor theorem, instead of
  trying to divide?
- Ex 17–20: real proofs, naming the theorem at each step. Ex 18 is the first proof by
  *contradiction on degrees*; Ex 19 needs him to notice that the long bracket in Theorem 4
  is a whole number; Ex 20 is the first proof that uses the identity theorem as a *tool*
  rather than quoting it.
- Watch whether he can state both halves of an induction proof cleanly — the binomial
  theorem proof depends on it, and this is the second time induction has appeared.

From notebook 05:
- Ex 1(c) and Ex 3(c): does he pull the **minus sign** out with the GCF, and does he spot
  the GCF at all before hunting for a pattern? (Trap 1 — the most common cause of a wrong
  answer in this whole topic.)
- Ex 4(d) and Ex 6(c): does he try to force a factorisation that does not exist, or does he
  reach for the discriminant and *prove* it is irreducible? Watch for "$x^2+9=(x+3)^2$".
- Ex 8(a),(c),(d): does he **stop too early**? $x^4-16=(x^2-4)(x^2+4)$ is the classic
  half-finished answer.
- Ex 8(e): the two-routes-one-answer question. This is the first exercise where the point is
  not the answer but **why the answer had to be the same** (Theorem 16). If he just does one
  route, he has missed it.
- Ex 14(b): does he divide $x^3=4x$ by $x$ and lose the root $x=0$? Almost everyone does.
- Ex 14(c): Trap 2 — does he set the brackets equal to $5$? Note that the wrong method gives
  one right answer by luck here, so he may not notice.
- Ex 16(c): the deep one — does he believe "no rational root" means "irreducible over
  $\mathbb{Q}$"? $x^4-4$ is the counterexample. Same misconception as Ex 20.
- Ex 9 / Ex 10: does he use the factor theorem sign correctly ($r$ a root $\Rightarrow$
  factor $x-r$)? This is the third notebook in a row with a sign trap of this shape — if he
  misses it again it goes on the permanent review list.
- Ex 11–12: does he use exact `Fraction` arithmetic, or floats? Ex 12 explicitly asks him to
  break it with floats — see whether he can explain *why* it breaks.
- Ex 17(b): completing the square in $a$ while treating $b$ as a constant. First time he has
  had to choose *which letter* to complete the square in.
- Ex 18: the parity argument (both even or both odd). This is a genuinely hard number-theory
  step and I expect him to need help; that is fine, but see whether he *notices* that the
  step is needed at all, or silently assumes $p,q$ are integers.
- Ex 19: can he build the right monic polynomial from an irrational number? That move
  ($\sqrt[3]2$ is a root of $x^3-2$) is the whole trick.
- Ex 20(d): the capstone. Does he reason about *which degrees the two pieces could have*?
- Big question to settle when answers arrive: **can he write a proof at all?** Five
  notebooks, twenty proof exercises set, zero seen.

From notebook 06:
- Ex 1(c) and Ex 2(b): the sign of $c$ for a divisor written with a **plus** ($x+3 \Rightarrow
  c=-3$). This is now the FOURTH notebook in a row with this trap. If he misses it again it
  goes on the permanent review list, no exceptions.
- Ex 2(a),(b): does he insert a $0$ for every missing power? Same trap as nb 04 Ex 9. Watch
  especially $2x^5+x^2-7$, which needs three zeros.
- Ex 3: does he say $c=2$ for the divisor $3x-6$ (correct, after factoring out the 3) or
  $c=6$? And does he remember the extra Theorem 9 step at all?
- Ex 5(c): $x^{100}-1$ — does he *think* (use $p(1)=0$) or does he try to build the table?
  The exercise is a test of whether he reaches for the theorem instead of the algorithm.
- Ex 6(b): does he divide the **remainder** by $a$? This is the classic Theorem 9 mistake and
  the exercise is built so that the wrong answer looks tidy.
- Ex 7(c): does he find **both** values of $k$ ($k=1$ and $k=-2$), or stop at the first? He
  has not yet been asked for "all solutions" of a quadratic condition in this course.
- Ex 8(c): $x^4-1$ — does he stop at $(x^2-1)(x^2+1)$? Same "stopping too early" trap as
  nb 05 Ex 8(a). Second appearance.
- Ex 9: does he keep deflating the **quotient**, or does he re-divide the original $p$ every
  time? Re-dividing $p$ gives remainder $0$ forever and is the classic multiplicity error.
- Ex 10(c): does he notice that a two-term approximation is *not* exact, and can he say how
  big the error is instead of writing "about the same"?
- Ex 11: does he use the bound theorems to *shrink the candidate list*, or does he just find
  the bounds and then ignore them?
- Ex 12: the coefficient-order bug. He must write the algorithm with the coefficients
  **reversed** relative to the notebook. If he silently reverses the list and calls the
  notebook function, he has dodged the exercise — the point is to feel the bug.
- Ex 16(d): does he see that `Fraction` gives remainders of exactly $0$, and can he say why
  (no rounding) rather than "because it is more accurate"?
- Ex 17: this is the third induction proof of the course and the first with a **sum** as the
  claim. Watch whether the inductive step actually *uses* the hypothesis, and whether he can
  handle the index shift. This is still an unverified skill after three attempts.
- Ex 18: does he prove (a) by induction (each row entry is an integer combination of integers)
  rather than by checking one example?
- Ex 19: does he use the **uniqueness** half of Theorem 8? Without it the proof is only half
  done. Uniqueness has now been the load-bearing step in Theorems 1, 5 and 8 of this notebook,
  and he has never been tested on whether he sees that.
- Ex 20(b): deliberately beyond him. The exercise asks him to do $n=1$ honestly and then say
  precisely where he is stuck. **Watch whether he can admit being stuck in a precise way** —
  that skill matters more than the answer, and I have no evidence about it yet.
- General: does he *check* every table against $p(c)$, as the notebook demands? If the checks
  are missing, the answers are worth much less.

From notebook 07:
- Ex 1(d) and Ex 2: does he factor the bottom **before** reading off the domain? Ex 1(d) has a
  hidden common factor of $x$, so a careless answer misses two of the three forbidden points.
- Ex 2, Ex 3, Ex 4: does he write the **restrictions** on every answer, including the ones that
  vanish from the simplified form (Ex 4(b) has four)? If the restrictions are missing, the
  answer is not finished — this is the single thing I will be strictest about in this topic.
- Ex 3: the reversed bracket. $\frac{4-x}{x-4}=-1$, not $+1$. Watch Ex 3(c), where the sign flip
  is buried inside a product and easy to miss.
- Ex 5(b): does he use the LCD $(x-2)(x+2)$, or does he multiply the two bottoms and get a
  degree-3 mess he then cannot cancel? (Trap 6.)
- Ex 6: the minus sign. The exercise plants the wrong answer explicitly, so if he agrees with the
  student he has walked straight in.
- Ex 7(a): both methods must give the same thing. If only one method is shown, he has skipped the
  point of the exercise.
- Ex 8(c): does he notice that synthetic division needs a divisor $x-c$ and $x^2+1$ is not of
  that shape? This tests whether he learned nb 06's *hypothesis*, not just its algorithm.
- Ex 9: the difference quotient — first real contact with calculus. Watch whether he can get the
  $h$ to cancel in (b) and (c); (b) needs a common denominator inside the top first.
- Ex 10(c): $\frac{x^3-x}{x^2-2x+1}$ has a hole AND a wall at the *same* factor $(x-1)$ appearing
  with different powers. This is the hardest classification of the set and I expect a slip.
- Ex 11(c): three terms, so three cover-up computations. Does he trust the formula, or does he
  fall back on solving a system?
- Ex 12(c),(d): the harmonic-mean surprise. Does he accept that the average speed is not the
  average of the speeds? (d) needs him to spot the $(u-v)^2$ after subtracting — a move from
  nb 05.
- Ex 13–16 (Python): the fastest evidence available. Ex 13 asks for hole-vs-wall classification
  in code; Ex 15(b),(c) deliberately break the cover-up formula on a repeated factor and ask
  **which hypothesis failed** — that is the real test of whether he reads theorems as objects
  with conditions. Ex 16(d) asks *why* the raw difference quotient returns exactly $0$.
- Ex 17: the discriminant argument. Does he reach for $D<0$ (nb 05 Thm 8) or does he just try
  numbers and give up?
- Ex 18: needs Lemma 6b. First time he has to use a lemma proved *in the same notebook* as a
  tool rather than as a step in the theorem it was made for.
- Ex 19(c): "what did the Lagrange proof give us that this one does not?" — I am looking for
  "it works for any number of factors, not just two". This tests whether he can see the *reach*
  of a proof, not only its correctness.
- Ex 20 (capstone): the degree-parity argument. Watch for (i) whether he actually uses the
  lowest-terms assumption, (ii) whether he sees that "even = odd" is the contradiction, and
  (iii) part (c), comparing this with the $\sqrt2$ proof of notebook 01. If he can draw that
  analogy himself, the whole nb 01 / nb 05 / nb 07 thread has landed.
- General: this is the third notebook where a **hypothesis** of a theorem is the real lesson
  (nb 06: divisor must be $x-c$; nb 07: distinct linear factors, and $d\neq0$ in cancelling).
  If he keeps applying rules outside their conditions, that becomes the top permanent weak spot.

From notebook 08:
- Ex 1(d),(f),(g): does he see that $-\sqrt{49}=-7$ (the minus is *outside*) but
  $\sqrt{(-7)^2}=+7$? Same family as the $-3^2$ vs $(-3)^2$ trap of nb 02 Ex 6 and nb 04 Ex 7(c).
- Ex 2: the bars. This is the FIFTH notebook in which the $\sqrt{x^2}=|x|$ trap appears. Watch
  2(d) $\sqrt[6]{(x-2)^6}=|x-2|$ and especially 2(f) $\sqrt{x^6}=|x|^3$ — the one where you may
  *not* drop the bars even though the exponent under the root is even.
- Ex 4(c): $\sqrt8+\sqrt[3]8$ — does he try to "combine" radicals with different indices?
- Ex 6(d): does he reach for the conjugate (which fails for a cube root) or for the
  $u^3-v^3$ identity? The exercise asks him to *say why* the conjugate cannot work.
- Ex 7: does he answer "$\frac{1}{2\sqrt5}$" and explain that putting $x=0$ is legal only in the
  simplified form? This is the calculus door; if he only simplifies and stops, he missed it.
- Ex 9: does he factor out the **negative** power (the smallest one), or the positive one? Same
  shape as the GCF trap of nb 05 Ex 1(c).
- Ex 10(d): does he write $x^2-4>0$ (strict) rather than $\ge0$? Two rules on one expression.
  Ex 10(f) is harder: a fraction is $\ge0$ in two ways, so the answer is a union.
- Ex 11: does he use one common power ($\mathrm{lcm}=12$) for all three, or compare them in
  pairs with decimals? Decimals here would be a small failure of nerve.
- Ex 12: three fake proofs. (a) and (b) are the ones from §5; (c) is the bars again. The point is
  to name the **first** wrong step and the hypothesis it breaks — not to say "you can't do that".
- Ex 13(b),(c): does he check the **sign** of his answer against the definition of the principal
  root, or does he stop as soon as the squares match?
- Ex 14: does he actually obey the "no library root inside the function" rule? And does he notice
  that $M=a+1$ still works for $a=0.001$ *because* the bound only has to be an upper bound?
- Ex 15(d): the honest question — bisection is proved, Newton is not. Watch whether he can say
  what was gained and what was given up, instead of just "Newton is faster".
- Ex 16(c): the "why $10^8$" question. He needs to connect 16 float digits with 8 shared digits.
  This is the first time he has had to *predict* where a computation breaks rather than observe it.
- Ex 17: the first proof asked for by name of a lemma from this notebook. Does he use the
  telescoping identity, or does he silently switch to induction (which the exercise forbids)?
  And does he find the counterexample showing $s\ge0$ is needed ($s=-2,t=1,n=2$)?
- Ex 18(b): the sharp one — he must point at the **sentence** in his own proof that fails, not
  say "because they are negative". This tests whether he reads his own proofs.
- Ex 19: the irrationality machine. Does he build the monic polynomial $x^n-a$ himself? Ex 19(c)
  checks whether he can recognise nb 01 Thm E as a special case of his own new result.
- Ex 20(a): needs Theorem 10 *by name* at the common-denominator step. If he does not mention it,
  he has not seen why it matters.
- Ex 20(b): deliberately beyond him, in the tradition of nb 06 Ex 20. **Watch whether he can say
  precisely where he is stuck** — still the one skill I have no evidence about.
- General: does he state the assumption on the letters ("assume $x>0$") before simplifying, or
  does he simplify first and hope? Notebook 07 asked for the same discipline about domains.

From notebook 09:
- Ex 1: does he call $(x+1)^2=x^2+2x+5$ **linear**? Definition 7 says "can be *written* as
  $ax+b=0$", so it is — after cancelling $x^2$. And (e) $5=0\cdot x+5$ is the trap in the other
  direction: it is an identity, not a linear equation, because $a=0$.
- Ex 2(b): does he answer "yes, $x=-1$ works" without noticing that $x=-1$ is **not in the
  domain**? This is Trap 2 in its smallest form, and it is the single most likely slip.
- Ex 3–4: routine. Watch only for the sign of the term moved across, and for 4(c), where the
  answer is $S=\mathbb{R}$ and the temptation is to write "$x=0$" or to think he made an error.
- Ex 5(a),(b): does the LCD multiply the term that had **no** fraction (Trap 6)? And the minus
  in front of a fraction (Trap 5, nb 07's oldest trap)?
- Ex 6(b): can he say what the equation *means* (money at two interest rates, or a mixture)?
  If he only computes, the translation skill of § 7 is not there yet.
- Ex 7: does he name the **case of Theorem 5** or just give the answer? Naming the case is the
  test; the answers are easy.
- Ex 8: the whole point. Does he (i) write the domain first, (ii) call his answer a *candidate*,
  (iii) check in the **original** equation, and (iv) name Theorem 6? Missing (i) or (iii) means
  the lesson did not land, even if the final set $\varnothing$ is right.
- Ex 9: the reverse test — the candidate is genuine, and checking is *still* compulsory. If he
  says "checking is only needed when the answer looks suspicious", that is exactly the wrong
  model and needs fixing on the spot.
- Ex 10: can he name the **moment** the equation stopped being quadratic (when the $x^2$ terms
  cancelled)? This is the "linear is a property after simplification" idea.
- Ex 11(b),(c): (b) needs a common denominator and then a *factoring* step; (c) is the first
  time he must collect the unknown out of a fraction and factor it out — the same move as
  Theorem 5's proof. Watch whether he states $u\neq f$, $x\neq3$, $y\neq2$.
- Ex 12(b): does he actually run the **triangle inequality** check (nb 03), or does he stop at
  the three numbers? The check is the part that connects two chapters.
- Ex 13: two errors, one of method (dividing by $x-3$, Theorem 7) and one of arithmetic
  ($x+2=5$ gives $x=3$, which is also the lost root — a deliberately confusing coincidence).
  Watch whether he finds **both**, and whether he can say *what was lost*, not just "you can't
  divide by zero".
- Ex 14: does his function follow **Theorem 5** (branch on $p=r$, then on $q=s$) or does he
  cheat by calling `sp.solve` and reading the list? The exercise forbids it for a reason.
- Ex 15: the detector. Does every extraneous answer he finds turn out to be a zero of the
  multiplier — and does he *say* that this is Theorem 6 confirmed, rather than a coincidence?
- Ex 16(c): the sentences matter more than the code. He must connect "16 correct digits" with
  "a coefficient that should be 0 came out $5.5\times10^{-17}$" and with "the true answer is
  $S=\varnothing$". First time he has been asked to explain *why* a computer answer is
  meaningless rather than merely inaccurate.
- Ex 17–18: real proofs by double inclusion. Watch whether he writes **both** directions, and
  whether he can point at the *single line* that needs $c\neq0$ / $a\neq0$. Notebook 08 Ex 18(b)
  asked for the same self-reading skill and there is still no evidence about it.
- Ex 19: the $E(x)=x^2+1$ question at the end is the sharpest part — the answer is "none, because
  $x^2+1>0$ has no real zero", and it tests whether he *uses* his own theorem instead of
  re-deriving.
- Ex 20(b): the linear identity theorem. Does he use two different points to get two equations
  and subtract, or does he wave at "two points determine a line"? The waving version is not a
  proof, and this is the notebook's main proof-rigour test.
- General: does he **write the domain before the algebra**, every single time? That one habit is
  what this whole notebook is trying to install, and it is the thing to check first in every
  answer he sends.


From notebook 10:
- Ex 1(c),(d),(f): does he see that $(x-1)^2=x^2+4$ is **not** quadratic (the $x^2$ cancels, so
  $a=0$), that $x(x+2)=7$ **is**, and that (f) depends on whether $m=0$? Same shape as nb 09
  Ex 1, and the same lesson: "quadratic" is a property *after* simplification.
- Ex 2: does he compute $D$ **before** hunting for factors, as the section asks? If he factors
  first and never mentions $D$, Theorem 8 has not landed.
- Ex 3: the whole point of the exercise is that (a) and (b) disagree. Watch whether he can name
  nb 09 **Theorem 7** and say the lost root is $0$ — not just "you can't divide by zero".
- Ex 4(c): $x^2=-16$. Does he write $S=\varnothing$, or does he write $x=\pm4i$ (jumping ahead)
  or "$x=\pm\sqrt{-16}$" (meaningless in $\mathbb{R}$)? The correct answer today is
  $\varnothing$, by Theorem 2, case 3.
- Ex 4(b),(d): does the $\pm$ survive? Trap 3 is the single most common slip in this topic.
- Ex 5(b): a leading coefficient of $3$. Does he divide by $3$ first, or try to complete the
  square with the $3$ still there? Both work, but the second needs care he may not have.
- Ex 6: does he state $D$ and the case of Theorem 5 *before* solving, every time?
- Ex 7(d): the trap. $x^2+2\sqrt3x+3=0$ has $D=0$, but Theorem 8 does **not** apply because the
  coefficients are not integers. If he says "rational roots because $D=0$ is a perfect square",
  he has used a theorem outside its hypotheses — the exact failure mode nb 08 Ex 12 was built to
  test, and still the thing I have no evidence about.
- Ex 8: the sign of the product. Does he see that $c/a<0$ forces the two roots to have opposite
  signs? That is reading a theorem *for information*, not for computation.
- Ex 9(c): why do the irrational parts cancel? The answer is the **sum** formula (they are
  conjugates); the product formula gives $9-2=7$. Watch whether he can say which formula does
  which job.
- Ex 10: two candidates, one of them $x=2$ which is forbidden. Does he check **both**? Does he
  name nb 09 Theorem 6? The answer is $S=\{3\}$.
- Ex 11: the forgotten $k=0$ case (Example 12 warned about it explicitly). If he still misses it
  after being shown, that is a real weak spot: *reading the hypotheses of a definition*.
- Ex 12(b): the frame adds $2$ cm on **each** side, so $4$ cm to each dimension. The classic slip
  is adding $2$. The answer is a $6\times9$ photo.
- Ex 12(c): two times, $t=1$ and $t=3$. Does he explain them physically (going up, coming down)?
  This is the first time a *second* root has had a meaning instead of being rejected.
- Ex 13: the first fake solution **passes its own check**. Watch whether he can explain why a
  passing check does not save it — checking finds fake solutions, it can never find *missing*
  ones. This is the sharpest conceptual question in the notebook.
- Ex 13, second one: $\frac{4\pm\sqrt{20}}{2}=4\pm2\sqrt5$ is Trap 5 (dividing only part of
  the numerator). The correct answer is $2\pm\sqrt5$.
- Ex 14: does his solver branch on the sign of $D$ (Theorem 5), or does he cheat and call
  `sp.solveset`? And does he handle $a=0$?
- Ex 15: does he read the changeover value of $c$ off the **discriminant** ($D=4-4c=0$, so $c=1$)
  rather than off the picture? The exercise says so explicitly.
- Ex 16(c),(d): the derivation on paper matters more than the code. He must connect this to nb 08
  lesson 6 by name.
- Ex 17–19: proofs. Watch for: proving the two roots are **different** in Ex 17 (most people
  forget that half), naming where $a\neq0$ is used **twice** in Ex 18, and in Ex 19(c) actually
  using the identity theorem instead of hand-waving.
- Ex 20(a): two proofs of the same fact — one quoting nb 04 Thm 8, one from Theorem 4 directly.
  Can he produce *two different* arguments for one statement? Notebook 03 Ex 20 asked the same
  kind of thing and there is still no evidence.
- Ex 20(c): deliberately hard (odd coefficients $\Rightarrow$ no rational root), in the tradition
  of nb 06 Ex 20 and nb 08 Ex 20(b). **The instruction to say exactly where he is stuck is the
  real test**, and it is the one skill I have asked for four times now with no answer.
- General: does he keep answers **exact** to the last line (Trap 10), and does he write the
  solution as a **set**?


From notebook 11:
- Ex 1(d),(f): $(1-i)^2$ and $-4i(2-7i)$ — the two places a sign dies. Does $-15i^2$ become
  $+15$ every time, or only when he is concentrating?
- Ex 2(f): the sum $i+i^2+\dots+i^{100}$. The answer is $0$ (25 complete cycles). If he computes
  100 terms instead of seeing the cycle, Theorem 8 has not landed.
- Ex 3(d),(e): does he use Theorem 7(3) and the triangle inequality **as information**, instead
  of computing both sides and comparing? Same skill as nb 10 Ex 8.
- Ex 5(c): the sharpest of the three. $\sqrt{-4}\cdot\sqrt{25}=\sqrt{-100}$ is **true** — one
  factor is non-negative, so the hypothesis does not fail the same way. If he answers "false,
  because negatives", he has learned a superstition, not the theorem.
- Ex 6: does he give **both** answers ($\mathbb{R}$ and $\mathbb{C}$) every time, or does he
  now think $\varnothing$ is always the wrong answer? Trap 9 cuts both ways.
- Ex 7: the $\frac{4\pm6i}{2}$ family — nb 10 Trap 5, third appearance. Watch for $4\pm3i$.
- Ex 9(c): builds an equation whose roots are $3-i$ and $5$ and asks whether it contradicts
  Theorem 13. It does not (the coefficients are not real). This tests whether he reads
  hypotheses — the single most repeated failure mode I am watching for (nb 08 Ex 12, nb 10
  Ex 7(d), Trap 7 here).
- Ex 10(d): $x^4+64$ needs the add-and-subtract trick from Example 12(c). Does he try, or does
  he stop? **If he stops, I want the sentence saying where.**
- Ex 11(c): roots $1+i$ and $2+3i$ — $b$ and $c$ cannot both be real. Does he *prove* it with
  Theorem 13, or just compute and shrug?
- Ex 12: the Theorem 14 method. Does he remember the **sign rule** $2xy=q$, or does he produce
  four sign combinations and keep them all?
- Ex 14: four wrong solutions. A is the missing second root, B is the $1/i$ sign (the answer is
  $-\frac23 i$, not $+\frac23 i$), C is dividing only part of the numerator, D is comparing
  complex numbers at all. D is the conceptual one — Theorem 9.
- Ex 15: build a `Cx` class in core Python. This is the whole notebook as code; if it works, he
  has built $\mathbb{C}$. Watch whether `__mul__` uses $ac-bd$ or the naive rule.
- Ex 16(b): predict inward/outward spiral **before running**, from $|z|$ and Theorem 7(3).
  A prediction made before the code runs is worth ten made after.
- Ex 17(c),(d): the numerical lesson. Does he trust the theorem over the printout?
- Ex 18(c), 19(a): induction, second and third outing since nb 02. Does he write a real base
  case and a real inductive step, or does he write "and so on"?
- Ex 20(a): the cubic case of Theorem 13, then "at least one real root" **using Theorem 15** —
  does he notice that he is allowed to use it because the exercise says so, and say where?
- Ex 20(b): re-prove Theorem 9 without looking. This is the one exercise designed to test
  *memory of a proof's shape* rather than recall of a result.
- Ex 20(c): $z+1/z$ real $\Rightarrow$ $z$ real or $|z|=1$. Deliberately hard, in the tradition
  of nb 06 Ex 20, nb 08 Ex 20(b) and nb 10 Ex 20(c). **The instruction to say exactly where he
  is stuck is the real test — it is now the fifth time I have asked, with no answer.**
- General: does he state the **set he is solving in** every single time? That is the habit this
  notebook exists to install, the way nb 09 installed "write the domain first".


## Session Log

### Session 11 — 2026-08-25 — Complex Numbers; Quadratic Equations in $\mathbb{C}$

- **Topic taught:** *Equations and Inequalities* § 3, **Complex Numbers; Quadratic Equations in
  the Complex Number System**. He wrote "please continue next topic", with no exercise answers,
  for the eleventh time. Noted in one line at the top of the session, then taught.
- **Notebook created:** `notebooks/11-complex-numbers.ipynb` — 88 cells, 38 code cells, 12
  matplotlib figures, no ASCII art, every cell carries an `id`, `nbformat.validate` passes.
  Verified: executes top to bottom with zero errors. No new dependency.
- **Naming:** from his own `README.md`, which already contained the filename.
- **What is inside:**
  - §0 recall table: fifteen earlier results this notebook stands on (nb 01, 02, 03, 04, 05/06,
    08, 10) plus four warm-up questions.
  - Intuition built in one line: **$i$ is the quarter turn**, and a quarter turn done twice is
    the half turn, which is multiplication by $-1$. From that, the multiplication rule
    $(a,b)(c,d)=(ac-bd,ad+bc)$ is *derived*, not announced — and the naive rule $(ac,bd)$ is
    shown to destroy the zero-product property.
  - **$\mathbb{C}$ constructed as ordered pairs**, so $i^2=-1$ is Theorem 2, a computation. The
    "does $i$ exist?" question is replaced by "can we build a field containing $\mathbb{R}$ with
    an element whose square is $-1$?" — and nb 01 Thm C is never contradicted, because it quantifies
    over *real* $t$. This was the single most important paragraph in the notebook.
  - Fifteen theorems. Thm 1 (field axioms, with the full associativity grind, paid for by the
    remark that every earlier algebraic identity is now free in $\mathbb{C}$), Thms 2–6
    (standard form, conjugates, division), Thm 7 ($|zw|=|z||w|$, triangle inequality), Thm 8
    (period 4), **Thm 9 ($\mathbb{C}$ cannot be ordered)**, Thm 10/10b (roots of negatives, and
    the $\sqrt{ab}$ counterexample), **Thm 11–12 (the quadratic formula over $\mathbb{C}$, and
    notebook 10 repaired: Vieta and factorisation lose the $D\ge0$ condition)**, Thm 13
    (conjugate root theorem), **Thm 14 (every complex number has a square root — constructive)**
    and Thm 15 (FTA, stated without proof).
  - **First deliberate unproved statement of the course** (Thm 15), with the reason, the list of
    what depends on it, and a promise to come back after limits. Everything else proved in full.
  - Theorem 9 given real weight: it is *why* there is no positive square root of $-1$, *why*
    Definition 8 is a choice, and *why* inequalities will stay real forever.
  - 11 traps, 16 worked examples, 12 figures. Figure 8 is the one I care about: the parabola
    that misses the axis on the left, and the two roots sitting symmetrically in the plane on
    the right, with the common real part $-b/(2a)$ = the vertex.
  - **Numerical lesson 9**: `1.0 + 1e-16 == 1.0` hides a real effect while rounding noise invents
    an imaginary one — two opposite failures, same size. Figure 12 (the cross) shows the roots
    sliding along the real axis, colliding, and leaving *perpendicular* — which is
    $\sqrt{\text{negative}}$, which is a quarter turn. The notebook's first idea, returning as
    its last.
- **What went well:** the notebook did what it was built for — it closed all three doors nb 10
  left open, and it removed hypotheses instead of adding them (Thm 12). The construction-first
  approach means he never has to take $i$ on faith.
- **Mistakes to revisit:** none of his (nothing has been submitted). One of **mine**, corrected
  here: this file previously called the $\mathbb{C}$ step "the sixth" time we needed a bigger
  number system. It is the fourth. The notebook says fourth.
- **Homework given:** the 20 exercises of notebook 11. Ex 14 (find the mistakes in four written
  solutions) needs no calculation and is the cheapest possible answer to send.
- **Next session plan:** ask for answers first — Ex 14 of nb 11, or Ex 13 of nb 10. If he says
  continue anyway, run the seven oral questions of § 8 (especially Q1, Q4, Q7) and then teach
  *Equations and Inequalities* § 4, **Radical Equations; Equations Quadratic in Form; Factorable
  Equations** → `notebooks/12-radical-and-quadratic-form-equations.ipynb`.

### Session 10 — 2026-08-24 — Quadratic Equations

- **Topic taught:** *Equations and Inequalities* § 2, **Quadratic Equations**. Second session of
  the day; he wrote "continue next topic" again, with no exercise answers. Tenth time; noted in
  one line and taught.
- **Notebook created:** `notebooks/10-quadratic-equations.ipynb` — 76 cells, 36 code cells, 9
  matplotlib figures, no ASCII art, every cell carries an `id`, `nbformat.validate` passes.
  Verified: executes top to bottom with no errors. No new dependency (numpy, sympy, matplotlib,
  plus `math` from the standard library).
- **Naming:** taken from his own `README.md`, which already listed the filename before the
  session started. Same for topics 3–7 of this chapter — see Current Focus.
- **What is inside:**
  - **§0 recall table**: fifteen earlier results this notebook stands on (nb 01, 02, 04, 05, 07,
    08, 09), plus three warm-up questions. Spaced repetition, since none is confirmed.
  - Intuition: *one bend changes everything* — the three shapes (two / one / none) set directly
    against nb 09's (one / none / all); the zero-product property drawn as a product touching
    zero exactly where a factor does; **completing the square drawn as a literal square with a
    missing corner**; the $\pm$ explained as coming from Theorem 2 and *not* from the radical
    sign; and the discriminant introduced as the parabola sliding up and down.
  - Definitions 1–5, with **double root / multiplicity** given a real definition rather than a
    slogan.
  - Ten theorems, all fully proved: Thm 1 (factoring, both directions), Thm 2 (square-root
    property, all three cases), Thm 3 (the completing-the-square identity), **Thm 4 (the
    quadratic formula, derived by multiplying by $4a$** so that no fractions appear until the
    last line — a trick worth stealing), **Thm 5 (the discriminant theorem)**, Thm 6 (Vieta),
    Thm 7 (factorisation), **Thm 8 (rational roots iff $D$ is a perfect square**, via the nb 05
    rational root theorem applied to $t^2-D$), Thm 9 (the vertex identity + the sign of a
    quadratic with $D<0$) and Thm 10 (vertex and axis of symmetry, flagged as a preview of a
    later chapter but proved in full).
  - The main structural point made out loud: the four methods are not four tricks. Factoring is
    what always happens when $D\ge0$ (Thm 7); the formula is completing the square done once
    with letters. *A formula is a proof done once so it never has to be done again.*
  - Traps (10), several of them recurrences: the $-3^2$ vs $(-3)^2$ family (seventh appearance),
    cancel-factors-not-terms (nb 07), dividing by $x$ (nb 09 Thm 7), and "no real solution is an
    answer, not an error".
  - Worked examples 1–14, ending with two word problems: a garden (reject the negative width)
    and a **ladder against a wall** that needs the Pythagorean theorem from nb 03 and lands on a
    $15$-$20$-$25$ triangle. Example 12 (parameter $k$) is built around the forgotten $k=0$ case.
  - The distinction drawn explicitly for the first time: a **fake** solution (invented by a
    dangerous move — nb 09 Thm 6) versus a **real** solution the *problem* rejects (a negative
    length). Two different reasons to discard an answer, and he should be able to name which.
  - Python: `sp.discriminant`; `sp.factor` over $\mathbb{Q}$ against `extension=sqrt(5)` to show
    Theorem 8 in action; Vieta and Thm 7 re-proved symbolically with letters; his own
    `solve_quadratic` branching on the sign of $D$ and raced against `solveset`; and **one
    clearly-labelled line of preview** showing the complex answer, with a sentence saying that
    nothing in the notebook depends on it.
  - **Numerical-analysis lesson 8, in two halves.** (a) The famous one: with $a=c=1$ the naive
    small root is wrong in the third digit at $b=10^7$, 25% wrong at $b=10^8$, and exactly $0.0$
    from $b=10^9$ on; the cure is *rationalising the numerator* from nb 08 lesson 6, giving
    $2c/(-b-\sqrt D)$, which stays correct everywhere. (b) The sharper one: the **test** $D>0$
    versus $D=0$ itself breaks — for roots $1$ and $1+\varepsilon$, once $\varepsilon\le
    10^{-8}$ the computer reports a double root although Theorem 5 proves there are two distinct
    ones. Stated as: a proof and a computation are not the same thing.
  - 9 figures: the three shapes with solution sets on number lines; the zero-product property
    drawn; completing the square as three area panels; the parabola family sliding through
    $D>0$, $D=0$, $D<0$; the square-root property as a horizontal line cutting $y=t^2$; the roots
    symmetric about the axis of symmetry with the two equal gaps arrowed; Example 4 as a shifted
    $y=x^2$; and the two numerical figures (error of naive vs stable on log-log, and the true
    root gap against the gap the computer sees).
- **What went well:** nothing to judge — still no answers from him, in any notebook.
- **Mistakes to revisit:** none recorded (see "Known Weak Spots" for what to look for).
- **Homework given:** the 20 exercises of notebook 10. 14–16 are Python (his own Theorem-5
  solver; drawing the discriminant family; breaking the formula on purpose). 17–20 are proofs,
  ending with "if $a,b,c$ are odd integers then there is no rational root — or say exactly where
  you are stuck".
- **Next session plan:** (1) **ask for answers first** — cheapest is Ex 16 of this notebook, then
  Ex 13 (whose first fake solution *passes its own check*); (2) if he insists on continuing, run
  the seven oral questions of § 8, especially Q3, Q5 and Q7; (3) then open **§ 3 — Complex
  Numbers** (→ `notebooks/11-complex-numbers.ipynb`), where Theorem 5's "not yet" is finally
  answered and Theorems 6–7 lose their $D\ge0$ hypothesis. Reuse the running
  "bigger number system" table — this is its sixth row.

### Session 9 — 2026-08-24 — Linear Equations (new chapter)

- **Topic taught:** *Equations and Inequalities* § 1, **Linear Equations** — the first topic of
  the second chapter. He wrote "continue next topic", with no exercise answers again. Ninth
  time; noted in one line and taught.
- **Naming:** the syllabus line reads "Linear Functions", but inside the *Equations and
  Inequalities* chapter the subject is equations, so the notebook is
  `notebooks/09-linear-equations.ipynb` and its first cell explains the choice. The function
  view is deferred to the later chapter that owns it.
- **Notebook created:** `notebooks/09-linear-equations.ipynb` — 76 cells, 36 code cells, 9
  matplotlib figures, no ASCII art, every cell carries an `id`, `nbformat.validate` passes.
  Verified: executes top to bottom with no errors
  (`jupyter nbconvert --to notebook --execute`). No new dependency (numpy, sympy, matplotlib).
- **What is inside:**
  - **§0 recall table** (the pattern kept from nb 07 and 08): eleven earlier results this
    notebook stands on, plus three warm-up questions. Spaced repetition, since none is confirmed.
  - Intuition: the *change of kind* — 01–08 rewrote objects, today we answer a question;
    expression = recipe, equation = question, **answer = a set**; the **balance scale**; the
    **two-machines / two-lines** picture that makes "how many solutions" visible; the three
    shapes; and solving as a **chain of equivalent equations** rather than as computing.
  - Definitions 1–8, with the domain of the equation ($D_L\cap D_R$) given its own definition
    so that "not in the domain" is a *defined* status, not an excuse.
  - Theorems, all fully proved by double inclusion from the nb 01 axioms: **Thm 1** (addition,
    with the hypothesis "defined on all of $D$" and a counterexample when it is dropped),
    **Thm 2** (multiplication by $c\neq0$, with the exact line that needs $c\neq0$),
    **Thm 3** (existence + uniqueness for $a\neq0$, uniqueness by the nb 08 three-line pattern
    + zero-product), **Thm 4** ($a=0$), **Thm 5** (the trichotomy — the proof of Figure 3),
    **Thm 6** ($S'=S\cup Z$, the extraneous-solution theorem) with **Cor 6a** (checking is the
    second half of the proof) and **Cor 6b** (squaring merges $L=R$ with $L=-R$ — the nb 08
    Trap 7 debt paid), and **Thm 7** (dividing deletes solutions), closed by a five-row table
    of which moves are safe and what each dangerous one does.
  - The mnemonic stated once, plainly: multiplying makes the equation bigger, so the answer set
    grows (fakes); dividing makes it smaller, so the answer set shrinks (losses).
  - Traps (9), including the two that are really *habits*: write the domain **before** the
    algebra, and check in the **original** equation, never in the cleared one.
  - Worked examples 1–13: named-step basics; both sides; brackets; numeric LCD; decimals;
    an identity; a contradiction; a rational equation whose only candidate is fake (with the
    "the curves are always exactly 1 apart" reason); a rational equation with a genuine answer
    (cross-multiplication named as Theorem 6, not as a separate rule); one that only *looks*
    quadratic; two **literal** equations; a **parameter** equation whose three cases are exactly
    Theorem 5; and a first word problem, answered in a sentence and checked against the words.
  - Python: `sp.Eq` vs `==`; **`solveset` vs `solve`** shown side by side so that `[]` meaning
    both "none" and "all" is visible; an exact checker using `.subs` + `simplify` + `sp.zoo`;
    clearing denominators by hand with `sp.cancel` and watching the fake root appear, then
    confirming $S'=S\cup Z$ *as an equality of SymPy sets*; and his own `solve_linear` written
    straight from Theorems 3–4 and raced against SymPy.
  - **Numerical-analysis lesson 7:** `(0.1+0.2)-0.3` as the coefficient $a$ turns "no solution"
    into $x\approx1.8\times10^{16}$; the fix (compare with a tolerance, never `== 0`); then
    **ill-conditioning** introduced by name with nearly parallel lines, and pointed forward to
    systems of equations and to training networks.
  - 9 figures: the balance scale before/after a legal move; two lines crossing at $x=4$; the
    three shapes with their solution sets drawn on number lines underneath; the chain of
    equivalent equations, four panels, crossing pinned at $x=4$; multiplying by zero collapsing
    two lines into one; the fake solution being born at the zero of $E$; cancelling $(x-1)$
    deleting a real root; the parameter example as a curve with a wall at $k=-2$ and a green
    band at $k=2$; and the ill-conditioning pair.
- **What went well:** nothing to judge — still no answers from him, in any notebook.
- **Mistakes to revisit:** none recorded (see "Known Weak Spots" for what to look for).
- **Homework given:** the 20 exercises of notebook 09. 14–16 are Python (his own Theorem-5
  solver; an extraneous-solution detector; breaking Theorem 5 with floats on purpose). 17–20 are
  proofs, ending with the linear identity theorem — the statement behind "two different lines
  cannot cross twice".
- **Next session plan:** (1) **ask for answers first** — the cheapest asks in the whole course
  are now Ex 16 (three lines of code + two sentences) and Ex 13 (find two mistakes, no
  calculation at all); (2) if he insists on continuing, run the seven oral questions of § 8,
  especially Q5, Q6 and Q7; (3) then open **Equations and Inequalities § 2 — Quadratic
  Equations** (→ `notebooks/10-quadratic-equations.ipynb`), where the zero-product property is
  already the engine, Theorem 5 has already made "how many solutions?" a real question, and
  $S=\varnothing$ over $\mathbb{R}$ becomes the door into § 3 *Complex Numbers*.

### Session 8 — 2026-08-22 — nth Roots; Rational Exponents

- **Topic taught:** Review § 8, *nth Roots; Rational Exponents* (eighth and last topic of the
  Review chapter). He wrote "please continue next topic", with no exercise answers again. Eighth
  time; noted in one line and taught.
- **Notebook created:** `notebooks/08-nth-roots-rational-exponents.ipynb` — 77 cells, 39 code
  cells, 11 matplotlib figures, no ASCII art, every cell carries an `id`. Verified: executes top
  to bottom with no errors (`uv run jupyter nbconvert --to notebook --execute`). No new
  dependency — numpy, sympy, matplotlib, plus `fractions` from the standard library.
- **What is inside:**
  - **§0 recall table** (kept from nb 07): the ten earlier results this notebook stands on, plus
    three warm-up questions. Spaced repetition, since none of them is confirmed.
  - Intuition: the root as a broken "undo" button; the even/odd split drawn with horizontal
    lines; the root as the **mirror image of a power in the line $y=x$**; the fifth telling of
    the "we had a system, something was missing, we built a bigger one" table, with $\sqrt x
    \notin\mathbb{R}(x)$ (nb 07 Ex 20) as the new bottom row; the family $y=x^{1/n}$; and
    $\sqrt{ab}$ **constructed with a semicircle** (nb 03 similar triangles), which hands AM–GM
    over for free.
  - Definitions 1–4: an $n$th root, the principal root (with the even/odd/negative table), a
    radical expression and its domain, simplest radical form.
  - Theorems, all fully proved: Lemma 1 (powers keep the order, from the nb 04 telescoping
    identity — no induction), **Corollary 1a (uniqueness)** which becomes the engine of the whole
    notebook, Lemma 2 (a power cannot jump), **Theorem 1 (existence by $\sup$)** generalising
    nb 02 Thm 7 from $n=2$ to every $n$ with both cases killed explicitly, Theorem 2 (odd index:
    always exactly one root; even index and negative radicand: none), **Theorem 3 ($\sqrt[n]{a^n}
    =|a|$ or $a$)**, Theorems 4–6 (product, quotient, root of a root), Theorem 7 (roots keep the
    order — sold as a *calculator-free comparison machine*), **Theorem 8 (no sum law, with the
    direction proved from the binomial theorem)**, Theorem 9 (AM–GM, proved algebraically to
    match the picture), **Theorem 10 (rational exponents are well defined)** and **Theorem 11
    (the four exponent laws for rationals)**.
  - Named the **three-line uniqueness pattern** out loud and then reused it in six proofs, so the
    technique is visible as a technique, not as six tricks.
  - Traps section (7): dropping the bars; splitting over a $+$; the $1=-1$ fake proof and exactly
    which hypothesis of Thm 4 it breaks; **simplifying that quietly changes the domain**
    ($\sqrt{x-1}\sqrt{x+1}$ vs $\sqrt{x^2-1}$, drawn); the invented rule for $\sqrt{x^2+9}$;
    a negative base with a fractional exponent ($(-8)^{1/3}$ vs $(-8)^{2/6}$); and extraneous
    solutions, flagged and postponed to the Equations chapter.
  - The honest gap stated plainly: $2^{\sqrt2}$ needs limits. Drawn as rational exponents filling
    in the curve — same treatment as the circle area (nb 03) and the asymptote (nb 07).
  - Worked examples 1–12: two simplifications (odd index, then the even one with the bars live);
    like radicals; multiplying out; **three rationalised denominators** including the cube-root
    conjugate from $u^3-v^3$; **rationalising the numerator of the difference quotient of
    $\sqrt x$** (second calculus teaser, after nb 07's $1/x$); two exponent simplifications;
    factoring out the smallest (negative) power; a domain table; comparing $\sqrt[3]5$ with
    $\sqrt[4]{11}$ by 12th powers; and un-nesting $\sqrt{7+4\sqrt3}$.
  - Python: the four ways to ask for a root and when each lies (`**(1/n)` returning a **complex**
    number, `np.sqrt` giving `nan`, `np.cbrt`, `sp.root` vs **`sp.real_root`**); exact vs float
    with `radsimp` and `sqrtdenest`; **`sp.refine(sqrt(x**2), Q.real(x)) -> Abs(x)`** to show
    SymPy refusing to drop the bars until it is allowed to; the four exponent laws tested on
    200 000 random cases *and then* proved symbolically; Trap 6 measured; **Theorem 1's proof run
    as bisection and raced against Newton's method** (41 steps vs 8 for $10^{-12}$).
  - **Numerical-analysis lesson 6:** catastrophic cancellation in $\sqrt{x+1}-\sqrt x$ — the
    naive form reaches 100% relative error at $x=10^{16}$, the rationalised form stays at machine
    precision everywhere. The point made explicitly: "rationalise the numerator" is not an
    old-fashioned habit, it is the difference between an answer and noise.
  - 11 figures: even vs odd powers; the mirror in $y=x$; the family $x^{1/n}$; the semicircle
    construction of $\sqrt{ab}$; the bisection brackets closing in (inside the proof, plus a log
    plot of the width); $\sqrt{x^2}$ vs $x$ against $\sqrt[3]{x^3}$ vs $x$; $\sqrt{a+b}$ vs
    $\sqrt a+\sqrt b$; the domain mismatch of Trap 4; $2^{k/n}$ filling in $2^x$; bisection vs
    Newton error curves; and the cancellation error on log–log axes.
- **What went well:** nothing to judge — still no answers from him, in any notebook.
- **Mistakes to revisit:** none recorded (see "Known Weak Spots" for what to look for).
- **Homework given:** the 20 exercises of notebook 08. 14–16 are Python (bisection root written
  from the proof; Newton vs bisection; breaking $\sqrt{x+1}-\sqrt x$ on purpose). 17–20 are
  proofs, ending with the deliberately-too-hard "$\sqrt[n]{x}$ is not a rational expression, or
  say exactly where you are stuck".
- **Next session plan:** (1) **ask for answers first** — cheapest ask is Ex 14–16 of this
  notebook; (2) if he insists on continuing, run the six oral questions of § 10, especially Q2
  (bars, argued from the definition), Q4 ("well defined") and Q5 ("the theorem is wrong" vs "the
  theorem does not apply"); (3) then open the new chapter, **Equations and Inequalities § 1 —
  Linear Functions**, in `notebooks/09-linear-functions.ipynb`.



### Session 7 — 2026-08-21 — Rational Expressions

- **Topic taught:** Review § 7, Rational Expressions (seventh topic in `math-topic.md`). He said
  "please continue next topic" again, in the same session as notebook 06. I noted the backlog in
  one line and taught.
- **Notebook created:** `notebooks/07-rational-expressions.ipynb` — 78 cells, 36 code cells,
  10 matplotlib figures, no ASCII art, every cell carries an `id`. Verified: executes top to
  bottom with no errors (`uv run jupyter nbconvert --to notebook --execute`). No new dependency —
  numpy, sympy, matplotlib only.
- **What is inside:**
  - **§0 "What we need from before"** — new this session: a recall table of the nine results from
    nb 01/04/05/06 that the notebook uses, plus two warm-up questions. Spaced repetition, since I
    still have no evidence any of them landed.
  - Intuition: the $\mathbb{Z}\to\mathbb{Q}$ / $\mathbb{R}[x]\to\mathbb{R}(x)$ table (same
    step, twice); the square-bracket vs round-bracket notation; the new danger (forbidden
    points); and the famous trap drawn as a **hole** in the line $y=x+1$.
  - Definitions 1–9: rational expression, domain, the rational function, **two meanings of
    equality**, lowest terms, proper/improper, LCD, complex fraction, and **field**.
  - Theorems 1–11 with full proofs: Thm 1 (at most $\deg q$ forbidden points, so the domain is
    infinite — the fact that makes everything else work); **Thm 2 (cross-multiplying is legal)**,
    proved with nb 04 Thm 8, which is what lets us move between the two meanings of "equal";
    Thm 3 (cancelling, plus a formal explanation of why "cancel a term" is not a special case —
    it needs $x\mid x+3$, which the factor theorem refutes); Thm 4 (the four operations, proved by
    *transporting* the number rules through Thm 2 — the proof technique is named and reused);
    **Thm 5 ($\mathbb{R}(x)$ is a field)** with the price of the extension made explicit;
    Lemma 6a (Bezout with constant gcd), Lemma 6b (cancellation lemma), **Thm 6 (lowest terms:
    existence and uniqueness up to a constant)**; Thm 7 (polynomial part + proper part, unique);
    Lemma 8a (divisibility in factored form) and **Thm 8 (LCD)**; **Thm 9 (hole vs wall)** — and
    here I stopped and said out loud that "runs off to infinity" is a **limit** statement we have
    not earned yet, exactly like the circle-area gap in nb 03; **Thm 10 (Lagrange
    interpolation)** with the switch-polynomial trick; **Thm 11 (partial fractions for distinct
    linear factors)** with the **cover-up formula**, proved *through* Lagrange rather than by
    solving a system.
  - Traps section (9): cancel a term; domain after simplifying; reversed bracket; the invented
    addition rule $\frac1a+\frac1b=\frac1{a+b}$; the lost minus sign; multiplying the LCD out
    too early; treating an expression like an equation; half-multiplying a complex fraction; and
    calling every forbidden point a wall.
  - Worked examples 1–12: domains (including one with an empty forbidden set); simplify;
    reversed bracket; multiply; divide; add with the LCD; subtract with the minus-sign trap live;
    a complex fraction **both ways**; improper split **using the nb 06 synthetic table**; the
    **difference quotient of $1/x$** (calculus teaser); partial fractions by cover-up; and a full
    analysis of $\frac{x^2-x-6}{x^2-9}$ (domain, reduce, classify each forbidden point, find the
    zero) drawn in one figure.
  - Python: a five-command SymPy tour (`factor`, `cancel`, `together`, `apart`, `simplify`) with a
    table of what each one *promises*; a `forbidden_values` function that reads the denominator
    **as written** — and a deliberate demonstration that calling `sp.together` first silently
    cancels and hands back the wrong domain (Trap 2, but committed by the library); an honest
    plotter using `np.nan` shown against the naive plot with its fake vertical line; the
    subtract-and-simplify-to-zero habit used as a **trap detector**; `my_lcd` built from
    `factor_list` (Thm 8) checked against `sp.lcm`; `cover_up` (Thm 11) checked against
    `sp.apart`; and `lagrange` (Thm 10) with a two-panel figure showing the unique cubic and the
    four switch polynomials.
  - **Fifth numerical-analysis lesson (§ 6.6):** the difference quotient of $1/x$ at $x=2$,
    computed raw and simplified, with an exact `Fraction` judge. The raw form loses accuracy as
    $h$ shrinks ($2.7\times10^{-16}$ at $h=10^{-1}$, $2.5\times10^{-1}$ at $h=10^{-16}$, where it
    returns exactly $0$); the simplified form stays at $10^{-17}$ throughout. Log-log figure. The
    lesson is the friendliest of the five: for once **doing the algebra fixes the numerics**, and
    it explains why calculus cancels the $h$ by hand before letting it go to zero.
  - **§8 "Still owed"** — limits; asymptotes properly; partial fractions with repeated factors
    and irreducible quadratics; and why `sp.cancel` uses the Euclidean algorithm rather than full
    factorisation.
  - 10 figures: the hole in $y=x+1$; factor-vs-term cancelling side by side; the polynomial part
    as what the curve hugs far away; the LCD exponent bars; hole vs wall; the partial-fraction
    overlay; the full analysis of one expression; naive plot vs `np.nan` plot; Lagrange plus the
    four basis polynomials; and the difference-quotient error curve.
- **What went well:** nothing to judge — still no answers from him for any of the seven
  notebooks.
- **Mistakes to revisit:** none recorded (still no answers).
- **Homework given:** the 20 exercises in notebook 07. Ex 1–12 by hand (domains, lowest terms,
  reversed brackets, multiply/divide, LCD sums, the minus-sign trap, complex fractions both ways,
  the improper split with a part that synthetic division **cannot** do, three difference
  quotients, hole-or-wall classification, cover-up partial fractions, and the average-speed
  problem ending in an AM-HM inequality). Ex 13–16 Python (a `describe` function that classifies
  every forbidden point; write your own `cancel` from `factor_list`; write `cover_up` and then
  **break it on a repeated factor and name the hypothesis that failed**; and repeat the
  difference-quotient experiment for $1/x^2$ with a `Fraction` judge). Ex 17–20 proofs:
  $\frac1a+\frac1b=\frac1{a+b}$ has no real solutions (discriminant); the reduced denominator
  divides the original (Lemma 6b); partial fractions the slow way and why Lagrange reaches
  further; and the capstone **$\sqrt x\notin\mathbb{R}(x)$** by a degree-parity argument,
  explicitly compared with the $\sqrt2$ proof of notebook 01 — which is also the doorway to
  topic 8.
- **Next session plan:** (1) **ask for answers first** — the Python sets (nb 06 Ex 12–16 or nb 07
  Ex 13–16) if he wants the smallest possible task. (2) If he insists on continuing, the six oral
  questions at the end of notebook 07 first. (3) Only then teach **nth Roots; Rational
  Exponents**, opening with his own Exercise 20: he will have proved the hole exists, so the new
  numbers have a reason to be built.


### Session 6 — 2026-08-21 — Synthetic Division

- **Topic taught:** Review § 6, Synthetic Division (sixth topic in `math-topic.md`). He said
  "please continue next topic". I flagged the six-notebook marking backlog in one line and
  taught anyway, as agreed with myself last session.
- **Notebook created:** `notebooks/06-synthetic-division.ipynb` — 77 cells, 36 code cells,
  9 matplotlib figures, no ASCII art. Verified: executes top to bottom with no errors
  (`uv run jupyter nbconvert --to notebook --execute`). No new dependency — numpy, sympy,
  matplotlib only. Every cell carries an `id`, so nbformat gives no warning.
- **What is inside:**
  - Intuition: the letters $x^3,x^2,x$ in a long division never influence a decision, they
    only say *which column* — and position already says that. Delete them and three rows of
    numbers remain. Second idea: divide by $x-c$ and **add** instead of subtracting, which
    removes the sign mistakes. Opening figure draws the long division and the synthetic table
    side by side with the same numbers highlighted.
  - Two warnings given before anything else: **write a $0$ for every missing power**, and the
    corner number is $c$, from "$x$ **minus** something" (table of divisor → $c$).
  - Definitions 1–4: monic linear divisor; **the synthetic recurrence** $b_{n-1}=a_n$,
    $b_{k-1}=a_k+cb_k$, $r=a_0+cb_0$ (stated as a boxed recipe *and* in words); divides;
    multiplicity. Explicit note that this notebook uses **highest power first**, the opposite
    of the Horner function in nb 04 — the order mismatch is named as a classic bug.
  - Theorems 1–11, all fully proved: Thm 1 (division by $x-c$: the remainder is a *number*,
    $\deg q=n-1$, existence **and uniqueness**, from nb 04 Thm 5); **Thm 2 (synthetic
    division is correct)** — multiply $(x-c)q+r$ out, collect powers, and show the three
    lines of Definition 2 are exactly the coefficient equations, with a paragraph afterwards
    hammering that the recurrence is *forced*, not invented; Thm 3 (remainder theorem, one
    line, plus a figure showing $r$ as the height of the graph); **Thm 4 (Horner = synthetic
    division)**, by induction, so the course's two algorithms become one; Thm 5 (factor
    theorem in table form, where the *uniqueness* of Thm 1 does the real work); Thm 6 (cost:
    exactly $n$ multiplications vs $\sim n^2/2$); **Thm 7 (deflation detects multiplicity)**,
    by induction, using the zero-product/degree rule of nb 04; **Thm 8 (expansion in powers
    of $(x-c)$)** — existence by strong induction, uniqueness by substituting $x=c$ and
    dividing, plus the $y=x-c$ change-of-variable view and an explicit forward pointer to
    Taylor; Thm 9 (divisor $ax-b$: quotient $\div a$, **remainder unchanged**); Thm 10
    (upper bound for real roots); Thm 11 (lower bound, alternating signs) — proved directly
    with the $(-1)^{n-1-k}b_k\ge0$ bookkeeping rather than hand-waved through $p(-x)$.
  - Worked examples 1–9: the basic table; missing powers with $x^4-16$ and the "what goes
    wrong without the zeros" note; a fractional $c$ **and** a non-monic divisor $2x-1$ via
    Thm 9; evaluation only (Horner by hand); finding an unknown coefficient $k$ without
    dividing; **factoring completely by repeated deflation** with both the multiply-back and
    the $x=1$ check; **measuring multiplicity** (a triple root, four runs shown as a table);
    the $(x-2)$ expansion done by hand and expanded back; and fencing the roots of a cubic
    into $[-3,4]$ with two tables.
  - Python: `synthetic_division` written straight from Definition 2 (six lines) with exact
    `Fraction` support; a reusable **`draw_synthetic` matplotlib table-drawer**; a
    **200-random-case check against `sp.div`** (all agree) with the habit named out loud —
    always test your mathematics against an independent implementation; remainder theorem by
    three routes; `peel_all_rational_roots` = rational root theorem + deflation, checked
    against `sp.factor`; `expand_about` (Thm 8) checked against SymPy including a
    fractional $c=1/3$; and `root_bounds` implementing Thms 10–11 against `np.roots`.
  - **Fourth numerical-analysis lesson (§ 5.8): deflation order.** With
    $p=(x-0.001)(x-0.5)(x-1)(x-3)(x-7)(x-1000)$, peeling the largest root first gives a first
    remainder of $24.2$ instead of $0$ and a quotient with relative error $6.6\times10^{-4}$;
    peeling the smallest first stays at $2\times10^{-16}$. Explained by the error-amplification
    factor $|c|$ per step in $b_{k-1}=a_k+cb_k$, drawn as a log-scale bar chart, and closed
    with the three lessons — peel smallest first, a correct theorem plus correct code is still
    not enough, and real root-finders polish against the *original* polynomial. Links back to
    the cancellation lessons of nb 03/04 and the ill-conditioning lesson of nb 05.
  - 9 figures: long division vs the table; the remainder as a graph height; the cost curves
    plus the speed-up ratio; deflation before/after; the $(x-c)$ partial sums rebuilding $p$;
    the upper-bound "forbidden zone"; two drawn synthetic tables from `draw_synthetic`; and
    the deflation-order bar chart.
- **What went well:** nothing to judge — still no answers from him for any of the six
  notebooks.
- **Mistakes to revisit:** none recorded (still no answers).
- **Homework given:** the 20 exercises in notebook 06. Ex 1–11 are by hand (tables, missing
  powers, the sign of $c$, evaluation, factor tests, a non-monic divisor with the
  divide-the-remainder trap, unknown coefficients, complete factoring, multiplicity, the
  $(x-c)$ expansion, root bounds). **Ex 12–16 are Python** — and this is the first notebook
  that makes him write real code: implement the algorithm from the definition with the
  coefficient order *reversed*, a one-pass divide-and-evaluate, a multiplicity counter with
  `Fraction`, `expand_about` plus a partial-sum figure, and a repeat of the deflation-order
  experiment including a `Fraction` run. Ex 17–20 are proofs: the closed formula
  $h_i=\sum_j a_{n-j}c^{i-j}$ by induction; integer rows stay integer, and deducing "an
  integer root divides $a_0$" (half of the rational root theorem, by a second route);
  **the two multiplicity tests agree** (Thm 7 $\iff$ Thm 8, needs the uniqueness half); and
  a two-part uniqueness capstone — any correct method must produce our $q$ and $r$, plus an
  honest attempt at the lower bound on the number of additions, where he is explicitly asked
  to say precisely where he gets stuck.
- **Next session plan:** (1) **ask for answers first.** If six notebooks feel too big, ask
  only for **Ex 12–16 of notebook 06** — code is quick to mark and impossible to fake. Then
  mark notebook 01 forwards. (2) If he insists on continuing, run the six oral questions at
  the end of notebook 06 (§ 7) first: why only $x-c$; where the recurrence came from; why the
  remainder is a number; what Horner throws away; which theorem proves two different
  quotients cannot both be right; and why peeling order can destroy a correct theorem.
  (3) Only then teach **Rational Expressions**, opening with the cancel-a-factor-not-a-term
  trap planted in notebook 05.


### Session 5 — 2026-08-20 — Factoring Polynomials

- **Topic taught:** Review § 5, Factoring Polynomials (fifth topic in `math-topic.md`). He
  said "continue next topic" again, so I taught rather than marked — see Current Focus for
  why this is now a problem.
- **Notebook created:** `notebooks/05-factoring-polynomials.ipynb` — 82 cells, 42 code
  cells, 11 matplotlib figures, no ASCII art. Verified: executes top to bottom with no
  errors (`uv run jupyter nbconvert --to notebook --execute`). No new dependency — numpy,
  sympy, matplotlib only.
- **What is inside:**
  - Intuition: factoring is **un-multiplying**; easy forwards, hard backwards, and that
    asymmetry is what cryptography is built on. The rectangle picture: multiplying = you
    know the sides and want the area, factoring = you know the area and want the sides.
    A table showing what each form (expanded vs factored) tells you at a glance. The
    number-system warning ($\mathbb{Q}$ vs $\mathbb{R}$) given early and repeated. Ends with
    the five-step **checklist** that the rest of the notebook proves.
  - Definitions 1–9: divides/factor, factorisation, **unit** and trivial factorisation,
    **irreducible** (over a stated $F$), completely factored, GCF/content, monic,
    **multiplicity**, quadratic in form. Also introduces the notation $\mathbb{Z}[x]$,
    $\mathbb{Q}[x]$, $\mathbb{R}[x]$.
  - Theorems, all fully proved: Thm 1 (zero-product for polynomials — the reason we factor
    at all, with the "$(x+1)(x-3)=5$ is not allowed" warning); Thm 2 (GCF extraction, with
    the **uniqueness** half proved so that "divide each term by the GCF" is legal);
    Thm 3 (grouping); Thm 4 (the six factoring identities, each proved, with the sum of
    cubes *derived from* the difference of cubes rather than re-proved); Thm 5 (monic
    trinomial, both directions, using the identity theorem of nb 04); Thm 6 (the **$ac$
    method**, proved via $a(ax^2+bx+c)=(ax+m)(ax+n)$); Thm 7 (**completing the square**);
    Thm 8 (**a real quadratic is reducible iff $D\ge0$** — both directions, the $D<0$ case
    by contradiction on degrees); Thm 9 (peel a root off, which re-proves nb 04 Thm 8 in a
    line).
  - **The rational root theorem done properly.** Fact (integer division with remainder, from
    well-ordering); **Lemma 10 = Bézout's identity**, proved by taking the smallest positive
    combination; Lemma 11 (coprimality survives powers) proved with the **binomial theorem**
    from nb 04; **Thm 12 (rational root theorem)** with both halves; Cor 13 (monic ⇒ integer
    roots) presented as an **irrationality machine**. Explicit note that the theorem finds
    only *rational* roots, and that finding none is a real answer.
  - **§3.9, the summit (marked as the hardest section, nothing depends on it):** the table
    "whole numbers vs polynomials" (size ↔ degree, primes ↔ irreducibles, division with
    remainder in both), then Lemma 14 (**Bézout for polynomials**), Lemma 15 (**Euclid's
    lemma for polynomials**), Thm 16 (**unique factorisation**, existence by strong
    induction, uniqueness via Lemma 15). The point made explicitly: it is the *same proof
    twice*, and the reusable move is "Bézout turns coprimality into an equation $=1$, then
    multiply that equation by whatever you want to divide". Ends with a dependency table.
  - Traps section (9 of them): forgetting the GCF; using zero-product when the side is not
    zero; "a sum of squares must factor"; stopping too early; **cancelling a term instead of
    a factor** (planted deliberately as the bridge to notebook 07); the sign of $(x-r)$;
    **"no real root" ≠ "irreducible"** with $x^4+4$; counting roots without multiplicity;
    factoring vs solving.
  - Worked examples 1–12: GCF with a negative leading term; grouping; difference of squares
    applied twice; monic trinomial with the pair table; the $ac$ method with the *reason* the
    grouping works; perfect square **and a near miss**; cubes with a hidden GCF; the **full
    algorithm** on $2x^3-3x^2-11x+6$ (checklist → rational roots → peel → quadratic, with
    both the multiply-back and the $x=1$ check); quadratic in form; solving with Trap 2 shown
    failing *and giving one right answer by luck*; the open-box volume from nb 04 factored as
    $4x(x-10)(x-15)$ so that the domain $0<x<10$ is now **proved** rather than argued; and a
    full **sign chart**.
  - Python: a SymPy tour (`factor`, `factor_list` read as multiplicity data, `expand`,
    multi-letter identities); the number system demo (`extension=sqrt(2)`, `gaussian=True`,
    and $x^4+4$ vs $x^4+1$); then **our own tools from scratch** on coefficient lists —
    `poly_str`, `content_and_primitive`, `divisors`, `rational_root_candidates`, `horner`
    (which already returns the quotient — deliberate seed for notebook 06), and
    `factor_rational_roots`, all checked against SymPy; the Theorem 4 identities verified by
    *subtracting and simplifying to zero*; a discriminant verdict function; and finally
    **Wilkinson's polynomial** — roots $1..15$, one coefficient changed by 1 part in $10^9$,
    and the roots fly off the real line (largest imaginary part ≈ 0.42). Named as
    **ill-conditioning** and linked forward to condition numbers in machine learning.
  - 11 figures: the rectangle factorisation; roots as crossings; $x^2-2$ vs $x^2+1$;
    completing the square as a literal square with the missing corner; the three
    discriminant cases; the rational-root candidate ticks with the real roots marked; the
    twin factor trees ($60$ and $x^4-16$); simple root crossing vs double root touching;
    $x^4-5x^2+4$ with all four roots; the two-panel sign chart; and the Wilkinson root
    scatter in the complex plane.
  - Ends with an honest "still owed" list: the fundamental theorem of algebra (needs complex
    numbers), Abel's theorem (no formula for degree $\ge5$), and how a computer really
    factors.
- **What went well:** nothing to judge — still no answers from him for any of the five
  notebooks.
- **Mistakes to revisit:** none recorded (still no answers).
- **Homework given:** the 20 exercises in notebook 05. Ex 11–13 are Python (write a GCF
  extractor; write an exact rational-root finder and show what floats do to it; plot a
  quartic, mark the double root from the picture alone, and build its sign chart).
  Ex 17–20 are proofs: the sum of cubes plus $a^2-ab+b^2>0$; **$x^2+bx+c$ factors over
  $\mathbb{Z}$ iff $b^2-4c$ is a perfect square** (includes a parity argument, the hardest
  step of the set); the rational root theorem as an irrationality machine ($\sqrt[3]2$,
  $\sqrt7$, and the general statement); and the capstone **$x^4+4=(x^2-2x+2)(x^2+2x+2)$**
  with both factors proved irreducible, ending with "why does no-real-root prove
  irreducibility for degree $\le3$ but not for degree 4?".
- **Next session plan:** (1) **ask for his answers before teaching anything.** Five sets are
  outstanding; mark 01 first. (2) Oral quiz, five minutes, before any new notebook: why does
  factoring help us solve equations, and why only when one side is $0$; what does
  "irreducible" depend on; state the rational root theorem and say why the search is finite;
  what is the difference between "no real root" and "cannot be factored"; and the two halves
  of an induction proof (still unverified after two induction proofs).
  (3) Only then teach **Synthetic Division**, and make him write the code himself this time.

### Session 4 — 2026-08-20 — Polynomials

- **Topic taught:** Review § 4, Polynomials (fourth topic in `math-topic.md`). He said
  "continue next topic", so I taught rather than marked — see Current Focus.
- **Notebook created:** `notebooks/04-polynomials.ipynb` — 90 cells, 38 code cells,
  12 matplotlib figures, no ASCII art. Verified: executes top to bottom with no errors
  (`uv run jupyter nbconvert --to notebook --execute`). No new dependency — numpy, sympy,
  matplotlib only.
- **What is inside:**
  - Intuition: a polynomial is a recipe made only of $+,-,\times$ — and the reason that
    matters is that *a computer can only add, subtract and multiply*. A table of
    non-examples with the exact rule each one breaks. Bricks ($1,x,x^{2},\dots$), a
    polynomial as a weighted sum of bricks, and a coefficient list as its true identity.
  - The degree presented as "the number that wins far from zero", with a three-window
    zoom-out figure showing $2x^{3}-5x+7$ becoming indistinguishable from $2x^{3}$.
  - Definitions 1–12: monomial, polynomial, the $\sum$ notation explained as a Python `for`
    loop, degree / leading coefficient / standard form, names by degree and by term count,
    equality of polynomials, sum / difference / **product via the convolution formula**,
    polynomial function, root, divides, several variables, factorial, binomial coefficient.
  - Theorems, all fully proved: Thm 1 (closure, and the product formula *derived* rather
    than assumed); Thm 2 (degree rules, including why the zero polynomial gets no degree);
    Thm 3 (the seven special products, each proved); Thm 4 ($a^{n}-b^{n}$ by telescoping);
    **Thm 5 (division algorithm — existence by strong induction, and uniqueness)**;
    Thm 6 (remainder theorem); Thm 7 (factor theorem, both directions); Thm 8 (at most $n$
    roots, by induction); **Thm 9 (identity theorem)** with an explicit note that it can
    fail over a finite number system; Lemma 10 (Pascal's rule); **Thm 11 (binomial theorem,
    by induction)** with the index-renaming step written out in full.
  - Traps section (8 of them), including $\deg(p+q)=\max$, "degree 5 means 5 real roots",
    and $x^{3}$ versus $3^{x}$ with a log-scale growth-race figure.
  - Worked examples 1–9: reading a polynomial; add/subtract with a deliberate degree drop;
    multiply with the "put $x=1$" self-check; special products including mental arithmetic
    ($103\times97$); **long division with every step shown** and checked by multiplying
    back; remainder/factor theorem shortcuts; $(2x-3)^{5}$ by the binomial theorem as a
    table; comparing coefficients to rewrite $x^{2}$ in powers of $(x-1)$ — announced as
    the first case of a **Taylor expansion**; and the open-box volume $V(x)=4x^{3}-100x^{2}
    +600x$ with a real discussion of its domain and a calculus teaser for the maximum.
  - Python: hand-written `poly_add` / `poly_sub` / `poly_mul` / `degree` on coefficient
    lists, checked against SymPy; **Horner's method** with a multiplication count against
    the naive method; **long division implemented from the proof of Thm 5** and checked
    against `sp.div`; a SymPy command tour; the binomial theorem checked for $n\le6$ (with
    an explicit note that checking is not proving); `np.polyfit` finding the unique cubic
    through 4 points; and the $(x-1)^{7}$ cancellation experiment — the expanded form's
    error is ~200x larger than the true value.
  - 12 figures: the bricks; a polynomial as a sum of pieces; the three-window zoom-out;
    roots of degree 1/2/3; the cut-and-turn proof of $a^{2}-b^{2}$; the $f=qg+r$ degree-bar
    diagram; two cubics agreeing at exactly 3 points; Pascal's triangle with the rule shown
    by arrows; $x^{3}$ vs $3^{x}$; the card-and-box pair; the 4-point cubic fit; and the
    catastrophic-cancellation pair.
  - Ends with a dependency table (which theorem rests on which) and an honest "still owed"
    list: the box maximum needs calculus, and "exactly $n$ roots" needs complex numbers and
    the fundamental theorem of algebra.
- **What went well:** nothing to judge — still no answers from him for any notebook.
- **Mistakes to revisit:** none recorded (still no answers).
- **Homework given:** the 20 exercises in notebook 04. Exercises 11–13 are Python (write
  Horner yourself and check against SymPy; `poly_pow` compared with Pascal's row 10; plot a
  cubic and count its roots against Theorem 8). Exercises 17–20 are proofs: $x-1$ divides
  $f$ iff the coefficients sum to zero; **there is no polynomial $p$ with $x\,p(x)=1$** (the
  honest reason $1/x$ is not a polynomial); $(a-b)\mid(f(a)-f(b))$ for integer coefficients,
  with an application; and even polynomials have only even-power terms, plus stating the odd
  case.
- **Next session plan:** (1) **ask for his answers before teaching anything** — four sets
  are outstanding and the weak-spot list is still pure guesswork; mark 01, then 02, 03, 04;
  (2) quiz him out loud on: why $1/x$ is not a polynomial, what the remainder theorem says
  and why the remainder is a *number*, why "equal for all $x$ $\Rightarrow$ equal
  coefficients" is a theorem and not a definition, and the two halves of an induction proof;
  (3) only then teach **Factoring Polynomials**.

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
