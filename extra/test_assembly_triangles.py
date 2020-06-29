from unittest import TestCase

from extra.assembly_triangles import is_triangle, assembly_ways


class Test(TestCase):
    def test_is_triangle(self):
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertFalse(is_triangle(1, 2, 3))
        self.assertFalse(is_triangle(1, 1, 3))

    def test_assembly_ways(self):
        self.assertEqual(3, assembly_ways([1, 2, 3, 4, 5]))
