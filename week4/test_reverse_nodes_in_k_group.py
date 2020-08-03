from unittest import TestCase

from utils.listnode import build_list
from week4.reverse_nodes_in_k_group import Solution


class TestSolution(TestCase):
    def test_reverse_kgroup(self):
        s = Solution()
        self.assertEqual('2->1->4->3->5', s.reverseKGroup(build_list('1->2->3->4->5'), 2).entire_list())
        self.assertEqual('3->2->1->4->5', s.reverseKGroup(build_list('1->2->3->4->5'), 3).entire_list())
