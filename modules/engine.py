import re

from difflib import SequenceMatcher
from modules.constant import Tag
from modules.context import Context
from modules.lexeme import SourceLexeme, TargetLexeme


class Engine:
    def __init__(self):
        self.matcher = SequenceMatcher()
        self.estimator = SequenceMatcher()
        self.ctx = Context()


    def run(self, src, trg):
        self.matcher.set_seqs(src, trg)

        lexemes = list()
        for tag, slo, shi, tlo, thi in self.matcher.get_opcodes():
            if tag == Tag.EQUAL:
                continue

            elif tag == Tag.REPLACE:
                moved_trg_indexes = set()
                for src_idx, src_line in enumerate(src[slo:shi]):
                    best_score = 0
                    best_trg_idx = None
                    src_signature = self.extract_signature(src_line)
                    for trg_idx, trg_line in enumerate(trg[tlo:thi]):
                        if trg_idx in moved_trg_indexes:
                            continue
                        trg_signature = self.extract_signature(trg_line)
                        score = self.calculate_score(src_signature, trg_signature)
                        distance = abs((slo + src_idx) - (tlo + trg_idx))
                        if distance <= 2 and score > best_score and score >= 0.9:
                            best_score = score
                            best_trg_idx = trg_idx
                    if best_score > 0.9:
                        moved_trg_indexes.add(best_trg_idx)
                        sno = slo + src_idx + 1
                        tno = tlo + best_trg_idx + 1
                        hint = f"moved from line {sno} to {tno}"
                        lexemes.append(SourceLexeme(sno, src_line, hint))
                        lexemes.append(TargetLexeme(tno, trg[tlo + best_trg_idx], hint))
                    else:
                        lexemes.append(SourceLexeme(slo + src_idx + 1, src_line))
                for idx, line in enumerate(trg[tlo:thi]):
                    if idx not in moved_trg_indexes:
                        lexemes.append(TargetLexeme(tlo + idx + 1, line))

            elif tag == Tag.DELETE:
                for idx, line in enumerate(src[slo:shi]):
                    lexemes.append(SourceLexeme(slo + idx + 1, line))

            elif tag == Tag.INSERT:
                for idx, line in enumerate(trg[tlo:thi]):
                    lexemes.append(TargetLexeme(tlo + idx + 1, line))

        return lexemes


    def calculate_score(self, src, trg):
        self.estimator.set_seqs(src, trg)
        return self.estimator.ratio()


    def extract_signature(self, line):
        match = re.match(self.ctx.lexeme_pattern(), line.strip().rstrip(','))
        return match.group(2).strip() if match else ""
