# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import NamedTuple

from utils.treenode import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.helper(root, 0)

    def helper(self, root: TreeNode, n: int) -> int:
        if not root:
            return 0

        temp = n * 10 + root.val
        if not root.left and not root.right:
            return temp
        return self.helper(root.left, temp) + self.helper(root.right, temp)
