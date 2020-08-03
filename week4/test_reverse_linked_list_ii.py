from unittest import TestCase

from utils.listnode import build_list
from week4.reverse_linked_list_ii import Solution


class TestSolution(TestCase):
    def test_reverse_between(self):
        s = Solution()
        self.assertEqual('1->4->3->2->5', s.reverseBetween(build_list('1->2->3->4->5'), 2, 4).entire_list())
