from typing import NamedTuple

from utils.treenode import TreeNode


class Info(NamedTuple):
    depth: int = 0


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        info = self.process(root)
        return info.depth

    def process(self, root: TreeNode) -> Info:
        if not root:
            return Info()

        lif = self.process(root.left)
        rif = self.process(root.right)

        depth = 1 + max(lif.depth, rif.depth)

        return Info(depth)
