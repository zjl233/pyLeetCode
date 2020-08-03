from unittest import TestCase

from week8.word_search_ii import Solution


class TestSolution(TestCase):
    def test_find_words(self):
        s = Solution()
        words = ["oath", "pea", "eat", "rain"]
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ]

        self.assertEqual({"eat", "oath"}, set(s.findWords(board, words)))
