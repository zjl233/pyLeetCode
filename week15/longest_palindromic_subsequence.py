from functools import lru_cache


def longest_palindrome_subsequence_brute_recursive(s: str) -> int:
    if not s:
        return 0

    n = process(0, len(s) - 1, s)
    return n


@lru_cache(None)
def process(i, j, s):
    if i > j:
        return 0
    if i == j:
        return 1

    if s[i] == s[j]:
        return process(i + 1, j - 1, s) + 2
    else:
        return max(process(i + 1, j, s), process(i, j - 1, s))


class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        n = len(s)
        # dp[i][j] 的含义是：s[i:j+1] 的最长回文子序列
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        r = 0  # 斜线，从左往右遍历的起始位置
        for c in range(1, n):
            i, j = r, c
            while i < n and j < n:
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                i, j = i + 1, j + 1

        return dp[0][n - 1]
