class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        h, w = len(word1) + 1, len(word2) + 1
        # dp 第一行，第一列是空串
        # dp[i][j] 的意思是 word1[:i] 变到 word2[:j] 需要多少代价，(注: python 中 str[:i] 取不到最后的字符)
        dp = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            dp[i][0] = i
        for j in range(w):
            dp[0][j] = j

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                insert = dp[i][j - 1] + 1
                delete = dp[i - 1][j] + 1
                # 分情况，最后一个字符相等，或者不相等
                replace = dp[i - 1][j - 1] + (1 if word1[i - 1] != word2[j - 1] else 0)
                dp[i][j] = min(insert, delete, replace)

        return dp[h - 1][w - 1]
