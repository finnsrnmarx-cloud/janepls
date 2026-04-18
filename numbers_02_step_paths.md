# Numbers, part 2 — step-k flat progressions

Every arithmetic-progression path over the 196-cell flat (row-major) indexing,
for strides k = 2…12, tabulated by hex sum and anchor coverage. Each cell
that lives at a puzzle-distinguished coordinate is scored.

## Anchor set

Strong anchors (uniquely puzzle-defined cells):
- (1,5) F of FIND THE START — the unique starting cell of FIND
- (1,14) terminal of FIND THE START
- (2,8) start of ADD THE HEXADECIMALS (both of the 4 paths that start here)
- (11,1) terminal of ADD THE HEXADECIMALS
- (9,14) start of STEP BY SIX
- (14,14) terminal of STEP BY SIX
- (3,3) start of THERE IS A DATE ON WIRE
- (5,13) terminal-A of DATE ON WIRE
- (10,2) start of LAST ENTRY ENTIRE INTEGER
- (12,13) terminal of LAST ENTRY ENTIRE INTEGER
- (14,8) the hyphen (literal "wire")

Weaker anchors (semantically significant but not uniquely-defining):
- (1,1) top-left
- (1,11) S of START (internal letter)
- (3,6) alternate start of ADD
- (5,14) DATE terminal-B

## Step-6 (the puzzle's explicitly-named stride), all offsets

| Offset | Start | End | Sum | Strong anchors hit | Weak anchors hit |
|---:|---|---|---:|---|---|
| 1 | (1,1) r | (14,11) s | **124** | (3,3) DATE-start | (1,1) TL |
| 2 | (1,2) s | (14,12) s | **54** | (1,14), (10,2) FIND-term, LAST-start | — |
| 3 | (1,3) d | (14,13) i | **167** | (5,13), (11,1) DATE-term-a, ADD-term | — |
| 4 | (1,4) i | (14,14) x | **134** | **(2,8), (14,8), (14,14)** ADD-start, hyphen, STEP-term | (3,6), (5,14) |
| 5 | (1,5) f | (14,9) t | **110** | **(1,5), (12,13)** F-of-FIND, LAST-term | (1,11) S-of-START |
| 6 | (1,6) i | (14,10) e | **101** | (9,14) STEP-start | — |

The six offsets partition the grid; their sums sum to 690 (total). Offset-4
is uniquely dominant with 3 strong + 2 weak anchors = 5 hits. Offset-5 has 2
strong + 1 weak = 3 hits. Every other offset has ≤2 strong hits.

### Why offset-4 (sum 134) is the load-bearing candidate

It is the only step-6 path that simultaneously:
1. Starts its first contribution at the **ADD HEXADECIMALS start cell** (2,8).
2. Walks through the **hyphen** at (14,8) — the only "wire" cell.
3. Terminates at the **STEP BY SIX terminal** (14,14).

Each of those three cells is a uniquely-anchored instruction landmark. No
other step-6 offset hits more than one strong anchor.

### Why offset-5 (sum 110) is the strongest alternative

- Start cell (1,5) IS the F of FIND THE START — so "FIND THE START" literally
  names the starting position.
- Passes through (1,11) the S of START.
- Passes through (12,13) = LAST ENTRY terminal.
- Does NOT reach the hyphen or (14,14).

Offset-5 is the best candidate if "FIND THE START" determines the origin.
Offset-4 is the best candidate if anchor coincidence is the decision rule.

## Other strides for completeness (k = 2…12)

Showing only the highest-anchor-coverage offset per stride. Full listing is
in `deep_dive.py` output.

| k | best offset | start | sum | strong anchors | rationale |
|---:|---:|---|---:|:---:|---|
| 2 | 2 | (1,2) | 289 | 5 | tiny stride hits lots by density |
| 3 | 1 | (1,1) | 258 | 5 | same |
| 4 | 2 | (1,2) | 170 | 4 | — |
| 5 | 1 | (1,1) | 110 | 6 | hits six strong anchors but start isn't puzzle-defined |
| **6** | **4** | **(1,4)** | **134** | **3** | **puzzle stride** |
| 7 | 1 | (1,1) | 99 | 3 | — |
| 8 | 6 | (1,6) | 95 | 4 | — |
| 9 | 7 | (1,7) | 104 | 1 | — |
| 10 | 1 | (1,1) | 47 | 3 | — |
| 11 | 3 | (1,3) | 37 | 3 | — |
| 12 | 10 | (1,10) | 114 | 3 | — |

Outside of k=6 (the explicit stride), no stride-offset pair dominates as
cleanly as offset-4 does at k=6, because smaller strides collect anchors by
density rather than by design.

## Row-stride-6 variants

| Start row | Rows visited | Hex sum |
|---:|---|---:|
| 1 | 1, 7, 13 | **166** |
| 2 | 2, 8, 14 | **180** |
| 3 | 3, 9 | 63 |
| 4 | 4, 10 | 153 |
| 5 | 5, 11 | 75 |
| 6 | 6, 12 | 53 |

## Column-stride-6 variants

| Start col | Cols visited | Hex sum |
|---:|---|---:|
| 1 | 1, 7, 13 | **150** |
| 2 | 2, 8, 14 | **123** (= ADD HEX king-path sum) |
| 3 | 3, 9 | 103 |
| 4 | 4, 10 | 90 |
| 5 | 5, 11 | **148** |
| 6 | 6, 12 | 76 |

Next: `numbers_03_phrase_and_anchor.md` — phrase king-path hex sums and the
offset-4 cell-by-cell walkthrough.
