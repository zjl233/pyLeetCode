from typing import List, Dict


#
#
# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # write code here
        d = {}
        for i, n in enumerate(numbers):
            d[n] = i
        for i, n in enumerate(numbers):
            if target - n in d and d[target - n] != i:
                return [i + 1, d[target - n] + 1]

