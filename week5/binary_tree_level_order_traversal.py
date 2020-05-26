from typing import List

from utils.treenode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res: List[List[int]] = []
        if not root:
            return res

        queue = [root]
        while queue:
            level = [node.val for node in queue]
            res.append(level)

            nxt = []
            for node in queue:
                for child in (node.left, node.right):
                    nxt.append(child) if child else None

            queue = nxt

        return res

