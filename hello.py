from typing import Optional

from utils.treenode import TreeNode


def build_tree() -> TreeNode:
    try:
        val, left, right = [int(s) for s in input().split()]
        root = TreeNode(val)

        if left != 0:
            root.left = build_tree()
        if right != 0:
            root.right = build_tree()

        return root
    except EOFError:
        print("建二叉树的时候出错了，不应当啊")


if __name__ == '__main__':
    res = build_tree()
    print(res)
