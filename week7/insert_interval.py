from typing import List


class Interval:

    def __init__(self, pair: List[int]) -> None:
        self.start = pair[0]
        self.end = pair[1]

    def to_list(self) -> List[int]:
        return [self.start, self.end]


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        ans: List[Interval] = []
        n = Interval(newInterval)

        for i, itv in enumerate(intervals):
            itv = Interval(itv)
            if itv.end < n.start:
                ans.append(itv)
            elif itv.start > n.end:
                ans.append(n)
                return [item.to_list() for item in ans] + intervals[i:]
            else:
                n.start = min(n.start, itv.start)
                n.end = max(n.end, itv.end)

        ans.append(n)
        return [itv.to_list() for itv in ans]
