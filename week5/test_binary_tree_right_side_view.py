from unittest import TestCase

from utils.treenode import test_tree
from week5.binary_tree_right_side_view import Solution


class TestSolution(TestCase):
    def test_right_side_view(self):
        s = Solution()
        self.assertEqual([1, 3, 6], s.rightSideView(test_tree()))

    def test_right_side_view_dfs(self):
        s = Solution()
        self.assertEqual([1, 3, 6], s.rightSideViewDfs(test_tree()))


