from modules.engine import Engine
from modules.statement import Statement


class FileDiff:
    def __init__(self, file_src, file_trg):
        self.file_src = file_src
        self.file_trg = file_trg
        self.scripts = list()
        self.engine = Engine()


    def extract_statements(self):
        src = self.file_src.strip().splitlines()
        trg = self.file_trg.strip().splitlines()

        lexemes = self.engine.analyze(src, trg)
        for lexeme in lexemes:
            token = lexeme.generate_token()
            statement = Statement(token)

        return lexemes
