from unittest import TestCase

from week15.coin_change import Solution


class TestSolution(TestCase):
    def test_coin_change(self):
        s = Solution()
        res = s.coinChange([1, 2, 5], 100)
        # self.assertEqual(3, s.coin_change([1, 2, 5], 100))
        self.assertEqual(20, res)

    def test_coin_change_dp(self):
        s = Solution()
        res = s.coinChangeDP([1, 2, 5], 100)
        self.assertEqual(20, res)
