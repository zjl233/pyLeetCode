class Solution:
    # TODO 把一种决策过程，通过 dp, 倒退出来
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        h, w = len(text1), len(text2)
        dp = [[0 for _ in range(w)] for _ in range(h)]

        # 初始化，第一列可能从某个位置开始，一直到最后，都是1
        for i in range(h):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            elif i > 0 and dp[i - 1][0] == 1:
                dp[i][0] = 1
        for j in range(w):
            if text1[0] == text2[j]:
                dp[0][j] = 1
            elif j > 0 and dp[0][j - 1] == 1:
                dp[0][j] = 1

        # 注意 dp 2阶段 一般从 1, 1  位置开始
        for i in range(1, h):
            for j in range(1, w):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j - 1],  # 已经形成的最长公共子序列，既不以 i 结尾，也不以 j 结尾
                        # i-1, j-1 可以舍弃，因为 i-1, j 是通过 i-1, j-1 得到的，只可能 >= i-1, j-1
                        dp[i - 1][j],  # 以 j 结尾，不以 i 结尾
                        dp[i][j - 1])  # 以 i 结尾，不以 j 结尾

        return dp[h - 1][w - 1]

