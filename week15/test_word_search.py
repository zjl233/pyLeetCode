from unittest import TestCase

from week8.word_search import Solution


class TestSolution(TestCase):
    def test_exist(self):
        s = Solution()
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertTrue(s.exist(board, "ABCCED"))
        self.assertTrue(s.exist(board, "SEE"))
        self.assertFalse(s.exist(board, "ABCB"))
