from collections import deque
from typing import List, Optional, Deque

from utils.treenode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res: List[List[int]] = []
        if not root:
            return res

        level = [root]
        while level:
            vals = [node.val for node in level]
            res.append(vals)

            level = [kid for n in level for kid in (n.left, n.right) if kid]  # 不将 空节点放入 level
            # level = [kid for n in level if n for kid in (n.left, n.right)]  # 因为之前空节点放入 level，所以这一次要判断一下，空节点.操作会报错
            # 上面放 val 的时候，也要判断一下

        return res

    def naiveLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        res: List[int] = []
        dq: Deque[Optional[TreeNode]] = deque([root])
        while dq:
            node = dq.popleft()
            if node:
                res.append(node.val)
                dq.append(node.left)
                dq.append(node.right)

        return res

