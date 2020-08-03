# week13

morris 遍历，面试装逼用，可以将空间复杂度降低到 O(1)

适用题目，不需要第三次回到节点。

比如
```
l = process(root.left)
r = process(root.right)

...root 拿到左右节点数据后，进行一顿操作

```
这种题目，就不适用

这个文件夹内，使用 morris 重写题目

判断搜索二叉树