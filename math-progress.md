# Math Learning — Progress Log

> This file is my long-term memory of what we've covered. I READ it at the start of every
> session and UPDATE it at the end. Newest entries at the top of the Session Log.

## Skill Ledger

*(A skill enters this list only after the exercises are done and checked.)*

### Topic 1 — Real Numbers (taught 2026-08-19, exercises **not yet checked**)
- [ ] Name the families $\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R}$ and place a number in the right one
- [ ] State the field axioms (A1–A6) and the order axioms (O1–O4)
- [ ] Prove from the axioms: $a\cdot 0 = 0$, $(-1)a = -a$, zero-product property
- [ ] Prove $\sqrt{2}$ is irrational (proof by contradiction + contrapositive lemma)
- [ ] Convert a repeating decimal to a fraction and explain *why* the trick works
- [ ] Absolute value as distance; prove the triangle inequality
- [ ] Idea of the completeness axiom (supremum, "the line has no holes")
- [ ] SymPy: `Rational`, `sqrt`, `is_rational`, `N`; why floats are only approximations
- [ ] NumPy arrays + `np.abs`, `np.all`, `np.isclose`; Matplotlib: a simple number-line plot

### Topic 2 — Algebra Essentials (taught 2026-08-19, exercises **not yet checked**)
- [ ] Algebraic expression, evaluation, **domain of a variable** (no division by 0, no even root of a negative)
- [ ] Tell an *identity* from an *equation*; test equivalence by simplifying the difference to 0
- [ ] State and use the principle of **mathematical induction** (base case + inductive step)
- [ ] Prove E1 $a^ma^n=a^{m+n}$, E2 $(a^m)^n=a^{mn}$, E3 $(ab)^n=a^nb^n$ by induction
- [ ] Explain why $a^0=1$ and $a^{-n}=1/a^n$ are **forced** definitions, not conventions
- [ ] Prove $\sqrt{a^2}=|a|$ (R2) and $\sqrt{ab}=\sqrt a\sqrt b$ for $a,b\ge 0$ (R3); know why the sign condition matters
- [ ] Prove that multiplying an inequality by a negative number reverses it (O5); reciprocals (O6)
- [ ] Scientific notation, and its link to how floats are stored
- [ ] SymPy: `symbols`, assumptions (`real=True`, `positive=True`), `subs`, `expand`, `factor`, `simplify`, `refine`, `solveset`, `continuous_domain`, `lambdify`

## Current Focus

**Topics 1 and 2 are taught; both sets of exercises are still open.** Both notebooks were
generated and executed top to bottom with no error. Next: I check the exercise answers, then
teach **Topic 3 — Geometry Essentials**.

## Known Weak Spots

*(Empty for now — fresh restart. I will fill this in from the exercise answers.)*

Things to watch for in Topic 1, based on what usually goes wrong:
- Ex. 11 & 18 — irrational $\times$ irrational vs. rational $\times$ irrational (the $r \neq 0$ condition)
- Ex. 15 — supremum that is **not** an element of the set
- Ex. 17, 20 — reusing the $\sqrt{2}$ proof structure for $\sqrt{3}$ and $\sqrt{2}+\sqrt{3}$
- Ex. 19 — the reverse triangle inequality (needs two applications of Theorem 7)

Things to watch for in Topic 2:
- Ex. 5 & 17 — dropping the absolute-value bars in $\sqrt{a^2}$
- Ex. 7 — forgetting to flip the inequality after multiplying/dividing by a negative
- Ex. 10, 16, 20 — writing a *complete* induction proof (base case stated, hypothesis used explicitly)
- Ex. 8 — expressions that agree everywhere except at one excluded point (domain traps)
- Ex. 1 — the difference between $-2^4$ and $(-2)^4$

## Session Log

### 2026-08-19 — Session 2

