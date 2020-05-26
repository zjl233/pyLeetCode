from unittest import TestCase

from utils.treenode import test_tree, TreeNode
from week5.check_completeness_of_a_binary_tree import Solution


class TestSolution(TestCase):
    def test_is_complete_tree(self):
        s = Solution()
        self.assertEqual(False, s.isCompleteTree(test_tree()))

        node1 = TreeNode(1)
        self.assertEqual(True, s.isCompleteTree(node1))
