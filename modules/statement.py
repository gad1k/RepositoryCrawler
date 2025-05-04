class Statement:
    def __init__(self, token):
        self.polarity = token["polarity"]
        self.index = token["index"]
        self.name = token["name"]
        self.type = token["type"]
        self.constraint = token["constraint"]
        self.hint = token["hint"]


    def __str__(self):
        return f"{self.polarity} :: {self.index:>2} :: {self.name:<6} :: " \
               f"{self.type:<11} :: {str(self.constraint):<8} :: {self.hint}"


    def get_vector(self, statement):
        vector = str(int(self.polarity != statement.polarity)) + \
                 str(int(self.index == statement.index)) + \
                 str(int(self.name == statement.name)) + \
                 str(int(self.type == statement.type)) + \
                 str(int(self.constraint == statement.constraint)) + \
                 str(int(self.tune_none_behavior(self.hint, statement.hint)))

        return vector


    def tune_none_behavior(self, a, b):
        if a is None and b is None:
            return False
        else:
            return a == b