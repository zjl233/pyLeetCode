from typing import List


# README 里有详细解释

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 边界情况
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m - 1] < nums[m] and nums[m + 1] < nums[m]:
                return m
            elif nums[m - 1] > nums[m]:
                r = m - 1  # 可能有门题
            else:
                l = m + 1  # 可能有门题

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([1, 2, 3, 1]))
    print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
