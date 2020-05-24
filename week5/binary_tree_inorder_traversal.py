from typing import List

from utils.treenode import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        # 不用提前将 root 放入 stack
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                # 触底，转向，右子树
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res

    # https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
    def inorderTraversalColor(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        stack = [root]
        while stack:
            cur = stack.pop()
            if isinstance(cur, TreeNode):
                stack.extend([cur.right, cur.val, cur.left])
            elif isinstance(cur, int):
                ans.append(cur)
        return ans
