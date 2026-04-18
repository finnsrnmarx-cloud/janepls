"""Canonical transcription of the Jane Street 'Can U Dig It?' (April 2026) grid.

The grid is 14x14. Rows and columns are 1-indexed externally but stored
0-indexed internally. The single non-letter cell is the hyphen at (14, 8).
"""

ROWS = [
    "rsdifindthsart",
    "ehresodaeetgna",
    "netrhalxhgowip",
    "egedauyueaenrp",
    "ptnnmllmxidnee",
    "ohuinkthanacsm",
    "alnpfyldebsttn",
    "uumjarebemehrw",
    "mithdceigiugts",
    "tlamibftoteget",
    "sailniitniapen",
    "nstoagrniiobrt",
    "ietiryeesprayw",
    "tunenty-tessix",
]

N = 14
HEX = set("abcdef")
HEX_VALUES = {ch: 10 + i for i, ch in enumerate("abcdef")}


def get(r, c):
    """1-indexed cell access. Returns the character at row r, column c."""
    return ROWS[r - 1][c - 1]


def flat(i):
    """1-indexed flat (row-major) access. flat(1) = (1,1), flat(15) = (2,1)."""
    r = (i - 1) // N + 1
    c = (i - 1) % N + 1
    return r, c


def flat_char(i):
    r, c = flat(i)
    return get(r, c)


def rc_to_flat(r, c):
    """Inverse of flat()."""
    return (r - 1) * N + c


def hex_value(ch):
    """Base-16 digit value for a-f; 0 for anything else (including hyphen)."""
    return HEX_VALUES.get(ch, 0)


def all_cells():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            yield r, c


def letter_count():
    """Count non-hyphen alphabetical cells."""
    return sum(1 for r, c in all_cells() if get(r, c).isalpha())


def char_frequencies():
    from collections import Counter
    return Counter(ch for r, c in all_cells() for ch in [get(r, c)])
