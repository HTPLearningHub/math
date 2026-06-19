# Math Learning — Progress Log

> This file is my long-term memory of what we've covered. I READ it at the start of every
> session and UPDATE it at the end. Newest entries at the top of the Session Log.

## Skill Ledger
- **Real numbers (intro)** — taught (awaiting student's exercises). Covers: the number
  systems ℕ⊂ℤ⊂ℚ⊂ℝ, decimal test for rationality, field axioms, order + absolute value +
  triangle inequality + intervals, proof that √2 is irrational, completeness (least upper
  bound) and density of ℚ in ℝ. Student asked for clarification on the ⇐ direction of the
  decimal test (repeating decimal → fraction); re-explained with the 10^k-shift trick.
- **Algebra essentials** — taught (awaiting student's exercises). Covers: expressions /
  like terms (= distributive law backwards), laws of exponents (with proofs) + negative
  exponents, scientific notation, solving linear equations (properties of equality,
  uniqueness of -b/a), linear inequalities + the flip-the-sign rule (proved),
  absolute-value equations & inequalities.
- **Geometry essentials** — taught (awaiting student's exercises). Covers: points/lines/
  rays/angles + angle types, vertical angles (proved equal), parallel-line/transversal
  angles, triangle angle sum = 180° (proved), Pythagorean theorem (rearrangement proof),
  perimeter/area/circles + π, coordinate geometry (distance/midpoint/slope) with the link
  distance = Pythagoras = Euclidean distance/norm (AI hook).
- **Polynomials** — taught (awaiting student's exercises). Covers: definition / degree /
  leading coeff / standard form / type names, add-subtract (combine like terms),
  multiply (distributive + FOIL), special products (a±b)² and (a+b)(a−b)=a²−b² (proved),
  degree rules deg(pq)=deg p+deg q (proved) & deg(p+q)≤max, evaluation + graph shape
  (turns, end behaviour). sympy Poly + numpy.polyval + matplotlib.

## Current Focus
Topic 4 of `math-topic.md`: **Polynomials**. Notebook delivered; student to study it and
complete the 20 exercises. Next topic in queue: **5. Factoring Polynomials**.

## Known Weak Spots (auto-revisit these)
- **Repeating-decimal → fraction** (decimal test, ⇐ direction): needed a second
  explanation. Re-quiz next session (e.g. "convert 0.\overline{27} to a fraction").
- Otherwise assess from the student's exercise answers (especially proofs).

## Session Log
<!-- Most recent first. Template:
### Session N — YYYY-MM-DD
- Topic taught:
- What went well:
- Mistakes / misconceptions to revisit:
- Homework given:
- Next session plan:
-->

### Session 4 — 2026-06-19
- **Topic taught:** Polynomials (topic 4 of `math-topic.md`).
- **Notebook created:** `notebooks/04-polynomials.ipynb` (20 cells; verified it runs
  end-to-end with nbconvert --execute).
- **Content:** definition/degree/leading coeff/standard form/type names, add-subtract,
  multiply (FOIL), special products (proved), degree rules (product rule proved), eval +
  graph shape. Difference of squares flagged as the seed of next topic (factoring).
- **Recall quiz given:** distance (2,3)-(7,15)=13, legs 6,8 → 10. Student again said
  "continue" without showing answers.
- **What went well:** good pace through foundations; concepts build cleanly.
- **Mistakes / misconceptions to revisit:** still no student-produced work seen — cannot
  assess real understanding yet. Keep nudging for exercise answers. Repeating-decimal
  conversion still unconfirmed.
- **Homework given:** 20 exercises (identify, operations, special products, proofs
  #16–20 incl. (a+b)³ and the deg(pq)=m+n proof).
- **Next session plan:** Recall on special products (esp. difference of squares), then
  start **Factoring Polynomials** (topic 5): notebook `05-factoring-polynomials.ipynb`.

### Session 3 — 2026-06-19
- **Topic taught:** Geometry Essentials (topic 3 of `math-topic.md`).
- **Notebook created:** `notebooks/03-geometry-essentials.ipynb` (21 cells; verified it
  runs end-to-end with nbconvert --execute).
- **Content:** basic objects + angle types, vertical angles (proved), parallel-line
  angles, triangle angle sum 180° (proved), Pythagoras (rearrangement proof),
  perimeter/area/circle, coordinate geometry (distance/midpoint/slope) with matplotlib
  pictures; flagged Euclidean distance/norm as the AI connection.
- **Recall quiz given:** 0.\overline{27}→3/11 and exponent laws — student said "continue"
  (did not show answers), so recall not yet confirmed; keep both on the watch list.
- **What went well:** steady progress through foundations.
- **Mistakes / misconceptions to revisit:** repeating-decimal conversion still unconfirmed
  by the student; re-check once they share exercise answers.
- **Homework given:** 20 exercises (angles, triangles/Pythagoras, area/coordinates,
  proofs #16–20 incl. exterior-angle theorem and the distance formula).
- **Next session plan:** Quick recall on Pythagoras + distance formula, then start
  **Polynomials** (topic 4): notebook `04-polynomials.ipynb`.

### Session 2 — 2026-06-19
- **Topic taught:** Algebra Essentials (topic 2 of `math-topic.md`).
- **Notebook created:** `notebooks/02-algebra-essentials.ipynb` (20 cells; verified it
  runs end-to-end with nbconvert --execute).
- **Content:** like terms via distributive law, laws of exponents (proved) + negative
  exponents, scientific notation, linear equations (properties of equality, unique -b/a),
  linear inequalities + flip-the-sign rule (proved), absolute-value eqns/inequalities
  with a matplotlib picture.
- **What went well:** Student engaged with lesson 1 — asked a good question about the
  repeating-decimal proof, which I re-explained.
- **Mistakes / misconceptions to revisit:** repeating-decimal → fraction (see Weak Spots).
- **Homework given:** 20 exercises (simplify, sci-notation, solve, proofs #16–20).
- **Next session plan:** Quiz on exponent laws + repeating-decimal conversion. Then start
  **Geometry Essentials** (topic 3): notebook `03-geometry-essentials.ipynb`.

### Session 1 — 2026-06-19
- **Topic taught:** Real Numbers (topic 1 of `math-topic.md`). First real lesson.
- **Notebook created:** `notebooks/01-real-numbers.ipynb` (20 cells; verified it runs
  end-to-end with `uv run jupyter nbconvert --execute`).
- **Environment:** Set up `uv` project (`pyproject.toml`), added numpy, sympy,
  matplotlib, jupyterlab. Created `notebooks/` folder.
- **What went well:** N/A yet (first session — no prior recall quiz possible).
- **Mistakes / misconceptions to revisit:** none yet; collect from exercise answers.
- **Homework given:** 20 exercises in the notebook (warm-up → proofs). Key proofs:
  #16 rational+irrational is irrational, #17 √3 irrational, #18 reverse triangle
  inequality, #20 sup of {x²<2} = √2 via completeness.
- **Next session plan:** Quiz briefly on √2-irrationality proof and the decimal test.
  Then start **Algebra Essentials** (topic 2): notebook `02-algebra-essentials.ipynb`.