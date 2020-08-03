from unittest import TestCase

from utils.treenode import test_tree
from week13.morris import morris, morris_pre, morris_in


class Test(TestCase):
    def test_morris(self):
        print(morris(test_tree()))

    def test_morris_pre(self):
        print(morris_pre(test_tree()))

    def test_morris_in(self):
        print(morris_in(test_tree()))
