from unittest import TestCase

from utils.listnode import build_list, entire_list
from week4.merge_k_sorted_lists import Solution


class TestSolution(TestCase):
    def test_merge_klists(self):
        lists_str = [
            "1->4->5",
            "1->3->4",
            "2->6",
        ]
        lists = [build_list(s) for s in lists_str]
        s = Solution()
        res = s.mergeKLists(lists)
        self.assertEqual("1->1->2->3->4->4->5->6", entire_list(res))

