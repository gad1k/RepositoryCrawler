class MovementBundle:
    def __init__(self):
        self.movements = dict()


    def add(self, movement):
        self.movements.update(movement)


    def get(self, src_offset):
        return self.movements.get(src_offset)


    def is_involved(self, trg_offset):
        return trg_offset in self.movements.values()
