from unittest import TestCase

from utils.listnode import build_list
from week4.add_two_numbers_ii import Solution


class TestSolution(TestCase):
    def test_add_two_numbers(self):
        s = Solution()
        self.assertEqual('7->8->0->7', s.addTwoNumbers(build_list('7->2->4->3'), build_list('5->6->4')).entire_list())
