from typing import NamedTuple


class Info(NamedTuple):
    success: int = 0
    noden: int = 1


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:

        info = self.process(N, K, W, 0)
        print("success:", info.success, "noden:", info.noden)
        return info.success / info.noden

    def process(self, N, K, W, sum_) -> Info:
        # 终止节点
        if sum_ >= K:
            # 成功节点
            if sum_ <= N:
                return Info(1, 1)
            # 失败节点
            else:
                return Info(0, 1)

        # 可以继续向下的节点
        success = 0
        noden = 1
        for i in range(1, W + 1):
            info = self.process(N, K, W, sum_ + i)
            success += info.success
            noden += info.noden

        return Info(success, noden)
