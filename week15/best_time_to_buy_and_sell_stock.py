from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        删除<<>>里面的文字，包括<<>>本身

        放置位置：
        每个函数的函数名下面，这样按 Ctrl-Q 的时候，就可以看到注释了
        (删除包括这一行及以上的注释)

        题目地址：
        <<LeetCode 或 牛客网地址>>
        <<注：牛客网不支持 Python3，也不支持 Python2，只能拿 Java 写了>>

        题型：
        <<链表，树，图，树形dp，[从左往右, L..R范围尝试，一个样本做行一个样本做列，条件不够业务来凑]的dp，好像没有办法归类耶~>>

        解题思路：
        <<用通俗易懂的话来描述解题思路。嗯，这个太宽泛了，需要换成更加具体的提示，至少提供简单的参考>>
        <<
        题解示例：
        如果数组`已经排好序`，
        那么从左向右遍历，目前为止的最大值 max_，小于等于将来遇到的值
        从右往左遍历，目前为止的最小值 min_, 大于等于将来遇到的值
        逆序数组刚好相反
        2 (6 4) 8 (10 9) 15
        >>

        参考：
        <<大佬的代码链接。如果无法精准定位，比如一页几十个评论的评论风格，使用链接 + @id 的方式定位>>

        time: O(n log n, n^2, 2^n)
        space: O(n log n, n^2, 2^n)
        ac: 100%
        """

        # 洗数据
        if not prices:
            return 0
        if len(prices) == 1:
            return 0

        lowest = prices[0]
        max_profit = 0
        # i 位置必须卖掉，那么买入时机就是 0~i 位置上的最小值，包括i
        for price in prices:
            lowest = min(lowest, price)
            max_profit = max(max_profit, price - lowest)

        return max_profit
