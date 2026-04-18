"""King-path DFS with cell-reuse prohibition.

A 'king path' moves to any of 8 neighbors per step (Chebyshev distance 1).
A path may not reuse a cell. find_phrase(s) returns every distinct
coordinate-path whose letters spell s (hyphen is skipped as a non-letter).
"""

from grid import N, get
from solver import king_neighbors


def find_phrase(phrase, max_results=None):
    """Return every distinct coordinate path that spells `phrase` as a king-walk
    without cell reuse. Phrase is matched case-insensitively against letter cells.
    """
    phrase = phrase.lower().replace(" ", "")
    if not phrase:
        return []
    results = []

    def dfs(path, visited):
        if max_results is not None and len(results) >= max_results:
            return
        idx = len(path)
        if idx == len(phrase):
            results.append(tuple(path))
            return
        target = phrase[idx]
        if idx == 0:
            cells = [(r, c) for r in range(1, N + 1) for c in range(1, N + 1) if get(r, c) == target]
        else:
            r, c = path[-1]
            cells = [(nr, nc) for nr, nc in king_neighbors(r, c) if get(nr, nc) == target]
        for cell in cells:
            if cell in visited:
                continue
            if max_results is not None and len(results) >= max_results:
                return
            path.append(cell)
            visited.add(cell)
            dfs(path, visited)
            visited.discard(cell)
            path.pop()

    dfs([], set())
    return results


def count_phrase(phrase, max_results=None):
    return len(find_phrase(phrase, max_results=max_results))


def exists_phrase(phrase):
    return bool(find_phrase(phrase, max_results=1))
