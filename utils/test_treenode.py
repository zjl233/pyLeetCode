from unittest import TestCase

from utils.treenode import test_tree, TreeNode


class TestTreeNode(TestCase):
    def test_entire_tree(self):
        s = test_tree().entire_tree()
