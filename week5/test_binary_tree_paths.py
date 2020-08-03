from typing import List
from unittest import TestCase

from utils.treenode import TreeNode
from week5.binary_tree_paths import Solution


class TestSolution(TestCase):
    def test_binary_tree_paths(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node5 = TreeNode(5)
        node1.left = node2
        node1.right = node3
        node2.right = node5

        s = Solution()
        res = s.binaryTreePaths(node1)
        self.assertEqual(["1->2->5", "1->3"], res)
