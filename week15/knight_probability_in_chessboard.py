from functools import lru_cache
from itertools import product
from typing import NamedTuple


# 对于非叶子节点
# 从这个分支向下，共有多少种，在棋盘里的情况
# 对于叶子节点
# 出去了，还是没出去
class Info(NamedTuple):
    in_: int = 0
    out: int = 0


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1

        info = self.process(N, K, r, c)
        return info.in_ / 8 ** K

    # 返回什么: 出去，和没出去的个数
    @lru_cache
    def process(self, N: int, K: int, r: int, c: int) -> Info:
        if not (0 <= r < N and 0 <= c < N):  # 出界，立刻返回
            return Info(0, 1)
        elif K == 0:  # 用完移动次数，并且没有出界
            return Info(1, 0)

        in_, out = 0, 0
        moves = list(product([r - 1, r + 1], [c - 2, c + 2])) + list(product([r - 2, r + 2], [c - 1, c + 1]))
        for y, x in moves:
            info = self.process(N, K - 1, y, x)
            in_ += info.in_
            out += info.out

        return Info(in_, out)
