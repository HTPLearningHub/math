# CLAUDE.md

## Math mentoring mode
When I ask for a math lesson (or say "let's continue math"):
1. First READ `math-progress.md` to recall where we are and my weak spots.
2. Act as my mathematics mentor following the rules in `math-tutor-prompt.md`.
3. Teach topics in the order listed in `math-topic.md`, one at a time.
4. For each tutorial, GENERATE a Jupyter notebook in `notebooks/` named
   `NN-topic.ipynb` (zero-padded order). The notebook must contain: intuition +
   explanation (markdown, B1 English), formal definitions, every theorem proved in
   full, worked examples, runnable Python that demonstrates the concept (numpy /
   sympy / matplotlib / pandas, with comments on every math-library line), exactly
   20 exercise cells I fill in myself (easy → hard, ending with proofs), and a short
   `uv` note. I should be able to re-run the whole notebook to repeat the tutorial.
   Keep code runnable and self-contained. Manage dependencies with `uv`.
5. At the END of every session, UPDATE `math-progress.md`: skill ledger,
   current focus, weak spots, a new Session Log entry (newest first), and the
   name of the notebook created.

Goal: take me from foundational math to research-level mathematics for AI.
