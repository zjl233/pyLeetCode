from unittest import TestCase

from week8.n_queens import Solution


class TestSolution(TestCase):
    def test_solve_nqueens(self):
        s = Solution()
        solutions = [
            [".Q..",
             "...Q",
             "Q...",
             "..Q."],

            ["..Q.",
             "Q...",
             "...Q",
             ".Q.."]
        ]
        self.assertEqual(solutions, s.solveNQueens(4))