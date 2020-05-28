from unittest import TestCase

from utils.listnode import ListNode
from week4.partition_list import Solution


class TestSolution(TestCase):
    def test_partition(self):
        s = Solution()
        # 输入: head = 1->4->3->2->5->2, x = 3
        # 输出: 1->2->2->4->3->5

        node6 = ListNode(2)
        node5 = ListNode(5, node6)
        node4 = ListNode(2, node5)
        node3 = ListNode(3, node4)
        node2 = ListNode(4, node3)
        node1 = ListNode(1, node2)

        head = s.partition(node1, 3)
        res = []
        print(head)
        while head:
            res.append(head.val)
            head = head.next
        print(res)

    def test_partition2(self):
        s = Solution()
        # 输入: head = 1->4->3->2->5->2, x = 3
        # 输出: 1->2->2->4->3->5

        node2 = ListNode(1)
        node1 = ListNode(1, node2)

        head = s.partition(node1, 0)
        res = []
        print(head)
        while head:
            res.append(head.val)
            head = head.next
        print(res)
