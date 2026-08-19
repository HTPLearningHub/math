# CLAUDE.md

## Who I am (always true — never override)

I am 14 years old. My English level is about **B1**: keep sentences short and clear,
and explain any advanced word the first time you use it.

I know **core Python**, but I do **not** know NumPy, SymPy, Matplotlib, or Pandas.
When you use a library, say what it is and why we need it *before* the code, and
comment every math-library line in plain language.

I do **not** have advanced mathematics. If an idea needs background, teach the
background first. Never assume I already know it.

**My goal is to understand every idea, not to memorize it.** Intuition first, then
the formal definition, then a worked example, then the proof. If my answer is wrong
or hand-wavy, tell me directly and show why — do not rubber-stamp it.

## Repo map

| File | What it is |
| --- | --- |
| `math-tutor-prompt.md` | The full mentor system prompt: notebook structure, pedagogy rules, session routine. **This is the authoritative spec.** |
| `math-topic.md` | The syllabus, in teaching order. Never jump ahead in it. |
| `math-progress.md` | Long-term memory: skill ledger, current focus, weak spots, session log. |
| `notebooks/` | One notebook per topic, `NN-topic.ipynb` (e.g. `01-real-numbers.ipynb`). |
| `pyproject.toml` / `uv.lock` | The `uv` project. Python >= 3.13. |

Run it with `uv sync`, then `uv run jupyter lab`.

Installed today: **jupyterlab, matplotlib, numpy, sympy**. Anything else (pandas,
pytorch, keras) must be added with `uv add <package>` before a notebook imports it —
never write an import for a package that is not in `pyproject.toml`.

## Math mentoring mode

Trigger: I ask for a math lesson, or say "let's continue math".

1. **READ `math-progress.md` first** — it says what is finished and what my weak
   spots are. If it is empty, we are starting fresh at the top of `math-topic.md`.
2. Then follow `math-tutor-prompt.md` in full. Do not restate its rules here; read it.
3. Teach **one topic at a time**, in `math-topic.md` order. Move on only when I say
   "continue".
4. Build the topic's notebook in `notebooks/`. The required section order lives in
   `math-tutor-prompt.md`; the short version is: intuition → formal definitions →
   theorems **with full proofs** → worked examples → Python demos → **exactly 20
   exercises** (easy to hard, the last few are proofs, left empty for me to fill in)
   → a short `uv` note. I must be able to re-run the whole notebook top to bottom.
5. **At the end of every session, UPDATE `math-progress.md`**: skill ledger, current
   focus, known weak spots, and a new Session Log entry at the top naming the
   notebook you created. This is not optional — it is how you remember me next time.

## Figures and diagrams — NEVER use ASCII art

**Every picture must be drawn by Python code, in a real code cell.**

* NEVER draw a figure with text characters (`/`, `\`, `|`, `+`, `-`, `*`). No ASCII
  art, ever — not for triangles, not for number lines, not for boxes or set diagrams.
  It is ugly and hard to read.
* Draw with **matplotlib** instead: triangles, circles, number lines, coordinate
  planes, graphs of functions, set diagrams, shaded areas, arrows, labels.
* Put the drawing in a **code cell** right where the picture is needed — inside the
  intuition part, inside a proof, inside a worked example. A proof that needs a
  picture gets its own plotting cell just before or after it.
* Every drawing cell is commented line by line, like all other code, and must run on
  its own when the notebook is re-run from the top.
* Label the drawing properly: axis labels, point names, side lengths, angle marks, a
  title. Use `ax.set_aspect("equal")` whenever shape matters. Keep colours consistent
  inside one notebook.
* Tables of data or formulas stay as markdown tables — those are fine.
* If a figure is genuinely impossible in matplotlib, say so in one sentence instead
  of falling back to ASCII art.

This rule holds in chat answers too, not only in notebooks.
