"""Element-symbol tracing in the grid.

Reports variously claim Al, Sn, Au, V, Pd, Ba, Ac, Ho, Ar, Fe, Ne, Dy are
traceable. This module checks each as a straight line and as a king path and
reports which exist. Also checks the full element-name spellings (ALUMINUM, TIN,
GOLD, etc.) for presence as king paths and straight lines.
"""

from paths import exists_phrase, find_phrase, count_phrase
from straight_line import find_straight, exists_straight


# (symbol, atomic number, full name)
ELEMENTS = [
    ("Al", 13, "aluminum"),
    ("Sn", 50, "tin"),
    ("Au", 79, "gold"),
    ("V", 23, "vanadium"),
    ("Pd", 46, "palladium"),
    ("Ba", 56, "barium"),
    ("Ac", 89, "actinium"),
    ("Ho", 67, "holmium"),
    ("Ar", 18, "argon"),
    ("Fe", 26, "iron"),
    ("Ne", 10, "neon"),
    ("Dy", 66, "dysprosium"),
]


def report_elements():
    rows = []
    for sym, z, name in ELEMENTS:
        sym_lc = sym.lower()
        sym_straight = find_straight(sym_lc)
        sym_king_exists = exists_phrase(sym_lc)
        name_straight = find_straight(name)
        name_king_count = count_phrase(name, max_results=1)
        rows.append({
            "symbol": sym,
            "z": z,
            "name": name,
            "symbol_straight_n": len(sym_straight),
            "symbol_king_ok": sym_king_exists,
            "name_straight_n": len(name_straight),
            "name_king_ok": bool(name_king_count),
        })
    return rows


if __name__ == "__main__":
    rows = report_elements()
    print(f"{'Sym':4}{'Z':>4}  {'Name':12} sym_straight  sym_king  name_straight  name_king")
    for r in rows:
        print(f"{r['symbol']:4}{r['z']:>4}  {r['name']:12} "
              f"{r['symbol_straight_n']:>12}  {r['symbol_king_ok']!s:>8}  "
              f"{r['name_straight_n']:>13}  {r['name_king_ok']!s:>9}")
