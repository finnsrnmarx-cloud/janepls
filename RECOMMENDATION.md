# Can U Dig It? — recommendation

## Primary submission: **134**

Derivation: treat the grid as a 196-element row-major flat array (hyphen at
position 190 counts as 0). Step by six from flat offset 4, selecting positions
4, 10, 16, 22, …, 196 — 33 cells total. Sum the hex-digit values of every a–f
letter on the path. Result: **134**.

Why this is the strongest candidate (full scoring in `evaluation.md`):
- Only step-by-6 offset whose path simultaneously visits **three
  puzzle-distinguished cells**: (2,8) = start of ADD THE HEXADECIMALS, (14,8) =
  the only hyphen (= "DATE ON WIRE" payload), (14,14) = terminal of STEP BY SIX.
- Simultaneously satisfies ADD THE HEXADECIMALS (literal hex sum), STEP BY SIX
  (literal stride), and THERE IS A DATE ON WIRE (hyphen on path).
- Fully arithmetically verified; the 12 hex letters on the path are
  a,a,a,d,a,e,c,b,b,c,a,b = 10+10+10+13+10+14+12+11+11+12+10+11 = 134.

## Hedge 1: **2160**

134 + 2026. Use this if Jane Street's April-2026 convention appends the
publication year as the "LAST ENTRY ENTIRE INTEGER" — a reading ChatGPT's
report defends, and that the puzzle's bottom-row date encoding arguably
supports.

## Hedge 2: **110**

Independent mechanic. Step-by-6 from flat offset 5, whose start cell (1,5) is
literally the F of FIND THE START. Path also hits (1,11) = S of START. Hex
sum = 110. Chosen as an independent hedge because its start is forced by
FIND whereas 134's is forced by anchor coincidence; different mistakes
rule out different candidates. If the solver's mistake is mis-locating the
start cell, 110 wins; if it is missing the anchor-coincidence argument, 134 wins.

## Hedge 3: **2192**

ChatGPT's primary. 166 (= rows 1, 7, 13 hex sum) + 2026. Parameter-heavy
derivation (row-stride chosen, rows 1/7/13 chosen over 2/8/14, year chosen
over 26), but all three choices are internally defensible.

## What would disprove the primary

- If Jane Street's solution cites a start cell other than (2,8) / (1,5) / (1,3),
  all step-by-6 candidates become suspect simultaneously.
- If the solution uses a non-hexadecimal operation (alphabet-index sums,
  atomic numbers, semitone counts) the ADD THE HEXADECIMALS axiom was
  misinterpreted.
- If the published answer is a sub-100 integer (23, 26, 46, 56, 79, 89),
  the grid's stride mechanic was a red herring and the answer is pure element
  chemistry or atomic-number arithmetic.
- If the answer is a six-digit hex concatenation (0xBEEF, 0xDEAD etc.) the
  "ADD" should have been "concatenate" — treat as an unlucky misreading.

## Post-mortem checklist (once Jane Street publishes)

1. Compare the solution's start cell against Claude's offset-4, Gemini's
   offset-3, ChatGPT's rows-1/7/13, and the new offset-5 finding.
2. Determine whether the wire reading (2026 vs 26 vs none) was intended.
3. Record whether element/atomic-number trivia was the real mechanic, a
   red herring, or a secondary confirmation.
4. Record the PWEI "Can U Dig It?" track as a confirmed or rejected exogenous
   vector (two reports disagree on song length and chart peak; only a
   primary source adjudicates).

## Reproducibility

The solver is `grid.py` + `solver.py` + `paths.py` + `straight_line.py`.
Sanity tests: `python tests.py`. Key runs:

```python
from solver import step_by_six_cells, hex_sum
hex_sum(step_by_six_cells(4))   # -> 134
hex_sum(step_by_six_cells(3))   # -> 167
hex_sum(step_by_six_cells(5))   # -> 110
```

All verification claims in `verification.md` can be re-derived from these
primitives.
