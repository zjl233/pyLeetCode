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

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head
        cur = head
        while cur:
            cpy = Node(cur.val, None, None)
            cpy.next = cur.next
            cur.next = cpy
            cur = cpy.next

        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        raw_list = head  # A->B->C
        cpy_list = head.next  # A'->B'->C'
        cpy_list_bak = head.next
        while raw_list:
            raw_list.next = raw_list.next.next
            cpy_list.next = cpy_list.next.next if cpy_list.next else None
            raw_list = raw_list.next
            cpy_list = cpy_list.next
        return cpy_list_bak

#