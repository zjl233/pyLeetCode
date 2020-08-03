from unittest import TestCase

from utils.treenode import TreeNode
from week5.binary_tree_maximum_path_sum import Solution


class TestSolution(TestCase):
    def test_max_path_sum(self):
        root = TreeNode().deserialize("[1,2,null,null,3]")
        s = Solution()
        self.assertEqual(6, s.maxPathSum(root))

        root2 = TreeNode().deserialize("[-10,9,null,null,20,15,7]")
        s = Solution()
        self.assertEqual(42, s.maxPathSum(root2))

        root3 = TreeNode().deserialize("[-3]")
        s = Solution()
        self.assertEqual(-3, s.maxPathSum(root3))


