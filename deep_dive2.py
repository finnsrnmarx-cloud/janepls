"""Phase 2 deep-dive: phrase-path hex sums, concatenation candidates, row/col
stride variants, and all 'nice' small number derivations."""
from solver import hex_sum, step_by_six, step_by_six_cells, row_hex, col_hex
from paths import find_phrase
from grid import get, flat, rc_to_flat, N


def phrase_info():
    phrases = [
        "FIND THE START",
        "ADD THE HEXADECIMALS",
        "STEP BY SIX",
        "THERE IS A DATE ON WIRE",
        "LAST ENTRY ENTIRE INTEGER",
    ]
    print("-- phrase king-path details --")
    for p in phrases:
        paths = find_phrase(p)
        print(f"\n{p}  letters={len(p.replace(' ', ''))}  paths={len(paths)}")
        for i, path in enumerate(paths):
            s = hex_sum(path)
            print(f"  path {i}: hex sum = {s}, start={path[0]} end={path[-1]}")


def offset4_concat():
    cells = step_by_six_cells(4)
    letters = [get(r, c) for r, c in cells]
    hex_only = [ch for ch in letters if ch in "abcdef"]
    print("\n-- offset-4 path hex letters (12 total) --")
    print("letters:", "".join(hex_only))
    print("decimal via concatenation:", int("".join(hex_only), 16))
    # alt: keep positional 0 for non-hex
    packed = "".join(ch if ch in "abcdef" else "0" for ch in letters)
    print(f"full 33-char zero-packed: {packed!r}")
    print(f"as hex number: {int(packed, 16)}")


def all_step6_sums():
    print("\n-- all step-6 offsets (sums sum to total=690) --")
    total = 0
    for off in range(1, 7):
        s = hex_sum(step_by_six_cells(off))
        total += s
        print(f"  offset {off}: sum={s}")
    print(f"  total: {total}")


def row_stride_variants():
    print("\n-- row stride-6 variants --")
    for start in range(1, 7):
        rows = list(range(start, 15, 6))
        s = sum(row_hex(r) for r in rows)
        print(f"  rows starting {start}: {rows}, hex sum = {s}")


def col_stride_variants():
    print("\n-- column stride-6 variants --")
    for start in range(1, 7):
        cols = list(range(start, 15, 6))
        s = sum(col_hex(c) for c in cols)
        print(f"  cols starting {start}: {cols}, hex sum = {s}")


def axiom_letter_counts():
    phrases = [
        "FIND THE START",
        "ADD THE HEXADECIMALS",
        "STEP BY SIX",
        "THERE IS A DATE ON WIRE",
        "LAST ENTRY ENTIRE INTEGER",
    ]
    lens = [len(p.replace(" ", "")) for p in phrases]
    print(f"\n-- axiom letter counts (no spaces) --  sum={sum(lens)}  list={lens}")


def offset4_anchors_explicit():
    cells = step_by_six_cells(4)
    anchors = {
        (1, 5): "F-of-FIND",
        (1, 11): "S-of-START",
        (2, 8): "ADD-start",
        (3, 6): "ADD-start-alt",
        (5, 13): "DATE-term-a",
        (5, 14): "DATE-term-b",
        (9, 14): "STEP-start",
        (10, 2): "LAST-start",
        (11, 1): "ADD-term",
        (12, 13): "LAST-term",
        (14, 8): "hyphen",
        (14, 14): "STEP-term",
    }
    print("\n-- offset-4 full cell-by-cell with anchor markers --")
    total = 0
    for i, (r, c) in enumerate(cells, 1):
        ch = get(r, c)
        flat_i = rc_to_flat(r, c)
        tag = anchors.get((r, c), "")
        from grid import hex_value
        v = hex_value(ch)
        total += v
        mark = " <==" if tag else ""
        print(f"  pos{flat_i:>3}  ({r:>2},{c:>2}) {ch!r}  val={v:>2}  running={total:>3}  {tag}{mark}")


phrase_info()
all_step6_sums()
offset4_concat()
offset4_anchors_explicit()
row_stride_variants()
col_stride_variants()
axiom_letter_counts()
