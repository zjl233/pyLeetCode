from itertools import product, chain
from typing import NamedTuple


# 对于非叶子节点
# 从这个分支向下，共有多少种，在棋盘里的情况
# 对于叶子节点
# 出去了，还是没出去
class Info(NamedTuple):
    in_: int = 0
    out: int = 0


# 如果总的可能性为 8 ** K，那么必定有 跳出去 再 调回来 的情况，这种情况无效
# 如果跳出去的时候终止，那么总的可能性就没有 8 ** K，需要记录 跳出去的次数

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1

        info = self.process(N, K, r, c)
        return info.in_ / 8 ** K

    # 返回什么: 出去，和没出去的个数
    def process(self, N: int, K: int, r: int, c: int) -> Info:
        if not (0 <= r < N and 0 <= c < N):  # 出界，立刻返回。跳出去再跳回来是无效的
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

    def knightProbabilityDP(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1

        dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K + 1)]  # 步数有 1 ~ k 层，第 0 是其实位置
        dp[0][r][c] = 1
        for h in range(1, K + 1):
            for r in range(N):
                for c in range(N):

                    moves = chain(product([r - 1, r + 1], [c - 2, c + 2]), product([r - 2, r + 2], [c - 1, c + 1]))
                    # moves = list(product([r - 1, r + 1], [c - 2, c + 2])) + list(product([r - 2, r + 2], [c - 1, c + 1]))
                    for y, x in moves:
                        if 0 <= y < N and 0 <= x < N:
                            dp[h][r][c] += dp[h - 1][y][x]

        s = 0
        for r in range(N):
            for c in range(N):
                s += dp[K][r][c]
        return s / 8 ** K
