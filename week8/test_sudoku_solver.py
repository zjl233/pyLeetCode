from unittest import TestCase

from week8.sudoku_solver import Solution


class TestSolution(TestCase):
    def test_solve_sudoku(self):
        sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
                  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        s = Solution()
        s.solveSudoku(sudoku)
        print(sudoku)
