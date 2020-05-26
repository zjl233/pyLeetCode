from unittest import TestCase

from utils.treenode import TreeNode
from week5.lowest_common_ancestor_of_a_binary_tree import Solution


class TestSolution(TestCase):
    def test_lowest_common_ancestor(self):
        node0 = TreeNode(0)
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node8 = TreeNode(8)
        node3.left = node5
        node3.right = node1
        node5.left = node6
        node5.right = node2
        node1.left = node0
        node1.right = node8
        node2.left = node7
        node2.right = node4

        s = Solution()
        print(s.lowestCommonAncestor(node3, node5, node1).val)
        print(s.lowestCommonAncestor(node3, node5, node4).val)
