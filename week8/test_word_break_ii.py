from unittest import TestCase

from week8.word_break_ii import Solution


class TestSolution(TestCase):
    def test_word_break(self):
        s = Solution()
        expect1 = [
            "cat sand dog",
            "cats and dog",
        ]
        res1 = s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        self.assertEqual(expect1, res1)

        expect2 = [
            "pine apple pen apple",
            "pine applepen apple",
            "pineapple pen apple",
        ]
        res2 = s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
        self.assertEqual(expect2, res2)

        expect3 = []
        res3 = s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
        self.assertEqual(expect3, res3)
