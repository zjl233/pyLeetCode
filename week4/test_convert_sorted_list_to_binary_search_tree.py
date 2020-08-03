from unittest import TestCase

from utils.listnode import build_list
from week4.convert_sorted_list_to_binary_search_tree import Solution


class TestSolution(TestCase):
    def test_sorted_list_to_bst(self):
        s = Solution()
        res = s.sortedListToBST(build_list([-10, -3, 0, 5, 9]))
        print(res)
