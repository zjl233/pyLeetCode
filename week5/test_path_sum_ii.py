from unittest import TestCase

from utils.treenode import test_tree
from week5.path_sum_ii import Solution


class TestSolution(TestCase):
    def test_path_sum(self):
        s = Solution()
        res = [[1, 2, 4]]
        self.assertEqual(res, s.pathSum(test_tree(), 7))

