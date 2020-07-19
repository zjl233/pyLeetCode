from unittest import TestCase

from utils.listnode import build_list
from week4.sort_list import Solution


class TestSolution(TestCase):
    def test_sort_list(self):
        s = Solution()
        self.assertEqual('1->2->3->4', s.sortList(build_list('4->2->1->3')).entire_list())
        self.assertEqual('-1->0->3->4->5', s.sortList(build_list('-1->5->3->4->0')).entire_list())
