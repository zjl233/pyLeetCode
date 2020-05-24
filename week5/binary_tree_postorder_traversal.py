from typing import List

from utils.treenode import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.append(cur.left) if cur.left else None
            stack.append(cur.right) if cur.right else None
        res.reverse()
        return res

    # https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
    def postorderTraversalColor(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        stack = [root]
        while stack:
            cur = stack.pop()
            if isinstance(cur, TreeNode):
                stack.extend([cur.val, cur.right, cur.left])
            elif isinstance(cur, int):
                ans.append(cur)
        return ans
