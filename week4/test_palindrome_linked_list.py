from unittest import TestCase

from utils.listnode import ListNode
from week4.palindrome_linked_list import Solution


class TestSolution(TestCase):
    def test_is_palindrome(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(1)

        node1.next = node2
        node2.next = node3

        s = Solution()
        s.isPalindrome(node1)