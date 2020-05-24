from unittest import TestCase

from utils.treenode import TreeNode
from week5.balanced_binary_tree import Solution


class TestSolution(TestCase):
    def test_is_balanced(self):
        s = Solution()
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node2.left = node1
        node2.right = node3
        self.assertTrue(s.isBalanced(node2))

    def test_is_balanced2(self):
        s = Solution()
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node2.left = node1
        node2.right = node3
        node1.left = node4
        node4.left = TreeNode(5)
        self.assertFalse(s.isBalanced(node2))
