from unittest import TestCase

from extra.longest_ased_subsequence import longest_sqeu, longest_sqeu_after_delete_num


class Test(TestCase):
    def test_longest_sqeu(self):
        self.assertEqual(4, longest_sqeu([1, 2, 3, 4, 3]))
        self.assertEqual(2, longest_sqeu([6, 3, 1, 3, 0]))
        self.assertEqual(4, longest_sqeu([7, 2, 3, 5, 6]))

    def test_longest_sqeu_after_change_num(self):
        self.assertEqual(5, longest_sqeu_after_delete_num([7, 2, 3, 1, 5, 6]))
