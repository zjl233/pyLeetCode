from typing import List
from unittest import TestCase

from utils.listnode import ListNode, build_list, entire_list
from week4.remove_duplicates_from_sorted_list_ii import Solution


class TestSolution(TestCase):
    def test_delete_duplicates(self):
        s = Solution()
        self.assertEqual('1', s.deleteDuplicates(build_list('1->2->2->2')).entire_list())
        self.assertEqual('1->2->5', s.deleteDuplicates(build_list('1->2->3->3->4->4->5')).entire_list())
        self.assertEqual('1->2->5', s.deleteDuplicates(build_list('1->2->3->3->4->4->5')).entire_list())
