# Cross-reference verification matrix

Every factual claim from the three reports (Claude / Gemini / ChatGPT) run through
the `grid.py` + `solver.py` + `paths.py` + `straight_line.py` toolkit. Entries marked
**VERIFIED** have been independently recomputed and agree with the report. **REFUTED**
means the toolkit disagrees. **TRIVIA** = external fact that cannot be checked without
a primary source we don't have; not treated as evidence.

## 1. Grid metadata

| Claim | Source | Status | Computed |
|---|---|---|---|
| Grid is 14×14 | all | VERIFIED | 14 rows × 14 cols |
| Hyphen at (14,8), only non-letter | all | VERIFIED | `[(14,8)]` |
| Q, V, Z absent | Claude + Gemini | VERIFIED | all three counts = 0 |
| J, K appear exactly once | Gemini | VERIFIED | J=1, K=1 |
| Total letter cells = 195 | Gemini | VERIFIED | 195 |
| Total hex letters sum = 690 | Claude + Gemini | VERIFIED | 690 |
| Perimeter hex = 141 | Claude + Gemini | VERIFIED | 141 |
| Interior (12×12) hex = 549 | Claude | VERIFIED | 549 |

## 2. Row / column / diagonal sums

All sums are of hex letters (a=10…f=15), other letters contribute 0.

| Claim | Source | Status | Computed |
|---|---|---|---|
| Row 1 hex = 51 | all | VERIFIED | 51 |
| Row 2 hex = 89 | Claude | VERIFIED | 89 |
| Row 3 hex | — | — | 24 |
| Row 4 hex = 89 | Claude | VERIFIED | 89 |
| Row 5 hex | — | — | 41 |
| Row 6 hex = 32 | Claude + Gemini | VERIFIED | 32 |
| Row 7 hex = 63 | Claude | VERIFIED | 63 |
| Row 8 hex = 63 | Claude (implicit in 180) | VERIFIED | 63 |
| Row 9 hex | — | — | 39 |
| Row 10 hex | — | — | 64 |
| Row 11 hex | — | — | 34 |
| Row 12 hex | — | — | 21 |
| Row 13 hex = 52 | ChatGPT | VERIFIED | 52 |
| Row 14 hex = 28 | Claude (implicit in 180 = 89+63+28) | VERIFIED | 28 |
| Rows 1,7,13 = 166 | all | VERIFIED | 51+63+52 = 166 |
| Rows 2,8,14 = 180 | Claude | VERIFIED | 89+63+28 = 180 |
| Rows 1–5 = 294 | Claude | VERIFIED | 294 |
| Col 1 hex = 38 | Claude | VERIFIED | 38 |
| Col 5 hex = 73 | ChatGPT | VERIFIED | 73 |
| Col 6 hex = 33 | Gemini | VERIFIED | 33 |
| Col 7 hex = 70 | Claude | VERIFIED | 70 |
| Col 8 hex = 61 | Claude + Gemini | VERIFIED | 61 |
| Col 11 hex = 75 | ChatGPT | VERIFIED | 75 |
| Col 13 hex = 42 | Claude | VERIFIED | 42 |
| Cols 1,7,13 = 150 | Claude + ChatGPT | VERIFIED | 38+70+42 = 150 |
| Cols 5,11 = 148 | ChatGPT | VERIFIED | 73+75 = 148 |

All remaining column sums: c2=38, c3=37, c4=41, c9=66, c10=49, c12=43, c14=24.

## 3. Step-by-6 flat arithmetic progressions (the pivotal mechanic)

| Offset | First cell | Last cell | Hex sum | Semantic anchors hit |
|---:|---|---|---:|---|
| 1 | (1,1) r | (14,11) s | **124** | (1,1) top-left |
| 2 | (1,2) s | (14,12) s | **54** | — |
| 3 | (1,3) d | (14,13) i | **167** | — (none) |
| 4 | (1,4) i | (14,14) x | **134** | (2,8) ADD-start, (14,8) hyphen, (14,14) STEP terminal |
| 5 | (1,5) f | (14,9) t | **110** | (1,5) F-of-FIND, (1,11) S-of-START |
| 6 | (1,6) i | (14,10) e | **101** | — |
| 9 | (1,9) t | (14,1) t | **154** | — |

