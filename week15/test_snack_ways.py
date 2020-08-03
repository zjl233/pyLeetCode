from unittest import TestCase

from week15.snack_ways import snack_brute, snack_dp, snack_dp2


class Test(TestCase):
    def test_snack_brute(self):
        self.assertEqual(6, snack_brute(5, [1, 2, 4]))
        self.assertEqual(8, snack_brute(10, [1, 2, 4]))
        self.assertEqual(2, snack_brute(5, [3, 6]))

    def test_snack_dp(self):
        self.assertEqual(6, snack_dp(5, [1, 2, 4]))
        self.assertEqual(8, snack_dp(10, [1, 2, 4]))
        self.assertEqual(2, snack_dp(5, [3, 6]))

    def test_snack_dp2(self):
        self.assertEqual(6, snack_dp2(5, [1, 2, 4]))
        # self.assertEqual(8, snack_dp2(10, [1, 2, 4]))
        # self.assertEqual(2, snack_dp2(5, [3, 6]))
