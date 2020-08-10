from typing import List

from utils.treenode import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True

        if not s or not t:
            return False

        if s.val == t.val:
            return self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right)
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

