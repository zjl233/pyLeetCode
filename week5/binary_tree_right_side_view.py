from typing import List

from utils.treenode import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res: List[int] = []
        level: List[TreeNode] = [root]
        while level:
            res.append(level[-1].val)
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res

    def rightSideViewDfs(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res: List[int] = []
        self.process(root, 0, res)
        return res

    def process(self, root: TreeNode, depth: int, res: List[int]) -> None:
        if not root:
            return

        if depth == len(res):
            res.append(root.val)

        self.process(root.right, depth + 1, res)
        self.process(root.left, depth + 1, res)
