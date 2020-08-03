# Definition for a Node.
from typing import Dict


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next: Node = next
        self.random = random


class Solution:
    def copyRandomListTouJi(self, head: 'Node') -> 'Node':
        if not head:
            return head

        d: Dict[Node, Node] = {}
        cur = head
        while cur:
            d[cur] = Node(cur.val)
            cur = cur.next

        for raw, cpy in d.items():
            if raw.next:
                cpy.next = d[raw.next]
            if raw.random:
                cpy.random = d[raw.random]

        return d[head]

    def copyRandomList(self, head: 'Node') -> 'Node':
        # 洗数据
        if not head:
            return head

        # 1. 在每个节点后面加上 node'
        # 2. 复制 node' 的 random（有 random 节点的才要复制）
        # 3. 把两个链表拆开

        # 第一步
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node

            cur = cur.next.next

        # 第二步
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next

            cur = cur.next.next

        # 第三步
        res = head.next

        cur = head
        while cur:
            new_cur = cur.next

            cur.next = cur.next.next
            new_cur.next = (new_cur.next.next if new_cur.next else None)

            cur = cur.next

        return res
