from unittest import TestCase

from basic_lab1.sorting_partice import sorting_partice


class Test(TestCase):
    def test_sorting_partice(self):
        self.assertEqual([('fang', 90), ('ning', 70), ('yang', 50)], sorting_partice([('fang', 90), ('yang', 50), ('ning', 70)], 0))
