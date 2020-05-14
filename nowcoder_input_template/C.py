# 和 A 一样，不过结束的条件为 0 0

while True:
    strs = input().split(' ')
    a, b = int(strs[0]), int(strs[1])
    if a == 0 and b == 0:
        break
    else:
        print(a + b)
