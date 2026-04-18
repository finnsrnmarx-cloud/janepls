"""Sanity tests that the grid transcription and primitive solvers are correct.
Run as: python tests.py
"""

from collections import Counter

from grid import N, ROWS, get, flat, rc_to_flat, hex_value, letter_count, char_frequencies
from solver import (
    row_hex, col_hex, hex_sum, row_cells, col_cells, perimeter_cells,
    interior_cells, step_by_six, step_by_six_cells, diag_main_cells,
    diag_anti_cells, king_neighbors, hex_letters,
)

def ok(cond, msg):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {msg}")
    if not cond:
        raise SystemExit(1)


# Dimensions
ok(len(ROWS) == 14, "14 rows")
ok(all(len(r) == 14 for r in ROWS), "14 columns in every row")

# Hyphen is the only non-letter, at (14,8)
non_letters = [(r, c) for r in range(1, 15) for c in range(1, 15) if not get(r, c).isalpha()]
ok(non_letters == [(14, 8)], f"hyphen only at (14,8); got {non_letters}")
ok(get(14, 8) == "-", "cell (14,8) is hyphen")

# Letter count
ok(letter_count() == 195, f"195 letter cells; got {letter_count()}")

# Missing letters (Q, V, Z absent; J, K exactly once)
freq = char_frequencies()
ok(freq.get("q", 0) == 0, "Q absent")
ok(freq.get("v", 0) == 0, "V absent")
ok(freq.get("z", 0) == 0, "Z absent")
ok(freq.get("j", 0) == 1, f"J once; got {freq.get('j')}")
ok(freq.get("k", 0) == 1, f"K once; got {freq.get('k')}")

# Flat indexing
ok(flat(1) == (1, 1), "flat(1) = (1,1)")
ok(flat(14) == (1, 14), "flat(14) = (1,14)")
ok(flat(15) == (2, 1), "flat(15) = (2,1)")
ok(flat(196) == (14, 14), "flat(196) = (14,14)")
ok(rc_to_flat(14, 14) == 196, "rc_to_flat(14,14) = 196")
ok(rc_to_flat(2, 8) == 22, "rc_to_flat(2,8) = 22")
ok(rc_to_flat(14, 8) == 190, "rc_to_flat(14,8) = 190")

# Hex values
ok(hex_value("a") == 10 and hex_value("f") == 15, "a=10, f=15")
ok(hex_value("g") == 0, "g contributes 0")
ok(hex_value("-") == 0, "hyphen contributes 0")

# Known row/col sums (consensus across reports)
ok(row_hex(1) == 51, f"row 1 hex = 51; got {row_hex(1)}")
ok(row_hex(2) == 89, f"row 2 hex = 89; got {row_hex(2)}")
ok(row_hex(4) == 89, f"row 4 hex = 89; got {row_hex(4)}")
ok(row_hex(7) == 63, f"row 7 hex = 63; got {row_hex(7)}")
ok(row_hex(6) == 32, f"row 6 hex = 32; got {row_hex(6)}")

# Step-by-6 flat positions
s4 = step_by_six(4)
ok(s4[0] == 4 and s4[-1] == 196 and len(s4) == 33, f"step-6 offset-4: 33 terms, last 196; got {len(s4)} ending {s4[-1]}")
ok(22 in s4 and 190 in s4 and 196 in s4, "step-6 offset-4 threads 22, 190, 196")

# Perimeter + interior = total
total_hex = sum(row_hex(r) for r in range(1, 15))
peri = hex_sum(perimeter_cells())
inter = hex_sum(interior_cells())
ok(peri + inter == total_hex, f"perimeter + interior == total ({peri} + {inter} = {total_hex})")

print()
print(f"total hex sum = {total_hex}")
print(f"perimeter hex sum = {peri}")
print(f"interior hex sum = {inter}")
print("all primitive tests passed")