Findings:
- **Claude's 134 (offset 4) VERIFIED.** Its path simultaneously visits three
  independently-anchored cells: the start of ADD THE HEXADECIMALS at (2,8),
  the grid's only hyphen at (14,8), and the terminal of STEP BY SIX at (14,14).
- **Gemini's 167 (offset 3) VERIFIED arithmetically** but its path hits zero
  semantic anchors. The start cell (1,3) is "the first 'd' in reading order",
  which is a rationale but not a puzzle-anchored choice.
- **Claude's hex-letter sequence for offset 4 VERIFIED:** 10+10+10+13+10+14+12+11+11+12+10+11 = 134 (letters a,a,a,d,a,e,c,b,b,c,a,b).
- **Offset 5 is the only offset that starts at a semantic anchor (F of FIND).**
  Its sum is 110. Both (1,5) and (1,11) — the F of FIND and the S of START —
  are on its path.

## 4. Gemini's self-reference claim

Gemini's flagship argument: step-6 offset-3 hex sum = 167 AND the LAST ENTRY
ENTIRE INTEGER path terminates at flat index 167.

| Sub-claim | Status | Notes |
|---|---|---|
| step-6 offset-3 sum = 167 | VERIFIED | 167 |
| LAST ENTRY ENTIRE INTEGER has exactly 1 king-path | VERIFIED | 1 path |
| Path starts at (10,2) | VERIFIED | (10,2) |
| Path ends at (12,13) | VERIFIED | (12,13) |
| (12,13) has flat index 167 | VERIFIED | 11·14 + 13 = 167 |
| (12,13) is ON the offset-3 step path | **REFUTED** | (12,13) is NOT one of the 33 offset-3 cells |

So Gemini's self-reference is real but weaker than advertised: the two 167s
coincide, but one is a sum and the other is a positional index, and the
step path does not actually touch (12,13).

## 5. Long phrase tracing (king-paths)

| Phrase | Claim | Source | Status | Paths found |
|---|---|---|---|---|
| FIND THE START | 1 path | ChatGPT | VERIFIED | 1 |
| ADD THE HEXADECIMALS | 4 paths | ChatGPT | VERIFIED | 4 |
| STEP BY SIX | 3 paths | ChatGPT | VERIFIED | 3 |
| THERE IS A DATE ON WIRE | 2 paths | ChatGPT | VERIFIED | 2 |
| LAST ENTRY ENTIRE INTEGER | 1 path | ChatGPT | VERIFIED | 1 |
| TWENTY is traceable | no | ChatGPT | VERIFIED (no) | 0 |
| TWENTYSIX traceable | no | implicit | VERIFIED (no) | 0 |
| SIX traceable | yes | all | VERIFIED | exists |
| IX traceable | yes | all | VERIFIED | exists |
| TUNE traceable | yes | Gemini | VERIFIED | exists |
| TUNES traceable | yes | Gemini | VERIFIED | exists |
| HUNDRED traceable | yes | Claude | VERIFIED | exists |
| MOORE traceable | no | Gemini (refuted 600 theory) | VERIFIED (no) | 0 |
| THERE IS A DATE ON WIRE king-path hex sum = 89 | Claude | VERIFIED | both paths sum to 89 |

Phrase terminal and start cells (all computed):
- FIND THE START: (1,5) → (1,14) = flat 14
- ADD THE HEXADECIMALS: (2,8) or (3,6) → (11,1) = flat 141
- STEP BY SIX: (9,14) → (14,14) = flat 196
- THERE IS A DATE ON WIRE: (3,3) → (5,13) or (5,14) = flat 69 or 70
- LAST ENTRY ENTIRE INTEGER: (10,2) → (12,13) = flat 167

