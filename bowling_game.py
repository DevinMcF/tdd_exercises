class BowlingGame:
    def __init__(self):
        self.pins = 0

    def roll(self, pins):
        self.pins += pins
        pass

    def score(self):
        return self.pins