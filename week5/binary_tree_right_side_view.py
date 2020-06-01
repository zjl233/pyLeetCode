from typing import List

from utils.treenode import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res: List[int] = []
        if not root:
            return res

        level = [root]
        while level:
            res.append(level[-1].val)
            level = [kid for n in level for kid in (n.left, n.right) if kid]

        return res