## 6. Straight-line words

| Claim | Source | Status | Notes |
|---|---|---|---|
| ALUMINUM straight-line (4,1)→(11,8) | Gemini | **REFUTED** | ALUMINUM traces once, but from **(2,8) → (9,1)** (anti-diagonal, going down-left). Gemini had the direction and endpoints wrong. |
| ALUMINUM exists as a single straight diagonal | Gemini (weaker form) | VERIFIED | One occurrence |
| ALUMINUM start cell coincides with ADD THE HEXADECIMALS start | new finding | VERIFIED | Both anchor at (2,8) |
| OPENER traces up column 1 from (7,1) | Gemini | **REFUTED** | OPENER traces column 1, but from **(6,1) up to (1,1)**, not from (7,1) |
| TIN traces | Gemini | VERIFIED | 2 straight-line traces: (12,3) SE diag to (14,5); (14,1) N to (12,1) |
| 'CAN OPENER'/'TIN OPENER' motif | Gemini | partial | OPENER and TIN both exist; their conceptual pairing is interpretive |

## 7. Element symbol / atomic number claims

Every element symbol in the reports was tested as a king-path and a straight line.
Atomic numbers are universal physical constants and confirmed.

| Element | Z | Symbol king-path traceable? | Symbol straight-line count |
|---|---:|---|---:|
| Al | 13 | yes | — |
| Sn | 50 | yes | — |
| Au | 79 | yes | — |
| V  | 23 | **no (letter V absent)** | 0 |
| Pd | 46 | yes | — |
| Ba | 56 | yes | — |
| Ac | 89 | yes | — |
| Ho | 67 | yes | — |
| Ar | 18 | yes | — |
| Fe | 26 | yes | — |
| Ne | 10 | yes | — |
| Dy | 66 | yes | — |

Sums referenced by reports:
- Al+Sn = 13+50 = 63 ✓
- Al+Sn+Au = 142 ✓
- Al+Ho+Ar+Fe+Ne+Sn = 13+67+18+26+10+50 = 184 ✓
- 33 + 23 + 79 = 135 ✓
- 33 × 23 = **759** (Claude flags the "760" candidate as off-by-one — correct flag)

## 8. Hexadecimal word values (reports' big-number candidates)

| Word | Reports' claimed value | Computed `int(word, 16)` | Status |
|---|---:|---:|---|
| 0xADDED | 712,685 then corrected to 11,394,781 | **712,173** | Claude's BOTH numbers wrong; actual value rules this candidate out arithmetically regardless |
| 0xCAB | 3,243 | 3,243 | VERIFIED |
| 0xDECADE | 14,598,366 | **14,600,926** | Claude's value wrong |
| 0xFACADE | 16,435,934 | 16,435,934 | VERIFIED |
| 0xBEEF | 48,879 | 48,879 | VERIFIED |
| 0xDEAD | 57,005 | 57,005 | VERIFIED |
| 0xFACE | 64,206 | 64,206 | VERIFIED |
| 0xCAFE | 51,966 | 51,966 | VERIFIED |
| 0xFEED | 65,261 | 65,261 | VERIFIED |
| 0xFADE | 64,222 | 64,222 | VERIFIED |
| 0xBEAD | 48,813 | 48,813 | VERIFIED |

All hex-word candidates are vastly outside the Jane Street historical answer
range (100–9,999). Treat as speculative bottom-tier regardless of magnitude.

## 9. Row 14 interpretation

