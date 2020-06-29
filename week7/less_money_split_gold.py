from heapq import heappush, heappop, heapify
from typing import List


def less_money(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    heapify(nums)
    res = 0
    while len(nums) >= 2:
        cmb = heappop(nums) + heappop(nums)
        res += cmb
        heappush(nums, cmb)

    # res += heappop(nums)
    return res


def oj_main():
    # 数字输入 start
    _ = int(input())

    ints = [int(s) for s in input().split()]  # 只留一行

    res = less_money(ints)
    print(res)
    # 数字输入 end


if __name__ == '__main__':
    oj_main()
