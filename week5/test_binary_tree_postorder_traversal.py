from unittest import TestCase

from utils.treenode import test_tree
from week5.binary_tree_postorder_traversal import Solution


class TestSolution(TestCase):
    def test_postorder_traversal(self):
        s = Solution()
        res = s.postorderTraversal(test_tree())
        self.assertEqual([4, 5, 2, 6, 3, 1], res)

