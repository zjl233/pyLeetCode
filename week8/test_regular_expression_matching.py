from unittest import TestCase

from week8.regular_expression_matching import Solution


class TestSolution(TestCase):
    def test_is_match(self):
        s = Solution()
        self.assertTrue(s.isMatch("ab", ".*"))

        self.assertFalse(s.isMatch("aa", "a"))
        self.assertTrue(s.isMatch("aa", "a*"))
        self.assertTrue(s.isMatch("aab", "c*a*b"))
        self.assertFalse(s.isMatch("mississippi", "mis*is*p*."))
        self.assertFalse(s.isMatch("ab", ".*c"))
        self.assertFalse(s.isMatch("", ".*c"))
        self.assertTrue(s.isMatch("aaa", "a*a"))


    def test_is_match_dp(self):
        s = Solution()
        # self.assertTrue(s.is_match_dp("ab", ".*"))

        # self.assertFalse(s.is_match_dp("aa", "a"))
        # self.assertTrue(s.is_match_dp("aa", "a*"))
        # self.assertTrue(s.is_match_dp("aab", "c*a*b"))
        self.assertFalse(s.is_match_dp("mississippi", "mis*is*p*."))
        self.assertFalse(s.is_match_dp("ab", ".*c"))
        self.assertFalse(s.is_match_dp("", ".*c"))
        self.assertTrue(s.is_match_dp("aaa", "a*a"))
