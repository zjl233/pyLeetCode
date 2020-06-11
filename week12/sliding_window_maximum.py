from collections import deque
from typing import List, Deque


class MonotonicQueue:

    def __init__(self) -> None:
        self.nums: Deque[int] = deque()
        self.maxs: Deque[int] = deque()

    def enqueue(self, x) -> None:
        self.nums.append(x)
        while self.maxs and self.maxs[-1] < x:
            self.maxs.pop()
        self.maxs.append(x)

    def dequeue(self) -> int:
        if not self.nums:
            raise RuntimeError

        n = self.nums.popleft()
        if self.maxs and n == self.maxs[0]:
            self.maxs.popleft()

        return n


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1 <= nums.length <= 10 ^ 5
        # -10 ^ 4 <= nums[i] <= 10 ^ 4
        # 1 <= k <= nums.length
        res: List[int] = []
        mq = MonotonicQueue()
        for i in range(0, k - 1):
            mq.enqueue(nums[i])
        for i in range(k - 1, len(nums)):
            mq.enqueue(nums[i])
            res.append(mq.maxs[0])
            mq.dequeue()
        return res
