from unittest import TestCase

from utils.treenode import test_tree
from week5.maximum_depth_of_binary_tree import Solution


class TestSolution(TestCase):
    def test_max_depth(self):
        s = Solution()
        self.assertEqual(3, s.maxDepth(test_tree()))


# 