class BowlingGame:
    total_score = 0
    frames = []
    current_frame = []

    def roll(self, pins):
        if (pins == 10) and (len(self.current_frame) == 0):
            self.frames.append([10])
        else:
            self.current_frame.append(pins)
        if len(self.current_frame) == 2:
            self.frames.append(self.current_frame)
            self.current_frame = []

    def score(self):
        for i, frame in enumerate(self.frames):
            if frame[0] != 10:
                self.total_score += sum(frame)
                if sum(frame) == 10:
                    self.total_score += self.frames[i + 1][0]
            else:
                self.total_score += 10
                self.total_score += sum(self.frames[i+1])
        return self.total_score
