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
    diameter: int = 0


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        info = self.process(root)
        return info.diameter - 1

    def process(self, root: TreeNode) -> Info:
        if not root:
            return Info()

        l = self.process(root.left)
        r = self.process(root.right)

        depth = 1 + max(l.depth, r.depth)
        diameter = 1 + l.depth + r.depth
        diameter = max(diameter, l.diameter, r.diameter)

        return Info(depth, diameter)
