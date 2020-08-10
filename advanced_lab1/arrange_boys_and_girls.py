def arrange(s: str) -> int:
    """
    题目地址：
    https://www.nowcoder.com/study/live/350/2/4
    2.4 课后作业1-调整队形
    pypy 3.6.1

    解题思路：
    将所有 B 移动到最左边或最右边，需要多少代价
    返回最少的代价
    """
    # 当前所有 B 的 index 和
    sum_ = 0
    # 当前 B 的 个数
    b = 0
    for i, ch in enumerate(s):
        if ch == 'B':
            sum_ += i
            b += 1

    # B 都在左边时，index 和，等差数列
    sum_l = (b * (b - 1)) // 2
    # B 都在右边时，index 和
    sum_r = (b * (len(s) - b + len(s) - 1)) // 2

    return min(sum_r - sum_, sum_ - sum_l)


def oj_main():
    # 字符输入 start
    word = input()
    res = arrange(word)
    print(res)
    # 字符输入 end


if __name__ == '__main__':
    oj_main()

#