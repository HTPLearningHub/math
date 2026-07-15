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

- **Complex Numbers; Quadratics in ℂ** — taught (awaiting student's exercises). Covers: imaginary
  unit i (i²=−1), complex number a+bi, real/imag parts, equality = two real equations, Argand
  plane, conjugate z̄, modulus |z|=√(a²+b²). Arithmetic: add/subtract/multiply (FOIL + i²→−1),
  divide by multiplying by the conjugate; ℂ is a field but has NO order. Proofs: Theorem 1 powers
  of i cycle mod 4, Theorem 2 conjugate is a homomorphism (bar of sum/product/double) + real/pure-
  imaginary tests, Theorem 3 z·z̄=|z|² & Re/Im via conjugate, Theorem 4 |zw|=|z||w| (via squaring),
  Theorem 5 triangle inequality |z+w|≤|z|+|w| (Re u≤|u| lemma), Theorem 6 √(−p)=i√p with the
  don't-merge-negative-radicals trap, Theorem 7 quadratic formula in ℂ (Δ<0 → conjugate-pair roots,
  callback completing the square topic 10), Theorem 8 Conjugate Root Theorem (real poly → complex
  roots in pairs; corollary odd degree has a real root). Fundamental Theorem of Algebra stated
  (ℂ algebraically closed). AI hook: ×i = 90° rotation (length preserved by Thm 4) → FFT/rotations/
  eigenvalues. Python: built-in 1j, sympy I / solve / conjugate, numpy.roots, cmath trap demo,
  Argand diagram + rotation plot.

