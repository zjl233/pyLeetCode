from unittest import TestCase

from week15.minimum_path_sum import Solution


class TestSolution(TestCase):
    def test_min_path_sum(self):
        s = Solution()
        g = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        self.assertEqual(7, s.minPathSum(g))
