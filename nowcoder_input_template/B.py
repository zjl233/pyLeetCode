'''
A+B(2)

题目描述

计算a+b
输入描述:

输入第一行包括一个数据组数t(1 <= t <= 100)
接下来每行包括两个正整数a,b(1 <= a, b <= 10^9)

输出描述:

输出a+b的结果

示例1
输入

2
1 5
10 20

输出
复制

6
30


'''

i = int(input())

for _ in range(i):
    strs = input().split(" ")
    a, b = int(strs[0]), int(strs[1])
    print(a + b)
