class Context:
    def __init__(self):
        pass


    def statement_pattern(self):
        return "^\s*(\w+)\s+((\w+)\s*(\(\d+\))?)(\s*(not)?\s+(null)?)?"


    def column_pattern(self):
        return r"\s+"
