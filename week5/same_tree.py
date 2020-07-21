# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from utils.treenode import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val == q.val and self.isSame(p, q):
            return True
        else:
            return False

    def isSame(self, p, q):
        if not p and not q:  # 两棵树都消耗完
            return True

        if not p or not q:  # 一棵树消耗完的情况下，一棵树没有消耗完
            return False

        if p.val == q.val:
            return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
        else:
            return False
