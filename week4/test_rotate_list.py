from unittest import TestCase

from utils.listnode import build_list
from week4.rotate_list import Solution


class TestSolution(TestCase):
    def test_rotate_right(self):
        s = Solution()
        self.assertEqual('4->5->1->2->3', s.rotateRight(build_list('1->2->3->4->5'), 2).entire_list())
        self.assertEqual('2->0->1', s.rotateRight(build_list('0->1->2'), 4).entire_list())
        self.assertEqual('1->2', s.rotateRight(build_list('1->2'), 2).entire_list())
