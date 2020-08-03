from unittest import TestCase

from week5.unique_binary_search_trees_ii import Solution


class TestSolution(TestCase):
    def test_generate_trees(self):
        s = Solution()
        s.generateTrees(10)
