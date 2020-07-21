# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List, NamedTuple

from utils.treenode import TreeNode


class Info(NamedTuple):
    paths: List[List[int]] = []


class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root:
            return []

        info = self.process(root, sum_)
        return info.paths

    def process(self, root: TreeNode, remain: int) -> Info:
        if not root:
            return Info()

        # 叶子节点，返回自身
        if not root.left and not root.right:
            if root.val == remain:
                return Info([[root.val]])

        # 非叶子节点，如果左右节点的paths 不为空，那么将 root.val 分别加入到前面
        lif = self.process(root.left, remain - root.val)
        rif = self.process(root.right, remain - root.val)

        paths: List[List[int]] = []
        if lif.paths:
            for path in lif.paths:
                paths.append([root.val] + path)
        if rif.paths:
            for path in rif.paths:
                paths.append([root.val] + path)

        return Info(paths)
