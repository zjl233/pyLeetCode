from unittest import TestCase

from week1.qiu_12n_lcof import Solution


class TestSolution(TestCase):
    def test_russia_mul(self):
        s = Solution()
        self.assertEqual(s.russia_mul(3, 4), 12)


class TestSolution(TestCase):
    def test_sum_nums(self):
        s = Solution()
        self.assertEqual(6, s.sumNums(3))
