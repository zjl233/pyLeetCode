from unittest import TestCase

from utils.listnode import ListNode
from week4.intersection_of_two_linked_lists import Solution


class TestSolution(TestCase):
    def test_get_intersection_node(self):
        s = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node1.next = node2
        node3.next = node2
        node5.next = node3
        print(s.getIntersectionNode(node1, node5).val)