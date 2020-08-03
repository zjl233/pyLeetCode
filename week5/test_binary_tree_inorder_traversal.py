from unittest import TestCase

from utils.treenode import test_tree
from week5.binary_tree_inorder_traversal import Solution


class TestSolution(TestCase):
    def test_inorder_traversal(self):
        s = Solution()
        res = s.inorderTraversal(test_tree())
        self.assertEqual([4, 2, 5, 1, 3, 6], res)

    def test_inorder_traversal_color(self):
        s = Solution()
        res = s.inorderTraversalColor(test_tree())
        self.assertEqual([4, 2, 5, 1, 3, 6], res)

    def test_inorder_traversal_mirrors(self):
        s = Solution()
        res = s.inorderTraversalMirrors(test_tree())
        self.assertEqual([4, 2, 5, 1, 3, 6], res)


