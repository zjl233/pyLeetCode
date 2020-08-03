from typing import List, Optional

from utils.listnode import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:
        # 洗数据
        if not lists:
            return None
        # 虽然下面的递归可以处理特殊情况，但我还是这样做
        if len(lists) == 1:
            return lists[0]

        res = self.process(lists)
        return res

    def process(self, lists) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        lh = self.process(lists[:mid])
        rh = self.process(lists[mid:])
        res = self.mergeTwoLists(lh, rh)
        return res

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 洗数据
        if not l1 or not l2:
            return l1 or l2

        dummy = ListNode(-1)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next
