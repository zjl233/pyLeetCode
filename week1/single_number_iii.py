from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # readme 里有解题步骤
        a_xor_b = 0
        for n in nums:
            a_xor_b ^= n
        right_bit = a_xor_b & (~a_xor_b + 1)

        a = 0
        for n in nums:
            # 类似于 hash 分桐操作
            if right_bit & n == 0:
                a ^= n

        b = a_xor_b ^ a

        return [a, b]


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 2, 1, 3, 2, 5]))
