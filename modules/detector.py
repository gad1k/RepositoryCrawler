from modules.distance import Distance
from modules.score import Score
from modules.movement_bundle import MovementBundle


class Detector:
    def __init__(self, src_block, trg_block):
        self.src_block = src_block
        self.trg_block = trg_block


    def find_movements(self, src_idx, trg_idx):
        movements = MovementBundle()

        for src_offset, src_line in enumerate(self.src_block):
            score = Score()
            for trg_offset, trg_line in enumerate(self.trg_block):
                if movements.is_involved(trg_offset):
                    continue
                distance = Distance(src_idx + src_offset, trg_idx + trg_offset)
                score.calculate(src_line, trg_line)
                if distance.meets_threshold() and score.needs_update():
                    score.update(trg_offset)
            if score.meets_threshold():
                movements.add({src_offset: score.get_best_idx()})

        return movements
