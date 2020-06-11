from typing import List

from utils.treenode import TreeNode


def morris(root: TreeNode) -> List[int]:
    res: List[int] = []
    if not root:
        return res

    cur = root
    while cur:
        res.append(cur.val)  # morris 序
        if cur.left:
            # 有左子树

            # 找左子树的最右节点，注意叶节点的 right 已经连接到 cur 的情况
            mr = cur.left
            while mr.right and mr.right is not cur:
                mr = mr.right

            if mr.right is None:  # 第一次来 mr
                mr.right = cur
                cur = cur.left
            elif mr.right is cur:  # 第二次来 mr
                mr.right = None
                cur = cur.right
            else:  # 判断不应该跑到这里
                raise RuntimeError
        else:
            # 没有左子树
            cur = cur.right

    return res


def morris_pre(root: TreeNode) -> List[int]:
    res: List[int] = []
    if not root:
        return res

    cur = root
    while cur:
        if cur.left:
            # 有左子树

            # 找左子树的最右节点，注意叶节点的 right 已经连接到 cur 的情况
            mr = cur.left
            while mr.right and mr.right is not cur:
                mr = mr.right

            if mr.right is None:  # 第一次来 cur , 将 mr.right 连到 自己身上
                res.append(cur.val)
                mr.right = cur
                cur = cur.left
            elif mr.right is cur:  # 第二次来 cur，将 mr.right 拆掉
                mr.right = None
                cur = cur.right
            else:  # 判断不应该跑到这里
                raise RuntimeError
        else:
            # 没有左子树
            res.append(cur.val)
            cur = cur.right

    return res


def morris_in(root: TreeNode) -> List[int]:
    res: List[int] = []
    if not root:
        return res

    cur = root
    while cur:
        if cur.left:
            # 有左子树

            # 找左子树的最右节点，注意叶节点的 right 已经连接到 cur 的情况
            mr = cur.left
            while mr.right and mr.right is not cur:
                mr = mr.right

            if mr.right is None:  # 第一次来 cur , 将 mr.right 连到 自己身上
                mr.right = cur
                cur = cur.left
            elif mr.right is cur:  # 第二次回 cur，将 mr.right 拆掉
                res.append(cur.val)  # <<<
                mr.right = None
                cur = cur.right
            else:  # 判断不应该跑到这里
                raise RuntimeError
        else:
            # 没有左子树
            res.append(cur.val)  # <<<
            cur = cur.right

    return res

