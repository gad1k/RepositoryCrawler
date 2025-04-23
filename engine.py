import difflib


file_1 = """
  col_01 varchar(10),
  col_02 varchar(10),
  col_03 varchar(10),
  col_04 varchar(10),
  col_05 varchar(10),
  col_06 varchar(10),
  col_07 varchar(10),
  col_08 varchar(10),
  col_09 varchar(10),
"""

file_2 = """
  col_01 varchar(10),
  col_02 varchar(10),
  col_08 varchar(10),
  col_03 varchar(15),
  col_07 varchar(10),
  col_44 varchar(10),
  col_05 varchar(10),
  col_06 varchar(10),
  col_09 varchar(10),
"""


def show_diff_with_line_numbers(text1, text2, file1_name="file_1.sql", file2_name="file_2.sql"):
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


show_diff_with_line_numbers(file_1, file_2)