| Claim | Source | Status | Notes |
|---|---|---|---|
| Row 14 visually reads "tunenty-tessix" ≈ TWENTY-SIX | all | descriptive | It does visually |
| TWENTY is actually traceable as a king-path | no | ChatGPT + verify | VERIFIED (no); row 14 has no valid TWENTY sub-trace |
| Row 14 encodes the number 26 | Claude/Gemini | interpretive | 26 is a visual reading, not a traceable word |
| Row 14 encodes 2026 (= puzzle publication year) | ChatGPT | interpretive | consistent with official April 2026 dating |
| Surplus letters TUNES can be anagrammed | Gemini | VERIFIED | u,n,t,e,s are indeed the extras |
| Tail reads SIX as a king-path | all | VERIFIED | exists |
| Tail reads IX (Roman 9) | Gemini | VERIFIED | exists; row 14 also ends …ix |

## 10. Meta-sums (self-describing candidates)

| Claim | Status | Computed |
|---|---|---|
| TUNES alphabet sum = 79 | VERIFIED | t+u+n+e+s = 20+21+14+5+19 = 79 |
| Sum of 5 axiom letter-counts (12+18+9+18+22) = 79 | VERIFIED | 79 |
| Au atomic number = 79 | VERIFIED | 79 |
| Three independent routes giving the same 79 | notable convergence | noted |

## 11. Trivia flagged but not verified (PWEI / The Wire)

These are external facts we can flag but not adjudicate without a primary source:

- PWEI "Can U Dig It?" 7″ duration: Claude says 3:15, Gemini reads 4:03. **Unresolved.**
- UK chart peak: Claude says #38, Gemini says #30. **Unresolved.**
- PWEI Track 6 memory-byte metadata = 27707 bytes (Gemini). Python confirms
  27707 in hex is **0x6C3B**, whose hex-digit sum is 6+12+3+11 = **32**. Gemini's
  narrative ADD-the-hexadecimals-of-0x6C3B does yield 32 mathematically, but the
  leap from a track's "memory used" metric to ADD THE HEXADECIMALS is not grid-endogenous.
- Claude's "dig said 23 times in the PWEI song": unverifiable without lyric analysis.
- Wire Tapper 22 durations → 3241/3242 (Gemini's original failure): flagged as rejected.

## 12. New findings not in any report

1. **Offset-5 (flat position 5) is the ONLY step-by-6 offset starting at a
   grid-semantic anchor.** (1,5) is the F of FIND THE START. (1,11), the S of
   START, also sits on this path. Hex sum = 110. No report identified this.
2. **ALUMINUM starts at (2,8)** — the exact same cell where ADD THE HEXADECIMALS
   starts. This cell is simultaneously: the start of an instruction, the start of
   the ALUMINUM diagonal, the entry point on offset-4 step, and a station on
   both DATE ON WIRE paths. It is by far the most structurally-privileged cell
   in the grid after (14,8).
3. **Both DATE ON WIRE paths pass through (2,8) at position 10.** The 89 sum
   for each path coincides with row-2 hex sum = 89 and row-4 hex sum = 89, an
   already-noticed coincidence (Actinium Ac Z=89).

## 13. Summary scorecard per report

- **Claude's report** — arithmetically strongest. Core claim (134) is the only
  step-by-6 candidate that threads 3 puzzle-anchored cells. Minor errors:
  0xADDED numeric value, 0xDECADE numeric value. Correctly flags 33×23=759
  and PWEI song-length disagreement.
- **Gemini's report** — the 167 self-reference is genuine but weaker than the
  report implies (the step path does not visit (12,13)). Reports (4,1)→(11,8)
  for ALUMINUM: wrong direction; correct direction is (2,8)→(9,1). Reports (7,1)
  for OPENER: wrong; correct start is (6,1). The "Vanadium absent = 23"
  argument is clever but requires the exogenous leap V/U-orthography.
- **ChatGPT's report** — phrase-tracing is perfect (all 5 counts match). The
  core 2192 derivation (rows 1,7,13 = 166 + 2026) is arithmetically correct,
  but both its addend choice (wire = 2026 vs 26) and its entry-selection
  (row-stepping vs flat-stepping) are parameter choices the grid does not
  force. 192 is a parallel weaker candidate.

Phase D (`evaluation.md`) ranks these against an explicit rubric.
