from unittest import TestCase

from utils.treenode import test_tree
from week5.diameter_of_binary_tree import Solution


class TestSolution(TestCase):
    def test_diameter_of_binary_tree(self):
        s = Solution()
        self.assertEqual(5, s.diameterOfBinaryTree(test_tree()))
