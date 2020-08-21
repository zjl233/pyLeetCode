from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        path: List[int] = []
        res: List[List[int]] = []
        self.process(nums, path, k, res)

        return res

    def process(self, nums: List[int], path: List[int], k: int, res: List[List[int]]) -> None:
        if len(path) == k:
            res.append(path.copy())
            return

        for i in range(len(nums)):
            n = nums[i]

            path.append(n)
            self.process(nums[:i] + nums[i + 1:], path, k, res)
            path.pop()

