from functools import cmp_to_key
from typing import List

"""
https://www.nowcoder.com/practice/d5d1a56491384b2486480730f78f6da2?tpId=101&&tqId=33198&rp=1&ru=/activity/oj&qru=/ta/programmer-code-interview-guide/question-ranking
题目描述
给定一个字符串的数组strs，请找到一种拼接顺序，使得所有的字符串拼接起来组成的字符串是所有可能性中字典序最小的，并返回这个字符串。
输入描述:
输入包含多行，第一行包含一个整数n（ 1 \leq n \leq 10^5 ）（1≤n≤10 
5
 ），代表字符串数组strs的长度，后面n行，每行一个字符串，代表strs[i]（保证所有字符串长度都小于10）。
输出描述:
输出一行，包含一个字符串，代表返回的字典序最小的字符串。
示例1
输入
复制
2
abc
de
输出
复制
abcde
示例2
输入
复制
2
b
ba
输出
复制
bab

"""


def lowest_order(strs: List[str]) -> str:
    if not strs:
        return ''

    # 直接排序，如果 x + y < y + x，那么 x 排前面
    strs.sort(key=cmp_to_key(lambda x, y: 1 if x + y > y + x else -1))
    return ''.join(strs)


def oj_main():
    # 用 pypy
    n = int(input())
    words = [''] * n
    for i in range(n):
        words[i] = input()
    print(lowest_order(words))


if __name__ == '__main__':
    oj_main()
