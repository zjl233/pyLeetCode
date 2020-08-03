from typing import List

from week7.insert_interval import Interval


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        itvs = [Interval(pair) for pair in intervals]
        ans: List[Interval] = []

        for itv in itvs:
            if ans and ans[-1].end >= itv.start:
                ans[-1].end = max(ans[-1].end, itv.end)
            else:
                ans.append(itv)

        return [i.to_list() for i in ans]
