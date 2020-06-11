from typing import NamedTuple

from utils.treenode import TreeNode


class Info(NamedTuple):
    lca: TreeNode = None
    count: int = 0


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        info = self.process(root, p, q)
        return info[0]

    def process(self, root, p, q) -> Info:
        if not root:
            return Info()

        l = self.process(root.left, p, q)
        r = self.process(root.right, p, q)

        count = l.count + r.count
        if root == p:
            count += 1
        if root == q:
            count += 1

        lca = None
        if count == 2:
            lca = root
        if l.lca is not None:
            lca = l.lca
        if r.lca is not None:
            lca = r.lca

        # lca = l.lca or r.lca or (root if count == 2 else None)

        return Info(lca, count)
