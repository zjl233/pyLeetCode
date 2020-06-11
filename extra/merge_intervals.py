from typing import List


class Interval:

    def __init__(self, left: int, right: int) -> None:
        self.left = left
        self.right = right

    def __and__(self, other: 'Interval') -> 'Interval':
        pass




class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda itv: itv[0])
