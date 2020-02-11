class BowlingGame:
    total_score = 0
    frames = []
    current_frame = []

    def roll(self, pins):
        if pins != 10:
            self.current_frame.append(pins)
        else:
            self.frames.append([10])
        if len(self.current_frame) == 2:
            self.frames.append(self.current_frame)
            self.current_frame = []

    def score(self):
        for i, frame in enumerate(self.frames):
            self.total_score += sum(self.frames[i])
            if sum(frame) == 10:
                self.total_score += self.frames[i + 1][0]
        return self.total_score

