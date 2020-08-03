from utils.treenode import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        cur = root
        p = TreeNode(float('-inf'))  # predecessor
        while cur:
            if cur.left:  # 有左子树
                mr = cur.left
                while mr.right and mr.right is not cur:
                    mr = mr.right

                if not mr.right:  # 第一次来 cur，将 mr 的有指针连接到自己身上
                    mr.right = cur
                    cur = cur.left
                else:  # 第二次来cur, 将 mr. 右指针裁掉
                    mr.right = None

                    if p.val >= cur.val:
                        return False
                    p = cur

                    cur = cur.right

            else:  # 无左子树
                if p.val >= cur.val:
                    return False
                p = cur
                cur = cur.right

        return True
