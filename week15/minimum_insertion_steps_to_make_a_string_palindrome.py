class Solution:
    def minInsertions(self, s: str) -> int:
        # 洗数据
        if not s:
            return 0
        if len(s) == 1:
            return 0

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # 填对角线
        for x in range(n):
            dp[x][x] = 0
        # 填对角线旁边的位置
        r, c = 0, 1
        while r < n - 1:
            if s[r] == s[c]:
                dp[r][c] = 0
            else:
                dp[r][c] = 1
            r, c = r + 1, c + 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                # 字符串首尾相等，直接将这个字符串的首尾添加到已经形成的回文串
                # 字符串首尾不等，先尝试将 L+1, R 或 L, R-1，变成回文
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

