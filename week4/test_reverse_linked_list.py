from unittest import TestCase

from utils.listnode import ListNode
from week4.reverse_linked_list import Solution


class TestSolution(TestCase):
    def test_reverse_list(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2

        s = Solution()
        p = s.reverseListRecursive(node1)
        while p:
            print(p.val)
            p = p.next
