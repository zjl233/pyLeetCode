# week1

https://www.nowcoder.com/study/live/348/1/5

时间复杂度，空间复杂度

## 基础排序 

选择排序，冒泡排序，插入排序

(如无特殊说明，有序指的都是升序)

先判断数组是否为空，以及长度是否大于0

**选择排序**

i: 0...n-1

遍历 i...n-1 找到 minIdx

交换 minIdx 和 i

**冒泡排序**

01 12 23 ... n-2 n-1 两两比较，> 的话，swap
01 12 23 ... n-2 n-3 两两比较...

**插入排序**

最有技巧的

i: 0...n-1

// 看 0..0 是否有序
// 看 0..1 是否有序
// 看 0..2 是否有序
// 看 0..3 是否有序
// 看 0..i 是否有序

判断有序的方法

比较 i-1 和 i，如果 >，一直交换到 i 到(目前)应该在的位置
```java
for(int j = i; j >= 1 && arr[j-1] > arr[j]; j--) {
    swap(arr, j-1, j)
}
```

因为 0...i-1 都是有序的，可能 arr[i] > arr[i-1]， 比较一次就结束了

为什么插入排序优于选择排序和冒泡排序：

选择排序和冒泡排序的时间复杂度与数据状况无关，

而插入排序不同，如果原始数据是有序的，并不会跑的第二个循环(只是摸一下第二个循环的判断条件)

最好时间复杂度 O(n)

## 二分法

**变体问题**

https://www.nowcoder.com/study/live/348/1/6
6:30

111111 2222 333333 444444
       |
       
求 刚好 <= 2 的位置

二分到没有数字，用一个全局变量记录成功的数字

https://www.nowcoder.com/study/live/348/1/6
14:30

**求任意的局部最小值**

162. Find Peak Element
https://leetcode.com/problems/find-peak-element/
和老师讲的正好相反，局部最大值

局部最小的定义

[0] < [1]
[n-1] < [n-2]

[i-1] > [i] < [i+1]

arr 无序，且无重复的数字

先比较 [0] <? [1], [n-1] <? [n-2]
如果为真，则返回
如果不为真，那么中间一定存在拐点

 \            /
0  1 ...   n-2 n-1
既然头尾有上升，有下降，那么中间必然有拐点

然后到中间找

 \         \/         /
0  1   m-1 m m+1   n-2 n-1

这个样子，返回 m

 \        /           /
0  1   m-1 m m+1   n-2 n-1

这个样子，到 1 和 m-1 中间找

 \          \         /
0  1   m-1 m m+1   n-2 n-1
同理


## 异或的性质

1. 0^n = n n^n = 0
2. 异或操作满足交换率，结合率
3. 不用额外变量，交换两个数字
4. 数组中，一种数出现了奇数次，其他数都出现了偶数次，求这个数
136. Single Number

5. 数组中，两种数出现了奇数次，其他数都出现了偶数次，求这个两数
260. Single Number III
如何记：无进位相加

提取最右的1

010010101000
->
000000001000

n&(~n+1) // 直接记就可以了

## 递归复杂度计算公式 master 

T(N) = aT(N/b) + O(N^d)

b: 每一次调用，规模缩小 b
a: 调用 a 次

如

```python
def process(nums, l, r):
    if len(nums) == 0:
        return
    m = (l + r) // 2
    process(nums, l, m)
    process(nums, m+1, r)

# T(N) = 2T(N/b) + O(1)
# 调用自身2次
# 每次调用，数据规模变为 1/2
```

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

为什么，经典归并排序时，arr[p1] arr[p2] 

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

大根堆：每一棵子树的最大值，都是子树的头节点

练习题

一个几乎有序的数组，几乎有序是指，一个数现在的位置，与它排好序的位置，相差的距离不超过 k

申请一个容量为 k+1 的小根堆，每次弹出最顶部的数，并且加入一个新的数

**注**

贪心算法大量用到堆

## 快排

荷兰国旗问题

leetcode 75 sort colors

https://leetcode.com/problems/sort-colors/

-1          n
 <区  [  ] >区
        |
        当前()
<区 .... 当前 间为 =区
        
1. 当前值 < 划分值，当前值与 <区 的下一个 swap，当前++，<区++
2. 当前值 = 划分值，当前++
3. 当前值 > 划分值，当前值与 >区 的下一个 swap，当前不动(因为刚挪过来的数还没看过)，>区--，

情况 1 时，想象一下，推书架里的书

当前 > >区终止

# week3

## 比较器

比较两个数 o1 o2，
如果返回负数，o1 排在前面
如果返回正数，o2 排在前面
如果返回0，o1 o2 排在前面都可以


### 排序算法小结

| name | time | space | stable |
| ---- | ---- | ----- | ------ |
|   冒泡、选择、插入        |  O(n^2)      | O(1) | 选择不是  |
下面3 个最重要
|    归并            |   O(nlogn)   | O(n) | 是  | 
|    快排            |   O(nlogn)   | O(logn) | 否  |
|    堆排序          |  O(nlogn)    | O(1) | 否  |

桶排思想
|   桶排序           |   O(n)      | O(n) | 取决于桶内排序算法  | 
|   计数排序         | O(n+r)         | O(n+r) |  是 | r 一般很小
|   基数排序         | l*排序算法         | 排序算法 |  是 |  l一般很小
如果用上面的 计数排序    l*O(n+1)           O(n+r)



冒泡、选择、插入 这三种排序里，最好的是 插入排序，在数据状况最优的情况下，时间复杂度为O(n)，因为只需要 摸一下第二重循环的判断条件，不需要进去跑
快排的最坏时间复杂度为 O(n^2)

