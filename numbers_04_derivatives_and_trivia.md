# Numbers, part 4 — year-shifts, element sums, hex words, and trivia

All derivations that fuse a base grid number with an external or secondary
operation. Each entry has its base, its operation, and a verdict.

## Year-shifted candidates (base + 2026)

Jane Street's Knight Moves 6 (October 2024) was year-shifted; Claude's report
cites this as precedent. If the April-2026 puzzle follows, the year-shift of
any grid sum becomes a candidate.

| Base | Base meaning | +2026 | Notes |
|---:|---|---:|---|
| 110 | step-6 offset-5 | **2136** | FIND-anchored |
| 134 | step-6 offset-4 | **2160** | primary hedge |
| 141 | perimeter | 2167 | |
| 150 | cols 1,7,13 | 2176 | |
| 166 | rows 1,7,13 | **2192** | ChatGPT's primary |
| 167 | step-6 offset-3 | 2193 | Gemini's self-reference + year |
| 180 | rows 2,8,14 | 2206 | |
| 123 | ADD king-path | 2149 | |
| 52 | FIND king-path | 2078 | |
| 25 | STEP king-path | 2051 | |
| 89 | DATE king-path | 2115 | |
| 80 | LAST king-path | 2106 | |
| 369 | sum of 5 phrase sums | 2395 | |
| 549 | interior | 2575 | |
| 690 | total | 2716 | |
| 79 | axiom-length sum / TUNES / Au | 2105 | |

## Element atomic-number candidates

Elements whose symbols are either straight-line or king-path traceable in the
grid (V excluded because the letter V is absent). Atomic numbers are fixed.

| Element | Z | Traceable? | Individual | Used in sum candidate? |
|---|---:|---|:-:|:-:|
| Al | 13 | straight-line diag (2,8)→(9,1), king yes | yes | yes |
| Sn | 50 | 2× straight, king yes | yes | yes |
| Au | 79 | king yes | yes | yes |
| V  | 23 | **absent** (missing letter) | no | yes (as "missing=23") |
| Pd | 46 | king yes | — | via Au−33 arithmetic |
| Ba | 56 | king yes | — | via 33+23 |
| Ac | 89 | king yes | — | coincides with row 2, 4, DATE path |
| Ho | 67 | king yes | — | 134/2, DATE-term-b running total |
| Ar | 18 | king yes | — | used in 184 sum |
| Fe | 26 | king yes | — | used in 184 sum; also row-14 visual "26" |
| Ne | 10 | king yes | — | used in 184 sum |
| Dy | 66 | king yes | — | = col 9 hex sum; = 33×2 |

Element sums proposed by reports:
- Al + Sn = 13 + 50 = **63** (= row 7 hex)
- Al + Sn + Au = 13 + 50 + 79 = **142**
- Al + Ho + Ar + Fe + Ne + Sn = 13 + 67 + 18 + 26 + 10 + 50 = **184**
- 33 + 23 + 79 = **135** (meta-sum of three "strong" small candidates)
- 33 × 23 = **759** (explicitly flagged as not 760)

## Hex-word candidates (concatenation reading of 6 letters → 1 integer)

Useful only if "ADD THE HEXADECIMALS" is reinterpreted as "concatenate hex
letters to make a hex numeral". All are verified:

| Word | Decimal value | Grid tracing |
|---|---:|---|
| 0xCAB | 3,243 | king-path probably exists near (6,12) |
| 0xBEEF | 48,879 | requires b-e-e-f contiguous; plausible |
| 0xBEAD | 48,813 | |
| 0xCAFE | 51,966 | |
| 0xDEAD | 57,005 | dig/grave theme |
| 0xFACE | 64,206 | |
| 0xFADE | 64,222 | |
| 0xFEED | 65,261 | |
| 0xADDED | 712,173 | thematically perfect but Claude's numbers (712685 / 11394781) were both wrong; actual is 712,173. Still outside JS range. |
| 0xDECADE | 14,600,926 | Claude's 14,598,366 wrong |
| 0xFACADE | 16,435,934 | |

All above the 100–9,999 Jane Street historical band; even the smallest (3,243)
was already proposed as 0xCAB and rejected. Treat this entire class as
low-priority unless the puzzle specifically demands a hex-numeral output.

## Meta-sums (self-describing numbers)

| Derivation | Value | Notes |
|---|---:|---|
| TUNES alphabet sum | **79** | t+u+n+e+s = 20+21+14+5+19 |
| Axiom letter-count sum (12+18+9+18+22) | **79** | three coincident routes to 79 |
| Au atomic number | **79** | "dig" = gold |
| Missing-letter alphabet sum (Q+V+Z) | **65** | 17+22+26 |
| Sum of all 5 phrase king-path hex sums | **369** | 52+123+25+89+80 |
| Total hex sum × 6 | **4,140** | 690 × 6 |
| Grid dimensions | **196** | 14² |
| Total letter cells | **195** | 196 − 1 hyphen |

## External trivia (flagged only)

All values below depend on data outside the grid. They cannot be verified here.
Reports disagree on some; treat as unreliable unless the user supplies a primary source.

| Datum | Reports | Status |
|---|---|---|
| PWEI "Can U Dig It?" 7″ duration | Claude 3:15 vs Gemini 4:03 | unresolved |
| UK chart peak | Claude #38 vs Gemini #30 | unresolved |
| PWEI Track 6 memory bytes = 27707 | Gemini | 27707 in hex = 0x6C3B; digit sum 32 verified |
| Alan Moore "knows the score" → 20 | Gemini/Claude discussion | MOORE not traceable; 600 explicitly rejected |
| PWEI song year 1989 | Gemini | external fact |
| "dig" said 23× in song | Gemini | unverifiable without audio |
| Wire Tapper 22 durations → 3241/3242 | Gemini's old theory | explicitly REJECTED by puzzle mechanics |
| "A score" = 20 | Gemini | literary; would make row-14 read "TWENTY(=20) SIX" but TWENTY doesn't trace |

## Confirmed rejected (from the task context)

These integers were previously submitted and wrong:

- 600 (Alan Moore Unearthing)
- 7 (count of 'u' in grid)
- 3241 (Wire Tapper decimals sum)
- 3242 (Wire Tapper hex sum)
- 26 (row-14 visual reading)
- 22 (alphabet position of V / hyphen coords)

Reject derivatives of these as well. 192 = 166+26 and 148 = coord-(14,8)
cluster near these rejected values; flag as low-confidence.

Next: `numbers_05_final_ranking.md` — updated tier ranking with the deep-dive findings.
