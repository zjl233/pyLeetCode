# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n < 2:
            return n
        # 从0开始，第0项为0，第1项是1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(0))
    print(s.Fibonacci(1))
    print(s.Fibonacci(10))  # 55
