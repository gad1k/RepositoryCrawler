class Distance:
    def __init__(self, src_idx, trg_idx):
        self.src_idx = src_idx
        self.trg_idx = trg_idx


    def meets_threshold(self):
        return abs(self.src_idx - self.trg_idx) <= 2
