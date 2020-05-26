from collections import deque
from typing import Deque

from utils.treenode import TreeNode


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        # 策略变更，将空节点也放入 nxt
        d: Deque[TreeNode] = deque()
        d.append(root)
        miss_node = False
        while d:
            node = d.popleft()
            if not node and not miss_node:  # 之前没有出现过空节点
                miss_node = True
            elif node and miss_node:  # 之前出现过空节点，并且现在有碰到了数字节点
                return False
            elif node:  # 将空节点也放入 queue
                d.append(node.left)
                d.append(node.right)

        return True

#