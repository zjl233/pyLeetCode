class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]

        i2 = i3 = i5 = 0
        for i in range(n):
            v = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
            dp.append(v)

            if v == dp[i2] * 2:
                i2 += 1
            if v == dp[i3] * 3:
                i3 += 1
            if v == dp[i5] * 5:
                i5 += 1

        return dp[n - 1]
