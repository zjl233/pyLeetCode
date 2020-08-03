from unittest import TestCase

from week15.longest_common_subsequence import Solution


class TestSolution(TestCase):
    def test_longest_common_subsequence(self):
        s = Solution()
        self.assertEqual(3, s.longestCommonSubsequence("abcde", "ace"))
        self.assertEqual(3, s.longestCommonSubsequence("abc", "abc"))
        self.assertEqual(0, s.longestCommonSubsequence("abc", "def"))
        self.assertEqual(2, s.longestCommonSubsequence("ezupkr", "ubmrapg"))
