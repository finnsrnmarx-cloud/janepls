# Theory evaluation and ranking

Every top candidate from the three reports scored against a 5-axis rubric.
Evidence is drawn exclusively from `verification.md`.

## Rubric (5 axes, max 3 points each → 15 max)

1. **Arithmetic correctness** — the candidate falls out of its claimed computation.
2. **Anchor coverage** — how many puzzle-distinguished cells the derivation uses:
   (1,5) F of FIND, (1,11) S of START, (2,8) ADD start, (14,8) hyphen/wire, (14,14) STEP terminal, (10,2) LAST ENTRY start, (12,13) LAST ENTRY terminal.
3. **Axiom coverage** — how many of the 5 embedded instructions the derivation explicitly uses (FIND THE START, ADD THE HEXADECIMALS, STEP BY SIX, THERE IS A DATE ON WIRE, LAST ENTRY ENTIRE INTEGER).
4. **Parameter-freeness** — how many free choices (which row set, which offset, whether to add 2026, etc.) the solver had to pick by hand.
5. **Jane Street style fit** — integer size (historically 100–9,999), no external trivia required, elegant.

## Scorecard

| # | Candidate | Derivation | Arith | Anchor | Axiom | Params | Style | **Total** |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | **134** | step-by-6 flat, offset 4, sum hex letters | 3 | 3 (hits ADD-start, hyphen, STEP-terminal) | 3 (ADD, STEP, and hyphen = DATE ON WIRE) | 2 (offset choice forced by anchor coincidence) | 3 | **14** |
| 2 | **2192** | rows 1,7,13 hex sum + 2026 | 3 | 1 (row-selection is "every 6th row", weak anchor) | 2 (ADD, STEP, DATE — 2026 reading) | 1 (row-vs-flat is a free choice; 2026 vs 26 is a free choice) | 3 | **10** |
| 3 | **167** | step-by-6 flat, offset 3, sum hex letters | 3 | 0 (no distinguished cell on path) + 1 coincidence (= flat index of (12,13) LAST ENTRY terminal) | 2 (ADD, STEP, weak LAST ENTRY gesture) | 2 (start "first d" is a principled but not forced choice) | 3 | **11** |
| 4 | 192 | rows 1,7,13 + 26 | 3 | 1 | 2 (weak LAST ENTRY reading of row 14 as 26) | 1 | 2 | **9** |
| 5 | 110 | step-by-6 flat, offset 5 | 3 | 3 (starts at F-of-FIND, hits S-of-START) | 3 (FIND, STEP, ADD) | 3 (start is fully forced: "begin at F of FIND THE START") | 2 (no way to hit hyphen or LAST ENTRY terminal) | **14** |
| 6 | 141 | perimeter hex sum | 3 | 1 (perimeter is "outer shell") | 1 (ADD only) | 1 (perimeter vs interior is a choice) | 2 | **8** |
| 7 | 549 | interior hex sum | 3 | 1 | 1 | 1 | 2 | **8** |
| 8 | 690 | all hex letters | 3 | 0 | 1 (ADD only — doesn't use STEP) | 3 | 2 | **9** |
| 9 | 166 | rows 1,7,13 hex sum | 3 | 1 | 2 | 2 | 2 | **10** |
| 10 | 2160 | 134 + 2026 | 3 | 3 | 3 | 1 (+2026 not forced) | 3 | **13** |

### Axis-by-axis commentary

**Arithmetic correctness.** All top candidates except the PWEI/Wire Tapper cluster
are arithmetically sound. The disqualifying failures (760, 3241/3242, 600, 26, 7)
are already ruled out in the verification matrix.

**Anchor coverage — the decisive axis.**
- **134**: threads (2,8), (14,8), (14,14). Three distinct semantic anchors on a
  single arithmetic progression. Uniquely strong.
- **110**: starts at (1,5) F-of-FIND, passes through (1,11) S-of-START. Anchor-
  coverage tied with 134 but in a different sense — start and internal anchors
  rather than start/middle/end.
- **167**: no step-path anchor hits, only a coincidence with the flat index of
  the LAST ENTRY terminal. The "self-reference" is real but one step weaker:
  the sum *names* a distinguished cell it does not *visit*.
- **2192 / 166 / 192**: the "every 6th row" justification only hits anchor
  cells incidentally. Row 7 contains (7,?) but no cell on rows 1/7/13 is a
  canonical anchor. Row selection by stride is a parameter choice.
- **141 / 549 / 690**: no semantic anchoring; these are whole-set sums.

**Axiom coverage.**
- **134** uses ADD THE HEXADECIMALS (hex sum), STEP BY SIX (stride), and
  touches the hyphen which is the DATE ON WIRE payload. It does not explicitly
  use FIND THE START or LAST ENTRY ENTIRE INTEGER as operations.
- **110** uses FIND THE START (origin = F of FIND), ADD THE HEXADECIMALS (hex sum),
  STEP BY SIX (stride). It does not use the wire or LAST ENTRY.
- **2192** uses ADD, a rowwise form of STEP (every 6th row, not every 6th entry),
  and DATE ON WIRE (read as 2026). It does not FIND — it just starts at row 1.
- **167** uses ADD and STEP; LAST ENTRY is a secondary after-the-fact coincidence
  only.

**Parameter-freeness.**
- **134** has one underdetermined parameter (which offset among 1..6). The anchor
  coincidence forces offset 4, so the parameter is effectively eliminated by evidence.
- **110** has zero free parameters once the FIND start is honored literally.
- **167** has the same offset-choice parameter, but offset 3 is not uniquely
  forced — it's chosen as "first hex-compliant character in reading order",
  which is a defensible but not forced rationale.
- **2192** has three parameter choices: row-stride vs column-stride vs flat-stride,
  which rows (1/7/13 vs 2/8/14), and 26 vs 2026 for the wire addend. Any one
  change dramatically shifts the answer.

**Jane Street style fit.** All four-digit answers fit the historical band.
Sub-100 candidates (23, 26, 32, 33, 46, 56, 63, 79, 89) are rare in JS history.
Above 10,000 candidates are essentially zero in JS history.

## The two candidates that tie at 14/15: 134 vs 110

The toolkit identifies a previously-unnoticed candidate — **110**, from step-by-6
starting at (1,5), the F of FIND THE START. It ties 134 on the rubric. Their
trade-off:

- **134** is stronger on middle+end anchors (hyphen, terminal).
- **110** is stronger on the FIND axiom (its start is literally the F of FIND).

Sub-arguments:
- 110's path does not reach (14,8) or (14,14) because 32 terms of stride 6
  starting at 5 end at 5 + 31·6 = 191 = (14,9), one short of the hyphen.
- 134's path touches (2,8) at its 4th element, (14,8) at its 32nd, and (14,14)
  at its 33rd. The (14,14) touch is the strongest single piece of evidence for
  134, because STEP BY SIX's king-path terminal is (14,14), so the stride path
  ends where the instruction-path ends.

On balance 134 is more aligned with the puzzle's stated mechanics than 110,
because only 134 terminates at a puzzle-distinguished cell ((14,14)). 110 is
the best secondary hedge if the FIND axiom is meant to fix the start.

## Candidates with possible "year" variants

If LAST ENTRY ENTIRE INTEGER instructs the solver to append 2026 (the year on
the wire / bottom row / publication) as a whole number, the corresponding
year-shifted candidates become:

| Base | +2026 | Notes |
|---:|---:|---|
| 134 | **2160** | year-shift of the strongest core candidate |
| 110 | 2136 | year-shift of offset-5 |
| 166 | 2192 | ChatGPT's main candidate |
| 150 | 2176 | column analog |
| 141 | 2167 | perimeter |
| 549 | 2575 | interior |
| 690 | 2716 | total |
| 167 | 2193 | year-shift of Gemini's core |

Whether to year-shift is a genuine ambiguity. Jane Street's precedent on year-
shifting (Knight Moves 6, Oct 2024 cited by Claude) is suggestive but not
authoritative. If the puzzle wants one positive integer, the more minimal
reading is to NOT year-shift unless the grid compels it.

## Top 5 submissions (ranked)

1. **134** — primary. Unique triple-anchor step-by-6 path.
2. **2160** — first hedge. Year-shift of 134 if JS's convention in 2026 is to append the year.
3. **110** — independent alternative. Forced FIND-start is its own argument.
4. **2192** — ChatGPT's primary; valid if row-stride is preferred over flat-stride and wire-reads-2026.
5. **167** — Gemini's primary; keep in reserve as the arithmetic-coincidence hedge.

Everything else (perimeter, interior, element sums, hex-word conversions,
PWEI trivia, Alan Moore 600, 26) either failed a verification step or scores
too low on anchor + parameter axes to compete.
