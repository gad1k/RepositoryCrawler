from difflib import SequenceMatcher

from modules.constant import Tag
from modules.lexeme import LexemeSource, LexemeTarget
from modules.statement import Statement


class FileDiff:
    def __init__(self, file_src, file_trg):
        self.file_src = file_src
        self.file_trg = file_trg
        self.sm = SequenceMatcher()


    def extract(self):
        src = self.file_src.strip().splitlines()
        trg = self.file_trg.strip().splitlines()
        self.sm.set_seqs(src, trg)

        for tag, src_lo, src_hi, trg_lo, trg_hi in self.sm.get_opcodes():
            if tag == Tag.EQUAL:
                continue
            if tag in (Tag.DELETE, Tag.REPLACE):
                for idx, item in enumerate(src[src_lo:src_hi], start=src_lo + 1):
                    lexeme = LexemeSource(idx, item)
            if tag in (Tag.INSERT, Tag.REPLACE):
                for idx, item in enumerate(trg[trg_lo:trg_hi], start=trg_lo + 1):
                    lexeme = LexemeTarget(idx, item)
                    token = lexeme.generate_token()
                    statement = Statement(token)

        pass