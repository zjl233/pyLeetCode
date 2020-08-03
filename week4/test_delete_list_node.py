from unittest import TestCase

from utils.listnode import build_list, entire_list
from week4.delete_list_node import Solution


class TestSolution(TestCase):
    def test_delete_node(self):
        s = Solution()
        head = build_list([4, 5, 1, 9])
        print('before delete', entire_list(head))
        h = s.deleteNode(head, 5)
        print('after delete', entire_list(h))
