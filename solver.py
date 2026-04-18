"""Primitive hex-sum solvers for arbitrary cell sets, rows, columns, diagonals,
and step-by-6 flat arithmetic progressions.

All coordinates are 1-indexed. Hex digits are a-f (10..15); all other
characters (including the hyphen) contribute 0.
"""

from grid import N, get, flat, hex_value


def hex_sum(cells):
    """Sum hex-digit values over a set/list of (r,c) cells."""
    return sum(hex_value(get(r, c)) for r, c in cells)


def hex_letters(cells):
    """Return (letter, value) tuples for hex cells in the given cell list (order preserved)."""
    out = []
    for r, c in cells:
        ch = get(r, c)
        if ch in "abcdef":
            out.append((ch, hex_value(ch)))
    return out


def row_cells(r):
    return [(r, c) for c in range(1, N + 1)]


def col_cells(c):
    return [(r, c) for r in range(1, N + 1)]


def row_hex(r):
    return hex_sum(row_cells(r))


def col_hex(c):
    return hex_sum(col_cells(c))


def perimeter_cells():
    cells = []
    for c in range(1, N + 1):
        cells.append((1, c))
        cells.append((N, c))
    for r in range(2, N):
        cells.append((r, 1))
        cells.append((r, N))
    return cells


def interior_cells():
    return [(r, c) for r in range(2, N) for c in range(2, N)]


def step_by_six(offset, total=None):
    """Return 1-indexed flat positions offset, offset+6, offset+12, ... up to
    the grid (196 cells). If total is given, limit the sequence to that many terms."""
    if total is None:
        total = 196
    return [i for i in range(offset, total + 1, 6)]


def step_by_six_cells(offset):
    """Return the (r,c) cells along the step-by-6 flat progression starting at offset."""
    return [flat(i) for i in step_by_six(offset)]


def diag_main_cells(r0, c0):
    """Cells along the main-diagonal (down-right) ray starting at (r0, c0) until the grid edge."""
    cells = []
    r, c = r0, c0
    while 1 <= r <= N and 1 <= c <= N:
        cells.append((r, c))
        r += 1
        c += 1
    return cells


def diag_anti_cells(r0, c0):
    """Cells along the anti-diagonal (down-left) ray starting at (r0, c0)."""
    cells = []
    r, c = r0, c0
    while 1 <= r <= N and 1 <= c <= N:
        cells.append((r, c))
        r += 1
        c -= 1
    return cells


def all_main_diagonals():
    """Every maximal SE diagonal. Order: top-row starts (1,1)..(1,N), then first-col starts (2,1)..(N,1)."""
    return [diag_main_cells(1, c) for c in range(1, N + 1)] + [
        diag_main_cells(r, 1) for r in range(2, N + 1)
    ]


def all_anti_diagonals():
    """Every maximal SW diagonal. Order: top-row starts (1,1)..(1,N), then last-col starts (2,N)..(N,N)."""
    return [diag_anti_cells(1, c) for c in range(1, N + 1)] + [
        diag_anti_cells(r, N) for r in range(2, N + 1)
    ]


def king_neighbors(r, c):
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 1 <= nr <= N and 1 <= nc <= N:
                yield nr, nc
