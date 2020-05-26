from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        lbd = self.left_bound(nums, target)
        rbd = self.right_bound(nums, target)

        return [lbd, rbd]

    def left_bound(self, nums: List[int], target: int):
        if len(nums) == 0:
            return -1

        l, r = 0, len(nums) - 1
        # 最后结束时 r < l
        #    r, l
        #       [....]
        #    r, l
        # [..]
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1

        if l <= len(nums) - 1 and nums[l] == target:
            return l
        else:
            return -1

    def right_bound(self, nums: List[int], target: int):
        if len(nums) == 0:
            return -1

        l, r = 0, len(nums) - 1
        # 最后结束时 r < l
        #    r, l
        #       [....]
        #    r, l
        # [..]
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1

        if r >= 0 and nums[r] == target:
            return r
        else:
            return -1
