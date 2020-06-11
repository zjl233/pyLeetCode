from typing import NamedTuple

from utils.treenode import TreeNode


class Info(NamedTuple):
    max_depth: int = 0


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        info = self.process(root)
        return info.max_depth

    def process(self, root) -> Info:
        if not root:
            return Info()

        l = self.process(root.left)
        r = self.process(root.right)

        max_depth = 1 + max(l.max_depth, r.max_depth)

        return Info(max_depth)


