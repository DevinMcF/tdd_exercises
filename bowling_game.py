class BowlingGame:
    def __init__(self):
        # pkd = pins knocked down
        self.pkd = 0

    def roll(self, pins):
        self.pkd += pins
        pass

    def score(self):
        return self.pkd
