from unittest import TestCase

from utils.treenode import TreeNode, test_tree
from week5.serialize_and_deserialize_binary_tree import Codec


class TestCodec(TestCase):
    def test_serialize(self):
        c = Codec()
        s = str([1, 2, 4, None, None, 5, None, None, 3, None, 6, None, None]).replace("None", "null")
        self.assertEqual(s, c.serialize(test_tree()))
        root = c.deserialize(s)
        root.entire_tree()
        # print(root.entire_tree())

