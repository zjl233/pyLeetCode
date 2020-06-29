# 字符串的交错组成问题
# 尝试模型：第三种，两个样本，一个做行，一个做列
# 相似题目，编辑距离
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        h, w = len(s1) + 1, len(s2) + 1
        # dp 中 i, j 指的是 字符串 s1, s2 的长度
        dp = [[False for _ in range(w)] for _ in range(h)]
        # 第一行，s1 为空串，s2 与 s3 一次比较，如果有一个为 False，以后都为 False break
        dp[0][0] = True
        for j in range(1, w):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                break

        for i in range(1, h):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                break

        for i in range(1, h):
            for j in range(1, w):
                dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]
                            or
                            s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])

        return dp[h - 1][w - 1]
