from utils.listnode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 不用洗数据

        carry = 0
        dummy = ListNode(-1)  # res 之前的节点
        cur = dummy
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry != 0:
            cur.next = ListNode(carry)

        return dummy.next
