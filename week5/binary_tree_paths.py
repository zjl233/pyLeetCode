from typing import List, NamedTuple

from utils.treenode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Info(NamedTuple):
    paths: List[List[int]] = []


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        info = self.process(root)
        paths = info.paths
        res = ["" for i in range(len(paths))]
        for i, path in enumerate(paths):
            res[i] = "->".join([str(n) for n in path])
        return res

    def process(self, root: TreeNode) -> Info:
        if not root:
            return Info()

        # 是根节点
        if not root.left and not root.right:
            return Info([[root.val]])

        l = self.process(root.left)
        r = self.process(root.right)
        for path in l.paths:
            path.insert(0, root.val)
        for path in r.paths:
            path.insert(0, root.val)

        paths = l.paths + r.paths
        return Info(paths)
