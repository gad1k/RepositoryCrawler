from difflib import SequenceMatcher
from modules.constant import Tag
from modules.context import Context
from modules.detector import Detector
from modules.hint import Hint
from modules.lexeme import SourceLexeme, TargetLexeme


class Engine:
    def __init__(self):
        self.sm = SequenceMatcher()
        self.ctx = Context()


    def produce_lexemes(self, src, trg):
        self.sm.set_seqs(src, trg)

        lexemes = list()
        for tag, slo, shi, tlo, thi in self.sm.get_opcodes():
            if tag == Tag.EQUAL:
                continue
            elif tag == Tag.REPLACE:
                detector = Detector(src[slo:shi], trg[tlo:thi])
                movements = detector.find_movements(slo, tlo)
                for src_idx, src_line in enumerate(src[slo:shi]):
                    trg_idx = movements.get(src_idx)
                    if trg_idx is not None:
                        hint = Hint(slo + src_idx, tlo + trg_idx)
                        lexemes.append(SourceLexeme(slo + src_idx + 1, src_line, hint.render()))
                        lexemes.append(TargetLexeme(tlo + trg_idx + 1, trg[tlo:thi][trg_idx], hint.render()))
                    else:
                        lexemes.append(SourceLexeme(slo + src_idx + 1, src_line))
                for trg_idx, trg_line in enumerate(trg[tlo:thi]):
                    if not movements.is_involved(trg_idx):
                        lexemes.append(TargetLexeme(tlo + trg_idx + 1, trg_line))
            elif tag == Tag.DELETE:
                for idx, line in enumerate(src[slo:shi]):
                    lexemes.append(SourceLexeme(slo + idx + 1, line))
            elif tag == Tag.INSERT:
                for idx, line in enumerate(trg[tlo:thi]):
                    lexemes.append(TargetLexeme(tlo + idx + 1, line))

        return lexemes
