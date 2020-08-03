from unittest import TestCase

from basic_lab2.insertion_sort_list import Solution
from utils.listnode import ListNode, build_list


class TestSolution(TestCase):
    def test_insertion_sort_list(self):
        s = Solution()
        ListNode()
        self.assertEqual('1->2->3->4', s.insertionSortList(build_list('4->2->1->3')).entire_list())
        self.assertEqual('-1->0->3->4->5', s.insertionSortList(build_list('-1->5->3->4->0')).entire_list())
