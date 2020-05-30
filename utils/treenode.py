from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = x
        self.left = left
        self.right = right


def test_tree() -> TreeNode:
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    return node1
