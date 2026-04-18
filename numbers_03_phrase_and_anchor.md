# Numbers, part 3 — phrase king-path sums and the offset-4 walkthrough

## Phrase king-path hex sums

Each of the five grid-embedded instructions is a king-path through the grid
without cell reuse. Summing hex digits along each path:

| Phrase | Paths | Hex sum per path | Length | Start | End |
|---|---:|---:|---:|---|---|
| FIND THE START | 1 | **52** | 12 | (1,5) | (1,14) |
| ADD THE HEXADECIMALS | 4 | **123** | 18 | (2,8) or (3,6) | (11,1) |
| STEP BY SIX | 3 | **25** | 9 | (9,14) | (14,14) |
| THERE IS A DATE ON WIRE | 2 | **89** | 18 | (3,3) | (5,13) or (5,14) |
| LAST ENTRY ENTIRE INTEGER | 1 | **80** | 22 | (10,2) | (12,13) |

All paths for the same phrase give identical hex sums; multiplicity comes from
sub-paths through repeated letter cells but they accumulate the same hex totals.

Sum of all 5 phrase hex sums: **52 + 123 + 25 + 89 + 80 = 369**.

## Coincidences with step-6 offset-4 running total

Offset-4 is the candidate = 134. Walking it cell-by-cell, the running hex
total passes through several phrase-related values:

| Flat pos | Cell | Char | Val | Running | Anchor / coincidence |
|---:|---|---|---:|---:|---|
| 4 | (1,4) | i | 0 | 0 | |
| 10 | (1,10) | h | 0 | 0 | |
| 16 | (2,2) | h | 0 | 0 | |
| 22 | (2,8) | a | 10 | **10** | **ADD-start** |
| 28 | (2,14) | a | 10 | 20 | |
| 34 | (3,6) | a | 10 | 30 | ADD-start-alt |
| 40 | (3,12) | w | 0 | 30 | |
| 46 | (4,4) | d | 13 | 43 | |
| 52 | (4,10) | a | 10 | 53 | |
| 58 | (5,2) | t | 0 | 53 | |
| 64 | (5,8) | m | 0 | 53 | |
| 70 | (5,14) | e | 14 | **67** | **DATE-term-b**; running = 134/2 exactly |
| 76 | (6,6) | k | 0 | 67 | (K singleton) |
| 82 | (6,12) | c | 12 | 79 | |
| 88 | (7,4) | p | 0 | 79 | |
| 94 | (7,10) | b | 11 | 90 | |
| 100 | (8,2) | u | 0 | 90 | |
| 106 | (8,8) | b | 11 | 101 | |
| 112 | (8,14) | w | 0 | 101 | |
| 118 | (9,6) | c | 12 | 113 | |
| 124 | (9,12) | g | 0 | 113 | |
| 130 | (10,4) | m | 0 | 113 | |
| 136 | (10,10) | t | 0 | 113 | |
| 142 | (11,2) | a | 10 | **123** | **= ADD HEXADECIMALS king-path hex sum** |
| 148 | (11,8) | t | 0 | 123 | |
| 154 | (11,14) | n | 0 | 123 | |
| 160 | (12,6) | g | 0 | 123 | |
| 166 | (12,12) | b | 11 | **134** | |
| 172 | (13,4) | i | 0 | 134 | |
| 178 | (13,10) | p | 0 | 134 | |
| 184 | (14,2) | u | 0 | 134 | |
| 190 | (14,8) | - | 0 | 134 | **hyphen** |
| 196 | (14,14) | x | 0 | 134 | **STEP-terminal** |

The running total reaches **123** (= ADD HEXADECIMALS king-path hex sum) at
flat position 142 — two cells after passing (11,1) which is the ADD-terminal.
It then gains exactly 11 more at (12,12) and stabilizes at 134 for the
remaining cells, including the hyphen and the grid terminal. No further hex
letters appear on the path after (12,12).

Also notable: at the DATE-terminal-b cell (5,14), the running total is 67 = 134/2 — the exact midpoint of the final answer.

## Hex letters concatenation (alternative reading of "ADD")

If "ADD THE HEXADECIMALS" is read as "concatenate hex letters" rather than
"sum hex letters", offset-4 produces:

```
a a a d a e c b b c a b
```

Interpreted as a single hex number: **0xAAADAECBBCAB = 187,662,938,651,819**.
Outside any Jane Street historical answer range; treat as a curiosity.

## Cross-sum opportunities (134 + phrase-sums)

| Combination | Value | Notes |
|---|---:|---|
| 134 alone | 134 | primary |
| 134 + FIND (52) | 186 | |
| 134 + ADD (123) | 257 | |
| 134 + STEP (25) | 159 | |
| 134 + DATE (89) | 223 | |
| 134 + LAST (80) | 214 | |
| 134 + all-5 phrase sums (369) | 503 | |
| 134 + 26 (row-14 visual) | 160 | |
| 134 + 9 (IX Roman) | 143 | |
| 134 × 2 | 268 | |
| 134 + 2026 | **2160** | primary year-shift |

None of these composite readings is as clean as standalone 134; all require a
second choice of operator ("then add which phrase?") that is not grid-forced.

Next: `numbers_04_derivatives_and_trivia.md` — year-shifts, atomic-number
sums, hex-word readings, and external trivia.
