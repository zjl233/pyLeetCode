from unittest import TestCase

from week8.permutations import Solution


class TestSolution(TestCase):
    def test_permute(self):
        s = Solution()
        expect1 = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
        res = s.permute([1, 2, 3])
        self.assertEqual(expect1, res)
