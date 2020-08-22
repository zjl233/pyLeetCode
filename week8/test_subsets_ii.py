from unittest import TestCase

from week8.subsets_ii import Solution


class TestSolution(TestCase):
    def test_subsets_with_dup(self):
        s = Solution()
        res = s.subsetsWithDup([1, 2, 2])
        expect1 = [
            [],
            [1],
            [1, 2],
            [1, 2, 2],
            [2],
            [2, 2],
        ]
        self.assertEqual(expect1, res)
