from difflib import SequenceMatcher


class Score:
    def __init__(self):
        self.best_ratio = 0
        self.best_offset = None
        self.cur_ratio = 0
        self.sm = SequenceMatcher()


    def calculate(self, src_line, trg_line):
        self.sm.set_seqs(src_line, trg_line)
        self.cur_ratio = self.sm.ratio()


    def needs_update(self):
        return self.cur_ratio > self.best_ratio and self.cur_ratio > 0.85


    def update(self, best_idx):
        self.best_ratio = self.cur_ratio
        self.best_offset = best_idx


    def meets_threshold(self):
        return self.best_ratio > 0.85


    def get_best_offset(self):
        return self.best_offset
