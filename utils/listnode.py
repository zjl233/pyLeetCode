from typing import Optional, List, Union


class ListNode:
    def __init__(self, val: int = 0, nxt: Optional['ListNode'] = None):
        self.val = val
        self.next = nxt

    def __repr__(self) -> str:
        return f'ListNode({self.val!r})'  # !r 为了区分 3 和 '3'

    def entire_list(self):
        vals = []
        cur = self
        while cur:
            vals.append(cur.val)
            cur = cur.next

        return '->'.join([str(v) for v in vals])


def entire_list(head: ListNode) -> str:
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next

    return '->'.join([str(v) for v in vals])


def build_list(vals: Union[List[int], str]) -> ListNode:
    if not vals:
        raise ValueError('vals must be no-empty int list')

    if isinstance(vals, str):
        "1->2->3"
        vals = [int(v) for v in vals.split("->")]

    dummy = ListNode(-1)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next
