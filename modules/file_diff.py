from modules.script import Add, Alter, Change, Drop, Move, Rename
from modules.statement_bundle import StatementBundle


class FileDiff:
    def __init__(self, src_file, trg_file):
        self.src_file = src_file
        self.trg_file = trg_file
        self.scripts = list()


    def build_scripts(self):
        statement_bundle = StatementBundle(self.src_file, self.trg_file)
        statements = statement_bundle.produce_statements()

        for statement in statements:
            print(statement)

        # while len(statements) != 0:
        #     statement = statements.pop(0)
        #
        #     for idx, stmt in enumerate(statements):
        #         vector = statement.get_vector(stmt)
        #         if vector == "Alter":
        #             script = Alter()
        #             statements.pop(idx)
        #             break
        #         elif vector == "Change":
        #             script = Change()
        #             statements.pop(idx)
        #             break
        #         elif vector == "Move":
        #             script = Move()
        #             statements.pop(idx)
        #             break
        #         elif vector == "Rename":
        #             script = Rename()
        #             statements.pop(idx)
        #             break
        #     else:
        #         if statement.has_positive_polarity():
        #             script = Add()
        #         else:
        #             script = Drop()
        #
        #     self.scripts.append(script)


    def render_scripts(self):
        for script in self.scripts:
            script.generate()

