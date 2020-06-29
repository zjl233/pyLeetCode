from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        题目地址：
        https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/

        https://www.nowcoder.com/study/live/348/2/13
        牛客网只能由 python2，所以到 LeetCode 上做了

        题型：
        好像没有办法归类耶~

        解题思路：
        如果数组`已经排好序`，
        那么从左向右遍历，目前为止的最大值 max_，小于等于将来遇到的值
        从右往左遍历，目前为止的最小值 min_, 大于等于将来遇到的值
        逆序数组刚好相反
        2 (6 4) 8 (10 9) 15

        参考：
        https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/264474/Python-O(n)-2-Loops-and-O(1)-space

        time: O(n)
        space: O(1)
        ac: 100%
        """

        # 洗数据
        if not nums:
            return 0
        if len(nums) == 1:
            return 0

        # 无序数组的结尾
        end = 0
        # 目前为止的最大值
        max_ = nums[end]
        for i, n in enumerate(nums):
            # 每次遇到逆序的数字，将结尾更新到遇到的逆序数字上
            if max_ > n:
                end = i
            max_ = max(max_, n)

        # 无序数组的开头
        start = len(nums) - 1
        # 目前为止的最小值
        min_ = nums[start]
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            # 每次遇到逆序的数字，将开头更新到遇到的逆序数字上
            if min_ < n:
                start = i
            min_ = min(min_, n)

        # 返回无序数组的长度
        if end != 0:
            return end - start + 1
        else:
            return 0
