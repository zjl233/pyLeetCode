from typing import List

from utils.misc import UnionFind


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not len(board):
            return

        h, w = len(board), len(board[0])
        uf = UnionFind([(r, c) for r in range(h) for c in range(w) if board[r][c] == 'O'])
        dummy = (h, w)  # 代表外部区域
        uf.add_node(dummy)
        for r in range(h):
            for c in range(w):
                if board[r][c] == 'O':
                    # 边缘节点，连接到 dummy 上
                    if r == 0 or r == h - 1 or c == 0 or c == w - 1:
                        uf.union((r, c), dummy)
                    # 按岛屿问题处理
                    for y, x in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= y < h and 0 <= x < w and board[y][x] == 'O':
                            uf.union((r, c), (y, x))

        for r in range(h):
            for c in range(w):
                # 没有与外界联通
                if board[r][c] == 'O' and not uf.is_same_set(dummy, (r, c)):
                    board[r][c] = 'X'
