from typing import List
from unittest import TestCase

from week15.minimum_insertion_steps_to_make_a_string_palindrome import Solution


class TestSolution(TestCase):
    def test_min_insertions(self):
        s = Solution()
        self.assertEqual(0, s.minInsertions("zzazz"))
        self.assertEqual(2, s.minInsertions("mbadm"))
        self.assertEqual(5, s.minInsertions("leetcode"))
        self.assertEqual(4, s.minInsertions("ab123ce21"))
