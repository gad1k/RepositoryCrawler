import re

from modules.constant import Polarity
from modules.context import Context


class Lexeme:
    def __init__(self, polarity, index, item, hint):
        self.polarity = polarity
        self.index = index
        self.item = item
        self.hint = hint
        self.ctx = Context()


    def generate_token(self):
        match = re.search(self.ctx.lexeme_pattern(), self.item, re.IGNORECASE)

        m1 = match.group(1)
        m2 = match.group(3)
        m5 = match.group(6)

        token = {
            "polarity": self.polarity,
            "index": self.index,
            "name": m1,
            "type": re.sub(self.ctx.space_pattern(), "", m2.strip()),
            "constraint": re.sub(self.ctx.space_pattern(), " ", m5.upper().strip()) if m5 else None,
            "hint": self.hint
        }

        return token


class SourceLexeme(Lexeme):
    def __init__(self, idx, item, hint=None):
        super().__init__(Polarity.NEGATIVE.value, idx, item.strip().rstrip(","), hint)


class TargetLexeme(Lexeme):
    def __init__(self, idx, item, hint=None):
        super().__init__(Polarity.POSITIVE.value, idx, item.strip().rstrip(","), hint)
