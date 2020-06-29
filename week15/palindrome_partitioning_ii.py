from typing import List

from week15.palindrome_partitioning import is_palindrome


# 返回 is_palindr[i][j] dp
# 从 i 到 j 是否为回文
def is_palindrome_dp(s: str) -> List[List[bool]]:
    if not s:
        raise RuntimeError

    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            # 回文长度为 2
            # 如 aa，是否为回文取决于当前首尾是否相等
            if j - i == 1 and s[i] == s[j]:
                dp[i][j] = True
            # 回文长度大于 2
            # 如 aba, abba，是否为回文取决于去除首尾，中间是否为回文
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]

    return dp


class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        return self.process(s, 0)

    def process(self, s: str, i: int) -> int:
        # 先写 base case
        # 一定要加后面的判断
        if i == len(s) - 1 or is_palindrome(s, i, len(s) - 1):
            return 0

        min_cut = float('inf')
        # partition point
        for j in range(i, len(s)):
            # is_palindr 判断的是 i~p 左闭右闭 是不是回文
            if is_palindrome(s, i, j):
                # s[p+1:] 的最小回文分割
                cut = self.process(s, j + 1)
                min_cut = min(min_cut, cut)

        return min_cut + 1

    def minCutDP(self, s: str) -> int:
        if not s:
            return 0

        is_palindr = is_palindrome_dp(s)
        n = len(s)
        # 从 将 s[:i+1] 分割为回文的最大分割次数是 回文长度 -1
        dp = [i for i in range(n)]
        for j in range(1, n):
            if is_palindr[0][j]:
                dp[j] = 0
                continue
            else:
                dp[j] = min([dp[i] + 1 for i in range(j) if is_palindr[i + 1][j]])

        return dp[-1]
