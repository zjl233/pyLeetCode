from unittest import TestCase

from utils.treenode import test_tree
from week5.binary_tree_zigzag_level_order_traversal import Solution


class TestSolution(TestCase):
    def test_zigzag_level_order(self):
        s = Solution()
        print(s.zigzagLevelOrder(test_tree()))
