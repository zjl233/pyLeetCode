from unittest import TestCase

from week15.integer_break import Solution


class TestSolution(TestCase):
    def test_integer_break(self):
        s = Solution()
        self.assertEqual(1, s.integerBreak(2))
        self.assertEqual(9, s.integerBreak(6))
        self.assertEqual(36, s.integerBreak(10))

    def test_integer_break_dp(self):
        s = Solution()
        # self.assertEqual(1, s.integerBreakDP(2))
        # self.assertEqual(9, s.integerBreakDP(6))
        self.assertEqual(36, s.integerBreakDP(10))