- **Topic taught:** Algebra Essentials.
- **Notebook created:** `notebooks/02-algebra-essentials.ipynb` (69 cells).
- **Contents:** warm-up recall quiz on Topic 1 (with hidden answers) → intuition "algebra is
  arithmetic with an unknown" → definitions (constant, variable, expression, evaluation, domain,
  equivalence, identity vs equation) → **mathematical induction** introduced with the domino
  picture and a first full proof ($1+2+\dots+n=\frac{n(n+1)}{2}$) → exponents: recursive
  definition, E1/E2/E3 proved by induction, Lemma E4 ($a\neq0 \Rightarrow a^n\neq0$, uses the
  zero-product theorem from notebook 01), $a^0=1$ and $a^{-n}=1/a^n$ derived as forced, E5, E6,
  plus a table of the five most common mistakes → square roots: uniqueness lemma R1, R2
  $\sqrt{a^2}=|a|$, R3 $\sqrt{ab}=\sqrt a\sqrt b$ with the counterexample for negative inputs →
  order theorems O5, O6 proved → scientific notation and its link to float storage → 5 worked
  examples → 8 Python demo cells → 20 exercises → `uv` note.
- **New links back to Topic 1:** zero-product property (Lemma E4, R1), $(-1)(-1)=1$ (R2),
  axioms A2/A3/A6 and O3/O4 used by name in every proof.
- **Verification:** executed top to bottom with `uv run jupyter nbconvert --execute`; every code
  cell ran with no error. One demo was rewritten after testing: SymPy only turns $\sqrt{t^2}$ into
  $|t|$ when the symbol is declared `real=True`, so the cell now shows all three cases
  (no assumption / real / positive) plus `refine`.
- **What went well:** nothing to judge yet — no student work in this session.
- **Homework given:** the 20 exercises in `notebooks/02-algebra-essentials.ipynb`
  (1–7 warm-up, 8–15 medium, 16–20 proofs, ending with Bernoulli's inequality by induction).
- **Next session plan:** check the answers for notebooks 01 and 02, quiz on induction (ask the
  student to state the two steps in their own words), then teach **Topic 3 — Geometry Essentials**
  in `notebooks/03-geometry-essentials.ipynb`.

### 2026-08-19 — Session 1 (restart from zero)

- **Status:** all previously generated notebooks were deleted by the student; `CLAUDE.md` was
  updated. We restarted the course from Topic 1.
- **Topic taught:** Real Numbers.
- **Notebook created:** `notebooks/01-real-numbers.ipynb` (63 cells).
- **Contents:** intuition (the number line) → the five families of numbers with set notation →
  field, order and completeness axioms → 8 theorems with full proofs (Lemma 1 uniqueness of the
  additive inverse, T1 $a\cdot0=0$, T2 $(-1)a=-a$, T3 zero-product, Lemma 2 even squares,
  T4 $\sqrt2$ irrational, Lemma 3 $\mathbb{Q}$ closed under arithmetic, T5 rational+irrational,
  T6 repeating decimal $\Leftrightarrow$ rational with the pigeonhole argument, Lemmas 4–5 and
  T7 triangle inequality, T8 density of $\mathbb{Q}$) → 5 worked examples → 8 Python demo cells →
  20 exercises → `uv` note.
- **Verification:** the whole notebook was executed top to bottom with
  `uv run jupyter nbconvert --execute`; every code cell ran with no error.
- **What went well:** nothing to judge yet — no student work in this session.
- **Mistakes to revisit:** none recorded yet.
- **Homework given:** the 20 exercises in `notebooks/01-real-numbers.ipynb`
  (1–8 warm-up, 9–15 medium, 16–20 proofs).
- **Next session plan:** short quiz on Topic 1 (classify numbers, name an axiom, restate the
  $\sqrt{2}$ proof in own words), review the exercise answers, then teach
  **Topic 2 — Algebra Essentials** in `notebooks/02-algebra-essentials.ipynb`.