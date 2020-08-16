from unittest import TestCase

from week8.permutations_ii import Solution


class TestSolution(TestCase):
    def test_permute_unique(self):
        s = Solution()
        res = s.permuteUnique([1, 1, 2])
        expect = [
            [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1]
        ]

        self.assertEqual(expect, res)
