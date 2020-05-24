from unittest import TestCase

from utils.treenode import test_tree
from week5.binary_tree_preorder_traversal import Solution


class TestSolution(TestCase):
    def test_preorder_traversal(self):
        s = Solution()
        res = s.preorderTraversal(test_tree())
        self.assertEqual([1, 2, 4, 5, 3, 6], res)

    def test_preorder_traversal_recusive(self):
        s = Solution()
        res = s.preorderTraversalRecusive(test_tree())
        self.assertEqual([1, 2, 4, 5, 3, 6], res)

    def test_preorder_traversal_color(self):
        s = Solution()
        res = s.preorderTraversalColor(test_tree())
        self.assertEqual([1, 2, 4, 5, 3, 6], res)
