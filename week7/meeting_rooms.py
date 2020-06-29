from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 1.按照区间的左边界排序
        # 2.挨个查看区间是否有交集，前一个区间的有边界是否 <= 后一个区间的左边界
        intervals.sort(key=lambda itv: itv[0])
        return all(intervals[i][1] <= intervals[i + 1][0] for i in range(len(intervals) - 1))

