from typing import NamedTuple


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Info(NamedTuple):
    head: Node = None
    tail: Node = None


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        info = self.process(root)
        # 链接头尾
        # ...
        info.head.left = info.tail
        info.tail.right = info.head
        return info.head

    def process(self, root) -> Info:
        if not root:
            return Info()

        l = self.process(root.left)
        r = self.process(root.right)

        if l.tail:
            l.tail.right = root
        if r.head:
            r.head.left = root

        root.left = l.tail
        root.right = r.head

        head = l.head if l.head else root
        tail = r.tail if r.tail else root
        return Info(head, tail)

