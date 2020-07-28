from unittest import TestCase

from week5.unique_binary_search_trees import Solution


class TestSolution(TestCase):
    def test_num_trees(self):
        s = Solution()
        self.assertEqual(5, s.numTrees(3))
