from typing import List
from unittest import TestCase

from week14.ugly_number_ii import Solution


class TestSolution(TestCase):
    def test_nth_ugly_number(self):
        s = Solution()
        self.assertEqual(12, s.nthUglyNumber(10))