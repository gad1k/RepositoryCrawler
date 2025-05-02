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
