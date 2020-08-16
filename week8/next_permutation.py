from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 找到比 nums 大的数中，最小的数
        if not nums or len(nums) == 1:
            return

        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i, j = i - 1, j - 1

        if i >= 0:
            while nums[i] >= nums[k]:
                k = k - 1

            nums[i], nums[k] = nums[k], nums[i]

        l, r = j, len(nums) - 1

        nums[l:r+1] = nums[l:r+1][::-1]

