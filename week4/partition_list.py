from utils.listnode import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        lth, ltt = None, None
        eqh, eqt = None, None

        while head:
            if head.val < x:
                if not lth and not ltt:
                    lth = ltt = head
                elif lth and ltt:
                    ltt.next = head
                    ltt = ltt.next
            elif head.val >= x:
                if not eqh and not eqt:
                    eqh = eqt = head
                elif eqh and eqt:
                    eqt.next = head
                    eqt = eqt.next
            head = head.next
        if ltt:
            ltt.next = eqh

        if eqt:
            eqt.next = None

        return lth if lth else eqh

    def partition_dummy(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        lth = ltt = ListNode()
        geh = get = ListNode()

        while head:
            if head.val < x:
                ltt.next = head
                ltt = ltt.next
            elif head.val >= x:
                get.next = head
                get = get.next
            head = head.next

        get.next = None
        ltt.next = geh.next

        return lth.next

#