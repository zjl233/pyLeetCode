from unittest import TestCase

from week7.max_cover import max_cover


class Test(TestCase):
    def test_max_cover(self):
        self.assertEqual(2, max_cover([1, 3, 6, 9], 2))
        self.assertEqual(3, max_cover([2, 7, 15, 19, 23, 34], 8))
