from unittest import TestCase

from utils.listnode import entire_list, ListNode, build_list


class Test(TestCase):
    def test_entire_list(self):
        node = ListNode(1, ListNode(2, ListNode(3)))
        self.assertEqual("1->2->3", entire_list(node))

    def test_build_list(self):
        list_str = "1->2->3"
        h1 = build_list(list_str)
        self.assertEqual(list_str, entire_list(h1))

        h2 = build_list([1, 2, 3])
        self.assertEqual(list_str, entire_list(h2))
