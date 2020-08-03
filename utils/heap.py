from heapq import heappop, heappush


# 只支持 int 的，大根堆和小根堆，python 小根堆的包装

class Heap:
    def __init__(self, nums=None, min_heap: bool = True) -> None:
        if nums is None:
            nums = []
        self.nums = nums
        self.min_heap = min_heap

    def push(self, num: int):
        heappush(self.nums, (num if self.min_heap else -num))

    def pop(self) -> int:
        return heappop(self.nums) if self.min_heap else -heappop(self.nums)

    def top(self) -> int:
        return self.nums[0] if self.min_heap else -self.nums[0]
