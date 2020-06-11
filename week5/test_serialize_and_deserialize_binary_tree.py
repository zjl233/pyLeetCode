from unittest import TestCase

from utils.treenode import TreeNode, test_tree
from week5.serialize_and_deserialize_binary_tree import Codec


class TestCodec(TestCase):
    def test_serialize(self):
        c = Codec()
        s = "1,2,3,4,5,#,6,#,#,#,#,#,#"
        self.assertEqual(s, c.serialize(test_tree()))
        root = c.deserialize(s)
        print(root)

