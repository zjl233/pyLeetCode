# 求 1+2+...+n ，要求不能使用乘除法

class Solution:
    def sumNums(self, n: int) -> int:
        # n * (n + 1) / 2
        res = self.russia_mul(n, n + 1)
        res >>= 1
        return res

    def russia_mul(self, a: int, b: int) -> int:
        # 最多支持 10000 以内的数字相称，也就是 最多，第 14 为 bit 为1
        # 所以要展开 14 次
        res = 0

        res += b & 1 and a  # 如果 b 的最低 bit 为一，那么后面表达式返回 a，神奇
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        res += b & 1 and a
        a <<= 1
        b >>= 1

        return res
