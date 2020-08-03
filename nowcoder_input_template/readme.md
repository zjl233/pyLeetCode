# 牛客网输入测试

## OJ在线编程常见输入输出练习场
https://ac.nowcoder.com/acm/contest/5646?from=hr_test#question
## 牛客网在线判题系统使用帮助 
https://www.nowcoder.com/discuss/276

```python
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
```


```python
import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print(int(lines[0]) + int(lines[1]))
except:
    pass
```


```python
def solution(a):
    ...


def oj_main():
    # 数字输入 start
    n = int(input())    

    ints = [int(s) for s in input().split()]  # 只留一行
    ints = [int(input()) for _ in range(n)]  # 只留一行

    ints_res = solution(ints)
    print(' '.join([str(i) for i in ints_res]))
    # 数字输入 end

    # 字符输入 start
    n = int(input())
    words = input().split()  # 只留一行
    words = [input() for _ in range(n)]  # 只留一行

    words_res = solution(words)
    print(' '.join(words_res))
    # 字符输入 end


if __name__ == '__main__':
    oj_main()

```