- **Radical / Quadratic-in-Form / Factorable Equations** — taught (awaiting student's exercises).
  Covers: radical equations (unknown under a root), the key idea of the EXTRANEOUS solution and the
  mandatory check-in-original step; two-radical equations (isolate–square–isolate–square); equations
  quadratic in form via substitution u=g(x) (u=x², √x, x^(1/3), 1/x, or an inner expression);
  factorable higher-degree equations via grouping + ZPP; the don't-divide-by-x trap again. Proofs:
  Theorem 1 raising to power n — forward always valid, odd n reversible (t↦tⁿ one-to-one, callback
  topic 8), even n only gives A=±B so extraneous roots appear; Theorem 2 substitution principle (x
  solves iff g(x)∈{u₁,u₂}, with domain/nonneg caveats); Theorem 3 factor⇒solve (ZPP, FTA for the
  complex closure). Worked: √(x+2)=x (−1 extraneous), two radicals, x⁴−13x²+36, x−5√x+6, grouping,
  x³=9x. AI hook: change of variables (u=x² turns a quartic into a parabola) → u-substitution/kernel
  trick. Python: sympy.solve (auto-drops extraneous) + a hand-written keep_valid() checker that
  shows −1 rejected, plus crossing/coordinate-change plots.

- **Solving Inequalities** — taught (awaiting student's exercises). Covers: inequalities /
  solution sets / interval notation (open/closed/half-open, ∪/∩, ∞ always excluded); boundary
  (critical) points = zeros of numerator OR denominator. Order rules re-proved FROM the order
  axioms (positives set P, trichotomy): Theorem 1 transitivity/add/multiply-by-positive/
  multiply-by-negative-FLIP, Theorem 2 reciprocal rule 0<a<b ⇒ 1/b<1/a (why you must NOT
  cross-multiply), Theorem 3 sign of a product (same/opposite signs; corollary count of negative
  factors), Theorem 4 constant sign between consecutive boundary points (test-point method
  justified; IVT flagged as the deep reason for calculus). Linear + compound (and=intersection,
  or=union), quadratic/polynomial by SIGN CHART, always-true/never (Δ<0 parabola), rational
  inequalities with the move-to-one-side rule. AI hook: feasible region = intersection of
  inequalities (budget triangle), ReLU=max(0,x), SVM margin, L² ball. Python: sympy
  solve_univariate_inequality / reduce_inequalities / solveset+Union, a hand-built sign_chart()
  using together/fraction, shaded-parabola and 2-D feasible-region plots.

- **Absolute Value Equations & Inequalities** — taught (awaiting student's exercises). Covers:
  |x| as distance from 0, piecewise def, and the |x|=√(x²) link (closes the topic-8 sign trap);
  |a−b| distance. Proofs: Theorem 1 basics (|x|≥0, |x|=0⟺x=0, |−x|=|x|, −|x|≤x≤|x|, |x|=a⟺x=±a via
  ZPP), Theorem 2 |xy|=|x||y| & quotient (via √(t²), 1-D shadow of topic-11 |zw|=|z||w|), Theorem 3
  the two master rules |x|≤a⟺−a≤x≤a and |x|≥a⟺x≤−a or x≥a (> is the negation of <), Theorem 4
  triangle inequality (add −|x|≤x≤|x| chains) + reverse triangle inequality ||x|−|y||≤|x−y|.
  Equations |f|=a / |f|=|g|⟺f=±g; inequalities as one interval (<) vs two rays (>); distance
  reading |x−c|<r = (c−r,c+r); isolate-first; square-both-sides for |A|≤|B|. AI hook: |x|=1-D L¹
  norm, MAE vs MSE loss curves, corner-at-0 = ReLU/subgradient, L¹ ball → Lasso sparsity. Python:
  sympy Abs / solve / solveset, numpy abs vs sqrt(x²), V-shape + shifted graph, MAE/MSE plot.

- **Problem-Solving Applications (Interest/Mixture/Motion/Work)** — taught (awaiting student's
  exercises). Covers: the five-step translation routine (name+units → express others → balancing
  sentence → solve → CHECK in words, reject impossible answers). Four model families: simple
  interest I=Prt (+ split-investment), mixture/concentration (pure amount conserved), uniform
  motion d=rt (opposite/same direction, upstream/downstream), constant-rate work (rates add,
  1/t₁+1/t₂=1/t). Proofs: Theorem 1 combined work rate t=t₁t₂/(t₁+t₂) with t<min sanity checks,
  Theorem 2 mixture concentration = weighted average lying between c₁,c₂ (convex combination).
  Worked A–F incl. a rational (upstream/downstream) and a quadratic (garden area, reject w=−8).
  AI hook: modelling/formalization; rates add = linearity; mixture = convex combination
  (expectation/ensembles/attention); check-in-words = model validation. Python: sympy.solve on the
  balancing equation for each type, reject-negative-root idiom, matplotlib "rates add" plot.

## Current Focus
**Equations and Inequalities ▸ 7. Problem-Solving: Interest, Mixture, Uniform Motion, Constant-Rate
Job Applications** — the LAST topic of the Equations & Inequalities block. Notebook
`15-problem-solving-applications.ipynb` delivered and verified (33 cells, runs end-to-end with 0
error outputs; sympy gives split-investment \$3000/\$7000 and combined work time 12/5=2.4 h matching
t₁t₂/(t₁+t₂)). Student to study it and complete the 20 exercises. This CLOSES the Equations &
Inequalities block. Next block: **Graphs** (now filled in `math-topic.md`) — start with
**Graphs ▸ 1. The Distance and Midpoint Formulas** → notebook `16-distance-midpoint-formulas.ipynb`
(note: distance/midpoint/slope were already introduced in topic 3 Geometry Essentials — treat this
as a deeper revisit + the graphing lead-in, not brand-new). Later blocks: Functions and Their
Graphs, then Linear and Quadratic Functions.

## Known Weak Spots (auto-revisit these)
- **Repeating-decimal → fraction** (decimal test, ⇐ direction): needed a second
  explanation. Re-quiz next session (e.g. "convert 0.\overline{27} to a fraction").
- **√(a²)=|a| sign trap** (topic 8): likeliest new error. Watch for the student writing
  √(a²)=a or √((x−4)²)=x−4 without absolute value; re-quizzed in-notebook 11 (√((3−x)²)=|x−3|).
- **Merging negative radicals** (topic 11): watch for √(−4)·√(−9)=√36=6 instead of (2i)(3i)=−6.
  Rule: convert to i FIRST, then multiply. Re-quizzed in-notebook 12; still unconfirmed.
- **Forgetting to check for extraneous roots** (topic 12): watch for the student keeping a
  squared-equation root that fails the original (e.g. keeping x=−1 for √(x+2)=x), or dividing
  by x and losing x=0. Rule: solve, then substitute back into the ORIGINAL. Re-quiz.
- **Not flipping the inequality sign / cross-multiplying rationals** (topic 13): watch for (1)
  dividing an inequality by a negative without flipping <→>, and (2) multiplying a rational
  inequality by a denominator of unknown sign. Re-quizzed in-notebook 14; still unconfirmed.
- **Absolute-value inequality direction** (topic 14): watch for turning |x|>a into −a<x<a
  (wrong — that's the < rule). < ⇒ one interval, > ⇒ two rays. Also isolate |·| first; reject
  |·|=negative. Re-quiz.
- **Word-problem set-up & rejecting impossible roots** (topic 15, NEW likely error): watch for
  (1) mis-stating the balancing equation (esp. mixture: use pure amount c·V, not concentrations
  added; work: rates 1/t add, not times), and (2) keeping a negative length/speed/time root.
  Rule: name with units, one balancing sentence, check in words. Re-quiz.
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

### Session 15 — 2026-07-15
- **Topic taught:** Problem-Solving: Interest, Mixture, Uniform Motion, Constant-Rate Job
  Applications (Equations & Inequalities ▸ 7) — the topic I had skipped; it is the TRUE last topic
  of the block. (Student flagged that `math-topic.md` still had topic 7 + the now-filled Graphs
  subtopics; corrected the plan and taught topic 7 before moving to Graphs.)
- **Notebook created:** `notebooks/15-problem-solving-applications.ipynb` (33 cells; verified
  end-to-end with `uv run jupyter nbconvert --execute` — 0 error outputs). sympy gives split
  investment \$3000/\$7000, mixture add 10 L, meeting time 2 h, boat speed 10 mph, combined work
  time 12/5 = 2.4 h (matches t₁t₂/(t₁+t₂)), garden 5×8 (rejecting w=−8).
- **Content:** the five-step translation routine; four model families (I=Prt, mixture pure-amount
  conservation, d=rt with combining speeds, work rates add → 1/t₁+1/t₂=1/t). Proofs: Theorem 1
  combined work rate + sanity checks, Theorem 2 mixture = weighted average between the parts (convex
  combination). Worked A–F incl. rational (upstream/downstream) and quadratic (area, reject negative
  root). AI hook: modelling/formalization, rates-add = linearity, mixture = convex combination
  (expectation/ensembles/attention), check-in-words = validation.
- **Recall given:** 3-item warm-up — |2x−1|<5 → (−2,3) (topic 14), |x−2|≥3 → two rays (topic 14),
  √(x+2)=x with extraneous x=−1 (topic 12). Solutions at end of §2.
- **What went well:** strong applied capstone — pulls together linear (topic 2/9), rational (topic 7),
  and quadratic (topic 10) solving inside word problems; the reject-impossible-root habit reuses the
  extraneous-check discipline from topic 12; the "rates add / weighted average" framing plants convex
  combinations for later ML.
- **Mistakes / misconceptions to revisit:** STILL no student-produced work seen (15 sessions). New
  likely errors: mis-setting the balancing equation (mixture/work especially) and keeping a negative
  length/speed/time root. All earlier traps remain unconfirmed by written work.
- **Homework given:** 20 exercises (interest incl. split accounts, mixture incl. price blends and
  3-way, motion incl. tail/headwind and round-trip average, work incl. a negative-rate drain and a
  find-the-other-worker, mixed quadratic/rational; proofs #17–20: derive t=t₁t₂/(t₁+t₂) & t<min,
  mixture is a weighted average between parts, same-direction gap rate r₁−r₂, and why a negative-time
  root is rejected).
- **Next session plan:** Equations & Inequalities block COMPLETE. Open session 16 with a quick recall
  on the five-step routine + one work-rate set-up, then start the **Graphs** block: topic 1 **The
  Distance and Midpoint Formulas** → notebook `16-distance-midpoint-formulas.ipynb` (revisit/deepen
  from topic 3, leading into graphing). Graphs order after: 2. Graphs of Equations/Intercepts/
  Symmetry, 3. Lines, 4. Circles, 5. Variation.

### Session 14 — 2026-07-15
- **Topic taught:** Equations and Inequalities Involving Absolute Value (Equations & Inequalities
  ▸ 6). [Correction: at the time I wrongly called this the last topic of the block; topic 7
  (Problem-Solving applications) was still remaining and was taught in session 15.]
- **Notebook created:** `notebooks/14-absolute-value-equations-inequalities.ipynb` (33 cells;
  verified end-to-end with `uv run jupyter nbconvert --execute` — 0 error outputs). sympy confirms
  every worked example: D→(−2,3), E→(−∞,−1]∪[5,∞), G→[−5,3], H→[−4,2/3]; numpy shows abs(x)=√(x²).
- **Content:** |x| as distance / piecewise / √(x²); distance |a−b|. Full proofs: Theorem 1 basics
  (incl. |x|=a⟺x=±a via ZPP and −|x|≤x≤|x|), Theorem 2 |xy|=|x||y|, Theorem 3 the two master
  inequality rules (< one interval, > two rays; > proved as the negation of <), Theorem 4 triangle
  + reverse triangle inequality. Equations |f|=a and |f|=|g|; isolate-first; square-both-sides for
  |A|≤|B|; distance reading |x−c|<r=(c−r,c+r). AI hook: |x|=1-D L¹ norm, MAE vs MSE loss curves,
  the corner-at-0 = ReLU/subgradient, L¹ ball → Lasso sparsity.
- **Recall given:** 3-item warm-up — x²−x−6>0 sign chart → (−∞,−2)∪(3,∞) (topic 13); −2x+1≥7 with
  the flip → (−∞,−3] (topic 13); √((x−5)²)=|x−5| sign trap (topic 8, = today's definition).
  Solutions at end of §2.
- **What went well:** clean capstone for the block — the definition |x|=√(x²) directly resolves the
  long-standing topic-8 sign trap; Theorem 4 reuses the topic-13 add-inequalities result and unifies
  with the topic-1 and topic-11 triangle inequalities; the master rules reuse the topic-13 flip rule;
  strong AI hook (norms/MAE/L¹/ReLU) closing toward the Graphs block.
- **Mistakes / misconceptions to revisit:** STILL no student-produced work seen (14 sessions). New
  likely error: reversing the |x|>a rule into an interval, and not isolating |·| first. Earlier
  traps (flip rule, cross-multiplying, √(a²)=|a|) still unconfirmed by written work.
- **Homework given:** 20 exercises (equations incl. |·|=0 and |·|=negative and |f|=|g|; inequalities
  < vs ≥ with isolate-first and a flip case; distance/tolerance modelling; harder: square-both-sides
  |2x−1|≤|x+3|, case-split |x−1|+|x+2|=5; proofs #18–20: |xy|=|x||y|, the triangle inequality with
  equality/strict examples, and the reverse triangle inequality as a stability statement).
- **Next session plan:** This finishes the Equations & Inequalities block. BEFORE session 15, fill in
  the **Graphs** subtopics in `math-topic.md` (currently just a heading). Likely order: the
  coordinate/Cartesian plane, graphs of equations (intercepts/symmetry), lines revisited, and circles
  (general form via completing the square). Open session 15 with a quick recall on the |x|<a vs |x|>a
  master rules + the distance reading, then start the first Graphs topic → notebook `15-...ipynb`.

### Session 13 — 2026-07-15
- **Topic taught:** Solving Inequalities (Equations & Inequalities ▸ 5).
- **Notebook created:** `notebooks/13-solving-inequalities.ipynb` (33 cells; verified end-to-end
  with `uv run jupyter nbconvert --execute` — 0 error outputs). sympy confirms every worked
  example: A→[−3,∞), D→(−∞,−2)∪(3,∞), E→ℝ, F→(−∞,−2]∪[1,4], G→(−∞,−2)∪[1,∞), H→(−∞,3)∪(7,∞).
- **Content:** inequalities/solution sets/interval notation; order rules re-proved FROM the order
  axioms (Theorem 1 add/mult incl. the flip on negative, Theorem 2 reciprocal rule, Theorem 3 sign
  of a product, Theorem 4 constant sign between boundary points = the sign-chart justification, IVT
  flagged for calculus). Linear + compound (and/or), quadratic/polynomial by sign chart, always-
  true/never via Δ<0, rational inequalities with the move-to-one-side rule (never cross-multiply).
  Worked A–H. AI hook: feasible region = intersection of inequalities (budget triangle plot),
  ReLU=max(0,x), SVM margin, L² ball.
- **Recall given:** 3-item warm-up — √(x+2)=x with the extraneous x=−1 (topic 12), x⁴−5x²+4=0 via
  u=x² (topic 12), x²+2x+5=0 → −1±2i (topic 11). Solutions at end of §2.
- **What went well:** strong continuity — order rules trace back to the topic-1 order axioms and the
  topic-2 flip rule; the sign chart reuses factoring (topic 5) and Δ<0 constant sign (topics 10/11);
  hand-built sign_chart() makes Theorem 4 concrete; feasible-region plot ties inequalities to
  constrained optimisation.
- **Mistakes / misconceptions to revisit:** STILL no student-produced work seen (13 sessions). New
  likely errors: forgetting to flip on a negative multiply/divide, and cross-multiplying a rational
  inequality (unknown denominator sign). Earlier traps (extraneous check, merge-negative-radicals)
  still unconfirmed.
- **Homework given:** 20 exercises (linear/compound incl. flip, quadratic/polynomial sign charts,
  always-true via Δ, x³≤4x don't-divide, four rationals incl. 1/x<3 and 2x/(x−1)≥1; proofs #17–20:
  add two inequalities, a<b ⇒ −b<−a, x²≥0 ⇒ x²+1>0 on ℝ, and a counterexample for cross-multiplying).
- **Next session plan:** Quick recall on the sign chart + the flip rule, then start **Equations and
  Inequalities Involving Absolute Value** (topic 6): notebook
  `14-absolute-value-equations-inequalities.ipynb`.

### Session 12 — 2026-07-15
- **Topic taught:** Radical Equations; Equations Quadratic in Form; Factorable Equations
  (Equations & Inequalities ▸ 4).
- **Notebook created:** `notebooks/12-radical-and-quadratic-form-equations.ipynb` (35 cells;
  verified end-to-end with `uv run jupyter nbconvert --execute` — 0 error outputs). The hand-written
  keep_valid() checker demonstrates the extraneous root: for √(x+2)=x it rejects x=−1 and keeps x=2.
- **Content:** radical equations + the extraneous-solution concept + the mandatory check step; two-
  radical equations; equations quadratic in form via substitution (u=x², √x, x^(1/3), 1/x, inner
  expr); factorable higher-degree via grouping + ZPP; don't-divide-by-x recall. Full proofs:
  Theorem 1 (raise to power n: forward safe; odd n reversible via one-to-one t↦tⁿ from topic 8; even
  n gives A=±B ⇒ extraneous), Theorem 2 (substitution principle), Theorem 3 (factor ⇒ solve via ZPP,
  FTA closure). Worked A–F incl. √(x+2)=x, √(2x+3)−√(x+1)=1, x⁴−13x²+36, x−5√x+6, grouping, x³=9x.
  AI hook: change of variables (u=x² turns a quartic into a parabola) → u-substitution / kernel trick.
- **Recall given:** 3-item warm-up — solve x²+2x+5=0 → −1±2i (topic 11); √(−4)·√(−9)=−6 (merge trap);
  i²³=−i. Solutions at end of §1.
- **What went well:** strong continuity — Theorem 1 reuses monotonicity/one-to-one of tⁿ (topic 8),
  ZPP + FTA (topics 5, 11), the don't-divide-by-x trap (topic 10), and the u=x² quartic→parabola plot
  ties change-of-variables straight to the substitution method. The extraneous root is the topic's
  spine and is demonstrated live by the checker.
- **Mistakes / misconceptions to revisit:** STILL no student-produced work seen (12 sessions).
  New likely error: forgetting the extraneous-root check (keeping a fake squared-equation root).
  Merge-negative-radicals trap re-quizzed again; both unconfirmed until the student submits work.
- **Homework given:** 20 exercises (single/two-radical with checks, quadratic-in-form with stated
  substitutions incl. x^(2/3), 1/x, inner-expression, and a complex-root branch, factorable/grouping,
  x⁴−16 over ℂ; proofs #18–20: odd-index needs no check, √f=g ⇒ g≥0 is why the check works, and prove
  the substitution principle for x⁴+bx²+c=0).
- **Next session plan:** Quick recall on the extraneous-root check + one quadratic-in-form
  substitution, then start **Solving Inequalities** (topic 5 of the Equations block): notebook
  `13-solving-inequalities.ipynb`.

### Session 11 — 2026-07-15
- **Topic taught:** Complex Numbers; Quadratic Equations in the Complex Number System
  (Equations & Inequalities ▸ 3). Finally solves the Δ<0 case left open in session 10.
- **Notebook created:** `notebooks/11-complex-numbers.ipynb` (41 cells; verified end-to-end
  with `uv run jupyter nbconvert --execute` — 0 error outputs). sympy returns the conjugate pair
  −3/4 ± (√31/4)i for 2x²+3x+5=0; numpy.roots agrees numerically; the ×i-rotation demo keeps all
  moduli equal.
- **Content:** imaginary unit i (i²=−1), a+bi, real/imag parts, equality = two real equations,
  Argand plane, conjugate, modulus. Arithmetic incl. division by the conjugate; ℂ is a field with
  NO order. Full proofs: Theorem 1 powers of i (mod 4), Theorem 2 conjugate homomorphism + real/
  pure-imaginary tests, Theorem 3 z·z̄=|z|², Theorem 4 |zw|=|z||w|, Theorem 5 triangle inequality,
  Theorem 6 √(−p)=i√p + the merge-radicals trap, Theorem 7 quadratic formula in ℂ (Δ<0 → conjugate
  pair, callback completing the square), Theorem 8 Conjugate Root Theorem + odd-degree corollary.
  Fundamental Theorem of Algebra stated (ℂ algebraically closed — the payoff of the whole solve-the-
  equation arc). AI hook: ×i = 90° rotation → FFT/rotations/eigenvalues.
- **Recall given:** 3-item warm-up — Δ of 2x²+3x+5 = −31 (no real roots, now solvable!); quadratic
  formula; √((3−x)²)=|x−3| sign trap; solutions at end of §3.
- **What went well:** strong continuity and closure — completes the Δ<0 gap from topic 10, reuses
  difference of squares (topic 4), ZPP (topic 5), conjugate-rationalising (topic 8), Pythagoras/
  distance for the modulus (topic 3), and Vieta (topic 10) to check the roots. FTA frames ℂ as the
  end of the "invent a new number" story.
- **Mistakes / misconceptions to revisit:** STILL no student-produced work seen (11 sessions).
  New likely error: merging negative radicals √(−4)·√(−9)=6 instead of −6 (Theorem 6 warning).
  The √(a²)=|a| trap re-quizzed again. Both unconfirmed until the student submits work.
- **Homework given:** 20 exercises (arithmetic/powers of i/conjugate-modulus/division, √ of
  negatives + the merge trap, solving Δ<0 quadratics, build-from-roots via Theorem 8, Vieta check,
  |z|=5 & Re=3 locus, 4th roots of unity + Argand plot; proofs #18–20: conjugate of a quotient,
  |z|=0⟺z=0 and |z̄|=|z|, and the Conjugate Root Theorem + odd-degree-has-a-real-root corollary).
- **Next session plan:** Quick recall on solving a Δ<0 quadratic + the negative-radical trap, then
  start **Radical Equations; Equations Quadratic in Form; Factorable Equations** (topic 4 of the
  Equations block): notebook `12-radical-and-quadratic-form-equations.ipynb`.

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