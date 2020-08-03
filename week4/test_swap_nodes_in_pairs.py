from unittest import TestCase

from utils.listnode import ListNode, build_list
from week4.swap_nodes_in_pairs import Solution


class TestSolution(TestCase):
    def test_swap_pairs(self):
        s = Solution()
        ListNode()

        self.assertEqual('2->1->4->3', s.swapPairs(build_list("1->2->3->4")).entire_list())

