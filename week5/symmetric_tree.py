from typing import Optional

from utils.treenode import TreeNode


class Solution:
    def isSymmetTric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isSym(root, root)

    def isSym(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:  # 两棵树都
            return True
        if not p or not q:
            return False

        if p.val == q.val:
            return self.isSym(p.left, q.right) and self.isSym(p.right, q.left)
        else:
            return False
