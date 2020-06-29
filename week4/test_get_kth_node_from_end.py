from unittest import TestCase

from utils.listnode import entire_list, build_list
from week4.get_kth_node_from_end import Solution


class TestSolution(TestCase):
    def test_get_kth_from_end(self):
        head = build_list([1, 2, 3, 4, 5])
        s = Solution()
        res = s.getKthFromEnd(head, 2)
        self.assertEqual(entire_list(res), "4->5")
