from unittest import TestCase

from week8.combination_sum_iii import Solution


class TestSolution(TestCase):
    def test_combination_sum3(self):
        s = Solution()
        expect1 = [[1, 2, 4]]
        res = s.combinationSum3(3, 7)
        self.assertEqual(expect1, res)

        expect2 = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        res = s.combinationSum3(3, 9)
        self.assertEqual(expect2, res)
