from utils.listnode import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        # 链表长度
        n = 1
        # 计算链表长度，并且将链表变成环
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        cur.next = head

        k = k % n
        # if k == 0:
        #     return head

        # 取从末尾开始的 (k + 1) th
        # 相当与从开头的 (n - k - 1) th
        cur = head
        for _ in range(n - k - 1):
            cur = cur.next

        res = cur.next
        cur.next = None
        return res
