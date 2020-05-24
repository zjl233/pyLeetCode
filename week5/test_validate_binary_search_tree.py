from unittest import TestCase

from utils.treenode import TreeNode
from week5.validate_binary_search_tree import Solution


class TestSolution(TestCase):
    def test_is_valid_bst(self):
        s = Solution()
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node2.left = node1
        node2.right = node3
        self.assertTrue(s.isValidBST(node2))

    def test_is_valid_bst2(self):
        s = Solution()
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node5.left = node1
        node5.right = node4
        node4.left = node3
        node4.right = node6
        self.assertFalse(s.isValidBST(node5))

    def test_is_valid_bst3(self):
        s = Solution()
        node0 = TreeNode(0)
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node3.left = node1
        node3.right = node5
        node5.left = node4
        node5.right = node6

        node1.left = node0
        node1.right = node2
        node2.right = TreeNode(3)

        self.assertFalse(s.isValidBST(node3))
