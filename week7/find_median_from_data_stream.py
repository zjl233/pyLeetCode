from heapq import heappop, heappush, heappushpop


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # lhalf 一般比 rhalf 长，长度差在 0， 1
        self.lo = []  # 大根堆，数组的左半边
        self.hi = []  # 小根堆，数组的右半边

    def addNum(self, num: int) -> None:
        heappush(self.hi, -heappushpop(self.lo, -num))

        if len(self.hi) > len(self.lo):
            heappush(self.lo, -heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) - len(self.hi) == 1:
            return -self.lo[0]
        else:  # 长度差为 0
            return (-self.lo[0] + self.hi[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
