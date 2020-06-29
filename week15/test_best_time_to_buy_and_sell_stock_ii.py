from unittest import TestCase

from week15.best_time_to_buy_and_sell_stock_ii import Solution


class TestSolution(TestCase):
    def test_max_profit(self):
        s = Solution()
        self.assertEqual(7, s.maxProfit([7, 1, 5, 3, 6, 4]))
        self.assertEqual(4, s.maxProfit([1, 2, 3, 4, 5]))
        self.assertEqual(0, s.maxProfit([7, 6, 4, 3, 1]))
