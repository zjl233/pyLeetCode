# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import NamedTuple

from utils.treenode import TreeNode


class Info(NamedTuple):
    depth: int = 0
    leaf: bool = False


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        info = self.process(root)
        return info.depth

    def process(self, root: TreeNode) -> Info:
        if not root:
            return Info()
        if not root.left and not root.right:
            return Info(1, True)

        l = self.process(root.left)
        r = self.process(root.right)
        depth = 1 + min(l.depth if l.leaf else float('inf'), r.depth if r.leaf else float('inf'))
        return Info(depth, l.leaf or r.leaf)
