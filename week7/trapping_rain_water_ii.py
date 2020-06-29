"""
https://leetcode-cn.com/problems/trapping-rain-water-ii/


给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。



示例：

给出如下 3x6 的高度图:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

返回 4 。


如上图所示，这是下雨前的高度图[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 的状态。





下雨后，雨水将会被存储在这些方块中。总的接雨水量是4。



提示：

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000

"""
from heapq import heappush, heappop
from typing import List, Tuple


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        hp: List[Tuple[int, int, int]] = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        # 将边缘放入 heap
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    h = heightMap[r][c]
                    heappush(hp, (h, r, c))
                    visited[r][c] = True

        # 从小根堆里一次弹出 top, 更新 max_h
        # 将 top 的邻居放入 小根堆的同时，计算 邻居高度与 max_h 的差，这就是邻居的蓄水量，注意邻居比 max_h 高的情况
        lmt_h = -1
        water = 0
        while hp:
            h, r, c = heappop(hp)
            # 当前区域的高度瓶颈，如果 lmt_h 更新了，那么就说明，lmt_h 所属的区域没有更低的格子了
            lmt_h = max(lmt_h, h)
            for y, x in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= y < m and 0 <= x < n and not visited[y][x]:
                    cur_h = heightMap[y][x]
                    # 当前区域的蓄水量，取决于当前区域的最大高度
                    water += max(0, lmt_h - cur_h)
                    heappush(hp, (cur_h, y, x))
                    visited[y][x] = True

        return water
