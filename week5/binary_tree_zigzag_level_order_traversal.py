from typing import List

from utils.treenode import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res: List[List[int]] = []
        if not root:
            return res

        level = [root]
        while level:
            res.append([n.val for n in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]

        for i in range(len(res)):
            if i % 2 != 0:
                res[i].reverse()

        return res

