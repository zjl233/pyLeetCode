from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lt, gt = -1, len(nums)
        i = 0
        # [:lt] 的是小于
        # [lt:i] 是等于
        # [i:] 是大于

        while i < gt:
            if nums[i] < 1:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                gt -= 1
                nums[gt], nums[i] = nums[i], nums[gt]
