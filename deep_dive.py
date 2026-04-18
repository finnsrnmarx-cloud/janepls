"""Exhaustive deep-dive: every step-k flat progression for k in 2..12 and every offset."""
from solver import hex_sum, step_by_six, step_by_six_cells
from grid import flat, get, N, rc_to_flat

ANCHORS = {
    (1, 1): "TL",
    (1, 5): "F-of-FIND",
    (1, 11): "S-of-START",
    (2, 8): "ADD-start",
    (3, 6): "ADD-start-alt",
    (9, 14): "STEP-start",
    (14, 8): "hyphen",
    (14, 14): "STEP-terminal",
    (10, 2): "LAST-start",
    (12, 13): "LAST-terminal",
    (3, 3): "DATE-start",
    (5, 13): "DATE-terminal-a",
    (5, 14): "DATE-terminal-b",
    (11, 1): "ADD-terminal",
    (1, 14): "FIND-terminal",
}


def path_step_k_offset(step, offset, limit=196):
    return [i for i in range(offset, limit + 1, step)]


def path_cells(step, offset):
    return [flat(i) for i in path_step_k_offset(step, offset)]


def anchor_hits(cells):
    return [(c, ANCHORS[c]) for c in cells if c in ANCHORS]


print(f"{'k':>3} {'off':>4} {'n':>4} {'hexsum':>7}  anchors")
results = []
for k in range(2, 13):
    for off in range(1, k + 1):
        cells = path_cells(k, off)
        if not cells:
            continue
        s = hex_sum(cells)
        hits = anchor_hits(cells)
        results.append((k, off, len(cells), s, hits))

# Rank by anchor-coverage then by size
results.sort(key=lambda r: (-len(r[4]), r[0], r[1]))

# Print top 40 by anchor-coverage
print("\n-- TOP 40 BY ANCHOR COUNT --")
for k, off, n, s, hits in results[:40]:
    names = ",".join(name for _, name in hits)
    print(f"{k:>3} {off:>4} {n:>4} {s:>7}  {names}")

# Find all candidates with >= 3 anchors
print("\n-- ALL WITH >=3 ANCHORS --")
for k, off, n, s, hits in results:
    if len(hits) < 3:
        break
    names = ",".join(name for _, name in hits)
    print(f"k={k} off={off} n={n} sum={s}  [{names}]")
