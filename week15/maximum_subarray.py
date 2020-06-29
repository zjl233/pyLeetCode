from typing import List


class Solution:
    # 一类非常难得思想：假设已经得到正确答案，观察正确答案得数据状况，设计相应得流程，得到符合这个状况得数据
    def maxSubArray(self, nums: List[int]) -> int:
        sum_, max_sum = 0, float('-inf')
        for n in nums:
            sum_ += n
            max_sum = max(max_sum, sum_)

            if sum_ < 0:
                sum_ = 0
        return max_sum
