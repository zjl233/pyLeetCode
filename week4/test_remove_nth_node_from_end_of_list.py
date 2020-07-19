from unittest import TestCase

from utils.listnode import build_list, entire_list
from week4.remove_nth_node_from_end_of_list import Solution


class TestSolution(TestCase):
    def test_remove_nth_from_end(self):
        head = build_list([1, 2, 3, 4, 5])
        s = Solution()
        h = s.removeNthFromEnd(head, 2)
        self.assertEqual(entire_list(h), "1->2->3->5")
