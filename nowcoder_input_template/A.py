'''
A+B(1)

计算a+b
输入描述:

输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据包括多组。

输出描述:

输出a+b的结果

示例1
输入
复制

1 5
10 20

输出
复制

6
30
'''

while True:
    try:
        strs = input().split(' ')
        a, b = int(strs[0]), int(strs[1])
        print(a + b)
    except:
        break
