class BowlingGame:
    # pkd = pins knocked down
    pkd = 0

    def roll(self, pins):
        self.pkd += pins

    def score(self):
        return self.pkd
