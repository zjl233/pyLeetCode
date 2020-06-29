def solution(s: str) -> str:
    """
    题目地址：
    https://www.nowcoder.com/study/live/348/2/12
    课后作业 2.12
    pypy 3.6.1

    参考：
    评论区的带佬，这一题只用比较器好像做不出来

    time: O(m)
    space: O(n)
    ac: 100%
    """
    # 将 str 转成 数组
    chs = [ch for ch in s]
    # 将 str 转成 数组，里面的只包含英文字母
    alphas = [ch for ch in s if str.isalpha(ch)]
    # 将 alphas 排序，大小写不敏感
    alphas.sort(key=str.casefold)
    # 将排序后的 alphas 填回原数组，遇到非英文字母就跳过
    j = 0  # 指向 chs 的指针
    for i, alpha in enumerate(alphas):
        while not str.isalpha(chs[j]):
            j += 1
        chs[j] = alphas[i]
        j += 1

    return ''.join(chs)


def oj_main():
    line = input()
    res = solution(line)
    print(res)


if __name__ == '__main__':
    # 多用例输入
    # 单用例也可以用
    while True:
        try:
            oj_main()
        except EOFError:
            break
