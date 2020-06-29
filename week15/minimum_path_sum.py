from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 清洗数据
        if not grid or not grid[0]:
            return 0

        h, w = len(grid), len(grid[0])
        # 第一行只依赖左边的数据
        for c in range(1, w):
            grid[0][c] += grid[0][c - 1]
        # 第一列只依赖上边的数据
        for r in range(1, h):
            grid[r][0] += grid[r - 1][0]

        # 选取上边和左边的最小值
        for r in range(1, h):
            for c in range(1, w):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[h - 1][w - 1]
