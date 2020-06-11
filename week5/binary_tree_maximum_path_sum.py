from typing import NamedTuple

from utils.treenode import TreeNode


class Info(NamedTuple):
    sum_: int = float('-inf')
    left_sum: int = 0
    right_sum: int = 0


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        info = self.process(root)
        return info.sum_

    def process(self, root) -> Info:
        if not root:
            return Info()

        l = self.process(root.left)
        r = self.process(root.right)

        from_left = max(max(l.left_sum, l.right_sum), 0)
        from_right = max(max(r.left_sum, r.right_sum), 0)

        left_sum = root.val + from_left
        right_sum = root.val + from_right
        sum_ = root.val + from_left + from_right

        return Info(max(sum_, l.sum_, r.sum_), left_sum, right_sum)
