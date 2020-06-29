from unittest import TestCase

from extra.reverse_sequence import reverse_sequence


class Test(TestCase):
    def test_reverse_sequence(self):
        self.assertEqual([4, 2, 1, 3], reverse_sequence([1, 2, 3, 4]))
