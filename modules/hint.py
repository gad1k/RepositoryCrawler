class Hint:
    def __init__(self, src_line_no, trg_line_no):
        self.src_line_no = src_line_no + 1
        self.trg_line_no = trg_line_no + 1


    def render(self):
        return f"moved from line {self.src_line_no} to {self.trg_line_no}"
