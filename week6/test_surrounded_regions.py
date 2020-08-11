from unittest import TestCase

from week6.surrounded_regions import Solution


class TestSolution(TestCase):
    def test_solve(self):
        s = Solution()
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ]
        s.solve(board)
        res = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"]
        ]
        self.assertEqual(res, board)
