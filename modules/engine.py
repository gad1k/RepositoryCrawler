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
        for tag, i1, i2, j1, j2 in self.matcher.get_opcodes():
            if tag == Tag.EQUAL:
                continue
            elif tag == Tag.REPLACE:
                matched_right = set()
                for idx1, l1 in enumerate(src[i1:i2]):
                    best_score = 0
                    best_idx2 = None
                    sig1 = self.extract_column_signature(l1)
                    for idx2, l2 in enumerate(trg[j1:j2]):
                        if idx2 in matched_right:
                            continue
                        sig2 = self.extract_column_signature(l2)
                        score = self.calculate_score(sig1, sig2)
                        line_distance = abs((i1 + idx1) - (j1 + idx2))
                        if line_distance <= 2 and score > best_score and score >= 0.9:
                            best_score = score
                            best_idx2 = idx2
                    if best_score > 0.9:
                        l_lineno = i1 + idx1 + 1
                        r_lineno = j1 + best_idx2 + 1
                        lexemes.append(SourceLexeme(l_lineno, l1, f"moved from line {l_lineno} to {r_lineno}"))
                        lexemes.append(TargetLexeme(r_lineno, trg[j1 + best_idx2], f"moved from line {l_lineno} to {r_lineno}"))
                        matched_right.add(best_idx2)
                    else:
                        lexemes.append(SourceLexeme(i1 + idx1 + 1, l1, None))
                for idx2, l2 in enumerate(trg[j1:j2]):
                    if idx2 not in matched_right:
                        lexemes.append(TargetLexeme(j1 + idx2 + 1, l2, None))
            elif tag == Tag.DELETE:
                for idx, line in enumerate(src[i1:i2]):
                    lexemes.append(SourceLexeme(i1 + idx + 1, line, None))
            elif tag == Tag.INSERT:
                for idx, line in enumerate(trg[j1:j2]):
                    lexemes.append(TargetLexeme(j1 + idx + 1, line, None))

        return lexemes


    def calculate_score(self, src, trg):
        self.estimator.set_seqs(src, trg)
        return self.estimator.ratio()


    def extract_column_signature(self, line):
        match = re.match(self.ctx.lexeme_pattern(), line.strip().rstrip(','))
        return match.group(2).strip() if match else ""
