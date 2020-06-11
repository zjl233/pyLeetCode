from typing import Optional

from utils.treenode import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        level = [root]
        while level:
            vals = [n.val if n else "#" for n in level]
            if not self.isListSym(vals):
                return False

            level = [kid for n in level if n for kid in (n.left, n.right)]

        return True

    def isListSym(self, vals) -> bool:
        # 为根节点的情况
        # 为什么对之后的层也有效，比如，有一层只有一个节点
        # 因为，把 None 也放进去了，每一层只能有 2n 个数
        if len(vals) == 1:
            return True

        if len(vals) % 2 != 0:
            return False

        h, t = 0, len(vals) - 1
        while h < t:
            if vals[h] != vals[t]:
                return False
            h, t = h + 1, t - 1

        return True
