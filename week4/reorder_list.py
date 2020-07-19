from utils.listnode import ListNode


class Solution:
    def reorderListExcellent(self, head):
        # 超神解法!!!!
        # https://leetcode.com/problems/reorder-list/discuss/44988/A-python-solution-O(n)-time-O(1)-space
        # @cmc
        if not head:
            return

        # find the mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next

        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        mid = self.get_mid(head)
        tail = self.reverse_list(mid)

        while tail != mid:
            head_next = head.next
            head.next = tail
            head = head_next

            tail_next = tail.next
            tail.next = head
            tail = tail_next

    def get_mid(self, head: ListNode) -> ListNode:
        # 至少有两个节点
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

