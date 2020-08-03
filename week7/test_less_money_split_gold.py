from unittest import TestCase

from week7.less_money_split_gold import less_money


class Test(TestCase):
    def test_less_money(self):
        self.assertEqual(90, less_money([10, 30, 20]))
        self.assertEqual(67, less_money([3, 9, 5, 2, 4, 4]))
