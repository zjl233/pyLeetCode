from unittest import TestCase

from utils.listnode import ListNode, build_list
from week4.remove_duplicates_from_sorted_list import Solution


class TestSolution(TestCase):
    def test_delete_duplicates(self):
        s = Solution()
        ListNode()
        self.assertEqual('1->2', s.deleteDuplicates(build_list('1->1->2')).entire_list())
        self.assertEqual('1->2->3', s.deleteDuplicates(build_list('1->1->2->3->3')).entire_list())
