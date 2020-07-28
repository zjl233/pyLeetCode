from typing import NamedTuple

from utils.treenode import TreeNode


class Info(NamedTuple):
    down_path: int = 0
    path: int = 0


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        info = self.process(root)
        return info.path

    def process(self, root) -> Info:
        if not root:
            return Info()

        l = self.process(root.left)
        r = self.process(root.right)

        down_path = root.val + (max(l.down_path, r.down_path) if max(l.down_path, r.down_path) > 0 else 0)
        path = root.val + (l.down_path if l.down_path > 0 else 0) + (r.down_path if r.down_path > 0 else 0)
        path = max(path, l.path if root.left else float('-inf'), r.path if root.right else float('-inf'))

        return Info(down_path, path)

