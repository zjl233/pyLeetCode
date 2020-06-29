from typing import List

def score_diff(nums: List[int]) -> int:
    """
    题目地址：
    https://www.nowcoder.com/study/live/350/2/5
    课后作业2-纸牌游戏
    pypy 3.6.1

    解题思路：
    这一题和老师讲的”纸牌游戏“不是同一类题目，被惯性思维带偏了，
    纸牌随便拿，所以每个人都会拿当前的最大值，
    所以卡组从大到小排序，每个人轮流拿一张

    """
    nums.sort(reverse=True)
    # 如果数组长度为奇数，末尾补一个0。让数组始终为偶数
    # 这样下面的循环就可以写得很爽了
    if len(nums) % 2 != 0:
        nums.append(0)

    diff = 0
    # 每一次的差值累计
    for i in range(0, len(nums), 2):
        diff += nums[i] - nums[i + 1]

    return diff


def oj_main():
    # 数字输入 start
    _ = int(input())
    ints = [int(s) for s in input().split()]

    int_res = score_diff(ints)
    print(int_res)
    # 数字输入 end


if __name__ == '__main__':
    oj_main()


