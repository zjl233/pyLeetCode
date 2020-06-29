from typing import List
from unittest import TestCase

from week4.copy_list_with_random_pointer import Solution, Node


class TestSolution(TestCase):
    def test_copy_random_list_lianxi(self):
        s = Solution()
        node7 = Node(7)
        node13 = Node(13)
        node7.next = node13
        node13.random = node7
        s.copyRandomList(node7)
