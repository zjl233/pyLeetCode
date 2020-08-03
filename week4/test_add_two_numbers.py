from unittest import TestCase

from utils.listnode import build_list, entire_list
from week4.add_two_numbers import Solution


class TestSolution(TestCase):
    def test_add_two_numbers(self):
        s = Solution()
        l1 = build_list([2, 4, 3])
        l2 = build_list([5, 6, 4, 8])
        res = s.addTwoNumbers(l1, l2)
        print(entire_list(res))

        l1 = build_list([6, 1])
        l2 = build_list([4])
        res = s.addTwoNumbers(l1, l2)
        print(entire_list(res))
