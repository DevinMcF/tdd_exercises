from unittest import TestCase
from bowling_game import BowlingGame


class TestBlowingGame(TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def roll_many(self, num_rolls, pins):
        for roll in range(num_rolls):
            self.game.roll(pins)

    def test_gutter_game(self):
        for roll in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    def test_all_ones_game(self):
        for roll in range(20):
            self.game.roll(1)
        self.assertEqual(self.game.score(), 20)

    def test_mixed_rolls(self):
        for roll in range(10):
            self.game.roll(2)
        for roll in range(10):
            self.game.roll(4)
        self.assertEqual(self.game.score(), 60)

    def test_one_spare(self):
        self.game.roll(7)
        self.game.roll(3)  # A Spare
        self.roll_many(18, 1)
        self.assertEqual(self.game.score(), 29)
