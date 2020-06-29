from typing import List


class Solution:
    # 非贪心解法，这一题同时也是线段最大重合问题
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 上车下车问题，统计公交车上，最多有多少人
        events = [(itv[0], 1) for itv in intervals] + [(itv[1], -1) for itv in intervals]
        events.sort()
        # 当前车上有多少人，车上最多的时候有多少人
        cur, max_ = 0, 0
        for _, e in events:
            cur += e
            max_ = max(max_, cur)
        return max_

