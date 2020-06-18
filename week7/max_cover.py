"""

链接：https://www.nowcoder.com/questionTerminal/b95092d4a288475c9f2a0163283e1c8b
来源：牛客网

有一个长度为m的数轴，现在有n个区间，每个区间有一个左右端点，现在需要选择最少的区间，覆盖整个数轴。


输入描述:
第一行两个整数n和m。
接下来n行，每行两个整数，表示区间。


输出描述:
输出最少的区间个数，覆盖整个数轴。如果无法覆盖，输出-1。
n，m不超过100000，区间端点的范围[1,m]。
示例1
输入
5 6
1 3
2 4
3 5
5 6
1 4
输出
2

"""
from typing import List


def max_cover(nums: List[int], rng: int) -> int:
    # 差分
    diff = [x - nums[i - 1] for i, x in enumerate(nums)][1:]
    # 下面三行，包括 while 里面的 if else 判断，都是套路
    # [l, r) 左闭右开
    # r 增加，rng -= nums[r]
    # l 增加，rng += nums[r]
    l, r = 0, 0
    cover = -1
    while r < len(diff):
        if rng >= diff[r]:
            rng -= diff[r]
            r += 1
            cover = max(cover, r - l)
        else:
            if l == r:
                l, r = l + 1, r + 1
            else:
                rng += diff[l]
                l += 1
    return cover + 1 if cover != -1 else cover

