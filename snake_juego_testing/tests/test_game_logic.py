import unittest
from test_game_logic import GameLogic

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()

    def test_initial_state(self):
        self.assertEqual(self.game.get_score(), 0)
        self.assertEqual(self.game.get_level(), 1)

    def test_score_increase(self):
        score, level = self.game.increase_score()
        self.assertEqual(score, 1)
        self.assertEqual(level, 1)

    def test_level_up(self):
        for _ in range(5):
            self.game.increase_score()
        self.assertEqual(self.game.get_score(), 5)
        self.assertEqual(self.game.get_level(), 2)

    def test_multiple_level_ups(self):
        for _ in range(15):
            self.game.increase_score()
        self.assertEqual(self.game.get_score(), 15)
        self.assertEqual(self.game.get_level(), 4)
