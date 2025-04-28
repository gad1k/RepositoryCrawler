class Context:
    def lexeme_pattern(self):
        return r"^\s*(\w+)\s+(((\w+)\s*(\(\d+\))?)(\s*(not)?\s+(null)?)?)"


    def space_pattern(self):
        return r"\s+"
