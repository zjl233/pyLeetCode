from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 和 bitwise 无关，这一题就是硬算
        # 0...110 6
        # 0...110 6
        # 0...011 3
        # 0...110 6
        # 从 0..31，上往下，遍历数组
        # 把它们的 1 都加起来，如果不是 3 的倍数，single number 在这一位上是 1
        # res |= i << 1 类似 +

        # 取出右边第 i 位 bit 的方式: (n >> i) & 1
        res = 0
        for i in range(32):
            count = 0
            for n in nums:
                count += (n >> i) & 1
            if count % 3 != 0:
                if i != 31:
                    res |= 1 << i
                else:
                    # python 的 int 不是 32 位
                    # 小例子，假设 int 只有 4 位
                    # 1101 -> 13

                    # 如果最高位是符号为，那么应该是 -3（区翻在加一）
                    # 可以通过 13 - 16 得到
                    # 13 - 1<<4
                    res -= 1 << 31

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([6, 6, 3, 6]))  # 3
    print(s.singleNumber([2, 2, 3, 2]))  # 3
    print(s.singleNumber([0, 1, 0, 1, 0, 1, 99]))  # 99
    print(s.singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]))  # 99
