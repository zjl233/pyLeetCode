from functools import lru_cache


class Solution:
    @lru_cache
    def integerBreak(self, n: int) -> int:
        # 动态规划，猜测，从左往右
        # 考虑 base case
        if n == 2:
            return 1

        max_ = -1
        for i in range(1, n - 1):
            # 继续拆分 n-i
            split_ = i * self.integerBreak(n - i)
            # 不拆了，直接返回
            not_split = i * (n - i)

            max_ = max(max_, split_, not_split)

        return max_

    def integerBreakDP(self, n: int) -> int:
        # 动态规划，猜测，从左往右
        # 考虑 base case
        if n == 2:
            return 1

        # dp[i] 的含义，就是题意，i 拆分后乘积的最大值
        # dp[n] 就是答案

        dp = [1 for _ in range(n + 1)]
        dp[2] = 1

        # dp 的第二重循环，对应这个循环
        # for i in range(1, n - 1):
        #     # 继续拆分 n-i
        #     split_ = i * self.integerBreak(n - i)
        #     # 不拆了，直接返回
        #     not_split = i * (n - i)
        #
        #     max_ = max(max_, split_, not_split)

        for i in range(3, n + 1):
            for j in range(1, i):
                # 继续拆分 n-i
                split_ = j * dp[i - j]
                # 不拆了，直接返回
                not_split = j * (i - j)
                dp[i] = max(dp[i], split_, not_split)

        return dp[n]

