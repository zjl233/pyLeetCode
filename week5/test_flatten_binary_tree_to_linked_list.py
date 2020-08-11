from typing import List
from unittest import TestCase

from utils.treenode import test_tree
from week5.flatten_binary_tree_to_linked_list import Solution


class TestSolution(TestCase):
    def test_flatten(self):
        s = Solution()
        root = test_tree()
        s.flatten(root)

        print(root)
