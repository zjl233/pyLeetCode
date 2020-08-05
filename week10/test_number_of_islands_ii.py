from unittest import TestCase

from week10.number_of_islands_ii import Solution


class TestSolution(TestCase):
    def test_num_islands2(self):
        s = Solution()
        res = s.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]])
        self.assertEqual([1, 1, 2, 3], res)
