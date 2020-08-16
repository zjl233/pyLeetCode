from typing import List
from unittest import TestCase

from week14.ugly_number import Solution


class TestSolution(TestCase):
    def test_is_ugly(self):
        s = Solution()
        self.assertTrue(s.isUgly(6))
        self.assertTrue(s.isUgly(8))
        self.assertFalse(s.isUgly(14))
