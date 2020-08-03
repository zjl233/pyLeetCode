from unittest import TestCase

from utils.listnode import build_list, entire_list
from week4.merge_two_sorted_lists import Solution


class TestSolution(TestCase):
    def test_merge_two_lists(self):
        h1 = build_list("1->2->4")
        h2 = build_list("1->3->4")
        s = Solution()
        res = s.mergeTwoLists(h1, h2)
        self.assertEqual("1->1->2->3->4->4", entire_list(res))
