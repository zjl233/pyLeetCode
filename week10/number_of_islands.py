from typing import List

from utils.misc import UnionFind


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        h, w = len(grid), len(grid[0])
        uf = UnionFind([(r, c) for r in range(h) for c in range(w) if grid[r][c] == '1'])
        for r in range(h):
            for c in range(w):
                if grid[r][c] == '1':
                    for y, x in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= y < h and 0 <= x < w and grid[y][x] == '1':
                            uf.union((r, c), (y, x))

        return len(uf.size)
