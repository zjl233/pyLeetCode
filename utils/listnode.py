from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, nxt: Optional['ListNode'] = None):
        self.val = val
        self.next = nxt

    def __repr__(self) -> str:
        return f'ListNode({self.val!r})'  # !r 为了区分 3 和 '3'


def entire_list(head: ListNode) -> str:
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next

    return '->'.join([str(v) for v in vals])


def build_list(vals: List[int]) -> ListNode:
    if not vals:
        raise ValueError('vals must be no-empty int list')

    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        node = ListNode(v)
        cur.next = node
        cur = cur.next
    return head
