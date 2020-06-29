from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        # 项目 (c, p) 元组
        # 小根堆(未解锁的项目)，按照 费用 排列
        # 大根堆(解锁的项目)，按照 利润 排列
        if not Profits or not Capital:
            return W

        locked = list(zip(Capital, Profits))
        heapify(locked)
        unlocked = []

        for _ in range(k):
            # 将未解锁项目中，费用小于 W 的，加入解锁项目
            while locked and locked[0][0] <= W:
                heappush(unlocked, -heappop(locked)[1])

            if not unlocked:
                return W

            W += -heappop(unlocked)

        return W

