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
            while root:
                stack.append(root)
                root = root.left
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

    def inorderTraversalMirrors(self, root: TreeNode) -> List[int]:
        vals: List[int] = []
        if not root:
            return vals

        cur = root
        while cur:
            if cur.left:  # 有左子树
                mr = cur.left
                while mr.right and mr.right is not cur:
                    mr = mr.right
                if not mr.right:  # 第一次来
                    mr.right = cur
                    cur = cur.left
                else:  # 第二次来
                    vals.append(cur.val)
                    mr.right = None
                    cur = cur.right
            else:  # 没有左子树
                vals.append(cur.val)
                cur = cur.right

        return vals

