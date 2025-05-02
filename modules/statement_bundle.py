from modules.engine import Engine
from modules.statement import Statement


class StatementBundle:
    def __init__(self, src_file, trg_file):
        self.src_file = src_file.strip().splitlines()
        self.trg_file = trg_file.strip().splitlines()
        self.engine = Engine()


    def produce_statements(self):
        statements = list()

        for lexeme in self.engine.produce_lexemes(self.src_file, self.trg_file):
            print(f"{lexeme.polarity} :: {lexeme.index:>2} :: {lexeme.item:<28} :: {lexeme.hint}")
            token = lexeme.generate_token()
            statement = Statement(token)
            statements.append(statement)

        return statements
