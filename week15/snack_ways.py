from typing import List

"""
https://www.nowcoder.com/practice/bf877f837467488692be703735db84e6?tpId=182&&tqId=34326&rp=1&ru=/activity/oj&qru=/ta/exam-all/question-ranking
题目描述
牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。
输入描述:
输入包括两行
第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。
输出描述:
输出一个正整数, 表示牛牛一共有多少种零食放法。
示例1
输入
复制
3 10
1 2 4
输出
复制
8
说明
三种零食总体积小于10,于是每种零食有放入和不放入两种情况，一共有2*2*2 = 8种情况。
"""


# 这一题用递归可过，用 dp 反而过不了
# n: 零食数量 b: 背包大小
# 递归, time: O(2^n)  space: O(n)
# dp,   time: O(nb)  space: O(nb) 空间压缩后 space: O(b)
# 背包问题，再零食数量较少时用 递归，在背包数量较少时用 dp
def snack_brute(bag: int, snacks: List[int]) -> int:
    # 洗数据
    # 背包可以装下所有零食的情况
    if sum(snacks) <= bag:
        return 2 ** len(snacks)

    res = process(bag, snacks, 0)
    return res


def process(remain: int, snacks: List[int], idx: int) -> int:
    # 提前结束，为了时间复杂度
    if remain < 0:
        return 0

    if idx == len(snacks):
        return 1

    ways = 0
    ways += process(remain, snacks, idx + 1)
    ways += process(remain - snacks[idx], snacks, idx + 1)

    return ways


# 写 dp 的时候，不要想 dp[i][j] 的含义。就把 dp 数组看成 递归 的加速器就可以了。

# 1. 变化的参数，以及 变动的范围
# 2. 位置依赖
# 3. 最终返回

# 1 <= bag <= 2 * 10^9, bag 范围太大了，空间压缩
def snack_dp(bag: int, snacks: List[int]) -> int:
    # 1. idx: 0~len(snacks) remain 0~bag
    # 2. [idx][remain] = [idx+1][remain] + ([idx+1][remain-snacks[idx]] if remain-snacks[idx] > 0)
    # 3. [0][bag]
    dp = [[0 for _ in range(bag + 1)] for _ in range(len(snacks) + 1)]
    for remain in range(bag + 1):
        dp[len(snacks)][remain] = 1

    for idx in range(len(snacks) - 1, -1, -1):
        for remain in range(bag + 1):
            dp[idx][remain] = dp[idx + 1][remain] + \
                              (dp[idx + 1][remain - snacks[idx]] if remain - snacks[idx] >= 0 else 0)

    return dp[0][bag]


# 1 <= bag <= 2 * 10^9, bag 范围太大了，空间压缩
def snack_dp2(bag: int, snacks: List[int]) -> int:
    # 洗数据

    if sum(snacks) <= bag:
        return 2 ** len(snacks)

    # 1. idx: 0~len(snacks) remain 0~bag
    # 2. [idx][remain] = [idx+1][remain] + ([idx+1][remain-snacks[idx]] if remain-snacks[idx] > 0)
    # 3. [0][bag]

    dp_prev = [1 for _ in range(bag + 1)]

    for idx in range(len(snacks) - 1, -1, -1):
        dp_cur = [0 for _ in range(bag + 1)]
        for remain in range(bag + 1):
            dp_cur[remain] = dp_prev[remain] + \
                             (dp_prev[remain - snacks[idx]] if remain - snacks[idx] >= 0 else 0)
        dp_prev = dp_cur

    return dp_prev[bag]


def oj_main():
    # 数字输入 start ===========================
    n, b = [int(s) for s in input().split()]
    snks = [int(s) for s in input().split()]
    res = snack_brute(b, snks)
    print(res)


if __name__ == '__main__':
    oj_main()
