from typing import List
from unittest import TestCase

from week15.distinct_subsequences_ii import Solution


class TestSolution(TestCase):
    def test_distinct_subseq_ii(self):
        s = Solution()
        self.assertEqual(19, s.distinctSubseqII("abcbb"))
        self.assertEqual(7, s.distinctSubseqII("abc"))
        self.assertEqual(6, s.distinctSubseqII("aba"))
        self.assertEqual(3, s.distinctSubseqII("aaa"))

