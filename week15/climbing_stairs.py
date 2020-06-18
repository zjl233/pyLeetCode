class Solution:
    # O(n)
    def climbStairs(self, n: int) -> int:
        # 斐波那契数列
        if n < 2:
            return 1

        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b

        return b

    def climbStairsMath(self, n: int) -> int:
        # 矩阵快速幂
        if n < 2:
            return 1

        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b

        return b
