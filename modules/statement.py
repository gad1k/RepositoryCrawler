class Statement:
    def __init__(self, token):
        self.polarity = token["polarity"]
        self.index = token["index"]
        self.name = token["name"]
        self.type = token["type"]
        self.constraint = token["constraint"]
