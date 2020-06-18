from unittest import TestCase

from week15.cd19 import deck_game, deck_game_dp


class Test(TestCase):
    def test_deck_game(self):
        self.assertEqual(101, deck_game([1, 2, 100, 4]))
        self.assertEqual(101, deck_game_dp([1, 2, 100, 4]))

