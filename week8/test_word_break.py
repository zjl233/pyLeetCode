from unittest import TestCase

from week8.word_break import Solution


class TestSolution(TestCase):
    def test_word_break(self):
        s = Solution()
        self.assertTrue(s.wordBreak("leetcode", ["leet", "code"]))
        self.assertTrue(s.wordBreak("applepenapple", ["apple", "pen"]))
        self.assertFalse(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_word_break_dp(self):
        s = Solution()
        self.assertTrue(s.wordBreakDP("leetcode", ["leet", "code"]))
        self.assertTrue(s.wordBreakDP("applepenapple", ["apple", "pen"]))
        self.assertFalse(s.wordBreakDP("catsandog", ["cats", "dog", "sand", "and", "cat"]))
