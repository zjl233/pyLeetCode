from typing import List
from unittest import TestCase

from utils.treenode import TreeNode
from week6.longest_consecutive_sequence import Solution


class TestSolution(TestCase):
    def test_longest_consecutive(self):
        s = Solution()
        self.assertEqual(4, s.longestConsecutive([100, 4, 200, 1, 3, 2]))
