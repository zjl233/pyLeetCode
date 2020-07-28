from typing import NamedTuple

from utils.treenode import TreeNode


class Info(NamedTuple):
    # 空节点返回的 info
    blc: bool = True
    h: int = 0


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not TreeNode:
            return True

        info = self.process(root)
        return info.blc

    def process(self, root) -> Info:
        if not root:
            return Info()

        l = self.process(root.left)
        r = self.process(root.right)

        is_blc = l.blc and r.blc and (abs(l.h - r.h) <= 1)
        h = max(l.h, r.h) + 1

        return Info(is_blc, h)

#