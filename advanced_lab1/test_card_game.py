from unittest import TestCase

from advanced_lab1.card_game import score_diff


class Test(TestCase):
    def test_score_diff(self):
        self.assertEqual(5, score_diff([2, 7, 4]))
