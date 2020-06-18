from unittest import TestCase

from week15.knight_probability_in_chessboard import Solution


class TestSolution(TestCase):
    def test_knight_probability(self):
        s = Solution()
        res = s.knightProbability(3, 2, 0, 0)
        self.assertEqual(0.0625, res)

    def test_knight_probability_dp(self):
        s = Solution()
        res = s.knightProbabilityDP(3, 2, 0, 0)
        self.assertEqual(0.0625, res)
