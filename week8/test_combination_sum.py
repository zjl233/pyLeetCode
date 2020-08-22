from unittest import TestCase

from week8.combination_sum import Solution


class TestSolution(TestCase):
    def test_combination_sum(self):
        s = Solution()
        candidates = [2, 3, 6, 7]
        target = 7
        expect = [
            [7],
            [2, 2, 3]
        ]
        res = s.combinationSum(candidates, target)
        self.assertEqual(expect, res)
