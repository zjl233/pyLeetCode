# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils.treenode import TreeNode


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:  # 十分奇怪，按理说 null 是任何树的子结构
            return False

        if A.val == B.val and self.almostSame(A, B):  # 现在，已 A B 为根
            return True
        else:  # 重新尝试，B 与 A 的左右节点
            return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def almostSame(self, A: TreeNode, B: TreeNode) -> bool:
        # 必须以 A B 为起点的情况下，B 是不是 A 的子结构
        if not B:  # B 子树消耗完
            return True
        if not A:  # B 子树没有消耗完的情况下，A 子树消耗完了
            return False

        if A.val == B.val:
            return self.almostSame(A.left, B.left) and self.almostSame(A.right, B.right)
        else:
            return False
