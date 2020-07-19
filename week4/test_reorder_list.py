from unittest import TestCase

from utils.listnode import build_list
from week4.reorder_list import Solution


class TestSolution(TestCase):
    def test_reorder_list(self):
        s = Solution()
        head1 = build_list('1->2->3->4')
        s.reorderList(head1)
        self.assertEqual('1->4->2->3', head1.entire_list())

        head2 = build_list('1->2->3->4->5')
        s.reorderList(head2)
        self.assertEqual('1->5->2->4->3', head2.entire_list())
