from unittest import TestCase

from utils.treenode import TreeNode
from week5.minimum_depth_of_binary_tree import Solution


class TestSolution(TestCase):
    def test_min_depth(self):
        s = Solution()
        root = TreeNode().deserialize('[1, 2]')
        root.entire_tree()
        self.assertEqual(2, s.minDepth(root))


