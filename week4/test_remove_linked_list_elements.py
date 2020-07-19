from unittest import TestCase

from utils.listnode import ListNode, build_list
from week4.remove_linked_list_elements import Solution


class TestSolution(TestCase):
    def test_remove_elements(self):
        s = Solution()
        self.assertEqual('1->2->3->4->5', s.removeElements(build_list('1->2->6->3->4->5->6'), 6).entire_list())
        self.assertEqual(None, s.removeElements(build_list('1->1'), 1))
