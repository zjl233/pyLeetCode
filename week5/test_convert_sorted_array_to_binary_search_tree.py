from unittest import TestCase

from week5.convert_sorted_array_to_binary_search_tree import Solution


class TestSolution(TestCase):
    def test_sorted_array_to_bst(self):
        nums = list(range(1, 8))
        s = Solution()
        root = s.sortedArrayToBST(nums)
        print(root)
