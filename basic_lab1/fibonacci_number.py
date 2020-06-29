class Solution:
    def fib_dp(self, N: int) -> int:
        """

        不想写注释了~
        题目地址：
        https://www.nowcoder.com/study/live/348/1/12
        课后作业 1.12

        https://leetcode-cn.com/problems/fibonacci-number
        Python 3.6
        牛客网不支持 Python3，所以到 LeetCode 上写

        time: O(n)
        space: O(n)
        ac: 100%
        """
        if N < 2:
            return N

        dp = [0] * (N + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[N]

    def fib_pythonic(self, N: int) -> int:
        """
        利用 python 特性的写法

        time: O(n)
        space: O(1)
        ac: 100%
        """

        if N < 2:
            return N

        a, b = 0, 1
        for _ in range(2, N + 1):
            a, b = b, a + b

        return b
