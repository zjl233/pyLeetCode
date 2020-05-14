# -*- coding: utf-8 -*-
# 写中文注释需要加上这一行

# python2 需要将 python3 中的所有 input() 换成 raw_input()
i = int(input())
desc = int(input()) == 0
table = []

for _ in range(i):
    strs = input().split(" ")
    name, score = strs[0], int(strs[1])
    table.append([name, score])

# sorted() 会产成新数组，list.sort() 原地排序
table.sort(key=lambda student: student[1], reverse=desc)

# python2 中的 print 是和 if for  一样的语句
for name, score in table:
    print(name, score)
