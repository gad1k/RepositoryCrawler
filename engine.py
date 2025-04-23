import difflib


with open("tests/integration/fixtures/simple_scenarios/add_column_null/src_file.sql") as src_file:
    src = src_file.read()

with open("tests/integration/fixtures/simple_scenarios/add_column_null/trg_file.sql") as trg_file:
    trg = trg_file.read()


def show_diff_with_line_numbers(text1, text2, file1_name="src_file.sql", file2_name="trg_file.sql"):
    lines1 = text1.strip().splitlines()
    lines2 = text2.strip().splitlines()

    sm = difflib.SequenceMatcher(None, lines1, lines2)

    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        print(f"\n=== {tag.upper()} ===")
        if tag in ("replace", "delete"):
            for idx, line in enumerate(lines1[i1:i2], start=i1 + 1):
                print(f"- {file1_name}:{idx:>3}: {line}")
        if tag in ("replace", "insert"):
            for idx, line in enumerate(lines2[j1:j2], start=j1 + 1):
                print(f"+ {file2_name}:{idx:>3}: {line}")


show_diff_with_line_numbers(src, trg)
