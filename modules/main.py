from modules.file_diff import FileDiff


with open("../tests/integration/fixtures/simple_scenarios/add_column_null/src_file.sql") as src_file:
    src = src_file.read()

with open("../tests/integration/fixtures/simple_scenarios/add_column_null/trg_file.sql") as trg_file:
    trg = trg_file.read()


file_diff = FileDiff(src, trg)
statements = file_diff.extract_statements()
pass
