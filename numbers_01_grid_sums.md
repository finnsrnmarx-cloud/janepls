# Numbers, part 1 — grid sums

Every number derivable from whole-grid structure: row sums, column sums,
perimeter, interior, total. Hex-digit values only (a=10…f=15, other letters
and the hyphen contribute 0). All values computed by `solver.py`.

## Row hex sums (14 values)

| Row | Sum | Notes |
|---:|---:|---|
| 1 | **51** | d(13)+f(15)+d(13)+a(10) |
| 2 | **89** | 7 hex letters; matches row 4; also Actinium Ac |
| 3 | 24 | lowest hex count in top half |
| 4 | **89** | coincidence with row 2; two independent Ac matches |
| 5 | 41 | |
| 6 | **32** | contains the K singleton at (6,6) |
| 7 | **63** | hex letters a,f,d,e,b sum = 63 |
| 8 | **63** | contains the J singleton at (8,4); hex letters a,e,b,e,e,e |
| 9 | 39 | |
| 10 | 64 | |
| 11 | 34 | |
| 12 | 21 | low-hex row |
| 13 | **52** | coincides with FIND THE START path hex sum (also 52) |
| 14 | **28** | "tunenty-tessix" — only e's contribute |

Row-group sums:
- Rows 1,7,13 = 51 + 63 + 52 = **166** (ChatGPT's row-stride-6 base)
- Rows 2,8,14 = 89 + 63 + 28 = **180** (alternate row-stride-6)
- Rows 1–5 = 51 + 89 + 24 + 89 + 41 = **294** (Claude's "discovery zone")

## Column hex sums (14 values)

| Col | Sum | Notes |
|---:|---:|---|
| 1 | **38** | |
| 2 | 38 | |
| 3 | 37 | |
| 4 | 41 | |
| 5 | **73** | |
| 6 | **33** | (a+c+b) — uniquely equals 33 among columns; "VANADIUM" decimal sum |
| 7 | **70** | highest individual column |
| 8 | **61** | column of the hyphen |
| 9 | 66 | equals Dysprosium Dy |
| 10 | 49 | |
| 11 | **75** | |
| 12 | 43 | |
| 13 | **42** | |
| 14 | 24 | |

Column-group sums:
- Cols 1,7,13 = 38 + 70 + 42 = **150** (column analog of rows 1,7,13)
- Cols 2,8,14 = 38 + 61 + 24 = **123** (equals ADD THE HEXADECIMALS path sum — notable)
- Cols 5,11 = 73 + 75 = **148** (ChatGPT's F-of-FIND column-stride)

## Perimeter / interior / total

| Partition | Sum | Notes |
|---|---:|---|
| Perimeter (52 border cells) | **141** | "Can Opener" outer shell |
| Interior (144 inner cells) | **549** | inner pulp |
| Whole grid (196 cells) | **690** | 141 + 549 |

Row + column cross-check: sum of 14 row sums = sum of 14 column sums = 690.

## Cross-coincidences worth noting

- Row 2 hex = Row 4 hex = 89. Both paths for THERE IS A DATE ON WIRE also
  produce 89 when you sum along the king-path. Three independent routes to 89.
- Row 13 hex = 52 = FIND THE START king-path hex sum.
- Col 2,8,14 = 123 = ADD THE HEXADECIMALS king-path hex sum.
- Col 6 = 33 uniquely (no other column = 33), and aligns with the "U column
  positions" sum Gemini cites.

Next: `numbers_02_step_paths.md` — every step-k flat progression.
