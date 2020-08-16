from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res: List[List[int]] = []
        self.process(nums, 0, res)
        return res

    def process(self, nums: List[int], x: int, res: List[List[int]]) -> None:
        if x == len(nums) - 1:
            res.append(nums.copy())
            return

        # 如果在这一位上，出现过相同的数字，就 continue
        seen = set()
        for i in range(x, len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])

            nums[i], nums[x] = nums[x], nums[i]
            self.process(nums, x + 1, res)
            nums[i], nums[x] = nums[x], nums[i]

