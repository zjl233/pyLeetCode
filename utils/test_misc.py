from unittest import TestCase

from utils.misc import UnionFind


class TestUnionFind(TestCase):
    def test_add_node(self):
        uf = UnionFind([i for i in range(6)])
        uf.union(1, 2)
        self.assertTrue(uf.is_same_set(1, 2))
        self.assertFalse(uf.is_same_set(1, 3))
        self.assertFalse(uf.is_same_set(2, 4))
        uf.add_node(7)
        uf.add_node(8)
        self.assertFalse(uf.is_same_set(7, 8))
        self.assertFalse(uf.is_same_set(1, 8))
        uf.union(7, 8)
        self.assertTrue(uf.is_same_set(7, 8))
        uf.union(1, 7)
        self.assertTrue(uf.is_same_set(2, 8))
