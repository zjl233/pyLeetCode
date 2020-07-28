# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from utils.treenode import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]

        return self.process(1, n)

    def process(self, start: int, end: int) -> List[Optional[TreeNode]]:
        if start > end:
            return [None]

        res: List[TreeNode] = []
        for i in range(start, end + 1):
            left_list = self.process(start, i - 1)
            right_list = self.process(i + 1, end)
            for left in left_list:
                for right in right_list:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res

