from unittest import TestCase
from bowling_game import BowlingGame


class TestBlowingGame(TestCase):
    def setUp(self):
        self.game = BowlingGame()

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
            self.game.roll(5)
        self.assertEqual(self.game.score(), 70)
