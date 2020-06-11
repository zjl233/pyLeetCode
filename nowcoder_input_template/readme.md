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


```python2
import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print int(lines[0]) + int(lines[1])
except:
    pass
```



