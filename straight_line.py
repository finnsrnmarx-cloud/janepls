"""Straight-line (8-direction, no turns) word occurrences in the grid.

Used for identifying elemental symbols and long words (ALUMINUM, TIN, OPENER)
that the reports claim appear on a single straight vector.
"""

from grid import N, get

DIRECTIONS = [
    (0, 1), (0, -1),
    (1, 0), (-1, 0),
    (1, 1), (1, -1), (-1, 1), (-1, -1),
]


def find_straight(word):
    """Return list of (start_cell, direction, end_cell) tuples for every
    straight-line occurrence of `word`. Case-insensitive."""
    word = word.lower()
    results = []
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if get(r, c) != word[0]:
                continue
            for dr, dc in DIRECTIONS:
                end_r = r + dr * (len(word) - 1)
                end_c = c + dc * (len(word) - 1)
                if not (1 <= end_r <= N and 1 <= end_c <= N):
                    continue
                ok = True
                for k in range(len(word)):
                    nr, nc = r + dr * k, c + dc * k
                    if get(nr, nc) != word[k]:
                        ok = False
                        break
                if ok:
                    results.append(((r, c), (dr, dc), (end_r, end_c)))
    return results


def exists_straight(word):
    return bool(find_straight(word))
