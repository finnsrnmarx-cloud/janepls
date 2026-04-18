# Numbers, part 5 — updated tier ranking with deep-dive findings

Consolidates `numbers_01` … `numbers_04`. The original `evaluation.md`
counted 134 as hitting 3 anchors; the expanded anchor set in the deep dive
confirms **134 hits 5 total anchors (3 strong + 2 weak)**, which widens its
lead. 110 picked up a third anchor (LAST ENTRY terminal at (12,13), flat 167),
making it the strongest alternative.

## Tier S — best justified

| # | Cand | Score | Derivation | Why top-tier |
|---|---:|---:|---|---|
| 1 | **134** | 14/15 | step-6 flat offset 4, hex sum | 5 anchor hits (ADD-start, ADD-alt, DATE-term-b, hyphen, STEP-terminal); strongest k=6 offset |
| 2 | 110 | 14/15 | step-6 flat offset 5, hex sum | 3 anchors including F-of-FIND as the start cell and (12,13) LAST-terminal on path |

Tied on rubric; 134 prefered because it terminates at a puzzle-distinguished
cell ((14,14)), whereas 110 ends at (14,9) which is unmarked.

## Tier A — credible alternatives

| # | Cand | Derivation | Note |
|---|---:|---|---|
| 3 | 2160 | 134 + 2026 | year-shift hedge of the primary |
| 4 | 2192 | 166 + 2026 | ChatGPT's primary; row-stride-6 over year |
| 5 | 167 | step-6 flat offset 3 | Gemini's primary; sum coincides with flat index of LAST ENTRY terminal |
| 6 | 2136 | 110 + 2026 | year-shift of Tier S #2 |

## Tier B — structural readings

| # | Cand | Derivation | Note |
|---|---:|---|---|
| 7 | 166 | rows 1,7,13 | base of 2192 without year |
| 8 | 150 | cols 1,7,13 | column analog |
| 9 | 148 | cols 5,11 | F-of-FIND column-stride |
| 10 | 141 | perimeter hex | "can opener" outer shell |
| 11 | 549 | interior hex | complement of 141 |
| 12 | 690 | total hex | simplest ADD reading |
| 13 | 124 | step-6 offset 1 | path starts at top-left |
| 14 | 101 | step-6 offset 6 | — |
| 15 | 180 | rows 2,8,14 | alternate row stride |
| 16 | 294 | rows 1–5 | Claude's "discovery zone" |
| 17 | 33 | col 6 alone | (a+c+b); "VANADIUM" decimal sum |
| 18 | 61 | col 8 alone | column of the hyphen |

## Tier C — phrase-path and meta

| # | Cand | Derivation | Note |
|---|---:|---|---|
| 19 | 52 | FIND king-path hex sum | also = row 13 hex |
| 20 | 123 | ADD king-path hex sum | also = cols 2,8,14 |
| 21 | 25 | STEP king-path hex sum | lowest |
| 22 | 89 | DATE king-path hex sum | three coincident paths to 89 |
| 23 | 80 | LAST king-path hex sum | |
| 24 | 369 | sum of all 5 phrase sums | meta-sum |
| 25 | 79 | axiom-length sum = TUNES = Au | three-way coincidence |
| 26 | 63 | Al+Sn = row 7 | |
| 27 | 142 | Al+Sn+Au | |
| 28 | 184 | 6-element sum | clean chemistry reading |
| 29 | 135 | 33+23+79 | meta-sum of small candidates |
| 30 | 65 | Q+V+Z alphabet | missing-letter reading |

## Tier D — hex-word concatenations (all outside JS range)

All verified arithmetically but all exceed 1,000 and most exceed 10,000.
Only plausible if "ADD THE HEXADECIMALS" means concatenate, not sum.

3243 (CAB), 48813 (BEAD), 48879 (BEEF), 51966 (CAFE), 57005 (DEAD),
64206 (FACE), 64222 (FADE), 65261 (FEED), 712,173 (ADDED),
14,600,926 (DECADE), 16,435,934 (FACADE).

## Tier E — rejected / disqualified

Explicitly known-wrong submissions or derivatives:
- 600 (Alan Moore — MOORE not traceable)
- 7 (U count)
- 26 (row-14 visual — TWENTY not traceable)
- 22 (V alphabet position / hyphen coords)
- 3241, 3242 (Wire Tapper arithmetic)
- 760 (33×23 off-by-one; true value 759)

## One-paragraph rationale for the top 5

1. **134** — Only step-6 offset hitting 3 strong anchors ((2,8),(14,8),(14,14)).
   Arithmetic verified. Running total has internal coincidences (67 midpoint at
   DATE-term-b, 123 at ADD-terminal area). Deep dive confirms no competing
   offset or stride matches this density of puzzle-defined cells.
2. **110** — Alternative primary if the FIND axiom forces the start cell.
   Offset-5 begins at (1,5) = F of FIND THE START and passes through (12,13)
   = LAST-terminal (flat 167). Fewer anchor hits than 134 but cleaner start.
3. **2160** — Year-shifted 134. Mandatory hedge if JS's April-2026 convention
   appends the publication year.
4. **2192** — ChatGPT's primary. Row-stride reading of "STEP BY SIX". Weaker
   on parameter-freeness (three choices: row vs flat, which rows, 2026 vs 26)
   but internally consistent.
5. **167** — Gemini's primary. The arithmetic self-reference (sum = flat index
   of LAST-terminal) is real but the step path itself does not visit (12,13).
   Keep as reserve; high chance it's a near-miss.

## Submission strategy

- Primary submission: **134**.
- If allowed one hedge: **2160**.
- If allowed two hedges: **2160** + **110**.
- If allowed three hedges: **2160**, **110**, **2192**.

The full file set is `numbers_01`…`numbers_05` plus `verification.md`,
`evaluation.md`, `RECOMMENDATION.md`, and the Python solver (`grid.py`,
`solver.py`, `paths.py`, `straight_line.py`, `deep_dive.py`, `deep_dive2.py`).
