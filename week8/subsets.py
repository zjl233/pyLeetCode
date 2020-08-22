from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        path: List[int] = []
        res: List[List[int]] = []
        self.process(nums, 0, path, res)
        return res

    def process(self, nums: List[int], begin: int, path: List[int], res: List[List[int]]) -> None:
        res.append(path.copy())

        for i in range(begin, len(nums)):
            n = nums[i]

            path.append(n)
            self.process(nums, i + 1, path, res)
            path.pop()
