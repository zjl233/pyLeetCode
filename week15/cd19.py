from typing import List


# 排成一条线的纸牌博弈问题
# https://www.nowcoder.com/practice/19c98d950b3347d19f991d10bde12288?tpId=101&&tqId=33159&rp=1&ru=/activity/oj&qru=/ta/programmer-code-interview-guide/question-ranking


def deck_game(nums: List[int]) -> int:
    return first(nums, 0, len(nums) - 1)


# 先手
def first(nums: List[int], l: int, r: int) -> int:
    if l == r:  # 只剩一张牌啦
        return nums[l]

    return max(nums[l] + second(nums, l + 1, r), nums[r] + second(nums, l, r - 1))


# 后手
def second(nums: List[int], l: int, r: int) -> int:
    if l == r:
        return 0

    return min(first(nums, l + 1, r), first(nums, l, r - 1))


def deck_game_dp(nums: List[int]) -> int:
    n = len(nums)
    fdp = [[0] * n for _ in range(n)]
    sdp = [[0] * n for _ in range(n)]

    for i in range(n):
        fdp[i][i] = nums[i]
        sdp[i][i] = 0

    for i in range(1, n):
        r, c = 0, i
        while c < n:
            fdp[r][c] = max(nums[r] + sdp[r + 1][c], nums[c] + sdp[r][c - 1])
            sdp[r][c] = min(fdp[r + 1][c], fdp[r][c - 1])

            r += 1
            c += 1

    return max(fdp[0][n - 1], sdp[0][n - 1])


def oj_main():
    from sys import stdin
    # 用 pypy 和 stdin 更快
    # input 会尝试猜测输入的数据类型

    n = int(stdin.readline().strip())
    ints = list(map(int, stdin.readline().split()))

    res = [1, 2, 3]
    print(' '.join([str(i) for i in res]))

    print(deck_game_dp(ints))


if __name__ == '__main__':
    oj_main()
