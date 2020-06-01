from typing import List


# 六一儿童节快乐!
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        if len(candies) == 0:
            return []

        maxc = max(candies)
        res = [c + extraCandies >= maxc for c in candies]
        return res
