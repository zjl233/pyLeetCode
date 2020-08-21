from unittest import TestCase

from week8.combination_sum_ii import Solution


class TestSolution(TestCase):
    def test_combination_sum2(self):
        s = Solution()
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expect = [
            [1, 7],
            [1, 2, 5],
            [2, 6],
            [1, 1, 6]
        ]
        res = s.combinationSum2(candidates, target)
        self.assertEqual(expect, res)
