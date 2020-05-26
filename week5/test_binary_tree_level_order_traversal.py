from unittest import TestCase

from utils.treenode import test_tree
from week5.binary_tree_level_order_traversal import Solution


class TestSolution(TestCase):
    def test_level_order(self):
        s = Solution()
        res = [
            [1],
            [2, 3],
            [4, 5, 6],
        ]
        self.assertEqual(res, s.levelOrder(test_tree()))
