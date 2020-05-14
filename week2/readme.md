# week2

归并，堆排和快排

## 归并排序

为什么比 基础排序算法快，因为没有浪费比较行为

T(N) = 2T(N/2) + O(N) 

经典题目，**每年都出现**


计算数组的小和
https://www.nowcoder.com/practice/edfe05a1d45c4ea89101d936cac32469?tpId=101&&tqId=33089&rp=1&ru=/activity/oj&qru=/ta/programmer-code-interview-guide/question-ranking

套在归并排序里的统计 
 
arr[p1] < arr[p2] 拷贝左边的到 help[i]
要严格小于(还是要看题目，如果定义是小于等于那就小于等于)

1 3 4 | 1 5


数组中的逆序对
https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=13&&tqId=11188&rp=1&ru=/activity/oj&qru=/ta/coding-interviews/question-ranking


## 堆排序

**堆结构**

API

1. void add(num)
2. int popMax()

**完全二叉树**

每一层，从左往右数没有空格

```
0 1 2 3 4 5
      
        0
       / \
      1   2
     / \ / 
    3  4 5

左 2*i+1
右 2*1+2

父 (i-1)/2
```