三个最重要的排序，快排的常数时间最优，做实验做出来的
堆排：追求额外空间少
归并：追求稳定

当然，快排的调用栈需要记录每一次 分裂时 p 的位置，也就是要记录 高度个 p， 为 O(logn)
计数排序是特殊的桶排序，一般用于区间较小，如高考成绩的排序


### 桶排序的两种实现思路: 写得有问题

**一般桶用链表**

优点：记录了入桶子顺序，稳定

流程，原数组 -> buckets -merge-> 原数组 

3 * O(n)

**桶用数组**


k 个木桶，每个桶用快排 k * (n/k)log(n/k)


### 计数排序实现稳定的技巧

得到区间右边界，从 原始数组 的右边复制数据到 help 数组，
             
考试成绩 [A C B D A C C D]
               |       |
               王      张

       A  B  C  D
counts[2, 1, 3, 2]
counts[i] = counts[i] + counts[i-1]

counts[2, 3, 6, 8] 得到所有区间的右边界 
        ,max)s

从右边开始，遍历原始数组，摸到  D-张
help[--counts['D'-'A']] = D-张
现在 counts[2, 3, 6, 7]

### 基数排序

[001, 000, 009, 011, 022, 100]

首先，找到最大值100，3位，其他数字不足补0

先按照个位排

00[0] 10[0] 00[1] 01[1] 02[2] 00[9]

0[0]0 1[0]0 0[0]1 0[0]9 0[1]1 0[2]2

[0]00 [0]01 [0]09 [0]11 [0]22 [1]00

因为数字的权重在最高位，所以要最后排，最高位

每次排序都要使用稳定排序算法，让上一次的排序传递下去

基数排序的时间复杂度取决于要排序的 元素长度 和 稳定排序算法 的复杂的


如果元素长度为 l，选桶排序，那么时间复杂度为 l * O(n+r)，l 一般非常小

空间 O(n+r)

上面的排三位数
time: 3 * O(n+10)
space: O(n+10)


### 实现稳定排序算法需要注意细节和不稳定算法的返例

#### 选择排序 不稳定 的例子

[5 5 5 5 3 5 5 5]
 张 王

第一轮
[3 5 5 5 5...]
   王    张

#### 冒泡排序 稳定

只要在两个数相等时，不 swap 就稳定

#### 插入排序 稳定

```
1 2  3 3
     <-
     break
```
和左边的数相等

#### 归并排序 稳定

arr[p1] == arr[p2] 时，先将左边的填入 help[]

例子:
数组只有两个数，使用归并排序
   [9, 9]
   王  张

#### 堆排 不稳定
 
[5, 4, 4, 6] heapify
    王 张

        5
       / \
   王 4   4 张
     /
    6

heapify()

        6
       / \
      5   4 张
     /
  王 4

[6, 5, 4, 4]
       张 王

#### 快排 不稳定

划分值 4
[6 6 6 6 3]
 王    张

[3 6 6 6 6]
       张 王   

#### 桶排序 稳定

桶用链表，记录进桶的顺序


### 一些大坑

1. “原地归并” 不需要掌握，因为会让时间复杂度变为 O(n^2)
2. 神坑题：奇数放左边，偶数放右边，且稳定。(快排的partition过程，快排作者也做不到)


# week4

## java 按值传递，还是引用传递

```java
Obj o = new Obj()
// o 是引用，也就是指针, 0xheap

map.put(o) 
// 存的是指针 0xheap，所以不管 o 有多大，o都是固定的 8 byte

// 但 String Float Integer 则完全不同
String s = new String("very very long...")
// s 也是指针，假设为 oxaddr

map.put(s)
// 现在 map 里存的不是 oxaddr，而是 "very very long..."

```

```
# 一种典型的内存泄露
global_map = {} # 生存周期特别长 

def f(): # 生存周期较短，且调用频繁
    global_map['k'] = 'v'
    # 函数结束前，没有 del global_map['k']
    # 现在 'k' 会一直存在于 global_map ℹ里
    # 如果 f() 被频繁调用，就会内存泄漏
```

## sorted map 实现

红黑树，avl 树，跳表，SB 树...

红黑树已经差不多被淘汰了，太难实现，但 Java C++ 这两个大象 还在用

所有操作的时间复杂度都是 O(logn)

## 链表题方法论

笔试：一切为了时间复杂度，能用 map 就用 map
面试：还是时间复杂度，但是注意要省空间

所以，笔试时可以偷鸡就偷鸡

题目

判断链表是否为回文结构:
nowcoder: https://www.nowcoder.com/practice/4b13dff86de64f84ac284e31067b86e2?tpId=101&tqId=33179&tPage=1&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking
leetcode: 234. Palindrome Linked List

partition 链表:
https://www.nowcoder.com/practice/04fcabc5d76e428c8100dbd855761778?tpId=101&tqId=33181&tPage=1&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking
86. Partition List

复制含有随机节点🙈的链表：
leetcode: 138. Copy List with Random Pointer

**判断链表是否有环的一系列问题（非常重要！！！）**：

做这种题目的时候，最大的阻碍是脑部很多不存在的结构
比如
```
     O   O
      \ /
       O  不可能存在这种结构，因为 ListNode 只有一个 next
      / \
     O   O
    
     O   O
      \ /
       O  只可能是 Y 字型
       |
       |

     O   
      \ 
       O  或者另一个分叉的长度为零
       |
       |

```     

找到两个`无环`链表的相交节点：
160. Intersection of Two Linked Lists


找到两个`可能有环`链表的相交节点：
160 的升级版本

先分别判断两个链表是否有环，再分类讨论


百度云里有代码


笔试用投机的方法做一下