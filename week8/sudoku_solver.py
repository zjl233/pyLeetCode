from pprint import pprint
from typing import List


class Solution:
    def __init__(self):
        self.sz = 9

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.process(board, 0, 0)

    def process(self, board: List[List[str]], r: int, c: int) -> bool:
        if r == self.sz:
            return True
        if c == self.sz:
            return self.process(board, r + 1, 0)
        if board[r][c] != '.':
            return self.process(board, r, c + 1)

        for ch in [str(n) for n in range(1, 10)]:
            if self.is_valid(board, r, c, ch):
                board[r][c] = ch
                if self.process(board, r, c + 1):
                    return True
                board[r][c] = '.'

        return False

    def is_valid(self, board: List[List[str]], r: int, c: int, n: str) -> bool:
        for i in range(self.sz):
            if board[r][i] == n:
                return False
            if board[i][c] == n:
                return False
            if board[(r // 3) * 3 + (i // 3)][(c // 3) * 3 + (i % 3)] == n:
                return False

        return True
