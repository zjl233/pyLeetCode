from typing import List
from unittest import TestCase

from week8.permutation_sequence import Solution


class TestSolution(TestCase):
    def test_get_permutation(self):
        s = Solution()
        self.assertEqual('2314', s.getPermutation(4, 9))