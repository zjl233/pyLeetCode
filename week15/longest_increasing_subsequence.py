from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 清洗数据
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        # 使用 dp 数组和 ends 数组
        # dp[i] 的含义：以 nums 中，i 位置结尾，的 LIS 长度最大值
        # ends[i] 的含义：所有长度为 i + 1 的 LIS，尾巴的最小值
        n = len(nums)
        dp = [0 for _ in range(n)]
        ends = [float('inf') for _ in range(n)]

        # 依次取出 nums 中的数，在 ends 中进行二分查找
        # 注意，二分查找时，如果出现相同的数，如 [7, 7, 7] 返回第一个 7 的 idx
        for i, n in enumerate(nums):
            idx = bisect_left(ends, n)
            if n <= ends[idx]:
                ends[idx] = n
                dp[i] = idx + 1
            else:
                ends[idx + 1] = n
                dp[i] = idx + 2

        return max(dp)
