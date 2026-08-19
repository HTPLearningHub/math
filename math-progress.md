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

## Current Focus

**Topic 1 — Real Numbers.** Notebook is generated and every code cell was executed
successfully. Waiting for the 20 exercises. Say **"continue"** when they are done, and we move to
Topic 2 — *Algebra Essentials*.

## Known Weak Spots

*(Empty for now — fresh restart. I will fill this in from the exercise answers.)*

Things to watch for in Topic 1, based on what usually goes wrong:
- Ex. 11 & 18 — irrational $\times$ irrational vs. rational $\times$ irrational (the $r \neq 0$ condition)
- Ex. 15 — supremum that is **not** an element of the set
- Ex. 17, 20 — reusing the $\sqrt{2}$ proof structure for $\sqrt{3}$ and $\sqrt{2}+\sqrt{3}$
- Ex. 19 — the reverse triangle inequality (needs two applications of Theorem 7)

## Session Log

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