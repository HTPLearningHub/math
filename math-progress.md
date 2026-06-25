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
- **Factoring Polynomials** — taught (awaiting student's exercises). Covers: GCF (distributive
  law backwards), factoring by grouping, trinomials x²+bx+c (add/multiply trick) and the
  AC method for ax²+bx+c (proved via a·(ax²+bx+c)=(ax+m)(ax+n)), special formulas — difference
  of squares, perfect-square trinomials, sum/difference of cubes (all proved; "SOAP" sign aid),
  general factoring strategy, Zero Product Property (proved from field axioms), Remainder
  Theorem & Factor Theorem (proved via division algorithm) as the bridge to synthetic division.
- **Synthetic Division** — taught (awaiting student's exercises). Covers: polynomial long
  division, the Division Algorithm (existence + uniqueness, both proved), synthetic division
  for divisor x−c with a "why it works" argument, Horner's method / fast evaluation linked to
  the Remainder Theorem, and the Rational Root Theorem (proved) + peel-off strategy for full
  factorisation. Hand-coded synthetic_division() and horner_eval() in pure Python, cross-checked
  with sympy.div / numpy.polyval.

- **Rational Expressions** — taught (awaiting student's exercises). Covers: definition P/Q with
  Q≠0 as the polynomial twin of ℚ, domain / excluded values, equality by cross-multiplication,
  lowest terms, Cancellation Law (proved), multiply/divide/add/subtract rules (all proved via
  common denominator BD), complex fractions, the difference quotient as a calculus seed, holes
  vs vertical asymptotes (matplotlib), partial-fractions teaser (sympy.apart). Key callback:
  proved F[x] has no zero divisors (so B,D≠0 ⇒ BD≠0) using the degree rule from topic 4, framing
  rational expressions as the field of fractions F(x) (twin of ℚ from ℤ). sympy factor/cancel/
  together/apart/simplify.

- **Quadratic Equations** — taught (awaiting student's exercises). Covers: standard form ax²+bx+c=0,
  parabola, roots/zeros. Solving by factoring (Zero Product Property recall, topic 5) + the
  "don't divide by x" trap. Proofs: Theorem 1 square-root method (cases on sign of k), Theorem 2
  the Quadratic Formula derived by completing the square on the general equation, Theorem 3
  discriminant test Δ=b²−4ac (two/one/none real roots), Theorem 4 Vieta r₁+r₂=−b/a & r₁r₂=c/a
  (via factored form coefficient matching), Theorem 5 vertex form a(x−h)²+k with h=−b/2a, k=c−b²/4a
  + min/max + axis of symmetry. Worked Δ>0/=0/<0 examples. AI hook: parabola = simplest convex
  loss, vertex = minimum, and a hand-coded 1-D gradient descent rolling to the vertex (x:−4→3).
  numpy.roots, sympy.solve, matplotlib parabola/vertex/roots plots.

- **Linear Functions** — taught (awaiting student's exercises). Covers: function (domain/range/
  vertical-line test), linear function f(x)=mx+b, slope as rise/run = Δy/Δx, average rate of
  change. Proofs: Theorem 1 constant-ARC characterizes linearity (both directions, ⇐ via anchor
  x=0), Theorem 2 slope well-defined, Theorem 3 two points → unique line (existence + uniqueness),
  Theorem 4 sign of m ⇒ increasing/decreasing/constant, Theorem 5 parallel ⟺ equal slopes,
  Theorem 6 perpendicular ⟺ m₁m₂=−1 (proved via Pythagoras, callback to topic 3). Slope-intercept/
  point-slope/general forms, intercepts, parallel/perp through a point, word problems. AI hook:
  linear regression as a single neuron (weight m, bias b) — numpy.polyfit cross-checked against
  the closed-form Cov/Var least-squares formula. sympy solve/subs, matplotlib line families +
  equal-aspect perpendicularity plot.

- **nth Roots; Rational Exponents** — taught (awaiting student's exercises). Covers: nth root
  definition, principal root (odd vs even index), radical notation; rational exponents
  a^(1/n)=ⁿ√a and a^(m/n). Proofs: Lemma A (x↦xⁿ strictly increasing on [0,∞) via the
  yⁿ−xⁿ factorisation), Theorem 1 existence+uniqueness of the principal root (completeness +
  binomial squeeze — callback to topic 1 sup), Theorem 2 laws of radicals (product/quotient/
  root-of-root/aᵐ via "raise to the n" + uniqueness), Theorem 3 √(a²)=|a| sign trap, Theorem 4
  rational exponents well-defined (m/n=p/q ⇒ same value), Theorem 5 exponent laws survive for
  rationals (common-denominator reduction to topic-2 integer laws). Simplest radical form,
  rationalizing (conjugates). Newton's method for ⁿ√A as the numerics/AI hook; norms/L^p/RMS/
  1/√t schedules. sympy root/radsimp/real_root, numpy, matplotlib.

## Current Focus
**Equations and Inequalities ▸ 2. Quadratic Equations**. Notebook
`10-quadratic-equations.ipynb` delivered and verified; student to study it and complete
the 20 exercises. Next topic in queue: **Equations and Inequalities ▸ 3. Complex Numbers;
Quadratic Equations in the Complex Number System** → notebook `11-complex-numbers.ipynb`.

## Known Weak Spots (auto-revisit these)
- **Repeating-decimal → fraction** (decimal test, ⇐ direction): needed a second
  explanation. Re-quiz next session (e.g. "convert 0.\overline{27} to a fraction").
- **√(a²)=|a| sign trap** (topic 8): likeliest new error. Watch for the student writing
  √(a²)=a or √((x−4)²)=x−4 without absolute value; re-quiz next session.
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

### Session 10 — 2026-06-25
- **Topic taught:** Quadratic Equations (Equations & Inequalities ▸ 2).
- **Notebook created:** `notebooks/10-quadratic-equations.ipynb` (29 cells; verified end-to-end
  with `uv run jupyter nbconvert --execute`). Discriminant solver classifies Δ>0/=0/<0 correctly,
  Vieta sum/product match −b/a & c/a, and gradient descent rolls from x=−4 to x≈3.0 (the vertex).
- **Content:** standard form + parabola + roots; factoring via Zero Product Property (recall topic
  5) and the don't-divide-by-x trap. Full proofs: Theorem 1 square-root method, Theorem 2 quadratic
  formula by completing the square on ax²+bx+c=0, Theorem 3 discriminant test, Theorem 4 Vieta's
  formulas, Theorem 5 vertex form a(x−h)²+k (h=−b/2a, k=c−b²/4a) + min/max + symmetry. Worked
  examples for all three Δ cases + vertex/optimisation.
- **Recall given:** 3-item warm-up — slope through (−1,4),(3,−4) = −2; perpendicular slope = −2
  (negative reciprocal, Theorem 6 session 9); √((2−x)²)=|x−2| sign trap; solutions at end of §1.
- **What went well:** strong continuity — factoring reuses ZPP (topic 5), square-root method reuses
  principal-root existence (topic 8) and difference of squares (topic 4), vertex/symmetry leads
  straight into the AI hook (parabola = convex loss, vertex = minimum, gradient descent demo).
- **Mistakes / misconceptions to revisit:** STILL no student-produced work seen (10 sessions).
  The √(a²)=|a| sign trap was re-quizzed again and remains unconfirmed by the student. Watch for
  (1) dividing by x and losing the x=0 root, (2) sign errors in completing the square / −b/2a,
  (3) forgetting the ± in the square-root step.
- **Homework given:** 20 exercises (factoring/square-root, completing the square + formula,
  discriminant + Vieta incl. r₁²+r₂², vertex/optimisation word problems, proofs #17–20: derive the
  quadratic formula, prove Vieta directly from the roots, sign of ax²+bx+c when Δ<0, and parabola
  symmetry f(h+t)=f(h−t)).
- **Next session plan:** Quick recall on the discriminant cases + the quadratic formula, then start
  **Complex Numbers; Quadratic Equations in the Complex Number System** (topic 3): notebook
  `11-complex-numbers.ipynb` — finally solving the Δ<0 case.

### Session 9 — 2026-06-25
- **Topic taught:** Linear Functions (Equations & Inequalities ▸ 1) — first topic of the new
  block after the Review block.
- **Notebook created:** `notebooks/09-linear-functions.ipynb` (31 cells; verified it runs
  end-to-end with `uv run jupyter nbconvert --execute`). Regression demo recovers y≈2.046x−1.323
  from noisy data, and the by-hand Cov/Var formula matches numpy.polyfit exactly.
- **Content:** function + domain/range + vertical-line test, f(x)=mx+b, slope = Δy/Δx, average
  rate of change. Full proofs: Theorem 1 (constant ARC ⟺ linear, both directions), Theorem 2
  (slope well-defined), Theorem 3 (two points → unique line: existence + uniqueness), Theorem 4
  (sign of m ⇒ increasing/decreasing/constant), Theorem 5 (parallel ⟺ equal slopes), Theorem 6
  (perpendicular ⟺ m₁m₂=−1, proved with Pythagoras — callback to topic 3 distance formula).
  Three forms of a line, intercepts, parallel/perp through a point, taxi/gym/tank word problems.
  AI hook: linear regression = a single neuron (m=weight, b=bias), numpy.polyfit vs closed-form.
- **Recall given:** 3-item warm-up at the top — √(a²)=|a| sign trap (topic 8), evaluate 8^(2/3) &
  16^(−3/4) (topic 8), and the weak spot 0.\overline{27}→3/11; full solutions at end of §1.
- **What went well:** clean transition into functions; Theorem 6 reuses the topic-3 distance
  formula, Theorem 4 reuses topic-2 order rules. Strong forward/AI hook (regression → ML neuron).
- **Mistakes / misconceptions to revisit:** STILL no student-produced work seen (9 sessions).
  Re-quizzed the √(a²)=|a| sign trap and 0.\overline{27}→3/11 in-notebook; neither yet confirmed
  by the student. Keep nudging for written attempts — especially proofs.
- **Homework given:** 20 exercises (slope/eval, building equations, parallel/perpendicular,
  modeling, proofs #17–20: unique x-intercept when m≠0, decreasing case of Theorem 4, midpoint
  stays on the line, and re-prove perpendicularity + why non-vertical is required).
- **Next session plan:** Quick recall on slope from two points + perpendicular slopes (negative
  reciprocal), then start **Quadratic Equations** (topic 2): notebook `10-quadratic-equations.ipynb`.

### Session 8 — 2026-06-23
- **Topic taught:** nth Roots; Rational Exponents (topic 8 of `math-topic.md`) — last item of
  the Review block.
- **Notebook created:** `notebooks/08-nth-roots-rational-exponents.ipynb` (64 cells; verified it
  runs end-to-end with `uv run jupyter nbconvert --execute`).
- **Content:** nth root + principal root (odd/even index), radicals, rational exponents.
  Full proofs: Lemma A (strict monotonicity of xⁿ), Theorem 1 existence+uniqueness of the
  principal root (completeness + binomial squeeze, callback to topic 1 sup), Theorem 2 laws of
  radicals, Theorem 3 √(a²)=|a|, Theorem 4 well-definedness of a^(m/n), Theorem 5 exponent laws
  for rationals (reduced to integer laws via common denominator). Simplest radical form,
  rationalizing with conjugates. Python: sympy root/radsimp/real_root, numpy law checks, a
  matplotlib plot of x^(1/n), and a hand-coded Newton iteration for the nth root (AI/numerics
  hook → norms, L^p, RMS, 1/√t schedules, Adam).
- **Recall given:** 3-item spaced-repetition warm-up at the top — topic 7 simplify+hole/asymptote
  for (x²−9)/(x²−x−6), topic 5 factor x³−8, and the weak spot 0.\overline{27}→3/11; full
  solutions placed at the end of §3.
- **What went well:** strong closure of the Review block — Theorem 1 reuses completeness/sup from
  topic 1, Theorem 5 reuses the integer exponent laws from topic 2, rationalizing reuses
  difference of squares from topic 4. Roots unified with powers (a^(1/n)).
- **Mistakes / misconceptions to revisit:** STILL no student-produced work seen (8 sessions).
  Repeating-decimal → fraction re-quizzed again in-notebook but not yet confirmed by the student.
  The √(a²)=|a| sign trap is the likeliest new error spot — check it in their answers.
- **Homework given:** 20 exercises (evaluate, rational-exponent form, simplest radical form,
  combine/rationalize incl. conjugates, the sign trap, solving, nested radical 3+2√2; proofs
  #18–20: product rule via uniqueness, √(a²)=|a| / parity of ⁿ√(aⁿ), and aʳaˢ=a^(r+s) for rationals).
- **Next session plan:** Quick recall on √(a²)=|a| and a^(m/n) evaluation, then begin the new
  block **Equations and Inequalities ▸ 1. Linear Functions**: notebook `09-linear-functions.ipynb`.

### Session 7 — 2026-06-23
- **Topic taught:** Rational Expressions (topic 7 of `math-topic.md`).
- **Notebook created:** `notebooks/07-rational-expressions.ipynb` (55 cells; verified it runs
  end-to-end with `uv run jupyter nbconvert --execute`).
- **Content:** rational expression P/Q as the polynomial analogue of a fraction, domain /
  excluded values, equality by cross-multiplication, lowest terms; Cancellation Law,
  multiply/divide/add/subtract rules — all proved; complex fractions; the difference quotient
  (calculus seed); holes vs vertical asymptotes plotted in matplotlib; partial-fractions teaser
  via sympy.apart. Proved F[x] has no zero divisors using the degree rule (callback to topic 4),
  framing F(x) as the field of fractions (twin of ℚ from ℤ).
- **Recall given:** opened with a 3-item spaced-repetition quiz — synthetic division/Remainder
  Theorem (p(2) for x³−2x²+3), factoring x²−x−6 & x²−9, and the lingering weak spot
  0.\overline{27}→3/11; all answers shown at the bottom of the worked examples.
- **What went well:** strong continuity — factoring (topic 5) feeds simplification, and the
  no-zero-divisors proof reuses the degree rule from topic 4. Good forward hooks (difference
  quotient → calculus; apart → partial fractions; F(x) → abstract algebra).
- **Mistakes / misconceptions to revisit:** STILL no student-produced work seen (7 sessions).
  Repeating-decimal → fraction re-quizzed in-notebook but not yet confirmed by the student.
  Keep nudging for written attempts before moving on.
- **Homework given:** 20 exercises (domains, simplify, multiply/divide, add/subtract, complex
  fractions, difference quotient, cubes; proofs #18–20: Cancellation Law, addition rule, and
  F[x] has no zero divisors + why BD is safe).
- **Next session plan:** Quick recall on the cancellation law + holes vs asymptotes, then start
  **nth Roots; Rational Exponents** (topic 8): notebook `08-nth-roots-rational-exponents.ipynb`.

### Session 6 — 2026-06-23
- **Topic taught:** Synthetic Division (topic 6 of `math-topic.md`).
- **Notebook created:** `notebooks/06-synthetic-division.ipynb` (verified it runs end-to-end
  with `uv run jupyter nbconvert --execute`).
- **Content:** long division, Division Algorithm (existence + uniqueness proved), synthetic
  division (algorithm + why it works), Horner's method / fast evaluation tied to the Remainder
  Theorem, Rational Root Theorem (proved) and repeated peel-off for full factorisation. Pure
  Python synthetic_division() + horner_eval(), cross-checked with sympy/numpy.
- **Recall given:** restated Factor Theorem, Remainder Theorem, and difference of cubes at top.
- **What went well:** tight continuity — Factor Theorem from topic 5 motivates the whole topic;
  Horner's method introduced as the real-world / AI-numerics hook.
- **Mistakes / misconceptions to revisit:** STILL no student work seen (6 sessions). Repeating-
  decimal → fraction conversion remains unconfirmed. Keep nudging for written attempts.
- **Homework given:** 20 exercises (long division, synthetic division, Horner evaluation,
  Rational Root Theorem full factoring, proofs #18–20: Remainder Theorem, RRT for monic cubic,
  and why a degree-1 divisor forces a constant remainder).
- **Next session plan:** Quick recall on synthetic division + Remainder Theorem, then start
  **Rational Expressions** (topic 7): notebook `07-rational-expressions.ipynb`.

### Session 5 — 2026-06-23
- **Topic taught:** Factoring Polynomials (topic 5 of `math-topic.md`).
- **Notebook created:** `notebooks/05-factoring-polynomials.ipynb` (verified it runs
  end-to-end with `uv run jupyter nbconvert --execute`).
- **Content:** GCF, grouping, trinomials + AC method (proved), special formulas (diff of
  squares, perfect squares, sum/diff of cubes — all proved), general strategy, Zero Product
  Property (proved), Remainder + Factor Theorem (proved) as bridge to synthetic division.
- **Recall given:** restated the three special products at the top as the seeds of factoring
  (multiplication run in reverse).
- **What went well:** clean continuity — factoring is literally lesson 4 read backwards, and
  the Factor Theorem sets up topic 6.
- **Mistakes / misconceptions to revisit:** STILL no student-produced work seen across 5
  sessions — cannot assess real understanding. Keep nudging for exercise answers; the
  repeating-decimal → fraction conversion remains unconfirmed.
- **Homework given:** 20 exercises (GCF/grouping, trinomials, special formulas, proofs
  #18–20 incl. difference-of-cubes, Factor-Theorem use, and the AC-method proof).
- **Next session plan:** Quick recall on difference of squares + sum/diff of cubes and the
  Factor Theorem, then start **Synthetic Division** (topic 6): notebook
  `06-synthetic-division.ipynb`.

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