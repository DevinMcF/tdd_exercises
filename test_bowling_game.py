from unittest import TestCase
from bowling_game import BowlingGame


class TestBlowingGame(TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def test_gutter_game(self):
        for roll in range(20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)
