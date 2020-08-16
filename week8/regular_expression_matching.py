class Solution:
    # 动态规划，行，列模型
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        return self.process(s, i, p, j)

    # i, j 的变动范围时 0~len(s), 0~len(p)
    def process(self, s: str, i: int, p: str, j: int):
        if i == len(s) and j == len(p):
            return True

        # p 耗尽，s 一定得耗尽
        if j >= len(p):
            return i >= len(s)
        # s 和 p 都耗尽了

        # s 耗尽
        if i >= len(s):
            # s = ""
            # p = a*b*c*
            if j + 1 < len(p) and p[j + 1] == "*":  # p 未耗尽，但可以 * 取零
                return self.process(s, i, p, j + 2)

            return False

        if j + 1 < len(p) and p[j + 1] == "*":
            if s[i] == p[j] or p[j] == ".":
                return self.process(s, i + 1, p, j) or self.process(s, i, p, j + 2)
            else:
                return self.process(s, i, p, j + 2)
        else:
            if s[i] == p[j] or p[j] == ".":
                return self.process(s, i + 1, p, j + 1)

        return False

    def is_match_dp(self, s: str, p: str) -> bool:
        h, w = len(s), len(p)
        dp = [[False for _ in range(w + 1)] for _ in range(h + 1)]

        # 填写最后两列与最后一行
        dp[h][w] = True
        # for i in range(h):
        #     dp[i][w] = False

        dp[h - 1][w - 1] = (s[h - 1] == p[w - 1]) or p[w - 1] == "."

        for j in range(w - 2, -1, -1):
            if p[j + 1] == ".":
                dp[h][j] = dp[h][j + 2]

        for i in range(h - 1, -1, -1):
            for j in range(w - 2, - 1, -1):
                if p[j + 1] == "*":
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i + 1][j] or dp[i][j + 2]
                        # return self.process(s, i + 1, p, j) or self.process(s, i, p, j + 2)
                    else:
                        dp[i][j] = dp[i][j + 2]
                        # return self.process(s, i, p, j + 2)
                else:
                    if s[i] == p[j] or p[j] == ".":
                        dp[i][j] = dp[i + 1][j + 1]
                        # return self.process(s, i + 1, p, j + 1)

        return dp[0][0]
